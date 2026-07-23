from settings import *

class Sprite:
    def __init__(self, texture, pos):
        self.texture = texture
        self.pos = pos

    def draw(self):
        draw_texture_ex(self.texture, self.pos, 0, SCALE, WHITE)

class Dino(Sprite):
    def __init__(self, run_textures, jump_texture, pos, jump_sound):
        self.run_textures = run_textures
        self.jump_texture = jump_texture
        super().__init__(self.run_textures[0],pos)
        self.jump_sound = jump_sound
        self.velocity = 0
        self.gravity = 2000
        self.jump_height = -1250
        self.frame_index = 0

    def update(self, dt):
        self.velocity += self.gravity *dt
        self.pos.y += self.velocity *dt
        if self.pos.y > FLOOR_LINE:
            self.pos.y = FLOOR_LINE
        if is_key_pressed(rl.KEY_SPACE):
            self.velocity = self.jump_height
            play_sound(self.jump_sound)

        self.frame_index += ANIMATION_SPEED *dt 
        if self.frame_index >= len(self.run_textures):
            self.frame_index = 0

    def draw(self):
        if self.pos.y >= FLOOR_LINE:
            self.texture = self.run_textures[int(self.frame_index)] 
        else:
            self.texture = self.jump_texture
        super().draw()

class MovingSprite(Sprite):
    def __init__(self, texture, pos, speed):
        super().__init__(texture, pos)
        self.speed = speed

    def update(self, dt):
        self.pos.x -= self.speed * dt
