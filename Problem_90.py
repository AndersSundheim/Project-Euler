'''
Created on Apr 11, 2016


Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

@author: Anders
'''
import itertools
c1 = [0,1,2,3,4,5,6,7,8,9]
c2 = [0,1,2,3,4,5,6,7,8,9]

d1 = list(itertools.combinations(c1,6))
dice_1 = d1

d2 = list(itertools.combinations(c2, 6))
dice_2 = d2
positive = []
for i in range(0,len(dice_1)):
    for j in range(0,len(dice_2)):
        if ((0 in dice_1[i] and 1 in dice_2[j]) or (0 in dice_2[j] and 1 in dice_1[i])) and ((0 in dice_1[i] and 4 in dice_2[j]) or (0 in dice_2[j] and 4 in dice_1[i])):
            if (0 in dice_1[i] and (9 in dice_2[j] or 6 in dice_2[j])) or (0 in dice_2[j] and (9 in dice_1[i] or 6 in dice_1[i])):
                if(1 in dice_1[i] and (9 in dice_2[j] or 6 in dice_2[j])) or (1 in dice_2[j] and (9 in dice_1[i] or 6 in dice_1[i])):
                    if (2 in dice_1[i] and 5 in dice_2[j]) or (2 in dice_2[j] and 5 in dice_1[i]):
                        if(3 in dice_1[i] and (9 in dice_2[j] or 6 in dice_2[j])) or (3 in dice_2[j] and (9 in dice_1[i] or 6 in dice_1[i])):
                            if(4 in dice_1[i] and (9 in dice_2[j] or 6 in dice_2[j])) or (4 in dice_2[j] and (9 in dice_1[i] or 6 in dice_1[i])):
                                if (8 in dice_1[i] and 1 in dice_2[j]) or (8 in dice_2[j] and 1 in dice_1[i]):
                                    x = sorted(dice_1[i])
                                    y = sorted(dice_2[j])
                                    positive.append({tuple(x),tuple(y)})
                                    
print(len(positive)/2)
                    
            

