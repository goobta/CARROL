all: report

report:
	latex report.tex
	bibtex report.aux
	latex report.tex
	latex report.tex
	pdflatex report.tex

clean:
	rm *.aux *.log *.pdf *.bbl *.dvi *.blg 
