from settings import *
from sprites import Sprite, Dino

class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME)
        init_audio_device()
        set_target_fps(60)
        self.dino = Dino(
            load_texture(join("DINO","assets","dino","run0.png")),
            Vector2(100, FLOOR_LINE),
            load_sound(join("DINO","audio","jump.wav"))
            ) 
    def update(self):
        self.dino.update()

    def draw(self):
        begin_drawing()
        clear_background(WHITE)

        draw_line_ex(
            Vector2(0,FLOOR_LINE+120),
            Vector2(1280,FLOOR_LINE+120),
            10 ,
            MAIN_COLOR
        )
        self.dino.draw()
        end_drawing()

    def run(self):
        while not window_should_close():
            self.draw()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()