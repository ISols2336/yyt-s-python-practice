from practaice_Poker import Suite, Card, Poker, Player
import time, random

cast = 10000
dealer = [Player('莉莉丝'), Player('柊筱娅'), Player('叶瞬光')]


def total_card(cards:Player.card):
    total = [i.num for i in cards]

    for i in range(len(total)):
        if total[i] > 10:
            total[i] = 10

    total_sum = sum(total)

    if any(num == 1 for num in total):

        if total_sum <= 11:
            total_sum += 10

    return total_sum


while cast > 0:

    poker = Poker()
    player = Player(input('请输入玩家名字'))
    pull_cast = int(input('请输入下注金额'))
    dealer_1 = random.choice(dealer)

    cast -= pull_cast
    time.sleep(2)
    print(f'本次庄家为{dealer_1}')

    while True:

        dealer_1.card = []
        player.card = []
        
        print(f'现在的资金{cast}')

        Poker.shuffle(poker)

        dealer_1.get_one(Poker.deal(poker))
        player.get_one(Poker.deal(poker))    
    
        print(f'庄家的手牌为{dealer_1.card}')
        time.sleep(1)
        print(f'玩家的手牌为{player.card}')

        y_or_n = input('是否继续摸牌？')

        while y_or_n == 'y':
    
            dealer_1.get_one(Poker.deal(poker))
            player.get_one(Poker.deal(poker))
    
            print(f'庄家的手牌为{dealer_1.card}')
            time.sleep(1)
            print(f'玩家的手牌为{player.card}')

            y_or_n = input('是否继续摸牌？')

        if total_card(player.card) <= 21:
            while total_card(dealer_1.card) < 17:
                dealer_1.get_one(Poker.deal(poker))
                time.sleep(1)
                print(f'庄家的手牌为{dealer_1.card}')


        if total_card(player.card) > 21:
            print(f'庄家{dealer_1}获胜')

        elif total_card(dealer_1.card) > 21:
            print(f'玩家{player}获胜')
            cast += pull_cast*2

        elif total_card(dealer_1.card) > total_card(player.card) and total_card(dealer_1.card) <= 21:
            print(f'庄家{dealer_1}获胜')

        elif total_card(dealer_1.card) < total_card(player.card) and total_card(player.card) <= 21:
            print(f'玩家{player}获胜')
            cast += pull_cast*2

        else:
            print('平局')
            cast += pull_cast
                
        break