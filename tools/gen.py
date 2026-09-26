#!/usr/bin/env python3
"""Genera las 7 landings de producto en ../products/ a partir de los datos de este archivo.
Uso: python3 tools/gen.py  (desde ~/Documents/Exowise-web). Despues: python3 tools/update_sitemap.py"""
import json, html
import os
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','products')+os.sep
P=[
 dict(slug='exoestate',name='ExoEstate',tint='#f3e3d3',
  tag=('Real estate GTM','GTM inmobiliario'),
  title=('Premium leads, under control.','Leads premium, bajo control.'),
  lead=('Go-to-market and lead management for premium real estate: attract high-value buyers, route every lead by role and never lose track of a contact.','Go-to-market y gestión de leads para bienes raíces premium: atraé compradores de alto valor, asigná cada lead por rol y nunca pierdas el control de un contacto.'),
  feats=[('Premium lead capture','Captura de leads premium','Campaigns and landing pages per development or property, feeding a single qualified pipeline.','Campañas y landings por desarrollo o propiedad que alimentan un único pipeline calificado.'),
   ('Role-based access','Acceso por roles','Director, sales manager, broker and partner roles: each one sees only the contacts they own or supervise.','Roles de director, gerente comercial, corredor y socio: cada uno ve solo los contactos que tiene asignados o supervisa.'),
   ('No contact leaks','Sin fuga de contactos','Contact data is protected by role; exports and hand-offs are logged so the relationship stays with the company.','Los datos de contacto se protegen por rol; exportaciones y traspasos quedan registrados para que la relación quede en la empresa.'),
   ('Assignment & follow-up','Asignación y seguimiento','Automatic lead routing, reminders and SLAs so no premium buyer waits.','Asignación automática de leads, recordatorios y tiempos de respuesta para que ningún comprador premium espere.'),
   ('GTM plan per project','Plan GTM por proyecto','Positioning, pricing, channels and launch plan for each development, with an AI assistant.','Posicionamiento, precios, canales y plan de lanzamiento para cada desarrollo, con asistente de IA.'),
   ('Pipeline analytics','Analítica del pipeline','Leads by source, stage and broker, conversion and time to close.','Leads por origen, etapa y corredor, conversión y tiempo de cierre.')],
  steps=[('Set up your projects','Cargá tus proyectos','Developments, units, prices and team roles.','Desarrollos, unidades, precios y roles del equipo.'),('Launch campaigns','Lanzá campañas','Capture and qualify premium leads.','Captá y calificá leads premium.'),('Close with control','Cerrá con control','Every contact tracked by role until the sale.','Cada contacto seguido por rol hasta la venta.')],
  uses=[('Luxury developers','Desarrolladores de alta gama'),('Premium real estate agencies','Inmobiliarias premium'),('Broker networks','Redes de corredores'),('International buyers programs','Programas para compradores internacionales')]),
 dict(slug='track-monitor',name='Track Monitor',tint='#fbe3c8',
  tag=('Fleet & parking','Flotas y playas'),
  title=('Know where every vehicle is — and what it cost.','Sabé dónde está cada vehículo, y cuánto costó.'),
  lead=('Real-time vehicle tracking and parking-lot control from a single web console, with trips, stops, access tags, rates and billing in one place.','Seguimiento de vehículos en tiempo real y control de playas de estacionamiento desde una sola consola web: recorridos, paradas, TAGs, tarifas y facturación en un mismo lugar.'),
  feats=[('Live map','Mapa en vivo','Live GPS positions and trip history drawn on the map, each vehicle with its own fixed color.','Posiciones GPS en vivo y recorridos sobre el mapa, cada vehículo con su color fijo.'),
   ('Smart stops','Paradas inteligentes','Automatic stop detection with arrival, departure, duration and “it’s here now”.','Detección automática de paradas con llegada, salida, duración y «está aquí ahora».'),
   ('Parking control','Control de playa','Plates, access tags, rates and contracts, with a simplified screen for the gate operator.','Matrículas, TAGs de acceso, tarifas y contratos, con una pantalla simple para el operador de la playa.'),
   ('Billing','Facturación','Contracts and billing linked to real usage, with exports to Excel.','Contratos y facturación ligados al uso real, con exportación a Excel.'),
   ('Any device','Cualquier dispositivo','Android tracking app over HTTPS or GPS hardware devices reporting every 15 seconds.','App Android de rastreo por HTTPS o dispositivos GPS que reportan cada 15 segundos.'),
   ('Works anywhere','Funciona en todo el mundo','Decimal coordinates worldwide, trips split automatically between separate journeys.','Coordenadas decimales en cualquier punto del planeta; los viajes se separan solos.')],
  steps=[('Install the tracker','Instalá el rastreador','Android app or GPS device on each vehicle.','App Android o equipo GPS en cada vehículo.'),('Register your fleet','Cargá tu flota','Plates, models, tags and rates.','Matrículas, modelos, TAGs y tarifas.'),('Monitor and bill','Controlá y facturá','Follow trips, stops and usage from the console.','Seguí recorridos, paradas y uso desde la consola.')],
  uses=[('Logistics & delivery fleets','Flotas de logística y reparto'),('Parking lots & garages','Playas de estacionamiento y garajes'),('Field service teams','Equipos de servicio en campo'),('Rental & corporate vehicles','Vehículos de alquiler y corporativos')]),
 dict(slug='ai-call-center',name=('AI Call Center','Call Center con IA'),tint='#efe1fb',
  tag=('Voice AI','IA de voz'),
  title=('A call center that never sleeps.','Un call center que nunca duerme.'),
  lead=('Conversational voice agents that call, answer, qualify and hand over leads 24/7 — outbound campaigns, inbound reception and SMS in one platform.','Agentes de voz conversacionales que llaman, atienden, califican y entregan leads 24/7: campañas salientes, recepción entrante y SMS en una sola plataforma.'),
  feats=[('Outbound campaigns','Campañas salientes','Sales and collections campaigns: paste your contacts, start, and the agents call with retries and schedules.','Campañas de ventas y cobranzas: pegás los contactos, iniciás, y los agentes llaman con reintentos y horarios.'),
   ('Virtual receptionist','Recepcionista virtual','Answers inbound calls, listens first, records claims and requests, and routes them to an inbox.','Atiende las llamadas entrantes, escucha primero, registra reclamos y solicitudes y los deja en una bandeja.'),
   ('SMS campaigns','Campañas SMS','Personalized texts with a one-tap confirmation link that turns into a lead automatically.','Mensajes personalizados con un link de confirmación en un toque que se convierte solo en lead.'),
   ('Lead delivery','Entrega de leads','Every accepted offer or payment promise becomes a lead, delivered to your partners.','Cada oferta aceptada o compromiso de pago se vuelve un lead y se entrega a tus socios.'),
   ('Your own lines','Tus propias líneas','Works with GSM gateways over SIP trunk: inbound and outbound on the same lines.','Funciona con gateways GSM por SIP trunk: entrante y saliente por las mismas líneas.'),
   ('Live dashboards','Tableros en vivo','Calls, conversions, confirmations and costs per campaign and per hour.','Llamadas, conversiones, confirmaciones y costos por campaña y por hora.')],
  steps=[('Configure your agents','Configurá tus agentes','Voice, script and what data to collect.','Voz, guion y qué datos recolectar.'),('Load a campaign','Cargá una campaña','Contacts, schedule and pace.','Contactos, horario y ritmo.'),('Get qualified leads','Recibí leads calificados','Results, summaries and leads ready to deliver.','Resultados, resúmenes y leads listos para entregar.')],
  uses=[('Consumer lending','Préstamos al consumo'),('Collections','Cobranzas'),('Customer service & claims','Atención al cliente y reclamos'),('Lead qualification','Calificación de leads')]),
 dict(slug='exovision',name='ExoVision',tint='#dfe5fd',
  tag=('Computer vision','Visión artificial'),
  title=('Your cameras, now they understand.','Tus cámaras, ahora entienden.'),
  lead=('On-premise video intelligence that recognizes faces, license plates and objects in real time — without a single image leaving your site.','Inteligencia de video en tus instalaciones que reconoce rostros, matrículas y objetos en tiempo real, sin que ninguna imagen salga de tu sitio.'),
  feats=[('Face recognition','Reconocimiento facial','Detects, aligns and matches faces against your own registry of people.','Detecta, alinea y compara rostros contra tu propio padrón de personas.'),
   ('Plate reading','Lectura de matrículas','Local plate detection and OCR, confirmed by several matching reads.','Detección y OCR de matrículas en local, confirmada por varias lecturas coincidentes.'),
   ('Object detection','Detección de objetos','People, vehicles, animals and 80 object classes — name new ones and they become known.','Personas, vehículos, animales y 80 clases de objetos; nombrás los nuevos y pasan a conocidos.'),
   ('Clear alerts','Alertas claras','Green: authorized. Amber: known, not authorized. Red: unknown.','Verde: autorizado. Ámbar: conocido sin autorización. Rojo: desconocido.'),
   ('Any camera','Cualquier cámara','Hikvision and any ONVIF/RTSP camera, plus USB and local capture devices.','Hikvision y cualquier cámara ONVIF/RTSP, además de USB y capturadoras locales.'),
   ('Open API','API abierta','JSON API to integrate with access control, gates and other systems.','API JSON para integrar con control de acceso, portones y otros sistemas.')],
  steps=[('Connect your cameras','Conectá tus cámaras','Add IP or USB cameras from the web panel.','Agregá cámaras IP o USB desde el panel web.'),('Register people & vehicles','Cargá personas y vehículos','Photos and plates, authorized or not.','Fotos y matrículas, autorizados o no.'),('Watch & get alerts','Mirá y recibí alertas','Live video with boxes and a searchable history.','Video en vivo con cuadros e historial con búsqueda.')],
  uses=[('Garages & gated communities','Garajes y barrios cerrados'),('Corporate access control','Control de acceso corporativo'),('Parking lots','Playas de estacionamiento'),('Warehouses & industrial sites','Depósitos y plantas industriales')]),
 dict(slug='gtm-creator',name='GTM Creator',tint='#f5e6dc',
  tag=('Go-to-market','Go-to-market'),
  title=('From idea to launch plan, with AI at your side.','De la idea al plan de lanzamiento, con IA a tu lado.'),
  lead=('Build a complete go-to-market plan for any product, guided by an AI assistant that fills it in with you and exports it ready to share.','Armá un plan completo de salida al mercado para cualquier producto, guiado por un asistente de IA que lo completa con vos y lo exporta listo para compartir.'),
  feats=[('Structured plan','Plan estructurado','Summary, ICP, pricing, competition, plan, metrics, risks, pending items and quote checklist.','Resumen, ICP, precios, competencia, plan, métricas, riesgos, pendientes y checklist de cotización.'),
   ('Embedded AI assistant','Asistente de IA integrado','Guides each section and writes into the forms — its edits are highlighted so you can review them.','Guía cada sección y escribe en los formularios; lo que escribe queda resaltado para que lo revises.'),
   ('Excel in and out','Excel de ida y vuelta','Export to .xlsx with a ready-to-share format, or import an existing plan.','Exportá a .xlsx con formato listo para compartir, o importá un plan existente.'),
   ('Autosave','Guardado automático','Every change is saved as you go.','Cada cambio se guarda solo.'),
   ('Multi-user','Multiusuario','Each user sees only their own plans.','Cada usuario ve solo sus propios planes.'),
   ('AI-ready','Listo para IA','Exposes an MCP connector so AI assistants can work on your plans.','Expone un conector MCP para que los asistentes de IA trabajen sobre tus planes.')],
  steps=[('Create a GTM','Creá un GTM','Start from scratch or import your Excel.','Empezá de cero o importá tu Excel.'),('Complete it with AI','Completalo con IA','The assistant proposes and you decide.','El asistente propone y vos decidís.'),('Share it','Compartilo','Export and send to your team.','Exportá y mandalo a tu equipo.')],
  uses=[('Product launches','Lanzamientos de producto'),('Software & SaaS vendors','Proveedores de software y SaaS'),('Channel partners','Socios de canal'),('Sales & pricing strategy','Estrategia comercial y de precios')]),
 dict(slug='opencti-voice-agent',name='Exo OpenCTI Voice Agent',tint='#e3f1e8',
  tag=('Voice & vision agent','Agente de voz y visión'),
  title=('An agent that sees, listens and tells you.','Un agente que ve, escucha y te avisa.'),
  lead=('An AI agent that watches and listens through your cameras and microphones, understands what is happening and alerts you — fully on-premise, with no per-use cost.','Un agente de IA que mira y escucha a través de tus cámaras y micrófonos, entiende lo que pasa y te avisa: todo local, sin costo por uso.'),
  feats=[('Tiered detection','Detección por niveles','Cheap filters first, expensive models only on confirmed events: motion, then people and sound, then vision and speech models.','Primero filtros baratos, modelos caros solo en eventos confirmados: movimiento, luego personas y sonido, luego visión y voz.'),
   ('Two senses together','Dos sentidos juntos','Sound wakes the camera and what the camera sees asks to listen: every alert has both halves.','El sonido despierta la cámara y lo que ve la cámara pide escuchar: cada aviso trae las dos mitades.'),
   ('Speech transcription','Transcripción de voz','Transcribes what is said, locally, in seconds.','Transcribe lo que se habla, en local, en segundos.'),
   ('Mobile alerts','Avisos al celular','Instant push notifications with what was heard and what is seen.','Notificaciones inmediatas con lo que se oyó y lo que se ve.'),
   ('Ask in plain language','Preguntale en lenguaje natural','Via AI assistants (MCP): “is anyone there?”, “what was said?”.','Desde asistentes de IA (MCP): «¿hay alguien?», «¿qué dijeron?».'),
   ('Private by design','Privado por diseño','Models run on your hardware. No images or audio leave the building, no API keys required.','Los modelos corren en tu equipo. Ni imagen ni audio salen del lugar, sin claves de API.')],
  steps=[('Connect camera & mic','Conectá cámara y micrófono','Any standard webcam or IP camera.','Cualquier webcam estándar o cámara IP.'),('Tune the thresholds','Ajustá los umbrales','See live, measured numbers as you adjust.','Mirá números medidos en vivo mientras ajustás.'),('Get alerts & ask','Recibí avisos y preguntá','On your phone or through your AI assistant.','En tu celular o a través de tu asistente de IA.')],
  uses=[('Homes & small offices','Casas y oficinas pequeñas'),('After-hours monitoring','Monitoreo fuera de horario'),('Remote sites','Sitios remotos'),('AI assistants that need eyes and ears','Asistentes de IA que necesitan ojos y oídos')]),
 dict(slug='exoagi-agent',name='ExoAGI Agent',tint='#fbe3c8',
  tag=('AI assistant','Asistente de IA'),
  title=('The AI colleague that joins the meeting.','La colega de IA que entra a la reunión.'),
  lead=('A voice AI assistant with a 3D avatar that joins your meetings, remembers your company knowledge and powers other AI systems as a reasoning engine.','Un asistente de IA por voz con avatar 3D que participa en tus reuniones, recuerda el conocimiento de tu empresa y potencia a otros sistemas de IA como motor de razonamiento.'),
  feats=[('Real-time voice','Voz en tiempo real','Natural conversation by voice or chat, with local or cloud models you choose.','Conversación natural por voz o chat, con modelos locales o en la nube a elección.'),
   ('3D avatar','Avatar 3D','Lip-synced 3D avatar that also works as her camera in video calls.','Avatar 3D con sincronía labial que también funciona como su cámara en videollamadas.'),
   ('Meeting presence','Presencia en reuniones','Joins Microsoft Teams, listens, answers when called, follows commands and keeps minutes.','Entra a Microsoft Teams, escucha, responde cuando la nombran, obedece órdenes y lleva la minuta.'),
   ('Company memory','Memoria de la empresa','Knowledge base over your own documents (PDF, Word, images, text) plus web research.','Base de conocimiento sobre tus documentos (PDF, Word, imágenes, texto) más investigación en la web.'),
   ('Reasoning engine for other AIs','Motor de razonamiento para otras IA','MCP server with channels per domain: your systems and assistants like Claude use her as their brain.','Servidor MCP con canales por rubro: tus sistemas y asistentes como Claude la usan como cerebro.'),
   ('Secure access','Acceso seguro','Login with admin key or Google, rate limiting, revocable tokens and OAuth 2.1.','Ingreso con clave o Google, límite de intentos, tokens revocables y OAuth 2.1.')],
  steps=[('Feed her knowledge','Dale conocimiento','Upload documents and let her research.','Subí documentos y dejala investigar.'),('Invite her','Invitala','To your meetings or as a connector for your AI tools.','A tus reuniones o como conector de tus herramientas de IA.'),('Work together','Trabajen juntos','Ask, delegate and keep the minutes.','Preguntá, delegá y guardá la minuta.')],
  uses=[('Executive & team assistant','Asistente ejecutiva y de equipo'),('Meeting minutes & follow-up','Minutas y seguimiento de reuniones'),('Domain expert for your systems','Experta de dominio para tus sistemas'),('Reasoning layer for AI products','Capa de razonamiento para productos de IA')]),
]
def nm(p):
    return p['name'] if isinstance(p['name'],tuple) else (p['name'],p['name'])
