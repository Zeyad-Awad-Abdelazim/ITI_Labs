## Task 1: Count the number of vowels in a string
# text = "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# text2 = "hello world"

# def count_vowels(txt):
#     vowels = "aeiou"
#     count = 0
#     for char in txt.lower():
#         if char in vowels:
#             count += 1
#     return count

# print("No of vowels: " + str(count_vowels(text)))
# print("No of vowels: " + str(count_vowels(text2)))

# # Task 2: Sort a list of numbers in ascending and descending order
# arr = input("Enter a list of numbers separated by spaces: ")
# arr = sorted(map(int, arr.split()))
# print(f"your arr sorted ascendingly : {arr}")
# print(f"your arr sorted descendingly : {arr [::-1]}")

# # Task 3 : Count the occurrences of a substring in a string
# subText = "iti"
# text = "Egyptian Information Technology Institute (ITI) is a leading institution in Egypt that provides high-quality education and training in the field of information technology. ITI offers various programs and courses designed to equip students with the skills and knowledge needed to excel in the tech industry."
# def count_substring(txt, sub):
#     count = 0
#     subLength = len(sub)
#     for i in range(len(txt) - subLength + 1):
#         if txt[i:i + subLength].lower() == sub.lower():
#             count += 1
#     return count

# print(f"The substring '{subText}' appears {count_substring(text, subText)} times in the text.")        

# # Task 4 : Write a program that remove all vowels from the input word and generate a brief version of it
# word = input("Enter a word: ")
# def remove_vowels(word):
#     vowels = "aeiouAEIOU"
#     return ''.join([char for char in word if char not in vowels])

# short_word = remove_vowels(word)
# print(f"Shortened version: {short_word}")

# # Task 5 : Find the index of all occurrences of the letter 'i' in a string
# anyString = input("Enter a string: ")

# for i in range(len(anyString)):
#     if anyString[i].lower() == 'i':
#         print(f"Found 'i' at index {i}")


# # Task 6 : Create a list of lists where each inner list contains the multiplication table for numbers from 1 to n
# num = int(input("Enter a number: "))
# entireRow = []
# for i in range(1, num + 1):
#     col = [i * j for j in range(1, i + 1)]
#     entireRow.append(col)

# print(entireRow)

# # Task 7: Mario Pyramid
# num = int(input("Enter Number: "))
# for i in range(1, num + 1):
#     print(' ' * (num - i), end='') 
#     print('*' * i)