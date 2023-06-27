import pygame
import shutil
import os
import sys, threading
from settings import *
from level import Level
from background import Background

class Game:
    def __init__(self):
        # Load a font for displaying text
        self.font = pygame.font.SysFont("Arial", 32)
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDHT, HEIGHT))
        self.background_surface = pygame.Surface((WIDHT, HEIGHT))
        pygame.display.set_caption('AromaStyle')
        # hintergund laden
        self.sprite_sheet = pygame.image.load("graphics/spritesheet2.png").convert_alpha()
        # Bereich des Bildes festlegen, das ausgeschnitten werden soll (x, y, width, heighth)
        self.sprite_rect = pygame.Rect(1280, 704, 64, 64)
        # Ausschnitt aus dem Sprite Sheet erstellen
        self.background_image = self.sprite_sheet.subsurface(self.sprite_rect)

        self.background = Background(self.background_image)

        self.clock = pygame.time.Clock()
        self.level = Level(self.background)

        # Definition der Gewinnanimation

    def show_win_animation(screen):
        # Hintergrund anzeigen
        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))  # Schwarzer Hintergrund
        screen.blit(background, (0, 0))

        # Text anzeigen
        font = pygame.font.SysFont("Arial", 48)
        text = font.render("Gewonnen!", True, (255, 255, 255))  # Weißer Text
        text_rect = text.get_rect(center=screen.get_rect().center)
        screen.blit(text, text_rect)

        # Bildschirm aktualisieren
        pygame.display.flip()
        pygame.time.wait(2000)  # Animation für 2 Sekunden anzeigen

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.background.draw(self.screen)

            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

# Initialize pygame
pygame.init()

# Set window size
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)

# Set font
font = pygame.font.Font(None, 36)

