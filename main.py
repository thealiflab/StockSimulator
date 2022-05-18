from game_brain import GameBrain

gameBrain = GameBrain()

rounds = 1
is_game_on = True

while is_game_on:
    print(f"=======================Round {rounds}==============================")

    if rounds == 6:
        is_game_on = False
    else:
        gameBrain.simulate()
        rounds += 1

gameBrain.result()
