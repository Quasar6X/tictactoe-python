import os
import re
import sys
import random as rnd
from quasar6.main.Player import Player
from quasar6.main import Game

P1 = Player(Player.def_name_1)
AI = Player(Player.def_name_2)
field = Game.Field.get_instance()
sounds = ('beep', 'boop', 'bleep', 'bloop')
marks = ('?', '!', '!?', '...', '(ノಠ益ಠ)ノ彡┻━┻', '..・ヾ(。＞＜)シ')


def choose_name():
    P1.set_name(Player.def_name_1)
    name = input("!!!  Do you want to choose a name? (y/n) > ")
    if name == 'y' or name == 'yes':
        P1.set_name(input("Player 1 name: ").strip())
    elif name == 'n' or name == 'no':
        return
    else:
        print("!!!  Please choose yes or no!")
        choose_name()


def restart():
    res = input("!!!  Another round? (y/n) > ")
    res.lower().strip()
    if res == 'y' or res == 'yes':
        field.reset_field()
        run()
        return
    elif res == 'n' or res == 'no':
        exit(0)
    else:
        print("!!!  Please choose yes or no!")
        restart()


def print_standings():
    print(P1.get_name() + " - " + AI.get_name())
    print(" " * (len(P1.get_name()) - 1) + str(P1.get_score()) + " - " + str(AI.get_score()) + "\n")


def help_message():
    print("\n!!!  Valid position values: 1-" + str(field.get_size()))
    print("!!!  Values are to be separated by a comma ',' first is row second is column e.g. '2,3'")
    print("!!!  In order to quit type 'quit' or 'q'")
    print("!!!  In order to reset the scoreboard type 'reset' or 'r'")
    print("!!!  In order to show this help message type 'help' or 'h'\n")


def run():
    pls = "\n!!!  Please retry!"
    if Game.p_turn == "X":
        while True:
            inp = input(P1.get_name() + " > ")
            inp.lower()
            inp.replace(" ", "")
            inp.replace("\t", "")
            if inp == 'q' or inp == 'quit':
                exit(0)
            if inp == 'r' or inp == 'reset':
                P1.set_score(0)
                AI.set_score(0)
                print_standings()
                run()
                return
            if inp == 'h' or inp == 'help':
                help_message()
                run()
                return

            positions = inp.split(",")
            if len(positions) < 2 or not re.match("^[ ]*[1-9](|[0-5])[ ]*,[ ]*[1-9](|[0-5])[ ]*$", inp):
                print("!!!  Invalid position!" + pls)
                run()
                return

            px = int(positions[0])
            py = int(positions[1])
            px -= 1
            py -= 1
            if px < 0 or px > field.get_size() - 1 or py < 0 or py > field.get_size() - 1:
                print("!!!  Invalid position!" + pls)
                run()
                return

            if not field.set_field_symbol(px, py):
                print("!!!  That field already has a symbol: " + field.get_symbol_at(px, py) + pls)
                run()
                return

            field.print_field()
            Game.p_turn = "O"
            break
    else:
        beep = ""
        for x in range(5, 16):
            if x == 0:
                beep += str(rnd.choice(sounds))
            else:
                beep += str(rnd.choice(sounds))
            if x != 15:
                beep += " "

        beep += rnd.choice(marks)
        print(beep.capitalize())
        (m, px, py) = field.max(-2, 2)
        field.set_field_symbol(px, py)
        field.print_field()
        Game.p_turn = "X"

    result = field.is_match()
    if result == "X":
        print(P1.get_name() + " Wins!")
        P1.set_score(P1.get_score() + 1)
        print_standings()
        restart()
        return
    if result == "O":
        print(AI.get_name() + " Wins!")
        AI.set_score(AI.get_score() + 1)
        print_standings()
        restart()
        return
    if result == "draw":
        print("It's a draw!")
        print_standings()
        restart()
        return

    run()


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=148))
os.system("title Tic-Tac-Toe by Quasar6")
print("\n _________    ___      ________                     _________    ________      ________              ", end="")
print("       _________    ________      _______      ")
print("|\\___   ___\\ |\\  \\    |\\   ____\\                   |\\___   ___\\ |\\   __  \\    |\\   ____\\   ", end="")
print("                |\\___   ___\\ |\\   __  \\    |\\  ___ \\     ")
print("\\|___ \\  \\_| \\ \\  \\   \\ \\  \\___|     ____________  \\|___ \\  \\_| \\ \\  \\|\\  \\   \\ \\  ", end="")
print("\\___|     ____________  \\|___ \\  \\_| \\ \\  \\|\\  \\   \\ \\   __/|    ")
print("     \\ \\  \\   \\ \\  \\   \\ \\  \\       |\\____________\\     \\ \\  \\   \\ \\   __  \\   \\ \\  ", end="")
print("\\       |\\____________\\     \\ \\  \\   \\ \\  \\\\\\  \\   \\ \\  \\_|/__  ")
print("      \\ \\  \\   \\ \\  \\   \\ \\  \\____  \\|____________|      \\ \\  \\   \\ \\  \\ \\  \\   \\ \\", end="")
print("  \\____  \\|____________|      \\ \\  \\   \\ \\  \\\\\\  \\   \\ \\  \\_|\\ \\ ")
print("       \\ \\__\\   \\ \\__\\   \\ \\_______\\                      \\ \\__\\   \\ \\__\\ \\__\\   \\ \\", end="")
print("_______\\                      \\ \\__\\   \\ \\_______\\   \\ \\_______\\")
print("        \\|__|    \\|__|    \\|_______|                       \\|__|    \\|__|\\|__|    \\|_______|    ", end="")
print("                   \\|__|    \\|_______|    \\|_______|")
print("                                                                    BY QUASAR6", end="")
print("                                                                v1.0.5\n")

choose_name()
help_message()
print_standings()
run()
