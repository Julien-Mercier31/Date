def Bysextile (année):
	if (année%4) == 0:
		if (année%100) == 0:
			if (année%400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False
		

			


