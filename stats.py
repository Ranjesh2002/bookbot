def text_count(count):
    words = count.split()
    return len(words)

def count_character(text):
    counts = {}
    text = text.lower()
    for word in text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def sort_on(item):
    return item["num"]

def sort_character(text):
    so = []
    for char, count in text.items():
        if char.isalpha():
            so.append({"char": char, "num": count})
    so.sort(key=sort_on, reverse=True)
    return so