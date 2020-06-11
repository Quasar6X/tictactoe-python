import random as rnd
from quasar6.main.Player import Player
from quasar6.main import Game
from appJar import gui

P1 = Player(Player.def_name_1)
AI = Player(Player.def_name_2)
field = Game.Field.get_instance()
sounds = ('beep', 'boop', 'bleep', 'bloop')
marks = ('?', '!', '!?', '...', ' (ノಠ益ಠ)ノ彡┻━┻', ' ..・ヾ(。＞＜)シ')


def set_player_name():
    string = app.stringBox("Choose a name", "Choose a name, or leave empty for default!")
    if string is None:
        return
    if len(string) > 25:
        app.warningBox("Wrong Player name", "Player name too long! It must not exceed 25 characters.")
        set_player_name()
        return
    if len(string) != 0:
        P1.name = string


def reset_scores():
    AI.score = 0
    P1.score = 0
    app.setLabel("Scores", str(P1.score) + " - " + str(AI.score))


def restart():
    for i in range(field.SIZE):
        for j in range(field.SIZE):
            app.setButtonFg(str(i) + "_" + str(j), "black")
            app.enableButton(str(i) + "_" + str(j))
            field.reset_field()
            app.setButton(str(i) + "_" + str(j), field.FIELD[i][j])


def on_press(name):
    if app.getButton(name) == "_" and Game.p_turn == "X":
        app.setButtonFg(name, "blue")
        app.clearMessage("AI")
        app.setButton(name, "X")
        strings = name.split("_")
        field.set_field_symbol(int(strings[0]), int(strings[1]))
        Game.p_turn = "O"
        if is_win() == "X":
            yesno = app.yesNoBox("You win", "You win!\nAnother round?")
            if yesno:
                restart()
            else:
                exit()
            return
        ai_turn()
        return


def disable_buttons():
    for i in range(field.SIZE):
        for j in range(field.SIZE):
            app.disableButton(str(i) + "_" + str(j))


def is_win():
    result = field.is_match()
    if result == "X":
        P1.score += 1
        disable_buttons()
        app.setLabel("Scores", str(P1.score) + " - " + str(AI.score))
        return "X"
    if result == "O":
        AI.score += 1
        disable_buttons()
        app.setLabel("Scores", str(P1.score) + " - " + str(AI.score))
        return "O"
    if result == "draw":
        disable_buttons()
        return "Draw"
    return False


def ai_turn():
    if Game.p_turn == "O":
        beep = ""
        for x in range(3, 7):
            if x == 0:
                beep += str(rnd.choice(sounds))
            else:
                beep += str(rnd.choice(sounds))
            if x != 6:
                beep += " "

        beep += rnd.choice(marks)
        app.setMessage("AI", "AI: " + beep.capitalize())
        (m, px, py) = field.max(-2, 2)
        field.set_field_symbol(px, py)
        app.setButton(str(px) + "_" + str(py), "O")
        app.setButtonFg(str(px) + "_" + str(py), "red")
        Game.p_turn = "X"
        if is_win() == "O":
            yesno = app.yesNoBox("AI Wins", "AI Wins!\nAnother round?")
            if yesno:
                restart()
            else:
                exit()
            return
        elif is_win() == "Draw":
            yesno = app.yesNoBox("Draw", "It's a draw!\nAnother round?")
            if yesno:
                restart()
            else:
                exit()
            return
        return 


app = gui("Tic-Tac-Toe by Quasar6     Version 1.1", "400x600")
app.setBg("lightyellow")
app.setSticky("news") # noqa
app.setExpand("both") # noqa
app.setFont(size=24)
set_player_name()
for k in range(field.SIZE):
    for n in range(field.SIZE):
        app.addNamedButton(field.FIELD[k][n], str(k) + "_" + str(n), on_press, k, n, 1)
        app.setButtonBg(str(k) + "_" + str(n), "lightyellow")

app.setSticky("s") # noqa
app.setExpand("column") # noqa
app.addEmptyMessage("AI", 3, 0, 3)
app.setMessageAspect("AI", 400)
app.addLabel("Sc", P1.name + " - " + AI.name, 4, 0, 3)
app.addLabel("Scores", str(P1.score) + " - " + str(AI.score), 5, 0, 3)
app.getLabelWidget("Sc").config(font="Helvetica 20")
app.getLabelWidget("Scores").config(font="Helvetica 20")
app.addNamedButton("Reset Scores", "ResScore", reset_scores, 7, 0, 3)
app.setButtonBg("ResScore", "red")
app.go()
