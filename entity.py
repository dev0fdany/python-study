from settings import *

class Food:
    def __init__(self, food_texture):
        self.position = self.get_random_cell()
        self.food_texture = food_texture

    def draw(self):
        draw_texture(self.food_texture, int(OFF_SET+ self.position.x * CELL_SIZE), int(OFF_SET+ self.position.y * CELL_SIZE), COLOR_FOOD)

    def get_random_cell(self):
        x = int(get_random_value(0, 24))
        y = int(get_random_value(0, 24))
        return Vector2(x,y)

    def get_position(self, snake_body):
        self.snake_body = snake_body
        is_colliding = True
        while is_colliding:
            self.food_future_position = self.get_random_cell()
            is_colliding = False
            for body_segment in self.snake_body:
                if vector2_equals(body_segment, self.food_future_position):
                    is_colliding = True
                    break
        return self.food_future_position


class Snake():
    def __init__(self):
        self.body_position = self.get_position() #list
        self.direction  = Vector2(1, 0)

    def draw(self):
        for body_pos in self.body_position:
            body_rec = Rectangle(int(OFF_SET+ body_pos.x * CELL_SIZE), int(OFF_SET+ body_pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            draw_rectangle_rounded(body_rec, 0.3, 5, COLOR_FR)

    def get_position(self):
        body = [Vector2(4,9),Vector2(5,9),Vector2(6,9)]
        return body

    def grow(self):
        self.body_position.append(vector2_add(self.body_position[-1], self.direction))

    def check_collision_head(self):
        self.headless_body = self.body_position.copy()
        self.headless_body.pop()
        is_colliding = True
        while is_colliding:
            is_colliding = False
            for body_segment in self.headless_body:
                if vector2_equals(body_segment, self.body_position[-1]):
                    is_colliding = True
                    return True

    def reset(self):
        self.body_position = self.get_position() #list
        self.direction  = Vector2(1, 0)

    def update(self, dt):
        next_head_pos = vector2_add(self.body_position[-1], self.direction)
        if next_head_pos.x < 0 or next_head_pos.x >= CELL_COUNT:
            return False
        if next_head_pos.y < 0 or next_head_pos.y >= CELL_COUNT:
            return False
        self.body_position.pop(0)
        self.body_position.append(next_head_pos)
        return True


    def input(self):
        if is_key_pressed(rl.KEY_W) and self.direction.y != 1:
            self.direction = Vector2(0, -1)
        if is_key_pressed(rl.KEY_A) and self.direction.x != 1:
            self.direction = Vector2(-1, 0)
        if is_key_pressed(rl.KEY_S) and self.direction.y != -1:
            self.direction = Vector2(0, 1)
        if is_key_pressed(rl.KEY_D) and self.direction.x != -1:
            self.direction = Vector2(1, 0)


