# To store custom functions related to the application

from flask import session
from datetime import datetime
from ast import literal_eval


def store_new_game_data(player1, player2, player3, player4):
    # Create new session and add known & dummy data
    session["player1"] = player1
    session["player2"] = player2
    session["player3"] = player3
    session["player4"] = player4
    session["total_scores"] = {"player1": 0, "player2": 0, "player3": 0, "player4": 0}
    session["current_round"] = 1
    session["saved"] = False
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
    for i in range(1, session["current_round"] if session["current_round"] <= 21 else 21):
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
    

# Function to check if the total sum of positive scores entered equals 40.
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


# Function to save the results to the stats tracker file
def determine_rankings():
    # Determine the ranking of the players
    session["rankings"] = sorted(session["total_scores"].items(), key=lambda x: x[1])
    session.modified = True


def save_endgame_results():
    # Save the match data to the stats file
    match_data = dict(date=str(datetime.utcnow()),
                      first=session[session["rankings"][0][0]],
                      second=session[session["rankings"][1][0]],
                      third=session[session["rankings"][2][0]],
                      fourth=session[session["rankings"][3][0]])
    with open("./db/matches.txt", "a") as file:
        file.write(str(match_data) + "\n")
    session["saved"] = True
    session["current_round"] = 21
    session.modified = True


def build_statistics():
    with open("./db/matches.txt", "r") as matches_file:
        stats = matches_file.readlines()
    # Store the names who have participated in matches in a list
    names = []
    for match in stats:
        # convert to dictionary
        match = literal_eval(match)
        names.append(match["first"])
        names.append(match["second"])
        names.append(match["third"])
        names.append(match["fourth"])
    names = list(dict.fromkeys(names))
    # Store the number of matches each player participated in
    matches = {}
    for name in names:
        matches[name] = 0
        for match in stats:
            match = literal_eval(match)
            if name == match["first"] or name == match["second"] or name == match["third"] or name == match["fourth"]:
                matches[name] += 1
    # Store the number of wins each player participated in
    wins = {}
    for name in names:
        wins[name] = 0
        for match in stats:
            match = literal_eval(match)
            if match["first"] == name:
                wins[name] += 1
    with open("./db/stats.txt", "w") as stats_file:
        stats_file.write(str(names) + "\n")
        stats_file.write(str(matches) + "\n")
        stats_file.write(str(wins))


# Function to test session-stored scores, is not used now.
def test_print_session_scores():
    print("current round: " + str(session["current_round"]))
    for i in range(1, 21):
        print(str(i) + ". kor:", session["round" + str(i)]["scores"]["player1"], session["round" + str(i)]["scores"]["player2"], session["round" + str(i)]["scores"]["player3"], session["round" + str(i)]["scores"]["player4"])
    print("total scores: ", session["total_scores"]["player1"], session["total_scores"]["player2"], session["total_scores"]["player3"], session["total_scores"]["player4"])