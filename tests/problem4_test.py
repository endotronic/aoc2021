from problem4 import (
    BingoBoard,
    solve_part1,
    solve_part2,
)


provided_example = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
    "",
    "3 15  0  2 22",
    "9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7",
]


def test_problem4_part1() -> None:
    assert solve_part1(provided_example) == 4512


def test_problem4_part2() -> None:
    assert solve_part2(provided_example) == 1924


def test_bingo_board_col() -> None:
    board = BingoBoard.from_strings(
        [
            "14 21 17 24  4",
            "10 16 15  9 19",
            "18  8 23 26 20",
            "22 11 13  6  5",
            "2  0 12  3  7",
        ]
    )

    board.call(17)
    assert not board.is_won()
    board.call(23)
    assert not board.is_won()
    board.call(12)
    assert not board.is_won()
    board.call(15)
    assert not board.is_won()
    board.call(13)
    assert board.is_won()


def test_bingo_board_row() -> None:
    board = BingoBoard.from_strings(
        [
            "14 21 17 24  4",
            "10 16 15  9 19",
            "18  8 23 26 20",
            "22 11 13  6  5",
            "2  0 12  3  7",
        ]
    )

    board.call(22)
    assert not board.is_won()
    board.call(13)
    assert not board.is_won()
    board.call(11)
    assert not board.is_won()
    board.call(6)
    assert not board.is_won()
    board.call(5)
    assert board.is_won()
