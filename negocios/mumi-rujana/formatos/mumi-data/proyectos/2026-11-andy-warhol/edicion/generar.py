"""Genera hf/index.html (Mumi Data · Andy Warhol) a partir de transcripcion.json."""
import json, re, html
W = json.load(open('transcripcion.json'))
DUR = 73.07
# --- correcciones de la transcripción automática ---
def reemplazar(i0, i1, texto):
    global W
    t0, t1 = W[i0]['start'], W[i1]['end']
    pal = texto.split(); paso = (t1 - t0) / len(pal)
    nuevas = [{'id': f'r{i0}_{k}', 'text': x, 'start': round(t0 + k*paso, 3), 'end': round(t0 + (k+1)*paso, 3)} for k, x in enumerate(pal)]
    W = W[:i0] + nuevas + W[i1+1:]
# pedido de Mumi (v2): texto en castellano y frases corregidas
reemplazar(177, 193, '¿Querés saber los 8 puntos que usaba Andy Warhol para convertir tu música en arte?')
reemplazar(160, 163, 'convertirlos en algo musical.')
reemplazar(148, 154, 'Podés convertirlo en algo musical,')
reemplazar(48, 51, 'Velvet Underground.')
for w in W:
    if w['text'] == 'Apropión': w['text'] = 'Apropiación'
    if w['text'] == 'puedes': w['text'] = 'podés'
KEY = {'música','visual','andy','warhol','banana','arte','obra','ocho','8','puntos','clave','repetición','repetir',
       'cotidiano','cotidianos','lata','sopa','subte','canción','velvet','underground','original','imagen','colectiva','musical','cd','video'}
def clean(t): return re.sub(r'[^\wáéíóúñü]', '', t.lower())

# --- grupos de 2-3 palabras: corte en fin de frase, pausa >=150 ms o 3 palabras ---
groups, cur = [], []
for i, w in enumerate(W):
    cur.append(w)
    nxt = W[i+1] if i+1 < len(W) else None
    end_sentence = w['text'][-1] in '.,!?'
    pause = nxt and nxt['start'] - w['end'] >= 0.15
    if len(cur) >= 3 or end_sentence or pause or not nxt:
        groups.append(cur); cur = []
caps = []
for gi, g in enumerate(groups):
    s = max(0.15, g[0]['start']); e = g[-1]['end'] + 0.12
    if gi + 1 < len(groups): e = min(e, groups[gi+1][0]['start'])
    e = min(e, DUR - 0.05)
    words = ' '.join(
        f'<span class="k">{html.escape(w["text"])}</span>' if clean(w['text']) in KEY else html.escape(w['text'])
        for w in g)
    caps.append((f'c{gi}', round(s, 2), round(e - s, 2), words))

# --- palabras gigantes, carteles e insertos (inicio, fin) ---
BIG = [  # id, start, end, html, color, top
    ('b-visual', 2.20, 3.00, 'VISUAL', 'red', 820),
    ('b-andy', 9.10, 10.85, 'ANDY WARHOL', 'blue andy', 940),
    ('b-arte', 12.10, 13.40, 'OBRA<br>DE ARTE', 'red', 760),
    ('b-nadie', 20.70, 21.95, 'NADIE', 'blue', 840),
    ('b-visual2', 25.80, 27.40, 'LO VISUAL', 'red', 840),
    ('b-ocho', 30.05, 33.90, '<span class="n">8</span><br>PUNTOS CLAVE', 'red', 330),
    ('b-sonidos', 57.60, 58.85, 'SONIDOS', 'blue', 840),
]
TAGS = [  # carteles de puntos
    ('t1', 34.00, 37.60, '1', 'REPETICIÓN'),
    ('t2', 49.70, 52.10, '2', 'LO COTIDIANO'),
]
ZOOMS = [2.24, 9.12, 20.72, 25.04, 28.64, 37.68, 52.16, 58.88, 64.91, 68.07]

