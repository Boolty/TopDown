import pygame, sys
from settings import *
from objekt import *
from player import Player
from enemy import AI
from debug import debug


class Level:
    def __init__(self, background):
        self.background = background
        self.ai_sprites = pygame.sprite.Group()
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # create the bars surface
        self.fuel_surface = pygame.Surface((120, 20))
        self.cargo_surface = pygame.Surface((120, 20))

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    rock((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'a':
                    AI((x, y), [self.visible_sprites, self.ai_sprites], self.obstacle_sprites, self.background)
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.background)
                elif col == 's1':
                    street1((x, y), [self.visible_sprites])
                elif col == 's2':
                    street2((x, y), [self.visible_sprites])
                elif col == 's3':
                    street3((x, y), [self.visible_sprites])
                elif col == 's4':
                    street4((x, y), [self.visible_sprites])
                elif col == 's5':
                    street5((x, y), [self.visible_sprites])
                elif col == 's6':
                    street6((x, y), [self.visible_sprites])
                elif col == 's7':
                    street7((x, y), [self.visible_sprites])
                elif col == 's8':
                    street8((x, y), [self.visible_sprites])
                elif col == 'c1':
                    curve1((x, y), [self.visible_sprites])
                elif col == 'c2':
                    curve2((x, y), [self.visible_sprites])
                elif col == 'c3':
                    curve3((x, y), [self.visible_sprites])
                elif col == 'c4':
                    curve4((x, y), [self.visible_sprites])
                elif col == 'c5':
                    curve5((x, y), [self.visible_sprites])
                elif col == 'c6':
                    curve6((x, y), [self.visible_sprites])
                elif col == 'c7':
                    curve7((x, y), [self.visible_sprites])
                elif col == 'c8':
                    curve8((x, y), [self.visible_sprites])
                elif col == 'g':
                    ground((x, y), [self.visible_sprites])
                elif col == 'fs':
                    fuelstation((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'm':
                    mine((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'z':
                    ziel((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'b':
                    busch((x, y), [self.visible_sprites, self.obstacle_sprites])

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)

        font = pygame.font.Font(None, 24)
        frontend = pygame.font.Font(None, 200)
        fuel_text = font.render(f"FUEL: {int(self.player.fuel)}", True, (255, 255, 255))
        cargo_text = font.render(f"CARGO: {self.player.cargo}", True, (255, 255, 255))
        self.fuel_surface.fill((0, 0, 0))
        self.cargo_surface.fill((0, 0, 0))
        self.fuel_surface.blit(cargo_text, (10, 0))  # Position of cargo text is below fuel text
        self.cargo_surface.blit(fuel_text, (10, 0))
        offset_pos = (10, 30)
        offset_pos_c = (10, 50)
        self.display_surface.blit(self.fuel_surface, offset_pos)
        self.display_surface.blit(self.cargo_surface, offset_pos_c)

        self.visible_sprites.update(self.player)  # Player als Parameter übergeben
        self.ai_sprites.update(self.player)  # Player als Parameter übergeben

        if self.player.fuel <= 0 or self.player.cargo <= 0: # Check if player's fuel is less than or equal to 0
            game_over_text = frontend.render("GAME OVER", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=self.display_surface.get_rect().center)
            self.display_surface.blit(game_over_text, game_over_rect)
            pygame.display.update()
            pygame.time.delay(2000)

            #pygame.quit()
            #sys.exit()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # sort sprites by y-coordinate
        sorted_sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)

        # draw street sprites first
        street_sprites = []
        for i in range(1, 9):
            street_sprites.extend([sprite for sprite in sorted_sprites if isinstance(sprite, globals()[f"street{i}"])])
        for sprite in street_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        # draw street sprites first
        curve_sprites = []
        for i in range(1, 9):
            curve_sprites.extend(
                [sprite for sprite in sorted_sprites if isinstance(sprite, globals()[f"street{i}"])])
        for sprite in curve_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        # draw curve sprites after street sprites
        curve_sprites = []
        for i in range(1, 9):
            curve_sprites.extend(
                [sprite for sprite in sorted_sprites if isinstance(sprite, globals()[f"curve{i}"])])
        for sprite in curve_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        # draw other sprites after ground
        # Nichts eintragen sonst kein Bild
        for sprite in sorted_sprites:
            if not isinstance(sprite, (street1, street2, street3, street4, street5, street6, street7, street8, ground, curve1,
                                       curve2, curve3, curve4, curve5, curve6, curve7, curve8)):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)

