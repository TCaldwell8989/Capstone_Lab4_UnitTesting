def camel_case(sentence):
    ''' Convert sentence by first word being in lower case, followed by capitalizing each word following'''
    new_sentence = ''

    if sentence == '':
        raise ValueError('Sentence must not be blank or empty.')

    words = sentence.lstrip(' ').split(' ')             #remove leading spaces and break by spaces
    new_sentence += (words[0].lower())      #First word lowercased
    for word in words[1:]:                  #Loop starting at index 1 (2nd word))
        new_sentence += (word.capitalize()) #Capitalizing first letter
    return new_sentence

def head_banner():
    ''' Display Banner'''
    msg = "CAMELCASE GENERATOR PROGRAM"
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

def main():

    head_banner()

    sentence = input('Enter your sentence: ')
    new_sentence = camel_case(sentence)
    print(new_sentence)

if __name__ == '__main__':
    main()

