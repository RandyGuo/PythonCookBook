'''
Created on May 19, 2016
Problem:
Splitting String on any of Multiple Delimiters
You need to split a string into fields, but the delimiters (and spacing around them) are't consistent 
throughout the string
@author: Administrator
'''


if __name__ == '__main__':
    line = 'asdf fjdk; afed, fjek,asdf,     foo'
    import re
    splitted_line = re.split(r'[;,\s]\s*',line)
    print splitted_line