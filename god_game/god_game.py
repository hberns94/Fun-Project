import pygame
import random
import math
import os
import winsound
import names
import numpy as np
from sklearn.cluster import KMeans

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (240, 240, 236)
GREY = (127, 127, 127)
BLUE =  (0, 119, 190)
GREEN = (89, 166, 8)
RED =   (255,   0,   0)
TAN = 	(194, 178, 128)
 
# Set the height and width of the screen
size = [720, 480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("YOU ARE GOD!")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

t=0
t_cloud=0
t_n=0
t_n_r=0
len_old=0
t_boat=0
notif_text=''
rect_length_notif=0
space_text=''

YEAR=6300
year_count=0

land_x=[]
land_y=[]
land_hitbox=[]
land_farm_stage=[]
land_farm_i=[]
land_farm_tended=[]
land_snow=[]
land_tread=[]
grain_x=[]
grain_y=[]
grain_food=[]
settler_x=[]
settler_y=[]
settler_health=[]
settler_home=[]
settler_inv_wood=[]
settler_inv_food=[]
settler_hunger=[]
settler_sheltered=[]
settler_dead_x=[]
settler_dead_y=[]
settler_dead=[]
settler_dead_buried=[]
settler_dead_gender=[]
settler_baby_x=[]
settler_baby_y=[]
settler_baby_parent=[]
settler_baby_age=[]
settler_baby_grown=[]
settler_baby_name=[]
settler_happiness=[]
settler_gender=[]
settler_job=[]
settler_age=[]
settler_social=[]
settler_name=[]
settler_morality=[]
settler_sick=[]
settler_drunk=[]
settler_status=[]
tree_x=[]
tree_y=[]
house_x=[]
house_y=[]
house_upgrade=[]
boat_x=[]
boat_y=[]
boat_landed=[]
boat_otw=0
church_stage=0
church_x=0
church_y=0
church_rendered=0
windmill_stage=[]
windmill_x=[]
windmill_y=[]
tavern_stage=[]
tavern_x=[]
tavern_y=[]
animal_x=[int(size[0]/2),int(size[1]/2)]
animal_y=[int(size[0]/2),int(size[1]/2)]
animal_fertility=[100, 100]
animal_dead_x=[]
animal_dead_y=[]
animal_food=[]
cloud_x=[]
cloud_y=[]
cloud_storm=[]
cloud_cap=[]
cloud_spawner_bool=0
rain_x=[]
rain_y=[]
rain_fall=[]
notification=[]
font=pygame.font.SysFont('timesnewroman',  10)

r_l=10
mod=0.3
fertility=0.5

spawned=0

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path
sound_path = os.path.join(resource_path, 'sounds')

background_music=(os.path.join(sound_path, 'background2.wav'))

winsound.PlaySound(background_music, winsound.SND_LOOP + winsound.SND_ASYNC)

image_settler = pygame.image.load(os.path.join(image_path, 'settler.png')).convert_alpha()
image_settler_f = pygame.image.load(os.path.join(image_path, 'settler_f.png')).convert_alpha()
image_settler_sick = pygame.image.load(os.path.join(image_path, 'settler_sick.png')).convert_alpha()
image_settler_f_sick = pygame.image.load(os.path.join(image_path, 'settler_f_sick.png')).convert_alpha()
image_settler_dead = pygame.image.load(os.path.join(image_path, 'settler_dead.png')).convert_alpha()
image_settler_dead_f = pygame.image.load(os.path.join(image_path, 'settler_dead_f.png')).convert_alpha()
image_settler_baby = pygame.image.load(os.path.join(image_path, 'settler_baby.png')).convert_alpha()
image_tree = pygame.image.load(os.path.join(image_path, 'tree.png')).convert_alpha()
image_house = pygame.image.load(os.path.join(image_path, 'house.png')).convert_alpha()
image_house_st2 = pygame.image.load(os.path.join(image_path, 'house_st2.png')).convert_alpha()
image_house_st3 = pygame.image.load(os.path.join(image_path, 'house_st3.png')).convert_alpha()
image_animal = pygame.image.load(os.path.join(image_path, 'animal.png')).convert_alpha()
image_meat  = pygame.image.load(os.path.join(image_path, 'meat.png')).convert_alpha()
image_grave = pygame.image.load(os.path.join(image_path, 'grave.png')).convert_alpha()
image_church = pygame.image.load(os.path.join(image_path, 'church.png')).convert_alpha()
image_church_st1 = pygame.image.load(os.path.join(image_path, 'church_st1.png')).convert_alpha()
image_church_st2 = pygame.image.load(os.path.join(image_path, 'church_st2.png')).convert_alpha()
image_windmill = pygame.image.load(os.path.join(image_path, 'windmill.png')).convert_alpha()
image_windmill_st2 = pygame.image.load(os.path.join(image_path, 'windmill_st2.png')).convert_alpha()
image_farm_st1 = pygame.image.load(os.path.join(image_path, 'farm_st1.png')).convert_alpha()
image_farm_st2 = pygame.image.load(os.path.join(image_path, 'farm_st2.png')).convert_alpha()
image_farm_st3 = pygame.image.load(os.path.join(image_path, 'farm_st3.png')).convert_alpha()
image_grain = pygame.image.load(os.path.join(image_path, 'grain.png')).convert_alpha()
image_boat = pygame.image.load(os.path.join(image_path, 'boat.png')).convert_alpha()
image_tavern = pygame.image.load(os.path.join(image_path, 'tavern.png')).convert_alpha()

def cal_Dist(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist

def find_centroid(x,y):
    centroid = (int(sum(x) / len(x)),int( sum(y) / len(y)))
    return centroid


def check_land(x,y,settler_tread_bool): 
    for i in range(0,len(land_hitbox)):
        rect=land_hitbox[i] 
        if rect.collidepoint(x,y):
            if settler_tread_bool: land_tread[i]=land_tread[i]+.1
            return rect.collidepoint(x,y)
            break
         

def render_cloud(cloud_x,cloud_y):
    for i in range(0,len(cloud_x)):
        r1=random.randint(25,30)
        r2=random.randint(15,20)
        if cloud_storm[i]:
            pygame.draw.circle(screen,GREY,[cloud_x[i],cloud_y[i]],r1)
        else: pygame.draw.circle(screen,(220,220,220),[cloud_x[i],cloud_y[i]],r2)

def render_rain(rain_x,rain_y):
    if temp<32: color=WHITE
    else: color=(100,100,255)
    for i in range(0,len(rain_x)):
        pygame.draw.circle(screen,color,[rain_x[i],rain_y[i]],0)
        
def render_land(land_x,land_y):
    st1_render=[]
    st2_render=[]
    st3_render=[]

    for i in range(0,len(land_x)):
        if len(land_hitbox[i].collidelistall(land_hitbox))<=5: color=TAN
        elif temp>32:
             if 89+land_tread[i]<180 and 8+land_tread[i]<100: color=(int(89+land_tread[i]), 166,int(8 +land_tread[i]))
             else: color=(180, 135, 100)
        else: color=WHITE
        pygame.draw.rect(screen,color,land_hitbox[i])
        if land_farm_stage[i]>1 and land_farm_stage[i]<2 :
             st1_render.append(i)
        elif land_farm_stage[i]>2 and land_farm_stage[i]<3:
             st2_render.append(i)
        elif land_farm_stage[i]>3:
             st3_render.append(i)
            
    for i in st1_render:
         screen.blit(image_farm_st1, (land_x[i]-10,land_y[i]-10))
    for i in st2_render:
         screen.blit(image_farm_st2, (land_x[i]-10,land_y[i]-10))
    for i in st3_render:
         screen.blit(image_farm_st3, (land_x[i]-10,land_y[i]-10))
             
def render_settler(settler_x,settler_y):
    for i in range(0,len(settler_x)):
        if settler_gender[i]==1:
             if settler_sick[i]: screen.blit(image_settler_sick, (settler_x[i]-1, settler_y[i]-9))
             else: screen.blit(image_settler, (settler_x[i]-1, settler_y[i]-9))
        else:
             if settler_sick[i]: screen.blit(image_settler_f_sick, (settler_x[i]-1, settler_y[i]-9))
             else: screen.blit(image_settler_f, (settler_x[i]-1, settler_y[i]-9))

def render_settler_baby(settler_x,settler_y):
    for i in range(0,len(settler_baby_x)):
        screen.blit(image_settler_baby, (settler_baby_x[i]-1, settler_baby_y[i]-6))

def render_settler_dead(settler_dead_x,settler_dead_y):
    for i in range(0,len(settler_dead_x)):
        if settler_dead_buried[i]: screen.blit(image_grave, (settler_dead_x[i]-1, settler_dead_y[i]-4))
        elif settler_dead_gender[i]: screen.blit(image_settler_dead, (settler_dead_x[i]-4, settler_dead_y[i]-3))
        else: screen.blit(image_settler_dead_f, (settler_dead_x[i]-4, settler_dead_y[i]-3))

def render_tree(tree_x,tree_y):
    for i in range(0,len(tree_x)):
        screen.blit(image_tree, (tree_x[i]-4, tree_y[i]-12))

def render_buildings(house_x,house_y,render_order,church_x,church_y,windmill_x,windmill_y):
    for i in render_order:

        if i in range(0,len(house_x)):
             if house_upgrade[i]<2: screen.blit(image_house, (house_x[i]-6, house_y[i]-18))
             elif house_upgrade[i]<4: screen.blit(image_house_st2, (house_x[i]-6, house_y[i]-22))
             else: screen.blit(image_house_st3, (house_x[i]-6, house_y[i]-24))
        if i ==len(house_x)+int(church_stage>0)-1 and church_stage>0:
            if church_stage<1:
               screen.blit(image_church_st1, (church_x-8, church_y-28))
            elif church_stage<2 and church_stage>1:
               screen.blit(image_church_st2, (church_x-8, church_y-28))
            elif church_stage>2: screen.blit(image_church, (church_x-8, church_y-28))
        elif i >len(house_x)+int(church_stage>0)-1 and i<len(house_x)+int(church_stage>0)-1+len(windmill_stage):
             j=i-len(house_x)-int(church_stage>0)
             if windmill_stage[j]<1 and windmill_stage[j]>0:
                  screen.blit(image_church_st1, (windmill_x[j]-8, windmill_y[j]-28))
             elif windmill_stage[j]<2 and windmill_stage[j]>=1:
                  screen.blit(image_windmill_st2, (windmill_x[j]-8, windmill_y[j]-28))
             elif windmill_stage[j]>=2: screen.blit(image_windmill, (windmill_x[j]-8, windmill_y[j]-28))   
        elif i >len(house_x)+int(church_stage>0)-1+len(windmill_stage):
             j=i-len(house_x)-int(church_stage>0)-len(windmill_stage)
             if tavern_stage[j]<1 and tavern_stage[j]>0:
                  screen.blit(image_church_st1, (tavern_x[j]-8, tavern_y[j]-28))
             elif tavern_stage[j]>=1: screen.blit(image_tavern, (tavern_x[j]-8, tavern_y[j]-20))   

def render_animal(animal_x,animal_y):
    for i in range(0,len(animal_x)):
        screen.blit(image_animal, (animal_x[i]-5, animal_y[i]-8))

def render_meat(animal_dead_x,animal_dead_y):
    for i in range(0,len(animal_dead_x)):
        screen.blit(image_meat, (animal_dead_x[i]-5, animal_dead_y[i]-8))

def render_grain(grain_x,grain_y):
    for i in range(0,len(grain_x)):
        screen.blit(image_grain, (grain_x[i]-4, grain_y[i]-9))

def render_boat(boat_x,boat_y):
    for i in range(0,len(boat_x)):
        screen.blit(image_boat, (boat_x[i]-13, boat_y[i]-19))
    
            

class player:
    
    def draw_land(land_x,land_y):
        mouse_clk=pygame.mouse.get_pressed()
        x_m,y_m=pygame.mouse.get_pos()

        if mouse_clk[0] and not check_land(x_m,y_m,0):
            land_x.append(x_m)
            land_y.append(y_m)
            land_hitbox.append(pygame.Rect(x_m-r_l,y_m-r_l,2*r_l,2*r_l))
            land_farm_stage.append(0)
            land_snow.append(0)
            land_tread.append(0)
            
        del_i=[]
        
        if mouse_clk[2]:
            for i in range(0,len(land_x)):
                if cal_Dist(x_m,y_m,land_x[i],land_y[i])<r_l:
                    del_i.append(i)
                    for j in range(0,len(land_farm_i)):
                        if land_farm_i[j]==i:
                            land_farm_i[j]=-10
                            land_farm_tended[j]=-10
                        if land_farm_i[j]>i and land_farm_i[j]!=-10: land_farm_i[j]=land_farm_i[j]-1
                
        for i in sorted(del_i, reverse=True):
            land_x.pop(i)
            land_y.pop(i)
            land_farm_stage.pop(i)
            land_hitbox.pop(i)

        if -10 in land_farm_i: land_farm_i.remove(-10)
        if -10 in land_farm_tended: land_farm_tended.remove(-10)
        render_land(land_x,land_y)
    def spawn_settler():
        x_m,y_m=pygame.mouse.get_pos()
        if pygame.key.get_pressed()[32]:
            last_name=[names.get_last_name(), names.get_last_name()]   
            settler.born(x_m,y_m,last_name)
    def spawn_cloud():
        x_m,y_m=pygame.mouse.get_pos()
        if pygame.key.get_pressed()[99]:
            cloud_x.append(x_m)
            cloud_y.append(y_m)
            cloud_storm.append(0)
            cloud_cap.append(20)
    def get_info():
         x_m,y_m=pygame.mouse.get_pos()
         info_vis=0
          
         for i in range(0,len(settler_x)):
              if cal_Dist(x_m,y_m,settler_x[i],settler_y[i])<10 and info_vis==0:
                   status_str=str(int(settler_status[i]))+' stars'
                   text = font.render(settler_name[i][0]+" "+settler_name[i][1][0]+"  Age: "+str(int(settler_age[i]*(15/YEAR)))+" Job: "+settler_job[i]+" Status: "+status_str, True, RED, BLACK)   
                   textRect = text.get_rect()
                   textRect.bottomleft = (x_m, y_m)
                   screen.blit(text, textRect)
                   info_vis=1
                   break
              

              

class settler:
    def next_move(settler_x,settler_y):
        global settler_dead
        global settler_baby_parent
        global church_stage
        global church_x
        global church_y
        global windmill_stage
        global windmill_x
        global windmill_y
        global animal_food
        global grain_food  
        
        for i in range(0,len(settler_x)):
            x_mod=0
            y_mod=0
            settler_sheltered[i]=0
            death_notifed=0
            if not check_land(settler_x[i],settler_y[i],1):#seek land
              
                x_dest=0
                y_dest=0
                dist_short=9999
                for j in range(0,len(land_x)):
                    dist=cal_Dist(settler_x[i],settler_y[i],land_x[j],land_y[j])
                    if dist<dist_short:
                        dist_short=dist
                        x_dest=land_x[j]
                        y_dest=land_y[j]
                  
                if settler_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1

            elif settler_hunger[i]>500 and (len(animal_dead_x)>0 or len(grain_x)>0 or len(animal_x)>2 or settler_inv_food[i]>0):#seek food
                food_x=animal_dead_x+grain_x
                food_y=animal_dead_y+grain_y
                food_amount=animal_food+grain_food

                if settler_inv_food[i]>0:
                    settler_hunger[i]=0
                    settler_inv_food[i]=settler_inv_food[i]-1

                elif len(food_x)>0:
                    dist_short=9999
                    for j in range(0,len(food_x)):
                        dist=cal_Dist(settler_x[i],settler_y[i],food_x[j],food_y[j])
                        if dist<dist_short:
                            dist_short=dist
                            x_dest=food_x[j]
                            y_dest=food_y[j]
                            food_short=j
                            

                     
                    if settler_x[i]-x_dest>0:
                        x_mod=mod
                    else:
                        x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                        y_mod=mod
                    else:
                        y_mod=mod*-1

                    if dist_short<3:
                        settler_inv_food[i]=settler_inv_food[i]+5
                        food_amount[food_short]=food_amount[food_short]-5
                        animal_food=food_amount[:len(animal_food)]
                        grain_food=food_amount[len(animal_food):]
                elif len(animal_x)>2 and settler_job[i]=='hunter':
                    dist_short=9999
                    for j in range(0,len(animal_x)):
                        dist=cal_Dist(settler_x[i],settler_y[i],animal_x[j],animal_y[j])
                        if dist<dist_short:
                            dist_short=dist
                            x_dest=animal_x[j]
                            y_dest=animal_y[j]
                            animal_short=j
                            

                     
                    if settler_x[i]-x_dest>0:
                        x_mod=mod
                    else:
                        x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                        y_mod=mod
                    else:
                        y_mod=mod*-1

                    if dist_short<3:
                        r_disease=random.random()
                        if r_disease<0.1:
                             settler_sick[i]=1
                             notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" caught a disease")
                             print(settler_name[i][0]+" "+settler_name[i][1][0]+" caught a disease")
                        animal.hunted(animal_short)
                        if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
                    
                    
            elif settler_home[i] and (temp<32 or settler_health[i]<50) and not settler_sheltered[i]: #seek shelter when cold
                i_h=-1
                for j in range(0,len(settler_home)):
                    if settler_home[j]:   
                        i_h=i_h+1
                        if j==i: break
                   
                x_dest=house_x[i_h]
                y_dest=house_y[i_h]
                

                 
                if settler_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1

                if cal_Dist(settler_x[i],settler_y[i],x_dest,y_dest)<3:
                    if settler_job[i]=='leader' and house_upgrade[i_h]==0:
                         house_upgrade[i_h]=1
                         print(house_upgrade)
                    if settler_job[i]=='leader' and settler_status[i] > 4 and house_upgrade[i_h]==2:
                         house_upgrade[i_h]=3
                    settler_sheltered[i]=1
                    if settler_hunger[i]<1000 and settler_health[i]<100:
                         if not settler_sick[i] and settler_age[i]<YEAR*10*0.5: settler_health[i]=settler_health[i]+1
                         else: settler_health[i]=settler_health[i]+.01 
                    x_mod=x_mod*3
                    y_mod=y_mod*3
  

            elif len(animal_x)>2 and settler_job[i]=='hunter' and len([k for k, e in enumerate(settler_hunger) if e > 500])>0 and len(animal_dead_x)<1: #seek to hunt when people are hungry
                    dist_short=9999
                    for j in range(0,len(animal_x)):
                        dist=cal_Dist(settler_x[i],settler_y[i],animal_x[j],animal_y[j])
                        if dist<dist_short:
                            dist_short=dist
                            x_dest=animal_x[j]
                            y_dest=animal_y[j]
                            animal_short=j
                            

                     
                    if settler_x[i]-x_dest>0:
                        x_mod=mod
                    else:
                        x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                        y_mod=mod
                    else:
                        y_mod=mod*-1

                    if dist_short<3:
                         r_disease=random.random()
                         if r_disease<0.1:
                             settler_sick[i]=1
                             notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" caught a disease")
                             print(settler_name[i][0]+" "+settler_name[i][1][0]+" caught a disease")
                         animal.hunted(animal_short)             
                         if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
    
            elif ((len(settler_x)+len(settler_baby_x)*0.25)>len(house_x) or (len([k for k, e in enumerate(house_upgrade) if e==1])>0 or len([k for k, e in enumerate(house_upgrade) if e==3])>0))and len(tree_x)>1 and settler_job[i]=='builder':#seek material for shelter

                 if settler_inv_wood[i]<5 and len(tree_x)>1:
                    dist_short=9999
                    for j in range(0,len(tree_x)):
                         dist=cal_Dist(settler_x[i],settler_y[i],tree_x[j],tree_y[j])
                         if dist<dist_short:
                             dist_short=dist
                             x_dest=tree_x[j]
                             y_dest=tree_y[j]
                             tree_short=j

                          
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if dist_short<3:
                         settler_inv_wood[i]=settler_inv_wood[i]+1
                         tree.chop(tree_short)

                 elif (len([k for k, e in enumerate(house_upgrade) if e==1])>0 or len([k for k, e in enumerate(house_upgrade) if e==3])>0) and settler_inv_wood[i]>=5: 
                      for j in range(0,len(house_upgrade)):
                           if house_upgrade[j]==1 or house_upgrade[j]==3 :
                                x_dest=house_x[j]
                                y_dest=house_y[j]
                                j_dest=j
                                break
                      if settler_x[i]-x_dest>0:
                           x_mod=mod
                      else:
                           x_mod=mod*-1

                      if settler_y[i]-y_dest>0:
                           y_mod=mod
                      else:
                           y_mod=mod*-1

                      if cal_Dist(settler_x[i],settler_y[i],x_dest,y_dest)<3:
                           settler_inv_wood[i]=settler_inv_wood[i]-5
                           if house_upgrade[j_dest]==1: house_upgrade[j_dest]=2
                           elif house_upgrade[j_dest]==3: house_upgrade[j_dest]=4
                           if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
                           
                                
            elif (avg_an_fert=='-' or avg_an_fert<85) and len(land_farm_i)<len(settler_x)/4 and settler_job[i]=='farmer': #seek to build farms
                dist_short=9999
                no_build=0

                for j in range(0,len(land_x)):
                    dist=cal_Dist(settler_x[i],settler_y[i],land_x[j],land_y[j])
                    if dist<dist_short and j not in land_farm_i and len(land_hitbox[j].collidelistall(land_hitbox))>5:
                        #for k in range(0,len(house_x)):
                        #     if land_hitbox[j].collidepoint(house_x[k], house_y[k]):
                        #          no_build=1
                        #          break
                        if not no_build:
                             dist_short=dist
                             x_dest=land_x[j]
                             y_dest=land_y[j]
                             land_j=j
                
                if dist_short!=9999:
                     if settler_x[i]-x_dest>0:
                          x_mod=mod
                     else:
                          x_mod=mod*-1

                     if settler_y[i]-y_dest>0:
                          y_mod=mod
                     else:
                          y_mod=mod*-1
                     if dist_short<3:
                          land_farm_stage[land_j]=1
                          land_farm_i.append(land_j)
                          land_farm_tended.append(1)
            elif 0 in land_farm_tended and settler_job[i]=='farmer': #seek to tend farms
                k=0
                dist_short=9999
                for j in land_farm_i:
                    dist=cal_Dist(settler_x[i],settler_y[i],land_x[j],land_y[j])
                    if dist<dist_short and not land_farm_tended[k] :
                        dist_short=dist
                        x_dest=land_x[j]
                        y_dest=land_y[j]
                        land_j=j
                        land_k=k
                    k=k+1
                if settler_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1
                if dist_short<3:
                     land_farm_tended[land_k]=1
                     if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
            elif any(k>4 for k in land_farm_stage) and settler_job[i]=='farmer': #seek to harvest farms
                dist_short=9999
                for j in land_farm_i:
                    dist=cal_Dist(settler_x[i],settler_y[i],land_x[j],land_y[j])
                    if dist<dist_short and land_farm_stage[j]>3.25 :
                        dist_short=dist
                        x_dest=land_x[j]
                        y_dest=land_y[j]
                        land_j=j
                if settler_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1
                if dist_short<3:
                     farm.harvested(land_j)
                     if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
            elif len(settler_dead_buried)>0 and not all(settler_dead_buried): #seek to burry the dead
                dist_short=9999
                for j in range(0,len(settler_dead_buried)):
                    if not settler_dead_buried[j]:
                        dist=cal_Dist(settler_x[i],settler_y[i],settler_dead_x[j],settler_dead_y[j])
                        if dist<dist_short:
                            dist_short=dist
                            x_dest=settler_dead_x[j]
                            y_dest=settler_dead_y[j]
                            dead_short=j

                     
                if settler_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1

                if dist_short<3:
                    settler_dead_buried[dead_short]=1


            elif len(house_x)>=len(settler_x) and settler_age[i]<YEAR*10*0.35 and settler_happiness[i]>50  and settler_health[i]>50 and settler_gender[i] and len(settler_x)>1 and len([k for k, e in enumerate(settler_gender) if e == 0])>len(settler_baby_parent)  : #seak mate
                dist_short=9999
                for j in range(0,len(settler_x)):
                    
                    dist=cal_Dist(settler_x[i],settler_y[i],settler_x[j],settler_y[j])
                    if dist<dist_short and not settler_gender[j] and j not in settler_baby_parent and settler_age[j]<YEAR*10*0.35 and settler_health[j]>50 and not any(item in settler_name[i][1] for item in settler_name[j][1]):
                         dist_short=dist
                         x_dest=settler_x[j]
                         y_dest=settler_y[j]
                         settler_short=j

                if dist_short<9999:    
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                if dist_short<3:
                    settler_baby_parent.append(settler_short)
                    if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
                    #print(settler_age[i]*(15/6300), settler_age[j]*(15/6300))
                    last_name=[settler_name[i][1][0], settler_name[settler_short][1][0]]
                    notification.append("The "+last_name[0]+" family has a new member")
                    print("The "+last_name[0]+" family has a new member")
                    print(settler_name[i][1][0]+"-"+settler_name[i][1][1]+" and "+settler_name[settler_short][1][0]+"-"+settler_name[settler_short][1][1])
                    settler_baby.born(x_dest,y_dest,last_name)
            elif (((len(land_farm_i)>len(windmill_stage)*5 and len(land_farm_i)>4) or len([k for k, e in enumerate(windmill_stage) if e < 2])>0)) and settler_job[i]=='builder':#seek to build windmill 
                 if settler_inv_wood[i]<5 and len(tree_x)>1:
                    dist_short=9999
                    for j in range(0,len(tree_x)):
                         dist=cal_Dist(settler_x[i],settler_y[i],tree_x[j],tree_y[j])
                         if dist<dist_short:
                             dist_short=dist
                             x_dest=tree_x[j]
                             y_dest=tree_y[j]
                             tree_short=j

                          
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if dist_short<3:
                         settler_inv_wood[i]=settler_inv_wood[i]+1
                         tree.chop(tree_short)


                 elif settler_inv_wood[i]>=5:
                      if len([k for k, e in enumerate(windmill_stage) if e < 2])==0 or len(windmill_stage)==0: windmill_stage.append(-1)
                     
                      for j in range(0,len(windmill_stage)):
                           if windmill_stage[j]==-1:
                                windmill_stage[j]=0
                                farm_x=[land_x[k] for k in land_farm_i]
                                farm_y=[land_y[k] for k in land_farm_i]
                                farm_coord=np.array(tuple(zip(farm_x,farm_y)))
                                cent_index=KMeans(n_clusters=len(windmill_stage), random_state=0).fit_predict(X=farm_coord, y=None, sample_weight=None)
                                print(cent_index)
                                cent=find_centroid([farm_x[p] for p in [k for k, e in enumerate(cent_index) if e == len(windmill_stage)-1]],[farm_y[p] for p in [k for k, e in enumerate(cent_index) if e == len(windmill_stage)-1]])
                                x_dest=cent[0]
                                y_dest=cent[1]
                           
                                windmill_x.append(x_dest)
                                windmill_y.append(y_dest)
                                j_dest=j
                                
             

                           elif windmill_stage[j]>=0 and windmill_stage[j]<2:
                                x_dest=windmill_x[j]
                                y_dest=windmill_y[j]
                                j_dest=j
          

                           
                      if settler_x[i]-x_dest>0:
                           x_mod=mod
                      else:
                           x_mod=mod*-1

                      if settler_y[i]-y_dest>0:
                           y_mod=mod
                      else:
                           y_mod=mod*-1

                      if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                           settler_inv_wood[i]=settler_inv_wood[i]-5
                           windmill_stage[j_dest]+=.5
                           if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
                 
            elif (((len(house_x)>len(tavern_stage)*20 and len(house_x)>5) or len([k for k, e in enumerate(tavern_stage) if e < 1])>0)) and settler_job[i]=='builder':#seek to build tavern 
                 if settler_inv_wood[i]<5 and len(tree_x)>1:
                    dist_short=9999
                    for j in range(0,len(tree_x)):
                         dist=cal_Dist(settler_x[i],settler_y[i],tree_x[j],tree_y[j])
                         if dist<dist_short:
                             dist_short=dist
                             x_dest=tree_x[j]
                             y_dest=tree_y[j]
                             tree_short=j

                          
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if dist_short<3:
                         settler_inv_wood[i]=settler_inv_wood[i]+1
                         tree.chop(tree_short)


                 elif settler_inv_wood[i]>=5:
                      if len([k for k, e in enumerate(tavern_stage) if e < 1])==0 or len(tavern_stage)==0: tavern_stage.append(-1)
                     
                      for j in range(0,len(tavern_stage)):
                           if tavern_stage[j]==-1:
                                tavern_stage[j]=0
                                house_coord=np.array(tuple(zip(house_x,house_y)))
                                cent_index=KMeans(n_clusters=len(tavern_stage), random_state=0).fit_predict(X=house_coord, y=None, sample_weight=None)
                                print(cent_index)
                                cent=find_centroid([house_x[p] for p in [k for k, e in enumerate(cent_index) if e == len(tavern_stage)-1]],[house_y[p] for p in [k for k, e in enumerate(cent_index) if e == len(tavern_stage)-1]])
                                x_dest=cent[0]
                                y_dest=cent[1]
                           
                                tavern_x.append(x_dest)
                                tavern_y.append(y_dest)
                                j_dest=j
                                
             

                           elif tavern_stage[j]>=0 and tavern_stage[j]<1:
                                x_dest=tavern_x[j]
                                y_dest=tavern_y[j]
                                j_dest=j
          

                           
                      if settler_x[i]-x_dest>0:
                           x_mod=mod
                      else:
                           x_mod=mod*-1

                      if settler_y[i]-y_dest>0:
                           y_mod=mod
                      else:
                           y_mod=mod*-1

                      if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                           settler_inv_wood[i]=settler_inv_wood[i]-5
                           tavern_stage[j_dest]+=.25
                           if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
            elif church_stage<2 and len(house_x)>25 and settler_job[i]=='builder': #seek to build church
                 if settler_inv_wood[i]<5 and len(tree_x)>1:
                    dist_short=9999
                    for j in range(0,len(tree_x)):
                         dist=cal_Dist(settler_x[i],settler_y[i],tree_x[j],tree_y[j])
                         if dist<dist_short:
                             dist_short=dist
                             x_dest=tree_x[j]
                             y_dest=tree_y[j]
                             tree_short=j

                          
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if dist_short<3:
                         settler_inv_wood[i]=settler_inv_wood[i]+1
                         tree.chop(tree_short)
                 elif church_stage==0 and settler_inv_wood[i]>=5:
                    cent=find_centroid(house_x,house_y)
                    x_dest=cent[0]
                    y_dest=cent[1]
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                        church_x=x_dest
                        church_y=y_dest
                        settler_inv_wood[i]=settler_inv_wood[i]-5
                        church_stage=.1
                 elif church_stage>0 and church_stage<2 and settler_inv_wood[i]>=5:
                    x_dest=church_x
                    y_dest=church_y
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                        church_stage=church_stage+.1
                        settler_inv_wood[i]=settler_inv_wood[i]-5
                        if settler_status[i]<5: settler_status[i]=settler_status[i]+.1

   
            elif sum(tavern_stage)>=1 and settler_happiness[i]<100 and settler_morality[i]<75: #seek tavern when sad
                 dist_short=9999
                 for j in range(0,len(tavern_x)):
                      dist=cal_Dist(settler_x[i],settler_y[i],tavern_x[j],tavern_y[j])
                      if dist<dist_short and tavern_stage[j]>.9:
                           dist_short=dist
                           x_dest=tavern_x[j]
                           y_dest=tavern_y[j]
                           tavern_short=j   



                 if settler_x[i]-x_dest>0:
                     x_mod=mod
                 else:
                     x_mod=mod*-1

                 if settler_y[i]-y_dest>0:
                     y_mod=mod
                 else:
                     y_mod=mod*-1

                 if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                     settler_sheltered[i]=1
                     x_mod=x_mod*3
                     y_mod=y_mod*3
                     if settler_happiness[i]<100 and settler_drunk[i]<(100-settler_morality[i]):
                         settler_happiness[i]=settler_happiness[i]+0.1
                         settler_drunk[i]=settler_drunk[i]+0.1
   
            
   
            elif church_stage>=2 and settler_happiness[i]<100 and settler_morality[i]>25: #seek church when sad
                 x_dest=church_x
                 y_dest=church_y
                 if settler_x[i]-x_dest>0:
                     x_mod=mod
                 else:
                     x_mod=mod*-1

                 if settler_y[i]-y_dest>0:
                     y_mod=mod
                 else:
                     y_mod=mod*-1

                 if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                     settler_sheltered[i]=1
                     x_mod=x_mod*3
                     y_mod=y_mod*3
                     if settler_happiness[i]<100:
                         settler_happiness[i]=settler_happiness[i]+0.1
            elif len(settler_x)>1 and t%10==0: #seek to socialize when bored
                 dist_short=9999
                 for j in range(0,len(settler_x)):
                     dist=cal_Dist(settler_x[i],settler_y[i],settler_x[j],settler_y[j])
                     if dist<dist_short and j!=i and len([k for k, e in enumerate(settler_social[i]) if e == j])<10:
                          dist_short=dist
                          x_dest=settler_x[j]
                          y_dest=settler_y[j]
                          settler_short=j

                 if dist_short<9999:    
                     if settler_x[i]-x_dest>0:
                          x_mod=mod
                     else:
                          x_mod=mod*-1

                     if settler_y[i]-y_dest>0:
                          y_mod=mod
                     else:
                          y_mod=mod*-1

                 if dist_short<7:
                     if settler_happiness[i]<100: settler_happiness[i]=settler_happiness[i]+0.5
                     settler_social[i].append(settler_short)
                     if len(settler_social[i])>(len(settler_x)-2)*10: settler_social[i]=[]
                     r_social_action=random.random()
                     r_disease=random.random()
                     if settler_sick[i] and r_disease<0.5 and not settler_sick[j]:
                          settler_sick[j]=1
                          notification.append(settler_name[j][0]+" "+settler_name[j][1][0]+" caught a disease from "+settler_name[i][0]+" "+settler_name[i][1][0])
                          print(settler_name[j][0]+" "+settler_name[j][1][0]+" caught a disease from "+settler_name[i][0]+" "+settler_name[i][1][0])
                     elif settler_sick[j] and r_disease<0.5 and not settler_sick[i]:
                          settler_sick[i]=1
                          notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" caught a disease from "+settler_name[j][0]+" "+settler_name[j][1][0])
                          print(settler_name[i][0]+" "+settler_name[i][1][0]+" caught a disease from "+settler_name[j][0]+" "+settler_name[j][1][0])     
                     if settler_inv_food[i]>1 and settler_morality[i]>65 and settler_inv_food[i]>settler_inv_food[settler_short] and r_social_action>0.5:
                          settler_inv_food[i]=settler_inv_food[i]-1
                          settler_inv_food[settler_short]=settler_inv_food[settler_short]+1
                          if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
                          if settler_happiness[i]+5<100: settler_happiness[i]=settler_happiness[i]+5
                          else: settler_happiness[i]=100
                          if settler_happiness[i]+10<100: settler_happiness[settler_short]=settler_happiness[settler_short]+10
                          else: settler_happiness[settler_short]=100
                          #notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" just gave food to "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0])
                          print(settler_name[i][0]+" "+settler_name[i][1][0]+"(Morality:"+str(settler_morality[i])+") "+"just gave food to "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0])
                     if settler_morality[i]<35 and settler_inv_food[settler_short]>0 and r_social_action>0.5:
                          settler_inv_food[i]=settler_inv_food[i]+1
                          settler_inv_food[settler_short]=settler_inv_food[settler_short]-1
                          if settler_happiness[i]+5<100: settler_happiness[i]=settler_happiness[i]+5
                          else: settler_happiness[i]=100
                          if settler_happiness[i]-10>0: settler_happiness[settler_short]=settler_happiness[settler_short]-10
                          else: settler_happiness[settler_short]=0
                          #notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" stole food from "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0])
                          print(settler_name[i][0]+" "+settler_name[i][1][0]+"(Morality:"+str(settler_morality[i])+") "+"stole food from "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0])
                          r_caught=random.random()
                          if r_caught<0.2:
                               r_die=random.random()
                               if settler_health[i]>100*r_die:
                                    settler_health[i]=settler_health[i]-int(100*r_die)
                                    settler_happiness[i]=0
                                    if settler_status[i]>0: settler_status[i]=settler_status[i]-.1
                                    notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" took "+str(int(100*r_die))+" damage from "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0]+" for stealing")
                                    print(settler_name[i][0]+" "+settler_name[i][1][0]+" took "+str(int(100*r_die))+" damage from "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0]+" for stealing")
                                    settler_inv_food[i]=settler_inv_food[i]-1
                                    settler_inv_food[settler_short]=settler_inv_food[settler_short]+1
                               else:
                                    settler_health[i]=0
                                    notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" was killed by "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0]+" for stealing")
                                    print(settler_name[i][0]+" "+settler_name[i][1][0]+" was killed by "+settler_name[settler_short][0]+" "+settler_name[settler_short][1][0]+" for stealing")
                                    death_notifed=1
                                    settler_inv_food[settler_short]=settler_inv_food[settler_short]+settler_inv_food[i]
            x_r=random.random()         
            y_r=random.random()
            if settler_drunk[i]>50:
                 x_mod=0
                 y_mod=0
            if x_r+x_mod<0.5:
                settler_x[i]=settler_x[i]+1
            else:
                settler_x[i]=settler_x[i]-1

            if y_r+y_mod<0.5:
                settler_y[i]=settler_y[i]+1
            else:
                settler_y[i]=settler_y[i]-1

          
            settler.build(i)
            settler_age[i]=settler_age[i]+1
            if settler_drunk[i]>0: settler_drunk[i]-=0.05
            if temp<32 and not settler_sheltered[i]:
                 settler_health[i]=settler_health[i]-0.1
                 if settler_health[i]<1 and not death_notifed:
                      notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" froze to death")
                      print(settler_name[i][0]+" "+settler_name[i][1][0]+" froze to death")
                      death_notifed=1
            if settler_hunger[i]>1000:
                 settler_health[i]=settler_health[i]-0.1
                 if settler_health[i]<1 and not death_notifed:
                      notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" starved to death")
                      print(settler_name[i][0]+" "+settler_name[i][1][0]+" starved to death")
                      death_notifed=1
            if settler_age[i]>YEAR*10*0.5:
                 settler_health[i]=settler_health[i]-0.1*random.randint(0,1)
                 if settler_health[i]<1 and not death_notifed:
                      notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" died of old age")
                      print(settler_name[i][0]+" "+settler_name[i][1][0]+" died of old age")
                      death_notifed=1
            if settler_sick[i]:
                 settler_health[i]=settler_health[i]-0.1*random.randint(0,1)
                 if settler_health[i]<1 and not death_notifed:
                      notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" died from disease")
                      print(settler_name[i][0]+" "+settler_name[i][1][0]+" died from disease")
                      death_notifed=1
            if settler_age[i]>YEAR*10*0.35 and settler_job[i]!='leader': settler_job[i]='retired'
            if settler_health[i]<1:
                settler_dead_x.append(settler_x[i])
                settler_dead_y.append(settler_y[i])
                for j in range(0,len(settler_baby_parent)):
                    if settler_baby_parent[j]==i: settler_baby_parent[j]=-10
                    if settler_baby_parent[j]>i and settler_baby_parent[j]!=-10: settler_baby_parent[j]=settler_baby_parent[j]-1
                settler_dead.append(i)
            settler_hunger[i]=settler_hunger[i]+1
          
        for i in sorted(settler_dead, reverse=True):
            settler.die(i)
           
        settler_dead=[]
        render_settler_dead(settler_dead_x,settler_dead_y)
        render_settler(settler_x,settler_y)

    def build(i):

        if settler_inv_wood[i]>=5 and settler_job[i]=='builder' and (len(settler_x)+len(settler_baby_x)*0.25)>len(house_x):
            no_build=0   
            for j in range(0,len(house_x)):
                 if cal_Dist(settler_x[i],settler_y[i],house_x[j],house_y[j])<10:
                      no_build=1
                      break
            for j in land_farm_i:
                    if land_hitbox[j].collidepoint(settler_x[i],settler_y[i]):
                      no_build=1
                      break
            if church_x!=0 and cal_Dist(settler_x[i],settler_y[i],church_x,church_y)<15: no_build=1         
            if not no_build:       
                 for j in range(0,len(settler_home)):
                      if not settler_home[j]:
                                settler_home[j]=1
                                break
                      
                 house_x.append(settler_x[i])
                 house_y.append(settler_y[i])
                 house_upgrade.append(0)
                 if settler_status[i]<5: settler_status[i]=settler_status[i]+.1
                 settler_inv_wood[i]=settler_inv_wood[i]-5
   
    def die(i):
        settler_dead_buried.append(0)
        settler_dead_gender.append(settler_gender[i])
        settler_x.pop(i)
        settler_y.pop(i)
        settler_home.pop(i)
        settler_inv_wood.pop(i)
        settler_inv_food.pop(i)
        settler_hunger.pop(i)
        settler_health.pop(i)
        settler_sheltered.pop(i)
        settler_social.pop(i)
        settler_happiness.pop(i)
        settler_gender.pop(i)
        settler_job.pop(i)
        settler_age.pop(i)
        settler_name.pop(i)
        settler_morality.pop(i)
        settler_sick.pop(i)
        settler_drunk.pop(i)
        settler_status.pop(i)
        for j in range(0,len(settler_x)):
            if settler_happiness[j]>5:
                settler_happiness[j]=settler_happiness[j]-5
            else: settler_happiness[j]=0 
    def born(x,y,last_name):
         settler_x.append(x)
         settler_y.append(y)
         if sum(settler_home)<len(house_x):
              settler_home.append(1)

         else: settler_home.append(0)
         settler_inv_wood.append(0)
         settler_inv_food.append(0)
         settler_hunger.append(0)
         settler_health.append(100)
         settler_sheltered.append(0)
         settler_social.append([])
         settler_sick.append(0)
         settler_drunk.append(0)
         settler_status.append(2.5)
         if avg_happiness!='-': settler_happiness.append(avg_happiness)
         else: settler_happiness.append(100)
         settler_age.append(YEAR)
         r=random.random()
         r_job=random.randint(0,2)
         r_moral=random.gauss(50,15)
         settler_morality.append(r_moral)
         if r>.5:
             settler_gender.append(0)
             first_name=names.get_first_name(gender='female')
         else:
             settler_gender.append(1)
             first_name=names.get_first_name(gender='male')
         settler_name.append([first_name, last_name])
         if r_job==0: settler_job.append('farmer')
         elif r_job==1: settler_job.append('hunter')
         elif r_job==2: settler_job.append('builder')
         #print(settler_job)

    def elect_leader():
         if int(avg_happiness)>75 and len([k for k, e in enumerate(settler_job) if e =='leader'])>0:
              i=settler_job.index('leader')
              if settler_status[i]+0.5<5: settler_status[i]=settler_status[i]+0.5
              else: settler_status[i]=5 
              if settler_morality[i]<25: moral_str='Evil'
              elif settler_morality[i]>=25 and settler_morality[i]<35: moral_str='Immoral'
              elif settler_morality[i]>=35 and settler_morality[i]<65: moral_str='Neutral'
              elif settler_morality[i]>=65 and settler_morality[i]<75: moral_str='Moral'
              else: moral_str='Good'
              notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" maintained their leadership of the settlement  Disposition: "+moral_str)
              print(settler_name[i][0]+" "+settler_name[i][1][0]+" maintained their leadership of the settlement  Disposition: "+moral_str)

         else:
              if len([k for k, e in enumerate(settler_job) if e =='leader'])>0: settler_job[settler_job.index('leader')]='ex-leader'
              i=settler_status.index(max(settler_status))
              settler_job[i]='leader'
              if settler_morality[i]<25: moral_str='Evil'
              elif settler_morality[i]>=25 and settler_morality[i]<35: moral_str='Immoral'
              elif settler_morality[i]>=35 and settler_morality[i]<65: moral_str='Neutral'
              elif settler_morality[i]>=65 and settler_morality[i]<75: moral_str='Moral'
              else: moral_str='Good'
              notification.append(settler_name[i][0]+" "+settler_name[i][1][0]+" became the leader of the settlement  Disposition: "+moral_str)
              print(settler_name[i][0]+" "+settler_name[i][1][0]+" became the leader of the settlement  Disposition: "+moral_str)
