## TRY EXCEPT FINALLY
# try:
#     print('Trying to process')
#     my_num = 5 / 0
#     # my_num = 5 / num
#     print('Successfully processed')
# except ArithmeticError:
#     print('There was an Arithmetic error.')
# except Exception:
#     print('There was some error.')
# finally:
#     print('Process ended')

try:
    f = open('09-some_text.txt','r')
    # f = open('09-some_text.txt','w')
    f.write('Test write to some text!')
except IOError:
    print('ERROR: COULD NOT FIND FILE OR WRITE TO IT!')
else:
    print('Success!')
finally:
    print('closing file')
    f.close()
print('hello world!')
