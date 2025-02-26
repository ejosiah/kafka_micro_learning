from threading import Thread
from threading import Lock
import pygame
import locale

def get_color(value):
    if value == 0 :
        return 'black'
    elif value < 0 :
        return 'red'
    return 'green'

def format_currency(amount):
    locale.setlocale(locale.LC_ALL, 'C')
    return '${:,.2f}'.format(amount)


class UI(Thread):
    def __init__(self, profitTracker):
        Thread.__init__(self)
        self.pt = profitTracker
        self.font_size = 50
        pygame.init()
        pygame.font.init()
        self.resolution = (750, 150)
        pygame.display.set_caption("Sales profit tracker")
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('./JetBrainsMono-Regular.ttf', self.font_size)
        self.margin = 10

    def render(self, label, value, color, line):
        text = self.font.render(label, True, 'black')
        rect = text.get_rect()
        y = line * (rect.height + self.margin)
        rect.topleft = (0, y)
        self.screen.blit(text, rect)

        x = rect.width + self.margin
        text = self.font.render(value, True, color)
        rect = text.get_rect()
        rect.topleft = (x, y)
        self.screen.blit(text, rect)

    def run(self):
        print("ui started")
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("white")
            
            last_profit = self.pt.profits[-1]
            total = self.pt.total()



            self.render("Last Sale:", format_currency(last_profit), get_color(last_profit), 0)
            self.render("total profit:", format_currency(total), get_color(total), 1)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.font.quit()
        pygame.quit()
        print("UI succesfully shutdown")