class tree:
    def grow(tree_x,tree_y):
        if len(tree_x)<int(len(land_x)*fertility) and len(land_x)>100:
            ran=random.random()
            i_ran=int(len(land_x)*ran)
            if len(land_hitbox[i_ran].collidelistall(land_hitbox))>5:
                 tree_x.append(land_x[i_ran])
                 tree_y.append(land_y[i_ran])
        for i in range(0,len(tree_x)):
            if not check_land(tree_x[i],tree_y[i],0):
                tree_x[i]=-10
                tree_y[i]=-10
        if -10 in tree_x: tree_x.remove(-10)
        if -10 in tree_y: tree_y.remove(-10)
        
        render_tree(tree_x,tree_y)

    def chop(i):
        global fertility
        if fertility>0.01:new_fertility=fertility-0.01
        else: new_fertility=0

        fertility=new_fertility
        tree_x.pop(i)
        tree_y.pop(i)


class house:
    def built(house_x,house_y):
        i_house=[]
        for i in range(0,len(house_x)):
            
            if not check_land(house_x[i],house_y[i],0):
                house_x[i]=-10
                house_y[i]=-10
                house_upgrade[i]=-10    
                i_house.append(i)
        i_h=0
        for i in range(0,len(settler_home)):
            if settler_home[i]:
                if i_h in i_house:
                    settler_home[i]=0
                i_h=i_h+1
        if -10 in house_x: house_x.remove(-10)
        if -10 in house_y: house_y.remove(-10)
        if -10 in house_y: house_upgrade.remove(-10)
        buildings_y=house_y
        if church_stage>0:
            buildings_y=buildings_y+[church_y]    
        buildings_y=buildings_y+windmill_y+tavern_y
        render_order=sorted(range(len(buildings_y)), key=lambda k: buildings_y[k])
        render_buildings(house_x,house_y,render_order,church_x,church_y,windmill_x,windmill_y)
    

