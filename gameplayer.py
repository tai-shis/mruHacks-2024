import pygame
import gameplayerclass

class GamePlayer:
	
	def __init__(self, startTime : int):
		pygame.init()
	
	
		self.screenDim = (500,500)
		self.screen = pygame.display.set_mode(self.screenDim)
		self.background = (255,255,255)
		self.running = False
		
		self.ballGroup = pygame.sprite.Group()
		self.blockGroup = pygame.sprite.Group()
		self.blockTarget = pygame.sprite.Group()

		
		'''
			Tutorial

			CreateLevel
			Design
			Play
			Next

			end

		'''
		self.gameState = "Tutorial"
	

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
					self.gameState == "CreateLevel"

			if self.gameState == "Design":
				if e.type == pygame.KEYUP:
					if e.key == pygame.K_RETURN:
						self.gameState == "Play"
					if e.key == pygame.K_DELETE:
						#delete most recent user block
						pass
	
	def update(self, dt):
		self.ballGroup.update()
		self.blockGroup.update()
		self.blockTarget.update()

		if self.gameState == "Tutorial":
			pass
		elif self.gameState == "Create":
			#Call create Level
			pass
		elif self.gameState == "Design":
			#Call create Level
			pass
		elif self.gameState == "Play":
			 
			pass
		elif self.gameState == "Next":
			#add points, 
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
	main = GamePlayer(0)
	print("starting...")
	main.run()
	print("shuting down...")
        
    