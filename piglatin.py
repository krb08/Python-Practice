#Pig Latin (from Martyr2'S Mega Project Ideas List!)
#Convert input string into Pig Latin
from string import punctuation

def pig_latin(text):
    #convert text to lower case
    text = text.lower() 
    #list of vowels
    vowels = ["a", "e", "i", "o", "u"]
    #remove punctuation fro text
    text = ''.join(c for c in text if c not in punctuation)
    word_string =""
    #convert text from string to list
    word_list = text.split()
    for word in word_list:
        #if word is a number
        if word.isdigit():
            pass
        #if word length is 1
        if len(word) == 1:
            word += 'way'
        #if word begins with a vowel, add 'way' to the end
        elif word[0] in vowels:
            word += 'way'
        #if word begins with consonant
        else:
            #and second letter is also a consonant, add first to letter + ay to the end
            if word[1] not in vowels:
                char = word[0] + word[1]
                word = word[2:]
                word += char + 'ay'
            #and second letter is a vowel, add the first letter + 'ay' to the end
            else:
                char = word[0]
                word = word[1:]
                word += char + 'ay'
       
        #add translated words to string variable
        word_string += str(word) + ' '
    #Text translated to Pig Latin
    print(word_string)

text = input("Enter text to translate to Pig Latin:\n")
print("Translated text is:\n")
pig_latin(text)