class animal:
    def next_move(animal_x,animal_y):
        num_fertile=sum(1 for i in animal_fertility if i>50)
        for i in range(0,len(animal_x)):
            x_mod=0
            y_mod=0
            ran=random.random()

            M=(len(land_x))*0.1
            if M==0: M=0.1
            P_t=len(animal_x)
            r=0.1
            P_t=P_t+r*P_t*(1-P_t/M)
            if P_t<0: P_t=0
            dist_short_settler=9999
            for j in range(0,len(settler_x)):
                    dist=cal_Dist(animal_x[i],animal_y[i],settler_x[j],settler_y[j])
                    if dist<dist_short_settler:
                        dist_short_settler=dist
                        x_away=settler_x[j]
                        y_away=settler_y[j]
                        
            
            if not check_land(animal_x[i],animal_y[i],0):#seek land 
                x_dest=0
                y_dest=0
                dist_short=9999
                for j in range(0,len(land_x)):
                    dist=cal_Dist(animal_x[i],animal_y[i],land_x[j],land_y[j])
                    if dist<dist_short:
                        dist_short=dist
                        x_dest=land_x[j]
                        y_dest=land_y[j]
                  
                if animal_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if animal_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1


            elif dist_short_settler<10: #avoid settler
                if animal_x[i]-x_away<0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if animal_y[i]-y_away<0:
                    y_mod=mod
                else:
                    y_mod=mod*-1
                
      
            elif len(animal_x)<P_t and len(animal_x)>1 and animal_fertility[i]>50 and num_fertile>1: #seek mate
                dist_short=9999
                for j in range(0,len(animal_x)):
                    dist=cal_Dist(animal_x[i],animal_y[i],animal_x[j],animal_y[j])
                    if dist<dist_short and i!=j and animal_fertility[j]>50:
                        dist_short=dist
                        x_dest=animal_x[j]
                        y_dest=animal_y[j]
                        animal_short=j
                  
                if animal_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if animal_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1

                if dist_short<3:

                    
                    animal.breed(animal_short)



            
            x_r=random.random()
            y_r=random.random() 
            if x_r+x_mod<0.5:
                animal_x[i]=animal_x[i]+1
            else:
                animal_x[i]=animal_x[i]-1

            if y_r+y_mod<0.5:
                animal_y[i]=animal_y[i]+1
            else:
                animal_y[i]=animal_y[i]-1

            if animal_fertility[i]<100: animal_fertility[i]=animal_fertility[i]+0.025

        render_animal(animal_x,animal_y)
        for i in range(0,len(animal_food)):
            if animal_food[i]<1 or not check_land(animal_dead_x[i],animal_dead_y[i],0):
                animal_dead_x.pop(i)
                animal_dead_y.pop(i)
                animal_food.pop(i)
        render_meat(animal_dead_x,animal_dead_y)
        

    def breed(i):
        r=random.random()
        if r<0.5:
            if animal_fertility[i]>=50:animal_fertility[i]=animal_fertility[i]-50
            else: animal_fertility[i]=0
            animal_x.append(animal_x[i])
            animal_y.append(animal_y[i])
            animal_fertility.append(0)
    def hunted(i):
        animal_dead_x.append(animal_x[i])
        animal_dead_y.append(animal_y[i])
        animal_x.pop(i)
        animal_y.pop(i)
        animal_fertility.pop(i)
        animal_food.append(15)
        


