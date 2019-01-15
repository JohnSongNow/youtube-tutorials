import random as random


def schedule_jobs(jobs, length):
    '''
    Returns a schedule that maximzes the payoff of the jobs available
    given a list of jobs.

    Jobs are in format of (job_number, deadline, payoff)
    '''
    schedule = []

    # sorting based on payoff
    jobs.sort(key = lambda job: job[2])

    # loop through until we have no room to add jobs 
    while length > 0 and len(jobs) > 0:
        for job in jobs:
            # if we can add jobs add them
            if(length <= job[1]):
                schedule.append(job)
                jobs.remove(job)
                break
        
        # subtract the cost of the job to get interval length available
        length -= 1

    return schedule


def schedule_intervals(intervals, length):
    '''
    Returns a schedule that maximizes the amount of intervals available to be ran
    given a list of intervals.

    Intervals are in the format of (intervals_number, start, duration)
    Intervals are later changed to (intervals_number, start, duration, end)
    '''
    schedule = []
    time = 0


    # calculate end time by appending it towards the end
    interval = list(map(lambda interval: interval.append(interval[1] + interval[2]), intervals))

    # sorting based on earilest deadline first
    intervals.sort(key = lambda interval: interval[3])

    # loop through until we have no room to add jobs 
    while time < length and len(intervals) > 0:

        # check if we can fit the first interval
        if(length >= intervals[0][3]):
            time = intervals[0][3]
            schedule.append(intervals[0])
            intervals.pop(0)

        # now remove all incomptiable intervals
        for interval in intervals:
            if interval[1] < time:
                intervals.remove(interval)

    return schedule


def generate_random_jobs(length, count=-1):
    '''
    Generates a list of jobs in a tuple format of
    (job_number, deadline, payoff)
    '''
    if count < 0:
        count = random.randint(10, 20)
    jobs = [[x, random.randint(1, 5), random.randint(2, 10) * 10] for x in range(count)]
    return jobs


def generate_random_intervals(length, count=-1):
    '''
    Generates a list of intervals in a tuple format of
    (intervals_number, start, duration)
    '''
    if count < 0:
        count = random.randint(10, 20)
    intervals = [[x, random.randint(1, length), random.randint(1, 3)] for x in range(count)]
   
    # fixing all the intervals that are past the length
    for interval in intervals:
        if interval[0] + interval[1] > length:
            interval[1] = length - interval[0]

    return intervals


if __name__ == "__main__":
    print(schedule_jobs(generate_random_jobs(6), 6))
    print(schedule_intervals(generate_random_intervals(20), 20))