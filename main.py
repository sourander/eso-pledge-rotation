import configparser
import json
from datetime import date, datetime, timedelta
from helpers.pledgetools import offset_pledge_lists, pledge_by_date

# CONFIG
config_path = 'configs/pledges.ini'

# Load the configuration file
config = configparser.ConfigParser()
config.read(config_path)

# Get the reference date in format yyyy/m/d
ref_date = datetime.strptime(config.get('Reference', 'Date'), '%Y/%m/%d').date()

# Difficulty levels as they appear in the config.ini
difficulties = ('Easy', 'Mid', 'DLC')

# Get the reference date's pledges
ref_date_pledges = [config.get('Reference', d) for d in difficulties]

# Load the list of all pledges
pledges_lists = [json.loads(config.get('Pledges', d)) for d in difficulties]

# Order the lists
pledges_ordered = offset_pledge_lists(pledges_lists, ref_date_pledges)


# Print stats
print(f'Counts of different pledges: Easy:{len(pledges_lists[0])}, Mid: {len(pledges_lists[1])}, DLC:{len(pledges_lists[2])}')


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
print("="*89)

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
