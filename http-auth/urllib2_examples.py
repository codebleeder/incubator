__author__ = 'codebleeder'
import urllib2

the_url = 'http://www.google.com/'
f = urllib2.urlopen(the_url)
print f.read()
