import numpy as np
import configparser
from datetime import datetime
import json


def _offset_pledge_lists(pledges_lists, ref_date_pledges):
    """
    Offsets all pledge lists so that the 0th element is today's pledge.

    :param pledges_lists: Should contain three lists of pledge names. One for each pledge giver.
    :return: list of lists
    """

    # Container
    reordered_pledges_lists = []

    for pledges, todays_pledge in zip(pledges_lists, ref_date_pledges):
        # Find out the index of today's pledge and reverse it
        offset = pledges.index(todays_pledge) * -1

        # Offset the list by n_offset elements
        pledges = list(np.roll(pledges, offset))

        reordered_pledges_lists.append(pledges)

    return reordered_pledges_lists


def pledge_by_date(ref_date, query_date, pledges) -> str:
    """
    :param ref_date: The date of reference
    :param query_date: The query date
    :param pledges:  The list of pledges. 0th is expected to be the one of reference date.
    :return: The name of the pledge
    """

    # Count how many days between today and the reference date
    delta = (query_date - ref_date).days
    count = len(pledges)

    return pledges[delta % count]


def get_ref_date(config_path):
    """
    Read the reference date from config.ini and returns it as a datetime object
    :return: datetime
    """

    # Load the configuration file
    config = configparser.ConfigParser()
    config.read(config_path)

    # Get the reference date in format yyyy/m/d
    return datetime.strptime(config.get('Reference', 'Date'), '%Y/%m/%d').date()


def pledges_reordered_by_config_date(config_path: str) -> list:
    """
    Reads the config.ini and returns list containing 3 lists. Each list contains that pledge
    givers' pledges ordered so that 0th item is as of reference date.

    :param config_path: File path to the config.ini file
    :return: Dungeon names in nested format as of: list<list<str>>
    """

    # Load the configuration file
    config = configparser.ConfigParser()
    config.read(config_path)

    # Difficulty levels as they appear in the config.ini
    difficulties = ('Easy', 'Mid', 'DLC')

    # Get the reference date's pledges
    ref_date_pledges = [config.get('Reference', d) for d in difficulties]

    # Load the list of all pledges
    pledges_lists = [json.loads(config.get('Pledges', d)) for d in difficulties]

    # Print stats
    print(
        f'Counts of different pledges: Easy:{len(pledges_lists[0])}, Mid:{len(pledges_lists[1])}, DLC:{len(pledges_lists[2])}')

    # Order the lists
    return _offset_pledge_lists(pledges_lists, ref_date_pledges)
