import pygame
from settings import *


class rock(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class fuelstation(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Load sprite sheet
        self.sprite_sheet = pygame.image.load("graphics/test/fuelstationm.png").convert_alpha()
        # Define area of image to be cut out (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 47, 64)
        # Create subsurface of the sprite sheet
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # Rotate the image by 45 degrees
        self.image = pygame.transform.rotate(self.background_image, 270)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class mine(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Load sprite sheet
        self.sprite_sheet = pygame.image.load("graphics/test/mine.png").convert_alpha()
        # Define area of image to be cut out (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 500, 500)
        # Create subsurface of the sprite sheet
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # Rotate the image by 45 degrees
        self.image = pygame.transform.rotate(self.background_image, 0)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class ziel(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Load sprite sheet
        self.sprite_sheet = pygame.image.load("graphics/test/ziel.png").convert_alpha()
        # Define area of image to be cut out (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 500, 500)
        # Create subsurface of the sprite sheet
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # Rotate the image by 45 degrees
        self.image = pygame.transform.rotate(self.background_image, 0)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

class busch(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/spritesheet2.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class ground(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/spritesheet2.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(192, 192, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(64, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(128, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(192, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street5(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street6(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(64, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street7(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(128, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class street8(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_ou.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(192, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)

class curve2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(64, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(128, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(192, 0, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve5(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(0, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve6(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(64, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve7(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(128, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)


class curve8(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Hintergrund laden
        self.sprite_sheet = pygame.image.load("graphics/street_lokv.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, height)
        self.ground_rect = pygame.Rect(192, 64, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.ground_rect)
        # image-Attribut setzen
        self.image = self.background_image
        self.rect = self.image.get_rect(topleft=pos)