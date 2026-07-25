#Read file

file = open("file_reader/data.txt", "r")
content = file.read()
file.close()

print(content)

#Count words
words = content.split()
print("Total words:", len(words))

#Count lines
lines = content.split("\n")
print("Total lines:", len(lines))

#Find most common word
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common = max(word_count, key=word_count.get)

print("Most common word:", most_common)