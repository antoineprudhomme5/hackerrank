from math import ceil

MAX_EXPENDITURE_AMOUNT = 200


def get_median_from_counts(counts, d):
    median = 0

    if d % 2 == 0:
        count = 0
        m1 = None
        m2 = None
        for i in range(len(counts)):
            count = count + counts[i]
            if m1 is None and count >= d / 2:
                m1 = i
            if m2 is None and count >= (d / 2) + 1:
                m2 = i
                break
        median = (m1 + m2) / 2
    else:
        count = 0
        for i in range(len(counts)):
            count = count + counts[i]
            if count >= d / 2:
                median = i
                break

    return median


def activity_notifications(expenditures, d):
    counts = [0] * (MAX_EXPENDITURE_AMOUNT + 1)
    notif_count = 0

    # init count array
    for i in range(d):
        counts[expenditures[i]] = counts[expenditures[i]] + 1

    for i in range(d, len(expenditures)):
        median = get_median_from_counts(counts, d)

        if expenditures[i] >= (median * 2):
            notif_count = notif_count + 1

        # update counts for next step
        counts[expenditures[i-d]] = counts[expenditures[i-d]] - 1
        counts[expenditures[i]] = counts[expenditures[i]] + 1

    return notif_count
