while True: #pokreni beskonačnu petlju za upis
    try:
        visina = int(input("Enter height (1-8):")) #upis broja 1 do 8
        if visina<0 or visina>8:
            print("Enter whole number between 1 and 8!")
            continue #pogrešan upis pravog tipa, vrati se na upis
        else:
            break #ispravan upis, izađi iz petlje
    except:
        print("Wrong input type! Please use integer 1 to 8") #Pogrešan tip upisan, vrati se na upis
znak = "#" #tijelo piramide
uvlaka = visina-1 #početna uvlaka, ukupna visina minus 1 jer zadnji red nema uvlake
broj=1 #brojač redova, za svaki red dodaje po 1 znak
while visina>0 : #početak petlje iscrtavanja piramide
    print(visina," "* uvlaka, znak*broj, " ", znak*broj) #ispis piramide
    visina = visina -1 #smanji visinu
    uvlaka = uvlaka-1 #smanji uvlaku
    broj=broj+1 #povečaj broj reda