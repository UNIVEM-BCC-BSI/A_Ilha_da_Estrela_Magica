import pygame, time, random, StringSplitter
import perguntas, Botao, Mapa, Musica, Level, Batalha, Loja, Narrativa, Predo

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()
pygame.display.set_caption('A Ilha da Estrela Mágica')
icone = pygame.image.load('icone_jogo.jpeg')
pygame.display.set_icon(icone)
# print('<' + '=' * 100 + '>')
# <==== GLOBAL VARIABLES ====>
menu_state = 'mainMenu'
perguntas = perguntas.perguntas
battleActive, musicActive = False, True
levelList, enemyList = 0, 0
dinheiros = 0
tempoRetorno = time.time()
font = pygame.font.SysFont('comicsansms', 30)
fontBattle = pygame.font.SysFont('comicsansms', 20)
poderes = {
    'vida_extra': 0,
    'tempo_extra': 0,
    'dano_extra': 0,
    'sans': 0,
    'instinto_inferior': 0,
}

TEXT_COL = (255, 255, 255)
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# <==== IMPORT SPRITES ====>
# random stuff
map_sprite = pygame.image.load('sprite/bosqueDivino.jpg').convert_alpha()
pedro = pygame.image.load('sprite/pedro.png').convert_alpha()
vendedor = pygame.image.load('sprite/vendedor.png').convert_alpha()
pedro_instinto = pygame.image.load('sprite/pedro_instinto.png').convert_alpha()
sans_drogado = pygame.image.load('sprite/sans_drogado.png').convert_alpha()
pedro_sound = pygame.mixer.Sound('sound/final_judgement.mp3')
pedro_instinto_sound = pygame.mixer.Sound('sound/instinto_inferior.mp3')
pedro_sans_sound = pygame.mixer.Sound('sound/sans.mp3')
menu_sound = pygame.mixer.Sound('sound/tela_inicial_e_mapa.wav')
socao = pygame.mixer.Sound('sound/socao.mp3')
menu_boss_sound = pygame.mixer.Sound('sound/pedro_liberto.mp3')
level_selection = pygame.mixer.Sound('sound/level_selection.wav')
item_comprado = pygame.mixer.Sound('sound/item_comprado.wav')
inimigo_derrotado = pygame.mixer.Sound('sound/inimigo_derrotado.mp3')
game_over = pygame.mixer.Sound('sound/game_over.mp3')
venceu = pygame.mixer.Sound('sound/venceu.mp3')
batalha_1 = pygame.mixer.Sound('sound/batalha_1.wav')
batalha_2 = pygame.mixer.Sound('sound/batalha_2.wav')
batalha_3 = pygame.mixer.Sound('sound/batalha_3.wav')

# general buttons
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
button_group_item_5 = pygame.sprite.GroupSingle()
button_item_5 = Botao.Button(button_unp_right, button_pressed_right, WIDTH * 0.2, HEIGHT * 0.7, 3)
button_group_item_5.add(button_item_5)
button_group_store = pygame.sprite.GroupSingle()
button_store = Botao.Button(button_unp_store, button_pressed_store, WIDTH * 0.7, HEIGHT * 0.57, 3)
button_group_store.add(button_store)

# Level buttons
button_group_level_1 = pygame.sprite.GroupSingle()
button_level_1 = Botao.Button(button_unp_level_1, button_pressed_level_1, (WIDTH * 0.17), (HEIGHT * 0.72), 3)
button_group_level_1.add(button_level_1)
button_group_level_2 = pygame.sprite.GroupSingle()
button_level_2 = Botao.Button(button_unp_level_2, button_pressed_level_2, (WIDTH * 0.4), (HEIGHT * 0.66), 3)
button_group_level_2.add(button_level_2)
button_group_level_3 = pygame.sprite.GroupSingle()
button_level_3 = Botao.Button(button_unp_level_3, button_pressed_level_3, (WIDTH * 0.57), (HEIGHT * 0.37), 3)
button_group_level_3.add(button_level_3)
button_group_level_4 = pygame.sprite.GroupSingle()
button_level_4 = Botao.Button(button_unp_level_4, button_pressed_level_4, (WIDTH * 0.61), (HEIGHT * 0.15), 3)
button_group_level_4.add(button_level_4)
button_group_boss = pygame.sprite.GroupSingle()
button_boss = Botao.Button(button_unp_boss, button_pressed_boss, (WIDTH * 0.61), (HEIGHT * 0.15), 3)
button_group_boss.add(button_boss)

