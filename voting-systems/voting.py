import random as random

'''
Generates a random set of voters and canadidates along with their preferences and computes the winner according to different voting systems.
Voters have a preference set as a list, ranging from [x_0, x_1, ...., x_n] where x_0 is their least prefered canadiates and x_n is their most prefereced canadiate.
'''
def compute_ftfp(voters):
    '''
    First past the post - Voters only pick their most liked candidate
    '''
    candidate_count = len(voters[0])

    # ftfp process
    count = [0] * candidate_count
    for vote in voters:
        count[vote[candidate_count - 1]] += 1
    
    # selecting winner from the remaining count
    winner = 0
    winner_count = 0
    for candidate in range(candidate_count):
        if count[candidate] > winner_count:
            winner = candidate 
            winner_count = count[candidate]
    return winner


def compute_borda_count(voters):
    '''
    Borda count - Assign a simple preference list then total for winner
    '''
    candidate_count = len(voters[0])

    # borda process
    count = [0] * candidate_count
    for vote in voters:
        for rank in range(candidate_count):
            count[vote[rank]] += rank

    # selecting winner from the remaining count
    winner = 0
    winner_count = 0
    for candidate in range(candidate_count):
        if count[candidate] > winner_count:
            winner = candidate 
            winner_count = count[candidate]
    return winner


def compute_instant_runoff(voters):
    '''
    Instant runoff - Assign a prefernece list, eliminate the lowest 
    done by 
    '''
    candidate_count = len(voters[0])

    # pool process
    pool = [[] for i in range(candidate_count)]
    for vote in voters:
        pool[vote[candidate_count - 1]].append(vote)

    # check criteria
    losers = []
    winner_count = 0

    # checking if any candidates have a simple majority
    while winner_count <= len(voters) / 2:
        winner = 0
        winner_count = 0
        
        # find our winner
        for candidate in range(candidate_count):
            if candidate not in losers:
                if len(pool[candidate]) > winner_count:
                    winner = candidate
                    winner_count = len(pool[candidate])

        # else find the loser then
        loser = winner
        loser_count = winner_count
        for candidate in range(candidate_count):
            if candidate not in losers:
                if len(pool[candidate]) < loser_count and len(pool[candidate]) > 0:
                    loser = candidate
                    loser_count = len(pool[candidate])

        # keeping track of who lost
        losers.append(loser)
        
        # reallocate loser
        for voter in pool[loser]:
            next_vote = candidate_count - 1
            while voter[next_vote] in losers:
                next_vote -= 1
            pool[voter[next_vote]].append(vote)
        pool[loser] = []

    return winner



def generate_voters(voter_count, candidate_count):
    '''
    Generates a set of voter preferences for a set amount of candidates
    ranging from 0 to candidate_count, voters are then shuffled with the
    list order representing their preference
    '''
    voters = []
    for x in range(voter_count):
        voter = list(range(candidate_count))
        random.shuffle(voter)
        voters.append(voter)
    return voters


if __name__ == "__main__":
    candidate_count = 6
    voter_count = 100000000

    voters = generate_voters(voter_count, candidate_count)
    print("Winner of borda count is:" + str(compute_borda_count(voters)))
    print("Winner of ftfp is:" + str(compute_ftfp(voters)))
    print("Winner of instant runoff is:" + str(compute_instant_runoff(voters)))
