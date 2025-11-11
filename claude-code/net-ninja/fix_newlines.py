import re

with open(r"C:\Projects\books\claude-code\net-ninja\02-claude-md-init.txt", "r") as f:
    text = f.read()

text = text.replace("\n", " ")
sentences = re.split(r'(?<=[.?!])\s+', text)

with open(r"C:\Projects\books\claude-code\net-ninja\02-claude-md-init.txt", "w") as f:
    for sentence in sentences:
        f.write(sentence.strip() + "\n")
