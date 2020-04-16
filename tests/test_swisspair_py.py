from unittest import TestCase

from swisspair_py import SwissPair


class TestSwissPair(TestCase):
    def setUp(self):
        self.sp = SwissPair()

    def tearDown(self):
        self.sp.reset_players()

    def test_version(self):
        assert self.sp.VERSION == "0.1.0"

    def test_default_players(self):
        assert self.sp.players == []

    def test_default_pairings(self):
        assert self.sp.pairings == {}

    def test_adding_player(self):
        self.sp.add_player("aoeu")
        assert self.sp.players[0]["player_name"] == "aoeu"

    def test_removing_player(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.remove_player("aoeu")
        assert len(self.sp.players) == 1

    def test_pair_simple(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        assert self.sp.pair() == {
            "table_1": [
                {
                    "player_name": "aoeu",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
                {
                    "player_name": "hehe",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
            ]
        }

    def test_pair_simple_two_tables(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.add_player("bubu")
        self.sp.add_player("cece")
        assert self.sp.pair() == {
            "table_1": [
                {
                    "player_name": "aoeu",
                    "opponents": [],
                    "wins": 0,
                    "points": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                },
                {
                    "player_name": "hehe",
                    "opponents": [],
                    "wins": 0,
                    "points": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                },
            ],
            "table_2": [
                {
                    "player_name": "bubu",
                    "opponents": [],
                    "wins": 0,
                    "points": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                },
                {
                    "player_name": "cece",
                    "opponents": [],
                    "wins": 0,
                    "points": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                },
            ],
        }

    def test_pair_simple_three_tables_and_bye(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.add_player("bubu")
        self.sp.add_player("cece")
        self.sp.add_player("ioio")
        self.sp.add_player("yeye")
        self.sp.add_player("bbbb")
        assert self.sp.pair() == {
            "table_1": [
                {
                    "player_name": "aoeu",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
                {
                    "player_name": "hehe",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
            ],
            "table_2": [
                {
                    "player_name": "bubu",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
                {
                    "player_name": "cece",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
            ],
            "table_3": [
                {
                    "player_name": "ioio",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
                {
                    "player_name": "yeye",
                    "opponents": [],
                    "wins": 0,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 0,
                },
            ],
            "bye": [
                {
                    "player_name": "bbbb",
                    "opponents": [],
                    "wins": 1,
                    "winning_percentage": 0.0,
                    "owp": 0.0,
                    "points": 3.0,
                }
            ],
        }

    def test_add_results_tie(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.pair()
        assert self.sp.add_results((1, 1, 1, 1)) == [
            {
                "player_name": "aoeu",
                "opponents": ["hehe"],
                "wins": 0,
                "winning_percentage": 0.0,
                "owp": 0.0,
                "points": 1.5,
            },
            {
                "player_name": "hehe",
                "opponents": ["aoeu"],
                "wins": 0,
                "winning_percentage": 0.0,
                "owp": 0.0,
                "points": 1.5,
            },
        ]

    def test_add_results_player1_wins(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.pair()
        assert self.sp.add_results((1, 2, 1, 0)) == [
            {
                "player_name": "aoeu",
                "opponents": ["hehe"],
                "wins": 1,
                "winning_percentage": 1.0,
                "owp": 0.0,
                "points": 3.0,
            },
            {
                "player_name": "hehe",
                "opponents": ["aoeu"],
                "wins": 0,
                "winning_percentage": 0.0,
                "owp": 0.0,
                "points": 0,
            },
        ]

    def test_add_results_player2_wins(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.pair()
        assert self.sp.add_results((1, 0, 2, 0)) == [
            {
                "player_name": "aoeu",
                "opponents": ["hehe"],
                "wins": 0,
                "winning_percentage": 0.0,
                "owp": 0.0,
                "points": 0,
            },
            {
                "player_name": "hehe",
                "opponents": ["aoeu"],
                "wins": 1,
                "winning_percentage": 1.0,
                "owp": 0.0,
                "points": 3.0,
            },
        ]

    def test_finish_round(self):
        self.sp.add_player("aoeu")
        self.sp.add_player("hehe")
        self.sp.pair()
        self.sp.add_results((1, 0, 2, 0))
        assert self.sp.finish_round() == [
            {
                "player_name": "aoeu",
                "opponents": ["hehe"],
                "wins": 0,
                "points": 0.0,
                "winning_percentage": 0.0,
                "owp": 1.0,
            },
            {
                "player_name": "hehe",
                "opponents": ["aoeu"],
                "wins": 1,
                "points": 3.0,
                "winning_percentage": 1.0,
                "owp": 0.0,
            },
        ]
