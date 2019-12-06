#Finding all Perrin Numbers

def p(n):

	if n>35:
		return round(1.324717957244746025961**n) 

	if (n==0):
		return 3
	if (n==1):
		return 0
	if (n==2):
		return 	2

	return p(n-2) + p(n-3)


