'''
Andrew Habib
09 April 2021
Egg Catcher Program
---> Main Code
'''
# Import pygame to enable options related to object oriented programming and forming games in python
import pygame, os

# Import Tk from tkinter to enable options related to manipulating windows
from tkinter import Tk

# Import options to allow pop-up message boxes to be used for interaction with the user 
from tkinter import messagebox

# Andrew's Egg Catcher Game Module
# Import options to create and manipulate a basket for an Egg Catcher Game
from EggCatcherGameElementsModule import Basket

# Andrew's Egg Catcher Game Module
# Import options to create and manipulate a basket for an Egg Catcher Game
from EggCatcherGameElementsModule import Egg

# Import randomizing options that would aid in randomly generating the rate and the frequency in which eggs would drop
import random

# Import everything from pygame locals
# Enables options to utilize the mouse and keyboard to perform certain functions in the program regarding movement
from pygame.locals import *

# Formulate a function that will play the game's background music
def playBackgroundMusic():
    
    # Initialize the pygame mixer which will be used as a music playing object
    pygame.mixer.init()
    
    # Load the mp3 audio file in pygame mixer to get the program to recognize the music file we want playing in the background
    pygame.mixer.music.load("audio/J.Geco - Chicken Song.mp3")
    
    # Play the loaded mp3 audio file indefinitely 
    pygame.mixer.music.play(-1)

# Formulate a function that will contain the code to movement of the basket left and right using the keyboard
def enableKeyboardMovement():
    
    # Ensuring basic basket movement at a steady pace and in the correct direction 
    # No up or down keys as the basket may only catch eggs horizontally
    # Check if the current action is the user pressing the A or the Left Arrow Keys
    if event.key == K_a or event.key == K_LEFT:
        
        # Each time the user enters one of those two keys, the basket will move 2 pixels left
        # A continuous left movement could be achieved by holding the key (See later code)
        basketCatcher.move(2, "MOVELEFT")
    
    # Check if the current action is the user pressing the D or the Right Arrow Keys   
    if event.key == K_d or event.key == K_RIGHT:
        
        # Each time the user enters one of those two keys, the basket will move 2 pixels right
        # A continuous right movement could be achieved by holding the key (See later code)
        basketCatcher.move(2, "MOVERIGHT")
    
    # Ensure that the basket Catcher does not go off the screen 
    
    # Check if the X position of the basket is less than or equal to 0 (Left side of the surface)
    if basketCatcher.getX() <= 0:
        
        # Set the X position of the basket to 0 to ensure it does not pass the left side of the surface
        # The X position of the basket will never be lower than 0
        basketCatcher.setX(0)
        
    # Otherwise, check if the X position of the basket is greater than or equal to the width of the surface minus the width of the basket
    # The width of the basket must be subtracted since the X position is measured using the top left corner
    # Must not pass the right side of the surface so it does not go off the screen
    elif basketCatcher.getX() >= surface.get_width() - basketCatcher.getWidth():
        
        # Set the X position of the basket to the width of the surface minus the width of the basket
        # The X position will never be higher than the surface width minus the basket width
        basketCatcher.setX(surface.get_width() - basketCatcher.getWidth())

