import random
import art  # 로고 출력용

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def check_blackjack(hand):
    return 11 in hand and 10 in hand


def player_turn(player_cards):
    while True:
        current_score = calculate_score(player_cards)
        if current_score > 21:
            print("You went over 21! You lose.")
            return current_score

        more_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if more_card == 'y':
            player_cards.append(random.choice(cards))
            print(f"Your cards: {player_cards}, current score: {current_score}")
        else:
            break
    return current_score


def dealer_turn(dealer_cards):
    print(f"Dealer's initial hand: {dealer_cards}, initial score: {calculate_score(dealer_cards)}")
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        print(f"Dealer draws a card. Current hand: {dealer_cards}, current score: {calculate_score(dealer_cards)}")
    return calculate_score(dealer_cards)


def compare_scores(player_score, dealer_score):
    if player_score > 21:
        return "You lose. Your score went over 21."
    if dealer_score > 21:
        return "You win! Dealer's score went over 21."
    if player_score > dealer_score:
        return "You win!"
    elif player_score < dealer_score:
        return "You lose!"
    else:
        return "It's a draw!"


def play_game():
    print(art.logo)
    player_cards = random.choices(cards, k=2)
    dealer_cards = random.choices(cards, k=2)

    print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")

    if check_blackjack(player_cards) or check_blackjack(dealer_cards):
        if check_blackjack(player_cards) and check_blackjack(dealer_cards):
            print("Both have Blackjack! It's a draw.")
        elif check_blackjack(player_cards):
            print("You win with a Blackjack!")
        else:
            print("Computer wins with a Blackjack!")
        return

    player_score = player_turn(player_cards)
    if player_score > 21:
        return

    dealer_score = dealer_turn(dealer_cards)
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    result = compare_scores(player_score, dealer_score)
    print(result)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()