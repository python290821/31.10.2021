# 1
# "i wake up at 6:00 am"
# create a list containing only letters (hint: isalpha)
# create a list containing only digits (hint: isdigit)
_sentence = 'i wake up at 6:00 am'
print([_letter for _letter in _sentence if _letter.isalpha()])
#_only_words = []
#for _letter in _sentence:
#    if _letter.isalpha():
#        _only_words.append(_letter)
print([_digit for _digit in _sentence if _digit.isdigit()])

# 2
# [5.9, 0.9, -9.2, 11.1 ] -- create a list as ints
# [5,   0,    -9, 11 ]
_floats = [5.9, 0.9, -9.2, 11.1 ]
print([int(x) for x in _floats])
# nums = [[1,2,6], [7,8,9], [100,5,2]]
# create a list of the max [6, 9, 100]
# create a list of the min [1, 7, 2]
# create a list of avg
#import statistics
#print(statistics.mean([1,2,3]))
import statistics
nums = [[1,2,6], [7,8,9], [100,5,2]]
print([max(sub_list) for sub_list in nums])
#maxs = []
#for sub_list in nums:
#    print(sub_list)
#    maxs.append(max(sub_list))
print([min(sub_list) for sub_list in nums])
print([(sub_list, f'avg={statistics.mean(sub_list)}') for sub_list in nums])
# 3
# _prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# return prices bigger than 0, for lower than zero return 0
o_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = []
for x in o_prices:
    if x > 0:
        prices.append(x)
    else:
        prices.append(0)
#        [ _APPEND_A_CONDITION_ELSE_B _FOR_ _IF_TRUE_ ]
prices = [x if x > 0 else 0 for x in o_prices]
x = int(input())
print('positive' if x > 0 else 'negative')
def positive_or_negative(x):
    return 'positive' if x > 0 else 'negative'
_salary = int(input())
_salary = _salary * 0.9 if _salary < 5000 else _salary * 0.8
if _salary < 5000:
    _salary = _salary * 0.9
else:
    _salary = _salary * 0.8

# 4
# ['hello', '', 'python', 'world', 'full stack','a']
# list of len if len < 3 then -1


