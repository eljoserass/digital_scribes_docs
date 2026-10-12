"""Figuras propias para intuicion-audio-metricas.md; ejemplos ilustrativos.

Requiere Pillow para el GIF e Inkscape para las versiones PNG nuevas.
Ejecutar con Python desde cualquier carpeta.
No descarga datos, modelos ni material de terceros.
"""
from pathlib import Path
from html import escape
from math import sin
import subprocess
import shutil
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


def acoustic_encoder():
    s = Svg("encoders.svg", 1200, 650, "Encoder: del sonido a representaciones útiles", "El audio se transforma en características, patrones locales y vectores contextualizados. ASR conserva una secuencia temporal; un speaker encoder con pooling produce un vector por segmento para comparar voces.")
    s.text(32, 80, "Ruta ilustrativa tipo Whisper: cada bloque aprende una transformación.", 18, MUTED)
    boxes = [(32,180,"Audio"),(268,180,"Log-Mel"),(504,205,"Convoluciones"),(764,180,"Transformer")]
    for x,w,label in boxes:
        s.rect(x,120,w,126)
        s.text(x+w/2,150,label,20,NAVY,True,anchor="middle")
    points = " ".join(f"{50+i*1.9:.2f},{207+17*sin(i*.44)*sin(i*.13):.2f}" for i in range(77))
    s.parts.append(f'<polyline points="{points}" fill="none" stroke="{NAVY}" stroke-width="2"/>')
    for col in range(8):
        for row in range(4):
            color = ["#00547a","#6bbb90","#b9d8e6","#eff5f8"][(row+col*3)%4]
            s.rect(289+col*17,167+row*15,15,13,color,"none",0)
    s.text(606,192,"patrones locales",17,anchor="middle")
    s.text(606,220,"menos pasos",17,anchor="middle")
    s.text(854,192,"combinar contexto",17,anchor="middle")
    s.text(854,220,"entre pasos",17,anchor="middle")
    for x1,x2 in [(212,268),(448,504),(709,764)]:
        s.line(x1,184,x2,184,arrow=True)
    s.line(944,184,979,184,arrow=True)
    for i in range(4):
        s.rect(995+i*35,149,22,69,MINT,NAVY,1)
        s.text(1006+i*35,240,f"h{i+1}",14,anchor="middle")
    s.text(1057,116,"Vectores",19,NAVY,True,anchor="middle")
    s.text(1057,273,"secuencia temporal",15,MUTED,anchor="middle")
    s.text(32,304,"h1, h2… son listas de números aprendidos; todavía no son palabras ni identidades.",20,NAVY,True)
    s.line(32,335,1159,335,color="#dce5e9")
    s.text(32,378,"Qué queremos conservar cambia según la tarea",23,NAVY,True)
    s.rect(32,416,529,157,PALE)
    s.text(56,451,"Encoder acústico para ASR",22,NAVY,True)
    s.text(56,489,"Conservar evolución de los sonidos.",20)
    s.text(56,524,"Secuencia de vectores → salida de texto.",19)
    s.rect(603,416,556,157,MINT)
    s.text(627,451,"Speaker encoder + pooling",22,NAVY,True)
    s.text(627,489,"Resumir rasgos de voz de un segmento.",20)
    s.text(627,524,"Muchos pasos → un vector para comparar voces.",19)
    s.text(32,618,"El dibujo no es audio ni un espectrograma real. Otras arquitecturas usan otra ruta.",18,MUTED)
    s.save()


