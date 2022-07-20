from datetime import date, timedelta
from helpers.pledgetools import pledge_by_date, pledges_reordered_by_config_date, get_ref_date

# Get the list of lists where 0th item of each list is the reference date's pledge
pledges_ordered = pledges_reordered_by_config_date('configs/pledges.ini')
ref_date = get_ref_date('configs/pledges.ini')

###################
# FIND THE MONDAY #
###################
today = date.today()
monday_date = today - timedelta(days=today.weekday())

# If it is Sunday, change to next week
if today.weekday() == 6:
    monday_date = monday_date + timedelta(days=7)

givers = ['Maj', 'Glirion', 'Urgarlag']

##########
# Print ##
##########

print(f'WEEK: {monday_date.isocalendar()[1]}')
print(f" ")
print(f"{'day yyyy-mm-dd':<20}{givers[0]:<25}{givers[1]:<25}{givers[2]}")
print("=" * 89)

for n in range(7):
    # Today + n days
    n_day = monday_date + timedelta(days=n)

    # Date stuff for printing purposes
    isodate = n_day.isoformat()
    weekday = n_day.strftime('%a')

    # Easy, Medium and DLC Pledges
    eaz = pledge_by_date(ref_date, n_day, pledges_ordered[0])
    mid = pledge_by_date(ref_date, n_day, pledges_ordered[1])
    dlc = pledge_by_date(ref_date, n_day, pledges_ordered[2])

    print(f"{weekday:<4} {isodate:<15}{eaz:<25}{mid:<25}{dlc}")

    print(f" ")
