<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Insitu Dashboard · Edding & Maped</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #f5f4f0;
  --surface: #ffffff;
  --border: #e2e0d8;
  --text: #1a1916;
  --text-2: #6b6860;
  --text-3: #a8a69e;
  --red: #c0392b;
  --red-bg: #fdf0ee;
  --red-border: #f5c6c0;
  --amber: #b45309;
  --amber-bg: #fffbeb;
  --amber-border: #fde68a;
  --green: #166534;
  --green-bg: #f0fdf4;
  --green-border: #bbf7d0;
  --blue: #1d4ed8;
  --blue-bg: #eff6ff;
  --blue-border: #bfdbfe;
  --accent: #1a1916;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }

header { background: var(--surface); border-bottom: 1px solid var(--border); padding: 0 2rem; display: flex; align-items: center; justify-content: space-between; height: 56px; }
.logo { font-family: 'DM Mono', monospace; font-size: 13px; font-weight: 500; letter-spacing: 0.05em; color: var(--text); }
.logo span { color: var(--text-3); }

main { max-width: 1200px; margin: 0 auto; padding: 2rem; }

.upload-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 3rem 2rem; text-align: center; }
.upload-zone { border: 1.5px dashed var(--border); border-radius: 8px; padding: 2.5rem; cursor: pointer; transition: border-color 0.15s, background 0.15s; }
.upload-zone:hover, .upload-zone.drag { border-color: var(--accent); background: var(--bg); }
.upload-icon { font-size: 32px; margin-bottom: 12px; }
.upload-title { font-size: 18px; font-weight: 500; margin-bottom: 6px; }
.upload-sub { font-size: 13px; color: var(--text-2); margin-bottom: 20px; }
.btn { display: inline-flex; align-items: center; gap: 6px; padding: 9px 18px; border-radius: 6px; font-size: 13px; font-weight: 500; cursor: pointer; border: 1px solid var(--border); background: var(--surface); color: var(--text); font-family: inherit; transition: background 0.12s; }
.btn:hover { background: var(--bg); }
.btn-primary { background: var(--accent); color: #fff; border-color: var(--accent); }
.btn-primary:hover { opacity: 0.88; }
.btn-primary:disabled { opacity: 0.4; cursor: not-allowed; }

.file-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 16px; justify-content: center; }
.chip { display: inline-flex; align-items: center; gap: 6px; background: var(--bg); border: 1px solid var(--border); border-radius: 99px; padding: 4px 10px; font-size: 12px; font-family: 'DM Mono', monospace; }
.chip-remove { cursor: pointer; color: var(--text-3); line-height: 1; font-size: 14px; }
.chip-remove:hover { color: var(--red); }

.action-row { display: flex; align-items: center; justify-content: center; gap: 12px; margin-top: 20px; }
.file-count { font-size: 13px; color: var(--text-2); }

.loading { display: flex; flex-direction: column; align-items: center; gap: 16px; padding: 3rem; }
.spinner { width: 36px; height: 36px; border: 2.5px solid var(--border); border-top-color: var(--accent); border-radius: 50%; animation: spin 0.7s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.loading-text { font-size: 14px; color: var(--text-2); }

#results { display: none; }

.metrics { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 10px; margin-bottom: 1.5rem; }
.metric { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 16px; }
.metric-label { font-size: 11px; color: var(--text-2); text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px; }
.metric-value { font-size: 28px; font-weight: 600; font-family: 'DM Mono', monospace; }
.metric-value.red { color: var(--red); }
.metric-value.amber { color: var(--amber); }

.alerts { margin-bottom: 1.5rem; }
.alert-item { background: var(--red-bg); border: 1px solid var(--red-border); border-radius: 8px; padding: 10px 14px; font-size: 13px; color: var(--red); margin-bottom: 6px; }
.alert-item strong { font-weight: 600; }

.panel { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }
.panel-header { display: flex; align-items: center; justify-content: space-between; padding: 1rem 1.25rem; border-bottom: 1px solid var(--border); }
.panel-title { font-size: 14px; font-weight: 500; }
.tabs { display: flex; gap: 2px; background: var(--bg); border-radius: 6px; padding: 3px; }
.tab { padding: 5px 14px; border-radius: 4px; font-size: 12px; font-weight: 500; cursor: pointer; color: var(--text-2); border: none; background: none; font-family: inherit; }
.tab.active { background: var(--surface); color: var(--text); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }

.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
th { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--border); font-size: 11px; font-weight: 500; color: var(--text-2); text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap; background: var(--bg); }
td { padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: #fafaf8; }

.badge { display: inline-block; padding: 2px 8px; border-radius: 99px; font-size: 11px; font-weight: 500; white-space: nowrap; }
.b-ok { background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); }
.b-no { background: var(--red-bg); color: var(--red); border: 1px solid var(--red-border); }
.b-warn { background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber-border); }
.b-info { background: var(--blue-bg); color: var(--blue); border: 1px solid var(--blue-border); }
.b-gray { background: var(--bg); color: var(--text-2); border: 1px solid var(--border); }
.na { color: var(--text-3); font-size: 11px; }

