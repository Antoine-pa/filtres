from PIL import Image
import os

def traitement (triplet): # La fonction qui réalise le traitement des couleurs 'inversion

    ancienRouge=triplet[0]
    ancienVert=triplet[1]
    ancienBleu=triplet[2]


    nouveauRouge=int((ancienRouge+ancienVert+ancienBleu)/4)
    nouveauVert=int((ancienRouge+ancienVert+ancienBleu)/4)
    nouveauBleu=int((ancienRouge+ancienVert+ancienBleu)/4)


    return(nouveauRouge,nouveauVert,nouveauBleu)


# Programme Principal

imageDebut = Image.open("warhol.bmp") #Ouverture de l'image initiale.

imageDebut.show() #Affichage de cette image.

dimx = imageDebut.size[0]  #Récupération de ses dimensions.
dimy = imageDebut.size[1]

imageModifiee = Image.new('RGB', (dimx,dimy),(255,255,255)) # Création de l'image de sortie

for i in range(0,dimx,1):
    for j in range(0,dimy,1):
        rvb=imageDebut.getpixel((i,j)) # On récupère le triplet des 3 composantes
        rvbmodifie=traitement(rvb) # On inverse ce triplet.
        imageModifiee.putpixel((i,j),(rvbmodifie[0],rvbmodifie[1],rvbmodifie[2]))

imageModifiee.save("warholModifie_bleu.bmp", "bmp") # On enregistre l'image finale

imageModifiee.show()

imageDebut.close()

imageModifiee.close()


