'''
Name: TestHandler
Created on Jul 31, 2014
Description:

@author: TaiweiPan

History:
Who          When                  What
---------------------------------------


'''
import webapp2
from data_store.DataStore import NDBDataStore

class TestHandler(webapp2.RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        """Handles default landing page"""
        #NDBDataStore().add_user("123", "google", "Taiwei")
        #NDBDataStore().get_user_key("taiwei608")
        #NDBDataStore().add_url("taiwei608", "www.AVerMedia.com", "search", ["search", "mail"])
        NDBDataStore().get_rul_info("taiwei608", "www.yahoo.com")