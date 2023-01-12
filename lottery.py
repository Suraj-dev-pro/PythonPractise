"""Simulate the powerball lottery using python Correy Schafer's tutorial """
import random
import json

white_possibles = list(range(1,70))
red_possibles = list(range(1,27))

tickets_per_drawing = 10000
num_drawing = 9999

total_spent = 0
earnings =0

times_won = {
    "5+p":0,
    "5":0,
    "4+p":0,
    "4":0,
    "3+p":0,
    "3":0,
    "2+p":0,
    "1+p":0,
    "p":0,
    "0":0
}

def calc_win_amt(my_numbers,winning_numbers):
    win_amt = 0
    white_matches=len(my_numbers["white"].intersection(winning_numbers["white"]))
    power_match = my_numbers["red"] == winning_numbers["red"]
    
    if white_matches == 5:
        if power_match:
            win_amt = 2_000_000_000
            times_won["5+p"] +=1
        else:
            win_amt = 1_000_000
            times_won["5"] +=1
    elif white_matches == 4:
        if power_match:
            win_amt = 50_000
            times_won["4+p"] +=1
        else:
            win_amt = 100
            times_won["4"] +=1
    elif white_matches == 3:
        if power_match:
            win_amt = 100
            times_won["3+p"] +=1
        else:
            win_amt = 7
            times_won["3"] +=1
    elif white_matches == 2 and power_match:
            win_amt = 7
            times_won["2+p"] +=1
    elif white_matches == 1 and power_match:
            win_amt = 4
            times_won["1+p"] +=1
    elif power_match:
        win_amt = 4
        times_won["p"] +=1
    else:
        times_won["0"] +=1
        
    return win_amt
hit_jp = False
drawings = 0
years = 0
#for drawing in range (num_drawing):
while True:
    drawings +=1
    white_drawing = set(random.sample(white_possibles,k=5))
    red_drawing = random.choice(red_possibles)
    
    winning_numbers = {'white':white_drawing,'red':red_drawing}
    for ticket in range(tickets_per_drawing):
        total_spent += 2
        my_white = set(random.sample(white_possibles,k=5))
        my_red = random.choice (red_possibles)
        
        my_numbers = {'white':my_white,'red': my_red}
        
        win_amt = calc_win_amt (my_numbers,winning_numbers)
        earnings += win_amt
        
        if win_amt == 2_000_000_000:
            hit_jp = True
            break
        
    if drawings % 156 == 0:
        years+=1
        print(f'{years}years')    
        
    if hit_jp:
        break
        
print(f'Spent: ${total_spent:,}') 
print(f' Earnings: ${earnings:,} ')

print(json.dumps(times_won,indent=2))