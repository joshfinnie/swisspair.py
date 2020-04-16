from swisspair_py import SwissPair


def test_tournament():
    tournament = SwissPair()

    #  Add 8 players for 4 rounds of Swiss
    for i in range(0, 9):
        tournament.add_player(f"player_{i+1}")

    #  Pair for first round
    assert tournament.pair() == {
        "table_1": [
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_1",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_2",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
        ],
        "table_2": [
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_3",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_4",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
        ],
        "table_3": [
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_5",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_6",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
        ],
        "table_4": [
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_7",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_8",
                "points": 0,
                "winning_percentage": 0.0,
                "wins": 0,
            },
        ],
        "bye": [
            {
                "opponents": [],
                "owp": 0.0,
                "player_name": "player_9",
                "points": 3.0,
                "winning_percentage": 0.0,
                "wins": 1,
            }
        ],
    }

    # Submitting results for Round 1
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 1, 1))
    tournament.add_results((4, 2, 1, 0))

    assert tournament.finish_round() == [
        {
            "opponents": ["player_2"],
            "owp": 0.0,
            "player_name": "player_1",
            "points": 3.0,
            "winning_percentage": 1.0,
            "wins": 1,
        },
        {
            "opponents": ["player_1"],
            "owp": 1.0,
            "player_name": "player_2",
            "points": 0.0,
            "winning_percentage": 0.0,
            "wins": 0,
        },
        {
            "opponents": ["player_4"],
            "owp": 1.0,
            "player_name": "player_3",
            "points": 0.0,
            "winning_percentage": 0.0,
            "wins": 0,
        },
        {
            "opponents": ["player_3"],
            "owp": 0.0,
            "player_name": "player_4",
            "points": 3.0,
            "winning_percentage": 1.0,
            "wins": 1,
        },
        {
            "opponents": ["player_6"],
            "owp": 0.0,
            "player_name": "player_5",
            "points": 1.5,
            "winning_percentage": 0.0,
            "wins": 0,
        },
        {
            "opponents": ["player_5"],
            "owp": 0.0,
            "player_name": "player_6",
            "points": 1.5,
            "winning_percentage": 0.0,
            "wins": 0,
        },
        {
            "opponents": ["player_8"],
            "owp": 0.0,
            "player_name": "player_7",
            "points": 3.0,
            "winning_percentage": 1.0,
            "wins": 1,
        },
        {
            "opponents": ["player_7"],
            "owp": 1.0,
            "player_name": "player_8",
            "points": 0.0,
            "winning_percentage": 0.0,
            "wins": 0,
        },
        {
            "opponents": [],
            "owp": 0.0,
            "player_name": "player_9",
            "points": 3.0,
            "winning_percentage": 0.0,
            "wins": 1,
        },
    ]

    #  Pair for second round
    assert tournament.pair() == {
        "table_1": [
            {
                "player_name": "player_1",
                "opponents": ["player_2"],
                "wins": 1,
                "points": 3.0,
                "winning_percentage": 1.0,
                "owp": 0.0,
            },
            {
                "player_name": "player_4",
                "opponents": ["player_3"],
                "wins": 1,
                "points": 3.0,
                "winning_percentage": 1.0,
                "owp": 0.0,
            },
        ],
        "table_2": [
            {
                "player_name": "player_7",
                "opponents": ["player_8"],
                "wins": 1,
                "points": 3.0,
                "winning_percentage": 1.0,
                "owp": 0.0,
            },
            {
                "player_name": "player_9",
                "opponents": [],
                "wins": 1,
                "points": 3.0,
                "winning_percentage": 0.0,
                "owp": 0.0,
            },
        ],
        "table_3": [
            {
                "player_name": "player_5",
                "opponents": ["player_6"],
                "wins": 0,
                "points": 1.5,
                "winning_percentage": 0.0,
                "owp": 0.0,
            },
            {
                "player_name": "player_2",
                "opponents": ["player_1"],
                "wins": 0,
                "points": 0.0,
                "winning_percentage": 0.0,
                "owp": 1.0,
            },
        ],
        "table_4": [
            {
                "player_name": "player_6",
                "opponents": ["player_5"],
                "wins": 0,
                "points": 1.5,
                "winning_percentage": 0.0,
                "owp": 0.0,
            },
            {
                "player_name": "player_3",
                "opponents": ["player_4"],
                "wins": 0,
                "points": 0.0,
                "winning_percentage": 0.0,
                "owp": 1.0,
            },
        ],
        "bye": [
            {
                "player_name": "player_8",
                "opponents": ["player_7"],
                "wins": 1,
                "points": 3.0,
                "winning_percentage": 0.0,
                "owp": 1.0,
            }
        ],
    }

    # Round 2
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 1, 1))
    tournament.add_results((4, 2, 1, 0))
    tournament.finish_round()

    # Round 3
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 1, 1))
    tournament.add_results((4, 2, 1, 0))
    tournament.finish_round()

    # Round 4
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 1, 1))
    tournament.add_results((4, 2, 1, 0))

    assert tournament.finish_round() == [
        {
            "player_name": "player_1",
            "opponents": ["player_2", "player_4", "player_9", "player_8"],
            "wins": 4,
            "points": 12.0,
            "winning_percentage": 1.0,
            "owp": 0.5833333333333333,
        },
        {
            "player_name": "player_2",
            "opponents": ["player_1", "player_6", "player_5"],
            "wins": 1,
            "points": 3.0,
            "winning_percentage": 0.3333333333333333,
            "owp": 0.5,
        },
        {
            "player_name": "player_3",
            "opponents": ["player_4", "player_5", "player_6"],
            "wins": 1,
            "points": 6.0,
            "winning_percentage": 0.0,
            "owp": 0.3333333333333333,
        },
        {
            "player_name": "player_4",
            "opponents": ["player_3", "player_1", "player_7", "player_9"],
            "wins": 2,
            "points": 6.0,
            "winning_percentage": 0.5,
            "owp": 0.75,
        },
        {
            "player_name": "player_5",
            "opponents": ["player_6", "player_8", "player_3", "player_2"],
            "wins": 1,
            "points": 7.5,
            "winning_percentage": 0.25,
            "owp": 0.35416666666666663,
        },
        {
            "player_name": "player_6",
            "opponents": ["player_5", "player_2", "player_8", "player_3"],
            "wins": 1,
            "points": 6.0,
            "winning_percentage": 0.3333333333333333,
            "owp": 0.35416666666666663,
        },
        {
            "player_name": "player_7",
            "opponents": ["player_8", "player_9", "player_4"],
            "wins": 2,
            "points": 6.0,
            "winning_percentage": 0.3333333333333333,
            "owp": 0.6666666666666666,
        },
        {
            "player_name": "player_8",
            "opponents": ["player_7", "player_5", "player_6", "player_1"],
            "wins": 2,
            "points": 7.5,
            "winning_percentage": 0.5,
            "owp": 0.5416666666666666,
        },
        {
            "player_name": "player_9",
            "opponents": ["player_7", "player_1", "player_4"],
            "wins": 3,
            "points": 9.0,
            "winning_percentage": 1.0,
            "owp": 0.7222222222222222,
        },
    ]