# Define menu options
menu_items = ["Start", "Einstellungen", "Schließen"]
selected_item = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move selection up
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                # Move selection down
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                # Execute selected item
                if selected_item == 0:
                    # Start game
                    game = Game()
                    game.run()
                elif selected_item == 1:
                    print('Einstellungen')
                    print('#############')
                    print('Default Settings:')
                    print('[0]Speichern \n', '### Auflösung ###\n', '[1]WIDHT = 1280\n', '[2]HEIGHT = 720\n',
                          '[3]FPS = 60\n', '### Spieler Einstellungen ###\n', '[4]PLAYER_SPEED = 5\n',
                          '[5]PLAYER_FUEL = 400\n', '[6]PLAYER_FUEL_DEPLETION_RATE = 0.1\n', '[7]PLAYER_FUEL_REGEN_RATE = 0.5\n',
                          '[8]PLAYER_CARGO = 150\n', '#### Enemey settings ###\n', '[9]ENEMEY_SPEED = 2\n', '[10]ENEMEY_STOLE = 0.1\n',
                          '[11]ENEMEY_RANGE = 500\n')
                    while True:
                        value = 0
                        choos = input('Ändern 0-11: ')
                        if int(choos) == 1:
                            print('Current Value: ', WIDHT)
                            value = int(input('WIDHT: '))
                            WIDHT = value
                            print('Change Value: ', WIDHT)
                        elif int(choos) == 2:
                            print('Current Value: ', HEIGHT)
                            value = int(input('HEIGHT: '))
                            HEIGHT = value
                            print('Change Value: ', HEIGHT)
                        elif int(choos) == 3:
                            print('Current Value: ', FPS)
                            value = int(input('FPS: '))
                            FPS = value
                            print('Change Value: ', FPS)
                        elif int(choos) == 4:
                            print('Current Value: ', PLAYER_SPEED)
                            value = int(input('PLAYER_SPEED: '))
                            PLAYER_SPEED = value
                            print('Change Value: ', PLAYER_SPEED)
                        elif int(choos) == 5:
                            print('Current Value: ', PLAYER_FUEL)
                            value = int(input('PLAYER_FUEL: '))
                            PLAYER_FUEL = value
                            print('Change Value: ', PLAYER_FUEL)
                        elif int(choos) == 6:
                            print('Current Value: ', PLAYER_FUEL_DEPLETION_RATE)
                            value = int(input('PLAYER_FUEL_DEPLETION_RATE: '))
                            PLAYER_FUEL_DEPLETION_RATE = value
                            print('Change Value: ', PLAYER_FUEL_DEPLETION_RATE)
                        elif int(choos) == 7:
                            print('Current Value: ', PLAYER_FUEL_REGEN_RATE)
                            value = int(input('PLAYER_FUEL_REGEN_RATE: '))
                            PLAYER_FUEL_REGEN_RATE = value
                            print('Change Value: ', PLAYER_FUEL_REGEN_RATE)
                        elif int(choos) == 8:
                            print('Current Value: ', PLAYER_CARGO)
                            value = int(input('PLAYER_CARGO: '))
                            PLAYER_CARGO = value
                            print('Change Value: ', PLAYER_CARGO)
                        elif int(choos) == 9:
                            print('Current Value: ', ENEMEY_SPEED)
                            value = int(input('ENEMEY_SPEED: '))
                            ENEMEY_SPEED = value
                            print('Change Value: ', ENEMEY_SPEED)
                        elif int(choos) == 10:
                            print('Current Value: ', ENEMEY_STOLE)
                            value = int(input('ENEMEY_STOLE: '))
                            ENEMEY_STOLE = value
                            print('Change Value: ', ENEMEY_STOLE)
                        elif int(choos) == 11:
                            print('Current Value: ', ENEMEY_RANGE)
                            value = int(input('ENEMEY_RANGE: '))
                            ENEMEY_RANGE = value
                            print('Change Value: ', ENEMEY_RANGE)
                        elif choos == '0':
                            # Define the file paths
                            original_file = 'settings.py'
                            new_file = 'nwsettings.py'

                            # Read the contents of the original file
                            with open(original_file, 'r') as f:
                                contents = f.readlines()

                            # Modify the contents as desired
                            contents[1] = 'WIDHT = ' + str(WIDHT) + '\n'
                            contents[2] = 'HEIGHT = ' + str(HEIGHT) + '\n'
                            contents[3] = 'FPS = ' + str(FPS) + '\n'
                            contents[9] = 'PLAYER_SPEED = ' + str(PLAYER_SPEED) + '\n'
                            contents[10] = 'PLAYER_FUEL = ' + str(PLAYER_FUEL) + '\n'
                            contents[11] = 'PLAYER_FUEL_DEPLETION_RATE = ' + str(PLAYER_FUEL_DEPLETION_RATE) + '\n'
                            contents[12] = 'PLAYER_FUEL_REGEN_RATE = ' + str(PLAYER_FUEL_REGEN_RATE) + '\n'
                            contents[13] = 'PLAYER_CARGO = ' + str(PLAYER_CARGO) + '\n'
                            contents[16] = 'ENEMEY_SPEED = ' + str(ENEMEY_SPEED) + '\n'
                            contents[17] = 'ENEMEY_STOLE = ' + str(ENEMEY_STOLE) + '\n'
                            contents[18] = 'ENEMEY_RANGE = ' + str(ENEMEY_RANGE) + '\n'

                            # Write the modified contents to a new file
                            with open(new_file, 'w') as f:
                                f.writelines(contents)

                            # Copy the original file's permissions to the new file
                            shutil.copymode(original_file, new_file)

                            # Rename the original file
                            os.rename(original_file, 'original_file_backup.py')

                            # Rename the new file to the original file's name
                            os.rename(new_file, original_file)

                            break

                elif selected_item == 2:
                    # Exit game
                    pygame.quit()
                    sys.exit()

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw menu items
    for i, item in enumerate(menu_items):
        text = font.render(item, True, (0, 0, 0))
        if i == selected_item:
            # Highlight selected item
            pygame.draw.rect(screen, (100, 100, 100), (100, 100 + i * 50, text.get_width() + 10, text.get_height() + 10))
        screen.blit(text, (105, 105 + i * 50))

    # Update screen
    pygame.display.update()