BANANA = '''<svg viewBox="0 0 300 500"> <defs> <pattern id="bn-dots" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="4.5" cy="4.5" r="2.2" fill="#171713"/></pattern> <clipPath id="bn-body"><path d="M92 44 C 172 70, 242 168, 240 282 C 238 382, 192 448, 138 478 C 122 488, 104 478, 112 462 C 150 418, 152 352, 142 272 C 132 184, 110 112, 76 64 Z"/></clipPath> </defs> <path d="M92 44 C 172 70, 242 168, 240 282 C 238 382, 192 448, 138 478 C 122 488, 104 478, 112 462 C 150 418, 152 352, 142 272 C 132 184, 110 112, 76 64 Z" fill="#FFEC4E"/> <g clip-path="url(#bn-body)"> <path d="M76 64 C 110 112, 132 184, 142 272 C 152 352, 150 418, 112 462 L 150 470 C 178 420, 186 350, 178 270 C 170 180, 140 110, 92 50 Z" fill="url(#bn-dots)" opacity=".75"/> <path d="M80 70 C 112 118, 132 190, 142 272 C 150 350, 148 414, 116 458 C 134 430, 160 380, 158 300 C 156 220, 128 130, 80 70 Z" fill="#171713"/> <path d="M96 50 C 168 104, 206 196, 200 300 C 196 380, 168 438, 128 474" fill="none" stroke="#171713" stroke-width="5" stroke-linecap="round"/> <path d="M150 92 C 196 150, 222 230, 218 310" fill="none" stroke="#171713" stroke-width="3" stroke-linecap="round" opacity=".7"/> <path d="M168 118 c 10 4, 16 14, 10 18 c -8 2, -14 -8, -10 -18 z" fill="#171713"/> <path d="M214 214 c 6 10, 6 26, -2 28 c -6 -4, -6 -20, 2 -28 z" fill="#171713"/> <path d="M206 360 c 10 6, 10 30, 0 40 c -8 -6, -10 -28, 0 -40 z" fill="#171713"/> <path d="M180 196 c 6 2, 8 8, 4 10 c -4 0, -6 -6, -4 -10 z" fill="#171713"/> <path d="M178 420 c 8 2, 10 12, 4 14 c -6 -2, -8 -10, -4 -14 z" fill="#171713"/> </g> <path d="M92 44 C 172 70, 242 168, 240 282 C 238 382, 192 448, 138 478 C 122 488, 104 478, 112 462 C 150 418, 152 352, 142 272 C 132 184, 110 112, 76 64 Z" fill="none" stroke="#171713" stroke-width="9" stroke-linejoin="round"/> <path d="M76 64 L 56 28 C 52 16, 66 8, 78 14 L 98 40 C 96 52, 86 60, 76 64 Z" fill="#171713"/> <path d="M112 462 C 104 478, 122 490, 138 478 C 130 470, 120 464, 112 462 Z" fill="#171713"/> </svg>'''
CAN = '''<svg viewBox="0 0 160 220"><ellipse cx="80" cy="22" rx="58" ry="14" fill="#F5F3E9" stroke="#171713" stroke-width="6"/><path d="M22 22 V198 A58 14 0 0 0 138 198 V22" fill="#F5F3E9" stroke="#171713" stroke-width="6"/><path d="M22 30 V100 A58 14 0 0 0 138 100 V30 A58 14 0 0 1 22 30 Z" fill="#F20D08"/><text x="80" y="80" text-anchor="middle" font-family="Bebas Neue" font-size="40" fill="#F5F3E9">TOMATE</text><text x="80" y="150" text-anchor="middle" font-family="Bebas Neue" font-size="44" fill="#F20D08">MUMI</text><circle cx="80" cy="178" r="8" fill="#FFEC4E" stroke="#171713" stroke-width="3"/></svg>'''
PLAY = '''<svg viewBox="0 0 340 260"><rect x="12" y="12" width="316" height="236" rx="18" fill="#F5F3E9" stroke="#171713" stroke-width="10"/><rect x="12" y="12" width="316" height="34" fill="#171713"/><rect x="12" y="214" width="316" height="34" fill="#171713"/><rect x="30" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="30" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="70" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="70" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="110" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="110" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="150" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="150" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="190" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="190" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="230" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="230" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="270" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="270" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="310" y="22" width="18" height="14" rx="3" fill="#F5F3E9"/><rect x="310" y="224" width="18" height="14" rx="3" fill="#F5F3E9"/><path d="M140 82 L 222 130 L 140 178 Z" fill="#F20D08" stroke="#171713" stroke-width="8" stroke-linejoin="round"/></svg>'''
CD = '''<svg viewBox="0 0 300 300"><circle cx="150" cy="150" r="138" fill="#F5F3E9" stroke="#171713" stroke-width="10"/><circle cx="150" cy="150" r="112" fill="none" stroke="#2C7EF4" stroke-width="14"/><circle cx="150" cy="150" r="90" fill="none" stroke="#EFC3EB" stroke-width="14"/><circle cx="150" cy="150" r="70" fill="none" stroke="#FFEC4E" stroke-width="14"/><circle cx="150" cy="150" r="52" fill="#F20D08" stroke="#171713" stroke-width="6"/><text x="150" y="141" text-anchor="middle" font-family="Bebas Neue" font-size="30" fill="#F5F3E9">MUMI</text><circle cx="150" cy="160" r="14" fill="#171713"/><path d="M70 80 A 110 110 0 0 1 120 46" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".8"/></svg>'''
ANDY = '''<svg viewBox="0 0 200 200"><path d="M60 182 Q100 168 140 182 L152 200 L48 200 Z" fill="#171713"/><ellipse cx="100" cy="122" rx="46" ry="56" fill="#EFC3EB" stroke="#171713" stroke-width="6"/><circle cx="80" cy="120" r="16" fill="#171713"/><circle cx="120" cy="120" r="16" fill="#171713"/><path d="M96 120 L104 120" stroke="#171713" stroke-width="6"/><path d="M86 152 Q100 158 114 152" fill="none" stroke="#171713" stroke-width="5" stroke-linecap="round"/><path d="M42 100 L34 62 L52 72 L48 34 L66 56 L72 22 L88 50 L100 16 L112 48 L126 22 L134 54 L152 34 L150 72 L168 62 L160 100 Q140 78 100 80 Q60 78 42 100 Z" fill="#F5F3E9" stroke="#171713" stroke-width="6" stroke-linejoin="round"/></svg>'''
TILE = ['#FFEC4E', '#2C7EF4', '#EFC3EB', '#75EF89', '#F20D08', '#F5F3E9']

