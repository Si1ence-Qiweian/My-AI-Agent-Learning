numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n ** 2 for n in numbers1]
print(squares)

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even = [n for n in numbers2 if n % 2 == 0]
print(even)

words = ["apple", "kiwi", "banana", "fig"]
words_len4 = [word for word in words if len(word) > 4]
print(words_len4)

lengths = {word: len(word) for word in words}
print(lengths)

print([word[0] for word in words])

alley = {word[0] for word in words}
print(alley)

alley_upper = {word.upper() for word in alley}
print(alley_upper)