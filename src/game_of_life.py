#!/bin/env python3

import argparse
from entities.engine import Engine


def main():

    parser = argparse.ArgumentParser(description="Game of Life")
    parser.add_argument("--grid-size", dest="grid_size", default=100, type=int)

    args = parser.parse_args()

    engine = Engine(args.grid_size)

    engine.start()

if __name__ == "__main__":
    main()