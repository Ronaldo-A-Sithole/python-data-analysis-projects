import os
print(os.getcwd())

try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: data.txt not found")

with open("data.txt", "r") as file:
    content = file.read()

print("File content:\n", content)

# Count words
words = content.split()
print("Total words:", len(words))

# Count lines
lines = content.split("\n")
print("Total lines:", len(lines))

# Count word frequency
word_count = {}

for word in words:
    word = word.lower()  # normalize
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common = max(word_count, key=word_count.get)

print("Most common word:", most_common)