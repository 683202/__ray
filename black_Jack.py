
'''

    ## BLACKJACK GAME.
    ## THIS CODE ONLY IMPLEMENTS THE 'hit' AND 'stay' ACTIONS AS IN A STANDARD BLACKJACK GAME.
    ## COMPUTER IS THE DEALER IN THIS GAME.
    ## RAJEEV RANJAN
    ## April 5, 2k18

'''


import random


class Deck() :

    available_no_of_cards = 52
    types_of_cards_available = 4
    numbered_cards = [x for x in range(2, 11)] * 4 ## 0
    random.shuffle(numbered_cards)
    kings = 4 ## 1
    queens = 4 ## 2
    jacks = 4 ## 3
    aces = 4 ## 4

    count = 0

    def __init__(self) :
        pass

    def adjust_deck(self, type_of_card) :

        if type_of_card == 'queens' :

            if Deck.queens > 0 :

                Deck.queens -= 1
                Deck.count += 1
                # if Deck.queens == 0 :
                #     Deck.types_of_cards_available -= 1
            else :
                return -1

        elif type_of_card == 'jacks' :

            if Deck.jacks > 0 :

                Deck.jacks -= 1
                Deck.count += 1
                # if Deck.jacks == 0 :
                #     Deck.types_of_cards_available -= 1
            else :
                return -1

        elif type_of_card == 'aces' :

            if Deck.aces > 0 :

                Deck.aces -= 1
                Deck.count += 1
                # if Deck.aces == 0 :
                #     Deck.types_of_cards_available -= 1
            else :
                return -1

        else :

            if Deck.kings > 0 :

                Deck.kings -= 1
                Deck.count += 1
                # if Deck.kings == 0 :
                #     Deck.types_of_cards_available -= 1
            else :
                return -1

    def pick_a_card(self) :

        while Deck.count < 52 :

            card = random.randint(1, 100) % 5
            # print('card type {}'.format(card))

            if card == 0 :

                if self.adjust_deck('queens') == -1 :
                    # print('-1 returned..')
                    continue
                else :
                    return ('queen', 10, 10, False)

            elif card == 1 :

                if self.adjust_deck('jacks') == -1 :
                    # print('-1 returned..')
                    continue
                else :
                    return ('jack', 10, 10, False)

            elif card == 2 :

                if self.adjust_deck('aces') == -1 :
                    continue
                else :
                    return ('ace', 1, 11, False)

            elif card == 3 :
                if self.adjust_deck('kings') == -1 :
                    continue
                else :
                    return ('king', 10, 10, False)

            else :

                if len(Deck.numbered_cards) == 0 :
                    continue

                else :

                    random_index = random.randint(0, 100) % len(Deck.numbered_cards)
                    card = Deck.numbered_cards[random_index]
                    del(Deck.numbered_cards[random_index])
                    Deck.count += 1
                    return (card, card, card, False)

class Dealer() :

    def __init__(self, deck_object, balance) :

        self.cards = []
        self.total_sum_list = [0]
        self.balance = balance
        self.cards.append(deck_object.pick_a_card())
        temp_var = (self.cards[0][0], self.cards[0][1], self.cards[0][2], True)
        self.cards[0] = temp_var
        self.cards.append(deck_object.pick_a_card())
        self.hit_count = 0

        for eachCard in self.cards :

            if eachCard[0] == 'ace' :

                if len(self.total_sum_list) == 1 :

                    self.total_sum_list = [x + 1 for x in self.total_sum_list]
                    self.total_sum_list += [x + 10 for x in self.total_sum_list]

                else :

                    self.total_sum_list += [x + 1 for x in self.total_sum_list ]
                    self.total_sum_list += [x + 10 for x in self.total_sum_list]

            else :

                if len(self.total_sum_list) == 1 :

                    self.total_sum_list = [x + eachCard[1] for x in self.total_sum_list ]

                else :

                    self.total_sum_list += [x + eachCard[1] for x in self.total_sum_list ]

        self.total_sum_list = [x for x in self.total_sum_list if x <= 21]
        self.total_sum_list = list(set(self.total_sum_list))

    def hit(self, deck_object) :

        current_card = deck_object.pick_a_card()
        self.hit_count += 1
        self.cards.append(current_card)

        if current_card[0] == 'ace' :

            if len(self.total_sum_list) == 0 :
                self.total_sum_list = [1, 11]

            else :

                self.total_sum_list = [x + 1 for x in self.total_sum_list]
                self.total_sum_list += [x + 10 for x in self.total_sum_list]

        else :

            if len(self.total_sum_list) == 0 :

                self.total_sum_list = [current_card[1]]

            else :

                self.total_sum_list = [x + current_card[1] for x in self.total_sum_list]

        self.total_sum_list = [x for x in self.total_sum_list if x <= 21]
        self.total_sum_list = list(set(self.total_sum_list))

        return self.total_sum_list

    def stay(self) :

        return self.total_sum_list

    def get_max_val(self) :

        if len(self.total_sum_list) == 0 :
            return 22

        else :
            return max(self.total_sum_list)


    def get_min_val(self) :

        if len(self.total_sum_list)  == 0 :
            return 22

        return min(self.total_sum_list)

    def print_cards_but_hidden(self) :

        temp_list = []

        for eachCard in self.cards :

            if not eachCard[3] :

                temp_list += (eachCard, )

        print(f"Dealer's face up cards : {temp_list}")

    def print_dealers_cards(self) :

        temp_list = []
        for eachCard in self.cards :
            temp_list += (eachCard, )
        # print(f"Dealer's hands {self.cards}\n")
        print(f"Dealer's hand : {temp_list}")

    def update_balance(self, value) :

        self.balance += value

    def get_balance(self) :

        return self.balance

    def has_blackjack(self) :

        return self.hit_count == 0 and 21 in self.total_sum_list


