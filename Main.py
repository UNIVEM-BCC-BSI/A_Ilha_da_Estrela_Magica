import pygame
import perguntas, Botao, Mapa, Inimigo, Level, Batalha, Loja

pygame.init()
print('<' + '=' * 100 + '>')
# <==== GLOBAL VARIABLES ====>
menu_state = 'mainMenu'
perguntas = perguntas.perguntas
battleActive = False
levelList, enemyList = [], []
dinheiros = 27
font = pygame.font.SysFont('comicsansms', 50)
fontBattle = pygame.font.SysFont('comicsansms', 30)
poderes = {
    'vida_extra': 0,
    'tempo_extra': 0,
    'dano_extra': 0,
    'esquiva': 0,
    'sans': 0,
    'instinto_inferior': 0,
}

TEXT_COL = (255, 255, 255)
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# <==== IMPORT SPRITES ====>
button_unp_play = pygame.image.load('sprite/play_button_unp.png').convert_alpha()
button_pressed_play = pygame.image.load('sprite/play_btn.png').convert_alpha()
button_unp_quit = pygame.image.load('sprite/quit_button_unp.png').convert_alpha()
button_pressed_quit = pygame.image.load('sprite/quit_button.png').convert_alpha()

button_unp_left = pygame.image.load('sprite/left_btn_unp.png').convert_alpha()
button_pressed_left = pygame.image.load('sprite/left_btn.png').convert_alpha()
button_unp_right = pygame.image.load('sprite/right_btn_unp.png').convert_alpha()
button_pressed_right = pygame.image.load('sprite/right_btn.png').convert_alpha()

button_unp_store = pygame.image.load('sprite/store_button_unp.png').convert_alpha()
button_pressed_store = pygame.image.load('sprite/store_btn.png').convert_alpha()

# Level button
button_unp_level_1 = pygame.image.load('sprite/level_1_unp.png').convert_alpha()
button_pressed_level_1 = pygame.image.load('sprite/level_1_btn.png').convert_alpha()
button_unp_level_2 = pygame.image.load('sprite/level_2_unp.png').convert_alpha()
button_pressed_level_2 = pygame.image.load('sprite/level_2_btn.png').convert_alpha()
button_unp_level_3 = pygame.image.load('sprite/level_3_unp.png').convert_alpha()
button_pressed_level_3 = pygame.image.load('sprite/level_3_btn.png').convert_alpha()
button_unp_level_4 = pygame.image.load('sprite/level_4_unp.png').convert_alpha()
button_pressed_level_4 = pygame.image.load('sprite/level_4_btn.png').convert_alpha()
button_unp_boss = pygame.image.load('sprite/boss_unp_btn.png').convert_alpha()
button_pressed_boss = pygame.image.load('sprite/boss_btn.png').convert_alpha()

button_unp_level_1_red = pygame.image.load('sprite/level_1_unp_btn_red.png').convert_alpha()
button_pressed_level_1_red = pygame.image.load('sprite/level_1_btn_red.png').convert_alpha()
button_unp_level_2_red = pygame.image.load('sprite/level_2_unp_btn_red.png').convert_alpha()
button_pressed_level_2_red = pygame.image.load('sprite/level_2_btn_red.png').convert_alpha()
button_unp_level_3_red = pygame.image.load('sprite/level_3_unp_btn_red.png').convert_alpha()
button_pressed_level_3_red = pygame.image.load('sprite/level_3_btn_red.png').convert_alpha()
button_unp_level_4_red = pygame.image.load('sprite/level_4_unp_btn_red.png').convert_alpha()
button_pressed_level_4_red = pygame.image.load('sprite/level_4_btn_red.png').convert_alpha()

