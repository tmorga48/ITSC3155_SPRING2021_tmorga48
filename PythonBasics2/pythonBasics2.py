# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE
  c3 = n.count("3")
  c6 = n.count("6")
  c9 = n.count("9")

  d = dict([
    ('count3' , c3),
    ('count6' , c6),
    ('count9' , c9)
  ])

  if d['count3'] > d['count6'] and d['count3'] > d['count9']:
    return 3
  if d['count6'] > d['count3'] and d['count6'] > d['count9']:
    return 6
  if d['count9'] > d['count3'] and d['count9'] > d['count6']:
    return 9  


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  n = len(s) 
  count = 0
  cur_count = 1
  d = dict()
   
  for i in range(n): 
          
    if (i < n - 1 and 
        s[i] == s[i + 1]): 
        cur_count += 1
  
    else: 
        if cur_count > count: 
            count = cur_count 
            d[s[i]] = cur_count
            cur_count = 1
  
  m = max(d.values())
  a = [] 
  
  for keys in d.keys():
    if d[keys] == m:
      a.append(keys)

  return a    

   



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  s = s.lower()
  s = s.replace(' ', '')

  for i in range(len(s)//2):
    if s[i] != s[-1-i]:
          return False
   
  return True

