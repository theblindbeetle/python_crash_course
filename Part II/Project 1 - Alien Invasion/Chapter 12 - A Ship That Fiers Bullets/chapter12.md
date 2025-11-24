# Chapter 12: A Ship that Fires Bullets
### Let's build a game called *Alien Invasion!*
We'll use the `Pygame` modules that manage graphics, animation and sound.<br>
In this chapter you'll set up Pygame and then create a rocket ship that 
moves left and right and fires bullets in response to player input.
> While building this game, <i><b>you'll learn how to manage large projects
> that span multiple files</b></i>.

We'll refactor a lot of code and manage file contents to organize the project
and make the code efficient.

> NOTE:<br>
> Aline Invasion spans a number of different files, so make a new
> alien_invasion folder on your system. Be sure to save all the files 
> for the project to this folder so your import statements will work correctly.
> <br>&emsp;Also, if you feel comfortable using version control you might
> want to use it for this project.
> 
---
## 12.1 Planning Your Project
When you build a project it's important to have a plan. So that, when you
write code it has a purpose to accomplish, and you can complete the project.

Here's a general gameplay's description. It doesn't cover every aspect
of the game, but provides a clear idea of how to start building the game.

> In *Alien Invasion*, the player controls a rocket ship that appears at
> the bottom center of the screen. The player can move the ship right 
> and left using the arrow keys and shoot bullets using the space-bar.<br>
> When the game begins, a fleet of aliens fills the sky and moves across
> and down the screen. The player shoots and destroys the aliens.<br> 
> If the player shoots all the aliens, the new fleet that appears moves
> faster than the previous fleet. If any alien hits the player's ship or
> reaches the bottom of the screen, the player loses ship. If the player
> loses three ships, the game ends.

In this first stage we create a ship that moves left and right and fires
bullets when pressing the space-bar. After setting up this behavior, we can
create aliens and refine the gameplay.

---
## 12.2 Installing Pygame
The pip module helps to install Python packages. Try the following command:
```commandline
python -m pip install pygame
```
If the previous one doesn't work try with the `--user` flag: 
```commandline
python -m pip install --user pygame
```

---
## 12.3 Starting the Game Project
Let's start with an empty Pygame window. Later we are going to:
* draw the game elements:
  * ship
  * aliens
* make the game respond to user input
* set background color
* load a ship image

### 12.3.1 Creating a Pygame Window and Responding to User Input
Let's create a Pygame window to represent the game.
> NOTE:
> The files of every section will be on each folder as usual.
> But also, as this is a project, and we want all the files to work together,
> you'll see that on the folder 
> <b><i>'../Project 1 - Alien Invasion/alien_invasion/'</i></b>.


```python
# REFER: ../Project 1.../alien_invasion.py
# REFER: ../12.3.../12.3.1.../aline_invasion.py
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently draw screen visible.\
            pygame.display.flip()

if __name__ == '__main__'
    #Make a game instance, and run the game.
        ai = AlienInvasion()
        ai.run_game()
```
> NOTE:<br> This chunk of piece of code have double reference because we
> are adding the files in individual sections such as the project's folder.
> Each individual section contains the piece of code related to the current
> chapter, while the project's folder contains the final results

Let's break code down:
* We import `sys` and `pygame` modules. _*1_
* *Alien Invasion* starts the class `AlienInvasion`
  * In the `__init__()` method:
      * The `pygame.init()` function initialize the background settings 
      that Pygame needs to work properly.
      * The `pygame.display.set_mode()` creates the display window. _*2_
      * The display window is assign to `self.screen`, which is in the
        `__init__()` method,
        making `self.screen` available in every method in the class. _*3_
  * The game is controlled by the `run_game()` method, which contains a 
    `while` loop running continually, and contains:
    * A `for` loop managing the screen updates, which is an *event loop*. _*4_
    * To access the events that Pygame detects, we'll use the
      `pygame.evente.get()` function. _*5_
      * The call to `pygame.display.flip()` tells Pygame to make the most
        recent ly drawn screen visible. _*6_
* At the end we create an instance of the game, and call `run_game()`. _*7_

