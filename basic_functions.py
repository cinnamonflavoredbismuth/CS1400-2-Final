# Basic Functions
import pygame

# THINGS TO DO WITH SCREEN

def pystart(): # 
        pygame.init()
        # Set up the display
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Spanish or Vanish')
        pygame.display.set_icon(pygame.image.load('images/logo_uwu.png'))
        return(screen)


screen=pystart()


def clear(screen=pystart()): # 
        screen.fill((255, 255, 255))
        background_image = pygame.image.load('images/BG.webp')  # Load the image
        background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen
        screen.blit(background_image, (0,0))

def birds(): # 
        bird1 = pygame.image.load("images/logo_uwu.png")
        bird2 = pygame.transform.flip(bird1, True, False)  # Flip the image horizontally
        bird1 = pygame.transform.scale(bird1, (200, 200))  # Scale the image to fit the screen 
        bird2 = pygame.transform.scale(bird2, (200, 200))  # Scale the image to fit the screen
        screen.blit(bird1, (30, 0)) # Draw the first bird image at (0, 0)
        screen.blit(bird2, (900,0))



# THINGS TO DO WITH BUTTONS

class button: #       0     1       2       3         4     5     6        7        8         9         10                11              12        13
        def __init__(self, width, height, StartPos, text, font, fontsize, hover_color, main_color, text_offset, verticle_text_offset, text_color, locked): # This is the button class
                self.width = width
                self.height = height
                self.StartPos = StartPos
                self.text = text
                self.font = font
                self.fontsize = fontsize
                self.hover_color = hover_color
                self.main_color = main_color
                self.text_offset = text_offset
                self.verticle_text_offset = verticle_text_offset
                self.text_color = text_color
                self.locked = locked
        def __str__(self): # String of information for the button object
                return f"""
                Width: {self.width}
                Height: {self.height}
                StartPos: {self.StartPos}
                Text: {self.text}
                Font: {self.font}
                Fontsize: {self.fontsize}
                Hover_color: {self.hover_color}
                Main_color: {self.main_color}
                Text_offset: {self.text_offset}
                Verticle_text_offset: {self.verticle_text_offset}
                Text_color: {self.text_color}
                Locked: {self.locked}"""

        def btn(self): # Creates the button with pygame and displays it on the pygame window
                mouse = pygame.mouse.get_pos() # Stores mouse coordinates
                if self.StartPos['x'] <= mouse[0] <= self.StartPos['x'] + self.width and self.StartPos['y'] <= mouse[1] <= self.StartPos['y']+self.height: 
                        pygame.draw.rect(screen,self.hover_color,[self.StartPos['x'],self.StartPos['y'],self.width,self.height]) # If mouse is hovering
                        screen.blit(pygame.font.SysFont(self.font,self.fontsize).render(self.text , True , self.text_color),(self.StartPos['x']+self.text_offset,self.StartPos['y']+self.verticle_text_offset)) # Putting text on the button
                else: 
                        pygame.draw.rect(screen,self.main_color,[self.StartPos['x'],self.StartPos['y'],self.width,self.height]) # If mouse is not touching
                        screen.blit(pygame.font.SysFont(self.font,self.fontsize).render(self.text , True , self.text_color),(self.StartPos['x']+self.text_offset,self.StartPos['y']+self.verticle_text_offset)) # Putting text on the button
        
def if_clicked(btn, event): # 
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos  # This is safe now
        if btn.StartPos['x'] <= x <= btn.StartPos['x'] + btn.width and btn.StartPos['y'] <= y <= btn.StartPos['y'] + btn.height:
            click()
            return True
    return False
        
def display_buttons(buttons): # Makes multiple buttons displayed
        for x in list(buttons.values()):
                x.btn()

# THINGS TO DO WITH TEXT DISPLAY 

def display(message, sec, x=50, y=50): # Displays a message on the screen by itself for a certain amount of seconds
    font = pygame.font.Font(None, 36)
    surface = font.render(message, True, (0, 0, 0))
    screen.blit(surface, (x, y))
    pygame.display.flip()  # Update the display
    if sec != 0:
        pygame.time.delay(sec * 1000)  # Waits a certain amount of seconds before continuing


# def text(msg): # Formats inputted text for txt_input
#     black = (0, 0, 0)
#     font = pygame.font.Font(None, 36)
#     return font.render(msg, True, black)