class settler_baby:
    def next_move(settler_baby_x,settler_baby_y):
        global settler_baby_grown
        for i in range(0,len(settler_baby_x)):
            x_mod=0
            y_mod=0
            
            if not check_land(settler_baby_x[i],settler_baby_y[i],0):#seek land
              
                x_dest=0
                y_dest=0
                dist_short=9999
                for j in range(0,len(land_x)):
                    dist=cal_Dist(settler_baby_x[i],settler_baby_y[i],land_x[j],land_y[j])
                    if dist<dist_short:
                        dist_short=dist
                        x_dest=land_x[j]
                        y_dest=land_y[j]
                  
                if settler_baby_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_baby_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1

            elif len(settler_x)>0:

                if settler_baby_parent[i]==-10:
                    settler_baby_parent[i]=int(random.random()*(len(settler_x)))
     
                if settler_baby_parent[i] in range(0,len(settler_x)):
                     x_dest=settler_x[settler_baby_parent[i]]
                     y_dest=settler_y[settler_baby_parent[i]]

                else:
                    settler_baby_grown.append(i)
                    x_dest=0
                    y_dest=0

                if settler_baby_x[i]-x_dest>0:
                    x_mod=mod
                else:
                    x_mod=mod*-1

                if settler_baby_y[i]-y_dest>0:
                    y_mod=mod
                else:
                    y_mod=mod*-1

            else: settler_baby_grown.append(i)
            
            x_r=random.random()
            y_r=random.random() 
            if x_r+x_mod<0.5:
                settler_baby_x[i]=settler_baby_x[i]+1
            else:
                settler_baby_x[i]=settler_baby_x[i]-1

            if y_r+y_mod<0.5:
                settler_baby_y[i]=settler_baby_y[i]+1
            else:
                settler_baby_y[i]=settler_baby_y[i]-1

            settler_baby_age[i]=settler_baby_age[i]+1
            if settler_baby_parent[i] in range(0, len(settler_health))  and settler_health[settler_baby_parent[i]]<50:
                 r_neglect=random.random()
                 if r_neglect<0.2:
                      for j in range(0,len(settler_x)):
                           if settler_happiness[j]>5:
                                settler_happiness[j]=settler_happiness[j]-5      
                           else: settler_happiness[j]=0
                           if j==settler_baby_parent[i]: settler_happiness[j]=0
                      settler_baby_grown.append(i)
                      notification.append("The "+settler_baby_name[i][0]+" family has lost a child")
                      print("The "+settler_baby_name[i][0]+" family has lost a child")
                      
            if settler_baby_age[i]>YEAR:
                settler.born(settler_baby_x[i],settler_baby_y[i],settler_baby_name[i])
                settler_baby_grown.append(i)

        for i in sorted(settler_baby_grown, reverse=True):
            settler_baby_x.pop(i)
            settler_baby_y.pop(i)
            settler_baby_age.pop(i)
            settler_baby_parent.pop(i)
            settler_baby_name.pop(i)
        settler_baby_grown=[]
        render_settler_baby(settler_baby_x,settler_baby_y)
    def born(x,y,last_name):
        settler_baby_x.append(x)
        settler_baby_y.append(y)
        settler_baby_age.append(0)
        settler_baby_name.append(last_name)

