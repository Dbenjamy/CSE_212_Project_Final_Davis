# This is one way to implement 'intersection':

def find_openings(sched1,sched2):
    openings = set()
    for item in sched1:
        # Remember that checking for membership
        # is very efficient.
        if item in sched2:
            openings.add(item)
    return openings


stacy_schedule = {'9AM','10AM','12PM','1PM','2PM','4PM','5PM'}
markus_schedule = {'7AM','8AM','11PM','2PM','3PM'}

print(find_openings(stacy_schedule,markus_schedule))