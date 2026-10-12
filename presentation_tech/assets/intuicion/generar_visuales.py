"""Figuras propias para intuicion-audio-metricas.md; ejemplos ilustrativos.

Requiere Pillow para el GIF. Ejecutar con Python desde cualquier carpeta.
No descarga datos, modelos ni material de terceros.
"""
from pathlib import Path
from html import escape
from math import sin
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
NAVY = "#00547a"
GREEN = "#6bbb90"
INK = "#183747"
MUTED = "#62747e"
WARN = "#b75940"
PALE = "#eff5f8"
MINT = "#e5f3ec"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


class Svg:
    def __init__(self, name, width, height, title, description):
        self.name = name
        self.width = width
        self.height = height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#00547a"/></marker></defs>',
            f'<rect width="{width}" height="{height}" fill="white"/>',
        ]
        self.text(32, 43, title, 25, NAVY, True)

    def text(self, x, y, content, size=19, color=INK, bold=False, anchor="start"):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" fill="{color}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}">{escape(content)}</text>')

    def rect(self, x, y, w, h, fill=PALE, stroke=NAVY, radius=10):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')

    def line(self, x1, y1, x2, y2, color=NAVY, width=2, arrow=False, dash=False):
        attrs = ' marker-end="url(#arrow)"' if arrow else ""
        if dash:
            attrs += ' stroke-dasharray="6 5"'
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{attrs}/>')

    def circle(self, x, y, r, fill=NAVY):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')

    def save(self):
        (OUT / self.name).write_text("\n".join(self.parts + ["</svg>"]), encoding="utf-8")


def transducer():
    s = Svg("rnnt.svg", 1120, 590, "RNN-T: dos formas de avanzar", "Un camino ilustrativo avanza por el audio al emitir blank y añade tokens sin avanzar el audio al emitir texto. El encoder y el predictor se combinan en el joiner.")
    s.text(32, 77, "Camino ilustrativo para «no hay tos»; no son tiempos medidos.", 17, MUTED)
    x0, y0, dx, dy = 100, 408, 145, 78
    for i in range(5):
        x = x0 + i * dx
        s.line(x, y0, x, y0 - 3 * dy, color="#dce5e9", width=1)
        s.text(x, y0 + 33, f"t{i + 1}", 18, anchor="middle")
    for j in range(4):
        y = y0 - j * dy
        s.line(x0, y, x0 + 4 * dx, y, color="#dce5e9", width=1)
        s.text(x0 - 25, y + 6, str(j), 17, MUTED, anchor="end")
    s.text(360, 477, "Pasos acústicos →", 19, NAVY, anchor="middle")
    s.text(32, 129, "Tokens", 16, MUTED)
    s.text(32, 149, "emitidos", 16, MUTED)
    path = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3)]
    for a, b in zip(path, path[1:]):
        x1, y1 = x0 + a[0]*dx, y0 - a[1]*dy
        x2, y2 = x0 + b[0]*dx, y0 - b[1]*dy
        s.line(x1, y1, x2, y2, width=4, arrow=True)
        if a[1] == b[1]:
            s.text((x1+x2)/2, y1-12, "blank", 16, NAVY, anchor="middle")
        else:
            token = ["no", "hay", "tos"][b[1]-1]
            s.text(x1+15, (y1+y2)/2+6, token, 19, NAVY, True)
    s.rect(760, 127, 305, 62)
    s.text(912, 164, "Encoder: audio", 20, anchor="middle")
    s.rect(760, 222, 305, 62, MINT)
    s.text(912, 259, "Predictor: texto previo", 20, anchor="middle")
    s.rect(795, 326, 235, 65)
    s.text(912, 367, "Joiner", 21, NAVY, True, anchor="middle")
    s.line(1039, 158, 1090, 158)
    s.line(1090, 158, 1090, 359)
    s.line(1090, 359, 1030, 359, arrow=True)
    s.line(912, 284, 912, 326, arrow=True)
    s.text(912, 427, "¿Token o blank?", 20, NAVY, True, anchor="middle")
    s.line(912, 391, 912, 402, arrow=True)
    s.text(32, 545, "Emitir texto actualiza el predictor. Emitir blank avanza el índice acústico.", 21, NAVY, True)
    s.save()


