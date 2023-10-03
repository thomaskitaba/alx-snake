import pygame
import math
import time
import random
import csv


pygame.init()
clock = pygame.time.Clock()

# GAME SETTING

background_image_mode = "DARK" # default 
background_image_mode = "DAY"	# option 2

# GAME DATA

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)
YELLOW = (255, 255,0)
BACKGROUND = BLACK
TEXT_GREY = ( 100, 100, 100)

SCORE = 0
SCORE_2 = 0


#screen_width = 640 #1440
#screen_height = 640
#screen_size_l = [640,640]
#screen_width = 1440
#screen_height = 640
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width,height = screen.get_size()
width -= 60
height -= 60

screen_width = width +60
screen_height = height + 60

#screen = pygame.display	.set_mode((screen_width, screen_height))
pygame.display.set_caption("Thomas Kitaba")


# to generate food_2 
far_from_meteor = [0]
far_from_food = [0]
snake_speed_list= [0]

play_sound= [0]
move_sound = pygame.mixer.Sound("snake_audio_files/move_sound_2.mp3")
swallow_sound = pygame.mixer.Sound("snake_audio_files/swallow_1.mp3")

# DECLARE AND INITIALIZE DORECTIONS

head_right= False
head_left = False				
head_up = False
head_down = False

game_over = False
game_over_1 = False

# COLLISION VARIABLES
distance_with_left_top_meteor = [1000] 
distance_with_left_bottom_meteor = [1000] 
distance_with_right_top_meteor = [1000] 
distance_with_right_bottom_meteor = [1000] 
distance_with_center_meteor = [1000] 

food_distance_with_left_top_meteor = [1000] 
food_distance_with_left_bottom_meteor = [1000] 
food_distance_with_right_top_meteor = [1000] 
food_distance_with_right_bottom_meteor = [1000] 
food_distance_with_center_meteor = [1000] 

collision_counter = [0]
overlap_with_meteor = [1]
meteor_explosion = [0, 0]
collide_with_next_level = [0]
# LEVEL AND SCORE 

food_amount_to_change_level = 10

f_t_c_l= food_amount_to_change_level
score_to_change_level = []

LEVEL = 1
LEVEL_2 = 1
for i in range(food_amount_to_change_level, food_amount_to_change_level * 1000, food_amount_to_change_level):
  score_to_change_level.append(i)
    
up_click_time = 0
right_click_time = 0
down_click_time = 0
left_click_time = 0


food_l = [[300, 300],[200,200],[549,246]]
poisen_l = [[385,532], [371,111], [432,184]]


os = 100  #offset_short = 100
om = 200 #offset_medium= 200
ol = 400 #offset_long = 300
sw = screen_width #offset_long = 300
sh = screen_height #offset_long = 300

#initial snake speed
snake_speed=  20
snake_size = [3]
block = 40

start_x_l = [snake_size[0] * block]
start_y_l = [screen_height * 0.5 - om]

start_x = start_x_l[0]
start_y = start_y_l[0]


max_horizontal_snake_size = int(screen_width/ block )
max_vertical_snake_size = int(screen_height/ block )

max_snake_size = max_horizontal_snake_size * max_vertical_snake_size 

#move_sound = pygame.mixer.Sound("snake_audio_files/move_sound_1.mp3")

#swallow_sound = pygame.mixer.Sound("snake_audio_files/swallow_1.mp3")



# DEFINE FONTS FOR GAME
snake_big_font = pygame.font.SysFont("Comic Sans MS", 40)

snake_body_center = [0,0]

# initial snake body size
#snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
snake_body = []
#snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y],[start_x - block*3, start_y],[start_x - block*4, start_y],[start_x - block*5, start_y],[start_x - block*6, start_y],[start_x - block*7, start_y],[start_x - block*8, start_y],[start_x - block*9, start_y],[start_x - block*10, start_y],[start_x - block*11, start_y],[start_x - block*12, start_y],[start_x - block*13, start_y],[start_x - block*14, start_y],[start_x - block*15, start_y],[start_x - block*16, start_y],[start_x - block*17, start_y],[start_x - block*17, start_y],[start_x - block*18, start_y],[start_x - block*19, start_y],[start_x - block*20, start_y],[start_x - block*21, start_y],[start_x - block*22, start_y],[start_x - block*23, start_y],[start_x - block*25, start_y],[start_x - block*25, start_y],[start_x - block*26, start_y],[start_x - block*27, start_y],[start_x - block*28, start_y],[start_x - block*29, start_y],[start_x - block*30, start_y],[start_x - block*31, start_y],[start_x - block*32, start_y]]

for i in range (0,snake_size[0]):
  snake_body.append([start_x - block*i, start_y])
  
#snake_body = [[start_x, start_y]]
snake_body_temp = []
snake_width = block
snake_height = block




      ##################
      ## GENERATE WORLD ##
      ## WALL 1 ___ WALL 2 ##
      ##################
      
# DIVIDE SCREEN INTO 4 QUADRANTS 

screen_half_x = screen_width/2
screen_half_y = screen_height/2

generate_q1 = True 
generate_q2 = True 
generate_q3 = True 
generate_q_4 = True 

# select line orientation
select_random_direction = -1

# line 1 quadrant 1
random_start_q1_line_1 = [0,0]
random_end_q1_line_1 = [0,0]

#line 2 quadrant 1
random_start_q1_line_2 = [0,0]
random_end_q1_line_2 = [0,0]



  #  GENERATE WORLD FUNCTION		
def generate_wall_1(start_x,start_y,end_x, end_y):

  pygame.draw.line(screen, BLACK, (start_x,start_y), (end_x, end_y), 40)	

def generate_wall_2(start_x,start_y,end_x, end_y):

  pygame.draw.line(screen, BLACK, (start_x,start_y), (end_x, end_y), 40)	



snakeimage= pygame.image.load("game_objects/snakepart.png")
snake_image= pygame.transform.scale(snakeimage, (block,block))

## SNAKE HEAD
#snake_texture_head = pygame.image.load("game_objects/snake_head_0.png")

snake_texture_head = pygame.image.load("game_objects/snake_head_1.png")

# SNAKE BODY
#snake_texture= pygame.image.load("game_objects/snake_body_.jpg")

#
snake_texture= pygame.image.load("game_objects/earth_image_0.png")

snake_texture= pygame.image.load("game_objects/snake_body_1.png")

# SNAKE TAIL
#snake_texture_tail= pygame.image.load("game_objects/snake_tail_0.jpg")

snake_texture_tail= pygame.image.load("game_objects/snake_tail_0.jpg")

snake_texture_l= [pygame.transform.scale(snake_texture_head, (block,block)), pygame.transform.scale(snake_texture, (block,block)),  pygame.transform.scale(snake_texture_tail, (block,block))]

snake_body_center = [0,0]


#========= SNAKE BODY AND FOOD ======
# grow snake
def update_body():
  if game_over == False:
    for parts in range(len(snake_body) -1, 0, -1):
      snake_body[parts] = snake_body[parts - 1]
      
      
def draw_snake(body_part ):
    
    if game_over == False:
        if play_sound[0] == 1:
          move_sound.play()
    
    for b in range (len(snake_body)):
      if b == 0:
        pass
        #pygame.draw.rect(screen,BACKGROUND, pygame.Rect(body_part[b][0],body_part[b][1], snake_width, snake_height))
        
      else:
        pass
      
        #pygame.draw.rect(screen,(BACKGROUND), pygame.Rect(body_part[b][0],body_part[b][1], snake_width, snake_height))
    
    for b in range (len(snake_body)):
      
      #DRAW HEAD
      if b == 0:
        
        screen.blit(snake_texture_l[0], (snake_body[b][0],snake_body[b][1]))
        
      else: # DRAW BODY
        screen.blit(snake_texture_l[1], (snake_body[b][0],snake_body[b][1]))
      
      #DRAW TAIL
      if b == len(snake_body)- 1:
        screen.blit(snake_texture_l[1], (snake_body[b][0],snake_body[b][1]))
        

  #screen.blit(snake_image, (snake_body[0][0],snake_body[0][1]))
  
