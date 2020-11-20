import Bysextile as b
import mois as m

def verification (jour,mois,année):
	jomo = m.mois(mois,année)
	if jomo != False :
		if jour <= jomo and jour > 0  :
			return True
	else :
		return False