button_group_level_1_red = pygame.sprite.GroupSingle()
button_level_1_red = Botao.Button(button_unp_level_1_red, button_pressed_level_1_red, (WIDTH * 0.17), (HEIGHT * 0.72), 3)
button_group_level_1_red.add(button_level_1_red)
button_group_level_2_red = pygame.sprite.GroupSingle()
button_level_2_red = Botao.Button(button_unp_level_2_red, button_pressed_level_2_red, (WIDTH * 0.44), (HEIGHT * 0.66), 3)
button_group_level_2_red.add(button_level_2_red)
button_group_level_3_red = pygame.sprite.GroupSingle()
button_level_3_red = Botao.Button(button_unp_level_3_red, button_pressed_level_3_red, (WIDTH * 0.57), (HEIGHT * 0.37), 3)
button_group_level_3_red.add(button_level_3_red)
button_group_level_4_red = pygame.sprite.GroupSingle()
button_level_4_red = Botao.Button(button_unp_level_4_red, button_pressed_level_4_red, (WIDTH * 0.61), (HEIGHT * 0.15), 3)
button_group_level_4_red.add(button_level_4_red)

button_group_level_1_grey = pygame.sprite.GroupSingle()
button_level_1_grey = Botao.Button(button_unp_level_1_grey, button_pressed_level_1_grey, (WIDTH * 0.17), (HEIGHT * 0.72), 3)
button_group_level_1_grey.add(button_level_1_grey)
button_group_level_2_grey = pygame.sprite.GroupSingle()
button_level_2_grey = Botao.Button(button_unp_level_2_grey, button_pressed_level_2_grey, (WIDTH * 0.44), (HEIGHT * 0.66), 3)
button_group_level_2_grey.add(button_level_2_grey)
button_group_level_3_grey = pygame.sprite.GroupSingle()
button_level_3_grey = Botao.Button(button_unp_level_3_grey, button_pressed_level_3_grey, (WIDTH * 0.57), (HEIGHT * 0.37), 3)
button_group_level_3_grey.add(button_level_3_grey)
button_group_level_4_grey = pygame.sprite.GroupSingle()
button_level_4_grey = Botao.Button(button_unp_level_4_grey, button_pressed_level_4_grey, (WIDTH * 0.61), (HEIGHT * 0.15), 3)
button_group_level_4_grey.add(button_level_4_grey)
button_group_boss_grey = pygame.sprite.GroupSingle()
button_boss_grey = Botao.Button(button_unp_boss_grey, button_pressed_boss_grey, (WIDTH * 0.61), (HEIGHT * 0.15), 3)
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
button_option_a = Botao.Button_Enemy(button_unp_a, button_pressed_a, WIDTH * 0.04, HEIGHT * 0.51, 3, "a")
button_group_option_a.add(button_option_a)
button_group_option_b = pygame.sprite.GroupSingle()
button_option_b = Botao.Button_Enemy(button_unp_b, button_pressed_b, WIDTH * 0.52, HEIGHT * 0.51, 3, 'b')
button_group_option_b.add(button_option_b)
button_group_option_c = pygame.sprite.GroupSingle()
button_option_c = Botao.Button_Enemy(button_unp_c, button_pressed_c, WIDTH * 0.04, HEIGHT * 0.76, 3, 'c')
button_group_option_c.add(button_option_c)
button_group_option_d = pygame.sprite.GroupSingle()
button_option_d = Botao.Button_Enemy(button_unp_d, button_pressed_d, WIDTH * 0.52, HEIGHT * 0.76, 3, 'd')
button_group_option_d.add(button_option_d)


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
], screen, {
    'level_selection': level_selection
})

