from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from alien import Alien
import game_function as gf
import pygame
from pygame.sprite import Group


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # alien = Alien(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # gf.update_aliens(ai_settings, ship, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens,bullets,play_button)


run_game()
