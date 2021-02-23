import csv

with open('10k.csv', newline='') as tenK_data:
    tenK_data_dict = csv.DictReader(tenK_data, delimiter=';')
    hours_list = []
    for row in tenK_data_dict:
        hours_list.append(row['Hours'])

print(hours_list)

total_hours = 0

for item in hours_list:
    total_hours += float(item)

print(total_hours)

with open('10k.csv', newline='') as tenK_data:
    tenK_data_dict = csv.DictReader(tenK_data, delimiter=';')
    days_list = []
    for row in tenK_data_dict:
        days_list.append(row['Date'])

print(days_list)

total_days = len(days_list)
print(total_days)

goal = total_days * 3
current_pace = total_hours
how_far_behind_goal = goal - current_pace
print(how_far_behind_goal)
