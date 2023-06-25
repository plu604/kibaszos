# To store custom functions related to the application

from flask import session, flash


def store_new_game_data(player1, player2, player3, player4):
    # Create new session and add known & dummy data
    session["player1"] = player1
    session["player2"] = player2
    session["player3"] = player3
    session["player4"] = player4
    session["total_scores"] = {"player1": 0, "player2": 0, "player3": 0, "player4": 0}
    session["current_round"] = 1
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
    if round == session["current_round"]:
        session["current_round"] += 1
    # Add the scores to the total scores, recalculating each round in case there was an edit
    session["total_scores"]["player1"] = 0
    session["total_scores"]["player2"] = 0
    session["total_scores"]["player3"] = 0
    session["total_scores"]["player4"] = 0
    for i in range(1, session["current_round"]):
        session["total_scores"]["player1"] += session["round" + str(i)]["scores"]["player1"]
        session["total_scores"]["player2"] += session["round" + str(i)]["scores"]["player2"]
        session["total_scores"]["player3"] += session["round" + str(i)]["scores"]["player3"]
        session["total_scores"]["player4"] += session["round" + str(i)]["scores"]["player4"]


# Function to test if the entered score is valid
def scoring_validation(score1, score2, score3, score4):
    scores = [score1, score2, score3, score4]
    for score in scores:
        if 40 < score or score < 0 and score != -10:
            return False
    return True
    

def sum_validation(score1, score2, score3, score4):
    sum = 0
    scores = [score1, score2, score3, score4]
    for score in scores:
        if score > 0:
            sum += score
    if sum == 40:
        return True
    else:
        return False


# Function to test session-stored scores, is not used now.
def test_print_session_scores():
    print("current round: " + str(session["current_round"]))
    for i in range(1, 21):
        print(str(i) + ". kor:", session["round" + str(i)]["scores"]["player1"], session["round" + str(i)]["scores"]["player2"], session["round" + str(i)]["scores"]["player3"], session["round" + str(i)]["scores"]["player4"])
    print("total scores: ", session["total_scores"]["player1"], session["total_scores"]["player2"], session["total_scores"]["player3"], session["total_scores"]["player4"])