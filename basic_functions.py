import pygame
screen = pygame.display.set_mode((1200, 800))
def btn(dict):
        mouse = pygame.mouse.get_pos() # Stores mouse coordinates
        if dict['StartPos']['x'] <= mouse[0] <= dict['StartPos']['x'] + dict['width'] and dict['StartPos']['y'] <= mouse[1] <= dict['StartPos']['y']+dict['height']: 
            pygame.draw.rect(screen,dict['hover_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is hovering
        else: 
            pygame.draw.rect(screen,dict['main_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is not touching
        screen.blit(pygame.font.SysFont(dict['font'],dict['fontsize']).render(dict['text'] , True , dict["text_color"]),(dict['StartPos']['x']+dict["text_offset"],dict['StartPos']['y'])) # Putting text on the button