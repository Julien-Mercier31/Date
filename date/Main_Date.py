
import Verification as v
y = "y"
while y =="y":
	print ("Donner une date, Nous vous dirons si elle est correcte ou non")
	print ("Donner l'année.")
	année 	= int (input ())
	print ("Donner le mois en nombre.")
	mois  	= int (input ())
	print ("Donner le jour en nombre.")
	jour	= int (input())
	valid 	= v.verification (jour,mois,année)
	if valid :
		print ("La Date est correcte")
	else:
		print ("La date est incorecte")
	print ("pour continuer taper sur y.")
	y = input()
