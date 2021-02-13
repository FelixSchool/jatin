import re
pattern = 'the 29 Netherlands'
sentence = 'welcome to the 29 Netherlands port of Europe'

fff = re.findall(pattern, sentence)
print('found', fff)