class farm:
    def grow(land_farm_stage):
        j=0
        for i in land_farm_i:
            if temp>32 and land_farm_tended[j]:
                land_farm_stage[i]=land_farm_stage[i]+temp*0.000013
        
            elif temp<32:
                land_farm_stage[i]=1
                land_farm_tended[j]=0
            if abs(land_farm_stage[i]-2)<0.001 or abs(land_farm_stage[i]-3)<0.001: land_farm_tended[j]=0
            j=j+1

        grain_gone=[]      
        for i in range(0,len(grain_food)):
            if grain_food[i]<1 or not check_land(grain_x[i],grain_y[i],0):
                grain_gone.append(i)
                
        for i in sorted(grain_gone, reverse=True):
            grain_x.pop(i)
            grain_y.pop(i)
            grain_food.pop(i)
        render_grain(grain_x,grain_y)
    def harvested(i):
        land_farm_stage[i]=1
        grain_x.append(land_x[i])
        grain_y.append(land_y[i])
        wm_mult=sum(windmill_stage)*5
        grain_food.append(20+wm_mult)


class cloud:
    def move(cloud_x,cloud_y):
        del_cloud=[]
        
        if len(cloud_x)>0: cent=find_centroid(cloud_x,cloud_y)
        for i in range(0,len(cloud_x)):
            if t%2==1: cloud_x[i]=cloud_x[i]-1
            if len(cloud_x)>200 and cal_Dist(cloud_x[i],cloud_y[i],cent[0],cent[1])<200:
                cloud_storm[i]=1
            #else: cloud_storm[i]=0        
            if cloud_x[i]<0:
                del_cloud.append(i)

            if cloud_storm[i] and random.random()<0.05:
                rain_x.append(cloud_x[i]+random.randint(-15,15))
                rain_y.append(cloud_y[i])
                rain_fall.append(0)
                cloud_cap[i]=cloud_cap[i]-1
            if cloud_cap[i]<1: cloud_storm[i]=0
        for i in sorted(del_cloud, reverse=True):
            cloud_x.pop(i)
            cloud_y.pop(i)
            cloud_storm.pop(i)
            cloud_cap.pop(i)
        render_cloud(cloud_x,cloud_y)
    def rain(rain_x,rain_y):
        del_rain=[]
        for i in range(0,len(rain_x)):
            rain_y[i]=rain_y[i]+3
            rain_fall[i]=rain_fall[i]+1
            if temp>32:
                for j in land_farm_i:
                    if land_hitbox[j].collidepoint(rain_x[i],rain_y[i]):
                        land_farm_stage[j]=land_farm_stage[j]+0.0001
                    

            if rain_fall[i]>35: del_rain.append(i)
        for i in sorted(del_rain, reverse=True):
            rain_x.pop(i)
            rain_y.pop(i)
            rain_fall.pop(i)
        render_rain(rain_x,rain_y)