def tiles(n, art, ink):
    out = []
    for i in range(n):
        bg = TILE[(i * 5 + i // 4) % len(TILE)]
        col = ink if bg not in ('#171713',) else '#F5F3E9'
        out.append(f'<div class="tile" id="{art}{i}" style="background:{bg};color:{col}">{BANANA if art=="ba" else CAN}</div>')
    return ''.join(out)

parts = []
parts.append(f'<video id="cam" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/video.mp4" data-has-audio="true"></video>')
parts.append('<div id="st-video" class="clip sticker" data-start="4.96" data-duration="1.90" data-track-index="1"><div id="st-video-in" class="st-in">' + PLAY + '</div></div>')
parts.append('<div id="st-cd" class="clip sticker" data-start="7.10" data-duration="1.30" data-track-index="1"><div id="st-cd-in" class="st-in">' + CD + '</div></div>')
QA = ['#FFEC4E', '#2C7EF4', '#F20D08', '#75EF89']
parts.append('<div id="ins-andy" class="clip insert" data-start="9.10" data-duration="1.75" data-track-index="1"><div id="ia-in" class="ins-in grid2">' + ''.join(f'<div class="tile" id="an{i}" style="background:{c}">{ANDY}</div>' for i, c in enumerate(QA)) + '</div></div>')
# inserto banana (voz en off)
parts.append('''<div id="ins-banana" class="clip insert" data-start="13.44" data-duration="6.40" data-track-index="1"><div id="ib-in" class="ins-in cream stripes">
  <div id="ib-art" class="big-banana">''' + BANANA + '''</div>
  <div id="ib-lbl" class="paper-label">THE VELVET UNDERGROUND &amp; NICO · 1967</div></div></div>''')
parts.append(f'''<div id="ins-rep" class="clip insert" data-start="43.20" data-duration="6.50" data-track-index="1"><div id="ir-in" data-layout-allow-overlap class="ins-in grid4">{tiles(16,"ba","#171713")}</div>
  <div id="ir-lbl" class="grid-label">REPETICIÓN</div></div>''')
parts.append(f'''<div id="ins-lata" class="clip insert" data-start="53.70" data-duration="2.70" data-track-index="1"><div id="il-in" data-layout-allow-overlap class="ins-in grid3">{tiles(9,"ca","#171713")}</div></div>''')
for bid, s, e, h, col, top in BIG:
    parts.append(f'<div id="{bid}" class="clip big {col}" data-start="{s}" data-duration="{round(e-s,2)}" data-track-index="2" style="top:{top}px"><div id="{bid}-in" class="big-in">{h}</div></div>')
for tid, s, e, n, txt in TAGS:
    parts.append(f'<div id="{tid}" class="clip tag" data-start="{s}" data-duration="{round(e-s,2)}" data-track-index="3"><div class="tag-rot"><div id="{tid}-in" class="tag-in"><span class="tag-n">{n}.</span> {txt}</div></div></div>')
parts.append('<div id="t-subte" class="clip tag small" data-start="61.00" data-duration="3.70" data-track-index="3"><div class="tag-rot"><div id="t-subte-in" class="tag-in blue">ESCUCHÁ: SUBTE</div></div></div>')
parts.append(f'<div id="caps" class="clip" data-start="0" data-duration="{DUR}" data-track-index="4" data-track-kind="captions">' +
             ''.join(f'<div id="{cid}" class="cap" ><div id="{cid}-in" class="cap-in">{wh}</div></div>' for cid, s, d, wh in caps) + '</div>')
parts.append(f'<div id="sello" data-layout-allow-safe-zone class="clip" data-start="0" data-duration="{DUR}" data-track-index="5"><div class="sello-rot"><div id="sello-in" class="sello-in">MUMI <b>DATA</b></div></div></div>')
parts.append(f'<div id="fin" class="clip" data-start="71.55" data-duration="{round(DUR-71.55,2)}" data-track-index="6"><div id="fin-in" class="fin-in cream stripes"><div class="fin-t">MUMI<br><span>DATA</span></div><div class="fin-b">{BANANA}</div></div></div>')

js = ['const tl = gsap.timeline({ paused: true });']
# zooms de golpe
for z in ZOOMS:
    js.append(f'tl.set("#cam", {{ scale: 1.14 }}, {z}).set("#cam", {{ scale: 1 }}, {z + 1.6});')
# subtítulos
for cid, s, d, _ in caps:
    js.append(f'tl.fromTo("#{cid}-in", {{ scale: 0.82, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.12, ease: "back.out(3)" }}, {s});')
    js.append(f'tl.set("#{cid}", {{ opacity: 1, visibility: "visible" }}, {s}).set("#{cid}", {{ opacity: 0, visibility: "hidden" }}, {round(s+d,2)});')
for bid, s, e, *_ in BIG:
    js.append(f'tl.fromTo("#{bid}-in", {{ scale: 1.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.18, ease: "power4.out" }}, {s}).to("#{bid}-in", {{ opacity: 0, duration: 0.1 }}, {round(e-0.1,2)});')
for tid, s, e, *_ in TAGS + [('t-subte', 61.0, 64.7)]:
    js.append(f'tl.fromTo("#{tid}-in", {{ x: -700 }}, {{ x: 0, duration: 0.28, ease: "back.out(1.6)" }}, {s}).to("#{tid}-in", {{ x: 900, duration: 0.22, ease: "power2.in" }}, {round(e-0.22,2)});')
js.append('tl.fromTo("#st-video-in", { scale: 0, rotation: -20 }, { scale: 1, rotation: -6, duration: 0.25, ease: "back.out(2.5)" }, 4.96);')
js.append('tl.fromTo("#st-cd-in", { scale: 0, rotation: 0 }, { scale: 1, rotation: 360, duration: 1.2, ease: "power2.out" }, 7.10);')
for i in range(4):
    js.append(f'tl.fromTo("#an{i}", {{ scale: 0 }}, {{ scale: 1, duration: 0.18, ease: "back.out(2)" }}, {round(9.1 + i*0.08, 2)});')
js.append('tl.fromTo("#ib-in", { y: 1920 }, { y: 0, duration: 0.25, ease: "power3.out" }, 13.44);')
js.append('tl.fromTo("#ib-art", { rotation: -25, scale: 0.6 }, { rotation: 0, scale: 1, duration: 0.5, ease: "back.out(2)" }, 13.5).to("#ib-art", { scale: 1.08, duration: 5.5, ease: "none" }, 14.0);')
js.append('tl.fromTo("#ib-lbl", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.3 }, 16.24);')
js.append('tl.to("#ib-in", { y: -1920, duration: 0.2, ease: "power3.in" }, 19.62);')
for i in range(16):
    js.append(f'tl.fromTo("#ba{i}", {{ scale: 0 }}, {{ scale: 1, duration: 0.18, ease: "back.out(2)" }}, {round(43.2 + i*0.09, 2)});')
js.append('tl.fromTo("#ir-lbl", { scale: 2, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.25, ease: "power4.out" }, 44.8);')
js.append('tl.to("#ir-in", { scale: 1.06, duration: 4.5, ease: "none" }, 45.0);')
for i in range(9):
    js.append(f'tl.fromTo("#ca{i}", {{ y: -300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.2, ease: "back.out(2)" }}, {round(53.7 + i*0.07, 2)});')
js.append('tl.fromTo("#sello-in", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2)" }, 0.3);')
js.append('tl.fromTo("#fin-in", { scale: 1.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "power4.out" }, 71.55);')
js.append('window.__timelines["main"] = tl;\ntl.seek(0);')

CSS = '''
@font-face { font-family: "Bebas Neue"; src: url("assets/fonts/BebasNeue-Regular.ttf"); }
@font-face { font-family: "Space Mono"; font-weight: 700; src: url("assets/fonts/SpaceMono-Bold.ttf"); }
:root { --red:#F20D08; --blue:#2C7EF4; --yellow:#FFEC4E; --green:#75EF89; --pink:#EFC3EB; --cream:#F5F3E9; --ink:#171713; }
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1080px; height:1920px; overflow:hidden; background:var(--ink); }
#root { position:relative; width:1080px; height:1920px; overflow:hidden; font-family:"Bebas Neue"; }
#cam { position:absolute; inset:0; width:1080px; height:1920px; object-fit:cover; transform-origin:50% 22%; z-index:0; }
.insert { position:absolute; inset:0; z-index:5; overflow:hidden; }
.ins-in { position:absolute; inset:0; }
.cream { background:var(--cream); }
.stripes { background-image:repeating-linear-gradient(90deg, rgba(44,126,244,.16) 0 46px, transparent 46px 92px); }
.big-banana { position:absolute; left:200px; top:250px; width:760px; height:760px; width:800px; height:800px; color:var(--ink); }
.big-banana svg { width:100%; height:100%; filter:drop-shadow(14px 14px 0 rgba(23,23,19,.9)); }
.paper-label { position:absolute; left:90px; right:90px; top:190px; text-align:center; font-family:"Space Mono"; font-weight:700; font-size:40px; color:var(--ink);
  background:var(--yellow); padding:22px 18px; border:5px solid var(--ink); box-shadow:10px 10px 0 var(--ink); }
.sticker { position:absolute; left:0; right:0; top:560px; height:480px; z-index:5; display:flex; justify-content:center; }
.st-in { width:480px; height:480px; display:flex; align-items:center; justify-content:center; }
.st-in svg { width:100%; height:100%; filter:drop-shadow(10px 10px 0 #171713); }
.grid2 { display:grid; grid-template-columns:repeat(2,1fr); grid-template-rows:repeat(2,370px); gap:8px; padding:8px; background:var(--ink); top:150px; height:764px; left:0; right:0; position:absolute; }
.grid2 .tile { overflow:hidden; } .grid2 .tile svg { width:auto; height:88%; }
#ins-andy { background:var(--ink); }
.big.andy { font-size:170px; }
.grid4, .grid3 { display:grid; background:var(--ink); gap:8px; padding:8px; }
.grid4 { grid-template-columns:repeat(4,1fr); grid-template-rows:repeat(4,1fr); top:350px; bottom:860px; }
.grid3 { grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(3,1fr); top:200px; bottom:860px; }
.ins-in.grid4, .ins-in.grid3 { position:absolute; left:0; right:0; }
#ins-rep, #ins-lata { background:var(--ink); }
.tile { display:flex; align-items:center; justify-content:center; }
.tile svg { width:82%; height:82%; }
.grid-label { position:absolute; left:0; right:0; top:180px; text-align:center; font-size:150px; line-height:1; color:var(--red);
  text-shadow:6px 6px 0 var(--cream); }
.big { position:absolute; left:0; right:0; z-index:6; text-align:center; line-height:.86; font-size:200px; }
.big-in { display:inline-block; text-shadow:7px 7px 0 var(--ink); }
.big.red { color:var(--red); } .big.blue { color:var(--blue); }
.big .n { font-size:520px; line-height:.8; color:var(--yellow); }
.tag { position:absolute; left:0; right:0; top:820px; z-index:7; display:flex; justify-content:center; }
.tag.small { top:300px; }
.tag-rot { transform:rotate(-4deg); }
.tag-in { background:var(--red); color:var(--cream); font-size:120px; line-height:1; padding:26px 46px 14px; border:6px solid var(--ink); box-shadow:12px 12px 0 var(--ink); }
.tag.small .tag-in { font-size:96px; }
.tag-in.blue { background:var(--blue); }
.tag-n { color:var(--yellow); }
#caps { position:absolute; inset:0; z-index:8; }
.cap { position:absolute; left:0; right:0; top:1110px; text-align:center; visibility:hidden; opacity:0; }
.cap-in { display:inline-block; color:var(--yellow); font-size:96px; line-height:1; padding:0 20px; max-width:800px;
  -webkit-text-stroke:4px var(--ink); paint-order:stroke fill; text-shadow:6px 6px 0 var(--ink); }
.cap-in .k { color:var(--red); }
#sello { position:absolute; right:22px; bottom:26px; width:300px; height:120px; z-index:9; }
.sello-rot { transform:rotate(-6deg); width:100%; height:100%; }
.sello-in { width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--cream); color:var(--ink);
  font-size:66px; border:4px solid var(--ink); clip-path:polygon(0 8%,6% 0,20% 6%,38% 0,55% 5%,72% 0,88% 6%,100% 2%,98% 30%,100% 62%,97% 100%,80% 94%,60% 100%,40% 95%,22% 100%,4% 94%,0 70%,3% 40%); }
.sello-in b { color:var(--red); font-weight:400; margin-left:12px; }
#fin { position:absolute; inset:0; z-index:10; }
.fin-in { position:absolute; inset:0; }
.fin-t { position:absolute; left:0; right:0; top:520px; text-align:center; font-size:300px; line-height:.85; color:var(--ink); }
.fin-t span { color:var(--red); }
.fin-b { position:absolute; left:340px; top:1080px; width:400px; height:400px; color:var(--ink); }
.fin-b svg { width:100%; height:100%; }
'''
page = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
{chr(10).join(parts)}
</div>
<script>
{chr(10).join(js)}
</script>
</body>
</html>'''
open('hf/index.html', 'w').write(page)
print(len(caps), 'grupos de subtítulos')
