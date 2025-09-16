import random

# 初始化扑克牌
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [r + s for s in suits for r in ranks]

# 计算点数
def calculate_score(hand):
    values = []
    for card in hand:
        rank = card[:-1]
        if rank in ['J', 'Q', 'K']:
            values.append(10)
        elif rank == 'A':
            values.append(11)  # 先按11算
        else:
            values.append(int(rank))
    total = sum(values)
    # 如果爆点就把A算1
    while total > 21 and 11 in values:
        values[values.index(11)] = 1
        total = sum(values)
    return total

# 发牌函数
def deal(deck):
    return deck.pop()

def blackjack():
    random.shuffle(deck)
    player = [deal(deck), deal(deck)]
    dealer = [deal(deck), deal(deck)]

    print("你的手牌:", player, "分数:", calculate_score(player))
    print("庄家的明牌:", dealer[0])

    # 玩家回合
    while calculate_score(player) < 21:
        action = input("要牌(h)还是停牌(s)? ").lower()
        if action == 'h':
            player.append(deal(deck))
            print("你的手牌:", player, "分数:", calculate_score(player))
        else:
            break

    if calculate_score(player) > 21:
        print("你爆牌了，庄家赢！")
        return

    # 庄家回合
    print("庄家的手牌:", dealer, "分数:", calculate_score(dealer))
    while calculate_score(dealer) < 17:
        dealer.append(deal(deck))
        print("庄家要牌:", dealer, "分数:", calculate_score(dealer))

    # 胜负比较
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    if dealer_score > 21 or player_score > dealer_score:
        print("你赢了！")
    elif player_score == dealer_score:
        print("平局！")
    else:
        print("庄家赢！")

blackjack()
