from flask import Flask, request, jsonify, send_from_directory
import subprocess, re, json, tempfile, os
from pathlib import Path
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

def is_negative(s):
    return re.match(r'^no+\.?$', s.strip().lower()) is not None or s.strip() == ''

def get_answer_after(text, pattern):
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if not m: return None
    for line in text[m.end():].split('\n'):
        line = line.strip()
        if line: return line
    return None

def get_images_per_page(path):
    r = subprocess.run(["pdfimages", "-list", path], capture_output=True, text=True)
    pages = {}
    for line in r.stdout.split('\n'):
        m = re.match(r'\s*(\d+)\s+\d+\s+image\s+(\d+)\s+(\d+)', line)
        if not m: continue
        page = int(m.group(1))
        w, h = int(m.group(2)), int(m.group(3))
        if w < 400 or h < 400: continue
        pages[page] = pages.get(page, 0) + 1
    return pages

def parse_form(path, filename):
    r = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True)
    text = r.stdout
    v = {}

    m = re.search(r'Name:\s*([^\n]+)', text)
    v['mercaderista'] = m.group(1).strip().replace(' Email:', '') if m else ''

    m = re.search(r'CUSTOMER\s*\nName:\s*(.+?)(?:\nCode:)', text, re.DOTALL)
    v['punto_de_venta'] = ' '.join(m.group(1).split()) if m else ''

    m = re.search(r'City:\s*(.+)', text)
    v['ciudad'] = m.group(1).strip() if m else ''

    v['tipo'] = 'TRANSFERENCIA' if 'TRANSFERENCIA' in text else ('MERCADEO' if 'MERCADEO' in text else '')

    m = re.search(r'1\) FECHA\s*\n(\d{4}-\d{2}-\d{2})', text)
    v['fecha'] = m.group(1) if m else ''

    m = re.search(r'LABOR PRINCIPAL REALIZADA[^\n]*\n([^\n]+)', text)
    v['labor_realizada'] = m.group(1).strip().replace('?', 'O') if m else ''

    m = re.search(r'cual es el paso a seguir[^\n]*\n([^\n]+)', text)
    v['paso_a_seguir'] = m.group(1).strip() if m else ''

    v['cliente_cerrado'] = 'CLIENTE CERRADO' in text.upper()

    m = re.search(r'PROXIMA VISITA\s*\n(\d{4}-\d{2}-\d{2})', text)
    v['proxima_visita'] = m.group(1) if m else ''

    ans = get_answer_after(text, r'REFERENCIAS\s*\n')
    v['alerta_inventario'] = None if (ans is None or is_negative(ans)) else ans

    ans = get_answer_after(text, r'Ejemplo de respuesta[^\n]*\n')
    v['lenta_rotacion'] = None if (ans is None or is_negative(ans)) else ans

    imgs = get_images_per_page(path)
    p1 = imgs.get(1, 0)
    p2 = imgs.get(2, 0)

    if v['tipo'] == 'MERCADEO':
        v['tiene_exhibicion_edding'] = p1 >= 1
        v['tiene_exhibicion_maped'] = (p1 >= 4) or (p2 >= 1)
        v['tiene_pop'] = p2 >= 3
    elif v['tipo'] == 'TRANSFERENCIA':
        v['tiene_pop'] = p1 >= 2
        v['tiene_exhibicion_edding'] = p2 >= 1
        v['tiene_exhibicion_maped'] = p2 >= 3
    else:
        v['tiene_exhibicion_edding'] = None
        v['tiene_exhibicion_maped'] = None
        v['tiene_pop'] = False

    v['_filename'] = filename
    return v

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    files = request.files.getlist('pdfs')
    if not files:
        return jsonify({'error': 'No se recibieron archivos'}), 400

    results = []
    errors = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for f in files:
            if not f.filename.lower().endswith('.pdf'):
                continue
            fname = secure_filename(f.filename)
            fpath = os.path.join(tmpdir, fname)
            f.save(fpath)
            try:
                result = parse_form(fpath, fname)
                results.append(result)
            except Exception as e:
                errors.append({'archivo': fname, 'error': str(e)})

    return jsonify({'visitas': results, 'errores': errors})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
