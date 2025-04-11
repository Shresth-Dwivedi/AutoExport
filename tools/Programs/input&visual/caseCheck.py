sentence = input("Enter a sentence to go: ")
u, l = 0, 0
for x in sentence:
	if x.isupper():
		u+=1
	else:
		l+=1
print("Total characters: ", (u+l), "\nTotal uppercase characters: ", (u), "\nTotal lowercase characters: ", (l))