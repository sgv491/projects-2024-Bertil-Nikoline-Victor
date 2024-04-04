# Data analysis project

Our project is titled **PROJECT TITLE** and is about EXPLAIN.

The **results** of the project can be seen from running [dataproject.ipynb](dataproject.ipynb).

We apply the **following datasets**:

1. dataX.csv (*source*) 
1. dataY.csv (*source*)

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:

``pip install matplotlib-venn``

# Idéer til projektstruktur
Mål: Målet med projektet er at vise, hvordan sammenhængen mellem inflation og arbejdsløshed har udviklet sig over tid i USA og Danmark og sammenligne denne sammenhæng med Philips-kurvens teoretiske sammenhæng. I projektet vil vi bruge data fra FRED (St. Louis Fed) og Danmarks Statistik, som vil importeres vha. API'er.

Strukturen vil være som følger:
1) Benytte API'er til at importere data fra FRED og Danmarks Statistik og rense denne til at vise årlig inflation og årlig arbejdsløshed (gns. af 12 måneder)
2) Illustrere udviklingen i inflation og arbejdsløshed over tid i de to lande.
3) Illustrere den empiriske Philips-kurve for USA startende i 1960'erne inkl. regressionskurve-fit (eksponentiel aftagende)
4) Udvide disse illustrationer for flere årtier frem i tiden
5) Generere et interaktivt plot (widget) for USA, hvor man kan vælge rullende årtier, hvorfra den empiriske Philips-kurve illustreres
6) Sammenligningsplot mellem USA og DK's empiriske Philips-kurve i et bestemt årti (evt. som widget med flere årtier, hvis muligt)


Tilføjelser:
1) Delkonklusioner
2) Spørgende opgave - stil spørgsmål og besvar åbent løbende
3) Konklusion der ikke er for konkluderende men mere opsummerende over hvad vi har set
4) Tilføj doc-strings for helper filer
5) bertils samlede graf skal med ind
6) Nedslag i perioder, både kort beskrevet, og 3 grafer man går mere ned i