import sys
import difflib
from datetime import date, datetime, timedelta
from helpers.pledgetools import pledge_by_date, pledges_reordered_by_config_date, get_ref_date

# Get the list of lists where 0th item of each list is the reference date's pledge
pledges_ordered = pledges_reordered_by_config_date('configs/pledges.ini')
ref_date = get_ref_date('configs/pledges.ini')

# For human-readability
givers = ['Maj', 'Glirion', 'Urgarlag']

# Ask what the user is looking for
query = input("Enter the dungeon name:")

if not any([query in x for x in pledges_ordered]):
    print("The dungeon you are looking does not exist.")
    print("Trying to find similar existing suggestions.")

    # Stitch all the pledges into a single list for similarity searching
    all_pledge_names = [item for sublist in pledges_ordered for item in sublist]

    # Find similar items
    suggestions = difflib.get_close_matches(query, all_pledge_names)

    # Toggle for avoiding sys exit
    suggestion_was_approved = False

    # Verbosity
    print(f"\nFound {len(suggestions)} suggestions.")

    for suggestion in suggestions:
        # Ask user for input
        s = input(f"Did you mean '{suggestion}'? Answer Y or YES.")
        s = s.lower()

        if s == 'y' or s == 'yes':
            # Use the suggestion
            query = suggestion

            # Toggle
            suggestion_was_approved = True
            break

    if not suggestion_was_approved:
        sys.exit("Quit since the dungeon name was invalid and no alternative was found or chosen.")

# Set pledge giver index
idx = [query in x for x in pledges_ordered].index(True)

# Only this giver's pledges
pledges = pledges_ordered[idx]

# Today
today = date.today()
found_date = None

# Search this giver's pledges
for n in range(len(pledges)):

    # Today + n days
    n_day = today + timedelta(days=n+1)

    # Query
    if query == pledge_by_date(ref_date, n_day, pledges):
        found_date = n_day
        break

assert found_date, f"The pledge '{query}' was not found in list: {pledges}."

# Pretty print
print(f"\nThe next run for the {query} is...")
print(f"In {(found_date - today).days} days from now")
print(f"In {found_date.strftime('%A, %B %d')}")
