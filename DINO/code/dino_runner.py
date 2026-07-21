import raylib as rl
from pyray import *

init_window(1366, 768, "DINO RUNNER 3000")
init_audio_device()
set_target_fps(24)
# game variable
pos_y = 512
dino_position = Vector2(252, int(pos_y))
velocity = 0
gravity = 10.8
floor_line = 425
ob_x = 1366

# load
dino = load_texture("DINO/assets/dino/run0.png")
cactus = load_texture("DINO/assets/cactii/cactus0.png")
font_cus = load_font("DINO/fonts/RETRO_SPACE.ttf")
jump = load_sound("DINO/audio/jump.wav")
music_game = load_music_stream("DINO/audio/music.mp3")
play_music_stream(music_game)
while not window_should_close():
        #update_music_stream(music_game)
        delta = get_frame_time()
        # INPUT
        if is_key_pressed(rl.KEY_Q) or is_key_pressed(rl.KEY_ESCAPE):
                close_window()
        if is_key_pressed(rl.KEY_SPACE):
                velocity -= 400
                dino_position.y -= velocity * delta
                play_sound(jump)

        # DRAW
        begin_drawing()
        clear_background(RAYWHITE)
        # line
        draw_line_ex(Vector2(0,floor_line+50),Vector2(1366,floor_line+50),8,GRAY)
        draw_texture_ex(dino, Vector2(int(dino_position.x), int(dino_position.y)),0,3,WHITE)

        end_drawing()
        # Player MOVEMENT
        velocity += gravity
        dino_position.y = velocity
        if dino_position.y > floor_line:
                dino_position.y = floor_line