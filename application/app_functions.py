# To store custom functions related to the application

from flask import session


def store_new_game_data(player1, player2, player3, player4):
    # Create new session and add known & dummy data
    session["player1"] = player1
    session["player2"] = player2
    session["player3"] = player3
    session["player4"] = player4
    for i in range(1, 21):
        # Generate an entry for each round
        session["round" + str(i)] = {"sequence": i, "adu": 0, "direction": 0, "starts": 0, "scores": {"player1": 0, "player2": 0, "player3": 0, "player4": 0}}
        # Set the adu, direction, and starting player for each round
        match i % 5:
            case 1:
                session["round" + str(i)]["adu"] = "treff"
            case 2:
                session["round" + str(i)]["adu"] = "karo"
            case 3:
                session["round" + str(i)]["adu"] = "kor"
            case 4: 
                session["round" + str(i)]["adu"] = "pikk"
            case 0:
                session["round" + str(i)]["adu"] = "szan"
        
        match i % 4:
            case 1:
                session["round" + str(i)]["direction"] = "jobbra"
                session["round" + str(i)]["starts"] = player1
            case 2:
                session["round" + str(i)]["direction"] = "balra"
                session["round" + str(i)]["starts"] = player2
            case 3:
                session["round" + str(i)]["direction"] = "szembe"
                session["round" + str(i)]["starts"] = player3
            case 0:
                session["round" + str(i)]["direction"] = "nem"
                session["round" + str(i)]["starts"] = player4


def save_scores(round, player1_score, player2_score, player3_score, player4_score):
    # Save the scores for the given round
    session["round" + str(round)]["scores"]["player1"] = player1_score
    session["round" + str(round)]["scores"]["player2"] = player2_score
    session["round" + str(round)]["scores"]["player3"] = player3_score
    session["round" + str(round)]["scores"]["player4"] = player4_score