def speaker_embeddings():
    s = Svg("embeddings-voz.svg",1200,660,"Embeddings de voz: comparar segmentos", "Una red compartida transforma diferentes segmentos en vectores de voz. Vectores cercanos se agrupan en hablantes. El plano es un dibujo ilustrativo, no una proyección de datos reales.")
    s.text(32,79,"Queremos reconocer una voz aunque cambien las palabras.",19,MUTED)
    for i,txt in enumerate(["Segmento 1","Segmento 2","Segmento 3","Segmento 4"]):
        y=112+i*82
        s.rect(32,y,196,56,PALE)
        s.text(130,y+35,txt,20,anchor="middle")
        s.line(228,y+28,304,277,arrow=True)
    s.rect(304,182,277,190)
    s.text(442,220,"La misma red",21,NAVY,True,anchor="middle")
    s.text(442,257,"Speaker encoder",21,anchor="middle")
    s.text(442,291,"+ pooling temporal",21,anchor="middle")
    s.text(442,337,"un vector por segmento",17,MUTED,anchor="middle")
    s.line(581,277,647,277,arrow=True)
    for i in range(4):
        y=122+i*84
        s.text(653,y+22,f"e{i+1}",22,NAVY,True)
        for col in range(4):
            color=GREEN if (col+i%2)%3 else NAVY
            s.rect(703+col*17,y,12,35,color,"none",1)
    s.line(781,277,820,277,arrow=True)
    s.line(841,429,1158,429,color=MUTED,arrow=True)
    s.line(841,429,841,115,color=MUTED,arrow=True)
    s.rect(895,124,151,105,MINT,GREEN,20)
    s.rect(992,301,141,108,PALE,NAVY,20)
    for x,y,label,col in [(925,156,"e2",NAVY),(988,194,"e4",NAVY),(1020,334,"e1",NAVY),(1088,375,"e3",NAVY)]:
        s.circle(x,y,7,col)
        s.text(x+13,y+6,label,19,col,True)
    s.text(964,114,"S2",21,NAVY,True,anchor="middle")
    s.text(1062,294,"S1",21,NAVY,True,anchor="middle")
    s.text(1000,471,"Agrupar vectores parecidos",18,NAVY,True,anchor="middle")
    s.rect(32,513,1127,95,PALE)
    s.text(56,550,"Coseno: comparar la dirección de los vectores. Clustering: decidir qué agrupar.",20,NAVY,True)
    s.text(56,584,"S1/S2 son grupos de voz; no dan nombres ni roles por sí solos.",19)
    s.text(32,640,"Plano 2D y colores ilustrativos: no son embeddings reales ni resultados del proyecto.",18,MUTED)
    s.save()


def eend():
    s=Svg("eend.svg",1200,765,"EEND: predecir quién está activo en cada paso", "La red produce actividades por hablante y tiempo, con varias salidas altas para solapamiento. PIT compara permutaciones de los canales para que intercambiar S1 y S2 no sea un error de entrenamiento.")
    s.text(32,79,"End-to-End Neural Diarization: actividades por tiempo, no palabras.",19,MUTED)
    s.rect(32,113,262,110)
    s.text(163,156,"Características",21,NAVY,True,anchor="middle")
    s.text(163,189,"secuencia acústica",19,anchor="middle")
    s.rect(360,113,341,110,MINT)
    s.text(530,151,"Red que procesa la secuencia",18,NAVY,True,anchor="middle")
    s.text(530,188,"BLSTM o Transformer",20,anchor="middle")
    s.rect(767,113,393,110)
    s.text(963,154,"Probabilidades de actividad",20,NAVY,True,anchor="middle")
    s.text(963,189,"por hablante y paso acústico",19,anchor="middle")
    s.line(294,168,360,168,arrow=True)
    s.line(701,168,767,168,arrow=True)
    s.text(32,281,"Ejemplo de salida: oscuro = probabilidad alta",20,NAVY,True)
    left,top,width,height=290,314,112,62
    activities=[[0,0,1,1,1,0],[1,1,1,0,0,0]]
    for i,row in enumerate(activities):
        s.text(167,top+i*height+39,f"Salida S{i+1}",20,NAVY,True)
        for j,active in enumerate(row):
            s.rect(left+j*width,top+i*height,width-5,height-5,NAVY if active else PALE,"#dce5e9",2)
    for j in range(6):
        s.text(left+j*width+54,top-16,f"t{j+1}",18,MUTED,anchor="middle")
    s.line(left+2*width+54,446,left+2*width+54,470,color=NAVY)
    s.text(left+2*width+54,496,"Solapamiento: dos voces activas",17,NAVY,True,anchor="middle")
    s.text(left+5*width+54,471,"Sin habla",17,MUTED,anchor="middle")
    s.line(32,522,1160,522,color="#dce5e9")
    s.text(32,562,"PIT: los nombres de las salidas no tienen por qué coincidir con la referencia",21,NAVY,True)
    s.rect(32,589,539,94,PALE)
    s.text(54,626,"Comparar S1 con A y S2 con B",20)
    s.text(54,661,"Calcular el error de toda la secuencia.",18,MUTED)
    s.rect(611,589,549,94,MINT)
    s.text(633,626,"Comparar S1 con B y S2 con A",20)
    s.text(633,661,"Calcular el error de toda la secuencia.",18,MUTED)
    s.text(32,727,"Entrenar con el menor error entre las correspondencias. No cambiar el mapa en cada frame.",19,NAVY,True)
    s.save()


def export_new_pngs():
    executable=shutil.which("inkscape")
    if executable is None:
        print("Inkscape no está instalado: los SVG están disponibles; PNG sin regenerar.")
        return
    for stem in ("encoders","embeddings-voz","eend"):
        subprocess.run([executable,str(OUT/f"{stem}.svg"),"--export-type=png",f"--export-filename={OUT/f'{stem}.png'}"],check=True,capture_output=True)


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
    for build in (transducer,decoder,metrics,percentiles,ctc,acoustic_encoder,speaker_embeddings,eend,export_new_pngs):
        build()
    print(f"Figuras generadas en {OUT}")
