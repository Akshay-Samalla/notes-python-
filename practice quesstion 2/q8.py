'''

sort Words by Length
  Sort them in ascending order of their lengths.
	words = ["apple", "banana", "cherry", "date", "fig"]


'''

words = ["apple", "banana", "cherry", "date", "fig"]
words=sorted(words , key=lambda x :len(x))
print(list(words))