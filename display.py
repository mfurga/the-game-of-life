# -*- coding: utf-8 -*-

import pygame

__all__ = ("Display")

WHITE = pygame.Color(255, 255, 255, 255)
BLACK = pygame.Color(0, 0, 0, 255)

class Display(object):

  def __init__(self, width: int = 48, height: int = 32, scale: int = 10,
               caption: str = "") -> None:
    self.width = width * scale
    self.height = height * scale
    self.scale = scale
    self.caption = caption

    self._live = BLACK
    self._dead = WHITE

    self.__init_display()

  def __init_display(self) -> None:
    pygame.display.init()
    pygame.display.set_caption(self.caption)

    self.surface = pygame.display.set_mode((self.width, self.height), 0, 8)
    self.clear_surface()

  def __translate_point(self, point: tuple) -> tuple:
    return (point[0] * self.scale, point[1] * self.scale)

  def __validate_point(self, point: tuple) -> bool:
    return 0 <= point[0] and point[0] < self.width and \
           0 <= point[1] and point[1] < self.height

  def __draw_point(self, point: tuple, color: pygame.Color) -> bool:
    point = self.__translate_point(point)
    if not self.__validate_point(point):
      return False
    pygame.draw.rect(self.surface, color, (*point, self.scale, self.scale))
    return True

  def clear_surface(self) -> None:
    self.surface.fill(self._dead)
    self.commit()

  def set_point(self, point: tuple) -> bool:
    return self.__draw_point(point, self._live)

  def clear_point(self, point: tuple) -> bool:
    return self.__draw_point(point, self._dead)

  def get_point(self, point: tuple) -> int:
    point = self.__translate_point(point)
    if not self.__validate_point(point):
      return -1
    color = self.surface.get_at(point)
    return 1 if color == self._live else 0

  def count_live_neighbours(self, point: tuple) -> int:
    neighbours = -1 if self.get_point((point[0], point[1])) == 1 else 0
    for x in (-1, 0, 1):
      for y in (-1, 0, 1):
        if self.get_point((point[0] + x, point[1] + y)) == 1:
          neighbours += 1
    return neighbours

  def commit(self) -> None:
    pygame.display.flip()