.tab-pane { display: none; }
.tab-pane.active { display: block; }

.merc-card { border-bottom: 1px solid var(--border); padding: 1.25rem; }
.merc-card:last-child { border-bottom: none; }
.merc-head { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
.avatar { width: 38px; height: 38px; border-radius: 50%; background: var(--bg); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; font-family: 'DM Mono', monospace; color: var(--text); flex-shrink: 0; }
.merc-name { font-weight: 500; font-size: 14px; }
.merc-sub { font-size: 12px; color: var(--text-2); }
.stats { display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 12px; }
.stat { font-size: 12px; color: var(--text-2); }
.stat strong { color: var(--text); font-weight: 500; }

.inner-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.inner-table th { background: var(--bg); padding: 6px 10px; font-size: 10px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-2); font-weight: 500; border-bottom: 1px solid var(--border); }
.inner-table td { padding: 7px 10px; border-bottom: 1px solid var(--border); }
.inner-table tr:last-child td { border-bottom: none; }

.top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.top-bar-left { font-size: 13px; color: var(--text-2); }

.error-item { background: var(--amber-bg); border: 1px solid var(--amber-border); border-radius: 8px; padding: 8px 12px; font-size: 12px; color: var(--amber); margin-bottom: 4px; font-family: 'DM Mono', monospace; }

@media (max-width: 640px) {
  main { padding: 1rem; }
  .metrics { grid-template-columns: repeat(2, 1fr); }
  header { padding: 0 1rem; }
}
</style>
</head>
<body>

<header>
  <div class="logo">INSITU <span>·</span> DASHBOARD</div>
  <div style="font-size:12px;color:var(--text-3)">Edding & Maped Colombia</div>
</header>

<main>
  <div id="upload-section">
    <div class="upload-card">
      <div class="upload-zone" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept=".pdf" multiple style="display:none">
        <div class="upload-icon">📄</div>
        <div class="upload-title">Sube los PDFs de Insitu Sales</div>
        <div class="upload-sub">Arrastra los archivos aquí o haz clic para seleccionarlos</div>
        <button class="btn" onclick="event.stopPropagation();document.getElementById('file-input').click()">Seleccionar archivos</button>
      </div>
      <div class="file-chips" id="file-chips"></div>
      <div class="action-row" id="action-row" style="display:none">
        <span class="file-count" id="file-count"></span>
        <button class="btn btn-primary" id="process-btn" onclick="processFiles()">Procesar formularios →</button>
      </div>
    </div>
  </div>

  <div id="loading-section" style="display:none">
    <div class="upload-card">
      <div class="loading">
        <div class="spinner"></div>
        <div class="loading-text" id="loading-text">Procesando formularios...</div>
      </div>
    </div>
  </div>

  <div id="results">
    <div class="top-bar">
      <div class="top-bar-left" id="lote-info"></div>
      <div style="display:flex;gap:8px">
        <button class="btn" onclick="exportCSV()">Exportar CSV</button>
        <button class="btn" onclick="resetApp()">Nuevo lote</button>
      </div>
    </div>

    <div class="metrics" id="metrics"></div>
    <div class="alerts" id="alerts"></div>
    <div id="errors-section"></div>

    <div class="panel">
      <div class="panel-header">
        <span class="panel-title" id="panel-title">Visitas</span>
        <div class="tabs">
          <button class="tab active" onclick="switchTab('tabla')">Tabla de visitas</button>
          <button class="tab" onclick="switchTab('mercaderista')">Por mercaderista</button>
        </div>
      </div>

      <div class="tab-pane active" id="tab-tabla">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Mercaderista</th><th>Punto de venta</th><th>Ciudad</th><th>Tipo</th>
              <th>Labor / Acción</th><th>Próx. visita</th>
              <th>Edding</th><th>Maped</th><th>POP</th><th>Alerta</th>
            </tr></thead>
            <tbody id="tbody"></tbody>
          </table>
        </div>
      </div>

      <div class="tab-pane" id="tab-mercaderista">
        <div id="merc-cards"></div>
      </div>
    </div>
  </div>
