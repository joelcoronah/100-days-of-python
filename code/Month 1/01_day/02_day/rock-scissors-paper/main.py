import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors \n")
    pc = random.choice(['r', 'p', 's'])

    if user == pc:
        return 'tie HAHA!'

    if how_win(user, pc):
        return 'U win, U rock!!'

    return 'Looser!'
    


def how_win(player, opponent):
    if (player =='r' and opponent=='s') or (player =='s' and opponent=='p') \
        or (player =='p' and opponent=='r'):
        return True;

print(play())
