from PIL import Image
from math import *

image1 = Image.open("iguane.jpg") #Ouverture de l'image initiale.

image1.show()

dimx=image1.size[0] # Récupération des dimensions de l'image
dimy=image1.size[1]

image2 = Image.new ('RGB' , (dimx,dimy),(255,255,255)) # Création d'une image vide.


for  y in range(1,dimy-1) :
    for x in range ( 1, dimx-2):

        rvbCentre = (image1.getpixel((x,y))[0]+image1.getpixel((x,y))[1]+image1.getpixel((x,y))[2])/3 # le pixel central !

        rvbVoisin1= (image1.getpixel((x+1,y-1))[0]+image1.getpixel((x+1,y-1))[1]+image1.getpixel((x+1,y-1))[2])/3 # Les 8 voisins
        rvbVoisin2= (image1.getpixel((x-1,y+1))[0]+image1.getpixel((x-1,y+1))[1]+image1.getpixel((x-1,y+1))[2])/3

        rvbVoisin3= (image1.getpixel((x-1,y-1))[0]+image1.getpixel((x-1,y-1))[1]+image1.getpixel((x-1,y-1))[2])/3
        rvbVoisin4= (image1.getpixel((x+1,y+1))[0]+image1.getpixel((x+1,y+1))[1]+image1.getpixel((x+1,y+1))[2])/3

        rvbVoisin5= (image1.getpixel((x,y-1))[0]+image1.getpixel((x,y-1))[1]+image1.getpixel((x,y-1))[2])/3
        rvbVoisin6= (image1.getpixel((x,y+1))[0]+image1.getpixel((x,y+1))[1]+image1.getpixel((x,y+1))[2])/3
        rvbVoisin7= (image1.getpixel((x-1,y))[0]+image1.getpixel((x-1,y))[1]+image1.getpixel((x-1,y))[2])/3
        rvbVoisin8= (image1.getpixel((x+1,y))[0]+image1.getpixel((x+1,y))[1]+image1.getpixel((x+1,y))[2])/3


        norme = round(sqrt((rvbVoisin1-rvbVoisin2)**2+(rvbVoisin3-rvbVoisin4)**2+(rvbVoisin5-rvbVoisin6)**2+(rvbVoisin7-rvbVoisin8)**2))


        if norme > 55:
            image2.putpixel((x,y),(0,0,0))
        elif 55 >=norme > 120:
            image2.putpixel((x,y),(140,140,140))


image2.show() #Afficher

image2.save("Gris.bmp","bmp") #On sauvegarde la nouvelle image
