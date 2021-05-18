import pygame
import random
import math
import os
import winsound
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [720, 480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("YOU ARE GOD!")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

t=0


land_x=[]
land_y=[]
land_hitbox=[]
land_farm_stage=[]
land_farm_i=[]
land_farm_tended=[]
land_snow=[]
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
settler_happiness=[]
settler_gender=[]
settler_job=[]
settler_age=[]
settler_social=[]
tree_x=[]
tree_y=[]
house_x=[]
house_y=[]
church_stage=0
church_x=0
church_y=0
church_rendered=0
windmill_stage=0
windmill_x=0
windmill_y=0
animal_x=[20, 21]
animal_y=[20, 21]
animal_fertility=[100, 100]
animal_dead_x=[]
animal_dead_y=[]
animal_food=[]
cloud_x=[]
cloud_y=[]
cloud_storm=[]
cloud_cap=[]
rain_x=[]
rain_y=[]
rain_fall=[]


r_l=10
mod=0.3
fertility=0.5

spawned=0

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path
sound_path = os.path.join(resource_path, 'sounds')

background_music=(os.path.join(sound_path, 'background.wav'))

winsound.PlaySound(background_music, winsound.SND_LOOP + winsound.SND_ASYNC)

image_settler = pygame.image.load(os.path.join(image_path, 'settler.png')).convert_alpha()
image_settler_f = pygame.image.load(os.path.join(image_path, 'settler_f.png')).convert_alpha()
image_settler_dead = pygame.image.load(os.path.join(image_path, 'settler_dead.png')).convert_alpha()
image_settler_dead_f = pygame.image.load(os.path.join(image_path, 'settler_dead_f.png')).convert_alpha()
image_settler_baby = pygame.image.load(os.path.join(image_path, 'settler_baby.png')).convert_alpha()
image_tree = pygame.image.load(os.path.join(image_path, 'tree.png')).convert_alpha()
image_house = pygame.image.load(os.path.join(image_path, 'house.png')).convert_alpha()
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

def cal_Dist(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist

def find_centroid(x,y):
    centroid = (int(sum(x) / len(x)),int( sum(y) / len(y)))
    return centroid


def check_land(x,y):
    for rect in land_hitbox:
        if rect.collidepoint(x,y):
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
    if temp>32: color=GREEN
    else: color=WHITE
    for i in range(0,len(land_x)):
        
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
            screen.blit(image_settler, (settler_x[i]-1, settler_y[i]-9))
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

        if i in range(0,len(house_x)): screen.blit(image_house, (house_x[i]-6, house_y[i]-18))
        if i ==len(house_x)+int(church_stage>0)-1 and church_stage>0:
            if church_stage<1:
               screen.blit(image_church_st1, (church_x-8, church_y-28))
            elif church_stage<2 and church_stage>1:
               screen.blit(image_church_st2, (church_x-8, church_y-28))
            elif church_stage>2: screen.blit(image_church, (church_x-8, church_y-28))
        elif i ==len(house_x)+int(church_stage>0)+int(windmill_stage>0)-1 and windmill_stage>0:
            if windmill_stage<1:
               screen.blit(image_church_st1, (windmill_x-8, windmill_y-28))
            elif windmill_stage<2 and windmill_stage>1:
               screen.blit(image_windmill_st2, (windmill_x-8, windmill_y-28))
            elif windmill_stage>2: screen.blit(image_windmill, (windmill_x-8, windmill_y-28))   


def render_animal(animal_x,animal_y):
    for i in range(0,len(animal_x)):
        screen.blit(image_animal, (animal_x[i]-5, animal_y[i]-8))

def render_meat(animal_dead_x,animal_dead_y):
    for i in range(0,len(animal_dead_x)):
        screen.blit(image_meat, (animal_dead_x[i]-5, animal_dead_y[i]-8))

def render_grain(grain_x,grain_y):
    for i in range(0,len(grain_x)):
        screen.blit(image_grain, (grain_x[i]-4, grain_y[i]-9))


    
            

class player:
    
    def draw_land(land_x,land_y):
        mouse_clk=pygame.mouse.get_pressed()
        x_m,y_m=pygame.mouse.get_pos()

        if mouse_clk[0] and not check_land(x_m,y_m):
            land_x.append(x_m)
            land_y.append(y_m)
            land_hitbox.append(pygame.Rect(x_m-r_l,y_m-r_l,2*r_l,2*r_l))
            land_farm_stage.append(0)
            land_snow.append(0)
            
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
            settler.born(x_m,y_m)
    def spawn_cloud():
        x_m,y_m=pygame.mouse.get_pos()
        if pygame.key.get_pressed()[99]:
            cloud_x.append(x_m)
            cloud_y.append(y_m)
            cloud_storm.append(0)
            cloud_cap.append(20)
         

              

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
            
            if not check_land(settler_x[i],settler_y[i]):#seek land
              
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
                        animal.hunted(animal_short)
                    
                    
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
                    settler_sheltered[i]=1
                    if settler_hunger[i]<1000 and settler_age[i]<63000*0.5 and settler_health[i]<100: settler_health[i]=settler_health[i]+1
                    x_mod=x_mod*3
                    y_mod=y_mod*3
  

            elif len(animal_x)>2 and settler_job[i]=='hunter' and (sum(settler_hunger)/len(settler_hunger))>750 and len(animal_dead_x)<1: #seek to hunt when people are hungry
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
                        animal.hunted(animal_short)             
                    
    
            elif (len(settler_x)+len(settler_baby_x)*0.25)>len(house_x) and len(tree_x)>1 and settler_job[i]=='builder':#seek material for shelter

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
            elif (avg_an_fert=='-' or avg_an_fert<85) and len(land_farm_i)<len(settler_x)/4 and settler_job[i]=='farmer': #seek to build farms
                dist_short=9999
                for j in range(0,len(land_x)):
                    dist=cal_Dist(settler_x[i],settler_y[i],land_x[j],land_y[j])
                    if dist<dist_short and j not in land_farm_i:
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


            elif len(house_x)>=len(settler_x) and settler_age[i]<63000*0.35 and settler_happiness[i]>50 and settler_gender[i] and len(settler_x)>1 and len([k for k, e in enumerate(settler_gender) if e == 0])>len(settler_baby_parent)  : #seak mate
                dist_short=9999
                for j in range(0,len(settler_x)):
                    dist=cal_Dist(settler_x[i],settler_y[i],settler_x[j],settler_y[j])
                    if dist<dist_short and not settler_gender[j] and j not in settler_baby_parent and settler_age[j]<63000*0.35:
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
                    #print(settler_age[i]*(15/6300), settler_age[j]*(15/6300))
                    settler_baby.born(x_dest,y_dest)
            elif windmill_stage<2 and len(land_farm_i)>5 and settler_job[i]=='builder': #seek to build windmill
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
                 elif windmill_stage==0 and settler_inv_wood[i]>=5:
                    farm_x=[land_x[k] for k in land_farm_i]
                    farm_y=[land_y[k] for k in land_farm_i]
                    cent=find_centroid(farm_x,farm_y)
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
                        windmill_x=x_dest
                        windmill_y=y_dest
                        settler_inv_wood[i]=settler_inv_wood[i]-5
                        windmill_stage=.1
                 elif windmill_stage>0 and windmill_stage<2 and settler_inv_wood[i]>=5:
                    x_dest=windmill_x
                    y_dest=windmill_y
                    if settler_x[i]-x_dest>0:
                         x_mod=mod
                    else:
                         x_mod=mod*-1

                    if settler_y[i]-y_dest>0:
                         y_mod=mod
                    else:
                         y_mod=mod*-1

                    if cal_Dist(x_dest,y_dest,settler_x[i],settler_y[i])<3:
                        windmill_stage=windmill_stage+.1
                        settler_inv_wood[i]=settler_inv_wood[i]-5
            elif church_stage<2 and len(house_x)>30 and settler_job[i]=='builder': #seek to build church
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


            elif church_stage>=2 and settler_happiness[i]<100: #seek church when sad
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
                     settler_health[i]=100
                     x_mod=x_mod*3
                     y_mod=y_mod*3
                     if settler_happiness[i]<100:
                         settler_happiness[i]=settler_happiness[i]+0.1
            elif len(settler_x)>1: #seek to socialize when bored
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
                     if settler_happiness[i]<100: settler_happiness[i]=settler_happiness[i]+0.1
                     settler_social[i].append(settler_short)
                     if len(settler_social[i])>(len(settler_x)-2)*10: settler_social[i]=[]
                  

            
            x_r=random.random()
            y_r=random.random() 
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
            if temp<32 and not settler_sheltered[i]: settler_health[i]=settler_health[i]-0.1
            if settler_hunger[i]>1000: settler_health[i]=settler_health[i]-0.1
            if settler_age[i]>63000*0.5: settler_health[i]=settler_health[i]-0.1*random.randint(0,1)
            if settler_age[i]>63000*0.35: settler_job[i]='retired'
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
            for j in range(0,len(settler_home)):
                 if not settler_home[j]:
                           settler_home[j]=1
                           break
                      
            house_x.append(settler_x[i])
            house_y.append(settler_y[i])
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
        for j in range(0,len(settler_x)):
            if settler_happiness[j]>5:
                settler_happiness[j]=settler_happiness[j]-5
            else: settler_happiness[j]=0 
    def born(x,y):
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
         if avg_happiness!='-': settler_happiness.append(avg_happiness)
         else: settler_happiness.append(100)
         settler_age.append(6300)
         r=random.random()
         r_job=random.randint(0,2)
         if r>.5:
             settler_gender.append(0)
         else:
             settler_gender.append(1)
         if r_job==0: settler_job.append('farmer')
         elif r_job==1: settler_job.append('hunter')
         elif r_job==2: settler_job.append('builder')
         #print(settler_job)


class tree:
    def grow(tree_x,tree_y):
        if len(tree_x)<int(len(land_x)*fertility) and len(land_x)>100:
            ran=random.random()
            i_ran=int(len(land_x)*ran)
            
            tree_x.append(land_x[i_ran])
            tree_y.append(land_y[i_ran])
        for i in range(0,len(tree_x)):
            if not check_land(tree_x[i],tree_y[i]):
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
            
            if not check_land(house_x[i],house_y[i]):
                house_x[i]=-10
                house_y[i]=-10

                i_house.append(i)
        i_h=0
        for i in range(0,len(settler_home)):
            if settler_home[i]:
                if i_h in i_house:
                    settler_home[i]=0
                i_h=i_h+1
        if -10 in house_x: house_x.remove(-10)
        if -10 in house_y: house_y.remove(-10)
       
        buildings_y=house_y
        if church_stage>0:
            buildings_y=buildings_y+[church_y]
        if windmill_stage>0:
            buildings_y=buildings_y+[windmill_y]
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
                        
            
            if not check_land(animal_x[i],animal_y[i]):#seek land 
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
            if animal_food[i]<1 or not check_land(animal_dead_x[i],animal_dead_y[i]):
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
            
            if not check_land(settler_baby_x[i],settler_baby_y[i]):#seek land
              
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
            if settler_baby_age[i]>6300:
                settler.born(settler_baby_x[i],settler_baby_y[i])
                settler_baby_grown.append(i)

        for i in sorted(settler_baby_grown, reverse=True):
            settler_baby_x.pop(i)
            settler_baby_y.pop(i)
            settler_baby_age.pop(i)
            settler_baby_parent.pop(i)
        settler_baby_grown=[]
        render_settler_baby(settler_baby_x,settler_baby_y)
    def born(x,y):
        settler_baby_x.append(x)
        settler_baby_y.append(y)
        settler_baby_age.append(0)

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
            if grain_food[i]<1 or not check_land(grain_x[i],grain_y[i]):
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
        if windmill_stage>2:
            grain_food.append(40)
        else: grain_food.append(20)


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
                        land_farm_stage[j]=land_farm_stage[j]+0.00025
                    

            if rain_fall[i]>35: del_rain.append(i)
        for i in sorted(del_rain, reverse=True):
            rain_x.pop(i)
            rain_y.pop(i)
            rain_fall.pop(i)
        render_rain(rain_x,rain_y)
        
temp=int(50+50*math.sin(t))+random.randint(-5,5)        
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)
     
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
    settler.next_move(settler_x,settler_y)
    settler_baby.next_move(settler_baby_x,settler_baby_y)
    animal.next_move(animal_x,animal_y)
    farm.grow(land_farm_stage)
    tree.grow(tree_x,tree_y)
    house.built(house_x,house_y)
    cloud.rain(rain_x,rain_y)
    cloud.move(cloud_x,cloud_y)
    if fertility<0.5: fertility=fertility+0.0001
    
    pop=len(settler_x)
    pop_ch=len(settler_baby_x)
    homes=len(house_x)
    if len(settler_health)==0: avg_health='-'
    else: avg_health=int(sum(settler_health)/len(settler_health))

    if len(settler_happiness)==0: avg_happiness='-'
    else: avg_happiness=int(sum(settler_happiness)/len(settler_happiness))

    if len(settler_age)==0: avg_age='-'
    else: avg_age=int((sum(settler_age)+sum(settler_baby_age))/(len(settler_age)+len(settler_baby_age))*(15/6300))
    if len(animal_fertility)==0: avg_an_fert='-'
    else: avg_an_fert=int(sum(animal_fertility)/len(animal_fertility))
    pygame.display.set_caption("Pop/homes: "+str(pop)+"("+str(pop_ch)+")"+" / "+str(homes)+" | Temp: "+str(temp)+"°F | Avg Age: "+str(avg_age)+" | Avg Health: "+str(avg_health)+"%"+" | Avg Happiness: "+str(avg_happiness))
    pygame.display.flip()
    t=t+1
pygame.quit()
