Calcola l'indice di Gulpease con un comando!

Requisiti:
	Si usano un file .pl (perl) e uno .sh (bash, ovvero riga di comando di linux).
	Per poterli usare serve:
		avere installato perl nel proprio sistema (si verifica col comando "perl -v" nel terminale);
		usare il terminale linux.

Come fare:
	1) Porre su una stessa cartella (va bene una qualunque) i seguenti file:
		launcher.sh
		gulpeasepdf.pl
		tutti i file pdf di cui si 

	2) Da terminale, spostarsi sulla cartella scelta ed eseguire il launcher digitando: 
		./launcher.sh

	In output sul terminale appaiono i nomi dei pdf e l'indice di gulpease

Attenzione:
	- i nomi dei -pdf non devono contenere spazi
	- funzionano i -pdf che scriviamo con latex, ma non tutti i .pdf vengono riconosciuti,
		ad esempio quelli ottenuti tramite scan