</main>

<script>
let uploadedFiles = [];
let DATA = [];

const fileInput = document.getElementById('file-input');
const dropZone = document.getElementById('drop-zone');

fileInput.addEventListener('change', e => handleFiles([...e.target.files]));
dropZone.addEventListener('dragover', e => { e.preventDefault(); dropZone.classList.add('drag'); });
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag'));
dropZone.addEventListener('drop', e => { e.preventDefault(); dropZone.classList.remove('drag'); handleFiles([...e.dataTransfer.files]); });

function handleFiles(files) {
  files.filter(f => f.name.endsWith('.pdf')).forEach(f => {
    if (!uploadedFiles.find(x => x.name === f.name)) uploadedFiles.push(f);
  });
  renderChips();
}

function renderChips() {
  document.getElementById('file-chips').innerHTML = uploadedFiles.map((f,i) =>
    `<span class="chip">${f.name}<span class="chip-remove" onclick="removeFile(${i})">×</span></span>`
  ).join('');
  const show = uploadedFiles.length > 0;
  document.getElementById('action-row').style.display = show ? 'flex' : 'none';
  document.getElementById('file-count').textContent = `${uploadedFiles.length} archivo${uploadedFiles.length>1?'s':''}`;
}

function removeFile(i) { uploadedFiles.splice(i,1); renderChips(); }

async function processFiles() {
  document.getElementById('upload-section').style.display = 'none';
  document.getElementById('loading-section').style.display = 'block';

  const msgs = ['Extrayendo texto de PDFs...','Detectando campos...','Contando imágenes por página...','Consolidando resultados...'];
  let mi = 0;
  const lt = document.getElementById('loading-text');
  const interval = setInterval(() => { mi=(mi+1)%msgs.length; lt.textContent=msgs[mi]; }, 2000);

  const fd = new FormData();
  uploadedFiles.forEach(f => fd.append('pdfs', f));

  try {
    const res = await fetch('/procesar', { method: 'POST', body: fd });
    const json = await res.json();
    DATA = json.visitas || [];
    clearInterval(interval);
    document.getElementById('loading-section').style.display = 'none';
    renderResults(json.errores || []);
    document.getElementById('results').style.display = 'block';
  } catch(e) {
    clearInterval(interval);
    lt.textContent = 'Error al procesar. Intenta de nuevo.';
  }
}

function eb(val) {
  if (val === null) return '<span class="na">—</span>';
  return val ? '<span class="badge b-ok">Sí</span>' : '<span class="badge b-no">No</span>';
}

function alertCell(v) {
  let p = [];
  if (v.cliente_cerrado) p.push('<span class="badge b-no">Cerrado</span>');
  if (v.alerta_inventario) p.push(`<div style="font-size:11px;font-style:italic;color:var(--amber);margin-top:3px">"${v.alerta_inventario}"</div>`);
  if (v.lenta_rotacion) p.push(`<div style="font-size:11px;font-style:italic;color:var(--amber);margin-top:3px">Lenta: "${v.lenta_rotacion}"</div>`);
  return p.length ? p.join('') : '<span class="na">—</span>';
}

function alertSum(v) {
  let b = [];
  if (v.cliente_cerrado) b.push('<span class="badge b-no">Cerrado</span>');
  if (v.alerta_inventario) b.push('<span class="badge b-warn">Inventario</span>');
  if (v.lenta_rotacion) b.push('<span class="badge b-warn">Lenta rot.</span>');
  return b.length ? b.join(' ') : '<span class="na">—</span>';
}

