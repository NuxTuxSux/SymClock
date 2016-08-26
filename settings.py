

General = {
	'width'		: 630,
	'height'	: 600,
	'background': (200,220,248),
	'drawOrder'	: ['penthagon','triangle','ball1','ball2','ball3','ball4']
}


# Triangle
Decaminutes = {
	# the size of the square area with respect to the window width (in percentage)
	'size'		: 26,

	# where to draw the triangle
	'position'	:	(50, 46),

	# an offset initial integer rotation
	'offset'	:	0,

	# the percentage of the border (100 draws a full triangle)
	'border'	:	100,

	# the colors of the vertices
	1 : (185, 16, 49),
	2 : (36, 29, 133),
	3 : (93, 24, 130),

	# where to save the precalculated image for faster loading
	'image'		:	'triangolo'
}

# Penthagon
Minutes = {
	# the size of the square area with respect to the window width (in percentage)
	'size'		: 70,

	# where to draw the penthagon
	'position'	:	(50, 50),

	# an offset initial integer rotation
	'offset'	:	0,
	
	# the percentage of the border (100 draws a full penthagon)
	'border'	:	25,

	# the colors of the vertices
	1 : (89,139,114),
	2 : (237,224,146),
	3 : (242,173,114),
	4 : (215,98,88),
	5 : (140,70,70),

	# where to save the precalculated image for faster loading
	'image'		:	'pentagono'

}


Hours = [
# sarebbe piu' preciso mettere i colori a parte. Ne vale la pena?
# size is  in percentage with respect to the window width
		
	{ # First ball
	
		'size'		: 8,
		'position'	: (36, 51),
		'color'		: (16, 16, 22)
	},
    { # Second ball	
	
		'size'		: 8,
		'position'	: (42, 62),
		'color'		: (47, 47, 55)
	},
	{ # Third ball
	
		'size'		: 8,
		'position'	: (58, 62),
		'color'		: (62, 62, 70)
	},
	{ # Fourth ball
	
		'size'		: 8,
		'position'	: (64, 51),
		'color'		: (129, 129, 138)
	}
]

#	verrebbe piu' elegante un file di configurazione con classi? Penso proprio di si'