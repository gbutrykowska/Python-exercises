# 8.1 W Stringu mogą się znaleźć również bomby - znaki '*',
# które wymazują przyległe litery, na przykład:
# aa*aa => a__a
# aa => ____

# Przykład stringów:
# zzzz*s*
# www*www****z
# *zd*qm*wp*bs*
def get_contest_list_after_bombs(contest_list):
    if "*" in contest_list:
        position = contest_list.index("*")
        if position < len(contest_list) - 1:
            del contest_list[position - 1]
            del contest_list[position + 1]
        else:
            del contest_list[position - 1]
    return contest_list
def get_left_score(contest_list):
    left_score = 0
    for letter in contest_list:
        if letter == "w":
            left_score += 4
        if letter == "p":
            left_score += 3
        if letter == "b":
            left_score += 2
        if letter == "s":
            left_score += 1
    return left_score

def get_right_score(contest_list):
    right_score = 0
    for letter in contest_list:
        if letter == "m":
            right_score += 4
        if letter == "q":
            right_score += 3
        if letter == "d":
            right_score += 2
        if letter == "z":
            right_score += 1
    return right_score

def print_letter_battle_result(left_score, right_score):
    if left_score == right_score:
        print(" It's a draw! ")
    elif left_score > right_score:
        print(" Left side won! ")
    else:
        print(" Right side won!")




contest_string = input("Please type in the contest string: ")
contest_list = list(contest_string)
contest_list = get_contest_list_after_bombs(contest_list)
left_score = get_left_score(contest_list)
right_score = get_right_score(contest_list)
print_letter_battle_result(left_score, right_score)