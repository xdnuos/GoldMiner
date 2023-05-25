from define import *
from entities.gold import Gold
from entities.tnt import TNT
from entities.other import Other
from entities.rock import Rock
from entities.mole import Mole
from entities.question import QuestionBag
# Kiểm tra va chạm giữa dây và item
def is_collision(rope, item):
    if rope.hoo.rect.colliderect(item.rect) and rope.state == 'expanding':
        return True
    return False 
def explosive_item(tnt, items):
    items_to_remove = []
    for item in items:
        if item == tnt:
            continue
        if math.sqrt(pow(abs(item.x-tnt.x),2) + pow(abs(item.y-tnt.y),2)) < 200:
            items_to_remove.append(item)
    for item in items_to_remove:
        items.remove(item)
        
def load_item(item_data,is_clover=False,is_gem=False,is_rock=False):
    item_name = item_data["type"]
    x = item_data["pos"]["x"]
    y = item_data["pos"]["y"]
    item = None
    match item_name:
        case "MiniGold":
            item = Gold(x,y,30,MiniGold_point)
        case "NormalGold":
            item = Gold(x,y,70,NormalGold_point)
        case "NormalGoldPlus":
            item = Gold(x,y,90,NormalGoldPlus_point)
        case "BigGold":
            if is_rock:
                item = Gold(x,y,150,BigGold_point*3)
            else:
                item = Gold(x,y,150,BigGold_point)
        case "MiniRock":
            if is_rock:
                item = Rock(x,y,30,MiniRock_point*3)
            else: item = Rock(x,y,30,MiniRock_point)
        case "NormalRock":
            if is_rock:
                item = Rock(x,y,60,NormalRock_point*3)
            else:
                item = Rock(x,y,60,NormalRock_point)
        case "QuestionBag":
            if is_clover:
                item = QuestionBag(x,y,lucky=2)
        case "Diamond":
            if is_gem:
                item = Other(x,y,diamond_image,int(Diamond_point*1.5))
            else: item = Other(x,y,diamond_image,Diamond_point)
        case "Mole":
            item = Mole(x,y,mole_image,Mole_point,direction=item_data["dir"])
        case "MoleWithDiamond":
            if is_gem:
                item = Mole(x,y,mole2_image,int(Diamond_point*1.5)+2,direction=item_data["dir"])
            else:
                item = Mole(x,y,mole2_image,MoleWithDiamond_point,direction=item_data["dir"])
        case "Skull":
            item = Other(x,y,skull_image,Skull_point)
        case "Bone":
            item = Other(x,y,bone_image,Bone_point)
        case "TNT":
            item = TNT(x,y)
        case _:
            item = None
    return item
def load_items(items_data,is_clover=False,is_gem=False,is_rock=False):
    items = []
    for item in items_data:
        # if(item != None):
        items.append(load_item(item,is_clover,is_gem,is_rock))
    return items
def load_level(level,is_clover,is_gem,is_rock):
    bg_name = None
    bg = None
    file_path = "levels.game"
    try :
        with open(file_path, "r") as file:
            data = json.load(file)
        bg_name = data[level]['type']
        match bg_name:
            case "LevelA":
                bg = bgA
            case "LevelB":
                bg = bgB
            case "LevelC":
                bg = bgC
            case "LevelD":
                bg = bgD
            case "LevelE":
                bg = bgA
            case _:
                bg = bgA
    except:
        print("No file levels.game!")
        sys.exit(0)
    return bg,load_items(data[level]['entities'],is_clover,is_gem,is_rock)
def random_level(level_number):
    ran_level = random.randint(1, 3)
    level_text  = "L"+str(level_number)+"_"+str(ran_level)
    return level_text
def draw_point(rope,dt,miner):
    if rope.text == "dynamite" and rope.text_direction !="None":
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt*rope.speed /(5)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.4
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed /(25)
        if rope.time_text < 0:
            if rope.text_direction == "left":
                rope.x_text -= dt * rope.speed
                if rope.x_text <= 500:  # Reached left boundary, change direction
                    rope.text_direction = "right"
            elif rope.text_direction == "right":
                rope.x_text += dt * rope.speed
                if rope.x_text >= 700:  # Reached right boundary, change direction
                    rope.text_direction = "None"
        screen.blit(dynamite_image,(rope.x_text,10))
    elif rope.text == "strength" and rope.text_direction !="None":
        rope.time_text -= dt
        miner.state = 3
        if rope.x_text > 400:
            rope.text_size += dt*rope.speed /(8)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.4
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed
        if rope.time_text < 0:
            if rope.text_direction == "left":
                rope.x_text -= dt * rope.speed
                if rope.x_text <= 400:  # Reached left boundary, change direction
                    rope.text_direction = "right"
            elif rope.text_direction == "right":
                rope.text_size -= dt*rope.speed /(5)
                if rope.text_size <= 0:  # Reached right boundary, change direction
                    miner.state = 3
                    rope.text_direction = "None"
        text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), int(rope.text_size))
        screen.blit(text_font.render("Sức mạnh", True, (0, 15, 0)), (rope.x_text, rope.y_text))
    elif rope.text != "" and rope.x_text > 120 and rope.text_direction !="None": # show tiền
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt*rope.speed /(5)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.2
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed /(25)
        if rope.time_text < 0:
            rope.x_text -= dt*rope.speed
        text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), int(rope.text_size))
        screen.blit(text_font.render("+$"+rope.text, True, (0, 15, 0)), (rope.x_text, rope.y_text))

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def blit_nor_text(surface, text_in, pos, font, color=pygame.Color('black')):
    text = font.render(text_in, True, color)
    surface.blit(text,text.get_rect(center = pos))
def is_enough_money(item_price):
    if item_price > get_score():
        return False
    return True
def buy_item(item_id,price):
    match item_id:
        case 1: #rock_collectors_book
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 2: #strength_drink
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 3: #gem_polish
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 4: #clover
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 5: #dynamite
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False

def get_high_score():
    