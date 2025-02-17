def is_palindrome(word):
    word = word.lower()
    return word == word[::-1] and len(word) > 1

sentences = open("sentences.txt","r")
results = []

for sentence in sentences:
    sentence = sentence.strip()
    words = sentence.split()
    word_cou = len(words)
    longest_word = ""
    max=0
    for word in words:
        curr_len = len(word)
        if curr_len > max:
            max = curr_len
            longest_word = word
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    if palindromes:
        palindromes = ', '.join(palindromes)
    else:
        palindromes = None
    result = (
        f"Sentence: {sentence}\n"
        f"Word Count: {word_cou}\n"
        f"Longest Word: {longest_word}\n"
        f"Palindromes: {palindromes}\n"
    )
    results.append(result)

output_file = open("sentence_analysis.txt","w")
output_file.write('\n'.join(results))