class InMemoryStorage():
    def __init__(self):
        self._players = []
        self._pairings = {}

    @property
    def players(self):
        return self._players

    @property
    def pairings(self):
        return self._pairings

    def reset_players(self):
        self._players = []

    def reset_pairings(self):
        self._pairings = {}
        return self._pairings

    def add_player(self, player):
        self._players.append(player)

    def get_player_by_name(self, name):
        player = list(filter(lambda x: x["player_name"] == name, self._players))
        return player[0]

    def remove_player_by_name(self, name):
        self._players = list(filter(lambda x: x["player_name"] != name, self._players))
