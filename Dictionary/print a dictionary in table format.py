dict1 = {}
 
# insert data into dictionary
dict1 = {(0, 0): 'Manish', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'SAchin', (1, 1): 20, (1, 2): 'Machine Learning',
         (2, 0): 'YAsh', (2, 1):21, (2, 2): 'OOPS with Java'
}
 
# print the name of the columns explicitly.
print(" NAME ", " AGE ", "  COURSE " )
 
# Iterate through the dictionary
for i in range(3):
     
    for j in range(3):
        print(dict1[(i, j)], end ='   ')
         
    print()
