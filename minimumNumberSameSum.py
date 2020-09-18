'''
Create a function 

def solution(N):

which accepts a number 'N' and returns minimum number greater than 'N', whose sum of digits is same as sum of digits of N

Example:
N : 28
It should return 37, since sum of digits of 28 is 10 and that of 37 is also 10 and its the next smallest number greater than N
which satisfies the condition

'''

def solution(N):
    Nlist = list(str(N))
    sumOriginal = 0
    for i in range(len(Nlist)):
        sumOriginal += int(Nlist[i])

    og_sum = sum([int(i) for i in str(N)])

    i = N + 1
    while i > N:
        iList = list(str(i))
        iSum = 0
        for j in range(len(iList)):
            iSum += int(iList[j])
        if iSum == sumOriginal:
            return(i)
        i += 1

N = 1000
print(solution(N))