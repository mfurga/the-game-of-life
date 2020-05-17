#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game import Game
import random

defaults = {
  "delay": 0.1,

  "display": {
    "width": 48,
    "height": 32,
    "scale": 10,
    "caption": "Conway's Game of Life"
  }
}

if __name__ == "__main__":
  count = 1000
  xs = [random.randint(0, defaults["display"]["width"]) for _ in range(count)]
  ys = [random.randint(0, defaults["display"]["height"]) for _ in range(count)]
  points = list(zip(xs, ys))

  defaults["points"] = points

  game = Game(defaults)
  game.start()
