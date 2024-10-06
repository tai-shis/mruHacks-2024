import pygame
import gameplayerclass
import time
import ball
import block
import math

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class GamePlayer:
	
	def __init__(self, timeLimit : int):
		pygame.init()
	
	
		self.screenDim = (500,500)
		self.screen = pygame.display.set_mode(self.screenDim)
		self.background = (255,255,255)
		self.running = False
		
		self.ballGroup = pygame.sprite.Group()
		self.blockGroup = pygame.sprite.Group()
		self.blockTarget = pygame.sprite.Group()

		self.gobalStartTime = time.time() 
		self.gobalEndTime = time.time() + timeLimit

		self.localStartTime = 0
		self.localEndTime = 0

		self.currentTotalScore = 0

		self.ghostBlock = None
		self.userBlocks = []

		self.currentBall = None
		self.levelCreaterBool = False

		self.blockActive = False
		'''
			Tutorial

			CreateLevel
			Design
			Play
			Next

			end

		'''
		self.gameState = "Tutorial"
	
	def levelMaker(self):
		pass

	def poll(self):
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.QUIT:
				self.running = False
			elif e.type == pygame.KEYUP:
				if e.key == pygame.K_ESCAPE:
					self.running = False
			
			if self.gameState == "Tutorial":
				if e.type == pygame.KEYUP:
					self.gameState = "Create"

			if self.gameState == "Design":
				if e.type == pygame.KEYUP:
					if e.key == pygame.K_RETURN:
						self.gameState = "Play"
					if e.key == pygame.K_DELETE:
						#delete most recent user block
						if not self.userBlocks:
							self.userBlocks[-1].kill()
	
	def update(self, dt):
		#self.ballGroup.update()
		self.blockGroup.update(dt)
		self.blockTarget.update(dt)
		print(self.gameState)
		if self.gameState == "Tutorial":
			pass
		elif self.gameState == "Create":
			if self.levelCreaterBool == False:
				self.currentBall = ball.Ball((30,30),math.pi/2, self.blockGroup)
				self.ballGroup.add(self.currentBall)
				self.levelCreaterBool = True
				self.gameState = "Play"
				
			#Call create Level
			pass
		elif self.gameState == "Design":
			if not self.blockActive:
				self.blockActive = True
				self.ghostBlock = block.Block((0,0),0)
				self.blockGroup.add(self.ghostBlock)



			#Call create Level
			pass
		elif self.gameState == "Play":
			#Update Level
			#clear ghost blocks
			self.ballGroup.update(dt)
			 
			pass
		elif self.gameState == "Next":
			#add points, 
			#clear level
			self.levelCreaterBool = False
			self.currentTotalScore 
			pass
		elif self.gameState == "End":
			pass
		else:
			#Close game
			pass
		




	def draw(self):
		self.ballGroup.draw(self.screen)
		self.blockGroup.draw(self.screen)
		self.blockTarget.draw(self.screen)
		pass
	


	def end(self):
		self.running = False
		
	def run(self):
		
		self.running = True
		clock = pygame.time.Clock()
		while self.running:
			dt = clock.tick(40) / 1000.0
			
			self.screen.fill(self.background)
			
			self.poll()
			self.update(dt)
			self.draw()
			
			pygame.display.flip()

if __name__ == '__main__':
	main = GamePlayer(10)
	print("starting...")
	main.run()
	print("shuting down...")
        
    