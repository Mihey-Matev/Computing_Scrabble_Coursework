# There are many comments in my code which are just parts of old code which I do not want to delete just yet, just in case i notice that i do need them later on.
# I have also predefined many classes without actually having defined their attributes or methods. I have done this so that I can work on anything when I need to.

import pygame, time#, threading, queue
#import _thread
import visual_elements, scenes, players, in_game


class Director: # This class is basically the class which links everything together and controls the whole game
	def __init__(self):
		self.theme_colour = (237, 180, 127)
		self.screen = pygame.display.set_mode((960, 720))
		pygame.display.set_caption("Scrabble-like Game")
		
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((255, 255, 255))
		
		self.quit_flag = False
		
		self.scene = scenes.MainMenuScene()#self.screen)		
		#self.clock = pygame.time.Clock()
		self.ChangeToScene(self.scene)
		self.MainGameLoop()
 
	
	# sets the background colour for the game, so it doesn't have to be done separately by each scene; however, if i scene does want to change the background colour, it still can.
	def BgColourDrawer(self):
		pygame.display.get_surface().fill((237, 180, 127))

	
	# The loop which allows the game to play; it ends only when the user presses the 'x' button or exit game button (in the main menu)
	def MainGameLoop(self): 
		while not self.quit_flag:
			#time = self.clock.tick(60)
 
			# Exit events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.Quit()
			
			# Detect events
			scene_to_change_to = self.scene.ProcessInput(pygame.event.get())
			
			# Update scene
			self.scene.Update()
 
			# Draw the screen
			self.BgColourDrawer()
			self.scene.Draw()#self.screen)
			pygame.display.flip()
			
			# If the user has clicked a button which should change the scene, change to the scene which that button specifies to change to
			if not (scene_to_change_to is None):
				self.ChangeToScene(scene_to_change_to)
 
	def ChangeToScene(self, scene):
		"Changes the current scene."
		self.scene = scene
		#self.scene.OnDraw(self.screen)
 
	def Quit(self):
		self.ChangeToScene(None)
		self.quit_flag = True

		
	
def main():
	pygame.init()
	main_director = Director()	
	

main()









"""
def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

threading.Thread(target=loop1_10).start()
"""
"""
# Define a function for the thread
def print_time( threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
	print ("end of " + threadName)

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 2, ) )
except:
   print ("Error: unable to start thread")

print ("hi")
while 1:
	time.sleep(1)
"""

#Example 1
"""
exitFlag = 0

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		
	def run(self):
		print ("Starting " + self.name)
		print_time(self.name, 5, self.counter)
		print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print ("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
time.sleep(3)
exitFlag = 1
print ("Exiting Main Thread")
"""



"""

#Example 2

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire(1)
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()	#Other threads can call a thread’s join() method. This blocks the calling thread until the thread whose join() method is called is terminated.
print ("Exiting Main Thread")

"""




#time.sleep(2)







		
			

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			