import numpy as np


def offset_pledge_lists(pledges_lists, ref_date_pledges):
    '''
    Offsets all pledge lists so that the 0th element is today's pledge.
    :param pledges_lists: Should contain three lists of pledge names. One for each pledge giver.
    :return: list of lists
    '''

    # Container
    reordered_pledges_lists = []

    for pledges, todays_pledge in zip(pledges_lists, ref_date_pledges):
        # Find out the index of today's pledge and reverse it
        offset = pledges.index(todays_pledge) * -1

        # Offset the list by n_offset elements
        pledges = np.roll(pledges, offset)

        reordered_pledges_lists.append(pledges)

    return reordered_pledges_lists


def pledge_by_date(query_date, ref_date, pledges):

    # Count how many days between today and the reference date
    delta = (ref_date - query_date).days
    count = len(pledges)

    return pledges[delta % count]
