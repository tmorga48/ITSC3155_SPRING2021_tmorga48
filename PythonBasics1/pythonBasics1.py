# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.

# Part A. count_char
# Define a function count_char(s, char) that takes a string and a character
# and returns the number of times the given character appears in the string
def count_char(s, char):
  x = 0
  
  if char == '':
    x=0
  else:      
    x = s.count(char)
  # YOUR CODE HERE

  return x

# Part B. is_power_of
# Define a function is_power_of(i,j) that takes 2 ints i and j
# and checks if i is a power of j or not
# the function should return True indicating that i is a power of j
# otherwise return False
def is_power_of(i,j):
  # YOUR CODE HERE
  if i < 0:
    if j < 0:
      i = abs(i)
      j = abs(j)
      p = 1
      while (p < j):
        p = p * i

  if i == 1:
    if j == 1:
      return True
  
  if i == 0:
    return True

  p = 1
  while (p < j):
    p = p * i

  if p == j:
    return True

  return False

# Part C. longest_word
# Define a function longest_word(s) that takes a string s
# where s is a sentence made up of words separated by a single space " "
# and returns the longest word in this sentence
# if 2 or more words are tied as longest then return the one that occurs LAST in the sentence
# if s is an empty string return an empty string
def longest_word(s):
  # YOUR CODE HERE

  return
