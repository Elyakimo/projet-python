import random
nombre = random.randint(1, 100)
print("Bienvenue dans le jeu du nombre mystère !")
print("Je vais penser à un nombre entre 1 et 100. Essayez de le deviner.")
demande = input("Voulez vous jouer ? (oui/non) ")
tentative = 0
if demande == "oui"or demande == "Oui"or demande == "OUI":
    print("Super ! Commençons le jeu.")
    while True and tentative<8:
        nb_choisi = int(input("Entrez votre nombre : "))
        if nb_choisi < nombre:
            print("C'est plus grand !")
        elif nb_choisi > nombre:
            print("C'est plus petit !")
        else:
            print("longin un fou trouvez le nombre en", tentative, "tentatives ! t'appel pas myamoto musashi")
        tentative += 1
    if tentative == 5:
        print("Xraa t'es nul largue arrête de jouer", nombre)
else:
    print("nass chiez de pas vouloir jouer ceb salez ropass")
