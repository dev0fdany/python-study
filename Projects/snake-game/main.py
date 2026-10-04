from settings import *
from entity import Food, Snake

class Game():
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME)
        init_audio_device()
        set_target_fps(60)
        self.target = load_render_texture(
            2*OFF_SET + GAME_WIDTH,
            2*OFF_SET + GAME_HEIGHT
        )
        self.imports_assets()
        self.food = Food(self.assets["food"])
        self.snake = Snake()
        self.time_since_last_update = 0
        self.time_interval = 0.2
        self.is_game_over = False
        self.score = 0

    def imports_assets(self):
        self.assets = {
            "food": load_texture(join("Graphics","food.png"))
        }
        self.audio = {
            "wall_hit": load_sound(join("Sounds","wall.mp3")),
            "eat": load_sound(join("Sounds","eat.mp3"))
        }

    def draw(self):
        begin_texture_mode(self.target)

        clear_background(COLOR_BG)
        #title - score
        draw_text(GAME_NAME, OFF_SET- 5, 20, FONT_SIZE, COLOR_FR)
        self.Score_string = f"Score: {self.score}"
        draw_text(self.Score_string, OFF_SET- 5, OFF_SET+GAME_HEIGHT+10, FONT_SIZE, COLOR_FR)
        # border
        draw_rectangle_lines_ex(Rectangle(OFF_SET-5, OFF_SET-5, GAME_WIDTH +10, GAME_HEIGHT + 10), 5, COLOR_FR)
        self.food.draw()
        self.snake.draw()
        if self.is_game_over:
            self.died()
        if self.is_game_over:
            self.died()
        end_texture_mode()

        begin_drawing()
        clear_background(BLACK)
        draw_texture_pro(
            self.target.texture,
            Rectangle(
                0,
                0,
                self.target.texture.width,
                -self.target.texture.height
            ),
            Rectangle(
                0,
                0,
                WINDOW_WIDTH,
                WINDOW_HEIGHT
            ),
            Vector2(0,0),
            0,
            WHITE
        )
        end_drawing()

    def check_food_collision(self):
        if vector2_equals(self.snake.body_position[-1], self.food.position):
            self.food.position = self.food.get_position(self.snake.body_position)
            self.score +=1
            self.snake.grow()
            play_sound(self.audio["eat"])

    def check_snake_collision_edges(self):
        if self.snake.body_position[-1].x == CELL_COUNT or self.snake.body_position[-1].x == -1:
            self.is_game_over = True
            play_sound(self.audio["wall_hit"])
        if self.snake.body_position[-1].y == CELL_COUNT or self.snake.body_position[-1].y == -1:
            self.is_game_over = True
            play_sound(self.audio["wall_hit"])

    def check_snake_head_collision(self):
        if self.snake.check_collision_head():
            self.is_game_over = True


    def update(self, dt):
        if is_key_pressed(rl.KEY_Q):
            close_window()
        if not self.is_game_over:
            self.time_since_last_update += dt
            self.snake.input()
            if self.time_since_last_update >= self.time_interval:
                is_alive = self.snake.update(dt)
                if not is_alive:
                    self.is_game_over = True
                    play_sound(self.audio["wall_hit"])
                self.check_food_collision()
                self.check_snake_collision_edges()
                self.check_snake_head_collision()
                self.time_since_last_update = 0
        else:
            if is_key_pressed(rl.KEY_SPACE):
                self.gamereset()

    def died(self):
        string_text = "YOU DIED!"
        strings_hint = "PRESS SPACE TO RESTART."
        text_width = measure_text(string_text, FONT_SIZE)
        text_hint_width = measure_text(strings_hint, FONT_SIZE)
        draw_text(string_text, int((GAME_WIDTH+ 2*OFF_SET - text_width) / 2) , int(GAME_HEIGHT / 2),FONT_SIZE, COLOR_FOOD)
        draw_text(strings_hint, int((2*OFF_SET+ GAME_WIDTH - text_hint_width) / 2) , int((OFF_SET+ GAME_HEIGHT) / 2),FONT_SIZE, COLOR_FR)

    def gamereset(self):
        self.snake.reset()
        self.food.position = self.food.get_random_cell()
        self.is_game_over =  False
        self.score = 0

    def run(self):
        while not window_should_close():
            dt = get_frame_time() 
            self.update(dt)
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()