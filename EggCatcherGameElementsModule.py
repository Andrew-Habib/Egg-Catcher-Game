'''
Andrew Habib
09 April 2021
Egg Catcher Program
---> Egg Catcher Game Elements Module
'''
# Egg Catcher Game Elements Module

# Import pygame to enable options related to object oriented programming and forming games in python
import pygame

# Formulate a class to be used to formulate a basket for an Egg Catcher Game
'''
This class will contain private variables within functions that will enable the programmer 
to manipulate different aspects of the basket including things like the size, dimensions,
movement (setter functions) along with being able to use accessor (getter) functions to access 
these components to be used when the programmer needs them
'''
class Basket:
    
    # Declare and initialize the private X positioning and Y positioning variables of the basket
    __xpos, __ypos = 0, 0
    
    # Declare and initialize the private width and height variables of the basket
    __width, __height = 0, 0
    
    # Declare and initialize the private basket variable that will eventually contain the image of the basket
    __imgBasket = None
    
    # Constructor - INIT 
    '''
    Formulate a constructor function whose purpose is to initialize private self variables and set default 
    values for the programmer in case the programmer chooses not to manipulate the variables him or herself.
    --> The function will contain 3 optional parameters if the programmer chooses to manipulate the image
    or the position of the image without using setter functions.
    '''
    def __init__(self, img=None, x=None, y=None):
        
        # Check if the user has not used the X position parameter and it is still equivalent to None
        if x == None:
            
            # Set the X position of the image to a default value of 0 (Pixels)
            self.__xpos = 0
            
        # Otherwise, the programmer has set an X position in the parameter
        else: 
            
            # Make the X position equal to the programmer's desired X position
            self.__xpos = x
        
        # Check if the user has not used the Y position parameter and it is still equivalent to None    
        if y == None:
            
            # Set the Y position of the image to a default value of 0 (Pixels)
            self.__ypos = 0
            
        # Otherwise, the programmer has set a Y position in the parameter
        else:
            
            # Make the Y position equal to the programmer's desired Y position
            self.__ypos = y
        
        # Check if the user has not used the image parameter and it is still equivalent to None
        if img == None:  
            
            # Set the image to a default image of a basket
            self.__imgBasket = pygame.image.load("images/basket.png")
        
        # Otherwise, the programmer has set an image for the basket
        else:
            self.__imgBasket = img
        
        # Set the private width variable to the image's actual width   
        self.__width = self.__imgBasket.get_width()
        
        # Set the private height variable to the image's actual height
        self.__height = self.__imgBasket.get_height()
    
    # Class function for basket movement
    '''
    Formulate a movement function whose purpose is to move the basket function towards
    a certain direction and at a certain speed determined by the amount of pixels the 
    basket will move with every iteration in the main program determined by the programmer.
    --> The function will contain 2 optional parameters if the programmer wants to 
    set a speed in pixels every iteration (integer) along with a string parameter that will
    determine the direction in which the basket object will move. The movement commands
    are shown below in the function along with their function.
    '''
    def move(self, pixels=1, direction="MOVEDOWN"):
        
        # Check if the direction set by the programmer is "MOVEUP"
        if direction == "MOVEUP":
            
            # Decrease the Y position of the basket image by the set number of pixels
            # Causes object to move up by 1 pixel each time
            self.__ypos = self.__ypos - pixels
        
        # Check if the direction set by the programmer is "MOVELEFT"
        elif direction == "MOVELEFT":
            
            # Decrease the X position of the basket image by the set number of pixels
            # Causes object to move left by 1 pixel each time
            self.__xpos = self.__xpos - pixels
        
        # Check if the direction set by the programmer is "MOVERIGHT" 
        elif direction == "MOVERIGHT":
            
            # Increases the X position of the basket image by the set number of pixels
            # Causes object to move right by 1 pixel each time
            self.__xpos = self.__xpos + pixels
        
        # Otherwise, check if the user has put any other value in the direction parameter of the function if any
        else:
            
            # The function will consider any other value as "MOVEDOWN"
            # Increases the Y position of the basket image by the set number of pixels
            # Causes object to move down by 1 pixel each time
            self.__ypos = self.__ypos + pixels
    
    '''
    Setter functions will enable the programmer to use our module to manipulate the values of things like 
    dimensions and location based on the programmer's needs on how they would like their basket object to look
    or act. Getter functions will enable the programmer to get these values to be used in their program
    to actually output and do whatever they need the function to do.
    '''
    # Class function for getting an image of a basket (Getter/ Accessor)
    # No parameters
    def getImage(self):
        
        # Return the image of the image of the basket
        return self.__imgBasket
    
    # Class function for setting the image of a basket (Setter/ Mutator)
    def setImage(self, img):
        
        # Store the image provided by the user in the private basket image variable
        self.__imgBasket = img
        
        # Set the private width variable to the image's actual width 
        self.__width = self.__imgBasket.get_width()
        
        # Set the private height variable to the image's actual height
        self.__height = self.__imgBasket.get_height()
            
    # Class function for getting the height of the image of the basket (Getter/ Accessor)
    def getHeight(self):
        
        # Return the height of the image of the basket
        return self.__height
    
    # Class function for getting the width of the image of the basket (Getter/ Accessor)
    def getWidth(self):
        
        # Return the width of the image of the basket
        return self.__width
    
    # Class function for getting the dimensions of the image of the basket (Getter/ Accessor)
    def getDimensions(self):
        
        # Return the height and width (dimensions) of the image of the basket as a tuple
        return (self.__height, self.__width)
    
    # Class function for getting the X position of the image of the basket (Getter/ Accessor)
    def getX(self):
        
        # Return the X position of the image of the basket
        return self.__xpos
    
    # Class function for getting the Y position of the image of the basket (Getter/ Accessor)
    def getY(self):
        
        # Return the Y position of the image of the basket
        return self.__ypos
    
    # Class function for getting the location of the image of the basket (Getter/ Accessor)
    def getLocation(self):
        
        # Return the X and Y position of the image as a tuple
        return (self.__xpos, self.__ypos)
    
    # Class function to set the X position of the image of the basket (Setter/ Mutator)
    # Function will contain 1 parameter to get the desired X position from the programmer
    def setX(self, x):
        
        # Set the X position of the basket image to the user's desired value
        self.__xpos = x
    
    # Class function to set the Y position of the image of the basket (Setter/ Mutator)
    # Function will contain 1 parameter to get the desired Y position from the programmer
    def setY(self, y):
        
        # Set the Y position of the basket image to the user's desired value
        self.__ypos = y
        
    # Class function to set the location of the image of the basket (Setter/ Mutator)
    # Function will contain 1 parameter to get the desired location from the programmer
    def setLocation(self, x, y):
        
        # Set the X position of the basket image to the user's desired value
        self.__xpos = x
        
        # Set the Y position of the basket image to the user's desired value
        self.__ypos = y   


