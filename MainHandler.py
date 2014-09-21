'''
Name: MainHandler
Created on Jul 25, 2014
Description:

@author: lekaha

History:
Who          When                  What
---------------------------------------


'''
import webapp2

class RootHandler(webapp2.RequestHandler):
    '''
    classdocs
    '''
    
    def get(self):
        """Handles default landing page"""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        
    def post(self):
        """ Handles default landing page """
        name = self.request.get("name")
        password = self.request.get("password")
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Name: ' + name + ', Pw:  ' + password)
        print "Name: " + name + ", Pw: " + password
        