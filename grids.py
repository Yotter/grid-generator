import pygame as pg
from pygame.locals import RESIZABLE
pg.init()
pg.display.set_caption('Drag the mouse to create some grids! C to clear, UP or DOWN arrow to change density')

# Constants:
displayW = 1000
displayH = 500
minSize = 50

# Colors:
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
lightGrey = (211,211,211)
darkGrey = (105,105,105)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


# Calculated Constants
clock = pg.time.Clock()
screen = pg.display.set_mode((displayW, displayH), RESIZABLE)

class Grid:
	def __init__(self, initPos):
		self.x0, self.y0 = initPos

	def draw(self, currMousePos=None):

		# Calculations
		if currMousePos != None:
			self.topLeftX = min(self.x0, currMousePos[0])
			self.topLeftY = min(self.y0, currMousePos[1])
			self.width = abs(currMousePos[0] - self.x0)
			self.height = abs(currMousePos[1] - self.y0)
			self.nHorizontal = self.width // minSize
			self.spacingHorizontal = self.width  # default value
			if self.nHorizontal != 0:
				self.spacingHorizontal = self.width / self.nHorizontal
			self.nVertical = self.height // minSize
			self.spacingVertical = self.height # default value
			if self.nVertical != 0:
				self.spacingVertical = self.height / self.nVertical

		# Outer Box
		# pg.draw.rect(screen, blue, (self.topLeftX, self.topLeftY, self.width, self.height), width=3)

		# Horizontal Lines
		for i in range(max(self.nHorizontal + 1, 2)):
			x = self.topLeftX + i * self.spacingHorizontal
			pg.draw.line(screen, black, (x, self.topLeftY), (x, self.topLeftY + self.height), width=3)


		# Vertical Lines
		for i in range(max(self.nVertical + 1, 2)):
			y = self.topLeftY + i * self.spacingVertical
			pg.draw.line(screen, black, (self.topLeftX, y), (self.topLeftX + self.width, y), width=3)



def test_function(x):
	pass

def main():
	global minSize
	screen.fill(white)
	locked = True
	frame = 0
	currentGrid = None
	oldGrids = []
	while locked:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				locked = False
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					locked = False
				elif event.key == pg.K_t:
					test_function(frame)
				elif event.key == pg.K_DOWN:
					minSize = max(1, minSize // 2)
				elif event.key == pg.K_UP:
					minSize = min(512, minSize * 2)
				elif event.key == pg.K_c:
					oldGrids = []
			elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
				pos = pg.mouse.get_pos()
				currentGrid = Grid(pos)
			elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
				oldGrids.append(currentGrid)
				currentGrid = None
		
		screen.fill(white)
		for grid in oldGrids:
			grid.draw()
		if currentGrid != None:
			currentGrid.draw(pg.mouse.get_pos())



		pg.display.update()
		clock.tick(60)
		frame += 1

	pg.quit()

main()