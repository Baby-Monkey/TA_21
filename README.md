Comenzi executie teste:
behave   -> comanda pentru executia tuturor testelor
behave -f html -o report.html   -> comanda pentru a executa toate testele si a loga raspunsul intr-un raport html
behave -f html -o report.html --tags=smoke,regression  -> comanda pentru executarea testelor din grupurile de smoke si regression

== Setup ==
Din Packages instalam librariile :
- pip install selenium
- pip install behave
- pip install behave-html-formatter

Adaug PLUGINS  - (Settings -> Plugins -> Marketplace)
gherkin  -->> suport pt feature files
ini  -->> pt raport

Structura si fisiere suplimentare
features
pages
steps
behave.ini  -->> suport pentru fișierele .ini, folosite pentru configurări și setări
browser.py  -->> aici definim driverul
environment.py -->> definim contextul. Contine cod ce se executa inainte de toate testele si dupa tote testele (hooks)
               -->> instantiem obiecte pentru toate clasele de paginile noi adaugate

