from turtle import Screen
from turtlehelena import Helenaturtle, Helenawall, Helenatext

NUMBER_OF_TURTLE = 9
X_POS = -400
Y_POS = [-300, -225, -150, -75, 0, 75, 150, 225, 300]
COLORS = ["red", "blue", "green", "purple", "brown", "gray", "black", "yellow", "pink",]


game_is_on = True
screen = Screen()

thewall = Helenawall()
theturtle = Helenaturtle("turtle", COLORS, X_POS, Y_POS, NUMBER_OF_TURTLE)

text = Screen()
guess = text.textinput("Guess the winner", "Guess turtle color to win the race:")

message = ""
while game_is_on:
    xcolor = theturtle.move_turtle()
    if xcolor in COLORS:
        game_is_on = False
        if guess.lower() == xcolor:
            message = (f"You Won!\nThe {xcolor} turtle won")
        else:
            message = (f"You Lost!\nThe {xcolor} turtle won")

thetext = Helenatext(message)


screen.exitonclick()
