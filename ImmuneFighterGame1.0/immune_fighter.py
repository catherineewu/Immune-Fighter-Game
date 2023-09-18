"""IMPORTS: Pygame, """
import pygame
from immune_fighter_variables import Theme
import immune_fighter_cells

"""INITIATE: Pygame, Screen, Caption"""
pygame.init()
screen = pygame.display.set_mode((800, 800))  # Create screen
pygame.display.set_caption("Immune Fighter 1.0")  # Title for game window
clock = pygame.time.Clock()


def check_hover(area, mouse_pos):
    if (area[0] <= mouse_pos[0] <= area[2]) and (area[1] <= mouse_pos[1] <= area[3]):
        return True
    else:
        return False


def display_menu(previous_screen, mouse_over=None):  # Work on mouse over menu option to change button
    screen.blit(Theme.title_mainmenu.default, Theme.title_mainmenu.coord)

    if mouse_over is not None:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    if previous_screen is not None:
        if mouse_over == "Return":
            screen.blit(Theme.icon_return.clicked, Theme.icon_return.coord)
        else:
            screen.blit(Theme.icon_return.default, Theme.icon_return.coord)
    if mouse_over == "New Game":
        screen.blit(Theme.button_newgame.clicked, Theme.button_newgame.coord)
    else:
        screen.blit(Theme.button_newgame.default, Theme.button_newgame.coord)
    if mouse_over == "Load Game":
        screen.blit(Theme.button_loadgame.clicked, Theme.button_loadgame.coord)
    else:
        screen.blit(Theme.button_loadgame.default, Theme.button_loadgame.coord)
    if mouse_over == "Save Game":
        screen.blit(Theme.button_savegame.clicked, Theme.button_savegame.coord)
    else:
        screen.blit(Theme.button_savegame.default, Theme.button_savegame.coord)
    if mouse_over == "Quit":
        screen.blit(Theme.button_quit.clicked, Theme.button_quit.coord)
    else:
        screen.blit(Theme.button_quit.default, Theme.button_quit.coord)


def main():

    """GAME WINDOW LOOP"""
    running = True
    quit_type = None
    current_screen = "Main Menu"
    previous_screen = 1
    current_background = None

    while running:
        screen.fill(Theme.seagreen.rgb)
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(Theme.text_copyright.white, Theme.text_copyright.coord)

        """Separate code by screens of gameplay."""

        """(1) MAIN MENU:
            - When opening game, display.
            - Objects displayed: Game Title, Main Menu Title, New Game Button, Load Game Button, Save Game Button,
                Quit Button
            - Functions used: display_menu(), 
            - User interactions: click on 4 buttons to start new game, load game from saved data, save data from
                current game, quit, or return to previous screen"""
        if current_screen == "Main Menu":

            if (previous_screen is not None) and (check_hover(Theme.icon_return.area, mouse_pos)):
                display_menu(previous_screen, mouse_over="Return")
            elif check_hover(Theme.button_newgame.area, mouse_pos):
                display_menu(previous_screen, mouse_over="New Game")
            elif check_hover(Theme.button_loadgame.area, mouse_pos):
                display_menu(previous_screen, mouse_over="Load Game")
            elif check_hover(Theme.button_savegame.area, mouse_pos):
                display_menu(previous_screen, mouse_over="Save Game")
            elif check_hover(Theme.button_quit.area, mouse_pos):
                display_menu(previous_screen, mouse_over="Quit")
            else:
                display_menu(previous_screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_type = "pygame.QUIT"
                    running = False  # FIXME: Remove this when set up closing window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_type = "pygame.QUIT"
                running = False  # FIXME: Remove this when set up closing window
                # pygame.quit() FIXME: Implement this code further down
                # sys.exit()

        """HANDLING CLOSING WINDOW:
        if quit_type == "pygame.QUIT" etc. etc. for handling closing window
            running = False
            pygame.quit()
            sys.exit()
        """

        pygame.display.update()  # Updates display window, FIXME: might change location
        clock.tick(60)  # Limits frame rate to 60 FPS


if __name__ == "__main__":
    main()