function renderResults(errors) {
  const total = DATA.length;
  const mercs = new Set(DATA.map(v=>v.mercaderista)).size;
  const cerrados = DATA.filter(v=>v.cliente_cerrado).length;
  const alertas = DATA.filter(v=>v.alerta_inventario||v.lenta_rotacion).length;
  const fechas = [...new Set(DATA.map(v=>v.fecha).filter(Boolean))].sort();
  const fechaStr = fechas.length===1 ? fechas[0] : fechas.length>1 ? `${fechas[0]} – ${fechas[fechas.length-1]}` : '';

  document.getElementById('lote-info').textContent = `${total} formularios procesados${fechaStr?' · '+fechaStr:''}`;
  document.getElementById('metrics').innerHTML = `
    <div class="metric"><div class="metric-label">Total visitas</div><div class="metric-value">${total}</div></div>
    <div class="metric"><div class="metric-label">Mercaderistas</div><div class="metric-value">${mercs}</div></div>
    <div class="metric"><div class="metric-label">Clientes cerrados</div><div class="metric-value ${cerrados>0?'red':''}">${cerrados}</div></div>
    <div class="metric"><div class="metric-label">Alertas inventario</div><div class="metric-value ${alertas>0?'amber':''}">${alertas}</div></div>
  `;

  const alertVisits = DATA.filter(v=>v.cliente_cerrado||v.alerta_inventario||v.lenta_rotacion);
  document.getElementById('alerts').innerHTML = alertVisits.length
    ? alertVisits.map(v => {
        let msgs=[];
        if(v.cliente_cerrado) msgs.push('Cliente cerrado');
        if(v.alerta_inventario) msgs.push(`Inventario: "${v.alerta_inventario}"`);
        if(v.lenta_rotacion) msgs.push(`Lenta rotación: "${v.lenta_rotacion}"`);
        return `<div class="alert-item"><strong>${v.mercaderista}</strong> — ${v.punto_de_venta.slice(0,50)} · ${msgs.join(' · ')}</div>`;
      }).join('') : '';

  if (errors.length) {
    document.getElementById('errors-section').innerHTML = errors.map(e =>
      `<div class="error-item">⚠ ${e.archivo}: ${e.error}</div>`).join('');
  }

  document.getElementById('tbody').innerHTML = DATA.map(v=>`<tr>
    <td style="white-space:nowrap;font-weight:500">${v.mercaderista}</td>
    <td style="font-size:12px;max-width:160px">${v.punto_de_venta}</td>
    <td>${v.ciudad}</td>
    <td><span class="badge ${v.tipo==='MERCADEO'?'b-info':'b-gray'}">${v.tipo||'—'}</span></td>
    <td style="font-size:12px;max-width:130px">${v.labor_realizada||v.paso_a_seguir||'—'}</td>
    <td style="font-size:12px;white-space:nowrap">${v.proxima_visita||'—'}</td>
    <td>${eb(v.tiene_exhibicion_edding)}</td>
    <td>${eb(v.tiene_exhibicion_maped)}</td>
    <td>${eb(v.tiene_pop)}</td>
    <td>${alertCell(v)}</td>
  </tr>`).join('');

  const byMerc = {};
  DATA.forEach(v=>{ const k=v.mercaderista||'Desconocido'; if(!byMerc[k]) byMerc[k]=[]; byMerc[k].push(v); });

  document.getElementById('merc-cards').innerHTML = Object.entries(byMerc).map(([name,visits])=>{
    const initials = name.split(/[\s,]+/).filter(Boolean).slice(0,2).map(w=>w[0]).join('').toUpperCase();
    const cerradosM = visits.filter(v=>v.cliente_cerrado).length;
    const alertasM = visits.filter(v=>v.alerta_inventario||v.lenta_rotacion).length;
    const totalAl = cerradosM+alertasM;
    const ciudades = [...new Set(visits.map(v=>v.ciudad))].join(', ');
    const proximas = visits.filter(v=>v.proxima_visita).map(v=>v.proxima_visita).sort();
    const sinEdding = visits.filter(v=>v.tiene_exhibicion_edding===false).length;
    const sinMaped = visits.filter(v=>v.tiene_exhibicion_maped===false).length;
    const sinPop = visits.filter(v=>v.tiene_pop===false).length;
    return `<div class="merc-card">
      <div class="merc-head">
        <div class="avatar">${initials}</div>
        <div style="flex:1"><div class="merc-name">${name}</div><div class="merc-sub">${ciudades}</div></div>
        ${totalAl>0?`<span class="badge b-no">${totalAl} alerta${totalAl>1?'s':''}</span>`:`<span class="badge b-ok">Sin alertas</span>`}
      </div>
      <div class="stats">
        <div class="stat">Visitas: <strong>${visits.length}</strong></div>
        <div class="stat">Cerrados: <strong>${cerradosM}</strong></div>
        <div class="stat">Sin exhib. Edding: <strong>${sinEdding}</strong></div>
        <div class="stat">Sin exhib. Maped: <strong>${sinMaped}</strong></div>
        <div class="stat">Sin POP: <strong>${sinPop}</strong></div>
        ${proximas.length?`<div class="stat">Próxima visita: <strong>${proximas[0]}</strong></div>`:''}
      </div>
      <div style="overflow-x:auto">
      <table class="inner-table">
        <thead><tr><th>Punto de venta</th><th>Ciudad</th><th>Tipo</th><th>Fecha</th><th>Labor/Acción</th><th>Próx. visita</th><th>Edding</th><th>Maped</th><th>POP</th><th>Alerta</th></tr></thead>
        <tbody>${visits.map(v=>`<tr>
          <td>${v.punto_de_venta.slice(0,30)}${v.punto_de_venta.length>30?'…':''}</td>
          <td>${v.ciudad}</td>
          <td><span class="badge ${v.tipo==='MERCADEO'?'b-info':'b-gray'}" style="font-size:10px">${v.tipo}</span></td>
          <td style="white-space:nowrap">${v.fecha}</td>
          <td style="max-width:120px;font-size:11px">${v.labor_realizada||v.paso_a_seguir||'—'}</td>
          <td style="white-space:nowrap">${v.proxima_visita||'—'}</td>
          <td>${eb(v.tiene_exhibicion_edding)}</td>
          <td>${eb(v.tiene_exhibicion_maped)}</td>
          <td>${eb(v.tiene_pop)}</td>
          <td>${alertSum(v)}</td>
        </tr>`).join('')}</tbody>
      </table></div>
    </div>`;
  }).join('');
}

