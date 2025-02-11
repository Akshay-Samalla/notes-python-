def count_coins():
    '''
    count the number of coins
    '''
    test_cases=int(input())
    friends={}
    for _ in range(test_cases):
        n=int(input())
        friends[n]=friends.get(n,0)+1
    print(friends)
if __name__ == '__main__':
    # here is the main function
    count_coins()