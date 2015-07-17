#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

val1 = form.getvalue('username')
val2 = form.getvalue('password')

print """Content-type: text/html

The form input is below...<br/>"""
print val1, val2