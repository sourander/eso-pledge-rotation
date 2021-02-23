from datetime import date, timedelta
from helpers.pledgetools import offset_pledge_lists, pledge_by_date

#############
# CONFIG ME #
#############
# Reference date - when the pledges of 'today' have been set below
ref_date = date(2021, 1, 1)

# Pledges today (or as of the reference date)
ez_on_ref_date = "Fungal Grotto I"
mid_on_ref_date = "Selene's Web"
dlc_on_ref_date = "Stone Garden"

# Names in the order or easy, medium, dlc
givers = ["Maj al-Ragath", "Glirion the Redbeard", "Urgarlag Chief-bane"]

pledges_eaz = ["Spindleclutch II", "Banished Cells I", "Fungal Grotto II",
               "Spindleclutch I", "Darkshade II", "Elden Hollow I",
               "Wayrest Sewers II", "Fungal Grotto I", "Banished Cells II",
               "Darkshade Caverns I", "Elden Hollow II", "Wayrest Sewers I"]

pledges_mid = ["Direfrost Keep", "Vaults of Madness", "Crypt of Hearts II",
               "City of Ash I", "Tempest Island", "Blackheart Haven",
               "Arx Corinium", "Selene's Web", "City of Ash II",
               "Crypt of Hearts I", "Volenfell", "Blessed Crucible"]

pledges_dlc = ["Falkreath Hold", "Fang Lair", "Scalecaller Peak", "Moon Hunter Keep",
               "March of Sacrifices", "Depths of Malatar", "Frostvault", "Moongrave Fane",
               "Lair of Maarselok", "Icereach", "Unhallowed Grave", "Stone Garden", "Castle Thorn",
               "Imperial City Prison", "Ruins of Mazzatun", "White-Gold Tower",
               "Cradle of Shadows", "Bloodroot Forge"]


# Reorder lists so that the 0th element is on reference day.
pledges_lists = offset_pledge_lists([pledges_eaz, pledges_mid, pledges_dlc],
                                    [ez_on_ref_date, mid_on_ref_date, dlc_on_ref_date])

# Print stats
print(f'Counts of different pledges: Easy:{len(pledges_eaz)}, Mid: {len(pledges_mid)}, DLC:{len(pledges_dlc)}')


###################
# FIND THE MONDAY #
###################
today = date.today()
monday_date = today - timedelta(days=today.weekday())


##########
# Print ##
##########

print(f'WEEK: {monday_date.isocalendar()[1]}')
print(f" ")
print(f"{'day yyyy-mm-dd':<19}{givers[0]:<25}{givers[1]:<25}{givers[2]}")
print("="*89)

for n in range(7):
    # Today + n days
    n_day = monday_date + timedelta(days=n)

    # Date stuff for printing purposes
    isodate = n_day.isoformat()
    weekday = n_day.strftime('%a')

    # Easy, Medium and DLC Pledges
    eaz = pledge_by_date(ref_date, n_day, pledges_lists[0])
    mid = pledge_by_date(ref_date, n_day, pledges_lists[1])
    dlc = pledge_by_date(ref_date, n_day, pledges_lists[2])

    print(f"{weekday:<4} {isodate:<15}{eaz:<25}{mid:<25}{dlc}")

    print(f" ")