class Player() :

    def __init__(self, deck_object, balance, bet) :

        self.bet = bet
        self.balance = balance - bet
        if bet > balance :
            print('cannot place bet..')
            return

        self.cards = []
        self.total_sum_list = [0]
        self.cards.append(deck_object.pick_a_card())
        self.cards.append(deck_object.pick_a_card())
        self.hit_count = 0

        for eachCard in self.cards :

            if eachCard[0] == 'ace' :

                if len(self.total_sum_list) == 1 :

                    self.total_sum_list = [x + 1 for x in self.total_sum_list]
                    self.total_sum_list += [x + 10 for x in self.total_sum_list]

                else :

                    self.total_sum_list = [x + 1 for x in self.total_sum_list ]
                    self.total_sum_list += [x + 10 for x in self.total_sum_list]

            else :

                if len(self.total_sum_list) == 1 :

                    self.total_sum_list = [x + eachCard[1] for x in self.total_sum_list ]

                else :

                    self.total_sum_list = [x + eachCard[1] for x in self.total_sum_list ]

        self.total_sum_list = [x for x in self.total_sum_list if x <= 21]
        self.total_sum_list = list(set(self.total_sum_list))

    def hit(self, deck_object) :

        new_card = deck_object.pick_a_card()
        self.cards.append(new_card)
        self.hit_count += 1

        if new_card == 'ace' :

            self.total_sum_list = [x + 1 for x in self.total_sum_list]
            self.total_sum_list += [x + 10 for x in self.total_sum_list]

        else :

            self.total_sum_list = [x + new_card[1] for x in self.total_sum_list]

        self.total_sum_list = [x for x in self.total_sum_list if x <= 21]
        self.total_sum_list = list(set(self.total_sum_list))

        return self.total_sum_list

    def stay(self) :

        return self.total_sum_list

    def is_it_21(self) :

        return 21 in self.total_sum_list

    def get_max_val(self) :

        if len(self.total_sum_list) == 0 :
            return 22

        return max(self.total_sum_list)

    def get_min_val(self) :

        if len(self.total_sum_list)  == 0 :
            return 22

        return min(self.total_sum_list)

    def print_players_cards(self) :

        print(f"Player's hand: {self.cards}\n")

    def set_bet(self, value) :

        self.bet = value

    def get_bet(self) :

        return self.bet

    def update_balance(self, value) :

        self.balance += value

    def double_bet(self) :

        self.bet *= 2

    def get_balance(self) :

        return self.balance

    def has_blackjack(self) :

        return self.hit_count == 0 and 21 in self.total_sum_list

