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

    def update(self, dt):
        self.time_since_last_update += dt
        self.snake.input()
        if self.time_since_last_update >= self.time_interval:
            self.snake.update(dt)
            self.check_food_collision()
            self.time_since_last_update = 0

    def run(self):
        while not window_should_close():
            dt = get_frame_time() 
            self.draw()
            self.update(dt)

if __name__ == "__main__":
    game = Game()
    game.run()