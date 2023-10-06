def printing_only_even_index_chars():
    word = input("Enter your word ")
    print("Original String:", word)
    new_word = []

    for letter in list(word)[0::2]:
        new_word.append(letter)
    print(''.join(new_word))


printing_only_even_index_chars()