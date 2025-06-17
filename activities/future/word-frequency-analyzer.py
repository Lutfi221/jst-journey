
file_path = "/Users/lutfi/neodata/areas/jst-journey/activities/2025-06-14/hp.txt"

with open(file_path, "r") as file:
    text = file.read()

words = text.split()

n_words = len(words)

print("The number of words in the file is: " + str(n_words))

word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1


print("Word and frequency:")

for word, frequency in word_frequency.items():
    if frequency > 30:
        print(word + ": " + str(frequency))
