from PIL import Image

nom_fichier = "cosmonaute.bmp"
imageDebut = Image.open(nom_fichier) #Ouverture de l'image initiale.

#imageDebut.show() # On affiche l'image initiale

Taillex = 265
Tailley = 190


nouvelleImage = Image.new('RGB', (Taillex,Tailley),(255,255,255)) # Création de l'image de sortie

for x in range(0,Taillex, 1):
    for y in range(0,Tailley, 1):


        RVB=imageDebut.getpixel((x,y)) # On récupère le triplet des 3 composantes




        NEW_RVB = {"R" : int(255-RVB[0]*1.5), "V" : int(255-RVB[1]*1.5), "B" : int(255-RVB[2]*1.5)}
        for a in NEW_RVB.items():
            if a[1] > 255:
                NEW_RVB[a[0]] = 255
            elif a[1] < 0:
                NEW_RVB[a[0]] = 0


        nouvelleImage.putpixel((x,y),(NEW_RVB.get("R"), NEW_RVB.get("V"), NEW_RVB.get("B")))



nouvelleImage.save("cosmonauteInverse22.bmp", "bmp") # On enregistre l'image finale

nouvelleImage.show()

imageDebut.close()

nouvelleImage.close()


