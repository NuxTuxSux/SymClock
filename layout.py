import pygame
import settings
from balls import Ball,Balls
from polygon import Polygon


class Layout:
	def __init__(self,scr):
		self.screen = scr
		self.Width, self.Height = scr.get_size()
		objs = {}

		balls = []
		for bSettings in settings.Hours:
			size = bSettings['size']*self.Width/100.
			surfBall = pygame.Surface((size,size),flags = pygame.SRCALPHA)
			b = Ball(surfBall)
			balls.append(b)
			pos = bSettings['position'][0] * self.Width / 100., bSettings['position'][1] * self.Width / 100.
			objs['ball' + str(len(balls))] = b, pos
		self.balls = Balls(balls[0],balls[1],balls[2],balls[3])

		pSettings = settings.Minutes
		size = pSettings['size']*self.Width/100.
		surfPent = pygame.Surface((size,size),flags = pygame.SRCALPHA)
		border = pSettings['border']
		self.penthagon = Polygon(surfPent,[pSettings[1],pSettings[2],pSettings[3],pSettings[4],pSettings[5]],pSettings['offset'],border,'penthagon')
		pos = pSettings['position'][0] * self.Width / 100., pSettings['position'][1] * self.Width / 100.
		objs['penthagon'] = self.penthagon, pos

		tSettings = settings.Decaminutes
		size = tSettings['size']*self.Width/100.
		surfTriang = pygame.Surface((size,size), flags = pygame.SRCALPHA)
		border = tSettings['border']
		self.triangle = Polygon(surfTriang,[tSettings[1],tSettings[2],tSettings[3]],tSettings['offset'],border,'triangle')
		pos = tSettings['position'][0] * self.Width / 100., tSettings['position'][1] * self.Width / 100.
		objs['triangle'] = self.triangle, pos

		self.objects = objs


	def draw(self):
		r,g,b = settings.General['background']
		self.screen.fill(pygame.Color(r,g,b))
	
		for objName in settings.General['drawOrder']:
			obj, (x,y) = self.objects[objName]
			obj.render()
			w, h = obj.surface.get_size()
			self.screen.blit(obj.surface,(x - w * .5, y - h * .5))
		pygame.display.flip()

