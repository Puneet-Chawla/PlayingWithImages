from collections import Counter

text = "as qw as qw as sd fg gh xc zxz sd er ty yu "

words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)


