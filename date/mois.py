import Bysextile as b

def mois (mois,année):
	if mois > 12 or mois<1   :
		print ("le mois est mauvais")
		return False
	elif mois < 8:
		if (mois%2) == 1 :
			return 31
		elif mois == 2:
			if (b.Bysextile(année)):
				return 29
			else: 
				return 28
		else:
			return 30
	elif (mois%2) == 0:
		return 31
	else:
		return 30  
