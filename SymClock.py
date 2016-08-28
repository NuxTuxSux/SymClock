import pygame, math, time, sys
import settings

from layout import Layout
from polygon import *
from balls import *

#	Fare hash di settings ;)


class Clock:

	def __init__(self, hours, decamins, mins):
		self.hours = hours
		self.decamins = decamins
		self.mins = mins
	def display_time(self):
		h, m = time.localtime()[3:5]
		self.hours.change_state(h)
		self.decamins.change_state(m / 10)
		self.mins.change_state(m % 10)
	def test_time(self,h,m):
		self.hours.change_state(h)
		self.decamins.change_state(m / 10)
		self.mins.change_state(m % 10)		



def surf2html(surface, form = 'png'):
	from PIL import Image
	from StringIO import StringIO
	import base64	
	def surf2base64(surf, frm):
		strCode = pygame.image.tostring(surf,'RGBA')
		#pilImage = Image.frombuffer('RGBA',surf.get_size(),strCode)
		pilImage = Image.frombuffer('RGBA', surf.get_size(), strCode, 'raw', 'RGBA', 0, 1)
		outMemFile = StringIO()
		pilImage.save(outMemFile,frm)
		outMemFile.seek(0)
		return base64.b64encode(outMemFile.read())

	res = "<!DOCTYPE html><html><head><title>Display Image</title></head><body bgcolor=#"
	res += color2hex(settings.General['background'])
	res += "><center><img style='display:block;'id='base64image'src='data:image/jpg;base64,"
	res += surf2base64(surface,form)
	res += "'/></center></body>"
	return res

def color2hex(rgb):
	def d2h(n):
		digits = map(str,range(10))+['A','B','C','D','E','F']
		return digits[n/16] + digits[n%16]
	return d2h(rgb[0]) + d2h(rgb[1]) + d2h(rgb[2])

if __name__ == "__main__":
	pygame.init()
	size = settings.General['width'], settings.General['height']
	
	args = sys.argv[1:]
	if args:
		screen = pygame.Surface(size)
	else:
		screen = pygame.display.set_mode(size)
	
	l=Layout(screen)
	c = Clock(l.balls, l.triangle, l.penthagon)
	if not args:
		while True:
			c.display_time()
			l.draw()
			time.sleep(20)
	else:
		if len(args) > 1:
			filename = args[1]
		else:
			h, m = time.localtime()[3:5]
			filename = str(h) + '.' + str(m)
		c.display_time()
		l.draw()
		if args[0] == 'img':
			pygame.image.save(l.screen,filename + '.png')
		elif args[0] == 'html':
			open(filename + '.html','w').write(surf2html(l.screen))
		elif args[0] == 'web':
			import Server
			Server.publishPage(surf2html(l.screen))

	



# non mi piace molto l'organizzazione, meglio da clock aggiungere gli elementi al layout forse



