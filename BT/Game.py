import pygame
import random
import sys


class Circle(pygame.sprite.Sprite):

    def __init__(self, x, y, radius, colors, gravity):
        pygame.sprite.Sprite.__init__(self)

        self.radius = radius
        color = random.choice(colors)
        self.gravity = gravity

        self.surface = pygame.Surface([2*radius, 2*radius], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.circle(self.surface, color, (radius,radius), radius)

    def fall(self):
        self.rect.y += self.gravity

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

class Rectangle(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.Surface([w, h])
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surface.fill(color)
        self.velocity = 0

    def move(self):
        self.rect.x += self.velocity

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

class Game:
    
    def __init__(self):
        # Initialize pygame object
        pygame.init()

        # Set size of screen
        screenWidth = 500
        screenHeight = 750
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.circleColors = [
                            '#F94892',
                            '#FF7F3F',
                            '#FBDF07',
                            '#89CFFD',
                            '#1CD6CE',
                            '#FEDB39',
                            '#B4FF9F',
                            ]

        self.circleList = []
        self.rectangle = Rectangle(250, 730, 150, 20, '#293462')
        self.score = 0

    def update(self):
        w, h = self.screen.get_size()

        # Move rectangle
        self.rectangle.move()
        if self.rectangle.rect.x <= 0:
            self.rectangle.rect.x = 0
        if self.rectangle.rect.x >= w - self.rectangle.rect.w:
            self.rectangle.rect.x = w - self.rectangle.rect.w

        # Move circle
        for circle in self.circleList:
            circle.fall()
            outOfScreen = circle.rect.y - circle.radius >= h
            # If circle out of screen, it disappear
            if outOfScreen:
                self.circleList.remove(circle)

            isCollide = pygame.sprite.collide_rect(circle, self.rectangle)
            if isCollide:
                self.circleList.remove(circle)
                self.score += 1

        if len(self.circleList) <= 5:
            x = random.randint(50, w - 50)
            y = 0
            gravity = random.randint(2, 7)
            circle = Circle(x, y, 20, self.circleColors, gravity)
            self.circleList.append(circle)
        for circle in self.circleList:
            circle.draw(self.screen)
        self.rectangle.draw(self.screen)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.score), True, '#293462')
        textRect = text.get_rect()
        textRect.center = (w//2, 32)
        self.screen.blit(text, textRect)

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        # Game loop
        while True:
            clock.tick(60)
            # Get event
            for event in pygame.event.get():
                # Handle exit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    # Move event
                    if event.key == pygame.K_a:
                        self.rectangle.velocity = -5
                    if event.key == pygame.K_d:
                        self.rectangle.velocity = 5
                # Stop event
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.rectangle.velocity = 0

            # Fill screen by gray
            self.screen.fill('#6E85B7')
            self.update()

def main():
    """ Main function."""
    game = Game()
    game.run()
# Run function main.
if __name__ == "__main__":
    main()