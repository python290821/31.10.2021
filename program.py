_phrase = ['keep', 'it', 'cool']
_under = ['_' * len(_word) for _word in _phrase]
#_under = []
#for _word in _phrase:
#    new_word = len(_word) * '_'
#    _under.append(new_word)
print(_phrase)
print(_under)

# this is more complicated than a list of letters

_letter = 'e' #input('enter a letter: ')
#new_under = [_letter for _word in _phrase for _letter in _phrase]
#print(new_under)
for _word_index in range(len(_phrase)):
    new_word = ''
    for _letter_index in range(len(_phrase[_word_index])):
        print(_phrase[_word_index][_letter_index], end='')
        if _phrase[_word_index][_letter_index] == _letter:
            new_word += _letter
        else:
            new_word += _under[_word_index][_letter_index]
    _under[_word_index] = new_word
    print()
print(_under)

_letter = 'o' #input('enter a letter: ')
#new_under = [_letter for _word in _phrase for _letter in _phrase]
#print(new_under)
for _word_index in range(len(_phrase)):
    new_word = ''
    for _letter_index in range(len(_phrase[_word_index])):
        print(_phrase[_word_index][_letter_index], end='')
        if _phrase[_word_index][_letter_index] == _letter:
            new_word += _letter
        else:
            new_word += _under[_word_index][_letter_index]
    _under[_word_index] = new_word
    print()
print(_under)
