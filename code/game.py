#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(700, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events/verifique todos os eventos
            # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #  pygame.quit()  # Close screen/fecha janela
            #        quit()  # end pygame/fecha pygame
