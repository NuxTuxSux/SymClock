

General = {
	'width'		: 630,
	'height'	: 600,
	'background': (8,20,40),
	'drawOrder'	: ['penthagon','triangle','ball1','ball2','ball3','ball4']
}


# Triangle
Decaminutes = {
	# the size of the square area with respect to the window width (in percentage)
	'size'		: 31.75,

	# where to draw the triangle
	'position'	:	(35, 45.24),

	# an offset initial integer rotation
	'offset'	:	0,

	# the percentage of the border (100 draws a full triangle)
	'border'	:	100,

	# the colors of the vertices
	1 : (255, 0, 0),
	2 : (0, 255, 0),
	3 : (0, 0, 255)
}

# Penthagon
Minutes = {
	# the size of the square area with respect to the window width (in percentage)
	'size'		: 68.25,

	# where to draw the penthagon
	'position'	:	(16.67, 26.98),

	# an offset initial integer rotation
	'offset'	:	0,
	
	# the percentage of the border (100 draws a full penthagon)
	'border'	:	25,

	# the colors of the vertices
	1 : (204,255,0),
	2 : (127,66,51),
	3 : (64,120,211),
	4 : (238,47,127),
	5 : (237,2,11)
}


Hours = [
# sarebbe piu' preciso mettere i colori a parte. Ne vale la pena?
# size is  in percentage with respect to the window width
		
	{ # First ball
	
		'size'		: 15.87,
		'position'	: (16.66, 17.46),
		'color'		: (0, 0, 32)
	},
    { # Second ball	
	
		'size'		: 15.87,
		'position'	: (35, 7.94),
		'color'		: (0, 0, 64)
	},
	{ # Third ball
	
		'size'		: 15.87,
		'position'	: (53.33, 7.94),
		'color'		: (0, 0, 96)
	},
	{ # Fourth ball
	
		'size'		: 15.87,
		'position'	: (71.67, 17.46),
		'color'		: (0, 0, 128)
	}
]

#	verrebbe piu' elegante un file di configurazione con classi? Penso proprio di si'