import os
import sys
import csv

def getFirstLetter(s):
    return s[0].capitalize()


def listaPresenti():
    lista=[]
    with open('../pages/presenti.txt', 'r') as presenti:
        lista = presenti.read().splitlines()
    return lista


def aggiungiVoce(titolo, descrizione):

    presenti = listaPresenti()

    if len(str(titolo)) == 0:
        print("--- Errore: titolo vuoto ---")
        exit()

    if titolo == 'q':
        print('End')
        exit()
    if str(titolo).lower() in presenti:
        print('--- Errore, termine '+titolo+' già presente ---')
        exit()
    if titolo[0].capitalize() not in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        print('--- Shit, non abbiamo considerato le eventuali parole che '
              'cominciano con cose diverse da una lettera, sorry ---')
        exit()

        # metto la capitol letter
    if len(titolo) > 1:
        titolo = titolo[0].capitalize()+titolo[1:]
    else:
        titolo = titolo.capitalize()
    with open('../pages/'+getFirstLetter(titolo)+'.tex', 'a') as file:
        if os.stat('../pages/'+getFirstLetter(titolo)+'.tex').st_size == 0:
            file.write('\subsection*{\\quad$'+getFirstLetter(titolo)+'\\quad$}\n')

        file.write('\subsubsection*{'+titolo+'}\n')
        file.write('\index{' + titolo + '}\n')
        file.write(descrizione+'\n\n')

        with open('../pages/presenti.txt', 'a') as file2:
            file2.write(titolo.lower()+'\n')
            presenti.append(titolo.lower())

        print('--- Aggiunto '+titolo+' ---')


if len(sys.argv) == 1:
    print('Script usage: \n'
          '\t script -a \t\t\t=> inserire a mano \n'
          '\t script -f nomefile.csv \t=> importa glossario da csv')
    exit()

elif len(sys.argv) ==2 and sys.argv[1] == '-a':

    while True:
        print('=> Inserire il nome del NUOVO TERMINE (\'q\' per uscire ):\n')
        titolo = input()
        print('=> inserisci la descrizione ')
        descrizione = input()

        aggiungiVoce(titolo, descrizione)

elif len(sys.argv) ==3 and sys.argv[1] == '-f':
    #lettura e scrittura da file csv

    #resetto presenti
    nuovofile = open('../pages/presenti.txt', 'w')
    for char in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        nuovofile = open('../pages/'+char+'.tex', 'w')
        nuovofile.close()
    nuovofile.close()

    with open(sys.argv[2]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        intestazione = True
        for row in csv_reader:
            if intestazione:
                print('Apertura del documento..')
                intestazione = False
            else:
                if row[1] == "":
                    print(row[0]+' non ha una descrizione! Impossibile proseguire')
                    exit()
                aggiungiVoce(row[0], row[1])

        print('Finito')

else:
    print("comando non riconosciuto")



