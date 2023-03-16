# File Created by: Julian Gospich
# Import the libraries
# My sources are: Pygame.org
from time import sleep 
from random import randint
import pygame as pg
import os
choices = ["Big rock","Lil paper","Sharp scissors"]
def RESULT(computer, player):
    if player == computer:
        return("We had the same thing therefore We tied!!!!!!!!!!!!!!!")
    # lines 88-105 are all the winning-losing scenarios of the game,  telling the computer how to play the game    
    elif player == "Big rock":
        if computer == "Sharp scissors":
            return("You have chosen Big rock, computer chose Sharp scissors... you won!")
        elif computer == "Lil paper":
            return("You have chosen Big rock, computer chose Lil paper... you lost!")
    elif player == "Sharp scissors":
        if computer == "Lil paper":
            return("You have chosen Sharp scissors, computer chose Lil paper... you won!")
        elif computer == "Big rock":
            return("You have chosen Sharp scissors, computer chose Big rock... you lost!")
    elif player == "Lil paper":
        if computer == "Big rock":
            return("You have chosen Lil paper, computer chose Big rock... you won!")
        elif computer == "Sharp scissors":
            return("You have chosen Lil paper, computer chose  Sharp scissors; you lost!")                  
    else:
        return "Error"

def guess():
    result = choices[randint(0,2)]
    return result  

def render_message(text): 
    m = font.render(text, True, GREEN)
    m_rect = m.get_rect()
    m_rect.bottom = screen_rect.top - (m_rect.top - m_rect.bottom)
    return (m, m_rect)

# setup asset folders - images and sounds
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1150
HEIGHT = 650
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (255, 255, 255)
BLUE = (255, 255, 255)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()

pg.display.set_caption(" Big Rock, Lil Paper, Sharp Scissors...")
clock = pg.time.Clock()

# # sounds
#scissors_sound = pg.mixer.Sound(os.path.join(game_folder, "scissors.wav"))

rock_image = pg.image.load(os.path.join(game_folder, 'roks.jpg')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paperfinal.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'Finalscissors7.jpg')).convert()
# creates transparency 
rock_image.set_colorkey(GREEN)
paper_image.set_colorkey(GREEN)
scissors_image.set_colorkey(GREEN)

screen.blit(rock_image, (400,200))
screen.blit(paper_image, (100,475))
screen.blit(scissors_image, (500,195))

# gets the geometry of the image
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
# places the images above each other
scissors_rect = scissors_image.get_rect()
paper_rect.left = rock_rect.right
scissors_rect.left = paper_rect.right

font = pg.font.SysFont(None,37)
(message, message_rect) = render_message("Choose Big rock, Lil paper or Sharp scissors")

# Computer guess is variable that returns 1 of 3 possible guesses of Big rock, Lil paper, or Sharp scissors
computer_guess = guess()

running = True
while running:
    clock.tick(FPS)
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            # print(mouse_coords)
            # print(mouse_coords[0])
            # print(mouse_coords[1])
            if rock_rect.collidepoint(mouse_coords):
                # calls function to compare computer choice and user choice (RESULT)
                result = RESULT(computer_guess, "Big rock")
                # returns the message and the rect (location) of the text, 
                # then displays the result of comparing user choice and the computers choice
                (message, message_rect) = render_message(result)  
                #returning Big rock, Lil paper, or Sharp scissors: selects the next computer guess
                computer_guess = guess()
            elif paper_rect.collidepoint(mouse_coords):
                result = RESULT(computer_guess, "Lil paper")
                (message, message_rect) = render_message(result)  
                computer_guess = guess()              
            elif scissors_rect.collidepoint(mouse_coords):
                result = RESULT(computer_guess, "Sharp scissors")
                (message, message_rect) = render_message(result)  
                computer_guess = guess()              
               

           
            # if mouse_coords[0] <= 500 and mouse_coords[1] <= 500:
            #  if mouse_coords == pg.mouse.get_pos():
            #     print("I clicked on the Big rock...")
    
    # get input from player...

    # update
    # Big rock_rect.y += 1
    # Lil paper_rect.y += 1
    # Sharp scissors_rect.x += 1
    # Sharp scissors_rect.y += 1
    
    # screen fill "resets" screen, blit is drawing the images on the screen
    screen.fill(BLACK)
    screen.blit(scissors_image, scissors_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(rock_image, rock_rect)
    screen.blit(message, message_rect)
    

    pg.display.flip()
pg.quit()
