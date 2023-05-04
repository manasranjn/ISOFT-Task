'''
Rabina is interested so much in gardening and she plants more trees in her garden. She plants trees in the order of rows and columns. She numbered the trees in column wise order. She planted mango tree only in the second column from both first and last of the last row. But later when the trees grew up she forgot where she planted mango trees. So help her to find whether the given tree number is a number of mango trees or not. Display whether “It is a mango tree” or “It is not a mango tree”.


Let the number of trees in a row is 'n'
So, the position of mango trees are - n+2 & 2n-1

'''

n= int(input("Enter the number of trees in each row: "))
tree_num = int(input("Enter the tree number to check: "))

if tree_num == n+2 or tree_num == 2*n-1:
    print("It is a mango tree")
else:
    print("It is not a mango tree")
