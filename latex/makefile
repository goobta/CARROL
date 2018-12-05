all: report

report:
	pdflatex report.tex
	bibtex report.aux
	pdflatex report.tex
	pdflatex report.tex

clean:
	rm *.aux *.log *.pdf *.bbl *.dvi *.blg 
