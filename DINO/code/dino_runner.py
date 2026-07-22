import raylib as rl
from pyray import *
from os.path import join

init_window(1280, 720, "DINO RUNNER 3000")
init_audio_device()
set_target_fps(60)
# game variable
dino_position = Vector2(100, 300)
velocity = 0
gravity = 0.8
floor_line = 500

cactus_pos_x = 1000

# loading textures
dino_texture = load_texture(join("DINO","assets","dino","run0.png"))
cactus_texture = load_texture(join("DINO","assets","cactii","cactus0.png"))
font_cus = load_font(join("DINO","fonts","RETRO_SPACE.ttf"))
jump = load_sound(join("DINO","audio","jump.wav"))
music_game = load_music_stream(join("DINO","audio","music.mp3"))

play_music_stream(music_game)
while not window_should_close():
        #update_music_stream(music_game)

        # player(Dino) movement
        velocity += gravity
        dino_position.y += velocity
        if dino_position.y > floor_line:
                dino_position.y = floor_line
        if is_key_pressed(rl.KEY_SPACE):
                velocity = -28
                play_sound(jump)

        # quit
        if is_key_pressed(rl.KEY_Q) or is_key_pressed(rl.KEY_ESCAPE):
                close_window()
        # obstacle logic
        cactus_pos_x -= 8

        # draw
        begin_drawing()
        clear_background(RAYWHITE)

        # line
        draw_line_ex(Vector2(0,floor_line+120), Vector2(1280,floor_line+120),10,GRAY)
        draw_texture_ex(dino_texture, dino_position, 0, 5, WHITE)
        draw_texture_ex(cactus_texture, Vector2(cactus_pos_x, floor_line), 0, 5, WHITE)

        # collision
        dino_rect = Rectangle(dino_position.x, dino_position.y, dino_texture.width * 5, dino_texture.height * 5)
        cactus_rec = Rectangle(cactus_pos_x, floor_line, cactus_texture.width * 5, cactus_texture.height * 5)
        if check_collision_recs(dino_rect, cactus_rec):
                close_window()

        if cactus_pos_x < 0:
                cactus_pos_x = 1280

        # text
        score_string = f"score: {int(get_time())}"
        text_width = measure_text_ex(font_cus,score_string, 40, 1).x
        draw_text_ex(font_cus, score_string,Vector2(640 - text_width / 2, 100), 40, 1, PURPLE)

        end_drawing()