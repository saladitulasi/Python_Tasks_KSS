def count_vowels(s):
    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count += 1

    return count

text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))