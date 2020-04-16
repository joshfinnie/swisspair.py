from .__version__ import __version__

from .storage.memory import InMemoryStorage


class SwissPair:

    VERSION = __version__
    WIN_POINTS = 3.0
    LOSS_POINTS = 0.0
    BYE_POINTS = WIN_POINTS
    TIE_POINTS = 1.5

    def __init__(self):
        self.engine = InMemoryStorage()

    def __generate_player_object(self, player_name):
        return {
            "player_name": player_name,
            "opponents": [],
            "wins": 0,
            "points": 0,
            "winning_percentage": 0.0,
            "owp": 0.0,
        }

    def reset_players(self):
        self.engine.reset_players()

    def add_player(self, player_name):
        player = self.__generate_player_object(player_name)
        self.engine.add_player(player)

    def __bye_win(self, player):
        player["wins"] += 1
        player["points"] += self.WIN_POINTS

    def __get_opponent(self, player_name, opponents):
        player = self.engine.get_player_by_name(player_name)
        for opponent in opponents:
            if opponent not in player["opponents"]:
                return opponent

    def pair(self):
        pairings = self.engine.reset_pairings()
        players = self.engine.players
        non_paired_player_names = [
            x["player_name"] for x in sorted(players, key=lambda x: x["points"], reverse=True)
        ]
        table = 1
        while len(non_paired_player_names):
            if len(non_paired_player_names) == 1:
                pairings["bye"] = [
                    self.engine.get_player_by_name(non_paired_player_names[0])
                ]
                self.__bye_win(
                    self.engine.get_player_by_name(non_paired_player_names[0])
                )
                non_paired_player_names.remove(non_paired_player_names[0])
                continue

            player_1_name = non_paired_player_names[0]
            player_2_name = self.__get_opponent(
                player_1_name, non_paired_player_names[1:]
            )
            pairings[f"table_{table}"] = [
                self.engine.get_player_by_name(player_1_name),
                self.engine.get_player_by_name(player_2_name),
            ]
            non_paired_player_names.remove(player_1_name)
            non_paired_player_names.remove(player_2_name)

            table += 1

        return pairings

    def __add_to_opponents_list(self, players):
        players[0]["opponents"].append(players[1]["player_name"])
        players[1]["opponents"].append(players[0]["player_name"])

    def __calc_winning_percentage(self, player_name):
        players = self.engine.players
        player = next(filter(lambda x: x["player_name"] == player_name, players))
        return player["wins"] / len(player["opponents"])

    def __update_win_percentage(self, players):
        players[0]["winning_percentage"] = self.__calc_winning_percentage(
            players[0]["player_name"]
        )
        players[1]["winning_percentage"] = self.__calc_winning_percentage(
            players[1]["player_name"]
        )

    def __add_win(self, players, windex):
        players[windex]["wins"] += 1
        self.__update_win_percentage(players)

    def add_results(self, t):
        pairings = self.engine.pairings
        table_id, player_1_results, player_2_results, tie = t
        if tie:
            pairings[f"table_{table_id}"][0]["points"] += self.TIE_POINTS
            pairings[f"table_{table_id}"][1]["points"] += self.TIE_POINTS
            self.__add_to_opponents_list(pairings[f"table_{table_id}"])
            return pairings[f"table_{table_id}"]
        if player_1_results > player_2_results:
            pairings[f"table_{table_id}"][0]["points"] += self.WIN_POINTS
            pairings[f"table_{table_id}"][1]["points"] += self.LOSS_POINTS
            self.__add_to_opponents_list(pairings[f"table_{table_id}"])
            self.__add_win(pairings[f"table_{table_id}"], 0)
            return pairings[f"table_{table_id}"]
        if player_1_results < player_2_results:
            pairings[f"table_{table_id}"][0]["points"] += self.LOSS_POINTS
            pairings[f"table_{table_id}"][1]["points"] += self.WIN_POINTS
            self.__add_to_opponents_list(pairings[f"table_{table_id}"])
            self.__add_win(pairings[f"table_{table_id}"], 1)
            return pairings[f"table_{table_id}"]

    def __update_owp(self, player):
        owp_total = 0
        for opp in player["opponents"]:
            owp_total += self.__calc_winning_percentage(opp)
        if len(player["opponents"]) == 0:
            return 0.0
        return owp_total / len(player["opponents"])

    def finish_round(self):
        players = self.engine.players
        for player in players:
            player["owp"] = self.__update_owp(player)
        return players

    def get_results(self):
        players = self.engine.players
        for player in players:
            del player["opponents"]
            del player["winning_percentage"]
            del player["wins"]
            player["record"] = f""

        return sorted(players, key=lambda x: (x["points"], x["owp"]), reverse=True)