function switchTab(name) {
  document.querySelectorAll('.tab').forEach((t,i)=>t.classList.toggle('active',['tabla','mercaderista'][i]===name));
  document.querySelectorAll('.tab-pane').forEach(t=>t.classList.remove('active'));
  document.getElementById('tab-'+name).classList.add('active');
}

function exportCSV() {
  const h = ['Mercaderista','Punto de venta','Ciudad','Tipo','Fecha','Labor/Acción','Próxima visita','Exhib. Edding','Exhib. Maped','POP','Cliente cerrado','Alerta inventario','Lenta rotación','Archivo'];
  const rows = DATA.map(v=>[
    v.mercaderista,v.punto_de_venta,v.ciudad,v.tipo,v.fecha,
    v.labor_realizada||v.paso_a_seguir,v.proxima_visita,
    v.tiene_exhibicion_edding===null?'—':v.tiene_exhibicion_edding?'Sí':'No',
    v.tiene_exhibicion_maped===null?'—':v.tiene_exhibicion_maped?'Sí':'No',
    v.tiene_pop===null?'—':v.tiene_pop?'Sí':'No',
    v.cliente_cerrado?'Sí':'No',v.alerta_inventario||'',v.lenta_rotacion||'',v._filename
  ].map(c=>`"${String(c||'').replace(/"/g,'""')}"`));
  const csv = [h.map(x=>`"${x}"`).join(','),...rows.map(r=>r.join(','))].join('\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob(['\ufeff'+csv],{type:'text/csv;charset=utf-8'}));
  a.download = `visitas_${new Date().toISOString().slice(0,10)}.csv`;
  a.click();
}

function resetApp() {
  uploadedFiles=[]; DATA=[];
  document.getElementById('file-input').value='';
  document.getElementById('file-chips').innerHTML='';
  document.getElementById('action-row').style.display='none';
  document.getElementById('results').style.display='none';
  document.getElementById('errors-section').innerHTML='';
  document.getElementById('upload-section').style.display='block';
}
</script>
</body>
</html>
