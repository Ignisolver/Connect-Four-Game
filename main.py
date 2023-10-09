from game.game import Game


def main():
    g = Game()
    try:
        g.start_game()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()