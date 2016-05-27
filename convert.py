def convert(well):
	r	= well[0]
	c	= int(well[1:])
	if r in 'ACEGIKMO':
		p	= 1
		r	= 'ABCDEFGH'['ACEGIKMO'.index(r)]
	elif r in 'BDFHJLNP':
		p	= 2
		r	= 'ABCDEFGH'['BDFHJLNP'.index(r)]
	if c in [1,3,5,7,9,11,13,15,17,19,21,23]:
		c	= str((c+1)/2)
	elif c in [2,4,6,8,10,12,14,16,18,20,22,24]:
		p	= p+2
		c	= str(c/2)
	return p,r+c
