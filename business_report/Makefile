.PHONY: all appendices clean
all:
	latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex
appendices:
	python3 scripts/sync_market_appendices.py
clean:
	latexmk -c -outdir=build main.tex
