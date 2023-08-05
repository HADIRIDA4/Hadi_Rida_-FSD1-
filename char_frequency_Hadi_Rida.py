def char_frequency (s) :
    Letter_count={} 
    for letter in s:
        Letter_count[letter]=Letter_count.get(letter, 0)+1
    print(Letter_count)
text=input("please enter your text ")
char_frequency(text) 