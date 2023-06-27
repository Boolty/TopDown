import pygame, math
from settings import *
from objekt import fuelstation, mine, ziel


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, background):
        super().__init__(groups)
        self.background = background
        self.sprite_sheet = pygame.image.load("graphics/player/playeru.png").convert_alpha()
        self.ground_rect = pygame.Rect(0, 0, 32, 109)
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.fuel = PLAYER_FUEL
        self.cargo = PLAYER_CARGO
        self.fuel_depletion_rate = PLAYER_FUEL_DEPLETION_RATE
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.obstacle_sprites = obstacle_sprites

        # load the run animation frames for each direction
        self.run_frames = {
            (0, 1): [
                pygame.image.load("graphics/player/playeru.png").convert_alpha(),
                # add more frames as needed
            ],
            (0, -1): [
                pygame.image.load("graphics/player/player.png").convert_alpha(),
                # add more frames as needed
            ],
            (1, 0): [
                pygame.image.load("graphics/player/playerR.png").convert_alpha(),
                # add more frames as needed
            ],
            (-1, 0): [
                pygame.image.load("graphics/player/playerl.png").convert_alpha(),
                # add more frames as needed
            ]
        }

        # set the initial frame and animation direction
        self.current_anim = self.run_frames[(1, 0)]
        self.frame_index = 0
        self.image = self.current_anim[self.frame_index]
        self.animation_speed = 0.1
        self.last_frame_update_time = pygame.time.get_ticks()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            print('y ',self.direction.y)
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            print(self.direction.x)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Wenn der Spieler sich bewegt, reduziert sich seine Ausdauer
        if self.direction.x != 0 or self.direction.y != 0:
            self.fuel = max(self.fuel - self.fuel_depletion_rate, 0)

        # Wenn die Ausdauer des Spielers auf 0 ist, kann er sich nicht mehr bewegen
        if self.fuel == 0:
            self.direction = pygame.math.Vector2(0, 0)

        movement_x = self.direction.x * speed
        movement_y = self.direction.y * speed

        pos_x = self.hitbox.x
        pos_y = self.hitbox.y

        self.hitbox.x += movement_x
        self.collision('horizontal')
        self.hitbox.y += movement_y
        self.collision('vertical')
        self.rect.center = self.hitbox.center

        actual_movement_x = self.hitbox.x - pos_x
        actual_movement_y = self.hitbox.y - pos_y

        self.background.move(-actual_movement_x, -actual_movement_y)

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if isinstance(sprite, fuelstation):  # Wenn der Spieler mit einem fuelstation-Objekt kollidiert
                        self.fuel = min(self.fuel + PLAYER_FUEL,
                                           PLAYER_FUEL)  # Erhöhe die Fuel um STREET1_FUEL_GAIN oder fülle sie auf 100%, falls der Wert größer als 100 ist
                    if isinstance(sprite, mine):  # Wenn der Spieler mit einem Street1-Objekt kollidiert
                        self.cargo = min(self.cargo + PLAYER_CARGO,
                                           PLAYER_CARGO)
                    if isinstance(sprite, ziel):  # Wenn der Spieler mit einem Street1-Objekt kollidiert
                        #gewinn animation
                        if self.cargo == 135:
                            pass

                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self, *args):
        # Rest of the update method
        self.input()
        self.move(self.speed)

        # update the animation
        time_now = pygame.time.get_ticks()
        time_since_last_frame = time_now - self.last_frame_update_time
        if time_since_last_frame >= self.animation_speed * 1000:
            self.last_frame_update_time = time_now

            # Update animation frames based on player direction
            if self.direction.x > 0:
                self.current_anim = self.run_frames[(1, 0)]
            elif self.direction.x < 0:
                self.current_anim = self.run_frames[(-1, 0)]
            elif self.direction.y > 0:
                self.current_anim = self.run_frames[(0, 1)]
            elif self.direction.y < 0:
                self.current_anim = self.run_frames[(0, -1)]

            self.frame_index += 1
            if self.frame_index >= len(self.current_anim):
                self.frame_index = 0  # reset the frame index if it exceeds the length of the current animation
            self.image = self.current_anim[self.frame_index]
