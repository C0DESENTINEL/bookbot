def get_num_words(content):
    words = content.split()
    word_count = len(words)
    return word_count

def get_num_char(content):
    content = content.lower()
    result = {}
    for char in content:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result