button_unp_level_1_grey = pygame.image.load('sprite/level_1_unp_grey.png').convert_alpha()
button_pressed_level_1_grey = pygame.image.load('sprite/level_1_btn_grey.png').convert_alpha()
button_unp_level_2_grey = pygame.image.load('sprite/level_2_unp_grey.png').convert_alpha()
button_pressed_level_2_grey = pygame.image.load('sprite/level_2_btn_grey.png').convert_alpha()
button_unp_level_3_grey = pygame.image.load('sprite/level_3_unp_grey.png').convert_alpha()
button_pressed_level_3_grey = pygame.image.load('sprite/level_3_btn_grey.png').convert_alpha()
button_unp_level_4_grey = pygame.image.load('sprite/level_4_unp_grey.png').convert_alpha()
button_pressed_level_4_grey = pygame.image.load('sprite/level_4_btn_grey.png').convert_alpha()
button_unp_boss_grey = pygame.image.load('sprite/boss_unp_grey.png').convert_alpha()
button_pressed_boss_grey = pygame.image.load('sprite/boss_btn_grey.png').convert_alpha()

# Enemy level button
enemy_unp_1 = pygame.image.load('sprite/enemy_1_unp_btn.png').convert_alpha()
enemy_pressed_1 = pygame.image.load('sprite/enemy_1_btn.png').convert_alpha()
enemy_unp_2 = pygame.image.load('sprite/enemy_2_unp_btn.png').convert_alpha()
enemy_pressed_2 = pygame.image.load('sprite/enemy_2_btn.png').convert_alpha()
enemy_unp_3 = pygame.image.load('sprite/enemy_3_unp_btn.png').convert_alpha()
enemy_pressed_3 = pygame.image.load('sprite/enemy_3_btn.png').convert_alpha()

enemy_unp_1_red = pygame.image.load('sprite/enemy_1_unp_btn_red.png').convert_alpha()
enemy_pressed_1_red = pygame.image.load('sprite/enemy_1_btn_red.png').convert_alpha()
enemy_unp_2_red = pygame.image.load('sprite/enemy_2_unp_btn_red.png').convert_alpha()
enemy_pressed_2_red = pygame.image.load('sprite/enemy_2_btn_red.png').convert_alpha()
enemy_unp_3_red = pygame.image.load('sprite/enemy_3_unp_btn_red.png').convert_alpha()
enemy_pressed_3_red = pygame.image.load('sprite/enemy_3_btn_red.png').convert_alpha()

enemy_unp_1_grey = pygame.image.load('sprite/enemy_1_unp_grey.png').convert_alpha()
enemy_pressed_1_grey = pygame.image.load('sprite/enemy_1_btn_grey.png').convert_alpha()
enemy_unp_2_grey = pygame.image.load('sprite/enemy_2_unp_grey.png').convert_alpha()
enemy_pressed_2_grey = pygame.image.load('sprite/enemy_2_btn_grey.png').convert_alpha()
enemy_unp_3_grey = pygame.image.load('sprite/enemy_3_unp_grey.png').convert_alpha()
enemy_pressed_3_grey = pygame.image.load('sprite/enemy_3_btn_grey.png').convert_alpha()

# Option button
button_unp_a = pygame.image.load('sprite/a_btn_unp.png').convert_alpha()
button_pressed_a = pygame.image.load('sprite/a_btn.png').convert_alpha()
button_unp_b = pygame.image.load('sprite/b_btn_unp.png').convert_alpha()
button_pressed_b = pygame.image.load('sprite/b_btn.png').convert_alpha()
button_unp_c = pygame.image.load('sprite/c_btn_unp.png').convert_alpha()
button_pressed_c = pygame.image.load('sprite/c_btn.png').convert_alpha()
button_unp_d = pygame.image.load('sprite/d_btn_unp.png').convert_alpha()
button_pressed_d = pygame.image.load('sprite/d_btn.png').convert_alpha()

# Enemy button
capanga_1 = pygame.image.load('sprite/capanga_1.png').convert_alpha()
capanga_2 = pygame.image.load('sprite/capanga_2.png').convert_alpha()
capanga_3 = pygame.image.load('sprite/capanga_3.png').convert_alpha()
capanga_4 = pygame.image.load('sprite/capanga_4.png').convert_alpha()

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  rect = img.get_rect(center=(x, y))
  screen.blit(img, rect)

