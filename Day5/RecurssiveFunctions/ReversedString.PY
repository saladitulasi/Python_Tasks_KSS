def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
string = "hello"
print("Reversed string:", reverse_string(string))