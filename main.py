from settings import *
from entity import Food, Snake

class Game():
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME)
        set_target_fps(60)
        self.food = Food()
        self.snake = Snake()
        self.time_since_last_update = 0
        self.time_interval = 0.2
        self.is_game_over = False

    def draw(self):
        begin_drawing()
        clear_background(COLOR_BG)
        self.food.draw()
        self.snake.draw()

        end_drawing()

    def check_food_collision(self):
        if vector2_equals(self.snake.body_position[-1], self.food.position):
            self.food.position = self.food.get_position(self.snake.body_position)
            self.snake.grow()

    def check_snake_collision_edges(self):
        if self.snake.body_position[-1].x == CELL_COUNT or self.snake.body_position[-1].x == -1:
            self.is_game_over = True
        if self.snake.body_position[-1].y == CELL_COUNT or self.snake.body_position[-1].y == -1:
            self.is_game_over = True

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
                self.snake.update(dt)
                self.check_food_collision()
                self.check_snake_collision_edges()
                self.check_snake_head_collision()
                self.time_since_last_update = 0
        else:
            self.died()

    def died(self):
        string_text = "YOU DIED!"
        text_width = measure_text(string_text, FONT_SIZE)
        draw_text(string_text, int(750 - text_width / 2) , int(750 / 2),FONT_SIZE, COLOR_FOOD)

    def gameover(self):
        self.snake.reset()
        self.food.position = self.food.get_random_cell()
        self.is_game_over =  True

    def run(self):
        while not window_should_close():
            self.draw()
            dt = get_frame_time() 
            self.update(dt)

if __name__ == "__main__":
    game = Game()
    game.run()