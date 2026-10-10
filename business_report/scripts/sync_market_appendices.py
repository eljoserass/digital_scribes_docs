#!/usr/bin/env python3
"""Regenera los apéndices LaTeX desde los inventarios Markdown del proyecto.

Solo usa la biblioteca estándar. No modifica las fuentes Markdown ni Zotero.
Los .tex generados se conservan para que el informe compile sin este script.
"""
from pathlib import Path
import re

REPORT=Path(__file__).resolve().parents[1]
ROOT=REPORT/'notes'
OUT=REPORT/'appendices'
CHARS={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}',
       '≥':r'\ensuremath{\geq}','≤':r'\ensuremath{\leq}','→':r'\ensuremath{\rightarrow}','−':r'\ensuremath{-}','×':r'\ensuremath{\times}','≈':r'\ensuremath{\approx}'}
def escape(s): return ''.join(CHARS.get(c,c) for c in s).replace('/',r'/\allowbreak{}')
def url_escape(s):return s.replace('%',r'\%').replace('#',r'\#').replace('&',r'\&').replace('_',r'\_')
LOCAL={'certificaciones-escribas-digitales.md':'app:proveedores','integraciones-hcis.md':'app:hcis','precios-escribas-digitales.md':'app:precios','analisis-escribas-digitales.md':'sec:candidatos'}
TOKEN=re.compile(r'\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*([^*]+)\*')
def inline(s):
    out=[];last=0
    for m in TOKEN.finditer(s):
        out.append(escape(s[last:m.start()]))
        if m.group(1) is not None:out.append(r'\textbf{'+inline(m.group(1))+'}')
        elif m.group(2) is not None:
            label=inline(m.group(2));url=m.group(3);base=url.split('#')[0]
            if base in LOCAL:out.append(r'\hyperref['+LOCAL[base]+']{'+label+'}')
            elif url.startswith(('executive_report/notes/', 'additional/')):
                out.append(label+' (archivo de notas del proyecto)')
            else:out.append(r'\href{'+url_escape(url)+'}{'+label+'}')
        elif m.group(4) is not None:out.append(r'\texttt{'+escape(m.group(4))+'}')
        else:out.append(r'\emph{'+inline(m.group(5))+'}')
        last=m.end()
    out.append(escape(s[last:]));return ''.join(out)

def table(lines,weights):
    rows=[[c.strip() for c in line.strip().strip('|').split('|')] for line in lines]
    n=len(rows[0]);assert all(len(r)==n for r in rows)
    assert len(weights)==n
    spec=''.join(r'L{\dimexpr '+str(w)+r'\linewidth-2\tabcolsep\relax}' for w in weights)
    output=[r'\begin{longtable}{'+spec+'}',r'\toprule',' & '.join(r'\textbf{'+inline(c)+'}' for c in rows[0])+r' \\',r'\midrule',r'\endfirsthead',' & '.join(r'\textbf{'+inline(c)+'}' for c in rows[0])+r' \\',r'\midrule',r'\endhead',r'\midrule',r'\multicolumn{'+str(n)+r'}{r}{\footnotesize Continúa en la página siguiente}',r'\endfoot',r'\bottomrule',r'\endlastfoot']
    for row in rows[2:]:output.append(' & '.join(inline(c) for c in row)+r' \\')
    output.append(r'\end{longtable}')
    return '\n'.join(output)

def convert(text,mode):
    lines=text.splitlines();result=[];i=0;bullet=False
    while i<len(lines):
        line=lines[i]
        if not line.startswith('- ') and bullet:result.append(r'\end{itemize}');bullet=False
        if line.startswith('# '):i+=1;continue
        if line.startswith('## '):
            h=line[3:];m=re.match(r'(\d+)\.\s*(.*)',h)
            result.append(r'\subsection*{'+inline(h)+'}')
            if m:result.append(r'\label{provider:'+m.group(1)+'}')
        elif line.startswith('|'):
            block=[]
            while i<len(lines) and lines[i].startswith('|'):block.append(lines[i]);i+=1
            n=len(block[0].strip().strip('|').split('|'))
            weights=({2:[.23,.77],3:[.24,.31,.45]} if mode=='cert' else {4:[.18,.08,.48,.26]} if mode=='hcis' else {5:[.15,.20,.36,.10,.19]})[n]
            result.append(table(block,weights));continue
        elif line.startswith('- '):
            if not bullet:result.append(r'\begin{itemize}');bullet=True
            result.append(r'\item '+inline(line[2:]))
        else:result.append(inline(line))
        i+=1
    if bullet:result.append(r'\end{itemize}')
    return '\n'.join(result)

def write(name,title,label,body,landscape=False):
    head='% !TEX root = ../main.tex\n'
    head+='% GENERADO por scripts/sync_market_appendices.py; editar el Markdown de origen.\n'
    head+=r'\clearpage'+'\n'+(r'\begin{landscape}'+'\n' if landscape else '')
    head+=r'\section{'+title+'}\n'+r'\label{'+label+'}\n'+r'\begingroup\footnotesize'+'\n'
    foot='\n'+r'\endgroup'+'\n'+(r'\end{landscape}'+'\n' if landscape else '')
    (OUT/name).write_text(head+body+foot)

def main():
    cert=(ROOT/'certificaciones-escribas-digitales.md').read_text()
    pos=cert.index('## 1. ')
    write('01_certificaciones.tex','Certificaciones y marcos de aseguramiento: alcance y evidencia','app:certificaciones',convert(cert[:pos],'cert'))
    headers=re.findall(r'^## (\d+)\. (.+)$',cert,re.M)
    count=len(headers)
    ids=list(range(1,count+1))
    assert [int(n) for n,_ in headers]==ids,'La numeración debe ser consecutiva.'
    index=['| N.º | Proveedor / producto |','| --- | --- |']+[f'| {n} | {name} |' for n,name in headers]
    index_tex=table(index,[.08,.92])
    body=f'El catálogo comprende {count} proveedores. Las fichas aplican criterios uniformes para distinguir declaraciones comerciales, documentación primaria examinada y limitaciones de la evidencia disponible.\n\n'+index_tex+'\n'+convert(cert[pos:],'cert')
    write('02_proveedores.tex','Catálogo de proveedores y evidencia documental','app:proveedores',body)
    for src,name,title,label,mode in [
        ('integraciones-hcis.md','03_hcis.tex','Interoperabilidad con Dedalus HCIS','app:hcis','hcis'),
        ('precios-escribas-digitales.md','04_precios.tex','Condiciones económicas y transparencia de la facturación','app:precios','price')]:
        source=(ROOT/src).read_text()
        row_ids=[int(n) for n in re.findall(r'^\| (\d+)\. ',source,re.M)]
        assert row_ids==ids,f'{src}: las filas deben coincidir con el catálogo.'
        write(name,title,label,convert(source,mode),landscape=True)
    print(f'Generados: glosario, {count} fichas, {count} integraciones y {count} precios.')

if __name__=='__main__':main()