# <==== BUTTONS ====>
# Select buttons
button_group_play = pygame.sprite.GroupSingle()
button_play = Botao.Button(button_unp_play, button_pressed_play, (WIDTH * 0.5), (HEIGHT * 0.25), 5)
button_group_play.add(button_play)
button_group_quit = pygame.sprite.GroupSingle()
button_quit = Botao.Button(button_unp_quit, button_pressed_quit, (WIDTH * 0.5), (HEIGHT * 0.5), 5)
button_group_quit.add(button_quit)
button_group_left = pygame.sprite.GroupSingle()
button_left = Botao.Button(button_unp_left, button_pressed_left, 35, 10, 3)
button_group_left.add(button_left)
button_group_item_1 = pygame.sprite.GroupSingle()
button_item_1 = Botao.Button(button_unp_right, button_pressed_right, WIDTH * 0.2, HEIGHT * 0.3, 3)
button_group_item_1.add(button_item_1)
button_group_item_2 = pygame.sprite.GroupSingle()
button_item_2 = Botao.Button(button_unp_right, button_pressed_right, WIDTH * 0.2, HEIGHT * 0.4, 3)
button_group_item_2.add(button_item_2)
button_group_item_3 = pygame.sprite.GroupSingle()
button_item_3 = Botao.Button(button_unp_right, button_pressed_right, WIDTH * 0.2, HEIGHT * 0.5, 3)
button_group_item_3.add(button_item_3)
button_group_item_4 = pygame.sprite.GroupSingle()
button_item_4 = Botao.Button(button_unp_right, button_pressed_right, WIDTH * 0.2, HEIGHT * 0.6, 3)
button_group_item_4.add(button_item_4)
button_group_store = pygame.sprite.GroupSingle()
button_store = Botao.Button(button_unp_store, button_pressed_store, WIDTH * 0.1, HEIGHT * 0.5, 3)
button_group_store.add(button_store)

# Level buttons
button_group_level_1 = pygame.sprite.GroupSingle()
button_level_1 = Botao.Button(button_unp_level_1, button_pressed_level_1, (WIDTH * 0.5), (HEIGHT * 0.75), 3)
button_group_level_1.add(button_level_1)
button_group_level_2 = pygame.sprite.GroupSingle()
button_level_2 = Botao.Button(button_unp_level_2, button_pressed_level_2, (WIDTH * 0.5), (HEIGHT * 0.625), 3)
button_group_level_2.add(button_level_2)
button_group_level_3 = pygame.sprite.GroupSingle()
button_level_3 = Botao.Button(button_unp_level_3, button_pressed_level_3, (WIDTH * 0.5), (HEIGHT * 0.5), 3)
button_group_level_3.add(button_level_3)
button_group_level_4 = pygame.sprite.GroupSingle()
button_level_4 = Botao.Button(button_unp_level_4, button_pressed_level_4, (WIDTH * 0.5), (HEIGHT * 0.375), 3)
button_group_level_4.add(button_level_4)
button_group_boss = pygame.sprite.GroupSingle()
button_boss = Botao.Button(button_unp_boss, button_pressed_boss, (WIDTH * 0.5), (HEIGHT * 0.375), 3)
button_group_boss.add(button_boss)

button_group_level_1_red = pygame.sprite.GroupSingle()
button_level_1_red = Botao.Button(button_unp_level_1_red, button_pressed_level_1_red, (WIDTH * 0.5), (HEIGHT * 0.75), 3)
button_group_level_1_red.add(button_level_1_red)
button_group_level_2_red = pygame.sprite.GroupSingle()
button_level_2_red = Botao.Button(button_unp_level_2_red, button_pressed_level_2_red, (WIDTH * 0.5), (HEIGHT * 0.625), 3)
button_group_level_2_red.add(button_level_2_red)
button_group_level_3_red = pygame.sprite.GroupSingle()
button_level_3_red = Botao.Button(button_unp_level_3_red, button_pressed_level_3_red, (WIDTH * 0.5), (HEIGHT * 0.5), 3)
button_group_level_3_red.add(button_level_3_red)
button_group_level_4_red = pygame.sprite.GroupSingle()
button_level_4_red = Botao.Button(button_unp_level_4_red, button_pressed_level_4_red, (WIDTH * 0.5), (HEIGHT * 0.375), 3)
button_group_level_4_red.add(button_level_4_red)

