def mesImpot (salaire):
	if salaire < 0:
		return False
	elif salaire >156244 :
		impot = (salaire - 156244) * 45/100 + (156244 - 73779)*41/100 + (73779 - 27519)* 30/100 + (27519 - 9964)*14/100
	elif salaire > 73779 :
		impot = (salaire - 73779)*41/100 + (73779 - 27519)* 30/100 + (27519 - 9964)*14/100
	elif salaire > 27519:
		impot = (salaire - 27519)* 30/100 + (27519 - 9964)*14/100
	elif salaire > 9664:
		impot = (salaire - 9964)*14/100
	else:
		impot = 0
	return impot


