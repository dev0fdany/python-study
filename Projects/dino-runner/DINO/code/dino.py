from settings import *
from sprites import Dino, MovingSprite, Score
from custom_timer import Timer

class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME)
        init_audio_device()
        set_target_fps(FPS)
        self.import_assets()
        self.gameover = False
        self.sprites = []
        self.collision_sprites = []
        self.background = []
        self.dino = Dino(
            self.assets["player_run"],
            self.assets["player_jump"],
            Vector2(100, FLOOR_LINE),
            self.audio["jump"]
            ) 
        self.sprites.append(self.dino)
        self.score = Score(self.assets["font"])
        self.timers = {
            "obstacle": Timer(2, self.spawn_obs, True, True),
            "cloud": Timer(3, self.spawn_cloud, True, True),
            "floor": Timer(2, self.spawn_floor, True, True),
            "floor_line": Timer(0.2, self.spawn_floor_lines, True, True)
        }
        play_music_stream(self.audio["music"])

    def import_assets(self):
        self.assets = {
            "player_run" : [load_texture(join("DINO","assets","dino",f"run{i}.png")) for i in range(2)],
            "player_jump": load_texture(join("DINO","assets","dino","jump.png")),
            "cactus_textures": [load_texture(join("DINO","assets","cactii",f"cactus{i}.png")) for i in range(4)],
            "enemy_textures": [load_texture(join("DINO","assets","enemy",f"enemy{i}.png")) for i in range(2)],
            "cloud_textures": [load_texture(join("DINO","assets","clouds",f"cloud{i}.png")) for i in range(4)],
            "floor_textures": [load_texture(join("DINO","assets","floor",f"floor{i}.png")) for i in range(4)],
            "font": load_font_ex(join("DINO","fonts","RETRO_SPACE.ttf"), FONT_SIZE, None, 0)
        }
        self.audio = {
            "music": load_music_stream(join("DINO","audio","music.mp3")),
           "jump": load_sound(join("DINO","audio","jump.wav"))
        }

    def spawn_cloud(self):
        cloud = MovingSprite(
            [choice(self.assets["cloud_textures"])],
            Vector2(WINDOW_WIDTH, FLOOR_LINE - randint(160,240)),
            randint(80,120)
        )
        self.background.append(cloud)

    def spawn_floor(self):
        floor = MovingSprite(
            [choice(self.assets["floor_textures"])],
            Vector2(WINDOW_WIDTH+ randint(-10,110), FLOOR_LINE+40),
            300
        )
        self.background.append(floor)
        self.timers["floor"].duration = randint( 1, 3)

    def spawn_floor_lines(self):
        floor_line_texture = gen_image_color(randint(2,8), 2, MAIN_COLOR)
        line_texture = load_texture_from_image(floor_line_texture)
        floor_lines = MovingSprite(
            [line_texture],
            Vector2(WINDOW_WIDTH, FLOOR_LINE + 160 + randint(-10, 30)),
            300
        )
        self.background.append(floor_lines)

    def spawn_obs(self):
        textures = [choice(self.assets["cactus_textures"])] if get_random_value(1,10) <=7 else self.assets["enemy_textures"]
        sprite = MovingSprite(
            textures,
            Vector2(WINDOW_WIDTH + get_random_value(20,100), FLOOR_LINE),
            300
        )
        self.sprites.append(sprite)
        self.collision_sprites.append(sprite)

    def collision_check(self):
        for sprite in self.collision_sprites:
            player_circle = self.dino.get_collision_circle()
            obs_circle = sprite.get_collision_circle()
            if check_collision_circles(player_circle[0], player_circle[1], obs_circle[0], obs_circle[1]):
                self.gameover = True
    def remove_sprite(self):
        self.sprites = [sprite for sprite in self.sprites if sprite.pos.x > -300]
        self.background = [bg_sprite for bg_sprite in self.background if bg_sprite.pos.x > -300]

    def update(self, dt):
        update_music_stream(self.audio["music"])
        for sprite in self.sprites + self.background:
            sprite.update(dt)
        for timer in self.timers.values():
            timer.update()
        self.collision_check()
        self.remove_sprite()

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
        if not self.gameover:
            self.score.draw(get_time())
            self.final_score = get_time()
        else:
            self.score.draw(self.final_score)

        end_drawing()

    def run(self):
        while not window_should_close():
            dt = get_frame_time()
            self.draw()
            if not self.gameover:
                self.update(dt)
            else:
                self.score.dead()
            if is_key_pressed(rl.KEY_Q):
                exit()


if __name__ == "__main__":
    game = Game()
    game.run()