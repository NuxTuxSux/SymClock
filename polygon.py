# memorizzare le immagini disegnate in modo da non ridisegnarle

import pygame,math

class Polygon:		# fare in modo che la simmetria del triangolo sia quella giusta

	def __init__(self, surface, colors, offset, border):
		self.n = len(colors)
		self._w, self._h = surface.get_size()		# comunque e' per superfici quadrate, darlo per assunto?
		self.state = False, 0						# (i,j)   i = True,False per la simmetria, j = 0,...,n-1 per la rotazione
		self.surface = surface
		alpha = math.pi * 2 / self.n
		r=self._w/2
		vertices = [(r+r*math.cos((i + offset * .5)*alpha-math.pi/(2*self.n)),r+r*math.sin((i + offset * .5)*alpha-math.pi/(2*self.n))) for i in range(-1,self.n-1)] #per il pentagono -1,4
		self.figures = []
		for i in range(self.n):
			s = pygame.Surface(surface.get_size(),flags = pygame.SRCALPHA)
			cols = colors[i%self.n:] + colors[:i%self.n]
			drawPol(vertices,cols,s,border)
			self.figures.append(s)
	
	def change_state(self,info):
		self.state = info>(self.n-1), info%self.n

	def render(self):	# D_10 = R u sR
		s,i = self.state
		self.surface = self.figures[i]
		if s:
			self.surface = pygame.transform.flip(self.surface,True,False)



def drawPol(ps, colors, surface, border):	# funziona meglio per poligoni regolari
	n = len(ps)
	xc, yc = 0, 0
	for p in ps:
		xc += p[0]
		yc += p[1]
	xc /= n
	yc /= n
	qs = []
	for p in ps:
		qs.append((xc + (p[0] - xc) * (100-border) / 100., yc + (p[1] - yc) * (100-border) /100.))
	
	def color(i,j):
		r,g,b = 0,0,0
		ws = weights((i,j),ps,side)
		for i in range(len(ws)):
			r += ws[i] * colors[i][0]
			g += ws[i] * colors[i][1]
			b += ws[i] * colors[i][2]
		return pygame.Color(int(r),int(g),int(b))

	def weights(p,ps,side):
		def weight(q):
			d = math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
			return max(0,side-d)
		ws = [weight(q) for q in ps]
		total = sum(ws)
		return [w/total for w in ws]

	def inside(q,ps):
		def angle(p,q,r):
			def arg(x,y):
				if (x,y)==(0,0):
					return 0
				else:
					return math.copysign(math.acos(x/math.sqrt(x*x+y*y)),y)

			a=arg(r[0]-q[0],r[1]-q[1])-arg(p[0]-q[0],p[1]-q[1])
			if a>math.pi:
				a-=2*math.pi
			if a<-math.pi:
				a+=2*math.pi
			return a
		thetas = [angle(p1,q,p2) for p1,p2 in zip(ps,ps[1:]+[ps[0]])]
		return all(x>=0 for x in thetas)
	
	side = math.sqrt((ps[0][0]-ps[1][0])**2+(ps[0][1]-ps[1][1])**2)
	x,X=int(min(x for x,y in ps)),int(max(x for x,y in ps))
	y,Y=int(min(y for x,y in ps)),int(max(y for x,y in ps))
	
	
	for i in range(x,X+1):
		for j in range(y,Y+1):
			if inside((i,j),ps) and (border == 100 or not inside((i,j),qs)):
				surface.set_at((i,j),color(i,j))
