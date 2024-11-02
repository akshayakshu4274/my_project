# word_frequency.py
def word_frequency(line):
    words = line.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    sorted_frequency = sorted(frequency.items())
    return sorted_frequency

