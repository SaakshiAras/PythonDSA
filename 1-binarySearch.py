# brute force Engine 
# PROBLEM : suppose we are given the list of cards and is shuffled and we want 
# to find the card given query and its position 
# for thsi we will be using linear search engine later, where it helps to search the element one by one given the position 

# few test cases 

test=  {
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query':3
    },
    'output':5
}
tests=[]
tests.append(test)
tests.append({
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query':15
    },
    'output':-1
})
tests.append({
    'input':{
        'cards':[11,10,3,2,1],
        'query':1
    },
    'output':4
})
tests.append({
    'input':{
        'cards':[],
        'query':1
    },
    'output':-1
})

def locate_card(cards,query):
    position=0
    print('cards:',cards)
    print('query:',query)
    while position < len(cards):
        if cards[position]==query:
            return position
        position+=1
        if position==len(cards):
            return -1

for test in tests:      
    print(locate_card(**test['input'])==test['output'])

 

# This is by using brute force solution 
    
#ANALYSE THE PROBLEM BY MINIMIZING THE ACCESS OF CARD (BIG O NOTATION)

# time complexity = cN ( fixed constant =c)
# Space complexity = c ( independent of N) ( constant space in RAM)
# Big O Notation : worst - case complexity 
    # i.e cN^3 + dN^2 + eN + f, in that Big O Notation is cN^3\

# here the time complexity is O(N)
  #  and space complexity is O(1)
    

# LINEAR SEARCH ENGINE 
    
def loc_card(cards,query):
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        mid_num = cards[mid]
        print("lo:",lo," hi:",hi," mid:", mid," mid_num:",mid_num)

        if mid_num == query:
            return mid
        elif mid_num < query:
            hi = mid -1
        elif mid_num > query:
            lo = mid+1
    return -1

c = [9,8,7,6,5,4,3,2,1]
q = 3 
print(loc_card(c,q))

# suppose c =[ 9,9,9,8,8,8,7,7,7,6,6,6]
# and q = 8 , output should be 3 
# for that we need to modify the code 

def test_loc(cards,query,mid):
    mid_num=cards[mid]
    print("mid",mid," mid number:",mid_num)
    if mid_num==query:
        if mid>=0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif mid_num < query:
        return 'left'
    else:
        return 'right'
def loc_cards(cards,query):
    lo,hi=0,len(cards)-1
    while lo<= hi:
        mid = (lo + hi )//2
        res = test_loc(cards,query,mid)
        if res == 'found':
            return mid 
        elif res == 'left':
            hi = mid -1
        elif res == 'right':
            lo = mid+1 

# in test case first we will consider the mid number
# if query == mid num then we will check its before val 
# and if its same then go search from left but if its unique 
# then return the mid num position as answer 
# same way we will check if mid num is greater than query 
# if it is greater than query then, search right because we are 
# considering list in decreasing order and same when query is greater than mid
# search from left [ 9,9,9,8,8,8,7,7,7]
# so when it searches it will agasin go back in loop and the ndo the mid search among the left 
# left and right search and get the answer and attach it to normal func (loc_cards)                                                                                                     
