
def changemaking(d,n):
    F = [0]*(n+1)
    for j in range(1,n+1):
        F[j] = min([F[j-i] for i in d if i<=j])+1
    return F


d=[1,3,4,5,6]
n=10
print changemaking(d,n)


def climbStairs(n):
    tmp = [1,2]
    if n==1:
        return tmp[0]
    elif n==2:
        return tmp[1]
    else:
        for i in range(2,n):
            tmp[0], tmp[1] = tmp[1], tmp[0]+tmp[1]
        return tmp[1]

print climbStairs(30)


def Q3(N,M):
    #[toss][sum of tosses]
    dp_number=[[0 for i in range(M+1)] for i in range(N+1)]
    for i in range(1,7):
        dp_number[1][i]=1
    for toss in range(2,N+1): # toss 2 to N times
        for sum_of_tosses in range(toss, M+1): # sum of tosses at each row
            for current_toss in range(1,7): # value of current ith roll
                rem = sum_of_tosses - current_toss # value needed before
                if rem > 0:
                    dp_number[toss][sum_of_tosses] += dp_number[toss-1][rem]


    print "N:", N, "M:", M
    print "number:", dp_number[N][M]
    print

Q3(2,7)
Q3(3,9)
Q3(8,24)
