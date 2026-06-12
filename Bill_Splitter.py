import random

friends = ['Ramesh','Sunita','Bikash','Anjali','Dipak']
total_bill = 3750

def split_bill(friends,total):
    return total / len(friends)

def pick_lucky(friends):
    lucky = random.choice(friends)
    return lucky

def final_summary(friends,total):

    share = split_bill(friends,total)
    lucky = pick_lucky(friends)

    for i in range(len(friends)):
        print(f'{friends[i]} : {share}')
    print(f'The lucky person who pays extra NPR 50 is {lucky}')
    lucky_share = share + 50 
    print(f'{lucky} : {lucky_share}')

final_summary(friends,total_bill)