button_group_level_1_grey = pygame.sprite.GroupSingle()
button_level_1_grey = Botao.Button(button_unp_level_1_grey, button_pressed_level_1_grey, (WIDTH * 0.5), (HEIGHT * 0.75), 3)
button_group_level_1_grey.add(button_level_1_grey)
button_group_level_2_grey = pygame.sprite.GroupSingle()
button_level_2_grey = Botao.Button(button_unp_level_2_grey, button_pressed_level_2_grey, (WIDTH * 0.5), (HEIGHT * 0.625), 3)
button_group_level_2_grey.add(button_level_2_grey)
button_group_level_3_grey = pygame.sprite.GroupSingle()
button_level_3_grey = Botao.Button(button_unp_level_3_grey, button_pressed_level_3_grey, (WIDTH * 0.5), (HEIGHT * 0.5), 3)
button_group_level_3_grey.add(button_level_3_grey)
button_group_level_4_grey = pygame.sprite.GroupSingle()
button_level_4_grey = Botao.Button(button_unp_level_4_grey, button_pressed_level_4_grey, (WIDTH * 0.5), (HEIGHT * 0.375), 3)
button_group_level_4_grey.add(button_level_4_grey)
button_group_boss_grey = pygame.sprite.GroupSingle()
button_boss_grey = Botao.Button(button_unp_boss_grey, button_pressed_boss_grey, (WIDTH * 0.5), (HEIGHT * 0.375), 3)
button_group_boss_grey.add(button_boss_grey)

# Enemies buttons
button_group_inimigo_1 = pygame.sprite.GroupSingle()
button_inimigo_1 = Botao.Button(enemy_unp_1, enemy_pressed_1, 100, 100, 3)
button_group_inimigo_1.add(button_inimigo_1)
button_group_inimigo_2 = pygame.sprite.GroupSingle()
button_inimigo_2 = Botao.Button(enemy_unp_2, enemy_pressed_2, 100, 200, 3)
button_group_inimigo_2.add(button_inimigo_2)
button_group_inimigo_3 = pygame.sprite.GroupSingle()
button_inimigo_3 = Botao.Button(enemy_unp_3, enemy_pressed_3, 100, 300, 3)
button_group_inimigo_3.add(button_inimigo_3)

button_group_inimigo_1_red = pygame.sprite.GroupSingle()
button_inimigo_1_red = Botao.Button(enemy_unp_1_red, enemy_pressed_1_red, 100, 100, 3)
button_group_inimigo_1_red.add(button_inimigo_1_red)
button_group_inimigo_2_red = pygame.sprite.GroupSingle()
button_inimigo_2_red = Botao.Button(enemy_unp_2_red, enemy_pressed_2_red, 100, 200, 3)
button_group_inimigo_2_red.add(button_inimigo_2_red)
button_group_inimigo_3_red = pygame.sprite.GroupSingle()
button_inimigo_3_red = Botao.Button(enemy_unp_3_red, enemy_pressed_3_red, 100, 300, 3)
button_group_inimigo_3_red.add(button_inimigo_3_red)

button_group_inimigo_1_grey = pygame.sprite.GroupSingle()
button_inimigo_1_grey = Botao.Button(enemy_unp_1_grey, enemy_pressed_1_grey, 100, 100, 3)
button_group_inimigo_1_grey.add(button_inimigo_1_grey)
button_group_inimigo_2_grey = pygame.sprite.GroupSingle()
button_inimigo_2_grey = Botao.Button(enemy_unp_2_grey, enemy_pressed_2_grey, 100, 200, 3)
button_group_inimigo_2_grey.add(button_inimigo_2_grey)
button_group_inimigo_3_grey = pygame.sprite.GroupSingle()
button_inimigo_3_grey = Botao.Button(enemy_unp_3_grey, enemy_pressed_3_grey, 100, 300, 3)
button_group_inimigo_3_grey.add(button_inimigo_3_grey)