# def letter_input(txt=[],x=0,y=0,event=None): # Finds which key/letter was pressed by the user
#         if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_a:
#                         screen.blit(text(f'a'), (x,y))
#                         return f'a'
#                 elif event.key == pygame.K_b:
#                         screen.blit(text(f'b'), (x,y))
#                         return f'b'
#                 elif event.key == pygame.K_c:
#                         screen.blit(text(f'c'), (x,y))
#                         return f'c'
#                 elif event.key == pygame.K_d:     
#                         screen.blit(text(f'd'), (x,y))
#                         return f'd'
#                 elif event.key == pygame.K_e:
#                         screen.blit(text(f'e'), (x,y))
#                         return f'e'
#                 elif event.key == pygame.K_f:
#                         screen.blit(text(f'f'), (x,y))
#                         return f'f'
#                 elif event.key == pygame.K_g:
#                         screen.blit(text(f'g'), (x,y))
#                         return f'g'
#                 elif event.key == pygame.K_h:
#                         screen.blit(text(f'h'), (x,y))
#                         return f'h'
#                 elif event.key == pygame.K_i:
#                         screen.blit(text(f'i'), (x,y))
#                         return f'i'
#                 elif event.key == pygame.K_j:
#                         screen.blit(text(f'j'), (x,y))
#                         return f'j'
#                 elif event.key == pygame.K_k:
#                         screen.blit(text(f'k'), (x,y))
#                         return f'k'
#                 elif event.key == pygame.K_l:
#                         screen.blit(text(f'l'), (x,y))
#                         return f'l'
#                 elif event.key == pygame.K_m:
#                         screen.blit((f'm'), (x,y))
#                         return f'm'
#                 elif event.key == pygame.K_n:
#                         screen.blit(text(f'n'), (x,y))
#                         return f'n'
#                 elif event.key == pygame.K_o:
#                         screen.blit(text(f'o'), (x,y))
#                         return f'o'
#                 elif event.key == pygame.K_p:
#                         screen.blit(text(f'p'), (x,y))
#                         return f'p'
#                 elif event.key == pygame.K_q:
#                         screen.blit(text(f'q'), (x,y))
#                         return f'q'
#                 elif event.key == pygame.K_r:
#                         screen.blit(text(f'r'), (x,y))
#                         return f'r'
#                 elif event.key == pygame.K_s:
#                         screen.blit(text(f's'), (x,y))
#                         return f's'
#                 elif event.key == pygame.K_t:
#                         screen.blit(text(f't'), (x,y))
#                         return f't'
#                 elif event.key == pygame.K_u:
#                         screen.blit(text(f'u'), (x,y))
#                         return f'u'
#                 elif event.key == pygame.K_v:
#                         screen.blit(text(f'v'), (x,y))
#                         return f'v'
#                 elif event.key == pygame.K_w:
#                         screen.blit(text(f'w'), (x,y))
#                         return f'w'
#                 elif event.key == pygame.K_x:
#                         screen.blit(text(f'x'), (x,y))
#                         return f'x'
#                 elif event.key == pygame.K_y:
#                         screen.blit(text(f'y'), (x,y))
#                         return f'y'
#                 elif event.key == pygame.K_z:
#                         screen.blit(text(f'z'), (x,y))
#                         return f'z'
#                 elif event.key == pygame.K_0:
#                         screen.blit(text(f'0'), (x,y))
#                         return f'0'
#                 elif event.key == pygame.K_1:
#                         screen.blit(text(f'1'), (x,y))
#                         return f'1'
#                 elif event.key == pygame.K_2:
#                         screen.blit(text(f'2'), (x,y))
#                         return f'2'
#                 elif event.key == pygame.K_3:
#                         screen.blit(text(f'3'), (x,y))
#                         return f'3'
#                 elif event.key == pygame.K_4:
#                         screen.blit(text(f'4'), (x,y))
#                         return f'4'
#                 elif event.key == pygame.K_5:
#                         screen.blit(text(f'5'), (x,y))
#                         return f'5'
#                 elif event.key == pygame.K_6:
#                         screen.blit(text(f'6'), (x,y))
#                         return f'6'
#                 elif event.key == pygame.K_7:
#                         screen.blit(text(f'7'), (x,y))
#                         return f'7'
#                 elif event.key == pygame.K_8:
#                         screen.blit(text(f'8'), (x,y))
#                         return f'8'
#                 elif event.key == pygame.K_9:
#                         screen.blit(text(f'9'), (x,y))
#                         return f'9'
#                 elif event.key == pygame.K_RETURN:
#                         txt= ''.join(txt)
#                         screen.blit(text(f'{txt}'), (x,y))
#                         return 'enter'
#                 else:
#                         display(f'Invalid character',1)
#                         return 'invalid'
#         else: 
#                 return None

# def inputting(x,y): # Lets the user input text on pygame, displays it in a certain spot, and then returns it
#         x2=x-40
#         user_txt=[]
#         run=True
#         while run==True:
#                 for event in pygame.event.get():
#                         if event.type == pygame.QUIT:
#                                 pygame.quit()
#                                 quit()
#                                 break
#                         else:  
#                                 x2=x2+5
#                                 letter=letter_input(txt=user_txt,x=x2,y=y,event=event)
#                                 if letter != None:
#                                         if letter=='enter':
#                                                 user_txt=''.join(user_txt)
#                                                 return user_txt
#                                         elif letter=='invalid':
#                                                 clear()
#                                                 x2=x2-5
#                                                 screen.blit(text(''.join(user_txt)), (x,y))
#                                         else: 
#                                                 user_txt.append(letter)

#                 pygame.display.update()

def txt_input(prompt, x=50,y=50):

    input_box = pygame.Rect(x, y, 250, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    font = pygame.font.Font(None, 36)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        clear()
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface = font.render(prompt + text, True, (0, 0, 0))
        width = max(250, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.display.flip()
    return text

# THINGS TO DO WITH MUSIC

def click(): # For playing a sound when a button is clicked
    click_sound = pygame.mixer.Sound("sounds/click.mp3")
    ####################################
    pygame.mixer.Sound.play(click_sound)

def start_up(): # For playing a sound when the program starts
        startup_sound = pygame.mixer.Sound("sounds/startup.mp3")
        pygame.mixer.Sound.play(startup_sound)

def bgm(): # For playing a sound in the background
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

                       # pygame.display.update()
                       # pygame.time.delay(10)# delay .01 seconds#screen.fill((255, 255, 255))  # Clear the screen with a white background

def wrong_sound(): # For playing a sound when a wrong button is clicked
        pygame.mixer.music.load("sounds/answer-wrong.mp3")
        pygame.mixer.music.play(0)  # Play the sound once

