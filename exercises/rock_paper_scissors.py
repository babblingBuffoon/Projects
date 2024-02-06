def rps(p1, p2):
    match p1 , p2:
        case "scissors" , "rock": return "Player 2 won!"
        case "rock" , "scissors": return "Player 1 won"
        case "rock" , "paper": return "player 2 won!"
        case "paper" , "rock": return "Player 1 won!"
        case "paper" , "scissors": return "Player 2 won!"
        case "scissors" , "paper": return "Player 1 won!"
        case _: return "Draw!"
        
        
def rps1(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


def rps2(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

print(rps2("rock" , "rock"))
print(0 - 0)