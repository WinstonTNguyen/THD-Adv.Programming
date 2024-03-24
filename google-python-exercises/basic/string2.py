#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if len(s) < 3:
    return s
  elif s[-3:] == 'ing':
    return s + 'ly'
  else:
    return s + 'ing'


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  allWordsNotToBad = s[s.find('not'):s.find('bad')+len('bad')]      # find all the words from 'not' .... 'bad'
  if allWordsNotToBad != '':
    return s.replace(allWordsNotToBad, 'good')                      # replace with 'good'
  else:
    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  if len(a)%2 == 0:               # If a is even
    aFront = a[:len(a)//2]        # get aFront from the start to a divided by 2 
    aBack = a[(len(a))//2:]       # get aBack from a divided by 2 to the end
  else:                           # a is not even
    aFront = a[:len(a)//2+1]      # get aFront from start to a divided by 2 + 1
    aBack = a[(len(a))//2+1:]     # get aBack from a divided by 2 + 1 to the end

  if len(b)%2 == 0:               # b same as a (see above)
    bFront = b[:len(b)//2]
    bBack = b[(len(b))//2:]
  else:
    bFront = b[:len(b)//2+1]
    bBack = b[(len(b))//2+1:]

  return aFront + bFront + aBack + bBack


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
