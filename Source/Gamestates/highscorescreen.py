import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer
from UI.button import Button
from messagewindow import MessageWindow

class HighScoreScreen:

    def __init__(self, manager, scoreManager, screen):
        self.stateManager = manager
        self.highScoreManager = scoreManager
        self.window = screen
        
        self.uiContainer = UIContainer(self.window)
        self.uiContainer.verticalStride = 0

        self.screenInfo = pygame.display.Info()
        
        self.titleFont = pygame.font.SysFont("monospace", 75, bold=True)
        self.scoreFont = pygame.font.SysFont("monospace", 45)
        self.textColour = (128, 128, 128)
        
        self.initiateReset = False

        # Create the message box
        centerX = self.screenInfo.current_w / 2
        centerY = self.screenInfo.current_h / 2
        message = "WARNING: That action cannot be undone. Are you positive you want to reset the scores to their default state?"
        self.resetMessage = MessageWindow(self.window, message, 650, 300, centerX, centerY)

        # Get most recent scores
        self.highScores = self.highScoreManager.getCurrentHighScores()
        self.initialHighScoreLoad = True
        self.updateHighScores()

        # Button sizes
        width = 170
        height = 40

        # Back button
        self.backButton = self.uiContainer.add_button("Back")
        self.backButton.rect = pygame.Rect((110 - (width / 2), self.screenInfo.current_h - 50 - (height / 2), width, height))

        # Reset button
        self.resetButton = self.uiContainer.add_button("Reset Highscores")
        self.resetButton.rect = pygame.Rect(self.screenInfo.current_w - 280 - (width / 2), self.screenInfo.current_h - 50 - (height / 2), width*2, height)

        self.reset_acceptButton = self.resetMessage.addButton("Yes, I'm sure", (-285, 95), (260, 30))
        self.reset_cancelButton = self.resetMessage.addButton("No", (165, 95), (130, 30))
        
        self.backButton.baseColour = self.resetButton.baseColour = (0, 0, 0)
        self.reset_cancelButton.baseColour = self.reset_acceptButton.baseColour = (16, 16, 16)
        
        self.resetMessage.textFont = pygame.font.SysFont("monospace", 30)
        
        hoverFill = 1
        hoverColour = (255, 255, 255)
        clickColour = (128, 128, 128)
        for button in self.uiContainer.components:
            if isinstance(button, Button):
                button.hoverColour = hoverColour
                button.clickColour = clickColour
                button.hoverFill = hoverFill
                button.font = pygame.font.SysFont("monospace", 30)
                
        for button in self.resetMessage.uiContainer.components:
            if isinstance(button, Button):
                button.hoverColour = hoverColour
                button.clickColour = clickColour
                button.hoverFill = hoverFill
                button.font = pygame.font.SysFont("monospace", 30)
                
    def start(self):
        if self.initialHighScoreLoad:
            self.initialHighScoreLoad = False
        else:
            self.updateHighScores()

        # Reset the reset variable - lol
        self.initiateReset = False
        pass

    def updateHighScores(self):
        """
        Updates the high score tuple.
        """
        self.highScores = self.highScoreManager.getCurrentHighScores()
        self.highScoreTuples = ((self.highScores["first"]["name"], self.highScores["first"]["score"]),
                                (self.highScores["second"]["name"], self.highScores["second"]["score"]),
                                (self.highScores["third"]["name"], self.highScores["third"]["score"]),
                                (self.highScores["fourth"]["name"], self.highScores["fourth"]["score"]),
                                (self.highScores["fifth"]["name"], self.highScores["fifth"]["score"]),
                                (self.highScores["sixth"]["name"], self.highScores["sixth"]["score"]),
                                (self.highScores["seventh"]["name"], self.highScores["seventh"]["score"]),
                                (self.highScores["eighth"]["name"], self.highScores["eighth"]["score"]),
                                (self.highScores["ninth"]["name"], self.highScores["ninth"]["score"]),
                                (self.highScores["tenth"]["name"], self.highScores["tenth"]["score"]))

    def update(self):
        self.updateHighScores()

        if not self.initiateReset:
            if self.backButton.was_pressed() or xo_input.escape:
                self.stateManager.switchGameState("MainScreen")
            if self.resetButton.was_pressed():
                self.initiateReset = True

            self.uiContainer.update()
        else:
            self.resetMessage.update()
            if self.reset_cancelButton.was_pressed():
                self.initiateReset = False
            if self.reset_acceptButton.was_pressed():
                self.highScoreManager.resetHighScores()
                self.updateHighScores()
                self.initiateReset = False

    def draw(self):
        # Draw the high scores
        self.drawText("HIGH SCORES", self.titleFont, 0, -225)
        y = -165
        for tuple in self.highScoreTuples:
            self.drawTextWithTuple(tuple, self.scoreFont, 0, y)
            y += 45

        # Draw the UI
        self.uiContainer.draw()

        # Draw the reset message
        if self.initiateReset:
            self.resetMessage.draw()
    
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