#Tic-Tac-Toe

spiel_aktiv = True
spielfeld = [" ","1","2","3","4","5","6","7","8","9"]
spieler_aktuell = 'O'

print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )

gewonnen_spieler_x = 0
gewonnen_spieler_o = 0

def reset_gewinne():
    global gewonnen_spieler_x
    global gewonnen_spieler_o
    gewonnen_spieler_x = 0
    gewonnen_spieler_o = 0

while spiel_aktiv:

    def spielfeld_ausgeben():
        print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
        print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
        print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )

    def spieler_eingabe():
        global spiel_aktiv
        while True:
            spielzug = input("Bitte Feld eingeben: ")

            if spielzug == 'q':
                spiel_aktiv = False
                return
        
            try:
                spielzug = int(spielzug)
            except ValueError:
                print("\nBitte Zahl von 1 bis 9 eingeben\n")
            else:
                if spielzug >= 1 and spielzug <= 9:
                    if spielfeld[spielzug] == 'X' or spielfeld[spielzug] == 'O':
                        print("\nDas Feld ist bereits belegt - ein anderes wählen!\n")
                    else:
                        return spielzug
                else:
                    print("\nZahl muss zwischen 1 und 9 liegen\n")

    def spieler_wechseln():
        global spieler_aktuell
        if spieler_aktuell == 'X':
            spieler_aktuell = 'O'
            
        else:
            spieler_aktuell = 'X'

    def kontrolle_gewonnen():
    #Reihen
        if spielfeld[1] == spielfeld[2] == spielfeld[3]:
            return spielfeld[1]
        if spielfeld[4] == spielfeld[5] == spielfeld[6]:
            return spielfeld[4]
        if spielfeld[7] == spielfeld[8] == spielfeld[9]:
            return spielfeld[7]
    #Spalten
        if spielfeld[1] == spielfeld[4] == spielfeld[7]:
            return spielfeld[1]
        if spielfeld[2] == spielfeld[5] == spielfeld[8]:
            return spielfeld[2]
        if spielfeld[3] == spielfeld[6] == spielfeld[9]:
            return spielfeld[3]
    #Diagonal
        if spielfeld[1] == spielfeld[5] == spielfeld[9]:
            return spielfeld[5]
        if spielfeld[7] == spielfeld[5] == spielfeld[3]:
            return spielfeld[5]

    def kontrolle_auf_unentschieden():
        if (spielfeld[1] == 'X' or spielfeld[1] == 'O') \
            and (spielfeld[2] == 'X' or spielfeld[2] == 'O') \
            and (spielfeld[3] == 'X' or spielfeld[3] == 'O') \
            and (spielfeld[4] == 'X' or spielfeld[4] == 'O') \
            and (spielfeld[5] == 'X' or spielfeld[5] == 'O') \
            and (spielfeld[6] == 'X' or spielfeld[6] == 'O') \
            and (spielfeld[7] == 'X' or spielfeld[7] == 'O') \
            and (spielfeld[8] == 'X' or spielfeld[8] == 'O') \
            and (spielfeld[9] == 'X' or spielfeld[9] == 'O'):
            return ('unentschieden')

    spielzug = spieler_eingabe()
    print("\nSpielzug: " + str(spielzug), "\n")
    if spielzug:
        spielfeld[spielzug] = 'X'
    
        spielfeld_ausgeben()

    while spiel_aktiv:
        print ("\nSpieler " + spieler_aktuell + " am Zug\n")
        spielzug = spieler_eingabe()

        spielfeld_KI = []
        for moegliche_felder in spielfeld:
            if moegliche_felder != 'X' and moegliche_felder != '0' and moegliche_felder != '':
                spielfeld_KI += moegliche_felder

        if spielzug:
            spielfeld[spielzug] = spieler_aktuell
            spielfeld_ausgeben()
            
            gewonnen = kontrolle_gewonnen()
            if gewonnen:
                print ("\nSpieler " + gewonnen + " hat gewonnen!\n")
                if gewonnen == "X":
                    gewonnen_spieler_x + 1
                elif gewonnen == "O":
                    gewonnen_spieler_o + 1
                spiel_aktiv = False
                break
            
            unentschieden = kontrolle_auf_unentschieden()
            if unentschieden:
                print ("\nSpiel ist unentschieden ausgegangen\n")
                spiel_aktiv = False
            
            spieler_wechseln()
#print("Spieler X hat ", gewonnen_spieler_x, " mal gewonnen.\nSpieler o hat", gewonnen_spieler_o, " mal gewonnen.\n")

print()