class boat:
     
     def next_move(boat_x,boat_y):
          global boat_otw
          global t_boat
          t_boat+=1
          if t_boat>YEAR/2 and boat_otw:
               boat_otw=0

          for i in range(0,len(boat_x)):
            x_mod=0
            y_mod=0
            
            if not check_land(boat_x[i],boat_y[i],0) and i not in boat_landed:#seek land
              
                x_dest=0
                y_dest=0
                dist_short=9999
                for j in range(0,len(land_x)):
                    dist=cal_Dist(boat_x[i],boat_y[i],land_x[j],land_y[j])
                    if dist<dist_short:
                        dist_short=dist
                        x_dest=land_x[j]
                        y_dest=land_y[j]
                  
                if boat_x[i]-x_dest>0:
                    x_mod=1
                else:
                    x_mod=-1

                if boat_y[i]-y_dest>0:
                    y_mod=1
                else:
                    y_mod=-1

            if check_land(boat_x[i],boat_y[i],0) and i not in boat_landed:
                boat.landed(boat_x[i],boat_y[i])
                boat_landed.append(i)
                 
            if  x_mod<0.5:
                boat_x[i]=boat_x[i]+1
            else:
                boat_x[i]=boat_x[i]-1

            if  y_mod<0.5:
                boat_y[i]=boat_y[i]+1
            else:
                boat_y[i]=boat_y[i]-1
          render_boat(boat_x,boat_y)
          
               
     def landed(x,y):
          r_landed=random.randint(4,8)
          for i in range(0,r_landed):
               last_name=[names.get_last_name(), names.get_last_name()]   
               settler.born(x,y,last_name)

          
     def arrive():
          global boat_otw
          global t_boat
          if (len(house_x)-len(settler_x)-len(settler_baby_x)*0.25>5 or (len(settler_x)==0 and len(tree_x)>15)) and not boat_otw:
               arrive_y=int(random.random()*size[1])
               arrive_x=int(size[0]+20)
               boat_x.append(arrive_x)
               boat_y.append(arrive_y)
               boat_otw=1
               t_boat=0
               




