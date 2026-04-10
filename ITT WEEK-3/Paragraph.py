import os

filename = input("Enter file name: ")

if os.path.exists(filename):

    file = open(filename, 'r', encoding='utf-8')
    text = file.read().lower()
    file.close()

    symbols = "!()-[]{};:'\"\,<>./?@#$%^&*_~—“”‘’"
    for s in symbols:
        text = text.replace(s, "")

    words = text.split()
    

    print(f"\nTotal no of words: {len(words)}")


    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    print("\nOccurrences (more than 1 time):")
    for w in counts:
        if counts[w] > 1:
            print(f"{w}: {counts[w]}")


    if words:
        largest_word = ""
        for w in words:
            if len(w) > len(largest_word):
                largest_word = w
        
        print(f"\nLargest word found: {largest_word}")
        print(f"Length: {len(largest_word)}")
        print(f"Reversed: {largest_word[::-1]}")

else:
    print("File not found!")









