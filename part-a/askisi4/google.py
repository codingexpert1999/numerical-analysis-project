import numpy as np

def getPageRank(A, PR, linked_websites, q):
    rank = (1 - q) / n

    if len(linked_websites) != 0:
        for j in linked_websites:
            rank += q*(PR[j] / len(list(filter(lambda x: x != 0, A[j]))))

    return rank
    
def stopIterations(PR, prev_PR):
    count = 0
    margin_error = 1.0e-7

    for i in range(len(PR)):
        if np.fabs(PR[i] - prev_PR[i]) <= margin_error:
            count += 1

    return count == len(PR)

def PageRank(A, R, n, q):
    power = 1
    PR = np.copy(R)
    prev_PR = np.copy(PR)

    while True:
        for i in range(n):
            linked_websites = []

            for k, link in enumerate(A[:, i]):
                if link != 0:
                    linked_websites.append(k) 

            PR[i] = getPageRank(A, PR, linked_websites, q)

        if stopIterations(PR, prev_PR):
            break

        prev_PR = np.copy(PR)
        power += 1

    return (PR, power)

def getPagesAndTheirRankings(ranks):
    n = len(ranks)
    temp_ranks = np.copy(ranks)
    ranks_dict = {}

    for i in range(n):
        max_rank = temp_ranks[i]
        index = i

        for j in range(n):
            if i != j:
                if temp_ranks[j] >= max_rank:
                    max_rank = temp_ranks[j]
                    index = j
        
        ranks_dict[index] = max_rank
        temp_ranks[index] = 0

    return ranks_dict

def setLinksSoTheySumUpToOne(A):
    # Change A values (for example if A has only 2 outgoing links then every 1 in row 0 will become 1/2)
    for i in range(n):
        number_of_outgoing_links = np.sum(A[i])
        for j in range(n):
            if A[i][j] == 1:
                A[i][j] = 1 / number_of_outgoing_links

def questionTwo(A, R, n):
    ranks, power = PageRank(A, R, n, 0.85)
    print(ranks)
    print(getPagesAndTheirRankings(ranks))

def questionThree(A, R, n):
    ranks, power = PageRank(A, R, n, 0.85)
    print(getPagesAndTheirRankings(ranks))
    print("And the power of convergence is " + str(power))

def questionFour(A, R, n):
    ranks, power = PageRank(A, R, n, 0.98)
    print(getPagesAndTheirRankings(ranks))
    print("And the power of convergence is " + str(power))

    ranks, power = PageRank(A, R, n, 0.4)
    print(getPagesAndTheirRankings(ranks))
    print("And the power of convergence is " + str(power))

def questionSix(A, R, n):
    ranks, power = PageRank(A, R, n, 0.85)
    print(getPagesAndTheirRankings(ranks))
    print("And the power of convergence is " + str(power))
    print(np.sum(ranks))

# Ερώτημα 2
A = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
]

A = np.array(A, np.float)
n, _ = A.shape

setLinksSoTheySumUpToOne(A)

R = np.zeros(n, np.float)
R[:] = 1 / n # rank vector (with initial values 1 / n)

questionTwo(A, R, n)

# Ερώτημα 3

# New Connections
# (14, 0), (13, 0), (12, 0), (9, 0)
# Deleted Connection
# (3, 7)
changed_A = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 1
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 2
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 3
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # 4
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], # 7
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 8
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], # 9
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 11
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0], # 12
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], # 13
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1], # 14
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]  # 15
    #1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
]

changed_A = np.array(changed_A, np.float)

setLinksSoTheySumUpToOne(changed_A)

# questionThree(changed_A, R, n)

# Ερώτημα 4
# print("Question 3")
# questionThree(changed_A, R, n)
# print("Question 4")
# questionFour(changed_A, R, n)

# Ερώτημα 5
A = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
]

A = np.array(A, float)

n,_ = A.shape

R = np.zeros(n, np.float)
R[:] = 1 / n

questionSix(A, R, n)
