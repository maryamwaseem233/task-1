A={3,5,6,9,8,2}
B={50,5,66,333,55}
C={65,33,34,66,22,11}
#print a union 
C=A.union(B)
print(C)

#PRINT INTERSECTION
print(A.intersection(B))

#PRINT DIFFERENCE
print(A.difference(B))

# #ADDING a SETS 

A.add(44)
print(A)

# #merge a two sets 
A.update(B,C)
print(A)

# #REMOVE A SETS 
B.REMOVE(66)
print(B)