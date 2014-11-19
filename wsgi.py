#!/usr/bin/env python
import os

def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        response_body = '''
def symbol4(d):
    s=[
    '`````●`',
    '````●●`',
    '```●`●`',
    '``●``●`',
    '`●```●`',
    '`●●●●●●',
    '`````●`',
    '`````●`',
    '`````●`',
    ]
    return s[d]
 
def symbol0(d):
    s=[
    '``●●●●`',
    '`●```●●',
    '`●```●●',
    '`●``●`●',
    '`●`●●`●',
    '`●`●``●',
    '`●●```●',
    '`●●```●',
    '``●●●●`',
    ]
    return s[d]
 
def symbol3(d):
    s=[
    '`●●●●●`',
    '``````●',
    '``````●',
    '``````●',
    '`●●●●●`',
    '``````●',
    '``````●',
    '``````●',
    '`●●●●●`',
    ]
    return s[d]
def symbol2(d):
    s=[
    '`●●●●●`',
    '`●````●',
    '``````●',
    '``````●',
    '``●●●●●',
    '`●`````',
    '`●`````',
    '`●`````',
    '`●●●●●●',
    ]
    return s[d]
def symbol3(d):
    s=[
    '`●●●●●`',
    '``````●',
    '``````●',
    '``````●',
    '`●●●●●`',
    '``````●',
    '``````●',
    '``````●',
    '`●●●●●`',
    ]
    return s[d]
def symbol1(d):
    s=[
    '```●```',
    '``●●```',
    '```●```',
    '```●```',
    '```●```',  
    '```●```',
    '```●```',
    '```●```',
    '`●●●●●●',
    ]
    return s[d]
def symbol0(d):
    s=[
    '``●●●●`',
    '`●```●●',
    '`●```●●',
    '`●``●`●',
    '`●`●●`●',
    '`●`●``●',
    '`●●```●',
    '`●●```●',
    '``●●●●`',
    ]
    return s[d]
def symbol5(d):
    s=[
    '`●●●●●●',
    '`●`````',
    '`●`````',
    '`●`````',
    '`●●●●●`',
    '``````●',
    '``````●',
    '``````●',
    '`●●●●●`',
    ]
    return s[d]
d=9
symboldict={"4":symbol4,"0":symbol0,"3":symbol3,
"2":symbol2,"3":symbol3,"1":symbol1,
"0":symbol0,"5":symbol5}
inp=input("輸入:")
for i in range(d):
    for c in inp:
        print(symboldict[c](i),end='')
    print()
 
'''

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body.encode('utf-8') ]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
