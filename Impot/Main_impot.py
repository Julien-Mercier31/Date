
import mesImpot as mi
y = "y"
while y =="y":
	print ("Donner nous votre salaire nous vous dirons combien d'impot vous paierez")
	print ("Donner votre salaire.")
	salaire 	= int (input ())
	impot = mi.mesImpot(salaire)

	if impot != False :
		print ("avec votre salaire vous paierez ", impot, "e")
	else :
		print("salaire faux")
	print ("pour continuer taper sur y.")
	y = input()
