# Dynamic programming is used to store previous values in matrix and can be used later
# Integer partitioning is a way of generating number of ways to represent a number 'n' as sum of integers
# create a matrix from 0 to n
# then write the same values for all the previous calculated values
# Ex: 5 we first write the same values till 0-4 then for 5 we write 5 = 4+1 and add value of 4 + index[1]
# Code not taught but create a matrix using this logic for n = 7