# Formulate a function that will contain the code to movement of the basket left and right using the mouse
def enableMouseMovement():
    
    # Set the X position of the basket to the X position of the mouse's cursor subtracted by half of the basket's width
    # Ensures that the mouse is centered horizontally with the basket to enable easier user control
    basketCatcher.setX(event.pos[0] - basketCatcher.getWidth() // 2)
    
    # Do not alter the Y position of the basket as the basket will not move up and down
    # Keep the Y position consistently at 550 pixels so the cursor does not impact the Y position
    basketCatcher.setY(550)   
    
    # Ensure that the basket Catcher does not go off the screen 
    
    # Check if the X position of the basket is less than or equal to 0 (Left side of the surface)
    if basketCatcher.getX() <= 0:
        
        # Set the X position of the basket to 0 to ensure it does not pass the left side of the surface
        # The X position of the basket will never be lower than 0
        basketCatcher.setX(0)
        
    # Otherwise, check if the X position of the basket is greater than or equal to the width of the surface minus the width of the basket
    # The width of the basket must be subtracted since the X position is measured using the top left corner
    # Must not pass the right side of the surface so it does not go off the screen
    elif basketCatcher.getX() >= surface.get_width() - basketCatcher.getWidth():
        
        # Set the X position of the basket to the width of the surface minus the width of the basket
        # The X position will never be higher than the surface width minus the basket width
        basketCatcher.setX(surface.get_width() - basketCatcher.getWidth())

# Formulate a function that will generate a list of 10 random integers 
# (Will be used later in the code to re-arrange eggs after at least 1 level is complete)
def onlyGenerateRandomNums():
    
    # Declare and initialize a variable storing an integer of 0
    # The variable will be used to store the current index of the list
    listIndex = 0
    
    # Declare and initialize a list of 10 values (They are none for now until values are generated and added)
    list_RandomNums = [None] * 10
    
    # For loop (Counted Loop) - Purpose is to generate the 10 random integers between 1 and 4 and then add them to the list
    # The loop will iterate in accordance to the length of the list
    for counter in range(len(list_RandomNums)):
        
        # Generate a random integer ranging from 1 - 4 inclusively
        randomNum = random.randint(1, 4)
        
        # Make the Random List of Numbers at the current index equal to the randomly generated number
        list_RandomNums[listIndex] = randomNum
        
        # Update the list Index by increasing it by 1 to move on to the next spot on the list
        listIndex = listIndex + 1
        
    # After the loop is complete, the listIndex will be re-initialized to 0 
    listIndex = 0
    
    # Return the list of the 10 random integers between 1 and 4
    return list_RandomNums

'''
Formulate a function that will generate the eggs that will fall from the chickens initially 
before the game even commences. The function will first create a list with random integers between 
1 and 4 to randomize the X position of the egg (Under which of the 4 chickens will the egg be dropped).
After the 10 numbers have been generated and put into the random numbers list, an egg object will be 
added to the Random Eggs list and will have set X positions based on which integer they are dealing with.
1-->X position is same as first Chicken
2-->X position is same as second Chicken
3-->X position is same as third Chicken
4-->X position is same as fourth Chicken
- This will mainly be used at the commencing of the game as eggs will not need to be regenerated afterwards
'''
def generateRandomEggs():
    
    # Declare and initialize a variable storing an integer of 0
    # The variable will be used to store the current index of the list
    listIndex = 0
    
    # List for 10 random integers between 1 and 4
    # Declare and initialize a list of 10 values (They are none for now until values are generated and added)
    list_RandomNums = [None] * 10
    
    # Declare and initialize a list that will contain 10 Egg objects to used for the commencing of the game
    list_RandomEggs = [None] * 10
    
    # For loop (Counted Loop) - Purpose is to generate a list of random numbers to randomly distribute eggs among the chickens
    # The loop will iterate in accordance to the length of the list
    # Each iteration will add a new random integer between 1 and 4
    for counter in range(len(list_RandomNums)):
        
        # Declare a variable that will store a random integer between 1 and 4
        randomNum = random.randint(1, 4)
        
        # Add the number to the list by replacing it to the left most "None" value (Replace instead of append)
        list_RandomNums[listIndex] = randomNum
        
        # Increase the value of the index by 1 to move on to the next value and replace it
        listIndex = listIndex + 1
        
    # After the loop is complete, the listIndex will be re-initialized to 0     
    listIndex = 0
    
    # Excess - Test Print Function - Displays the Random Numbers list
    print(list_RandomNums)
    
    # For loop (Counted Loop) - Purpose is to generate the egg objects from the egg class and then add them to the list
    # The loop will iterate in accordance to the length of the list
    # Each time, the list will contain 1 new egg with an X position depending on which random integer (1-4)it matches with
    # The arranging of eggs based on X position will occur when an egg is arranged according to the integer of its same index from the random numbers list 
    for counter in range(len(list_RandomEggs)):
        
        # Check if the Random Numbers list at the current index is equivalent to 1
        if list_RandomNums[listIndex] == 1:
            
            # Make the Random Eggs list at the current index equal to the Egg object
            list_RandomEggs[listIndex] = Egg()
            
            # Set the X position of the Random Eggs list at the current index in correspondence with the first chicken
            # This means that this specific egg will belong to chicken 1 as the integer attained this index was 1
            list_RandomEggs[listIndex].setX(Chicken1xPosition + adjustEggPosition)
            
            # Set the Y position of the Random Eggs list at the current index to a set value of 120 pixels
            list_RandomEggs[listIndex].setY(120)
            
            # Increase the value of the index by 1 to move on to the next value and replace it
            listIndex = listIndex + 1
        
        # Otherwise, check if the Random Numbers list at the current index is equivalent to 2 
        elif list_RandomNums[listIndex] == 2:
            
            # Make the Random Eggs list at the current index equal to the Egg object
            list_RandomEggs[listIndex] = Egg()
            
            # Set the X position of the Random Eggs list at the current index in correspondence with the second chicken
            # This means that this specific egg will belong to chicken 2 as the integer attained this index was 2
            list_RandomEggs[listIndex].setX(Chicken2xPosition + adjustEggPosition)
            
            # Set the Y position of the Random Eggs list at the current index to a set value of 120 pixels
            list_RandomEggs[listIndex].setY(120)
            
            # Increase the value of the index by 1 to move on to the next value and replace it
            listIndex = listIndex + 1
        
        # Otherwise, check if the Random Numbers list at the current index is equivalent to 3   
        elif list_RandomNums[listIndex] == 3:
            
            # Make the Random Eggs list at the current index equal to the Egg object
            list_RandomEggs[listIndex] = Egg()
            
            # Set the X position of the Random Eggs list at the current index in correspondence with the third chicken
            # This means that this specific egg will belong to chicken 3 as the integer attained this index was 3
            list_RandomEggs[listIndex].setX(Chicken3xPosition + adjustEggPosition)
            
            # Set the Y position of the Random Eggs list at the current index to a set value of 120 pixels
            list_RandomEggs[listIndex].setY(120)
            
            # Increase the value of the index by 1 to move on to the next value and replace it
            listIndex = listIndex + 1 
            
        # Otherwise, check if the Random Numbers list at the current index is equivalent to 4    
        elif list_RandomNums[listIndex] == 4:
            
            # Make the Random Eggs list at the current index equal to the Egg object
            list_RandomEggs[listIndex] = Egg()
            
            # Set the X position of the Random Eggs list at the current index in correspondence with the fourth chicken
            # This means that this specific egg will belong to chicken 4 as the integer attained this index was 4
            list_RandomEggs[listIndex].setX(Chicken4xPosition + adjustEggPosition)
            
            # Set the Y position of the Random Eggs list at the current index to a set value of 120 pixels
            list_RandomEggs[listIndex].setY(120)
            
            # Increase the value of the index by 1 to move on to the next value and replace it
            listIndex = listIndex + 1
    
    # Return the list comprised of the 10 egg objects that were generated      
    return list_RandomEggs

# Formulate a function that will generate a random list of integers
# The integers will determine how frequently to drop eggs based on the Y position of the current falling egg
# If the current egg reaches the Y position of the random integer generated, then the next egg will be released
def randomDropFrequency():
    
    # Declare and initialize a variable storing an integer of 0
    # The variable will be used to store the current index of the list    
    listIndex = 0
    
    # List for 10 random integers between 220 and 340
    # Declare and initialize a list of 10 values (They are None for now until values are generated and added)
    # Each of these indexes will serve as a y position condition that controls the release of the next egg
    randomDropList = [None] * 10
    '''
    For Loop - Counted Loop - Purpose is to re-iterate according to the Random Drop list length (10)
    to then generate a random integer between 220 and 340 and replace it with the list at the current
    index and so on until the entire list is filled with 10 random integers between 220 and 340
    '''
    for counter in range(len(randomDropList)):
        
        # Declare a variable that will store an integer between 220 and 340 inclusively
        randomDrop = random.randint(220, 340)
        
        # Replace the randomDropList at the current index (None) with the integer generated
        randomDropList[listIndex] = randomDrop
        
        # Increase the value of the index by 1 to move on to the next value and replace it
        listIndex = listIndex + 1
        
    # Return the random Drop list filled with random integers ranging from 220 - 340
    return randomDropList

# Create a new window with Tk from the Tkinter module then make it disappear for now  
root = Tk()
root.withdraw()

# Declare and initialize a string variable that stores the peripheral choice
# No resembles using the mouse and Yes resembles using the keyboard
peripheralChoice = "no"

# Before displaying the main surface, display a message box greeting the user to the Egg Catcher Game
messagebox.showinfo("Egg Catcher", "Welcome to Egg Catcher!")

# Declare a variable that will store the user's choice of whether or not they would like to use a keyboard or a mouse
# No == MOUSE -- Yes == KEYBOARD
# Prompt the user and ask them if they would like to use a keyboard to play or not
# Explain that No enables the Mouse and Yes enables the Keyboard
peripheralChoice = messagebox.askquestion("Egg Catcher", 
    "Would you like to use your Keyboard to play?\nClick Yes for Keyboard and No to use your Mouse")

# Declare a variable to store a boolean that determines whether or not the game will start
# For now, it is false as the user needs to hint that they would like to start
startgame = False

# Ensure that the game surface is centered right in the middle of your screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize all modules required for PyGame
pygame.init()

# Set the PyGame caption displayed on the top left of the surface to the name of the program (Egg Catcher)
pygame.display.set_caption('Egg Catcher')

# Set the cursor of the mouse to invisible by making the visibility false
pygame.mouse.set_visible(False)

# Make a call to the function to play the background music for the program
playBackgroundMusic()

# Initialize all sound objects
# Declare a variable to store the sound effect for the egg breaking
soundEffectBreakEgg = pygame.mixer.Sound("audio/EggBrokeSound.wav")

# Declare a variable to store the sound effect for the Chicken releasing the egg 
soundEffectReleaseEgg = pygame.mixer.Sound("audio/ChickenReleaseEggSound.wav")

# Declare a variable to store the sound effect for the Egg being caught
soundEffectEggCaught = pygame.mixer.Sound("audio/EggCaughtSound.wav")

# Set the surface window (main window) to a width of 500 pixels and a height of 750 pixels
surface = pygame.display.set_mode((500, 750))

# Declare a variable that will store the dimensions (width and height) of the surface
surface_dimensions = pygame.display.get_surface()

# Declare a variable that will store an initial integer of 0 serving as the starting score
score = 0

# Declare a variable that will store an initial integer of 1 serving as the starting level(hits) 
hits = 1

# Declare a variable that will store an initial integer of 150 serving as the starting health
# This value will determine the width of the health rectangle
health = 150

# Declare a variable that will store the font and font size for the starting message (HIT ENTER TO START)
# Font --> Neuropol.ttf, Font size --> 24
start_font = pygame.font.Font("neuropol.ttf", 24)

# Declare a variable that will store the font and font size for the game information (score, hits, etc.)
# Font --> Neuropol.ttf, Font size --> 18
game_font = pygame.font.Font("neuropol.ttf", 18)

# Declare a variable that will store a newly formed surface on which the text will go
# The starting font will be used on the starting output
# The output will be used to prompt the user to hit enter to start the screen
# Anti-aliasing is enabled for smoother edges and the color used is a very dark green
start_output = start_font.render("HIT ENTER TO START", 
    True, pygame.Color("#1c2e18"))

# Declare a variable that will store a newly formed surface on which the text will go
# The game font will be used on the scoring output
# The output will display the score along with its subtitle
# Anti-aliasing is enabled for smoother edges and the color used is green
score_output = game_font.render("{:<10s}{:<5d}".format("SCORE:", score), 
    True, pygame.Color("green"))

# Declare a variable that will store a newly formed surface on which the text will go
# The game font will be used on the level output
# The output will display the level along with its subtitle
# Anti-aliasing is enabled for smoother edges and the color used is green
level_output = game_font.render("{:<10s}{:<5d}".format("LEVEL:", hits), 
    True, pygame.Color("green"))

# Declare a variable that will store a newly formed surface on which the text will go
# The game font will be used on the word health going above the health bar
# The output will display the word health above the health bar
# Anti-aliasing is enabled for smoother edges and the color used is green
health_output = game_font.render("HEALTH", True, pygame.Color("green"))

# Declare a variable that will store the loaded image for the background picture form images folder
imgBackground = pygame.image.load('images/bg_bamboo.png')

# Declare a variable that will store the loaded image for the chicken picture from images folder
imgChicken = pygame.image.load("images/chicken.png")

# Declare a variable that will store an egg object from the Egg Class in Egg Catcher Module
# To be used to perform accurate measurements when creating X and Y position variables below
fallingEggChicken = Egg()

# Declare a variable that will store a basket object form the Basket Class in Egg Catcher Module
# This will be the basket that the user moves to catch the falling Eggs
basketCatcher = Basket()

# Set the basket Catcher X position to a default starting value at the exact center of the surface window
basketCatcher.setX(surface.get_width() // 2 - basketCatcher.getWidth() // 2)

# Set the basket Catcher Y position to a default value of 550 pixels 
# This will never change as the basket will not go up nor down but only left and right to catch eggs
basketCatcher.setY(550)

# Declare 4 variables that will store the X position measurements for each of the 4 chickens
# The same measurements will be used on the eggs when they are randomly outputted beneath a chicken when the game starts
'''
--> The measurements ensure that the chickens are reasonably spaced from the surface window's edges and
that the 4 chickens are evenly spaced apart to create an organized and esthetically pleasing game
'''
Chicken1xPosition = 50
Chicken2xPosition = (surface.get_width() - imgChicken.get_width() - 100) // 3 + 50
Chicken3xPosition = (surface.get_width() - imgChicken.get_width() - 100) // 3 * 2 + 50
Chicken4xPosition = surface.get_width() - imgChicken.get_width() - 50
adjustEggPosition = ((imgChicken.get_width() // 2) - (fallingEggChicken.getWidth() // 2)) - 5

# Declare and initialize an empty list for Random eggs
listRandomEggs = []

# Declare and initialize an empty list for integers that will determine when to drop the next egg
listDropMoment = []

# Make the Random Eggs list equal to the list of the 10 randomly X positioned eggs generated in the user-defined function above
listRandomEggs = generateRandomEggs()

# Make the list Drop Moment equal to the list of the 10 random Y positions (Deciding when to drop next egg) generated in the user-defined function above
listDropMoment = randomDropFrequency()

# Declare and initialize another new list for random eggs 
# Any eggs in this will be considered moving or broken
# An egg will not be placed in this list if it is neither of those conditions
newListRandomEggs = [None] 

# Two list indexes will be declared to avoid accessing the wrong indexes at the wrong times (Reduces chance for logical errors when accessing list Indexes)
# Declare and initialize a variable storing an integer for the index of a list
listIndex = 0

# Declare and initialize another variable storing an integer for the index of a list
listIndex2 = 0

# Declare and initialize a variable storing a boolean that determines whether or not the program will continue
# The variable should start as true so that the program may start when the user enters
programContinuity = True

# Declare and initialize a variable storing an integer for the increasing increment for speed
# This variable will update to increase the speed of eggs dropping as the levels progress
speedIncrement = 0

# Excess - Test Print Function - Displays at which Y coordinate the next egg will drop
print(listDropMoment)

pygame.time.set_timer(pygame.USEREVENT, 17 - speedIncrement)

# Handler for holding down a key on one's keyboard
# Set a set_repeat function to repeat corresponding events when keys on the keyboard are hit
# The interval is unaltered which the delay is 3 milliseconds
pygame.key.set_repeat(3)

# Keep the program running or looping until a condition to turn the programConituity to False is met
# This keeps the game running rather than stopping right on start up
# Program continuity will be false when either the user chooses to quit, the player has lost all of their health or the user has beat all 8 levels
while programContinuity == True:
    
    # For loop - Counted loop - Purpose is to cycle through every event currently in queue and clear it
    for event in pygame.event.get():
        
        # Check if the current event is the user clicking the close button to quit the game
        if event.type == pygame.QUIT:
            
            # Ensure that the program continuity is updated to false to end the program loop
            programContinuity = False
        
        # Check if the current event is a keyboard key being pressed down   
        if event.type == pygame.KEYDOWN:
            
            # Check if the user presses the enter key on either the main keyboard or keypad
            if event.key == K_KP_ENTER or event.key == K_RETURN:
                
                # Update start game to true to get the actual game starting right away
                startgame = True
        
        # Check if start game is equivalent to true
        # Will occur when user hits enter key to start       
        if startgame == True:
            
            # Check if the user presses down a keyboard key and the peripheralChoice is Yes (Keyboard input was chosen)
            if event.type == pygame.KEYDOWN and peripheralChoice == "yes":
                
                # Make a call to the function that enables left and right movement using the keyboard
                enableKeyboardMovement()
            
            # Otherwise, check if the user is moving their mouse and the peripheralChoice is No (Mouse input was chosen)          
            elif event.type == pygame.MOUSEMOTION and peripheralChoice == "no":
                
                # Make a call to the function that enables left and right movement using the mouse
                enableMouseMovement()
            
            # Check if the current event ID has been triggered (USEREVENT is the current event in queue) and if the hits (level) is less than 9 (There are only 8 levels)
            if event.type == pygame.USEREVENT and hits < 9:
                
                # Replace the 0th (first) index of newListRandomEggs (None) with the first number on listRandomEggs
                # This will cause 1 egg to be added to the list of moving or breaking eggs
                newListRandomEggs[0] = listRandomEggs[0]
                
                # For Loop - Counted Loop - Purpose is to cycle through every egg in the new list of random eggs and either break or move it
                for egg in newListRandomEggs:
                    
                    # Check if the current egg's Y position is greater than or equal to 550 pixels
                    if egg.getY() >= 550:
                        
                        # Break the egg using a function from the Egg class which will switch over to an image of a broken egg and not move the image anymore
                        egg.breakEgg()
                        
                    # Otherwise, the current egg's Y position is less than 550 pixels
                    else:
                        
                        # Move the egg using a function from the Egg class which will move the Egg 1 pixel downwards every iteration as per the parameters
                        egg.move(1, "MOVEDOWN")
                
                # Check if the Y position of the first egg in newListRandomEggs is equivalent to 121 pixels (First Egg started moving)
                if newListRandomEggs[0].getY() == 121:
                    
                    # Play the sound effect for a chicken releasing an egg
                    pygame.mixer.Sound.play(soundEffectReleaseEgg)
                
                # Check if the Y position of the egg in newListRandomEggs at the current index is 549 pixels and if the egg is not yet broken
                # This will ensure that the sound effect does not play twice if the egg breaks on the side of the basket
                # This will play 1 pixel right before it hits the ground at 550
                if newListRandomEggs[listIndex2].getY() == 549 and newListRandomEggs[listIndex2].isBroken() == False:
                    
                    # Play the sound effect for an egg breaking as it hits the ground
                    pygame.mixer.Sound.play(soundEffectBreakEgg)
                
                # Collision Detection - Checking if at least half of the egg has been caught within the basket from the top
                # Check if the current egg's Y position plus its height is equivalent to the basket's Y position plus 2 (To account for extra image space) and the 2nd list Index is not equal to 10
                if newListRandomEggs[listIndex2].getY() + newListRandomEggs[listIndex2].getHeight() == basketCatcher.getY() + 2 and listIndex2 != 10:
                    
                    # Check if the current egg's X position plus its width integer divided by two is greater than or equal to the basket's X position
                    if newListRandomEggs[listIndex2].getX() + (newListRandomEggs[listIndex2].getWidth()) // 2 >= basketCatcher.getX():
                        
                        # Check if the current egg's X position plus its width integer divided by two is less than or equal to the basket's X position plus its width
                        if newListRandomEggs[listIndex2].getX() + (newListRandomEggs[listIndex2].getWidth()) // 2 <= basketCatcher.getX() + basketCatcher.getWidth():
                            
                            # Move the current egg off of the screen to resemble being caught and so the egg does not show up again until after the game is complete
                            # Set the X position of the current egg at 800 pixels (Past width of surface)
                            newListRandomEggs[listIndex2].setX(800)
                            
                            # Set the Y position of the current egg at 800 pixels (Past the height of surface)
                            newListRandomEggs[listIndex2].setY(800)
                            
                            # Update the score by 10 to resemble attaining 10 points when catching an egg
                            score = score + 10
                            
                            # Play the sound effect for an egg being caught by the basket
                            pygame.mixer.Sound.play(soundEffectEggCaught)
                            
                            # Check if the 2nd list index is less than 9
                            if listIndex2 < 9:
                                
                                # Increase the 2nd list Index by 1
                                listIndex2 = listIndex2 + 1
                
                # Collision Detection - Checking if less than half of the egg is on the basket or the egg hits the basket from the side
                # Check if the current egg's Y position plus its height is greater than the basket's Y position plus 2 (To account for extra image space) and the 2nd list Index is not equal to 10
                if newListRandomEggs[listIndex2].getY() + newListRandomEggs[listIndex2].getHeight() > basketCatcher.getY() + 2 and listIndex2 != 10:
                    
                    # Check if the current egg's X position plus its width integer divided by two is less than to the basket's X position
                    if newListRandomEggs[listIndex2].getX() + (newListRandomEggs[listIndex2].getWidth()) // 2 < basketCatcher.getX():
                        
                        # Check if the current egg's X position is greater than or equal to the basket's X position minus the current egg's width
                        if newListRandomEggs[listIndex2].getX() >= basketCatcher.getX() - newListRandomEggs[listIndex2].getWidth():
                            
                            # Ensures that the breaking egg sound effect is not played twice
                            # Check if the current egg has been broken yet
                            if newListRandomEggs[listIndex2].isBroken() == False:
                                
                                # Play the sound effect for an egg breaking
                                pygame.mixer.Sound.play(soundEffectBreakEgg)
                                
                            # Break the egg using a function from the Egg class which will switch over to an image of a broken egg
                            # This time, the egg will keep moving as it has not yet reached 550 pixels
                            newListRandomEggs[listIndex2].breakEgg()
                    
                    # Otherwise, check if the current egg's X position plus its width integer divided by two is greater than to the basket's X position plus its width
                    elif newListRandomEggs[listIndex2].getX() + (newListRandomEggs[listIndex2].getWidth()) // 2 > basketCatcher.getX() + basketCatcher.getWidth():
                        
                        # Check if the current egg's X position is less than or equal to the basket's X position plus its width
                        if newListRandomEggs[listIndex2].getX() <= basketCatcher.getX() + basketCatcher.getWidth():
                            
                            # Ensures that the breaking egg sound effect is not played twice
                            # Check if the current egg has been broken yet
                            if newListRandomEggs[listIndex2].isBroken() == False:
                                
                                # Play the sound effect for an egg breaking
                                pygame.mixer.Sound.play(soundEffectBreakEgg)
                                
                            # Break the egg using a function from the Egg class which will switch over to an image of a broken egg
                            # This time, the egg will keep moving as it has not yet reached 550 pixels
                            newListRandomEggs[listIndex2].breakEgg()

                # Check if the current egg's Y position is equivalent to 550 (End of egg's path) and the 2nd list Index is not equivalent to 9                       
                if newListRandomEggs[listIndex2].getY() == 550 and listIndex2 != 9:  
                    
                    # Decrease the health bar (width of health rectangle) by 10 % 
                    health = health - (150 * 0.10)
                    
                    # Update the 2nd list Index by adding 1 to move on to the next index
                    listIndex2 = listIndex2 + 1
                
                # Check if the current egg's Y position is equivalent to the current drop moment (Condition enabling another egg to drop) minus 30 and the 1st list index is not equivalent to 9
                # 30 is subtracted to start the sound effect earlier to account for PyGame sound effect delay
                if newListRandomEggs[listIndex].getY() == listDropMoment[listIndex] - 30 and listIndex != 9:
                    
                    # Play the sound effect for a new egg being dropped by a chicken
                    pygame.mixer.Sound.play(soundEffectReleaseEgg)
                
                # # Check if the current egg's Y position is equivalent to the current drop moment (Condition enabling another egg to drop) and the 1st list index is not equivalent to 9
                if newListRandomEggs[listIndex].getY() == listDropMoment[listIndex] and listIndex != 9:
                    
                    # Increase the 1st list index by 1
                    listIndex = listIndex + 1
                    
                    # Append or add a new egg to the new moving/ breaking eggs list from the listRandomEggs containing the generated egg objects at the current index
                    newListRandomEggs.append(listRandomEggs[listIndex])
                '''
                Check if the current egg at list index 2 Y position is equivalent to 550 (end of egg's path) and list index 2 is equivalent to 9 (last index) or
                the current egg at list index 2 Y position is equivalent to 800 and list index 2 is equivalent to 9. This ensures that any of the 2 indexes are 
                not updated any further as the game is over at that point. The condition checks if the last egg in the level has either reached the ground or was
                caught by the basket.
                '''
                if (newListRandomEggs[listIndex2].getY() == 550 and listIndex2 == 9) or (newListRandomEggs[listIndex2].getY() == 800 and listIndex2 == 9):
                    
                    # Check if the current egg at list index 2 Y position is equivalent to 550 (end of egg's path) and list index 2 is equivalent to 9 (last index)
                    if newListRandomEggs[listIndex2].getY() == 550 and listIndex2 == 9:
                        
                        # Decrease the health bar (width of health rectangle) by 10 % one last time before the level ends     
                        health = health - (150 * 0.10) 
                    
                    # Declare a list that will store only the 10 new random integers to avoid regenerating eggs but rather reseting their positions
                    # The reset function from the class Egg in my module will automatically reset any broken eggs to normal eggs
                    listRandomNums = onlyGenerateRandomNums()
                    
                    # Excess - Test Print Function - Displays the new 10 random integers to ensure that the eggs are being re-arranged properly
                    print(listRandomNums)
                    '''
                    For loop - Counted loop - Purpose is to loop through every egg in the list of Random eggs and re-arrange them to their respective positions
                    behind each of the chickens based on which of the 4 integers were generated in every iteration  
                    --> Enumerate keeps track of iteration number
                    '''
                    for index, egg in enumerate(listRandomEggs):
                        
                        # Reset all of the eggs' Y positions to 100
                        
                        # Otherwise, check if the new random number generated at the current index is equivalent to 1
                        if listRandomNums[index] == 1:
                            
                            # Reset the X position of the current egg to the X position of the first chicken then adjust its position slightly for cleaner look
                            egg.reset(None, y=120, x=Chicken1xPosition + adjustEggPosition)
                        
                        # Otherwise, check if the new random number generated at the current index is equivalent to 2
                        elif listRandomNums[index] == 2:
                            
                            # Reset the X position of the current egg to the X position of the second chicken then adjust its position slightly for cleaner look
                            egg.reset(None, y=120, x=Chicken2xPosition + adjustEggPosition)
                        
                        # Otherwise, check if the new random number generated at the current index is equivalent to 3
                        elif listRandomNums[index] == 3:
                            
                            # Reset the X position of the current egg to the X position of the third chicken then adjust its position slightly for cleaner look
                            egg.reset(None, y=120, x=Chicken3xPosition + adjustEggPosition)
                            
                        # Otherwise, check if the new random number generated at the current index is equivalent to 4
                        elif listRandomNums[index] == 4:
                            
                            # Reset the X position of the current egg to the X position of the fourth chicken then adjust its position slightly for cleaner look
                            egg.reset(None, y=120, x=Chicken4xPosition + adjustEggPosition)   
                        
                    # Re-initialize only the following variables to proceed to the next level with proper statistics 
                    newListRandomEggs = [None] 
                    listDropMoment = randomDropFrequency()
                    
                    # Excess - Test Print Function - Displays the new drop moments
                    print(listDropMoment)
                    listIndex = 0
                    listIndex2 = 0  
                    hits = hits + 1
                    
                    # Set the timer for this event to 0 to ensure that the game does not continue before the user is ready
                    pygame.time.set_timer(pygame.USEREVENT, 0)
                    
                    # Check if the hits (level) is less than 9 and the health is not equal to 0
                    if hits < 9 and health != 0:
                        
                        # Display a message box that congratulates the user for moving on to the next level and output the level
                        messagebox.showinfo("Egg Catcher", "Congratulations, you are going to level " + str(hits) + "!")
                        
                        # Display a message box that tells the user to click again on the screen to activate their movement
                        messagebox.showinfo("Egg Catcher", "Click again on the screen to activate your movement!")
                        
                        # May work on older versions of PyGame to reset focus on main screen 
                        pygame.display.set_mode((500, 750))
                        
                        # Increase the speedIncrement by 2 to speed up the movement of the eggs
                        speedIncrement = speedIncrement + 2
                        
                        # Update the timer to the new interval set to make movement faster and thus the upcoming level more challenging than the previous
                        # This line will also get the eggs to start falling again but faster than the last time
                        pygame.time.set_timer(pygame.USEREVENT, 17 - speedIncrement)
                        
                    
    # Output the background and place its top left corner right on the top left corner of the surface (0, 0)                                          
    surface.blit(imgBackground, (0, 0))
    
    # Check if start game is equivalent to False (The user has not pressed enter to start the game yet)
    if startgame == False:
        
        surface.blit(start_output, 
            (surface_dimensions.get_width() // 2 - start_output.get_width() // 2, 
            surface_dimensions.get_height() // 2))    
        
    # Update the score and level output variables as the user is constantly gaining points or losing health
          
    # Declare a variable that will store a newly formed surface on which the text will go
    # The game font will be used on the scoring output
    # The output will display the score along with its subtitle
    # Anti-aliasing is enabled for smoother edges and the color used is green
    score_output = game_font.render("{:<10s}{:<5d}".format("SCORE:", score), 
        True, pygame.Color("green"))
    
    # Declare a variable that will store a newly formed surface on which the text will go
    # The game font will be used on the level output
    # The output will display the level along with its subtitle
    # Anti-aliasing is enabled for smoother edges and the color used is green
    level_output = game_font.render("{:<10s}{:<5d}".format("LEVEL:", hits), 
        True, pygame.Color("green"))
    
    # Output the score near the bottom left corner of the surface
    surface.blit(score_output, (20, surface_dimensions.get_height() - 130))
    
    # Output the level/ hits near the bottom right of the surface aligned with the score
    surface.blit(level_output, 
        (surface_dimensions.get_width() - level_output.get_width(), 
        surface_dimensions.get_height() - 130))
    
    # Output the word health near the bottom of the surface perfectly centered for esthetically pleasing and symmetrical look
    surface.blit(health_output, 
        (surface_dimensions.get_width() // 2 - health_output.get_width() // 2, 
        surface_dimensions.get_height() - 80))
    '''
    Draw a dark green with the following dimensions as the background rectangle for health bar
    The dimensions ensure that the rectangle is horizontally centered, it is located near the
    bottom of the surface and the dimensions are large enough for visibility but not too large.
    --> This rectangle will be hidden behind the health bar until the player loses health in which
    it will be revealed as the background
    '''
    pygame.draw.rect(surface, pygame.Color('#009600'), 
        (surface_dimensions.get_width() // 2 - 150 // 2, 
        surface_dimensions.get_height() - 50, 150, 20), 0)
    
    # The same dimensions are used here as in the rectangle above but with the color green
    # This rectangle is the health bar itself which will decrease as the player loses health
    pygame.draw.rect(surface, pygame.Color('green'), 
        (surface_dimensions.get_width() // 2 - 150 // 2, 
        surface_dimensions.get_height() - 50, health, 20), 0)
    
    # For loop - Counted loop - Purpose is to re-iterate based on the length of the list of Random Eggs then output the image of the egg
    for counter in range(len(listRandomEggs)):
        
        # Constantly output the current X and Y position of the every egg image in the list of 10 eggs including when the eggs move 1 pixel at a time
        # The updated position and the state of every egg will be shown with every iteration of the for loop along with every program iteration
        surface.blit(listRandomEggs[counter].getImage(), 
            (listRandomEggs[counter].getX(), listRandomEggs[counter].getY()))
    
    # Ouput all 4 of the chickens based on the the X positions that were pre-made for them using mathematical calculations and a set Y position of 100 so they are all lined up horizonatally
    surface.blit(imgChicken, (Chicken1xPosition, 100))
    surface.blit(imgChicken, (Chicken2xPosition, 100))
    surface.blit(imgChicken, (Chicken3xPosition, 100))
    surface.blit(imgChicken, (Chicken4xPosition, 100))
    
    # Constantly output the current X and Y position of the basket including when the user uses their mouse or keyboard to move the basket a certain direction
    # The updated position of the basket will always be shown as the user moves it to catch the eggs (The Y position will remain constant)
    surface.blit(basketCatcher.getImage(), (basketCatcher.getX(), basketCatcher.getY()))
    
    # Check if the player's health is less than or equal to 0 or they have finished level 8 
    if health <= 0 or hits >= 9:
        
        # Set the timer for egg dropping to 0 so that the game stops completely and no more eggs drop
        pygame.time.set_timer(pygame.USEREVENT, 0)
        
        # Declare a variable that will store the user's choice of whether or not they would like to play again
        # Prompt the user and ask them if they would like to play again
        potentialTermination = messagebox.askquestion("Egg Catcher", 
            "GAMEOVER!\nYou finished with " + str(score) + " points.\nWould you like to play again?")
        
        # Check if the user selected not to play again on the message box
        if potentialTermination == "no":
            
            # Set the program Continuity to false in which case, the game loop will end and the program will be terminated
            programContinuity = False
        
        # Otherwise, the user selected to play again    
        else: 
            # Re-initialize all important variables as if the program is just starting
            
            # Do not terminate the program by keeping the Program Continuity as True
            programContinuity = True
            
            # Make sure the game does not start right away unless the user hits enter again (Keep as False)
            startgame = False
            
            # Re-initialize all the critical lists and variables to restart a completely new game
            listRandomEggs = []
            listRandomEggs = generateRandomEggs()
            listDropMoment = randomDropFrequency()
            newListRandomEggs = [None] 
            listIndex = 0
            listIndex2 = 0
            speedIncrement = 0 
            score = 0
            hits = 1
            health = 150
            
            # Re-prompt the user and ask them if they would like to use a keyboard to play or not
            # Explain that No enables the Mouse and Yes enables the Keyboard 
            peripheralChoice = messagebox.askquestion("Egg Catcher", 
                "Would you like to use your Keyboard to play?\nClick Yes for Keyboard and No to use your Mouse")
            # Reset the timer back to 18 - speed increment (0) to ensure that level 1 starts slow again
            pygame.time.set_timer(pygame.USEREVENT, 17 - speedIncrement)
    
    # Apply any updates to the surface window as an event occurs        
    pygame.display.update()
    
    '''
    > Notes:
    - Ask about comment coding in class
    - Change in speed
    - sound effect of egg break
    - Comp Sci
    - Uncomment the background music
    - Change some game parameters
    '''
    '''
    > Further Ideas:
    - Add extra functions in the EggCatcherGameElementsModule
    - Ask for choice between mouse and keyboard
    - Add extra sound effect for the chicken dropping egg
    '''
    '''
    > Done:
    - Check over the EggCatcherGameElementsModule class Egg
    in breakEgg function to ensure that the code is functional
    - Set the y-axis to a randomly generated number as a condition to 
    release more eggs
    - Make timer for random numbers random as well
    - Fix collision detection
    - Potential debugging for the scoring and health bar
    - Adjust speed for keyboard playing
    - Fix ending of the game and timing
    - Add 3 sound effects 
    - Ask teacher about speed of timer
    - Ask teacher about message box problem
    - Ask teacher about off audio timing in first egg
    - Ask teacher about egg breaking when smashed by basket
    - Ask teacher about egg remaining broken until the level finishes
    - Implementing new ideas?
    - Break egg when in contact with the side of the basket
    - Comment code
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    