import re

## RE MATCHES
# patterns = ['term1','term2']
#
# text = 'This is a string with term1, not the other!'
# print('Text to be searched: "' + text + '"')
#
# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print('MATCH!')
#     else:
#         print('NO MATCH!')
#
# match = re.search('term1',text)
# print(type(match))
# print(match.start())

## RE SPLITS
# split_term = '@'
# email = 'user@gmail.com'
#
# print(re.split(split_term,email))

## RE FIND
# print(re.findall('match','test phrase match in middle'))
# print(re.findall('match','match will match twice here'))

## MULTI RE FIND
def multi_re_find(patterns,phrase):

    for pattern in patterns:
        print('Searching for pattern {}'.format(pattern))
        print(re.findall(pattern,phrase))
        print('\n')

# test_phrase = 'sdsd..sssddd..sdddsddd...dsds..dsssss..sddddd'
#
# test_patterns1 = ['sd*']
# test_patterns2 = ['sd+']
# test_patterns3 = ['sd{3}']
# test_patterns4 = ['sd{1,3}']
# test_patterns5 = ['s[sd]+']
#
# multi_re_find(test_patterns1,test_phrase)
# multi_re_find(test_patterns2,test_phrase)
# multi_re_find(test_patterns3,test_phrase)
# multi_re_find(test_patterns4,test_phrase)
# multi_re_find(test_patterns5,test_phrase)

test_phrase1 = 'This is a string! But it has punctuation. How can we remove it?'

test_phrase2 = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns1 = ['[^!.?]+'] # punctuation
test_patterns2 = ['[a-z]+'] # lower case letters
test_patterns3 = ['[A-Z]+'] # capital letters
test_patterns4 = [r'\d+'] # digits
test_patterns5 = [r'\D+'] # non-digits
test_patterns6 = [r'\s+'] # white space
test_patterns7 = [r'\S+'] # non-white space
test_patterns8 = [r'\w+'] # alphanumerical
test_patterns9 = [r'\W+'] # non-alphanumerical

multi_re_find(test_patterns1,test_phrase1)
multi_re_find(test_patterns2,test_phrase1)
multi_re_find(test_patterns3,test_phrase1)
multi_re_find(test_patterns4,test_phrase2)
multi_re_find(test_patterns5,test_phrase2)
multi_re_find(test_patterns6,test_phrase2)
multi_re_find(test_patterns7,test_phrase2)
multi_re_find(test_patterns8,test_phrase2)
multi_re_find(test_patterns9,test_phrase2)
