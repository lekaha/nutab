'''
Name: main
Created on Jul 6, 2014
Description:

@author: lekaha

History:
Who          When                  What
---------------------------------------


'''

import webapp2

class MainPage(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)