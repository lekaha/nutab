'''
Name: app_controller
Created on Jul 6, 2014
Description:

@author: Taiwei Pan

History:
Who          When                  What
---------------------------------------
Taiwei       2014/7/31             Define basic functions.

'''

class Controller(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    # User related
    def is_user_exist(self, user_id):
        '''
        Check is this user_id has registered.
        '''
        pass
    
    def add_user(self, user_id, oauth_type, user_name):
        '''
        Add a new user with user_id and user_name.
        '''
        pass
    
    def delete_user(self, user_id):
        '''
        Remove user with user_id.
        '''
        pass
        
    # Data related
    def upload_urls(self, user_id, url_list):
        '''
        pass
        Analyze these urls and add them to database.
        '''
        pass
        
    def get_urls_info(self, user_id, url_list):
        '''
        Get urls info from database.
        '''
        pass
        
        
        
        
        