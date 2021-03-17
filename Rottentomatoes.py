'''
 Rotten Tomatoes Rating System
 Code By Saideep Shetty
'''
answer = input("Enter the next review: ")
total = 0
positive = 0

percentage = 0
while answer != '':
    if answer == '1':
        positive += 1
    else:
        positive += 0
    total += 1
    percentage = (positive / total) * 100
    print("Review : ", percentage, '%')
    print('Reviews :', total, ' Positive: ', positive, ' Negative: ', total-positive)
    answer = input("Enter the next review: ")