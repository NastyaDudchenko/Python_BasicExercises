def remove_chars(word, n):
    print("Original String:", word)
    print("Transformed String:", word[int(n):])


word = input("Enter your word ")
n = input("How much chars you want to remove? ")

while not n.isdigit() or int(n) > len(word):
    print("Try again")
    n = input("How much chars you want to remove? ")
remove_chars(word, n)
