'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

# def single_letter_count(word, letter):
#     count = 0
#     for char in word:
#         if letter.lower() == char.lower():
#             count += 1
#     return count

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