# Battle buttons
button_group_option_a = pygame.sprite.GroupSingle()
button_option_a = Botao.Button_Enemy(button_unp_a, button_pressed_a, WIDTH * 0.1, HEIGHT * 0.55, 3, "a")
button_group_option_a.add(button_option_a)
button_group_option_b = pygame.sprite.GroupSingle()
button_option_b = Botao.Button_Enemy(button_unp_b, button_pressed_b, WIDTH * 0.53, HEIGHT * 0.55, 3, 'b')
button_group_option_b.add(button_option_b)
button_group_option_c = pygame.sprite.GroupSingle()
button_option_c = Botao.Button_Enemy(button_unp_c, button_pressed_c, WIDTH * 0.1, HEIGHT * 0.77, 3, 'c')
button_group_option_c.add(button_option_c)
button_group_option_d = pygame.sprite.GroupSingle()
button_option_d = Botao.Button_Enemy(button_unp_d, button_pressed_d, WIDTH * 0.53, HEIGHT * 0.77, 3, 'd')
button_group_option_d.add(button_option_d)

# Enemy
capanga_group_1 = Inimigo.Enemy()

# TESTE
mapa = Mapa.Map([
    button_group_level_1,
    button_group_level_2,
    button_group_level_3,
    button_group_boss,
    button_group_level_1_red,
    button_group_level_2_red,
    button_group_level_3_red,
    button_group_level_1_grey,
    button_group_level_2_grey,
    button_group_level_3_grey,
    button_group_boss_grey,
    button_group_store,
], [
    button_level_1,
    button_level_2,
    button_level_3,
    button_boss,
    button_level_1_red,
    button_level_2_red,
    button_level_3_red,
    button_level_1_grey,
    button_level_2_grey,
    button_level_3_grey,
    button_boss_grey,
    button_store,
], screen)

nivel = Level.LevelState([
    button_group_inimigo_1,
    button_group_inimigo_2,
    button_group_inimigo_3,
    button_group_inimigo_1_red,
    button_group_inimigo_2_red,
    button_group_inimigo_3_red,
    button_group_inimigo_1_grey,
    button_group_inimigo_2_grey,
    button_group_inimigo_3_grey,
], [
    button_inimigo_1,
    button_inimigo_2,
    button_inimigo_3,
    button_inimigo_1_red,
    button_inimigo_2_red,
    button_inimigo_3_red,
    button_inimigo_1_grey,
    button_inimigo_2_grey,
    button_inimigo_3_grey,
], screen)

batalha = Batalha.Battle([
    capanga_1,
    capanga_2,
    capanga_3,
    capanga_4,
], 1011, 228, 3, [
    button_group_option_a,
    button_group_option_b,
    button_group_option_c,
    button_group_option_d,
], [
  button_option_a,  
  button_option_b,  
  button_option_c,  
  button_option_d,
], screen, [
    'matematica',
    'portugues',
    'historia',
    'geografia',
    'biologia'
], fontBattle, poderes)

loja = Loja.Store(dinheiros, [
    button_group_item_1,
    button_group_item_2,
    button_group_item_3,
    button_group_item_4,
], [
    button_item_1,
    button_item_2,
    button_item_3,
    button_item_4,
], fontBattle, screen, poderes)


