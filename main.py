from roulette_info import process_bet

import random


base_bet = 100
bet_info1 = {
    # "Straight Up 12": base_bet*1,
    "Odd": base_bet*2,
    "Even": base_bet*2
}
total_bet: int = sum([v for v in bet_info1.values()])
print(f"TOTAL BET IS: {total_bet}")


def roll_and_record(bet_info) -> int:
    roll = random.randint(0, 36)
    # print(f"AND THE ROLL IS {roll}")

    final_money = process_bet(roll, bet_info=bet_info)
    # print(f"FINAL MONEY: {final_money}")
    return final_money


simulations = 20000000

netprofit = sum([roll_and_record(bet_info1) for _ in range(simulations)])/simulations - total_bet
netprofit_percent = (netprofit / total_bet) * 100
print(f"\n{netprofit=:.2f}\n{netprofit_percent=:.2f}%")