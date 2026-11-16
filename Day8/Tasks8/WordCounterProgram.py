# Word Counter Program

file = open("article.txt", "r")

content = file.read()

words = len(content.split())
lines = len(content.splitlines())
characters = len(content)

file.close()

print("Word Count:", words)
print("Line Count:", lines)
print("Character Count:", characters)