def play_game(dealer_object, player_object, deck_object) :

    player_object.print_players_cards()
    dealer_object.print_cards_but_hidden()

    turn = True ## Its player's turn.

    if player_object.has_blackjack() and dealer_object.has_blackjack() :

        dealer_object.print_dealers_cards()
        print("Player and dealer both have blackjacks..Player's bet is returned. Player's balance : {player_object.get_balance()}")
        player_object.update_balance(player_object.get_bet())
        player_object.set_bet(0)
        return player_object.get_balance()

    elif player_object.has_blackjack() :

        dealer_object.print_dealers_cards()
        player_object.double_bet()
        player_object.update_balance(player_object.get_bet())
        print(f"Player has blackjack. Bet doubled. Player's updated balance : {player_object.get_balance()}")
        return player_object.get_balance()

    else :

        while True :

            if turn :
                
                # player_object.print_players_cards()
                choice = input('\nHit or Stay ?: ')

                if choice.lower() == 'hit' :

                    player_object.hit(deck_object)
                    player_object.print_players_cards()
                    player_min_value = player_object.get_min_val()
                    # print(f" Player's  min value : {player_min_value}")

                    if player_min_value > 21 :

                        print('Player busts ! Lost bet')
                        print(f"Player's updated balance {player_object.get_balance()}")
                        dealer_object.update_balance(player_object.get_bet())
                        player_object.set_bet(0)
                        return player_object.get_balance()

                elif choice.lower() == 'stay' :

                    player_object.stay()
                    turn = False

                else :

                    continue

            else :

                dealer_object.print_dealers_cards()

                if dealer_object.has_blackjack() :

                    dealer_object.update_balance(player_object.get_bet())
                    player_object.set_bet(0)
                    print(f"Dealer has blackjack... Player loses bet..Player's updated balance : {player_object.get_balance()}")
                    return player_object.get_balance()

                if dealer_object.get_max_val() < 17 :

                    while dealer_object.get_max_val() < 17 :

                        dealer_object.hit(deck_object)

                if dealer_object.get_max_val() < 21 and dealer_object.get_max_val() < player_object.get_max_val() :

                    lis = [x for x in range(0, 100)]
                    lis = random.shuffle(lis)
                    random_choice = lis[0] % 2

                    if random_choice == 1 :

                        dealer_object.hit(deck_object)

                    else :

                        dealer_object.stay()

                player_max_val = player_object.get_max_val()
                # print(f'player max val is {player_max_val}')
                dealer_max_val = dealer_object.get_max_val()
                # dealer_min_value = dealer_object.get_min_val()
                # print(f"dealer's min value: {dealer_min_value}")
                dealer_object.print_dealers_cards()
                dealer_object.stay()

                if dealer_object.get_min_val() > 21 :

                    player_object.update_balance(player_object.get_bet() * 2)
                    print(dealer_object.print_dealers_cards())
                    print(f"Dealer busts.! Player's bet doubles. Player's new balance {player_object.get_balance()}")
                    return player_object.get_balance()

                if dealer_max_val <= 21 and player_max_val <= 21 and dealer_max_val > player_max_val :

                    print('Dealer wins!.. Player lose the bet.')
                    dealer_object.update_balance(player_object.get_bet())
                    player_object.set_bet(0)
                    print(f"Player's updated balance : {player_object.get_balance()}")
                    # player_object.bet = 0
                    return player_object.get_balance()

                if dealer_max_val <= 21 and player_max_val <= 21 and dealer_max_val < player_max_val :

                    print('Player wins... Bet doubled..')
                    dealer_object.update_balance(-1 * player_object.get_bet())
                    player_object.double_bet()
                    player_object.update_balance(player_object.get_bet())
                    player_object.set_bet(0)
                    print(f"Player's balance {player_object.get_balance()}")
                    return player_object.get_balance()

                if dealer_max_val <= 21 and player_max_val <= 21 and dealer_max_val == player_max_val :

                    print("It's a tie.. Player's bet returned")
                    player_object.update_balance(player_object.get_bet())
                    print(f" Player's updated balance is : {player_object.get_balance()}")
                    player_object.set_bet(0)
                    return player_object.get_balance()

                turn = True

def main() :

    balance = 0

    while True :

        while balance <= 0 :
            try :

                balance = int(input('Balance amount. ?: '))

            except :
                continue

            if balance > 0 :
                break
            else :
                continue

        print('\n\n ********************************  Initialising Game. ******************************* \n\n\n')

        deck_object = Deck()
        dealer_balance = float('inf')
        dealer_object = Dealer(deck_object, dealer_balance)

        while True :

            try :

                bet = int(input('Bet amount. ?: '))
                print('\n')
                break

            except :

                continue


        if bet > balance :
            continue

        player_object = Player(deck_object, balance, bet)
        balance = play_game(dealer_object, player_object, deck_object)

        while True :
            choice = input('\nAnother One (Y / N)? : ')

            if choice == 'n' or choice == 'N' :
                return
            elif choice == 'y' or choice == 'Y' :
                break
            else :
                continue

if __name__ == '__main__' :

    main()
