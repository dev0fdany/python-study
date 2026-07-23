from settings import *
from sprites import Dino, MovingSprite
from custom_timer import Timer

class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME)
        init_audio_device()
        set_target_fps(FPS)
        self.import_assets()
        self.sprites = []
        self.background = []
        self.dino = Dino(
            self.assets["player_run"],
            self.assets["player_jump"],
            Vector2(100, FLOOR_LINE),
            self.audio["jump"]
            ) 
        self.sprites.append(self.dino)
        self.timers = {
            "obstacle": Timer(2, self.spawn_obs, True, True),
            "cloud": Timer(3, self.spawn_cloud, True, True),
            "floor": Timer(2, self.spawn_floor, True, True),
            "floor_line": Timer(0.2, self.spawn_floor_lines, True, True)
        }

    def import_assets(self):
        self.assets = {
            "player_run" : [load_texture(join("DINO","assets","dino",f"run{i}.png")) for i in range(2)],
            "player_jump": load_texture(join("DINO","assets","dino","jump.png")),
            "cactus_textures": [load_texture(join("DINO","assets","cactii",f"cactus{i}.png")) for i in range(4)],
            "cloud_textures": [load_texture(join("DINO","assets","clouds",f"cloud{i}.png")) for i in range(4)],
            "floor_textures": [load_texture(join("DINO","assets","floor",f"floor{i}.png")) for i in range(4)]
        }
        self.audio = {
           "jump": load_sound(join("DINO","audio","jump.wav"))
        }

    def spawn_cloud(self):
        cloud = MovingSprite(
            choice(self.assets["cloud_textures"]),
            Vector2(WINDOW_WIDTH, FLOOR_LINE - randint(160,240)),
            randint(80,120)
        )
        self.background.append(cloud)

    def spawn_floor(self):
        floor = MovingSprite(
            choice(self.assets["floor_textures"]),
            Vector2(WINDOW_WIDTH+ randint(-10,110), FLOOR_LINE+40),
            300
        )
        self.background.append(floor)
        self.timers["floor"].duration = randint( 1, 3)

    def spawn_floor_lines(self):
        floor_line_texture = gen_image_color(randint(2,8), 2, MAIN_COLOR)
        line_texture = load_texture_from_image(floor_line_texture)
        floor_lines = MovingSprite(
            line_texture,
            Vector2(WINDOW_WIDTH, FLOOR_LINE + 160 + randint(-10, 30)),
            300
        )
        self.background.append(floor_lines)

    def spawn_obs(self):
        sprite = MovingSprite(
            choice(self.assets["cactus_textures"]),
            Vector2(WINDOW_WIDTH + get_random_value(20,100), FLOOR_LINE),
            300
        )
        self.sprites.append(sprite)

    def update(self, dt):
        for sprite in self.sprites + self.background:
            sprite.update(dt)
        for timer in self.timers.values():
            timer.update()

    def draw(self):
        begin_drawing()
        clear_background(WHITE)

        draw_line_ex(
            Vector2(0,FLOOR_LINE+120),
            Vector2(1280,FLOOR_LINE+120),
            10 ,
            MAIN_COLOR
        )
        for bg in self.background:
            bg.draw()
        for sprite in self.sprites:
            sprite.draw()
        end_drawing()

    def run(self):
        while not window_should_close():
            dt = get_frame_time()
            self.draw()
            self.update(dt)


if __name__ == "__main__":
    game = Game()
    game.run()