#====== FOOD 111111 =======

food_rectangle = 0
food_rectangle_coord=[]

def draw_food(x,y):
  
  food_rectangle = pygame.Rect(x,y,block,block)
  food_rectangle_coord = [food_rectangle.centerx, food_rectangle.centery]
  
  screen.blit( food_image_l[0] , (x,y))
  #pygame.draw.rect(screen, BLUE, food_rectangle )


#==== FOOD 2222222 =====
food_2_l = [[0,0]]
food_2_l[0][0] = int(random.randint(0,screen_width))
food_2_l[0][1] = int(random.randint(0,screen_height))

food_2_rectangle = 0
food_2_rectangle_coord=[]
s = 0 # distance between food_2 and meteor when food is spawned right before the score changes

#food_image_l= pygame.image.load("game_objects/blackhole_1.png")

#food_image_l =[ pygame.transform.scale(food_image_1, (80,80))]

b_h_w = 80
b_h_h = 80

food_image=                                                        [pygame.image.load("game_objects/blackhole_1.png"),                                                  pygame.image.load("game_objects/blackhole_2.png"), pygame.image.load("game_objects/blackhole_3.png"), pygame.image.load("game_objects/blackhole_4.png"),pygame.image.load("game_objects/blackhole_5.png"),pygame.image.load("game_objects/blackhole_5.png"),pygame.image.load("game_objects/blackhole_6.png"),pygame.image.load("game_objects/blackhole_7.png"),pygame.image.load("game_objects/blackhole_8.png"), pygame.image.load("game_objects/blackhole_9.png"), pygame.image.load("game_objects/blackhole_10.png")
]

food_image_l=[ pygame.transform.scale(food_image[0], (b_h_w, b_h_h)), pygame.transform.scale(food_image[1], (b_h_w, b_h_h)), pygame.transform.scale(food_image[2], (b_h_w, b_h_h)), pygame.transform.scale(food_image[3], (b_h_w, b_h_h)), pygame.transform.scale(food_image[4], (b_h_w, b_h_h)), pygame.transform.scale(food_image[5], (b_h_w, b_h_h)), pygame.transform.scale(food_image[5], (b_h_w, b_h_h)), pygame.transform.scale(food_image[6], (b_h_w, b_h_h)), pygame.transform.scale(food_image[7], (b_h_w, b_h_h)), pygame.transform.scale(food_image[8], (b_h_w, b_h_h)), pygame.transform.scale(food_image[9], (b_h_w, b_h_h)), pygame.transform.scale(food_image[0], (b_h_w, b_h_h))]


def draw_food_2(x,y):
  
  food_2_rectangle = pygame.Rect(x,y,block,block)
  food_2_rectangle_coord = [food_2_rectangle.centerx, food_2_rectangle.centery]
  