def decoder():
    s = Svg("decoder.svg", 1120, 620, "Red neuronal y decoding: dos pasos distintos", "El decoder atiende al audio codificado y al texto previo, produce probabilidades, y greedy o beam search selecciona una secuencia. Un ejemplo numérico muestra que greedy puede perder la secuencia de mayor probabilidad.")
    s.rect(32, 108, 236, 82)
    s.text(150, 141, "Audio codificado", 20, NAVY, True, anchor="middle")
    s.text(150, 172, "salida del encoder", 16, MUTED, anchor="middle")
    s.rect(32, 217, 236, 82, MINT)
    s.text(150, 250, "Texto previo", 20, NAVY, True, anchor="middle")
    s.text(150, 282, "«no refiere»", 21, anchor="middle")
    s.rect(340, 144, 277, 125)
    s.text(478, 181, "Decoder neuronal", 22, NAVY, True, anchor="middle")
    s.text(478, 216, "atención + otras capas", 18, anchor="middle")
    s.text(478, 249, "calcula probabilidades", 17, MUTED, anchor="middle")
    s.line(268, 149, 340, 185, arrow=True)
    s.line(268, 258, 340, 232, arrow=True)
    s.rect(699, 108, 363, 190, MINT)
    s.text(880, 143, "Decoding", 22, NAVY, True, anchor="middle")
    s.text(728, 184, "Greedy: una hipótesis", 19)
    s.text(728, 216, "Beam: varias hipótesis", 19)
    s.text(728, 264, "→ seleccionar texto", 20, NAVY, True)
    s.line(617, 205, 699, 205, arrow=True)
    s.text(660, 190, "P(token)", 14, MUTED, anchor="middle")
    s.line(880, 298, 880, 330)
    s.line(880, 330, 150, 330)
    s.line(150, 330, 150, 299, arrow=True)
    s.text(508, 352, "El texto elegido vuelve como prefijo para el siguiente paso.", 17, MUTED, anchor="middle")
    s.rect(32, 388, 1030, 192, fill=PALE)
    s.text(56, 423, "Por qué greedy y la mejor secuencia pueden diferir", 21, NAVY, True)
    s.text(56, 463, "Ruta A: «tiene» (0,6) → «tos» (0,4) → fin (1)     producto = 0,24", 19)
    s.text(56, 501, "Ruta B: «niega» (0,4) → «tos» (0,9) → fin (1)     producto = 0,36", 19)
    s.text(56, 547, "Greedy empieza por A; un beam que conserve B puede recuperarla. Valores inventados.", 17, MUTED)
    s.save()


def metrics():
    s = Svg("metricas.svg", 1120, 805, "Tres preguntas distintas sobre una transcripción", "DER mide segundos atribuidos incorrectamente. cpWER mide errores de palabras agrupadas por hablante. tcpWER añade restricciones temporales a los emparejamientos.")
    s.text(32, 99, "DER: ¿qué voz estaba hablando en cada intervalo?", 23, NAVY, True)
    x0, scale = 190, 77
    for label, y, boundary in [("Referencia", 136, 5), ("Predicción", 193, 6)]:
        s.text(32, y+26, label, 19)
        s.rect(x0, y, boundary*scale, 39, PALE, NAVY, 0)
        s.rect(x0+boundary*scale, y, (10-boundary)*scale, 39, MINT, NAVY, 0)
        s.text(x0+boundary*scale/2, y+26, "S1", 20, anchor="middle")
        s.text(x0+(boundary+(10-boundary)/2)*scale, y+26, "S2", 20, anchor="middle")
    s.rect(x0+5*scale, 190, scale, 45, fill="none", stroke=WARN, radius=0)
    for t in [0,5,6,10]:
        s.text(x0+t*scale, 258, f"{t} s", 16, MUTED, anchor="middle")
    s.text(32, 299, "1 s de confusión / 10 s de habla = 10 % DER. Sin solapamiento; collar = 0.", 20, NAVY, True)
    s.line(32, 329, 1062, 329, color="#dce5e9")
    s.text(32, 372, "cpWER: ¿qué palabras pertenecen a cada hablante?", 23, NAVY, True)
    s.text(32, 415, "Referencia", 19, MUTED, True)
    s.text(550, 415, "Predicción", 19, MUTED, True)
    s.text(32, 455, "S1: tengo tos", 22)
    s.text(550, 455, "S1: tengo tos desde", 22)
    s.text(32, 495, "S2: desde cuándo", 22)
    s.text(550, 495, "S2: cuándo", 22)
    s.text(32, 544, "Sin hablantes: mismo texto → WER = 0 %", 20, NAVY, True)
    s.text(32, 580, "Por hablante: «desde» sobra en S1 y falta en S2 → 2 / 4 = 50 % cpWER", 20, WARN, True)
    s.line(32, 610, 1062, 610, color="#dce5e9")
    s.text(32, 651, "tcpWER: ¿las palabras aparecen en un momento compatible?", 23, NAVY, True)
    s.text(32, 693, "Referencia: «no tengo alergias», minuto 1.", 20)
    s.text(32, 729, "Predicción: mismo hablante y texto, minuto 20.", 20)
    s.text(32, 772, "cpWER puede dar 0 %; tcpWER penaliza el desfase con una tolerancia razonable.", 18, NAVY, True)
    s.save()


