# sort comma seperated unique words alphanumerically
items = raw_input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
