'''

There are N children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

What are the minimum candies you must give?

Test Case 1:

Input: [1, 2, 3, 4, 5]
Output: 15
Explanation:

1 + 2 + 3 + 4 + 5

Test Case 2:

Input: [3, 5, 9]
Output: 6
Explanation:

1 + 2 + 3

Test Case 3:

Input: [8, 5, 7, 1, 1]
Output: 11
Explanation:

4 + 2 + 3 + 1 + 1
'''

def giveCandies(children):
    children.sort()
    candies = 0

    d = {}

    for i in range(len(children)):
        if children[i] not in d:
            d[children[i]] = 1
        else:
            d[children[i]] += 1

    count = 1
    for i in sorted(d.keys()):
        candies += count * d[i]
        count += 1

    return candies


children = [1, 2, 3, 4, 5]
print("Candies given out:", giveCandies(children))