> NOTES:
> 1. The modules we import are: 
>    * The `sys` module is for exiting the game when the player quits.
>    * The `pygame` module contain functionalities we need to make the game.
> 2. The display window arguments define the size of the game window. 
> This values can be adjusted as needed, depending on the screen size:
>    * 1200 pixels wide 
>    * 800 pixels high.
> 
> 3. The object assigned to `self.screen` is called *surface*. A surface in
> Pygame is a part of the screen where a game element can be displayed.
> Each element in the game, like an alien or a ship, is its own surface.
> The surface returned by `display.set_mod()` represents the entire 
> game window. When we activate the game's animation loop. this surface will
> be redrawn on every pass through the loop, so it can be updated with any
> changes triggered by the user input.
> 
> 4. An *event* is an action that the user performs while playing the game,
> such as pressing a key or moving the mouse. To make our program respond to
> events, we write this *event loop* to listen for the events and perform
> appropriate tasks depending on the kinds of events that occur.
> 
> 5. The `pygame.evente.get()` function returns a list of events between
> the last time it was called and the new call. Any keyboard or mouse event
> causes the for loop to run. We'll write a series of `if` in the loop to
> detect and respond to events. For example, when the player clicks the 
> game window's close button, a `pygame.QUIT` event is detected and call
> `sys.exit()` to exit the game.
> 
> 6. Every time the call to `pygame.display.flip()` pass through the `while`
> loop, the most recent drawn is displayed and the previous erased. This
> currently projects an empty screen.<br>
> `pygame.display.flip()` updates the display to show the new position the
> game elements and hide the old ones creating the illusion of 
> smooth movement.
> 
> 7. The game is placed in an `if` block so that only runs if the file is
> called directly. When you run this alien_invasion.py file, you should
> see an empty window.

### 12.3.2 Setting the Background Color
If you already executed the program, you've noticed the black background.
We'll change that at the end of the `__init__()` method:
```python
# REFER: ../Project 1.../alien_invasion.py
# REFER: ../12.3.../12.3.2.../aline_invasion.2.py
--ship--

    def __init__(self):
        --snip--
        pygame.display.set_caption("Alien Invasion")
        
        
        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        --snip--
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently draw screen visible.\
            pygame.display.flip()
--snip--
```
Pygame uses RGB colors (a mix of red, green, and blue). The colors go in
a range from 0 to 255. The most pure colors are: 
* red (255, 0, 0)
* green (0, 255, 0)
* blue (0, 0, 255)

Any other is a mix of those values. The clor `(230, 230, 230)` is an equal
amount of red, green, and blue, and results in the light grey color we use
for the background. This color is assigned to `self.bg_color`.
The other thing we added is the method `fill()` which fills the background,
which act on a surface and takes only the color argument.

