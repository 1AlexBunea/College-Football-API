
from flask import Flask
from flask_cors import CORS
import http.client


app = Flask("__name__")

CORS(app)

#adds the player data to a list
def add_players_to_dictionary(player_dictionary, full_name, player_position ,player_height, player_weight, player_year,
                              player_birth_place, player_team_name, player_conference):
    player_dictionary[full_name].append(player_position)
    player_dictionary[full_name].append(player_height)
    player_dictionary[full_name].append(player_weight)
    player_dictionary[full_name].append(player_year)
    player_dictionary[full_name].append(player_birth_place)
    player_dictionary[full_name].append(player_team_name)
    player_dictionary[full_name].append(player_conference)


def fill_player_dict(player_dictionary, data_list):
    for x in range(0, len(data_list)):
        if ("first_name" in data_list[x]):
            start_index = x
            new_index = x + 2
            full_name = data_list[new_index][8: len(data_list[new_index]) - 1]
            new_index += 1

            player_position = data_list[new_index][12: len(data_list[new_index]) - 1]
            new_index += 1

            for y in range(start_index, len(data_list)):
                if ("height" in data_list[y]):
                    new_index = y
                    break
            player_height = data_list[new_index][9: len(data_list[new_index])]

            for y in range(start_index, len(data_list)):
                if ("weight" in data_list[y]):
                    new_index = y
                    break
            player_weight = data_list[new_index][9: len(data_list[new_index])]

            for y in range(start_index, len(data_list)):
                if ("experience" in data_list[y]):
                    new_index = y
                    break
            player_year = data_list[new_index][14: len(data_list[new_index]) - 1]

            for y in range(start_index, len(data_list)):
                if ("birth_place" in data_list[y]):
                    new_index = y
                    break
            player_birth_place = (
                        data_list[new_index][15: len(data_list[new_index])] + ", " + data_list[new_index + 1] + ", " +
                        data_list[new_index + 2][0: len(data_list[new_index + 2]) - 1])

            for y in range(start_index, len(data_list)):
                if ("team_name" in data_list[y]):
                    new_index = y
                    break
            player_team_name = data_list[new_index][13: len(data_list[new_index]) - 1]

            for y in range(start_index, len(data_list)):
                if ("conference" in data_list[y]):
                    new_index = y + 1
                    break

            player_conference = data_list[new_index][8: len(data_list[new_index]) - 1]

            player_dictionary[full_name] = []

            # add all the data into a dictionary
            add_players_to_dictionary(player_dictionary, full_name, player_position, player_height, player_weight,
                                      player_year, player_birth_place, player_team_name, player_conference)

#accesses the API at a specific year and finds the player
def process(prospect_name, year):
    conn = http.client.HTTPSConnection("api.sportradar.us")

    api_key = "{your_api_key}"

    url_for_data = "/draft/nfl/trial/v1/en/" + str(year) + "/prospects.json?api_key=" + api_key

    conn.request("GET", url_for_data)

    res = conn.getresponse()
    data = res.read()

    # splits all the players into different lists
    data_list = str(data).split("prospects")[1].split(",")

    player_dictionary = {}

    fill_player_dict(player_dictionary, data_list)

    for player in player_dictionary:
        if (player == prospect_name): 
            ret = {player : player_dictionary[player]}
            return ret


#pulls data from data base and organizes into a dictionary
@app.route("/prospects/<username>/<year>")
def nfl_prospects(username, year):
    return process(username, year)[username]


if __name__ == "__main__":

    app.run(debug=True)


