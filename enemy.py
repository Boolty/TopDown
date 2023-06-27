import pygame, math
from settings import *


class AI(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, background):
        super().__init__(groups)
        self.background = background
        self.font = pygame.font.SysFont("Arial", 24)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/enemy/heli-removebg-preview.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 241, 209)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.speed = ENEMEY_SPEED

        self.obstacle_sprites = obstacle_sprites

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.cargo = max(player.cargo - ENEMEY_STOLE, 0)  # subtract 20 cargo from the player

        if self.rect.colliderect(player.rect):
            # AI hat den Spieler erreicht
            self.direction = pygame.math.Vector2(0, 0)
        else:
            # Berechne die Entfernung zum Spieler
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < ENEMEY_RANGE:
                # Der Spieler ist in der Nähe, bewege sich auf ihn zu
                self.direction = pygame.math.Vector2(dx, dy)
            else:
                # Der Spieler ist zu weit weg, bewege sich nicht
                self.direction = pygame.math.Vector2(0, 0)

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        movement_x = self.direction.x * self.speed
        movement_y = self.direction.y * self.speed

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