for i in range(0,10000):
     x_r=int(random.gauss(size[0]/2,50))
     y_r=int(random.gauss(size[1]/2,50))
     rect_r=pygame.Rect(x_r-r_l,y_r-r_l,2*r_l,2*r_l)
     if not check_land(x_r,y_r,0) and (len(rect_r.collidelistall(land_hitbox))>=2 or len(land_hitbox)<10) :
            land_x.append(x_r)
            land_y.append(y_r)
            land_tread.append(0)
            land_hitbox.append(pygame.Rect(x_r-r_l,y_r-r_l,2*r_l,2*r_l))
            land_farm_stage.append(0)
            land_snow.append(0)


          
temp=int(50+50*math.sin(t))+random.randint(-5,5)        
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(50)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(BLUE)
    
    if t%101==100:
        temp=int(50+50*math.sin(t/1000))+random.randint(-5,5)



    player.draw_land(land_x,land_y)
    player.spawn_settler()
    player.spawn_cloud()
    r_cloud=random.random()
    if r_cloud<0.0015 and not cloud_spawner_bool:
         t_cloud=0
         cloud_spawner_bool=1
         y_cloud_spawn_loc=random.random()*size[1]

    if cloud_spawner_bool:
         y_cloud_loc=int(random.gauss(y_cloud_spawn_loc,25))
         cloud_x.append(size[0])
         cloud_y.append(y_cloud_loc)
         cloud_storm.append(0)
         cloud_cap.append(20)
         t_cloud+=1

    if t_cloud>int(YEAR/(15+random.randint(-5,5))): cloud_spawner_bool=0    
         
         
    settler.next_move(settler_x,settler_y)
    settler_baby.next_move(settler_baby_x,settler_baby_y)
    boat.arrive()
    boat.next_move(boat_x,boat_y)
    animal.next_move(animal_x,animal_y)
    farm.grow(land_farm_stage)
    tree.grow(tree_x,tree_y)
    house.built(house_x,house_y)
    cloud.rain(rain_x,rain_y)
    cloud.move(cloud_x,cloud_y)
    player.get_info()    
    res = []
    [res.append(x) for x in notification if x not in res]
    notification=res
    
    if t%5==0:
         notif_text=notif_text+'  '
         space_text=space_text+'  '
    len_old=len(notification)
    
    if len(notification)>0:

         for i in notification:
               if font.size(space_text)[0]>font.size("   "+i+"   ")[0]:
                    notif_text=notif_text[:(len(notif_text)-len("   "+i+"   "))]+"   "+i+"   " 
                    notification.remove(i)
                    space_text=''
               else: break

    if font.size(notif_text)[0]>(size[0]+300):
         notif_text=notif_text[1:]     
    text = font.render(notif_text, True, RED, BLACK)
    
    textRect = text.get_rect()

    textRect.topright = (size[0]+200, 0)
    t_n_r+=1
    screen.blit(text, textRect)
    
    if t%YEAR==0:
         if year_count!=0 and len(settler_status)>0: settler.elect_leader()
         year_count+=1
         
    
    if fertility<0.5: fertility=fertility+0.0001
    
    pop=len(settler_x)
    pop_ch=len(settler_baby_x)
    homes=len(house_x)
    if len(settler_health)==0: avg_health='-'
    else: avg_health=int(sum(settler_health)/len(settler_health))

    if len(settler_happiness)==0: avg_happiness='-'
    else: avg_happiness=int(sum(settler_happiness)/len(settler_happiness))
 
    if len(settler_age)==0: avg_age='-'
    else: avg_age=int((sum(settler_age)+sum(settler_baby_age))/(len(settler_age)+len(settler_baby_age))*(15/YEAR))
    if len(animal_fertility)==0: avg_an_fert='-'
    else: avg_an_fert=int(sum(animal_fertility)/len(animal_fertility))
    pygame.display.set_caption("Pop/homes: "+str(pop)+"("+str(pop_ch)+")"+" / "+str(homes)+" | Temp: "+str(temp)+"°F | Avg Age: "+str(avg_age)+" | Avg Health: "+str(avg_health)+"%"+" | Avg Happiness: "+str(avg_happiness)+" | Year: "+str(year_count))
    pygame.display.flip()
     
    t=t+1
pygame.quit()
