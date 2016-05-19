'''
Created on May 19, 2016

@author: Administrator
'''

if __name__ == '__main__':
    filename = 'spam.txt'
    print "slice for judge",filename[-4:] == '.txt'
    url = 'http://www.python.org'
    print "url start with 'http'",url.startswith('http'),'end with "org"',url.endswith('org')
    print "url[:5] == 'http' or url[:6] == 'https:' -> ",url[:5] == 'http:'
    import re 
    match = re.match('http:|https:|fpt:',url)
    print 're.match =>',match.group()