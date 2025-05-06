"""
Code to load in a spritesheet. helper code for visualization
"""

import pygame


class SpriteSheet:
    """
    Helper code to load in the SpriteSheet. Created with help
    from the tutorial by Coding with Rus on youtube
    """

    # function to load in just one sprite from the spritesheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):
        """
            this takes one image from the spritesheet and loads it onto its own surface

        Args:
            frame: a int saying which sprite you want to load in
            width: a int defining the width of the loaded in image
            height: a int defining the hight of the loaded in image
            scale: an int describing the scale of the loaded in image

        Returns:
            a surface with a loaded sprite from the sprite sheet
        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image
