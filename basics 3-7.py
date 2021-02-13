import re

pattern = '9876543210'
test_string = 'My number is 9876543210, obviously, its a 10 digit number and it cannot be 1023456789'
result = re.findall(pattern, test_string)

if result:
    print(str(result))
    print('found')
else:
    print('not found')