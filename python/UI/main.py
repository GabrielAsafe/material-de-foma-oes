import cv2
import os
from PrepareFace import *



prepare()

PATH = os.getcwd()
BACK_GROUND_IMAGE = PATH +'/car.jpg'
OLHO = PATH +'/olho.jpg'
NARIZ = PATH +'/nariz.jpg'
BOCA = PATH +'/boca.jpg'


background_image = cv2.imread(BACK_GROUND_IMAGE)
R_olho = cv2.imread(OLHO, cv2.IMREAD_UNCHANGED)
L_olho = cv2.flip(R_olho,1)
nariz = cv2.imread(NARIZ, cv2.IMREAD_UNCHANGED)
boca = cv2.imread(BOCA, cv2.IMREAD_UNCHANGED)

alpha_channel = 1

X0Y0 = ((140,160), (406,160), (229,170), (128,222))#posição das partes da frente do carro | farol r ; farol , nariz e boca

X1Y1= ((73, 40),(73, 40),(156,78),(348,45))#tamanho final das partes do corpo| olho r ; olho , nariz e boca

"""
Ordem imagem vai ser o tamanho do vetor X0Y0, que vai de 0 à 3
"""
def makeOperation(parteDoCorpo, tamanhoFinalImagem,ordemImagem):


    resized_image = cv2.resize(parteDoCorpo, tamanhoFinalImagem)
    roi = background_image[X0Y0[ordemImagem][1]:X0Y0[ordemImagem][1] + resized_image.shape[0], X0Y0[ordemImagem][0]:X0Y0[ordemImagem][0] + resized_image.shape[1]]
    result = cv2.addWeighted(roi, 1 - alpha_channel, resized_image, alpha_channel, 0)
    background_image[X0Y0[ordemImagem][1]:X0Y0[ordemImagem][1] + resized_image.shape[0], X0Y0[ordemImagem][0]:X0Y0[ordemImagem][0] + resized_image.shape[1]] = result






def main():
   

    makeOperation(R_olho,X1Y1[0],0)
    makeOperation(L_olho,X1Y1[1],1)
    makeOperation(nariz,X1Y1[2],2)
    makeOperation(boca,X1Y1[3],3)

    cv2.imshow('Pasted Image', background_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()






# Save the resized image
#cv2.imwrite('path/to/save/resized_image.jpg', resized_image)

# Alternatively, you can overwrite the original image with the resized one
# cv2.imwrite(image_path, resized_image)
