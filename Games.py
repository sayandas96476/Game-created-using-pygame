
import pygame
import random
import sys

pygame.init()
HEIGHT=800
WIDTH=600
RED=(255,0,0)
BLUE=(0,0,255)
#GREEN=(0,255,200)
GREEN=(50,50,50)

YELLOW=(255,255,0)

SPEED=10

clock=pygame.time.Clock()



myFont = pygame.font.SysFont("monospace", 50)




player_pos=[370,501]
player_size=50

enemy_size=50
enemy_pos=[random.randint(0,WIDTH),0]
enemy_list=[enemy_pos]

screen = pygame.display.set_mode((HEIGHT,WIDTH))
gameover = False


score=0

def drop_enemies(enemy_list):
    delay= random.random()
    if len(enemy_list)<5 :
        x_pos=random.randint(0,WIDTH-enemy_size)
        y_pos=0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
          pygame.draw.rect(screen,BLUE,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))



def collision_check(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False




def update_enemy_positions(enemy_list,score):
    for enemy_pos in enemy_list:
        if enemy_pos[1]>=0 and enemy_pos[1]<HEIGHT:
            enemy_pos[1] += SPEED
        else:
            score+=1
            
            enemy_pos[0]=random.randint(0,WIDTH-enemy_size)
            enemy_pos[1]=0
    return score





def detect_collision(player_pos,enemy_pos):
    p_x=player_pos[0]
    p_y=player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if (e_x>p_x+20 and e_x<(p_x+player_size)) or (e_x<p_x and p_x<(e_x+enemy_size)):
        if(e_y>p_y and e_y<(p_y+player_size)) or (p_y>e_y and p_y<(e_y+enemy_size)):
            return True
            #screen.fill(YELLOW)
    return False




while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
         
            x=player_pos[0]
            y=player_pos[1]
            if event.key == pygame.K_LEFT:
                x-=player_size
                
            elif event.key == pygame.K_RIGHT:
    
                x+=player_size

            
            elif event.key == pygame.K_UP:
                y-=player_size

            
            elif event.key == pygame.K_DOWN:
                y+=player_size
            
                
            
                
            player_pos = [x,y]



    screen.fill((YELLOW))
    
    drop_enemies(enemy_list)


    



    score = update_enemy_positions(enemy_list,score)
    text = "Score:"+ str(score) 
    label = myFont.render(text, 1, (GREEN))
    screen.blit(label, (550,545))
   
    


    if collision_check(enemy_list,player_pos):
        gameover=True
        break
  
    draw_enemies(enemy_list)
    

    
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    clock.tick(30)
    pygame.display.update()