run = True
while run:
    screen.fill('White')


    # <==== MAIN MENU ====>
    if menu_state == 'mainMenu':
        draw_text(str(dinheiros), font, 'Black', WIDTH * 0.15, 100)
        draw_text('A Ilha da Estrela Mágica', font, 'Black', (WIDTH * 0.5), 100)

        button_group_play.update()
        button_group_play.draw(screen)

        button_group_quit.update()
        button_group_quit.draw(screen)

        if button_play.mouse_click() == True:
            menu_state = 'map'
            button_play.reset_state()

        if button_quit.mouse_click() == True:
            run = False
    
    # <==== MAP ====>
    if menu_state == 'map':
        screen.fill((52, 78, 91))
        draw_text(str(dinheiros), font, 'Black', WIDTH * 0.15, 100)
        draw_text('MAPA', font, TEXT_COL, (WIDTH * 0.5), 100)

        button_group_left.update()
        button_group_left.draw(screen)

        if len(levelList) == 3 and len(enemyList) == 3:
            mapa.map_state = 'boss'
            nivel.level_state = 'level_1'
            enemyList = []
        elif len(levelList) == 2 and len(enemyList) == 3:
            mapa.map_state = 'level_3'
            nivel.level_state = 'level_1'
            enemyList = []
        elif len(levelList) == 1 and len(enemyList) == 3:
            mapa.map_state = 'level_2'
            nivel.level_state = 'level_1'
            enemyList = []
        
        mapaRetorno = mapa.map_manager()

        if mapaRetorno == 'levelMenu':
            menu_state = 'levelMenu'
            batalha.newEnemy = True # matérias aleatórias
            mapa.reset_state()
        elif mapaRetorno == 'store':
            menu_state = 'store'
            loja.dinheiros = dinheiros
            mapa.reset_state()

        if button_left.mouse_click() == True:
            menu_state = 'mainMenu'
            button_left.reset_state()
        
        
    # <==== LEVEL MENU ====>
    if menu_state == 'levelMenu':
        screen.fill((52, 78, 91))
        draw_text('SELEÇÃO DE INIMIGO', font, TEXT_COL, WIDTH * 0.5, 100)

        button_group_left.update()
        button_group_left.draw(screen)

        if len(enemyList) == 3:
            nivel.level_state = 'boss'
        elif len(enemyList) == 2:
            nivel.level_state = 'level_3'
        elif len(enemyList) == 1:
            nivel.level_state = 'level_2'
                
        if nivel.level_manager() == 'battle':
            menu_state = 'battle'
            batalha.materiaEInimigoIndex += 1
            batalha.poderes = poderes
            batalha.reset_state()
            nivel.reset_state()

        if button_left.mouse_click() == True:
            menu_state = 'map'
            button_left.reset_state()

    # <==== BATTLE ====>
    if menu_state == 'battle':
        draw_text('BATALHA ÉPICA', font, 'Black', WIDTH * 0.5, 30)

        # button_group_left.update()
        # button_group_left.draw(screen)

        batalhaRetorno = batalha.battle_manager()

        if batalhaRetorno['estado'] == 'levelMenu':
            if batalhaRetorno['erros'] == 0:
                dinheiros += 3
            else:
                dinheiros += 1
            
            print(f'Dinheiros: {dinheiros}')
            menu_state = 'levelMenu'
            poderes = batalhaRetorno['poder']
            enemyList.append(True)
            if len(enemyList) == 3:
                levelList.append(True)
                batalha.materiaEInimigoIndex = -1
                batalha.reset_image()
                menu_state = 'map'

        if batalhaRetorno['estado'] == 'mainMenu':
            dinheiros = 0
            batalha.reset_all()
            # loja.reset_state()
            levelList, enemyList = [], []
            poderes = {
                'vida_extra': 0,
                'tempo_extra': 0,
                'dano_extra': 0,
                'esquiva': 0,
                'sans': 0,
                'instinto_inferior': 0,
            }
            nivel.level_state = 'level_1'
            mapa.map_state = 'level_1'
            menu_state = 'mainMenu'
        
        # if button_left.mouse_click() == True:
        #     menu_state = 'levelMenu'

    # <==== STORE ====>
    if menu_state == 'store':
        screen.fill((52, 78, 91))
        draw_text(str(dinheiros), font, 'Black', WIDTH * 0.15, 100)
        draw_text('LOJINHA DO SEU ZÉ', font, TEXT_COL, (WIDTH * 0.5), 100)

        button_group_left.update()
        button_group_left.draw(screen)

        lojaRetorno = loja.store_manager()
        poderes, dinheiros = lojaRetorno[0], lojaRetorno[1]

        if button_left.mouse_click() == True:
            menu_state = 'map'
            button_left.reset_state()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
