import json

# Open the files
with open("news.txt") as f:
    article = f.read()

with open("subs.json") as f:
    subs = json.load(f)

# Make the substitutions
for word in article.split():
    if word.lower() in subs:
        article = article.replace(word, subs[word.lower()])

# Write to a new file
with open('betternews.txt', 'w') as f:
    f.write(article)

# Close the files
f.close()