import cv2 as cv
import numpy as np
import sys
import time


pict = int(input("===============SELECT A PHOTO TO USE=========================\n[1]Bakugo\n[2]Himoutou\n[3]Blue eyes\n[4]Locker joke\nAnswer: "))

if (pict == 1):

	pic = "bak.jpg"

elif (pict == 2):

	pic = "derp.jpg"

elif (pict == 3):

	pic = "eyes.jpg"

elif (pict == 4):

	pic = "locker.jpg"

else:


	print("IT WAS STATED TO INPUT 1 - 4 ONLY! PLEASE REEEEEEEEEEAD")
	exit()
ch = cv.imread(pic)
img=cv.imread(pic)
choys = int(input("===============CHOOSE OPTION=========================\n[1]Default Image\n[2]Choose a Color\nAnswer: "))

if (choys == 1):
	cv.imshow("Default title",img)
	cv.waitKey(0)
	cv.destroyAllWindows()
	exit()

if (choys == 2):

	colo = int(input("===============SELECT A COLOR===============\n[1]COLORED(Transparency are neglected/DEFAULT)\n[2]UNCHANGED\n[3]GRAYSCALE(UNAVAILABLE)\nAnswer: "))
	if (colo == 1):
		c = 1
	elif (colo == 2):
		c = -1
	elif (colo == 3):
		print("PLEASE READ! WE JUST SAID IT WAS UNAVAILABLE!")
		exit()
	else:
		print("1 - 3 ONLY! SAYONARA!")
		exit()

else:
	print("Invalid")
	exit()

t = str(input("Enter title: "))
img = cv.imread(pic,c)
cv.imshow(t,img)
cv.waitKey(0)
cv.destroyAllWindows()

x = int(input("===============THAT IS ALL! ARIGATOOOOU===============\n[1]OK! BYE!\n[2]CHOTTO MATTE KUDASAI! I HAVE SOMTHING TO DO!\nAnswer: "))
	
if (x==1):
	print("SAYONARA~")
	exit()
elif (x==2):
	num = 1
	while num < 2 :
		q = int (input("===============WHAT MORE DO YOU WANT TO DO?===============\n[1]CHECK D-TYPE\n[2]CHECK SIZE SIZE PROPERTY\n[3]SHAPE\n[4]MODIFY A PIXEL\n[5]SET DIMENSION\n[6]EXIT\nAnswer: "))
		if (q == 1):
			print("The data type of image is: ",img.dtype,"\nloading...")
			time.sleep(2)
		elif (q == 2):
			print("The size property of the image is ",img.size,"\nloading...")
			time.sleep(2)
		elif (q == 3):
			print("The shape of image is: ",img.shape,"\nloading...")
			time.sleep(2)
		elif (q == 4):
			print("===============CURRENTLY MODIFYING PIXEL===============\nMax Pixel count: ",img.shape,"\nNOTE: YOU CANNOT BE EQUAL TO THE MAXIMUM PIXEL\nFORMAT = [row,column,flag]")
			r = int (input("Enter row: "))
			c = int (input("Enter Column: "))
			pixu = img[r,c]
			print ("This is the color value of the pixel: ",pixu)
			pixuch = int(input("*****change value?*****\n[1]YES\n[2]NO\nAnswer: "))
			if (pixuch == 1):
				pixu = img[r,c]
				redo = int(input("Adjust color Red 0-250: "))
				greeno = int(input("Adjust color Green 0-250: "))
				bloo = int(input("Adjust color Blue 0-250: "))
				img.itemset((r,c,0),redo)
				img.itemset((r,c,1),greeno)
				img.itemset((r,c,2),bloo)
				print ("The color of the pixel now: ",pixu)
				time.sleep(3)
				cv.imshow("t",img)
				cv.waitKey(0)
				cv.destroyAllWindows()
		elif (q == 5):
			print("*****SETTING DIMENSION*****\nMax Pixel count: ",img.shape,"\nNOTE: YOU CANNOT BE EQUAL TO THE MAXIMUM PIXEL!\nFormat: [xstart:xend,ystart:yend]")
			xs = int(input("Input X start: "))
			xe = int(input("Input X End: "))
			ys = int(input("Input Y start: "))
			ye = int(input("Input Y End: "))

			roi = img[xs:xe,ys:ye]
			cv.imshow (t,roi)
			cv.waitKey(0)
			cv.destroyAllWindows()
			
		elif (q == 6):
			print("THANKYOU FOR USING MEEE! BYE!")
			exit()
	

else:
	print("Goodbye.")
	exit()
