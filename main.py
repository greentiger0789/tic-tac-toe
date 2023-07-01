import random


def make_empty_mat() -> list:
    """ゲーム開始時の盤面を作る

    Returns:
        list: 盤面の配列
    """
    board_mat = []
    row = []
    for i in range(1, 10):
        row.append(str(i))
        if i % 3 == 0:
            board_mat.append(row)
            row = []
    return board_mat


def print_board(board_mat: list) -> None:
    """盤面をprintする

    Args:
        board_mat (list): 盤面の配列
    """
    for row in board_mat:
        print(row)


def player_turn(board_mat: list) -> list:
    """プレイヤーターンの進行

    Args:
        board_mat (list): 盤面の配列

    Returns:
        list: 盤面の配列
    """
    print("【Your turn】")
    while True:
        input_val = input("あなたは，◯です．数字を入力（1〜9）：")
        if input_val.isdigit() and int(input_val) in range(1, 10):
            if board_mat[(int(input_val) - 1) // 3][(int(input_val) - 1) % 3] not in [
                "◯",
                "✕",
            ]:
                board_mat[(int(input_val) - 1) // 3][(int(input_val) - 1) % 3] = "◯"
                break
            else:
                print("その場所はすでに埋まっています．")
        else:
            print("入力された文字列が1〜9の数字ではありませんでした．")
    return board_mat


def opponent_turn(board_mat: list) -> list:
    """相手ターンの進行

    Args:
        board_mat (list): 盤面の配列

    Returns:
        list: 盤面の配列
    """
    print("【Opponent's turn】")
    print("相手は✕です．")
    while True:
        input_val = random.choice(range(9))
        if board_mat[input_val // 3][input_val % 3] not in ["◯", "✕"]:
            print(f"Opponent's select: {input_val + 1}")
            board_mat[input_val // 3][input_val % 3] = "✕"
            break
    return board_mat


def check_win(board_mat: list, turn: str) -> bool:
    """勝利条件を満たしているか判定

    Args:
        board_mat (list): 盤面の配列
        turn (str): どちらのターンか

    Returns:
        bool: 勝利条件を満たしていたらTrueを返す
    """
    turns = ["player", "opponent"]
    turn_symbols = ["◯", "✕"]
    turn_symbol = turn_symbols[turns.index(turn)]
    flag = False
    for row in board_mat:
        if row == [turn_symbol for i in range(3)]:
            flag = True
            break

    for c in range(3):
        columun = [board_mat[i][c] for i in range(3)]
        if columun == [turn_symbol for i in range(3)]:
            flag = True
            break

    naname1 = []
    for i in range(3):
        naname1.append(board_mat[i][i])
    if naname1 == [turn_symbol for i in range(3)]:
        flag = True

    naname2 = []
    for i in range(3):
        naname2.append(board_mat[i][3 - i - 1])
    if naname2 == [turn_symbol for i in range(3)]:
        flag = True

    return flag


def main():
    """これはメイン関数です．"""
    print("Game Start!!")
    print()
    board_mat = make_empty_mat()
    print_board(board_mat)
    print()
    is_game_over = False
    for turn_number in range(9):
        if turn_number % 2 == 0:
            board_mat = player_turn(board_mat)
            print_board(board_mat)
            print()

            is_game_over = check_win(board_mat, "player")
            if is_game_over is True:
                winner = "Player"
                break
        else:
            board_mat = opponent_turn(board_mat)
            print_board(board_mat)
            print()

            is_game_over = check_win(board_mat, "opponent")
            if is_game_over is True:
                winner = "Opponent"
                break

    print("Game set!")
    if is_game_over:
        print(f"Winner: {winner}!")
    else:
        print("It's a draw.")


if __name__ == "__main__":
    main()
