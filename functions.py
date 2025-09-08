import random
import pandas as pd

# Names of participants in fantasy league
participants = []

def assign_draft_nums(players):
    # Randomize names list
    names = random.sample(players, k=len(players))
    
    # Randomize draft numbers
    num_participants = len(names)
    draft_nums = list(range(1, num_participants + 1))
    random_draft_nums = random.sample(draft_nums, k=len(draft_nums))
    
    # Assign random draft number to random name
    draft_order_assignment = {}
    
    for name in names:
        draft_order_assignment[name] = random.choice(random_draft_nums)
        random_draft_nums.remove(draft_order_assignment[name])
     
    # Return dictionary of names and assigned draft numbers   
    return draft_order_assignment
        
Draft_Order = assign_draft_nums(participants)

# Make table using a DataFrame
new = dict(sorted(Draft_Order.items(), key=lambda item: item[1]))
names = list(new.keys())
nums = list(new.values())
table = pd.DataFrame(data={'NAME':names, 'DRAFT NUMBER':nums})