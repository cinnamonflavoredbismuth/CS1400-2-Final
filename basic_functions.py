import pygame

def pystart():
        pygame.init()
        # Set up the display
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Spanish or Vanish')
        pygame.display.set_icon(pygame.image.load('logo_uwu.png'))
        return(screen)

def clear(screen=pystart()):
        screen.fill((255, 255, 255))
        background_image = pygame.image.load('BG.webp')  # Load the image
        background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen
        screen.blit(background_image, (0,0))
screen=pystart()

#screen = pygame.display.set_mode((1200, 800))
def btn(dict):
        mouse = pygame.mouse.get_pos() # Stores mouse coordinates
        if dict['StartPos']['x'] <= mouse[0] <= dict['StartPos']['x'] + dict['width'] and dict['StartPos']['y'] <= mouse[1] <= dict['StartPos']['y']+dict['height']: 
            pygame.draw.rect(screen,dict['hover_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is hovering
        else: 
            pygame.draw.rect(screen,dict['main_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is not touching
        screen.blit(pygame.font.SysFont(dict['font'],dict['fontsize']).render(dict['text'] , True , dict["text_color"]),(dict['StartPos']['x']+dict["text_offset"],dict['StartPos']['y']+dict['verticle_text_offset'])) # Putting text on the button


def display(message, sec, x=50, y=50): # Displays a message on the screen by itself for a certain amount of seconds
    pystart()
    font = pygame.font.Font(None, 36)

    surface = font.render(message, True, (0, 0, 0))
    screen.fill((255, 255, 255))  # Clear the screen for the message
    clear()
    screen.blit(surface, (x, y))
    pygame.display.flip()  # Update the display
    if sec != 0:
        pygame.time.delay(sec * 1000)  # Waits a certain amount of seconds before continuing


def text(msg):
    black = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    return font.render(msg, True, black)


def letter_input(txt=[],x=0,y=0,event=None):
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                        screen.blit(text(f'a'), (x,y))
                        return f'a'
                elif event.key == pygame.K_b:
                        screen.blit(text(f'b'), (x,y))
                        return f'b'
                elif event.key == pygame.K_c:
                        screen.blit(text(f'c'), (x,y))
                        return f'c'
                elif event.key == pygame.K_d:     
                        screen.blit(text(f'd'), (x,y))
                        return f'd'
                elif event.key == pygame.K_e:
                        screen.blit(text(f'e'), (x,y))
                        return f'e'
                elif event.key == pygame.K_f:
                        screen.blit(text(f'f'), (x,y))
                        return f'f'
                elif event.key == pygame.K_g:
                        screen.blit(text(f'g'), (x,y))
                        return f'g'
                elif event.key == pygame.K_h:
                        screen.blit(text(f'h'), (x,y))
                        return f'h'
                elif event.key == pygame.K_i:
                        screen.blit(text(f'i'), (x,y))
                        return f'i'
                elif event.key == pygame.K_j:
                        screen.blit(text(f'j'), (x,y))
                        return f'j'
                elif event.key == pygame.K_k:
                        screen.blit(text(f'k'), (x,y))
                        return f'k'
                elif event.key == pygame.K_l:
                        screen.blit(text(f'l'), (x,y))
                        return f'l'
                elif event.key == pygame.K_m:
                        screen.blit(text(f'm'), (x,y))
                        return f'm'
                elif event.key == pygame.K_n:
                        screen.blit(text(f'n'), (x,y))
                        return f'n'
                elif event.key == pygame.K_o:
                        screen.blit(text(f'o'), (x,y))
                        return f'o'
                elif event.key == pygame.K_p:
                        screen.blit(text(f'p'), (x,y))
                        return f'p'
                elif event.key == pygame.K_q:
                        screen.blit(text(f'q'), (x,y))
                        return f'q'
                elif event.key == pygame.K_r:
                        screen.blit(text(f'r'), (x,y))
                        return f'r'
                elif event.key == pygame.K_s:
                        screen.blit(text(f's'), (x,y))
                        return f's'
                elif event.key == pygame.K_t:
                        screen.blit(text(f't'), (x,y))
                        return f't'
                elif event.key == pygame.K_u:
                        screen.blit(text(f'u'), (x,y))
                        return f'u'
                elif event.key == pygame.K_v:
                        screen.blit(text(f'v'), (x,y))
                        return f'v'
                elif event.key == pygame.K_w:
                        screen.blit(text(f'w'), (x,y))
                        return f'w'
                elif event.key == pygame.K_x:
                        screen.blit(text(f'x'), (x,y))
                        return f'x'
                elif event.key == pygame.K_y:
                        screen.blit(text(f'y'), (x,y))
                        return f'y'
                elif event.key == pygame.K_z:
                        screen.blit(text(f'z'), (x,y))
                        return f'z'
                elif event.key == pygame.K_0:
                        screen.blit(text(f'0'), (x,y))
                        return f'0'
                elif event.key == pygame.K_1:
                        screen.blit(text(f'1'), (x,y))
                        return f'1'
                elif event.key == pygame.K_2:
                        screen.blit(text(f'2'), (x,y))
                        return f'2'
                elif event.key == pygame.K_3:
                        screen.blit(text(f'3'), (x,y))
                        return f'3'
                elif event.key == pygame.K_4:
                        screen.blit(text(f'4'), (x,y))
                        return f'4'
                elif event.key == pygame.K_5:
                        screen.blit(text(f'5'), (x,y))
                        return f'5'
                elif event.key == pygame.K_6:
                        screen.blit(text(f'6'), (x,y))
                        return f'6'
                elif event.key == pygame.K_7:
                        screen.blit(text(f'7'), (x,y))
                        return f'7'
                elif event.key == pygame.K_8:
                        screen.blit(text(f'8'), (x,y))
                        return f'8'
                elif event.key == pygame.K_9:
                        screen.blit(text(f'9'), (x,y))
                        return f'9'
                elif event.key == pygame.K_RETURN:
                        txt= ''.join(txt)
                        screen.blit(text(f'{txt}'), (x,y))
                        return 'enter'
                else:
                        screen.blit(text(f'Invalid character'),(x,y+20))
                        return None
        else: 
                return None


def txt_input(x,y):
        x=x-40
        user_txt=[]
        run=True
        while run==True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                                break
                        else:  
                                x=x+5
                                letter=letter_input(txt=user_txt,x=x,y=y,event=event)
                                if letter != None:
                                        if letter=='enter':
                                                user_txt=''.join(user_txt)
                                                return user_txt
                                        else: 
                                                user_txt.append(letter)

                pygame.display.update()


click_sound = pygame.mixer.Sound("click.mp3")
startup_sound = pygame.mixer.Sound("startup.mp3")

def click():
    ####################################
    pygame.mixer.Sound.play(click_sound)

def start_up():
        pygame.mixer.Sound.play(startup_sound)

def bgm():
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

                       # pygame.display.update()
                       # pygame.time.delay(10)# delay .01 seconds#screen.fill((255, 255, 255))  # Clear the screen with a white background
#txt_input(0,0)

