import statistics
import random
from coleman_functions import get_int
def get_number_of_dice():
	print('\nWelcome to Spicy-Dice!\n')
	dice = get_int('How many dice will you be playing with? ')
	dice_list = []
	for i in range(1,dice+1):
		new_dice=get_int(f'How many faces for die {i}? ')
		print(f'D{new_dice} selected')
		dice_list.append(new_dice)
	return dice_list

def roll(dice):
	sum = 0
	for i in dice:
		sum += random.randint(1,i)
	return sum

def session(dice):
	rolls = []
	counter = 0
	while True:
		counter+=1
		option = input('Hit "enter" to roll, or type "q" to exit: ')
		if option == 'q':
			return rolls
		else:
			result = roll(dice)
			rolls.append(result)
			print(f'Your roll[{counter}]: {result}')

def optimal_session(dice):
	min_roll = len(dice)
	max_roll = sum(dice)
	roll_range = max_roll - min_roll+1
	reps =roll_range*500
	
	rolls = []
	
	for i in range(1,reps+1):
		result = roll(dice)
		rolls.append(result)
	return rolls


def print_histogram(rolls,scientific =False):
    if len(rolls) > 0:
        # Determine the range of dice values from the rolls
        min_roll = min(rolls)
        max_roll = max(rolls)
        max_roll_digits = len(str(max_roll))
        
        # Create a list to count occurrences of each dice value
        counts = [0] * (max_roll - min_roll + 1)
        
        # Count occurrences of each dice roll
        for roll in rolls:
            counts[roll - min_roll] += 1
        
        # Calculate statistics
        mean = round(sum(rolls) / len(rolls), 1)
        print('\nStatistics:')
        print(f'Average roll: {mean}')
        if len(rolls) > 1:
             std = round(statistics.stdev(rolls),1)
             print(f'Roll standard deviation: {std}')
        
        # Find the highest count
        max_count = max(counts)
        
        # Normalize counts if the highest count is greater than 20
        if max_count > 30:
            normalization_factor = 30 / max_count
            normalized_counts = [round(count * normalization_factor) for count in counts]
        else:
            normalized_counts = counts
        
        # Print the histogram
        for i in range(min_roll, max_roll + 1):
            new_count = normalized_counts[i-min_roll]
            non_normalized_count = counts[i-min_roll]
            digits = len(str(i))  # Number of digits for the current roll value
            string = f"{i}: {' ' * (max_roll_digits - digits)}{'*' *new_count}"
            string_len = len(string)
            if scientific:
                print(string+(34-string_len)*' '+f'{round(non_normalized_count/sum(counts)*100,1)}% {non_normalized_count:.2e}/{sum(counts):.2e}')
            else:
                print(string+(34-string_len)*' '+f'{round(non_normalized_count/sum(counts)*100,1)}% {non_normalized_count}/{sum(counts)}')

while True:
	
	dice = get_number_of_dice()

	rolls = session(dice)

	print_histogram(rolls)
	
	optimal_rolls = optimal_session(dice)

	print('\nCalculating an optimal distribution...')

	print_histogram(optimal_rolls)
	
	print('\nThanks for using Spicy-Dice!')

	replay = input('Enter "y" to play again: ')
	
	if replay != "y":
		print('\nGoodbye.\n')
		break
