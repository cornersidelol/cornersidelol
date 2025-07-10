#List of alphabet
lower_alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def check_uppercase(sentence):
    for char in sentence:
        if char.isalpha():
            if char != char.upper():
                return False
    return True
        
def check(sentence):
    with open("C:\\sba\\words_alpha.txt") as f:
        words = set(f.read().split('\n'))

    sentence = remove_symbols(sentence)

    word_in_sentence = sentence.split()

    for y in range(0, len(word_in_sentence)):
        word = word_in_sentence[y].lower()
        if not word in words:
            return False
    return True

def remove_symbols(sentence):
    valid_letters = lower_alphabet_list + upper_alphabet_list
    cleaned_text = ''.join(char for char in sentence if char in valid_letters or char.isspace())
    return cleaned_text.strip()

def decrypt_shift(sentence, k):
    new_sentence = ""
    Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for y in range(0, len(sentence)):
        if sentence[y] in Letter:
            new_index = (Letter.index(sentence[y]) - k)%26
            new_sentence += Letter[new_index]
        else:
            new_sentence += sentence[y]
    return new_sentence

def encrypt_shift(sentence):
    new_sentence = ""
    Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for y in range(0, len(sentence)):
        if sentence[y] in Letter:
            new_index = (Letter.index(sentence[y]) + 8)%26
            new_sentence += Letter[new_index]
        else:
            new_sentence += sentence[y]
    return new_sentence

def count_letter(sentence):
    frequency = {}
    
    for char in sentence:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

def remove_space(sentence):
    new_sentence = ""
    Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for y in range(0, len(sentence)):
        if sentence[y] in Letter:
            new_sentence += sentence[y]
    return new_sentence

def count_most(sentence_with_no_space):
    new_sentence = sorted(sentence_with_no_space)
    mode = ""
    max = 0
    cur = 0
    for letter in new_sentence:
        if letter != mode:
            cur = 1
            if cur > max:
                mode = letter
        else:
            cur += 1
            max = cur
    return mode, max


            

# WORK HARD, PLAY HARD!
# EWZS PIZL, XTIG PIZL! -> 8