def test_big_tournament():
    tournament = SwissPair()

    #  Add 8 players for 6 rounds of Swiss
    for i in range(0, 19):
        tournament.add_player(f"player_{i+1}")

    # Round 1
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 2, 0))
    tournament.add_results((4, 2, 1, 0))
    tournament.add_results((5, 2, 1, 0))
    tournament.add_results((6, 1, 1, 1))
    tournament.add_results((7, 0, 2, 0))
    tournament.add_results((8, 1, 2, 0))
    tournament.add_results((9, 2, 1, 0))
    tournament.finish_round()

    # Round 2
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 2, 0))
    tournament.add_results((4, 2, 1, 0))
    tournament.add_results((5, 2, 1, 0))
    tournament.add_results((6, 1, 1, 1))
    tournament.add_results((7, 0, 2, 0))
    tournament.add_results((8, 1, 2, 0))
    tournament.add_results((9, 2, 1, 0))
    tournament.finish_round()

    # Round 3
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 2, 0))
    tournament.add_results((4, 2, 1, 0))
    tournament.add_results((5, 2, 1, 0))
    tournament.add_results((6, 1, 1, 1))
    tournament.add_results((7, 0, 2, 0))
    tournament.add_results((8, 1, 2, 0))
    tournament.add_results((9, 2, 1, 0))
    tournament.finish_round()

    # Round 4
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 2, 0))
    tournament.add_results((4, 2, 1, 0))
    tournament.add_results((5, 2, 1, 0))
    tournament.add_results((6, 1, 1, 1))
    tournament.add_results((7, 0, 2, 0))
    tournament.add_results((8, 1, 2, 0))
    tournament.add_results((9, 2, 1, 0))
    tournament.finish_round()

    # Round 5
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 2, 0))
    tournament.add_results((4, 2, 1, 0))
    tournament.add_results((5, 2, 1, 0))
    tournament.add_results((6, 1, 1, 1))
    tournament.add_results((7, 0, 2, 0))
    tournament.add_results((8, 1, 2, 0))
    tournament.add_results((9, 2, 1, 0))
    tournament.finish_round()

    # Round 6
    tournament.pair()
    tournament.add_results((1, 2, 1, 0))
    tournament.add_results((2, 0, 2, 0))
    tournament.add_results((3, 1, 2, 0))
    tournament.add_results((4, 2, 1, 0))
    tournament.add_results((5, 2, 1, 0))
    tournament.add_results((6, 1, 1, 1))
    tournament.add_results((7, 0, 2, 0))
    tournament.add_results((8, 1, 2, 0))
    tournament.add_results((9, 2, 1, 0))
    tournament.finish_round()
    assert tournament.finish_round() == [
        {
            "player_name": "player_1",
            "opponents": [
                "player_2",
                "player_4",
                "player_7",
                "player_16",
                "player_5",
                "player_14",
            ],
            "wins": 6,
            "points": 18.0,
            "winning_percentage": 1.0,
            "owp": 0.5833333333333333,
        },
        {
            "player_name": "player_2",
            "opponents": [
                "player_1",
                "player_12",
                "player_17",
                "player_11",
                "player_16",
                "player_4",
            ],
            "wins": 3,
            "points": 10.5,
            "winning_percentage": 0.5,
            "owp": 0.47222222222222215,
        },
        {
            "player_name": "player_3",
            "opponents": [
                "player_4",
                "player_5",
                "player_8",
                "player_12",
                "player_11",
                "player_10",
            ],
            "wins": 2,
            "points": 7.5,
            "winning_percentage": 0.3333333333333333,
            "owp": 0.3611111111111111,
        },
        {
            "player_name": "player_4",
            "opponents": [
                "player_3",
                "player_1",
                "player_19",
                "player_5",
                "player_6",
                "player_2",
            ],
            "wins": 4,
            "points": 12.0,
            "winning_percentage": 0.6666666666666666,
            "owp": 0.6055555555555555,
        },
        {
            "player_name": "player_5",
            "opponents": [
                "player_6",
                "player_3",
                "player_9",
                "player_4",
                "player_1",
                "player_7",
            ],
            "wins": 3,
            "points": 9.0,
            "winning_percentage": 0.5,
            "owp": 0.6388888888888888,
        },
        {
            "player_name": "player_6",
            "opponents": [
                "player_5",
                "player_7",
                "player_10",
                "player_14",
                "player_4",
                "player_17",
            ],
            "wins": 3,
            "points": 9.0,
            "winning_percentage": 0.5,
            "owp": 0.5,
        },
        {
            "player_name": "player_7",
            "opponents": [
                "player_8",
                "player_6",
                "player_1",
                "player_19",
                "player_14",
                "player_5",
            ],
            "wins": 4,
            "points": 12.0,
            "winning_percentage": 0.6666666666666666,
            "owp": 0.6611111111111111,
        },
        {
            "player_name": "player_8",
            "opponents": ["player_7", "player_10", "player_3", "player_17"],
            "wins": 2,
            "points": 6.0,
            "winning_percentage": 0.0,
            "owp": 0.37499999999999994,
        },
        {
            "player_name": "player_9",
            "opponents": [
                "player_10",
                "player_14",
                "player_5",
                "player_13",
                "player_12",
                "player_16",
            ],
            "wins": 4,
            "points": 12.0,
            "winning_percentage": 0.6666666666666666,
            "owp": 0.3611111111111111,
        },
        {
            "player_name": "player_10",
            "opponents": [
                "player_9",
                "player_8",
                "player_6",
                "player_15",
                "player_13",
                "player_3",
            ],
            "wins": 1,
            "points": 3.0,
            "winning_percentage": 0.16666666666666666,
            "owp": 0.45555555555555555,
        },
        {
            "player_name": "player_11",
            "opponents": [
                "player_12",
                "player_19",
                "player_18",
                "player_2",
                "player_3",
                "player_15",
            ],
            "wins": 2,
            "points": 9.0,
            "winning_percentage": 0.4,
            "owp": 0.46388888888888885,
        },
        {
            "player_name": "player_12",
            "opponents": [
                "player_11",
                "player_2",
                "player_13",
                "player_3",
                "player_9",
                "player_18",
            ],
            "wins": 0,
            "points": 6.0,
            "winning_percentage": 0.0,
            "owp": 0.4861111111111111,
        },
        {
            "player_name": "player_13",
            "opponents": [
                "player_14",
                "player_15",
                "player_12",
                "player_9",
                "player_10",
                "player_19",
            ],
            "wins": 2,
            "points": 7.5,
            "winning_percentage": 0.3333333333333333,
            "owp": 0.45,
        },
        {
            "player_name": "player_14",
            "opponents": [
                "player_13",
                "player_9",
                "player_16",
                "player_6",
                "player_7",
                "player_1",
            ],
            "wins": 4,
            "points": 12.0,
            "winning_percentage": 0.6666666666666666,
            "owp": 0.611111111111111,
        },
        {
            "player_name": "player_15",
            "opponents": [
                "player_16",
                "player_13",
                "player_10",
                "player_17",
                "player_11",
            ],
            "wins": 2,
            "points": 9.0,
            "winning_percentage": 0.6666666666666666,
            "owp": 0.3333333333333333,
        },
        {
            "player_name": "player_16",
            "opponents": [
                "player_15",
                "player_17",
                "player_14",
                "player_1",
                "player_2",
                "player_9",
            ],
            "wins": 3,
            "points": 9.0,
            "winning_percentage": 0.5,
            "owp": 0.5944444444444444,
        },
        {
            "player_name": "player_17",
            "opponents": [
                "player_18",
                "player_16",
                "player_2",
                "player_8",
                "player_15",
                "player_6",
            ],
            "wins": 2,
            "points": 7.5,
            "winning_percentage": 0.3333333333333333,
            "owp": 0.525,
        },
        {
            "player_name": "player_18",
            "opponents": ["player_17", "player_11", "player_19", "player_12"],
            "wins": 3,
            "points": 9.0,
            "winning_percentage": 0.75,
            "owp": 0.3666666666666667,
        },
        {
            "player_name": "player_19",
            "opponents": [
                "player_11",
                "player_4",
                "player_7",
                "player_18",
                "player_13",
            ],
            "wins": 4,
            "points": 12.0,
            "winning_percentage": 0.8,
            "owp": 0.55,
        },
    ]

    assert tournament.get_results() == [
        {"player_name": "player_1", "points": 18.0, "owp": 0.5833333333333333},
        {"player_name": "player_7", "points": 12.0, "owp": 0.6611111111111111},
        {"player_name": "player_14", "points": 12.0, "owp": 0.611111111111111},
        {"player_name": "player_4", "points": 12.0, "owp": 0.6055555555555555},
        {"player_name": "player_19", "points": 12.0, "owp": 0.55},
        {"player_name": "player_9", "points": 12.0, "owp": 0.3611111111111111},
        {"player_name": "player_2", "points": 10.5, "owp": 0.47222222222222215},
        {"player_name": "player_5", "points": 9.0, "owp": 0.6388888888888888},
        {"player_name": "player_16", "points": 9.0, "owp": 0.5944444444444444},
        {"player_name": "player_6", "points": 9.0, "owp": 0.5},
        {"player_name": "player_11", "points": 9.0, "owp": 0.46388888888888885},
        {"player_name": "player_18", "points": 9.0, "owp": 0.3666666666666667},
        {"player_name": "player_15", "points": 9.0, "owp": 0.3333333333333333},
        {"player_name": "player_17", "points": 7.5, "owp": 0.525},
        {"player_name": "player_13", "points": 7.5, "owp": 0.45},
        {"player_name": "player_3", "points": 7.5, "owp": 0.3611111111111111},
        {"player_name": "player_12", "points": 6.0, "owp": 0.4861111111111111},
        {"player_name": "player_8", "points": 6.0, "owp": 0.37499999999999994},
        {"player_name": "player_10", "points": 3.0, "owp": 0.45555555555555555},
    ]
