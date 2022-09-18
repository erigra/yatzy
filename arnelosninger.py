def calc_yatzy_score(dice):
    # Calculate the score for a given set of five dice values in yatzy.
    # Parameters: dice (list of int): List of dice values [1..6]
    assert len(dice) == 5

    # Build a list of the frequency of each dice number/value e.g. (1,3,3,6,6) -> (1,0,2,0,0,2)
    # In this example: one 1's, zero 2's, two 3's, zero 4's, zero 5's and two 6's.
    number_counts = []
    for dice_value in range(1, 7):     # loops through values 1..6
        number_counts.append(dice.count(dice_value))

    print(f'Dice:         {dice}')
    print(f'Number count: {number_counts}')

    # Scores for dice values
    for dice_value in range(1, 7):
        frequency = number_counts[dice_value - 1]  # The list starts at index 0, not 1, so have to subtract 1
        if frequency >= 1:
            print(f"Number of {dice_value}'s: {frequency}, score: {dice_value * frequency}")

    # Yatzy
    if 5 in number_counts:
        print('Yatzy, score: 50')

    # Four of a kind
    if max(number_counts) >= 4:
        # The index starts at 0, so have to add 1 to get the dice_value
        dice_value = number_counts.index(max(number_counts)) + 1
        print(f"Four {dice_value}'s, score: {4 * dice_value}")

    # Three of a kind
    if max(number_counts) >= 3:
        dice_value = number_counts.index(max(number_counts)) + 1
        print(f"Three {dice_value}'s, score: {3 * dice_value}")

    # House
    if 2 in number_counts and 3 in number_counts:
        print(f"House, score: {sum(dice)}")

    # Sequence
    if max(number_counts) == 1:
        print(f"Sequence, score: {sum(dice)}")

    # One pair, find pair with largest dice value if more than one pair.
    # Use list comprehension to get list of pair values.
    # It basically find all indices in number_counts (=dice value - 1) where there are at least two dice.
    # The i + 1 part is to correct for the fact that indices in Python go from [0..n-1],
    # but dice values go from [1..n].
    pair_values = [i + 1 for i in number_counts if number_counts[i] >= 2]
    if len(pair_values) >= 1:  # at least one pair, select largest dice value
        print(f"One pair {max(pair_values)}'s, score: {2 * max(pair_values)}")

    # Two pairs
    if len(pair_values) == 2:  # two pairs
        print(f"Two pairs {pair_values}, score: {2 * sum(pair_values)}")

    # Chance
    print(f'Chance, score: {sum(dice)}')


if __name__ == '__main__':
    throw = [4, 4, 3, 3, 3]
    calc_yatzy_score(throw)