batalha = Batalha.Battle([
    capanga_1,
    capanga_2,
    capanga_3,
    capanga_4,
], 1011, 228, 5, [
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
], fontBattle, poderes, [
    batalha_1,
    batalha_2,
    batalha_3,
    pedro_sans_sound
])

loja = Loja.Store(dinheiros, [
    button_group_item_1,
    button_group_item_2,
    button_group_item_3,
    button_group_item_4,
    button_group_item_5,
    button_group_left
], [
    button_item_1,
    button_item_2,
    button_item_3,
    button_item_4,
    button_item_5,
    button_left
], fontBattle, screen, poderes, vendedor)

pedro = Predo.Pedro([
    pedro,
    pedro_instinto,
    sans_drogado
], 1011, 220, {
    'pedro': pedro_sound,
    'pedro_instinto': pedro_instinto_sound,
    'pedro_sans': pedro_sans_sound
}, [
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

narrativaText = Narrativa.NarrativaText(font, menu_state, screen, {
    'vencedor': venceu,
    'game_over': game_over
})

musica_fundo = Musica.BgMusic(menu_sound)

scale_size = (int(WIDTH*0.1), int(HEIGHT*0.1))
img_blur = pygame.transform.smoothscale(map_sprite, scale_size)
img_blur = pygame.transform.smoothscale(img_blur, (WIDTH, HEIGHT))

run = True
while run:
    screen.blit(img_blur, (0, 0))
    if musicActive == True:
        musica_fundo.on_start()
        musicActive = False

    # <==== MAIN MENU ====>
    if menu_state == 'mainMenu':
        draw_text('A Ilha da Estrela Mágica', font, 'White', (WIDTH * 0.5), 80)

        button_group_play.update()
        button_group_play.draw(screen)

        button_group_quit.update()
        button_group_quit.draw(screen)

        if button_play.mouse_click() == True:
            menu_state = 'narrativa'
            narrativaText.menu_state = 'story'
            button_play.reset_state()

        if button_quit.mouse_click() == True:
            run = False
    
    # <==== MAP ====>
    if menu_state == 'map':
        screen.blit(map_sprite, (0, 0))
        draw_text(f'Dinheiro: {str(dinheiros)}', font, 'Black', WIDTH * 0.15, HEIGHT * 0.05)

        button_group_left.update()
        button_group_left.draw(screen)

        if levelList == 3 and enemyList == 3:
            musica_fundo = Musica.BgMusic(menu_boss_sound)
            musicActive = True
            mapa.map_state = 'boss'
            nivel.level_state = 'level_1'
            enemyList = 0
        elif levelList == 2 and enemyList == 3:
            mapa.map_state = 'level_3'
            nivel.level_state = 'level_1'
            enemyList = 0
        elif levelList == 1 and enemyList == 3:
            mapa.map_state = 'level_2'
            nivel.level_state = 'level_1'
            enemyList = 0
        
        mapaRetorno = mapa.map_manager()

        if mapaRetorno == 'levelMenu':
            menu_state = 'levelMenu'

            if batalha.gerarMaterias == True:
                batalha.newEnemy = True
                batalha.gerarMaterias = False
            
            nivel.musicActive = True
            mapa.reset_state()
            musica_fundo.on_exit()
        elif mapaRetorno == 'pedro':
            pedro.embaralharPerguntas()
            pedro.poderes = poderes
            pedro.musicActive = True
            mapa.reset_state()
            menu_state = 'pedro'
            musica_fundo.on_exit()
            pedro.startTime = time.time()
        elif mapaRetorno == 'store':
            menu_state = 'store'
            loja.dinheiros = dinheiros
            loja.musicActive = True
            mapa.reset_state()
            musica_fundo.on_exit()

        if button_left.mouse_click() == True:
            menu_state = 'mainMenu'
            button_left.reset_state()
        
        
    # <==== LEVEL MENU ====>
    if menu_state == 'levelMenu':
        draw_text('SELEÇÃO DE INIMIGO', font, TEXT_COL, WIDTH * 0.5, 100)

        button_group_left.update()
        button_group_left.draw(screen)

        nivelRetorno = nivel.level_manager()

        if enemyList == 3:
            nivel.level_state = 'boss'
        elif enemyList == 2:
            nivel.level_state = 'level_3'
        elif enemyList == 1:
            nivel.level_state = 'level_2'

        if nivelRetorno == 'battle':
            menu_state = 'battle'
            batalha.materiaEInimigoIndex += 1
            batalha.poderes = poderes
            batalha.musicActive = True
            batalha.reset_state()
            nivel.reset_state()

        if button_left.mouse_click() == True:
            menu_state = 'map'
            musicActive = True
            button_left.reset_state()

    # <==== BATTLE ====>
    if menu_state == 'battle':
        screen.fill('#31ad8c')
        draw_text('BATALHA ÉPICA', font, 'Black', WIDTH * 0.5, 30)

        batalhaRetorno = batalha.battle_manager()

        if batalhaRetorno['estado'] == 'levelMenu':
            if batalhaRetorno['morteOuVencedor'] == True:
                # print('Foi por vida extra')
                random.shuffle(batalha.perguntas[batalha.materiaInimigo[batalha.materiaEInimigoIndex]])

                batalha.materiaEInimigoIndex -= 1
                menu_state = 'levelMenu'
                poderes = batalhaRetorno['poder']
            else:
                if batalhaRetorno['erros'] == 0:
                    dinheiros += 3
                else:
                    dinheiros += 1
                
                # print(f'Dinheiros: {dinheiros}')
                menu_state = 'levelMenu'
                poderes = batalhaRetorno['poder']
                enemyList += 1

                # level terminado
                if enemyList == 3:
                    levelList += 1
                    batalha.materiaEInimigoIndex = -1
                    batalha.gerarMaterias = True
                    batalha.reset_image_sound()
                    menu_state = 'map'
                    musicActive = True
            nivel.musicActive = True
        
        if batalhaRetorno['estado'] == 'mainMenu':
            dinheiros = 0
            batalha.reset_all()
            # loja.reset_state()
            levelList, enemyList = 0, 0
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
            menu_state = 'narrativa'
            narrativaText.musicActive = True
            narrativaText.menu_state = 'skillIssue'
    
    # <==== PEDRO ====>
    if menu_state == 'pedro':
        screen.fill('#31ad8c')
        draw_text('"O" PEDRO', font, 'Black', WIDTH * 0.5, 30)

        pedroRetorno = pedro.battle_manager()

        if pedroRetorno['estado'] == 'win':
            menu_state = 'narrativa'
            narrativaText.musicActive = True
            narrativaText.menu_state = 'win'
            pedro.reset_all()
        elif pedroRetorno['estado'] == 'skillIssue':
            menu_state = 'narrativa'
            narrativaText.musicActive = True
            narrativaText.menu_state = 'skillIssue'
            pedro.reset_all()

    # <==== STORE ====>
    if menu_state == 'store':
        screen.fill((52, 78, 91))
        draw_text('LOJINHA DO SEU ZÉ', font, TEXT_COL, (WIDTH * 0.5), 100)

        lojaRetorno = loja.store_manager()
        poderes, dinheiros = lojaRetorno['compras'], lojaRetorno['dinheiros']

        if lojaRetorno['estado'] == 'map':
            menu_state = 'map'
            musicActive = True
            loja.reset_state()
    
    # <==== NARRATIVA ====>
    if menu_state == 'narrativa':
        screen.fill('White')
        narrativaRetorno = narrativaText.manager()

        if narrativaRetorno['estado'] == 'map':
            menu_state = 'map'
            narrativaText.reset_state()
        elif narrativaRetorno['estado'] == 'mainMenu':
            menu_state = 'mainMenu'
            narrativaText.reset_state()
            dinheiros = 0
            batalha.reset_all()
            # loja.reset_state()
            levelList, enemyList = 0, 0
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
            musica_fundo = Musica.BgMusic(menu_sound)
            musicActive = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
