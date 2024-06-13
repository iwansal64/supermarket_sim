import global_variables
import pygame
from typing import Callable, Tuple, Optional

class UI():
    def __init__(self, width: int, height: int, title: str, fps: int = 60):
        '''Initialize UI'''
        pygame.init()
        
        self.screen = pygame.display.set_mode((width, height)) #? Set screen

        pygame.display.set_caption(title) #? Set caption
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.running = True
        
    def fill_screen(self, color: Tuple[int, int, int]):
        '''Fill Screen or Change Screen Background'''
        self.screen.fill(color)
        
    def update_screen(self):
        '''Update Screen From Changes'''
        pygame.display.flip()
        self.clock.tick(self.fps)
        
    def add_text(self, text:str, pos:Tuple[int, int], color:Tuple[int, int, int]=(0, 0, 0), bgc:Optional[Tuple[int, int, int]]=None, font_size:int=48, font_family:str="calibri"):
        '''Add Text Into The Screen'''
        font = pygame.font.SysFont(font_family, font_size) #? Set up font
        text_element = font.render(text, True, color, bgc) #? Render font
        text_rect = text_element.get_rect(topleft=pos) #? Get text rect
        self.screen.blit(text_element, text_rect) #? Put the text into the screen

    def add_rect(self, pos:Tuple[float, float], size:Tuple[float, float], color: Tuple[int, int, int]=(0, 0, 0)):
        '''Add Rectangle To The Screen'''
        rect = pygame.Rect(pos[0], pos[1], size[0], size[1]) #? Create rectangle
        pygame.draw.rect(self.screen, color, rect) #? Put the rectangle with color

    def check_event(self, func:Callable[[pygame.event.Event], None]):
        '''Check each event with a function'''
        for event in pygame.event.get():
            func(event)
    

class SupermarketUI(UI):
    
    def __init__(self, width:int, height:int, title:str="Supermarket Simulation"):
        '''Use update_screen() to update the screen and don't forget to use `while SupermarketUI.running:` to keep the program running'''
        super().__init__(width, height, title)
        self.supermarket_handler = SupermarketHandler(self)
    
    
class SupermarketHandler:
    def __init__(self, supermarket_ui:SupermarketUI):
        '''Supermarket class'''
        self.supermarket_ui = supermarket_ui
        
    def create_supermarket(self, name:str, pos:Tuple[int, int], size:Tuple[int, int], color:Tuple[int, int, int]=(0, 0, 0)):
        '''Create a supermarket inside a screen'''
        self.supermarket_ui.add_rect(pos=pos, size=size, color=color)
        self.supermarket_ui.add_text(text=name, pos=(pos[0], pos[1]-30), font_size=26)


if __name__ == "__main__":
    '''Run tests here!'''
    ui = SupermarketUI(800, 800, title="SuperMarket Game!")
    def event_handler(event: pygame.event.Event):
        '''Handle event'''
        global ui
        if event.type == pygame.QUIT:
            ui.running = False

    while ui.running:
        ui.check_event(event_handler)
        ui.fill_screen((200, 200, 200))
        ui.add_text("Supermarket 1", (10, 10), font_size=26)
        ui.supermarket_handler.create_supermarket("RM Padang", (50, 150), (200, 200), (255, 25, 55))
        ui.supermarket_handler.create_supermarket("Samsung Store", (350, 150), (200, 200), (220, 220, 220))
        ui.update_screen()
        
    pygame.quit()
