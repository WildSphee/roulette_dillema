from typing import Dict, List

"""
Roulette is a popular casino game that offers a variety of bets, each with its own payout. 
Below are some of the most common bets found on a roulette table, along with their corresponding payouts
This table as 0-36 (no 00)

Straight Up	One single number	35:1
Split	Two connected numbers	17:1
Street	Three connected numbers vertically	11:1
Trio	Three numbers using the 0 and/or 00	11:1
Corner/Square	Four connected numbers to form a square	8:1
Basket/5 Number Bet	Five numbers using the 0 and the 00	6:1
Line/Double Street	Six connected numbers vertically	5:1
Column	Line of 12 numbers	2:1
Dozen	1st, 2nd, or 3rd grid of 12 numbers	2:1
Low	Grid of 1-18	1:1
High	Grid of 19-36	1:1
Even/Odd	Bet on all the even or odd numbers	1:1
Red/Black	Bet on all the red or black numbers	1:1
"""

# The bet contains info of all types of bets available and their pay
# denoted by [name of bet, 1:pay]
bet: Dict[str, int] = {}

# Straight Up	One single number	35:1
bet.update({f"Straight Up {n}": 35 + 1 for n in range(37)})

# Even/Odd	Bet on all the even or odd numbers	1:1
bet.update({"Even": 2})
bet.update({"Odd": 2})

# Red/Black	Bet on all the red or black numbers	1:1
bet.update({"Red": 2})
bet.update({"Black": 2})


# numbers and their triggers
# denoted ny [number to bet on: List of items to trigger[item1, item2]]
triggers: Dict[int, List[str]] = {}

triggers.update({n: [f"Straight Up {n}"] for n in range(37)})

for k, v in triggers.items():
    # 0 doesn't count towards black or red or even or odd
    if k == 0:
        continue
    
    if k % 2 == 0:
        triggers[k].append("Even")
    else:
        triggers[k].append("Odd")
    
    if k in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        triggers[k].append("Red")
    else:
        triggers[k].append("Black")


def process_bet(roll: int, bet_info: Dict[str, int]) -> int:
    """
    process the final money gain based on the bet and bet amount on each item

    args:
        roll: roll number
        bet_info: the information of a bet
    Returns:
        int: final monetary gain
    """
    final_money = 0
    list_of_winning_bets = triggers[roll]
    
    for k, v in bet_info.items():
        if k not in list_of_winning_bets:
            continue

        final_money += bet[k] * v
    
    return final_money