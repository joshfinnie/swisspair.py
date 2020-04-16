from unittest import TestCase

from swisspair_py.storage.memory import InMemoryStorage


class TestInMemoryStorage(TestCase):
    def setUp(self):
        self.storage = InMemoryStorage()

    def tearDown(self):
        self.storage.reset_players()

    def test_default_players(self):
        assert self.storage.players == []

    def test_default_pairings(self):
        assert self.storage.pairings == {}

    def test_reset_players(self):
        self.storage._players = "aoeu"
        self.storage.reset_players()
        assert self.storage._players == []

    def test_reset_pairings(self):
        self.storage._pairings = "aoeu"
        assert self.storage.reset_pairings() == {}

    def test_add_player(self):
        player = {"player_name": "aoeu"}
        self.storage.add_player(player)
        assert self.storage.players == [player]

    def test_get_player_by_name(self):
        player = {"player_name": "aoeu"}
        self.storage.add_player(player)
        assert self.storage.get_player_by_name("aoeu") == player

    def test_remove_player_by_name(self):
        player = {"player_name": "aoeu"}
        self.storage.add_player(player)
        self.storage.remove_player_by_name("aoeu")
        assert self.storage.players == []
