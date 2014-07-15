#!/usr/bin/python
'''
Title: Hangman
Description: A Simple Hangman Game 
Author: Usman Sher (@usmansher) 

Disclaimer: Its Just A Small Guessing Game made By Me (Beginning Of Coding).
'''

# Imports
import pygame, sys
from pygame.locals import *
from random import choice

# Color Variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 100, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Get The Words From a Text File
def getWords():
    f = open('wordlist.txt')
    words = []
    getLines = f.readline()
    while getLines:
        words.append(getLines.strip())
        getLines = f.readline()
    return words

# Word Spaces
def drawWordSpaces(screen, spaces):
    x = 10
    for i in range(spaces):
        pygame.draw.line(screen, ORANGE, (x, 350), (x+20, 350), 3)
        x += 30
        
# Letters
def drawLetter(screen, font, word, guess):
    x = 10
    for letter in word:
        if letter == guess:
            letter = font.render(letter, 3, BLACK)
            screen.blit(letter, (x, 300))
        x += 30
        
# Get Unique Letters
def getUniqLetters(word):
    unique= ''
    
    for letter in word:
        if letter not in unique:
            unique += letter
    return unique

# Gallows
def drawGallows(screen):
    pygame.draw.rect(screen, BLUE, (450, 350, 100, 10)) 
    pygame.draw.rect(screen, BLUE, (495, 250, 10, 100))
    pygame.draw.rect(screen, BLUE, (450, 250, 50, 10))
    pygame.draw.rect(screen, BLUE, (450, 250, 10, 25))

# Body Parts
def drawMan(screen, bodyPart):
    if bodyPart == 'head':
        pygame.draw.circle(screen, RED, (455, 285), 10)
    if bodyPart == 'body':
        pygame.draw.rect(screen, RED, (453, 285, 4, 50))
    if bodyPart == 'lArm':
        pygame.draw.line(screen, RED, (455, 310), (445, 295), 3)
    if bodyPart == 'rArm':
        pygame.draw.line(screen, RED, (455, 310), (465, 295), 3)
    if bodyPart == 'lLeg':
        pygame.draw.line(screen, RED, (455, 335), (445, 345), 3)
    if bodyPart == 'rLeg':
        pygame.draw.line(screen, RED, (455, 335), (465, 345), 3)

# The Main Function
def main():
    x = 800
    y = 500
    pygame.init() # Initialize Pygame 
    screen = pygame.display.set_mode((x, y)) # Set The Screen Size
    pygame.display.set_caption('Hangman By Usman Sher')
    screen.fill(WHITE) # Fill The Background
    font = pygame.font.SysFont('Courier New', 40) # Set Font & Size
    drawGallows(screen) # Draw The Gallows
    guessed = '' 
    words = getWords() # Get Words
    word = choice(words) # Get one word from words
    drawWordSpaces(screen, len(word)) # Draw The Word Spaces
    print word
    
    body = ['rLeg', 'lLeg', 'rArm', 'lArm', 'body', 'head'] # Body Parts
    correct = '' 
    unique = getUniqLetters(word)# Get Unique Words from the Word
    pygame.display.update()# Update The Display
    while body and len(correct) < len(unique): # While Bodyparts or Correct Guess is less than Unique Words
        # Keyboard Events
        for event in pygame.event.get(): 
            # Enable the Quit Button
            if event.type == QUIT:
                sys.exit()
            # If Key is pressed
            if event.type == KEYDOWN:
                # Check Whether Its a Alphabet or not
                if event.unicode.isalpha():
                    guess = event.unicode #Store Alphabet in variable guess
                    # Check Whether Guessed Word is Right Or Wrong
                    if guess in word and guess not in correct: 
                        #if it is
                        drawLetter(screen, font, word, guess) #Print The Letter on Screen
                        pygame.display.update() # Update The Display
                        correct += guess # Add Guessed Letter to Correct 
                    elif guess not in guessed:
                        # If Its Wrong
                        bodyPart = body.pop() # Delete a Bodypart and add it the the variable bodyPart
                        drawMan(screen, bodyPart) # Draw the Man with the Popped Bodypart
                        pygame.display.update() # Update the Display
                        guessed += guess # Add it to variable guessed
    if body: # Check Whether theres a part left in variable body 
        text = 'You Won!'# If True 
    else:
        text = 'You Lose! The word was '+ word # If False
    # print the Text
    endMessage = font.render(text, 3, BLACK) 
    screen.blit(endMessage, (0, 0))
    pygame.display.update()
    # Enable Quit Button
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
# Run The Program
if __name__ == '__main__':
    main()