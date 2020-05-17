# -*- coding: utf-8 -*-

from display import Display

from typing import List
import pygame
import sys
import time

__all__ = ("Game")

class Game(object):

  def __init__(self, config) -> None:
    self.display = Display(**config["display"])
    self.delay = config["delay"]

    self.__init_points(config["points"])

  def __init_points(self, points: List[tuple]) -> None:
    for point in points:
      self.display.set_point(point)
    self.display.commit()

  def __start_check_exit(self) -> bool:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return True
    return False

  def start(self) -> None:
    while True:
      if self.__start_check_exit():
        sys.exit(0)

      self.proccess_next_generation()
      time.sleep(self.delay)

  def proccess_next_generation(self):
    dead = []
    live = []

    for x in range(0, self.display.width // self.display.scale):
      for y in range(0, self.display.height // self.display.scale):
        live_neighbours = self.display.count_live_neighbours((x, y))

        if live_neighbours == 3 and self.display.get_point((x, y)) == 0:
          live.append((x, y))

        if live_neighbours not in (2, 3) and self.display.get_point((x, y)) == 1:
          dead.append((x, y))

    for point in live:
      self.display.set_point(point)

    for point in dead:
      self.display.clear_point(point)

    self.display.commit()
