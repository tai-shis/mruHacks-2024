import pygame
import gameplayerclass
import time
import ball
import block
import math
import goal

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class GamePlayer:
	
	def __init__(self, timeLimit : int):
		pygame.init()
		pygame.font.init() 

	
		self.screenDim = (500,500)
		self.screen = pygame.display.set_mode(self.screenDim)
		self.background = (255,255,255)
		self.running = False
		
		self.ballGroup = pygame.sprite.Group()
		self.blockGroup = pygame.sprite.Group()
		self.targetGroup = pygame.sprite.Group()

		self.gobalStartTime = time.time() 
		self.gobalEndTime = time.time() + timeLimit

		self.localStartTime = 0
		self.localEndTime = 0

		self.currentTotalScore = 0

		self.ghostBlock = None
		self.userBlocks = []

		self.currentBall = None
		self.levelCreaterBool = False

		self.currentGoal = None

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

		#text stuff
		self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
		self.golbalTimeText = self.my_font.render(f'Global Time {self.gobalEndTime - self.gobalStartTime}', False, (0, 0, 0))
	
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
					if e.key == pygame.K_BACKSPACE:
						#delete most recent user block
						if self.userBlocks:
							print(self.userBlocks)
							print("Block Deleted")
							self.userBlocks[-1].delete()
	
	def update(self, dt):
		#self.ballGroup.update()
		self.blockGroup.update(dt)
		self.targetGroup.update(dt)
		self.golbalTimeText = self.my_font.render(f'Global Time {round(self.gobalEndTime - time.time())}', False, (240, 240, 240))
		#print(self.gameState)
		if self.gameState == "Tutorial":
			pass
		elif self.gameState == "Create":
			if self.levelCreaterBool == False:
				self.currentBall = ball.Ball((30,30),math.radians(25), self.blockGroup, self.targetGroup)
				self.ballGroup.add(self.currentBall)

				self.currentGoal = goal.Goal((300,300))
				self.targetGroup.add(self.currentGoal)

				self.levelCreaterBool = True
				self.gameState = "Design"

				if not self.blockActive:
					self.blockActive = True
					self.ghostBlock = block.Block((0,0),0)
					self.blockGroup.add(self.ghostBlock)
				
			#Call create Level
			pass
		elif self.gameState == "Design":
			if not self.blockActive:
				self.blockActive = True
				self.ghostBlock = block.Block((0,0),0)
				self.blockGroup.add(self.ghostBlock)
			
			if self.ghostBlock.is_placed:
				self.blockActive = False
				self.userBlocks.append(self.ghostBlock)
				self.ghostBlock = None
		



			#Call create Level
			pass
		elif self.gameState == "Play":
			#Update Level
			#clear ghost blocks
			if self.ghostBlock:
				self.ghostBlock.delete()
			self.ballGroup.update(dt)
			self.blockActive = False

			if self.currentGoal.goal_reached:
				self.gameState = "Next"

			 
			pass
		elif self.gameState == "Next":
			#add points, 
			#clear level
			self.ballGroup.empty()
			self.blockGroup.empty()
			self.targetGroup.empty()

			self.levelCreaterBool = False
			#self.currentTotalScore 
			self.gameState = "Create"
			pass
		elif self.gameState == "End":
			pass
		else:
			#Close game
			pass
		




	def draw(self):
		self.screen.blit(self.golbalTimeText, (0,0))
		self.ballGroup.draw(self.screen)
		self.blockGroup.draw(self.screen)
		self.targetGroup.draw(self.screen)
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
	main = GamePlayer(180)
	print("starting...")
	main.run()
	print("shuting down...")
        
    