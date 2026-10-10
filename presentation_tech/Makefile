.PHONY: all clean previews
all:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
previews: all
	mkdir -p build/previews
	pdftoppm -jpeg -r 85 build/main.pdf build/previews/slide >/dev/null 2>&1
clean:
	latexmk -C -outdir=build main.tex