def LD(p,en):
    import json
    u="https://exowise.ai/products/"+p['slug']+".html"
    d={"@context":"https://schema.org","@graph":[
     {"@type":"SoftwareApplication","name":en,"url":u,"description":p['lead'][0],"applicationCategory":"BusinessApplication","operatingSystem":"Web","image":"https://exowise.ai/assets/og-image.png",
      "featureList":[f[0] for f in p['feats']]+["MCP connector for AI agents","Integration APIs for CRM, ERP and WMS"],
      "publisher":{"@type":"Organization","name":"Exowise","url":"https://exowise.ai/","email":"info@exowise.ai","logo":"https://exowise.ai/assets/logo-512.png"}},
     {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Exowise","item":"https://exowise.ai/"},{"@type":"ListItem","position":2,"name":"Products","item":"https://exowise.ai/#products"},{"@type":"ListItem","position":3,"name":en,"item":u}]}]}
    return json.dumps(d,ensure_ascii=False).replace("</","<\\/")

LOGO='<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M32 6a26 26 0 1 0 26 26" fill="none" stroke="#141414" stroke-width="5" stroke-linecap="round"/><path d="M32 6a26 26 0 0 1 26 26" fill="none" stroke="#F0A04B" stroke-width="5" stroke-linecap="round"/><circle cx="32" cy="32" r="7" fill="#F0A04B"/></svg>'
FAV="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath d='M32 6a26 26 0 1 0 26 26' fill='none' stroke='%23141414' stroke-width='6' stroke-linecap='round'/%3E%3Cpath d='M32 6a26 26 0 0 1 26 26' fill='none' stroke='%23F0A04B' stroke-width='6' stroke-linecap='round'/%3E%3Ccircle cx='32' cy='32' r='7' fill='%23F0A04B'/%3E%3C/svg%3E"
CSS=open(os.path.join(HERE,'prod.css'),encoding='utf-8').read()
for p in P:
    en,es=nm(p); E=html.escape
    ES={}
    def t(key,a,b):
        ES[key]=b; return f'<span data-i18n="{key}">{E(a)}</span>'
    feats=''.join(f'<div class="f reveal"><i></i><h3>{t(f"f{i}t",a,b)}</h3><p>{t(f"f{i}p",c,d)}</p></div>' for i,(a,b,c,d) in enumerate(p['feats']))
    steps=''.join(f'<div class="s reveal"><span>0{i+1}</span><h4>{t(f"s{i}t",a,b)}</h4><p>{t(f"s{i}p",c,d)}</p></div>' for i,(a,b,c,d) in enumerate(p['steps']))
    uses=''.join(f'<li>{t(f"u{i}",a,b)}</li>' for i,(a,b) in enumerate(p['uses']))
    ES['name']=es; ES['nav.back']='← Todos los productos'; ES['nav.cta']='Pedí una demo'
    ES['feat.eyebrow']='Qué hace'; ES['feat.title']='Todo lo que necesitás, nada que sobre.'
    ES['how.eyebrow']='Cómo funciona'; ES['use.eyebrow']='Para quién es'; ES['use.title']='Pensado para'
    ES['ct.title']=f'¿Querés ver {es} en acción?'; ES['ct.sub']='Contanos tu caso y armamos una demo con tus datos.'
    ES['ct.cta']='Pedí una demo →'; ES['ct.more']='Ver otros productos'; ES['ft.rights']='Todos los derechos reservados.'
    subject=f'Exowise%20-%20Demo%20{en.replace(" ","%20")}'
    page=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(en)} — Exowise</title>
<meta name="description" content="{E(p['lead'][0])}">
<meta property="og:title" content="{E(en)} — Exowise"><meta property="og:description" content="{E(p['lead'][0])}"><meta property="og:url" content="https://exowise.ai/products/{p['slug']}.html">
<meta name="robots" content="index, follow, max-image-preview:large"><link rel="canonical" href="https://exowise.ai/products/{p['slug']}.html">
<meta property="og:type" content="product"><meta property="og:site_name" content="Exowise"><meta property="og:image" content="https://exowise.ai/assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(en)} — Exowise"><meta name="twitter:description" content="{E(p['lead'][0])}"><meta name="twitter:image" content="https://exowise.ai/assets/og-image.png">
<meta name="theme-color" content="#f7f1ec"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon-192.png"><link rel="icon" type="image/png" sizes="96x96" href="/assets/favicon-96.png"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">{LD(p,en)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}:root{{--tint:{p['tint']}}}</style></head><body>
<header><nav class="wrap">
<a href="/" class="brand" aria-label="Exowise">{LOGO}Exowise</a>
<div class="right"><a href="/#products" class="back" data-i18n="nav.back">← All products</a>
<div class="lang" role="group" aria-label="Language"><button type="button" data-lang="en" class="on">EN</button><button type="button" data-lang="es">ES</button></div>
<a href="#contact" class="btn small" data-i18n="nav.cta">Request a demo</a></div></nav></header>
<main>
<section class="hero"><div class="glow"><span class="g1"></span><span class="g2"></span><span class="g3"></span></div><div class="wrap">
<span class="tag reveal">{t("tag",*p['tag'])}</span>
<h1 class="reveal" data-i18n="name">{E(en)}</h1>
<p class="title reveal">{t("title",*p['title'])}</p>
<p class="lead reveal">{t("lead",*p['lead'])}</p>
<div class="cta reveal"><a href="#contact" class="btn"><span data-i18n="ct.cta">Request a demo →</span></a><a href="#features" class="btn ghost"><span data-i18n="feat.eyebrow">What it does</span></a></div>
</div></section>
<section id="features"><div class="wrap"><p class="eyebrow reveal" data-i18n="feat.eyebrow">What it does</p><h2 class="reveal" data-i18n="feat.title">Everything you need, nothing you don’t.</h2><div class="fg">{feats}</div></div></section>
<section class="how"><div class="wrap"><p class="eyebrow reveal" data-i18n="how.eyebrow">How it works</p><div class="steps">{steps}</div></div></section>
<section class="integ"><div class="wrap"><p class="eyebrow reveal">{t("ig.eyebrow","AI-ready & integrations","Listo para IA e integraciones")}</p><h2 class="reveal">{t("ig.title","Plugs into your AI agents and your core systems.","Se conecta a tus agentes de IA y a tus sistemas centrales.")}</h2>
<div class="ig"><div class="card mcp reveal"><span class="badge">MCP</span><h3>{t("ig.m.t","Native MCP connector","Conector MCP nativo")}</h3><p>{t("ig.m.p","Every Exowise product exposes a Model Context Protocol server, so any AI agent can see, query and operate it — first of all our own ExoAGI Agent, and also Claude and other MCP-compatible assistants.","Cada producto Exowise expone un servidor Model Context Protocol, para que cualquier agente de IA pueda verlo, consultarlo y operarlo: primero nuestro propio ExoAGI Agent, y también Claude y otros asistentes compatibles con MCP.")}</p><a href="/products/exoagi-agent.html" class="lnk">{t("ig.m.a","Meet ExoAGI Agent →","Conocé ExoAGI Agent →")}</a></div>
<div class="card api reveal"><span class="badge">API</span><h3>{t("ig.a.t","Integration APIs for first-class solutions","APIs de integración con soluciones de primer nivel")}</h3><p>{t("ig.a.p","REST/JSON APIs and connectors to exchange data with the systems your business already runs on.","APIs REST/JSON y conectores para intercambiar datos con los sistemas sobre los que ya funciona tu negocio.")}</p><div class="chips"><span>CRM</span><span>ERP</span><span>WMS</span><span>{t("ig.a.c","Custom systems","Sistemas propios")}</span></div></div></div></div></section>
<section class="uses"><div class="wrap in2"><div><p class="eyebrow reveal" data-i18n="use.eyebrow">Who it’s for</p><h2 class="reveal" data-i18n="use.title">Built for</h2></div><ul class="reveal">{uses}</ul></div></section>
<section class="contact" id="contact"><div class="glow"><span class="g1"></span><span class="g3"></span></div><div class="wrap">
<h2 class="reveal" data-i18n="ct.title">Want to see {E(en)} in action?</h2>
<p class="sub reveal" data-i18n="ct.sub">Tell us about your case and we’ll set up a demo with your data.</p>
<div class="cta reveal"><a href="mailto:info@exowise.ai?subject={subject}" class="btn" data-i18n="ct.cta">Request a demo →</a><a href="/#products" class="btn ghost" data-i18n="ct.more">See other products</a></div>
</div></section></main>
<footer><div class="wrap"><span>© <span id="y">2026</span> Exowise. <span data-i18n="ft.rights">All rights reserved.</span></span><a href="/">exowise.ai</a></div></footer>
<script>
const ES={json.dumps(ES,ensure_ascii=False)};
const nodes=[...document.querySelectorAll('[data-i18n]')];const EN={{}};nodes.forEach(n=>{{if(!(n.dataset.i18n in EN))EN[n.dataset.i18n]=n.textContent}});
function setLang(l){{const d=l==='es'?ES:EN;nodes.forEach(n=>{{const v=d[n.dataset.i18n];if(v)n.textContent=v}});document.documentElement.lang=l;
document.querySelectorAll('.lang button').forEach(b=>b.classList.toggle('on',b.dataset.lang===l));document.title=(l==='es'?ES.name:EN.name)+' — Exowise';try{{localStorage.setItem('exo-lang',l)}}catch(e){{}}}}
document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
let sv=null;try{{sv=localStorage.getItem('exo-lang')}}catch(e){{}}const q=new URLSearchParams(location.search).get('lang');if(q==='es'||q==='en')setLang(q);else if(sv)setLang(sv);
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.1}});document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
document.getElementById('y').textContent=new Date().getFullYear();
</script></body></html>'''
    open(OUT+p['slug']+'.html','w',encoding='utf-8').write(page)
print('ok',[p['slug'] for p in P])
