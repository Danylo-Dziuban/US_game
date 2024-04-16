from turtle import Screen
import pandas
import os
from nameState import NameState

TITLE = "U.S. States Game"
PIC = 'RESOURCES/blank_states_img.gif'
DATA_FILE = 'RESOURCES/50_states.csv'

data = pandas.read_csv(DATA_FILE)
# unlearned_data = pandas.read_csv('RESOURCES/unlearned_states.csv')
screen = Screen()
screen.title(TITLE)
screen.bgpic(PIC)

guessed = 0

if os.path.getsize('RESOURCES/guessed.txt') != 0:
    with open('RESOURCES/guessed.txt', 'r') as file:
        guessed = int(file.read())

tries = 3
game_is_on = True
learned_states = []

if not os.path.getsize('RESOURCES/learned_states.csv') == 0:
    learned_data = pandas.read_csv('RESOURCES/learned_states.csv')
    learned_states = learned_data.state.to_list()

    for state_name in learned_states:
        state_data = learned_data[learned_data.state == state_name]

        state = NameState(state_data.x.item(), state_data.y.item(), state_data.state.item())

states = data.state.to_list()
# unlearned_new_data = {
#     "state": [],
#     "x": [],
#     "y": []
# }
learned_new_data = {
    "state": [],
    "x": [],
    "y": []
}

while game_is_on:
    guess = screen.textinput(f"{guessed}/50 States Guessed  {tries}: Tries Left", "Please, enter your guess (enter 'Exit' to exit):").title()

    if guess == "Exit":
        break

    if guess in states and guess not in learned_states:
        state_data = data[data.state == guess]
        learned_states.append(state_data.state.item())
        state = NameState(state_data.x.item(), state_data.y.item(), state_data.state.item())
        guessed += 1
        screen.title(f"{guessed}/50 States Guessed")
        continue

    tries -= 1

    if tries == 0:
        game_is_on = False

for state in states:
    state_data = data[data.state == state]

    if state_data.state.item() in learned_states:
        learned_new_data['state'].append(state_data.state.item())
        learned_new_data['x'].append(state_data.x.item())
        learned_new_data['y'].append(state_data.y.item())


# unlearned_csv = pandas.DataFrame(unlearned_new_data)
learned_csv = pandas.DataFrame(learned_new_data)

with open('RESOURCES/guessed.txt', 'w') as file:
    file.write(str(guessed))

guessed = 0

# unlearned_csv.to_csv('RESOURCES/unlearned_states.csv')
learned_csv.to_csv('RESOURCES/learned_states.csv')

screen.exitonclick()
