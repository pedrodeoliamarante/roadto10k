import pandas as pd

# importing csv
tenkdata = pd.read_csv('10k.csv', sep=';')

# creating sum of hours variable
total_hours = 0
for hour in tenkdata.Hours:
    total_hours += hour

# creating sum of days studied variable
total_days = len(tenkdata.Dates)

# creating how far behind goal variable
goal = total_days * 3
current_pace = total_hours
how_far_behind_goal = round(goal - current_pace, 2)


# function that determines pace change
def pace_change(days):
    total_hours_needed = round(how_far_behind_goal / days, 2)
    print(f"You are {how_far_behind_goal} hours behind your expected pace")
    print(
        f"To get back to your expected pace you need to study {total_hours_needed + 3} hours each day in the next {days} days, which is an increment of {total_hours_needed} hours.")


def how_long(total_hours_needed):
    days = round(how_far_behind_goal / total_hours_needed, 2)
    print(days)


how_long(0.5)
