# A. Roma and Lucky Numbers
# time limit per test1 second
# memory limit per test256 megabytes
# Roma (a popular Russian name that means 'Roman') loves the Little Lvov Elephant's lucky numbers.

# Let us remind you that lucky numbers are positive integers whose decimal representation only contains lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

# Roma's got n positive integers. He wonders, how many of those integers have not more than k lucky digits? Help him, write the program that solves the problem.

# Input
# The first line contains two integers n, k (1 ≤ n, k ≤ 100). The second line contains n integers ai (1 ≤ ai ≤ 109) — the numbers that Roma has.

# The numbers in the lines are separated by single spaces.

# Output
# In a single line print a single integer — the answer to the problem.
# Code
# n is number of integers
# k is the number of digits the integer can have
# integers is the list of integers

n, k = map(int, input().split()) 
integers = input().split() 
count = 0 # count of lucky integers

for d in integers:
  lucky_digits = 0 # 4, 7 count in integers
  for digit in d:
    if digit == "4" or digit == "7":
      lucky_digits += 1
    if lucky_digits <= k:
      count += 1
  
print(count)