### 12.3.3 Creating a Settings Class
New functionalities commonly require also new settings. Let's put all the 
values together in a module `settings` with a class `Settings`.
While working with the code, this helps to access all the settings 
through one single object, instead of multiple individual settings.
Also, gets easier working with the appearance and behavior as our project
grows. Let's create the _settings.py_ inside the `../alien_invasion/` folder,
and add this initial `Settings` class:
```python
# REFER: ../Project 1.../settings.py
# REFER: ../12.3.../12.3.3.../settings.py
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```
Now we need to adapt the `alien_invasion.py` so it can use the module
_settings_:
```python
# REFER: ../Project 1.../alien_invasion.py
# REFER: ../12.3.../12.3.1.../aline_invasion.3.py
--snip--
import Pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
          (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        --snip--
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
--snip--
```
What changed?
* We import the `Settings` class into the main program.
* And create an instance of `Settings`, which is assigned to `self.settings`.
* When we create a screen, we use the attributes of `Settings` on `set_mode(),
  where we use:
  * `screen_width`.
  * `screen_height`.
* To set the background we use `self.settings.bg_color`.

All the changes are made to improve the structure of the code, and no
visible changes when you run the program for now.

---
## 12.4 Adding the Ship Image
Let's add a ship to the game. With Pygame the `blit()` method draws an image
on the scree, which has to be loaded on our project.
In the project's folder `../alien_invasion/` let's add the folder `/images`
and let's add an image for our ship.

You can get the image _ship.bmp_ from the resources of the book 
(https://nostarch.com/pythoncrashcourse2e/).
If you want to use a different one you can do it.
Consider Pygame loads by default bitmap images (*.bmp), but you can
configure Pygame to use other file types.

If you have an image with a different format (the most populars jpg and png),
you can convert them to bitmap using Photoshop, GIMP, and Paint.

Also, if you're using a different image get one that the background is
transparent or a solid color, so you can easily make it equals to the image's
background color.

![ship.bmp](..%2Faline_invasion%2Fimages%2Fship.bmp)
<br>Figure 12-1: The ship for Alien Invasion

### 12.4.1 Creating the Ship Class
We need to display the ship, so we create a new module containing the class
`Ship` which manages most of the behavior of the player's ship:
```python
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```
Pygame lets you treat all elements like rectangles, even if they are not.
This approach works well enough that no player would notice that a collision
of elements with different shapes are handled as rectangles.

Let's describe the code:
* We import pygame module, and then define the class `Ship`.
* The `__init__()` method of `Ship` takes two parameters:
  * the `self` reference
  * the reference to the current instance of "AlienInvasion" `ai_game`.
* In the method we assign the screen so we can access easily ot it.
* The screen's `rect` attribute, through the `get_rect()` method, which assigned
to `self.screen_rect` places the ship in the correct location on the screen. 
* To load the image, we call `pygame.image.load()` and give it the location
of our ship image. This function returns the surface representing the ship,
which we assign to `self.ship`.
* Then, we call `get_rect()` to access the ship surface's `rect` attribute so
we can later use it to place the ship.

When you work with the `rect` object, you can use the x/y coordinates of the 
top, bottom, left, and right edges of the rectangle, as well as the center, to
place the object.<br>
When you center a game element, use `center`, `centerx`, or `centery` attributes
of `rect`. When you work at an edge, use `top`, `bottom`, `left`, or `right`
attributes. There are also attributes that combine these properties; `midbottom`
, `midtop`, `midleft`, and `midright`.<br>
You can also, just use the `x` and `y` attributes, which are coordinates from
the top left corner.

> NOTE: In Pygame, the origin (0, 0) is in the top-left corner of the screen,
and coordinates increase as you go down and to the right. On a 1200 by 800 
screen, the origin is in the top-left corner, and the bottom-right corner has
the coordinates (1200, 800). These coordinates refer to the game window, not 
the physical screen.

The ship will be set at the bottom center of the screen. Let's use the 
`midbottom` attribute of the screen's `rect`.
* `rect` is used to position the ship image so it's centered horizontally and
aligned with the bottom of the screen.
* The `blitme()` method draws the image to the screen at the position specified
by `self.rect`.

### 12.4.2 Drawing the Ship to the Screen
Now let's update `alien_invasion.py` to create a ship and calls the ship's
`blitme()` method:
```python
# REFER: ../Project 1.../alien_invasion.py
# REFER: ../12.4.../12.4.2.../aline_invasion.4.py
--ship--
from settings import Settings
from ship import Ship

class AlineInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        --snip--
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)

    def run_game(self):
        --snip--
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # Make the most recently draw screen visible.\
        pygame.display.flip()
--ship--
```
besides of the import we have two new lines:
* `self.ship = Ship(self)` The call to Ship() requires one argument, an instance
of AlienInvasion. The `self` argument refers to the instance of `AlienInvasion`,
giving to `Ship` access to the game's resources. And, `self.ship` is an instance
of `Ship`.
* `slef.ship.blitme()` with this, after filling the background we draw the ship
on the screen by calling the function. So, the ship appears on top of the
background.

---
## 12.5 Refactoring: The _check_events() and _update_screen() Methods
### 12.5.1 The _check_events() Method
### 12.5.2 The _update_screen() Method

---
## 12.6 Piloting the Ship
### 12.6.1 Responding to a Keypress
### 12.6.2 Allowing Continuous Movement
### 12.6.3 Moving Both Left and Right
### 12.6.4 Adjusting the Ship's Speed
### 12.6.5 Refactoring _check_events()
### 12.6.6 Pressing Q to Quit
### 12.6.7 Running the game in Fullscreen Mode

---
## 12.7 A Quick Recap
### 12.7.1 alien_invasion.py
### 12.7.2 settings.py
### 12.7.3 ship.py

---
## 12.8 Shooting Bullets