# Formulate a class to be used to formulate an Egg for an Egg Catcher Game
'''
This class will contain private variables within functions that will enable the programmer 
to manipulate different aspects of the basket including things like the size, dimensions,
movement (setter functions) along with being able to use accessor (getter) functions to access 
these components to be used when the programmer needs them.
'''        
class Egg:
    
    # Declare and initialize the private X positioning and Y positioning variables of the egg
    __xpos, __ypos = 0, 0
    
    # Declare and initialize the private width and height variables of the egg
    __width, __height = 0, 0
    
    # Declare and initialize the private egg variable that will eventually contain the image of the egg
    __imgEgg = None
    
    # Declare and initialize a private boolean variable that determines whether or not the egg is broken
    __broken = False
    
    # Constructor - INIT 
    '''
    Formulate a constructor function whose purpose is to initialize private self variables and set default 
    values for the programmer in case the programmer chooses not to manipulate the variables him or herself.
    --> The function will contain 3 optional parameters if the programmer chooses to manipulate the image
    or the position of the image without using setter functions.
    '''
    def __init__(self, img=None, x=None, y=None):
        
        # Check if the user has not used the X position parameter and it is still equivalent to None
        if x == None:
            
            # Set the X position of the image to a default value of 0 (Pixels)
            self.__xpos = 0
            
        # Otherwise, the programmer has set an X position in the parameter
        else: 
            
            # Make the X position equal to the programmer's desired X position
            self.__xpos = x
        
        # Check if the user has not used the Y position parameter and it is still equivalent to None    
        if y == None:
            
            # Set the Y position of the image to a default value of 0 (Pixels)
            self.__ypos = 0
            
        # Otherwise, the programmer has set a Y position in the parameter
        else:
            
            # Make the Y position equal to the programmer's desired Y position
            self.__ypos = y
        
        # Check if the user has not used the image parameter and it is still equivalent to None
        if img == None:  
            
            # Set the image to a default image of a egg
            self.__imgEgg = pygame.image.load("images/egg.png")
        
        # Otherwise, the programmer has set an image for the egg
        else:
            
            # Set the image to the programmer's desired image
            self.__imgEgg = img
        
        # Set the private width variable to the image's actual width   
        self.__width = self.__imgEgg.get_width()
        
        # Set the private height variable to the image's actual height
        self.__height = self.__imgEgg.get_height()
        
        # Set the private broken variable to False as the egg is not broken yet
        self.__broken = False
    
    # Class function to return a still broken image of the egg
    # The egg should stop moving unless the user moves it anyways and the image should convert to a broken egg image
    '''
    --> The function will contain 3 optional parameters if the programmer chooses to manipulate the image
    or the position of the image without using setter functions.
    '''
    def breakEgg(self, img=None, x=None, y=None):
        
        # Check if the user has not used the X position parameter and it is still equivalent to None
        if x == None:
            
            # Set the X position of the image to a default value of 0 (Pixels)
            self.__xpos = self.__xpos + 0
            
        # Otherwise, the programmer has set an X position in the parameter
        else: 
            
            # Make the X position equal to the programmer's desired X position
            self.__xpos = x
        
        # Check if the user has not used the Y position parameter and it is still equivalent to None    
        if y == None:
            
            # Set the Y position of the image to a default value of 0 (Pixels)
            self.__ypos = self.__ypos + 0
            
        # Otherwise, the programmer has set a Y position in the parameter
        else:
            
            # Make the Y position equal to the programmer's desired Y position
            self.__ypos = y
        
        # Check if the user has not used the image parameter and it is still equivalent to None
        if img == None:  
            
            # Switch the image of the egg to an image of a cracked egg   
            self.__imgEgg = pygame.image.load("images/cracked_egg.png")

        # Otherwise, the programmer has set an image for the broken egg
        else:
            
            # Set the image to the programmer's desired image
            self.__imgEgg = img
            
        # Set the private width variable to the image's (Cracked egg) actual width   
        self.__width = self.__imgEgg.get_width()
        
        # Set the private height variable to the image's (Cracked egg) actual height
        self.__height = self.__imgEgg.get_height()
        
        # Set the private boolean determining whether the egg is broken or not to true
        self.__broken = True
         
    # Class function to reset the image of the egg back to a normal egg and in its initial location before dropping
    # This function will be the same as the constructor as one is trying to reset or re-initialize the location and image of the egg
    '''
    --> The function will contain 3 optional parameters if the programmer chooses to manipulate the image
    or the position of the image without using setter functions.
    '''
    def reset(self, img=None, x=None, y=None):
        
        # Reset all critical positional and image variables to reset the egg back to its original state before moving or breaking
        
        # Check if the user has not used the X position parameter and it is still equivalent to None
        if x == None:
            
            # Set the X position of the image to a default value of 0 (Pixels)
            self.__xpos = 0
            
        # Otherwise, the programmer has set an X position in the parameter
        else: 
            
            # Make the X position equal to the programmer's desired X position
            self.__xpos = x
        
        # Check if the user has not used the Y position parameter and it is still equivalent to None    
        if y == None:
            
            # Set the Y position of the image to a default value of 0 (Pixels)
            self.__ypos = 0
            
        # Otherwise, the programmer has set a Y position in the parameter
        else:
            
            # Make the Y position equal to the programmer's desired Y position
            self.__ypos = y
            
        # Check if the user has not used the image parameter and it is still equivalent to None
        if img == None:  
            
            # Reset the image to a default image of a egg
            self.__imgEgg = pygame.image.load("images/egg.png")
        
        # Otherwise, the programmer has set an image for the egg
        else:
            
            # Set the image to the programmer's desired image
            self.__imgEgg = img
        
        # Set the private width variable to the image's actual width   
        self.__width = self.__imgEgg.get_width()
        
        # Set the private height variable to the image's actual height
        self.__height = self.__imgEgg.get_height()
        
        # Set the private broken variable to False
        self.__broken = False
               
    # Class function returning a boolean determining whether or not the egg is broken
    def isBroken(self):
        
        # Return the boolean determining whether or not the egg has been broken
        return self.__broken
    
    # Class function for egg movement
    '''
    Formulate a movement function whose purpose is to move the egg towards
    a certain direction and at a certain speed determined by the amount of pixels the 
    basket will move with every iteration in the main program determined by the programmer.
    --> The function will contain 2 optional parameters if the programmer wants to 
    set a speed in pixels every iteration (integer) along with a string parameter that will
    determine the direction in which the egg object will move. The movement commands
    are shown below in the function along with their function.
    '''
    def move(self, pixels=1, direction="MOVEDOWN"):
        
        # Check if the direction set by the programmer is "MOVEUP"
        if direction == "MOVEUP":
            
            # Decrease the Y position of the egg image by the set number of pixels
            # Causes object to move up by 1 pixel each time
            self.__ypos = self.__ypos - pixels
        
        # Check if the direction set by the programmer is "MOVELEFT"
        elif direction == "MOVELEFT":
            
            # Decrease the X position of the egg image by the set number of pixels
            # Causes object to move left by 1 pixel each time
            self.__xpos = self.__xpos - pixels
        
        # Check if the direction set by the programmer is "MOVERIGHT" 
        elif direction == "MOVERIGHT":
            
            # Increases the X position of the egg image by the set number of pixels
            # Causes object to move right by 1 pixel each time
            self.__xpos = self.__xpos + pixels
        
        # Otherwise, check if the user has put any other value in the direction parameter of the function if any
        else:
            
            # The function will consider any other value as "MOVEDOWN"
            # Increases the Y position of the egg image by the set number of pixels
            # Causes object to move down by 1 pixel each time
            self.__ypos = self.__ypos + pixels
    
    '''
    Setter functions will enable the programmer to use our module to manipulate the values of things like 
    dimensions and location based on the programmer's needs on how they would like their egg object to look
    or act. Getter functions will enable the programmer to get these values to be used in their program
    to actually output and do whatever they need the function to do.
    '''
    # Class function for getting an image of a egg (Getter/ Accessor)
    # No parameters
    def getImage(self):
        
        # Return the image of the image of the egg
        return self.__imgEgg
    
    # Class function for setting the image of a egg (Setter/ Mutator)
    def setImage(self, img):
        
        # Store the image provided by the user in the private egg image variable
        self.__imgEgg = img
        
        # Set the private width variable to the image's actual width 
        self.__width = self.__imgEgg.get_width()
        
        # Set the private height variable to the image's actual height
        self.__height = self.__imgEgg.get_height()
            
    # Class function for getting the height of the image of the egg (Getter/ Accessor)
    def getHeight(self):
        
        # Return the height of the image of the egg
        return self.__height
    
    # Class function for getting the width of the image of the egg (Getter/ Accessor)
    def getWidth(self):
        
        # Return the width of the image of the egg
        return self.__width
    
    # Class function for getting the dimensions of the image of the egg (Getter/ Accessor)
    def getDimensions(self):
        
        # Return the height and width (dimensions) of the image of the egg as a tuple
        return (self.__height, self.__width)
    
    # Class function for getting the X position of the image of the egg (Getter/ Accessor)
    def getX(self):
        
        # Return the X position of the image of the egg
        return self.__xpos
    
    # Class function for getting the Y position of the image of the egg (Getter/ Accessor)
    def getY(self):
        
        # Return the Y position of the image of the egg
        return self.__ypos
    
    # Class function for getting the location of the image of the egg (Getter/ Accessor)
    def getLocation(self):
        
        # Return the X and Y position of the image as a tuple
        return (self.__xpos, self.__ypos)
    
    # Class function to set the X position of the image of the egg (Setter/ Mutator)
    # Function will contain 1 parameter to get the desired X position from the programmer
    def setX(self, x):
        
        # Set the X position of the egg image to the user's desired value
        self.__xpos = x
    
    # Class function to set the Y position of the image of the egg (Setter/ Mutator)
    # Function will contain 1 parameter to get the desired Y position from the programmer
    def setY(self, y):
        
        # Set the Y position of the egg image to the user's desired value
        self.__ypos = y
        
    # Class function to set the location of the image of the egg (Setter/ Mutator)
    # Function will contain 1 parameter to get the desired location from the programmer
    def setLocation(self, x, y):
        
        # Set the X position of the egg image to the user's desired value
        self.__xpos = x
        
        # Set the Y position of the egg image to the user's desired value
        self.__ypos = y   


        
    
    
    
    
    
    
    
    
    