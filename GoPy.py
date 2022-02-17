size = int(input("GoPy oyunu boyutu: "))

while size < 3 or size > 8:
    print("Boyut en az 3 en çok 8 olabilir!")
    size = int(input("GoPy oyunu boyutu: "))


board, player, location, alphabet = [], "Galois", {}, [i for i in 'ABCDEFGH']
current_player = "M"
game = True
for i in range(size):
    columns = []
    for j in range(size):
        location.update({str(j)+str(alphabet[i]): str(j)+str(i)})
        columns.append("_")
    board.append(columns)

print(location)

def display_board(table):
    print("\t", end="")
    for i in range(size):
        print(alphabet[i], end="\t")
    print()
    for i in range(len(table)):
        for j in range(len(table)):
            if j==0:
                print(i, end="\t")
            print(table[i][j], end="\t")
        print()


def play_game(table):
    global player, current_player
    display_board(board)
    chosen_point = input("Sıra - {} --> ".format(player))
    while chosen_point not in location.keys():
        print("Lütfen geçerli bir hücre belirtiniz.")
        chosen_point = input("Sıra - {} --> ".format(player))

    row = int(location.get(chosen_point)[0])
    column = int(location.get(chosen_point)[1])
    if table[row][column] == "M" == current_player:
        print("Bu seçimi daha önce yaptınız.\nLütfen geçerli bir ") #aynı oyuncu devam edecek
    elif table[row][column] == "T" == current_player:
        print("You have made this choice before! ")
    elif table[row][column] == "M" and current_player == "T":
        print("The other player made this choice before! ")
    elif table[row][column] == "T" and current_player == "M":
        print("The other player made this choice before! ")
    else:
        table[row][column] = current_player
    check_rows(board)
    check_columns(board)
    check_diagonals(board)
    current_player_func()


def current_player_func():
    global current_player, player
    if current_player == "M":
        current_player, player = "T", "Nash"
    elif current_player == "T":
        current_player, player = "M", "Galois"


def check_rows(table):
    global game
    for i in range(size):
        for j in range(size-2):
            if table[i][j] == table[i][j+1] == table[i][j+2] == current_player:
                display_board(board)
                print("Kazanan --> {} - {}".format(player, current_player))
                game = False


def check_columns(table):
    global game
    count = 0
    for a in range(size):
        column_list = []
        for check_column in table:
            column_list.append(check_column[count])
        for j in range(size-2):
            if column_list[j] == column_list[j+1] == column_list[j+2] == current_player:
                display_board(board)
                print("Kazanan --> {} - {}".format(player, current_player))
                game = False
        count += 1


def check_diagonals(table): #değiştir
    global game
    count_for_left = 0
    count_for_right = size - 1
    diagonal_left_list, diagonal_right_list = [], []
    for check_column in table:
        diagonal_left_list.append(check_column[count_for_left])
        count_for_left += 1

    for check_column in table:
        diagonal_right_list.append(check_column[count_for_right])
        count_for_right -= 1

    if diagonal_right_list.count(current_player) == size or diagonal_left_list.count(current_player) == size:
        display_board(board)
        print("Winner: {}".format(current_player))
        game = False


while game:
    play_game(board)
