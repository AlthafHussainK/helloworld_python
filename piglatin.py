#Pyg Latin Translator

pyg = "yay"

original = raw_input("Enter a word: ")
word = word.lower()
first = word[0]

new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

if len(original) > 0 and original.isalpha() :
    print original
else :
    print "Empty or String contains numbers!"
