import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer

class HighScoreScreen:

    def __init__(self, manager, scoreManager, screen):
        self.stateManager = manager
        self.highScoreManager = scoreManager
        self.window = screen
        
        self.uiContainer = UIContainer(self.window)
        
        self.screenInfo = pygame.display.Info()
        
        self.titleFont = pygame.font.SysFont("monospace", 45, bold=True)
        self.scoreFont = pygame.font.SysFont("monospace", 20)
        self.textColour = (128, 128, 128)
        
        self.initiateReset = False
        pass

    def start(self):
        #Get most recent scores
        self.highScores = self.highScoreManager.getCurrentHighScores()
        
        # Reset the reset variable - lol
        self.initiateReset = False
        
        # Button sizes
        width = 150
        height = 20

        # Back button
        self.backButton = self.uiContainer.add_button()
        self.backButton.rect = pygame.Rect((100 - (width / 2), self.screenInfo.current_h - 50 - (height / 2), width, height))
        self.backButton.text = "Back"

        # Reset button
        self.resetButton = self.uiContainer.add_button()
        self.resetButton.rect = pygame.Rect(self.screenInfo.current_w - 100 - (width / 2), self.screenInfo.current_h - 50 - (height / 2), width, height)
        self.resetButton.text = "Reset Highscores"
        pass
        
    def update(self):
        self.highScores = self.highScoreManager.getCurrentHighScores()
        
        if not self.initiateReset:
            if self.backButton.was_pressed():
                self.stateManager.switchGameState("MainScreen")
            if self.resetButton.was_pressed():
                self.initiateReset = True

            self.uiContainer.update()
        else:
            if xo_input.btn_check:
                self.stateManager.switchGameState("MainScreen")
    
    def draw(self):
        self.drawText("HIGH SCORES", self.titleFont, 0, -130)
        self.drawTextWithTuple((self.highScores["first"]["name"], self.highScores["first"]["score"]), self.scoreFont, 0, -95)
        self.drawTextWithTuple((self.highScores["second"]["name"], self.highScores["second"]["score"]), self.scoreFont, 0, -70)
        self.drawTextWithTuple((self.highScores["third"]["name"], self.highScores["third"]["score"]), self.scoreFont, 0, -45)
        self.drawTextWithTuple((self.highScores["fourth"]["name"], self.highScores["fourth"]["score"]), self.scoreFont, 0, -20)
        self.drawTextWithTuple((self.highScores["fifth"]["name"], self.highScores["fifth"]["score"]), self.scoreFont, 0, 5)
        self.drawTextWithTuple((self.highScores["sixth"]["name"], self.highScores["sixth"]["score"]), self.scoreFont, 0, 30)
        self.drawTextWithTuple((self.highScores["seventh"]["name"], self.highScores["seventh"]["score"]), self.scoreFont, 0, 55)
        self.drawTextWithTuple((self.highScores["eighth"]["name"], self.highScores["eighth"]["score"]), self.scoreFont, 0, 80)
        self.drawTextWithTuple((self.highScores["ninth"]["name"], self.highScores["ninth"]["score"]), self.scoreFont, 0, 105)
        self.drawTextWithTuple((self.highScores["tenth"]["name"], self.highScores["tenth"]["score"]), self.scoreFont, 0, 130)
        
        self.uiContainer.draw()
        pass
    
    def final(self):
        pass
        
    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        self.window.blit(label, ((self.screenInfo.current_w/2) - (text_width/2) + offsetX, (self.screenInfo.current_h/2) - (text_height/2) + offsetY))
        
    def drawTextWithTuple(self, tuple, font, offsetX, offsetY):
        text_width, text_height = font.size(tuple[0])
        text = str(tuple[0]) + " : " + str(tuple[1])
        label = font.render(text, 1, self.textColour)
        self.window.blit(label, ((self.screenInfo.current_w/2) - text_width + offsetX, (self.screenInfo.current_h/2) - (text_height/2) + offsetY))