def percentiles():
    s = Svg("percentiles.svg", 1120, 670, "p50 y p95: ordenar las esperas", "Cien latencias inventadas ordenadas: p50 sesenta segundos, p95 ciento ochenta segundos y máximo seiscientos segundos. El percentil noventa y cinco describe la cola sin ser el máximo.")
    s.text(32, 80, "100 ejecuciones ilustrativas, ordenadas de la más rápida a la más lenta.", 18, MUTED)
    values = [20 + 40*i/49 for i in range(50)] + [60 + 120*i/44 for i in range(45)] + [220,260,310,360,600]
    assert len(values) == 100 and values[49] == 60 and values[94] == 180
    x0, y0, w, h = 110, 504, 855, 360
    xpos = lambda rank: x0 + rank/100*w
    ypos = lambda sec: y0 - sec/650*h
    for sec in [0,60,180,300,600]:
        y = ypos(sec)
        s.line(x0, y, x0+w, y, color="#dce5e9", width=1)
        s.text(x0-18, y+6, f"{sec} s", 16, MUTED, anchor="end")
    s.line(x0, y0, x0+w+20, y0, arrow=True)
    points = " ".join(f"{xpos(i+1):.2f},{ypos(v):.2f}" for i,v in enumerate(values))
    s.parts.append(f'<polyline points="{points}" fill="none" stroke="{NAVY}" stroke-width="4"/>')
    for rank, sec, label in [(50,60,"p50 = 60 s"),(95,180,"p95 = 180 s"),(100,600,"máx. = 600 s")]:
        x,y = xpos(rank),ypos(sec)
        s.line(x,y0,x,y,color=GREEN,dash=True)
        s.circle(x,y,6,NAVY)
        if rank==50:
            s.text(x-22,y-18,label,20,NAVY,True,anchor="end")
        elif rank==95:
            s.text(x-20,y-18,label,20,NAVY,True,anchor="end")
        else:
            s.text(x-20,y-18,label,20,WARN,True,anchor="end")
        s.text(x,y0+29,str(rank),17,MUTED,anchor="middle")
    s.text(538, 561, "Posición al ordenar las 100 ejecuciones →", 20, NAVY, anchor="middle")
    s.text(32, 609, "p50: espera típica.  p95: límite para aproximadamente 95 de cada 100 casos.", 21, NAVY, True)
    s.text(32, 644, "Las cinco ejecuciones más lentas pueden superar p95; aquí una tarda 10 minutos.", 18, MUTED)
    s.save()


def ctc():
    W,H = 1120,590
    titlefont=ImageFont.truetype(BOLD,28)
    bodyfont=ImageFont.truetype(FONT,23)
    smallfont=ImageFont.truetype(FONT,19)
    tokenfont=ImageFont.truetype(BOLD,33)
    frames=[]
    durations=[]
    labels=["t","t","_","o","o","_","s","s"]
    steps=list(range(9))+[9,10,11]
    for stage in steps:
        im=Image.new("RGB",(W,H),"white")
        d=ImageDraw.Draw(im)
        d.text((32,26),"CTC: varios pasos acústicos, pocos tokens de texto",font=titlefont,fill=NAVY)
        d.text((32,76),"Ejemplo con letras; los modelos también pueden usar subpalabras.",font=smallfont,fill=MUTED)
        for j in range(8):
            x=235+j*99
            d.text((x+30,123),f"t{j+1}",font=smallfont,fill=MUTED)
            d.rounded_rectangle((x,161,x+86,231),radius=8,fill=PALE,outline=NAVY,width=2)
            if j<min(stage,8):
                d.text((x+28,175),labels[j],font=tokenfont,fill=NAVY)
        d.text((32,180),"Predicción",font=bodyfont,fill=INK)
        d.text((32,251),"_ = blank: no emitir token aquí; no equivale necesariamente a silencio.",font=smallfont,fill=MUTED)
        d.text((32,310),"1. Colapsar",font=bodyfont,fill=INK)
        d.text((32,341),"repeticiones",font=smallfont,fill=MUTED)
        if stage>=9:
            collapsed=["t","_","o","_","s"]
            for j,t in enumerate(collapsed):
                x=235+j*99
                d.rounded_rectangle((x,300,x+86,370),radius=8,fill=MINT,outline=GREEN,width=2)
                d.text((x+28,314),t,font=tokenfont,fill=NAVY)
        d.text((32,429),"2. Quitar blank",font=bodyfont,fill=INK)
        if stage>=10:
            for j,t in enumerate(["t","o","s"]):
                x=235+j*99
                d.rounded_rectangle((x,414,x+86,484),radius=8,fill=MINT,outline=GREEN,width=2)
                d.text((x+28,428),t,font=tokenfont,fill=NAVY)
            d.text((631,434),"→  tos",font=tokenfont,fill=NAVY)
        d.text((32,530),"Este GIF muestra una ruta de decoding; entrenar CTC suma las rutas compatibles.",font=smallfont,fill=MUTED)
        frames.append(im)
        durations.append(650 if stage<9 else 1700 if stage<11 else 2600)
    frames[0].save(OUT/"ctc.gif",save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=False)
    frames[-1].save(OUT/"ctc-poster.png")


if __name__ == "__main__":
    for build in (transducer,decoder,metrics,percentiles,ctc):
        build()
    print(f"Figuras generadas en {OUT}")
