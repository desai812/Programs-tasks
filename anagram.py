
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", "")):
    print("The words are Anagrams")
else:
    print("The words are Not Anagrams")