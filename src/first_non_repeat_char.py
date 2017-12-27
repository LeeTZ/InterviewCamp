"""
Given a string, find the first character that appears only once in this string.

Questions you may ask:
Which character set does the stirng contain? (pure English characters? all ascii?)
What if there are no such characters? (return a string with "null"?)
"""

# s: given string
def first_non_repeat_char(s):
	res = "null"
	NUM_OF_CHAR = 256
	count = [0] * NUM_OF_CHAR
	for ch in s:
		count[ord(ch)] += 1
	for ch in s:
		if count[ord(ch)] == 1:
			res = ch
			break
	return res	

# tests
testStrings = ["apaple","Saber","aaaaaa","213jklsdfaijlefejia132412213jdk"]
for t in testStrings:
	print first_non_repeat_char(t)