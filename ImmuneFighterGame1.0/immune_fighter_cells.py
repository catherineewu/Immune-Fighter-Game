import os
import pygame
cwd = os.getcwd()


class Cells:
    """PARAMETERS:
        number (int): # of cell in order of unlock, position in cell index
        cell_name (str): name of type of cell, ex: 'Macrophage'
        char_name (str): name of cell character, ex: 'Margaret'
        level_unlocked (int): level of game completed to unlock cell type
        animation (str): different animations (to be made)

        health (int): # of health points (damage withstood before death)
        move (class): default attack/defense move
        special_move (class - Optional): special attack/defense move"""
    def __init__(self, number, cell_name, char_name, level_unlocked, animation, health):
        self.number, self.level_unlocked, self.health = number, level_unlocked, health
        self.cell_name, self.char_name, self.animation = cell_name, char_name, animation

        self.frame1 = pygame.image.load(f'{cwd}/Graphics/if_cell_{cell_name}_1.png')
        self.frame2 = pygame.image.load(f'{cwd}/Graphics/if_cell_{cell_name}_2.png')
        self.frame3 = pygame.image.load(f'{cwd}/Graphics/if_cell_{cell_name}_3.png')

        self.dimensions = (self.frame1.get_width(), self.frame1.get_height())

