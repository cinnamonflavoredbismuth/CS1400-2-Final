import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Spanish or Vanish')
pygame.display.set_icon(pygame.image.load('logo_uwu.png'))


# Image background
background_image = pygame.image.load('BG.webp')  # Load the image
background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen

#screen = pygame.display.set_mode((1200, 800))
def btn(dict):
        mouse = pygame.mouse.get_pos() # Stores mouse coordinates
        if dict['StartPos']['x'] <= mouse[0] <= dict['StartPos']['x'] + dict['width'] and dict['StartPos']['y'] <= mouse[1] <= dict['StartPos']['y']+dict['height']: 
            pygame.draw.rect(screen,dict['hover_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is hovering
        else: 
            pygame.draw.rect(screen,dict['main_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is not touching
        screen.blit(pygame.font.SysFont(dict['font'],dict['fontsize']).render(dict['text'] , True , dict["text_color"]),(dict['StartPos']['x']+dict["text_offset"],dict['StartPos']['y'])) # Putting text on the button

ex_dict = {
"width" : 500, # width of the button
"height" : 50, # height of the button
"StartPos": {"x" :  325,"y" : 630}, # Top left is 0,0
"text": "Quit", 
"font": "Arial",
"fontsize": 35,
"hover_color": (80,80,80),
"main_color": (40,40,40),
"text_offset": 225,
"text_color": (255,255,255)
}

def user_input():
    for event in pygame.event.get():
        # checking if keydown event happened or not
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                ex_dict = {
                "width" : 500, # width of the button
                "height" : 50, # height of the button
                "StartPos": {"x" :  325,"y" : 630}, # Top left is 0,0
                "text": "A key has been pressed", 
                "font": "Arial",
                "fontsize": 35,
                "hover_color": (80,80,80),
                "main_color": (40,40,40),
                "text_offset": 225,
                "text_color": ( 0, 0, 0)}
                # if keydown event happened
                # than printing a string to output
                print("A key has been pressed")
                text = str(ex_dict['text'])
                font = pygame.font.Font(ex_dict['font'], ex_dict['fontsize'])
                text = font.render(text, True, ex_dict["text_color"])
                screen.blit(text, (325, 630))
                #screen.blit(pygame.font.SysFont(ex_dict['font'],ex_dict['fontsize']).render(ex_dict['text'] , True , ex_dict["text_color"]),(ex_dict['StartPos']['x']+ex_dict["text_offset"],ex_dict['StartPos']['y']))
'''
while True:
    running = True
    while running:
        white = [255, 255, 255]
        screen.fill(white)  # Clear the screen with a white background
        pygame.display.flip()
        
            
        user_input()
'''

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('GeeksForGeeks', True, green, blue)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)
 
# infinite loop
while True:
 
    # completely fill the surface object
    # with white color
    screen(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()