#	for i in range 10:
    #food_image_l_rotating.append(pygame.transform.rotate(food_image_l[i], (meteor_rotation[1])))
  
  food_image_l_rotating = [pygame.transform.rotate(food_image_l[0], (meteor_rotation[1])),
  pygame.transform.rotate(food_image_l[1], (meteor_rotation[1])),  pygame.transform.rotate(food_image_l[2], (meteor_rotation[1])),pygame.transform.rotate(food_image_l[3], (meteor_rotation[1])), pygame.transform.rotate(food_image_l[4], (meteor_rotation[1])),
pygame.transform.rotate(food_image_l[5], (meteor_rotation[1])), pygame.transform.rotate(food_image_l[6], (meteor_rotation[1])),
pygame.transform.rotate(food_image_l[7], (meteor_rotation[1])), pygame.transform.rotate(food_image_l[8], (meteor_rotation[1])),
pygame.transform.rotate(food_image_l[9], (meteor_rotation[1])), pygame.transform.rotate(food_image_l[10], (meteor_rotation[1]))]
      
  a = int(food_image_l_rotating[0].get_width()) * 0.5 
  b = int(food_image_l_rotating[0].get_height()) * 0.5
  x = food_2_rectangle.centerx
  y = food_2_rectangle.centery
  #screen.blit( food_image_l_rotating[0] , (x - a,  y - b))
  
  pygame.draw.rect(screen, YELLOW, food_2_rectangle )
  if LEVEL % f_t_c_l == 1:
    screen.blit( food_image_l_rotating[0] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 2:
    screen.blit( food_image_l_rotating[1] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 3:
    screen.blit( food_image_l_rotating[2] , (x - a,  y - b))
  
  if  LEVEL % f_t_c_l == 4:
    screen.blit( food_image_l_rotating[3] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 5:
    screen.blit( food_image_l_rotating[4] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 6:
    screen.blit( food_image_l_rotating[5] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 7:
    screen.blit( food_image_l_rotating[6] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 8:
    screen.blit( food_image_l_rotating[7] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 9:
    screen.blit( food_image_l_rotating[8] , (x - a,  y - b))
  if LEVEL % f_t_c_l == 0:
    screen.blit( food_image_l_rotating[9] , (x - a,  y - b))
  
# @@@@@@end of SNAKE BODY FOOD@@@@ 

          ###############
          ###CONTROLLER###
          ###############

up_clicked = False
right_clicked = False
down_clicked = False
left_clicked = False


controller_size = [100]
controller_space = [10]
display_controller = True
controller_list = []
controller_list_clicked = []

controller_click_distance = int(math.sqrt((controller_size[0]/2 )**2 + (controller_size[0]/2 )**2))

up_rectangle = pygame.Rect(screen_width - 2*controller_space[0]  - 2* controller_size[0], screen_height - 3*controller_space[0]  - 3* controller_size[0], controller_size[0], controller_size[0])

right_rectangle = pygame.Rect(screen_width - controller_space[0]  - controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0], controller_size[0], controller_size[0])


down_rectangle = pygame.Rect(screen_width - 2*controller_space[0]  - 2* controller_size[0], screen_height - controller_space[0]  -  controller_size[0], controller_size[0], controller_size[0])
left_rectangle =pygame.Rect(screen_width - 3*controller_space[0]  - 3* controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0], controller_size[0], controller_size[0])


# orignal image
arrow_image = pygame.image.load("game_objects/arrow-up.png")
arrow_image_clicked = pygame.image.load("game_objects/up_clicked.png")
arrow_image_1= pygame.transform.scale(arrow_image, (controller_size[0], controller_size[0]))
#arrow down
arrow_image_1_clicked = pygame.transform.scale(arrow_image_clicked, (controller_size[0], controller_size[0]))

# controller up
arrow_rotated_up = pygame.transform.rotate(arrow_image_1, (0))
controller_list.append(arrow_rotated_up)

arrow_rotated_up_clicked = pygame.transform.rotate(arrow_image_1_clicked, (0))
controller_list_clicked.append(arrow_rotated_up_clicked)

# controller right
arrow_rotated_right = pygame.transform.rotate(arrow_image_1, (-90))
controller_list.append(arrow_rotated_right)

arrow_rotated_right_clicked = pygame.transform.rotate(arrow_image_1_clicked, (-90))
controller_list_clicked.append(arrow_rotated_right_clicked)

# controller down
arrow_rotated_down = pygame.transform.rotate(arrow_image_1, (180))
controller_list.append(arrow_rotated_down)

arrow_rotated_down_clicked= pygame.transform.rotate(arrow_image_1_clicked, (180))
controller_list_clicked.append(arrow_rotated_down_clicked)


# controller left
arrow_rotated_left = pygame.transform.rotate(arrow_image_1, (90))
controller_list.append(arrow_rotated_left)

arrow_rotated_left_clicked = pygame.transform.rotate(arrow_image_1_clicked, (90))
controller_list_clicked.append(arrow_rotated_left_clicked)

def draw_rect():
  
  # draw the base triangle  UP
  pygame.draw.rect(screen,BACKGROUND, up_rectangle)
  
  # draw the base triangle RIGHT
  pygame.draw.rect(screen,BACKGROUND, right_rectangle )
  
    # draw the base triangle DOWN
  pygame.draw.rect(screen,BACKGROUND, down_rectangle )
  
  # draw the base triangle LEFT
  pygame.draw.rect(screen,BACKGROUND, left_rectangle)
  
def draw_controller():
  
    # draw the base triangle
  #pygame.draw.rect(screen,(0,0,0,255), up_rectangle)
  
  # blit CONTROLLER UP
  if up_clicked:
    screen.blit(controller_list_clicked[0], (screen_width - 2*controller_space[0]  - 2* controller_size[0], screen_height - 3*controller_space[0]  - 3* controller_size[0]))
  else:
    screen.blit(controller_list[0], (screen_width - 2*controller_space[0]  - 2* controller_size[0], screen_height - 3*controller_space[0]  - 3* controller_size[0]))

  #+++++++++++++++++++++++++++++
  # draw the base triangle
#	pygame.draw.rect(screen,(0,0,0,255), right_rectangle )
  # blit CONTROLLER RIGHT
  
  if right_clicked:
    screen.blit(controller_list_clicked[1], (screen_width - controller_space[0]  - controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0]))
  else:
    screen.blit(controller_list[1], (screen_width - controller_space[0]  - controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0]))
  
  #+++++++++++++++++++++++++++++
  # draw the base triangle
  #pygame.draw.rect(screen,(0,0,0,255), down_rectangle )
  # blit CONTROLLER DOWN
  
  
  if down_clicked:
    screen.blit(controller_list_clicked[2], (screen_width - 2*controller_space[0]  - 2* controller_size[0], screen_height - controller_space[0]  -  controller_size[0]))
  else:
    screen.blit(controller_list[2], (screen_width - 2*controller_space[0]  - 2* controller_size[0], screen_height - controller_space[0]  -  controller_size[0]))
    #+++++++++++++++++++++++++++++
  # draw the base triangle
  #pygame.draw.rect(screen,(0,0,0,255), left_rectangle)
  # blit CONTROLLER LEFT
  
  if left_clicked:
    screen.blit(controller_list_clicked[3], (screen_width - 3*controller_space[0]  - 3* controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0]))
  else:
    screen.blit(controller_list[3], (screen_width - 3*controller_space[0]  - 3* controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0]))
    
        #################
        ####--LEVEL--######
        ####--SCORE--######
        #################
        
    # rendere hs, player name,  rank

lbl_score = snake_big_font.render("Score:", 1,TEXT_GREY)
lbl_level = snake_big_font.render("Level:", 1,TEXT_GREY)
    
def display_level_and_score(level, score):

  level = str(level)
  score = str(score)
  
  value_level = snake_big_font.render(level, 1,(255,0,0))
  value_score = snake_big_font.render(score, 1,(255,0,0))
  screen.blit(lbl_score, (screen_width * 0.5 - 250, 10))
  
  screen.blit(value_score, (screen_width * 0.5 - 50, 10))
  screen.blit(lbl_level, (screen_width * 0.5 + 50 ,  10))
  screen.blit(value_level, (screen_width * 0.5 + 250, 10))
  
  
  
#===================================
background_image_1= pygame.image.load("game_objects/space_111.jpeg")

background_image_2= pygame.image.load("game_objects/space_2.jpeg") 

background_image_3 = pygame.image.load("game_objects/space_3.jpeg")#TODO: to be changed

background_image_4 = pygame.image.load("game_objects/space_4.jpeg")

background_image_5 = pygame.image.load("game_objects/space_5.jpeg") #TODO: to be changed Image by <a href="https://pixabay.com/users/wikiimages-1897/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=11107">WikiImages</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=11107">Pixabay</a>

background_image_6 = pygame.image.load("game_objects/space_6.jpeg")

background_image_7 = pygame.image.load("game_objects/space_7.jpeg") # Image by <a href="https://pixabay.com/users/wikiimages-1897/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=67616">WikiImages</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=67616">Pixabay</a>

background_image_8 = pygame.image.load("game_objects/space_8.jpeg")

background_image_9 = pygame.image.load("game_objects/space_9.jpeg") #TODO: to be changed 

background_image_10= pygame.image.load("game_objects/space_10.jpeg") #TODO: to be changed


background_image_l = [pygame.transform.scale(background_image_1, (screen_width,screen_height)), pygame.transform.scale(background_image_2, (screen_width,screen_height)), pygame.transform.scale(background_image_3, (screen_width,screen_height)), pygame.transform.scale(background_image_4, (screen_width,screen_height)), pygame.transform.scale(background_image_5, (screen_width,screen_height)), pygame.transform.scale(background_image_6, (screen_width,screen_height)), pygame.transform.scale(background_image_7, (screen_width,screen_height)), pygame.transform.scale(background_image_8, (screen_width,screen_height)), pygame.transform.scale(background_image_9, (screen_width,screen_height)), pygame.transform.scale(background_image_10, (screen_width,screen_height))]

def background_image():
  
  #if background_image_mode == "DAY":
    #screen.blit(background_image_l[0],(0,0) )
  #if background_image_mode == "DARK":
    #screen.blit(background_image_l[1],(0,0) )
  f_t_c_l = food_amount_to_change_level
  if LEVEL % f_t_c_l == 1:
    screen.blit(background_image_l[0],(0,0) )
  if LEVEL % f_t_c_l == 2:
    screen.blit(background_image_l[1],(0,0) )
  if LEVEL % f_t_c_l == 3:
    screen.blit(background_image_l[2],(0,0) )
  if  LEVEL % f_t_c_l == 4:
    screen.blit(background_image_l[3],(0,0) )
  if LEVEL % f_t_c_l == 5:
    screen.blit(background_image_l[4],(0,0) )
  if LEVEL % f_t_c_l == 6:
    screen.blit(background_image_l[5],(0,0) )
  if LEVEL % f_t_c_l == 7:
    screen.blit(background_image_l[6],(0,0) )
  if LEVEL % f_t_c_l == 8:
    screen.blit(background_image_l[7],(0,0) )
  if LEVEL % f_t_c_l == 9:
    screen.blit(background_image_l[8],(0,0) )
  if LEVEL % f_t_c_l == 0:
    screen.blit(background_image_l[9],(0,0) )
#	if LEVEL > 10:
  #	screen.blit(background_image_l[1],(0,0) )
  
#def background_image():
  
  #if background_image_mode == "DAY":
  #	screen.blit(background_image_l[0],(0,0) )
#	if background_image_mode == "DARK":
  #	screen.blit(background_image_l[1],(0,0) )
        
#===================================
      ##################
      ##      LEVEL WORLD       ##
      ## 		10 LEVELS            ##
      ##################
    
os = 100  #offset_short = 100
om = 200 #offset_medium= 200
ol = 400 #offset_long = 300
sw = screen_width #offset_long = 300
sh = screen_height #offset_long = 300
 # meteor rectangle offset 
meteor_size_small = 100
meteor_size_mid = 100
meteor_size_big= 100

mro = meteor_size_mid * 0.5 


meteor_rotation = [0,0,0]
meteors_center_coord = []

# list for pll meteor coordinates
meteor_coordinate = [[om,om], [sw - om,  om], [sw - om, sh - om], [om, sh - om], [sw * 0.5, sh * 0.5]]

left_top_rect = pygame.Rect(meteor_coordinate[0][0] - mro, meteor_coordinate[0][1] - mro, meteor_size_mid, meteor_size_mid)

right_top_rect = pygame.Rect(meteor_coordinate[1][0] - mro, meteor_coordinate[1][1] - mro, meteor_size_mid, meteor_size_mid)


right_bottom_rect = pygame.Rect(meteor_coordinate[2][0] - mro, meteor_coordinate[2][1] - mro, meteor_size_mid, meteor_size_mid)

left_bottom_rect = pygame.Rect(meteor_coordinate[3][0] - mro, meteor_coordinate[3][1] - mro, meteor_size_mid, meteor_size_mid)

center_rect = pygame.Rect(meteor_coordinate[4][0] - mro, meteor_coordinate[4][1] - mro, meteor_size_mid, meteor_size_mid)

# TO BE USED IN COLLISION CALCULATION

meteor_rectangle_collision =        		     [[left_top_rect.centerx , left_top_rect.centery], [right_top_rect.centerx, right_top_rect.centery], [right_bottom_rect.centerx, right_bottom_rect.centery], [left_bottom_rect.centerx, left_bottom_rect.centery], [center_rect.centerx, center_rect.centery]]

#meteor_rectangle_collision =        		     [[left_top_rect.centerx - os , left_top_rect.centery - os], [right_top_rect.centerx - os, right_top_rect.centery - os], [right_bottom_rect.centerx - os, right_bottom_rect.centery - os], [left_bottom_rect.centerx - os, left_bottom_rect.centery - os], [center_rect.centerx - os, center_rect.centery -os]]


meteor_coordinate_rect = pygame.Rect(screen_width - controller_space[0]  - controller_size[0], screen_height - 2*controller_space[0]  - 2* controller_size[0], controller_size[0], controller_size[0])

level_1_world = [sw * 0.5, sh * 0.5]
#level_1_image_rect= pygame.Rect(level_1_world[0], level_1_world[1], meteor_size_big, meteor_size_big )

#level_2_world = [[sw - ol,  ol], [ol, sh - ol]]
level_2_world = [[ om,  om], [om, sh - om]]

level_3_world = [[om,om], [sw - om,  om], [om, sh - om]]

level_4_world = [[om,om], [sw - om,  om], [om, sh - om], [sw - om, sh - om]]

level_5_world = [[om,om], [sw - om,  om], [om, sh - om], [sw - om, sh - om], [sw * 0.5, sh * 0.5]]

#level_5_world = [[sw * 0.5, sh * 0.5],[om,om], [sw - om,  om], [om, sh - om]]

#level_4_world =  [[sw - om,  om], [om, sh - om],[om,om], [width  - om, height - om]]

#level_5_world = [[sw - os, os, sw - os, os], [os, os ,sw - os, os], [os, sh - 2*os, os, sh - os], [os , sh - 2*os, sw - os *2, sh - 2*os]]

level_6_world = [[0, 0, sw + os, 0], [0,0,0,sh+ os], [sw, sh , sw-os, sh], [sw, sh, sw, sh - os], [math.ceil(sw/2), math.ceil((sh-ol)/2), math.ceil(sw/2), sh - math.ceil((sh-ol)/2)]]

level_7_world = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

level_8_world = [[0, 0, sw + om, 0], [0,0,0,sh+ om], [sw, sh , sw-om, sh], [sw, sh, sw, sh - om], [0, sh - om, 0, sh], [0, sh , om, sh], [sw - om, 0, sw,0],[sw, 0, sw, sh+ om]]


level_9_world = [[0, 0, sw + om, 0], [0,0,0,sh+ om], [sw, sh , sw-om, sh], [sw, sh, sw, sh - om], [math.ceil(sw/2), math.ceil((sh-ol)/2), math.ceil(sw/2), sh - math.ceil((sh-ol)/2)], [0, sh - om, 0, sh], [0, sh , om, sh], [sw - om, 0, sw,0],[sw, 0, sw, sh+ om]]


meteor_1 = pygame.image.load("game_objects/meteor_image_1.png")

meteor_2 = pygame.image.load("game_objects/meteor_image_2.png")

meteor_3 = pygame.image.load("game_objects/meteor_image_3.png")

meteor_4 = pygame.image.load("game_objects/meteor_image_4.png")

meteor_5 = pygame.image.load("game_objects/meteor_image_5.png")

meteor_6 = pygame.image.load("game_objects/meteor_image_6.png")

meteor_7 = pygame.image.load("game_objects/meteor_image_7.png")

meteor_8 = pygame.image.load("game_objects/meteor_image_1.png")

meteor_9 = pygame.image.load("game_objects/meteor_image_1.png")

meteor_10 = pygame.image.load("game_objects/meteor_image_1.png")

meteor_11 = pygame.image.load("game_objects/meteor_image_1.png")

#Tramsformed to big

meteor_l = [																pygame.transform.scale(meteor_1, (meteor_size_big, meteor_size_big)), 			pygame.transform.scale(meteor_2,           		 (meteor_size_big, meteor_size_big)), 			pygame.transform.scale(meteor_3, (meteor_size_big, meteor_size_big)),
pygame.transform.scale(meteor_4, (meteor_size_big * 2, meteor_size_big * 2)), 
pygame.transform.scale(meteor_5, (meteor_size_big, meteor_size_big)), 
pygame.transform.scale(meteor_6, (meteor_size_big, meteor_size_big)),
pygame.transform.scale(meteor_7, (meteor_size_big, meteor_size_big)),			pygame.transform.scale(meteor_8, (meteor_size_big, meteor_size_big)), 			pygame.transform.scale(meteor_9, (meteor_size_big, meteor_size_big)) 
]

#TRANSFORMED TO MIDDIUM SIZE

#meteor_l_mid = [																pygame.transform.scale(meteor_1, (meteor_size_mid, meteor_size_mid)), 			pygame.transform.scale(meteor_2,           		 (meteor_size_mid, meteor_size_mid)), 			pygame.transform.scale(meteor_3, (meteor_size_mid, meteor_size_mid)), pygame.transform.scale(meteor_4, (meteor_size_mid, meteor_size_mid)), pygame.transform.scale(meteor_5, (meteor_size_mid, meteor_size_mid)), pygame.transform.scale(meteor_6, (meteor_size_mid, meteor_size_mid)), pygame.transform.scale(meteor_7, (meteor_size_mid, meteor_size_mid)), pygame.transform.scale(meteor_8, (meteor_size_mid, meteor_size_mid)), pygame.transform.scale(meteor_9, (meteor_size_mid, meteor_size_mid)) ]
e = 0# e = edge
meteor_l_mid = [																pygame.transform.scale(meteor_1, (meteor_size_mid + e, meteor_size_mid + e)), 			pygame.transform.scale(meteor_2,           		 (meteor_size_mid + e, meteor_size_mid + e)), 			pygame.transform.scale(meteor_3, (meteor_size_mid + e, meteor_size_mid + e)), pygame.transform.scale(meteor_4, (meteor_size_mid + e, meteor_size_mid + e)), pygame.transform.scale(meteor_5, (meteor_size_mid + e, meteor_size_mid + e)), pygame.transform.scale(meteor_6, (meteor_size_mid + e, meteor_size_mid + e)), pygame.transform.scale(meteor_7, (meteor_size_mid + e, meteor_size_mid + e)), pygame.transform.scale(meteor_8, (meteor_size_mid + e, meteor_size_mid + e)), pygame.transform.scale(meteor_9, (meteor_size_mid + e, meteor_size_mid + e)) ]

#TRANSFORMED TO SMALL

meteor_l_small = [																pygame.transform.scale(meteor_1, (meteor_size_small, meteor_size_small)), 			pygame.transform.scale(meteor_2,           		 (meteor_size_small, meteor_size_small)), 			pygame.transform.scale(meteor_3, (meteor_size_small, meteor_size_small)),
pygame.transform.scale(meteor_4, (meteor_size_small, meteor_size_small)), 
pygame.transform.scale(meteor_5, (meteor_size_small, meteor_size_small)), 
pygame.transform.scale(meteor_6, (meteor_size_small, meteor_size_small)),
pygame.transform.scale(meteor_7, (meteor_size_small, meteor_size_small)),			pygame.transform.scale(meteor_8, (meteor_size_small, meteor_size_small)), 			pygame.transform.scale(meteor_9, (meteor_size_small, meteor_size_small)) 
]


#meteors_center_coord = []
def display_meteor():
  
  # ----level 1 since we have 1 meteors
  meteor_level_1_rotating = pygame.transform.rotate(meteor_l_mid[0], (meteor_rotation[0]))
  
  # ----level 2 since we have 2 meteors
  meteor_1_level_2_rotating = pygame.transform.rotate(meteor_l_mid[1], (meteor_rotation[0]))
  
  meteor_2_level_2_rotating= pygame.transform.rotate(meteor_l_mid[2], (meteor_rotation[1]))
  
  # ----level 3 since we have 3 meteors
  meteor_1_level_3_rotating= pygame.transform.rotate(meteor_l_mid[1], (meteor_rotation[0]))
  
  meteor_2_level_3_rotating=pygame.transform.rotate(meteor_l_mid[1], (meteor_rotation[1]))
  
  meteor_3_level_3_rotating= pygame.transform.rotate(meteor_l_mid[0], (meteor_rotation[2]))
  
  # ----level 4 since we have 4 meteors
  meteor_1_level_4_rotating= pygame.transform.rotate(meteor_l_mid[1], (meteor_rotation[0]))
  
  meteor_2_level_4_rotating=pygame.transform.rotate(meteor_l_mid[1], (meteor_rotation[1]))
  
  meteor_3_level_4_rotating= pygame.transform.rotate(meteor_l_mid[0], (meteor_rotation[2]))
  
  meteor_4_level_4_rotating= pygame.transform.rotate(meteor_l_mid[2], (meteor_rotation[0]))
  
  # center coordinate    short _ name for use below
  a = int(meteor_level_1_rotating.get_width()) * 0.5 
  b = int(meteor_level_1_rotating.get_height()) * 0.5

  if  LEVEL == 1 or LEVEL == 11 or LEVEL == 21 or LEVEL == 31 or LEVEL == 41 or LEVEL == 51 or LEVEL == 61 or LEVEL == 71 or LEVEL == 81 or LEVEL == 91:
    snake_speed_list[0] = 10
    #pygame.draw.rect(screen, RED, center_rect, 4 )
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[4][0], meteor_rectangle_collision[4][1]] , meteor_size_mid * 0.5 ,4 )
    
    screen.blit(meteor_level_1_rotating,(meteor_coordinate[4][0] - a , meteor_coordinate[4][1] - b))
  
  
  if LEVEL == 2 or LEVEL == 12 or LEVEL == 22 or LEVEL == 32 or LEVEL ==  42 or LEVEL == 52 or LEVEL == 62 or LEVEL == 72 or LEVEL == 82:
    snake_speed_list[0] = 15
  
  # RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect, 4 )
    #pygame.draw.rect(screen, RED, left_bottom_rect ,4)
    
    # CIRCLE
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[3][0], meteor_rectangle_collision[3][1]] , meteor_size_mid * 0.5 ,4 )
    
    
    screen.blit(meteor_1_level_2_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_2_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_2_rotating.get_height()) * 0.5) )
    
    
    screen.blit(meteor_2_level_2_rotating,(meteor_coordinate[3][0] - int(meteor_2_level_2_rotating.get_width()) * 0.5 ,  meteor_coordinate[3][1] - int(meteor_2_level_2_rotating.get_height()) * 0.5) )
    
    
    
  if LEVEL == 3 or LEVEL == 13 or LEVEL == 23 or LEVEL == 33 or LEVEL == 43 or LEVEL == 53 or LEVEL == 63  or LEVEL == 73 or LEVEL == 83 or LEVEL == 93:
    
    snake_speed_list[0] = 20
    # RECTANGLE
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    #pygame.draw.rect(screen, RED, right_bottom_rect, 4 )
    
    # CIRCLE
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[2][0], meteor_rectangle_collision[2][1]] , meteor_size_mid * 0.5 ,4 )
    
    
    
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[2][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[2][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    
  
  
  if LEVEL == 4 or LEVEL == 14 or LEVEL == 24 or LEVEL == 34 or LEVEL == 44 or LEVEL == 54 or LEVEL == 64  or LEVEL == 74 or LEVEL == 84 or LEVEL == 94:
    snake_speed_list[0] = 25
    #screen.blit(meteor_l[3],(0, sh - ol +10))
    
    # RECTANGLE
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    #pygame.draw.rect(screen, RED, left_bottom_rect , 4)
    #pygame.draw.rect(screen, RED, center_rect, 4 )
    # CIRCLE
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[3][0], meteor_rectangle_collision[3][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[4][0], meteor_rectangle_collision[4][1]] , meteor_size_mid * 0.5 ,4 )
    
    screen.blit(meteor_1_level_4_rotating,(meteor_coordinate[1][0] - int(meteor_1_level_4_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_1_level_4_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_4_rotating,(meteor_coordinate[3][0] - int(meteor_2_level_4_rotating.get_width()) * 0.5 ,  meteor_coordinate[3][1] - int(meteor_2_level_4_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_4_rotating,(meteor_coordinate[4][0] - int(meteor_3_level_4_rotating.get_width()) * 0.5 ,  meteor_coordinate[4][1] - int(meteor_3_level_4_rotating.get_height()) * 0.5) )
    
  if LEVEL == 5 or LEVEL == 15 or LEVEL == 25 or LEVEL == 35 or LEVEL == 45 or LEVEL == 55 or LEVEL == 65  or LEVEL == 75 or LEVEL == 85 or LEVEL == 95:
    snake_speed_list[0] = 30
    
    
    #RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect, 4 )
    #pygame.draw.rect(screen, RED, left_bottom_rect , 4)
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    
    # CIRCLE
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[3][0], meteor_rectangle_collision[3][1]] , meteor_size_mid * 0.5 ,4 )
    
    # METEOR IMAGE
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[3][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[3][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    
  
  if LEVEL == 6 or LEVEL == 16 or LEVEL == 26 or LEVEL == 36 or LEVEL == 46 or LEVEL == 56  or LEVEL == 66  or LEVEL == 76 or LEVEL == 86 or LEVEL == 96:
    snake_speed_list[0] = 30
    
    #RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect, 4 )
    #pygame.draw.rect(screen, RED, right_top_rect, 4 )
    #pygame.draw.rect(screen, RED, right_bottom_rect, 4 )
    
    # CIRCLE
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[2][0], meteor_rectangle_collision[2][1]] , meteor_size_mid * 0.5 ,4 )
    
    # METEOR IMAGE
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[2][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[2][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    
  
  if LEVEL == 7  or LEVEL == 17 or LEVEL == 27 or LEVEL == 37 or LEVEL == 47 or LEVEL == 57 or LEVEL == 67 or LEVEL == 77 or LEVEL == 87 or LEVEL == 97:
    snake_speed_list[0] = 30
    
    #RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect, 4 )
    #pygame.draw.rect(screen, RED, left_bottom_rect, 4 )
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    #pygame.draw.rect(screen, RED, center_rect, 4 )
    # CIRCLE
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[3][0], meteor_rectangle_collision[3][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[4][0], meteor_rectangle_collision[4][1]] , meteor_size_mid * 0.5 ,4 )
    
    # METEOR IMAGE
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[3][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[3][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    
    screen.blit(meteor_level_1_rotating,(meteor_coordinate[4][0] - a , meteor_coordinate[4][1] - b))
    
    
  
  if LEVEL == 8 or LEVEL == 18 or LEVEL == 28 or LEVEL == 38 or LEVEL == 48 or LEVEL == 58 or LEVEL == 68 or LEVEL == 78 or LEVEL == 88 or LEVEL == 98:
    snake_speed_list[0] = 30
    #RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect,4 )
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    #pygame.draw.rect(screen, RED, right_bottom_rect , 4)
    #pygame.draw.rect(screen, RED, center_rect, 4 )
    
    #CIRCLE
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[2][0], meteor_rectangle_collision[2][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[4][0], meteor_rectangle_collision[4][1]] , meteor_size_mid * 0.5 ,4 )

    #METEOR IMAGE
    
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[2][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[2][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    screen.blit(meteor_level_1_rotating,(meteor_coordinate[4][0] - a , meteor_coordinate[4][1] - b))
    
  if LEVEL == 9 or LEVEL == 19 or LEVEL == 29 or LEVEL == 39 or LEVEL == 49 or LEVEL == 59 or LEVEL == 69  or LEVEL == 79 or LEVEL == 89 or LEVEL == 99:
    snake_speed_list[0] = 30
    #RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect, 4 )
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    #pygame.draw.rect(screen, RED, right_bottom_rect, 4 )
    #pygame.draw.rect(screen, RED, left_bottom_rect, 4 )
    
    #CIRCLE
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[2][0], meteor_rectangle_collision[2][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[3][0], meteor_rectangle_collision[3][1]] , meteor_size_mid * 0.5 ,4 )
    
    # METEOR IMAGE
    
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[2][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[2][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[3][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[3][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))

  if LEVEL == 10 or LEVEL == 20 or LEVEL == 30 or LEVEL == 40 or LEVEL == 50  or  LEVEL == 60 or LEVEL == 70  or LEVEL == 80 or LEVEL == 90 or LEVEL == 100:
    snake_speed_list[0] = 30
    #RECTANGLE
    #pygame.draw.rect(screen, RED, left_top_rect, 4 )
    #pygame.draw.rect(screen, RED, right_top_rect , 4)
    #pygame.draw.rect(screen, RED, right_bottom_rect , 4)
    #pygame.draw.rect(screen, RED, left_bottom_rect , 4)
    #pygame.draw.rect(screen, RED, center_rect,4 )
    #CIRCLE
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[0][0], meteor_rectangle_collision[0][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[1][0], meteor_rectangle_collision[1][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[2][0], meteor_rectangle_collision[2][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[3][0], meteor_rectangle_collision[3][1]] , meteor_size_mid * 0.5 ,4 )
    
    #pygame.draw.circle(screen, RED, [meteor_rectangle_collision[4][0], meteor_rectangle_collision[4][1]] , meteor_size_mid * 0.5 ,4 )
    
    
    #METEOR IMAGE
    screen.blit(meteor_1_level_3_rotating,(meteor_coordinate[0][0] - int(meteor_1_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[0][1] - int(meteor_1_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_2_level_3_rotating,(meteor_coordinate[1][0] - int(meteor_2_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[1][1] - int(meteor_2_level_3_rotating.get_height()) * 0.5) )
    
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[2][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[2][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    screen.blit(meteor_3_level_3_rotating,(meteor_coordinate[3][0] - int(meteor_3_level_3_rotating.get_width()) * 0.5 ,  meteor_coordinate[3][1] - int(meteor_3_level_3_rotating.get_height()) * 0.5))
    screen.blit(meteor_level_1_rotating,(meteor_coordinate[4][0] - a , meteor_coordinate[4][1] - b))
    
    ##################
    ##### EXPLOSION  ####
    ##################
    
meteor_explosion_sound_0 = pygame.mixer.Sound("snake_audio_files/meteor_explosion_audio_0.wav")

meteor_explosion_0= pygame.image.load("game_objects/meteor_explosion_0.png")
# <a href="https://www.freeiconspng.com/img/45932">Explosion Transparent Clipart Pictures</a>

meteor_explosion_1= pygame.image.load("game_objects/meteor_explosion_1.png")
#<a href="https://www.freeiconspng.com/img/45929">Free Explosion Transparent Pictures</a>
explosion_size = int(meteor_size_mid *2)

#meteor_explosion_0.set_colorkey(BLACK)
#meteor_explosion_0.SET_COLOR_KEY(BLACK)

meteor_explosion_l = [pygame.transform.scale(meteor_explosion_0, (explosion_size, explosion_size)), pygame.transform.scale(meteor_explosion_1, (explosion_size + 50, explosion_size + 20))]


def meteor_explosion(x,y):
    collision_time = pygame.time.get_ticks()
  
    meteor_explosion_sound_0.play()
    
    if current_time - collision_time <= 2000:
      screen.blit(meteor_explosion_l[1], (x - meteor_size_mid,y - meteor_size_mid))
    
      screen.blit(meteor_explosion_l[0], (x - meteor_size_mid,y - meteor_size_mid))
      
def reset_snake_position():
    snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]		
    #screen.blit(meteor_l[1],(screen_width * 0.5, screen_height * 0.5) )
    
    ##################
    ## RESET GAME LEVEL ##
    ##################
    
        #################
        #######GAME######
        #######START######
        #################

running = True
while running:

  #disp_screen()
  
  clock.tick(snake_speed)
  
  current_time = pygame.time.get_ticks()
  
  #screen.fill((0,0,0))
  screen.fill(BACKGROUND)
  background_image()
  display_meteor()				
  
  meteor_rotation[0] += 1
  meteor_rotation[1]  += 5
  meteor_rotation[2] += 10
  
  collide_with_next_level[0] = 0 # not colliding
  # === SNAKE BODY CENTER FOR COLLISION ==
  snake_body_rect = pygame.Rect(snake_body[0][0],snake_body[0][1], snake_width, snake_height)

  snake_body_center[0]= snake_body_rect.centerx
  snake_body_center[1]= snake_body_rect.centery
  
  
  #@@@@@@@@@@@@@@@@@@@@@@@@@
  #draw_rect()
  #@@@@@@@@@@@@@@@@@@@@@@@@@
  
  
  
  current_time = pygame.time.get_ticks()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = True
      
    if event.type == pygame.VIDEORESIZE:
      width, height = event.w, event.h
    
      #disp_screen(width, height)
      
    if event.type == pygame. MOUSEBUTTONDOWN:
    
      #snake_speed = 15
      # controller click
      mousex, mousey = pygame.mouse.get_pos()
      # distance between mouse and up
      
      distance_with_up = int(math.sqrt((mousex - up_rectangle.centerx)**2 + (mousey - up_rectangle.centery)**2))
      
      # distance between mouse and right
      distance_with_right= int(math.sqrt((mousex - right_rectangle.centerx)**2 + (mousey - right_rectangle.centery)**2))
      
      # distance between mouse and down
      distance_with_down = int(math.sqrt((mousex - down_rectangle.centerx)**2 + (mousey - down_rectangle.centery)**2))
      
    
      
      # distance between mouse and left
      distance_with_left = int(math.sqrt((mousex - left_rectangle.centerx)**2 + (mousey - left_rectangle.centery)**2))
      # CONTROLLER CLICK
      if distance_with_up <=   controller_click_distance:
        
        head_right= False
        head_left = False
        head_up = True
        head_down = False
        
        up_clicked = True
        right_clicked = False
        down_clicked = False
        left_clicked = False
        
      elif distance_with_right <=   controller_click_distance:
        head_right= True
        head_left = False
        head_up = False
        head_down = False
        
        up_clicked = False
        right_clicked = True
        down_clicked = False
        left_clicked = False
        
        
      elif distance_with_down <=   controller_click_distance:
        head_right= False
        head_left = False
        head_up = False
        head_down = True
        
        up_clicked = False
        right_clicked = False
        down_clicked = True
        left_clicked = False
        
      elif distance_with_left <=   controller_click_distance:
        head_right= False
        head_left = True
        head_up = False
        head_down = False
        
        up_clicked = False
        right_clicked = False
        down_clicked = False
        left_clicked = True
        
        #left_click_time = pygame.time.get_ticks()
        #if current_time - left_click_time > 4000:
          #snake_speed = 15
      else:
        #---------------------
        snake_speed= 40
        #---------------------
      #if game_over:
      #game_over = False
      
    if event.type == pygame. MOUSEBUTTONUP:
    
      if LEVEL_2  % food_amount_to_change_level == 0:
        snake_speed = 20
      else:
        snake_speed = LEVEL_2 % food_amount_to_change_level + 3 
        
      #reset_level_speed()
      up_clicked = False
      right_clicked = False
      down_clicked = False
      left_clicked = False
      #snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
    if event.type == pygame.KEYDOWN and game_over == False:
      if event.key == pygame.K_LEFT: # or distance_with_left <=   controller_click_distance:
        if head_right == True:
          #GAME OVER
          head_right= False
          head_left = False
          head_up = False
          head_down = False
        else:
          head_right= False
          head_left = True
          head_up = False
          head_down = False
      
        
        
      if event.key == pygame.K_RIGHT:# or distance_with_right <=   controller_click_distance: 
        if head_left == True:
          # GAME OVER
          head_right= False
          head_left = False
          head_up = False
          head_down = False
        else:
          
          head_right= True
          head_left = False
          head_up = False
          head_down = False
          
        
      if event.key == pygame.K_UP:# or distance_with_up <=   controller_click_distance:
        if head_down == True:
          #GAME OVER
          head_right= False
          head_left = False
          head_up = False
          head_down = False
        else:
          head_right= False
          head_left = False
          head_up = True
          head_down = False
          
        
      if event.key == pygame.K_DOWN:# or distance_with_down <=   controller_click_distance:
        
        if head_up == True:
          #GAME OVER
          head_right= False
          head_left = False
          head_up = False
          head_down = False
        else:
          head_right= False
          head_left = False
          head_up = False
          head_down= True
          
    
    #	if head_right= False and head_left = False and head_up = False and head_down= True:
      # CONTROLLERS CLICKED
  #if head_right or head_left or head_up or head_down:
    
  if head_right== False and head_left == False and head_up == False and head_down == True:
    play_sound[0] = 0
    
  if head_right:
#------------------------------------------------------
    update_body()
#------------------------------------------------------
    snake_body[0]= [snake_body[0][0] + 40, snake_body[0][1] ]
    play_sound[0] = 1
    
  if head_left:
#------------------------------------------------------
        update_body()
#------------------------------------------------------
        snake_body[0]= [snake_body[0][0] -40, snake_body[0][1] ]
        play_sound[0] = 1
        
  if head_up:
#------------------------------------------------------
    update_body()
#------------------------------------------------------
    snake_body[0]= [snake_body[0][0] , snake_body[0][1] - 40]
    play_sound[0] = 1

  if head_down:
#------------------------------------------------------
    update_body()
#------------------------------------------------------
    snake_body[0]= [snake_body[0][0] , snake_body[0][1] + 40]
    play_sound[0] = 1
  
  #if game_over == True:
    #reset_snake_position()
#------------------------------------------------------
  draw_snake( snake_body)
#------------------------------------------------------
          ################
          # SWALLOWING FOOD#
          ####    SCORE  ######
          ################
          
  food_distance_with_left_top_meteor[0] = int(math.sqrt((meteor_rectangle_collision[0][0] - food_l[0][0])**2 +(meteor_rectangle_collision[0][1] - food_l[0][1])**2))
  f_d_l_t_m = food_distance_with_left_top_meteor[0]
  
  food_distance_with_right_top_meteor[0] = int(math.sqrt((meteor_rectangle_collision[1][0] - food_l[0][0])**2 +(meteor_rectangle_collision[1][1] - food_l[0][1])**2))
  f_d_r_t_m = food_distance_with_right_top_meteor[0]
  
  food_distance_with_right_bottom_meteor[0] = int(math.sqrt((meteor_rectangle_collision[2][0] - food_l[0][0])**2 +(meteor_rectangle_collision[2][1] - food_l[0][1])**2))
  
  f_d_r_b_m  = food_distance_with_right_bottom_meteor[0]
  
  food_distance_with_left_bottom_meteor[0] = int(math.sqrt((meteor_rectangle_collision[3][0] - food_l[0][0])**2 +(meteor_rectangle_collision[3][1] - food_l[0][1])**2))
  
  
  f_d_l_b_m = food_distance_with_left_bottom_meteor[0]
  
  food_distance_with_center_meteor[0] = int(math.sqrt((meteor_rectangle_collision[4][0] - food_l[0][0])**2 +(meteor_rectangle_collision[4][1] - food_l[0][1])**2))			
  
  f_d_c_m = 	food_distance_with_center_meteor[0] + 40
  
  
  
  #swallow_food_child = int(math.sqrt((food_rectangle_coord[0] - snake_body[0][0])**2 +(food_rectangle_coord[1] - snake_body[0][1])**2))		
  
  swallow_food_child = int(math.sqrt((food_l[0][0] - snake_body[0][0])**2 +(food_l[0][1] - snake_body[0][1])**2))

    
          ################
          #### COLLISION####
          ################
          
  # if snake  eats itself  and if not [magic movment]
      #gameover
  for parts in range(1,len(snake_body) ):
    if snake_body[0][0] == snake_body[parts][0] and snake_body[0][1] == snake_body[parts][1]:
      
      game_over_1 = True
      reset_snake_position()
      meteor_explosion(snake_body[0][0] , snake_body[0][1] )
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      break
      
      
# ADD  CLOSED SCREEN MODE HERE
  
  # COLLISSION WITH  SCREEN
  if  snake_body[0][0] < 0:
    snake_body[0]= [screen_width + 40, snake_body[0][1]]

  if  snake_body[0][0]  > screen_width + 40:
    snake_body[0]= [0 , snake_body[0][1]]
    
  if snake_body[0][1] < 0: 
    snake_body[0]= [snake_body[0][0] , screen_height + 40]
  
  if snake_body[0][1] > screen_height + 40 :		
      snake_body[0]= [snake_body[0][0] , 0]
    
  if game_over_1:
    head_right= True
    head_left = False				
    head_up = False
    head_down = False
    
    # RESET SNAKE SIZE
    reset_snake_position()
    snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    game_over_1 = False
    
    # COLLISSION WITH METEOR
#level_1_world = [sw * 0.5, sh * 0.5]

#level_2_world = [[ om,  om], [om, sh - om]]

#level_3_world = [[om,om], [sw - om,  om], [om, sh - om]]

#level_4_world = [[om,om], [sw - om,  om], [om, sh - om], [sw - om, sh - om]]

#swallow_food_child = int(math.sqrt((food_l[0][0] - snake_body[0][0])**2 +(food_l[0][1] - snake_body[0][1])**2))
#meteor_rectangle_collision

  # ======== COLLISION=============
  # ======= WITH METEOR ==========
  
  distance_with_left_top_meteor[0] = int(math.sqrt((meteor_rectangle_collision[0][0] - snake_body_center[0])**2 +(meteor_rectangle_collision[0][1] - snake_body_center[1])**2))
  m_1 = distance_with_left_top_meteor[0]
  
  distance_with_right_top_meteor[0] = int(math.sqrt((meteor_rectangle_collision[1][0] - snake_body_center[0])**2 +(meteor_rectangle_collision[1][1] - snake_body_center[1])**2))
  m_2 = distance_with_right_top_meteor[0]
  
  distance_with_right_bottom_meteor[0] = int(math.sqrt((meteor_rectangle_collision[2][0] - snake_body_center[0])**2 +(meteor_rectangle_collision[2][1] - snake_body_center[1])**2))
  
  m_3 = distance_with_right_bottom_meteor[0]
  
  distance_with_left_bottom_meteor[0] = int(math.sqrt((meteor_rectangle_collision[3][0] - snake_body_center[0])**2 +(meteor_rectangle_collision[3][1] - snake_body_center[1])**2))
  
  m_4 = distance_with_left_bottom_meteor[0]
  
  distance_with_center_meteor[0] = int(math.sqrt((meteor_rectangle_collision[4][0] - snake_body_center[0])**2 +(meteor_rectangle_collision[4][1] - snake_body_center[1])**2))
  
  m_5 = distance_with_center_meteor[0]
  
  collision_distance = om * 0.5 
  f_t_m = 150 #food_to_meteor_offset
  f_t_l = food_amount_to_change_level
  s_t_l = score_to_change_level
  
  
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
  # check if it is  last food of level
  if SCORE > 0:
    s = collision_distance * 2
    if SCORE  % f_t_l == s_t_l[LEVEL - 1] - 1 % f_t_l:
      s = collision_distance * 3
    else: 
      s = collision_distance * 2
    
  #swallow_food_2 = int(math.sqrt((food_2_rectangle_coord[0] - snake_body_center[0])**2 +(food_2_rectangle_coord[1] - snake_body_center[1])**2))
  swallow_food_2 = int(math.sqrt((food_2_l[0][0] - snake_body[0][0])**2 +(food_2_l[0][1] - snake_body[0][1])**2))
  draw_food_2(food_2_l[0][0], food_2_l[0][1])
  
  
  if swallow_food_2< block:
    SCORE_2 += 1
    #snake_speed += 1
    swallow_sound.play()
    
    for i in range( len(score_to_change_level)):
      
      if SCORE_2 == score_to_change_level[i]:
        
        snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
        
        #head_right= False
      #	head_left = False
    #		head_up = False
  #			head_down = False
        
        LEVEL += 1
        
    # check score to change level
    
    generate_food_2 = True
        
    while generate_food_2:
        food_2_l[0][0] = int(random.randint(0,screen_width - 40))
        food_2_l[0][1] = int(random.randint(0,screen_height - 40))
#----- part 1111 -----------------------------				
        # means collides with next levels meteor
        if m_1 > s  and m_2 > s  and m_3 > s  and m_4 > s  and m_5 > s :
          far_from_meteor[0] = 1
        else:
          far_from_meteor[0] = 0
          
#----222-------------------------------------
        for parts in range(1,len(snake_body)):
          
          distance_of_food_2_snake = int(math.sqrt((food_2_l[0][0] - snake_body[parts][0])**2 +(food_2_l[0][1] - snake_body[parts][1])**2))
          
          if distance_of_food_2_snake <= 40 :
            
            #far_from_food[0] = 0
            break
              
          if parts == len(snake_body) - 1:
            
            far_from_food[0]= 1
            
#-----333  ---------------------------------									
        #far_from_meteor == True
        
        if far_from_food[0] == 1 and far_from_meteor[0] == 1: 
          generate_food_2 = False
          
          snake_body.append([snake_body[len(snake_body) - 1][0], snake_body[len(snake_body) - 1][1]])
          move_sound.play()
          break
  
  
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
  #collision_distance = int(math.sqrt(2 * (meteor_size_mid)**2))
  R = 0.5
  
  if  LEVEL == 1 or LEVEL == 11 or LEVEL == 21 or LEVEL == 31 or LEVEL == 41 or LEVEL == 51 or LEVEL == 61 or LEVEL == 71 or LEVEL == 81 or LEVEL == 91:
  #if LEVEL_2 % f_t_l == 1:
    if distance_with_center_meteor[0] <= collision_distance  - collision_distance * R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5]
      #snake_body = [[100 , 400], [60, 400], [20, 400]]
      meteor_explosion(meteor_rectangle_collision[4][0] , meteor_rectangle_collision[4][1] )	
      #	meteor_explosion[0] = snake_body[0][0]
        #meteor_explosion[1] = snake_body[0][1]
      
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      #game_over = True
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
      
  # next levels meteor coordinate
  
        
    
  if LEVEL == 2 or LEVEL == 12 or LEVEL == 22 or LEVEL == 32 or LEVEL ==  42 or LEVEL == 52 or LEVEL == 62 or LEVEL == 72 or LEVEL == 82:
  #if LEVEL_2 % f_t_l == 2:
  
    if distance_with_left_top_meteor[0] <= collision_distance  - collision_distance * R :
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5] 
      meteor_explosion(meteor_rectangle_collision[0][0] , meteor_rectangle_collision[0][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1= True
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if  distance_with_left_bottom_meteor[0] <= collision_distance  - collision_distance *R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5] 
      meteor_explosion(meteor_rectangle_collision[3][0] , meteor_rectangle_collision[3][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1= True
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
  #	if distance_with_left_bottom_meteor[0] <= collision_distance:
      #collision_counter[0] += 1
      #game_over = True
      

  if LEVEL == 3 or LEVEL == 13 or LEVEL == 23 or LEVEL == 33 or LEVEL == 43 or LEVEL == 53 or LEVEL == 63  or LEVEL == 73 or LEVEL == 83 or LEVEL == 93:
  #if LEVEL_2 % f_t_l == 3:
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5] 
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_right_bottom_meteor[0] <= collision_distance  - collision_distance *R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5] 
      meteor_explosion(meteor_rectangle_collision[2][0] , meteor_rectangle_collision[2][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    #if distance_with_right_bottom_meteor[0] <= collision_distance:
      #collision_counter[0] += 1
      #game_over = True
      
  if LEVEL == 4 or LEVEL == 14 or LEVEL == 24 or LEVEL == 34 or LEVEL == 44 or LEVEL == 54 or LEVEL == 64  or LEVEL == 74 or LEVEL == 84 or LEVEL == 94:
  #if LEVEL_2 % f_t_l == 4:
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * R] 
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_left_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5] 
      meteor_explosion(meteor_rectangle_collision[3][0] , meteor_rectangle_collision[3][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
      
    if distance_with_center_meteor[0] <= collision_distance  - collision_distance * R:
      start_x_l = [snake_size[0] * block]
      start_y_l = [screen_height * 0.5] 
      meteor_explosion(meteor_rectangle_collision[4][0] , meteor_rectangle_collision[4][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
      
  
  if LEVEL == 5 or LEVEL == 15 or LEVEL == 25 or LEVEL == 35 or LEVEL == 45 or LEVEL == 55 or LEVEL == 65  or LEVEL == 75 or LEVEL == 85 or LEVEL == 95:
  #if LEVEL_2 % f_t_l == 5:
    
    
    if distance_with_left_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[0][0] , meteor_rectangle_collision[0][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
  

    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_left_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[3][0] , meteor_rectangle_collision[3][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
  
  if LEVEL == 6 or LEVEL == 16 or LEVEL == 26 or LEVEL == 36 or LEVEL == 46 or LEVEL == 56  or LEVEL == 66  or LEVEL == 76 or LEVEL == 86 or LEVEL == 96:
    
    if distance_with_left_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[0][0] , meteor_rectangle_collision[0][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_right_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[2][0] , meteor_rectangle_collision[2][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    
  if LEVEL == 7 or LEVEL == 17 or LEVEL == 27 or LEVEL == 37 or LEVEL == 47 or LEVEL == 57 or LEVEL == 67 or LEVEL == 77 or LEVEL == 87 or LEVEL == 97:
    if distance_with_left_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[0][0] , meteor_rectangle_collision[0][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_left_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[3][0] , meteor_rectangle_collision[3][1] )
    
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_center_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[4][0] , meteor_rectangle_collision[4][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
  
  if LEVEL == 8 or LEVEL == 18 or LEVEL == 28 or LEVEL == 38 or LEVEL == 48 or LEVEL == 58 or LEVEL == 68 or LEVEL == 78 or LEVEL == 88 or LEVEL == 98:
    
    if distance_with_left_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[0][0] , meteor_rectangle_collision[0][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_right_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[2][0] , meteor_rectangle_collision[2][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    if distance_with_center_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[4][0] , meteor_rectangle_collision[4][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
  
  if LEVEL == 9 or LEVEL == 19 or LEVEL == 29 or LEVEL == 39 or LEVEL == 49 or LEVEL == 59 or LEVEL == 69  or LEVEL == 79 or LEVEL == 89 or LEVEL == 99:
    if distance_with_left_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[0][0] , meteor_rectangle_collision[0][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_right_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[2][0] , meteor_rectangle_collision[2][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_left_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[3][0] , meteor_rectangle_collision[3][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
  
  
  if LEVEL == 10 or LEVEL == 20 or LEVEL == 30 or LEVEL == 40 or LEVEL == 50  or  LEVEL == 60 or LEVEL == 70  or LEVEL == 80 or LEVEL == 90 or LEVEL == 100:
    
    if distance_with_right_top_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[1][0] , meteor_rectangle_collision[1][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_right_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[2][0] , meteor_rectangle_collision[2][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
      
    if distance_with_left_bottom_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[3][0] , meteor_rectangle_collision[3][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
    if distance_with_center_meteor[0] <= collision_distance  - collision_distance * R:
      meteor_explosion(meteor_rectangle_collision[4][0] , meteor_rectangle_collision[4][1] )
      
      far_from_meteor[0] = 0
      far_from_food[0] = 0
      reset_snake_position()
      game_over_1 = True
      snake_body = [[start_x, start_y], [start_x -block, start_y], [start_x - block*2, start_y]]
    
  # affter 3 collisions
    if game_over_1 == True:
      head_right= False
      head_left = False
      head_up = False
      head_down = False
      
  #display_meteor()				
  #generate_wall_1( 50,50, 50,200)
  display_level_and_score( LEVEL, SCORE_2)
    
  draw_controller()
  
  pygame.display.update()

  
        
  
  
