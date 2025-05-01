import pygame
screen = pygame.display.set_mode((1200, 800))
def btn(dict):
        mouse = pygame.mouse.get_pos() # Stores mouse coordinates
        if dict['StartPos']['x'] <= mouse[0] <= dict['StartPos']['x'] + dict['width'] and dict['StartPos']['y'] <= mouse[1] <= dict['StartPos']['y']+dict['height']: 
            pygame.draw.rect(screen,dict['hover_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is hovering
        else: 
            pygame.draw.rect(screen,dict['main_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is not touching
        screen.blit(pygame.font.SysFont(dict['font'],dict['fontsize']).render(dict['text'] , True , dict["text_color"]),(dict['StartPos']['x']+dict["text_offset"],dict['StartPos']['y'])) # Putting text on the button

def display(message, sec): # Displays a message on the screen by itself for a certain amount of seconds
    pygame.init()
    background_image = pygame.image.load('BG.webp')  # Load the image
    background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen
    font = pygame.font.Font(None, 36)

    surface = font.render(message, True, (0, 0, 0))
    screen.fill((255, 255, 255))  # Clear the screen for the message
    screen.blit(background_image, (0,0))
    screen.blit(surface, (50, 50))
    pygame.display.flip()  # Update the display
    pygame.time.delay(sec * 1000)  # Wait for 3 seconds before quitting