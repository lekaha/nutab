'''
Name: data_store.datastore
Created on Jul 6, 2014
Description:

@author: Taiwei Pan

History:
Who          When                  What
---------------------------------------
Taiwei Pan   2014/7/31             

'''

from google.appengine.ext import ndb
import logging

class NDBDataStore(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
                
    def is_user_exist(self, user_id):
        user = UserInfo.query(UserInfo.user_id == user_id).fetch()
        if user:
            logging.info("user exist")
            return True
        else:
            logging.info("user not exist")
            return False
    
    def add_user(self, user_id, oauth_type, user_name):
        if  not self.is_user_exist(user_id):
            user = UserInfo()
            user.user_id = user_id
            user.oauth_type = oauth_type
            user.user_name = user_name
            user.put()
    
    def get_user_key(self, user_id):
        user = UserInfo.query(UserInfo.user_id == user_id).fetch()
        if user:
            logging.info(user[0].key)
            return user[0].key
        else:
            return None
    
    def add_url(self, user_id, url, group, tags):
        if self.is_user_exist(user_id):
            new_url = UrlInfo(parent = self.get_user_key(user_id))
            new_url.url = url
            new_url.group = group
            new_url.tags = tags
            new_url.put()
    
    def get_rul_info(self, user_id, url):
        if self.is_user_exist(user_id):
            key = self.get_user_key(user_id)
            user_url_query = UrlInfo.query(ancestor = key)
            url_infos = user_url_query.filter(UrlInfo.url == url).fetch()
            for url_entry in url_infos:
                logging.info(url_entry)
            return url_entry
                
        
class BaseInfo(ndb.Model):
    create_time = ndb.DateTimeProperty(auto_now_add = True)
    last_modify_time = ndb.DateTimeProperty(auto_now = True)
    
class UrlInfo(BaseInfo):
    url = ndb.StringProperty()
    group = ndb.StringProperty()
    tags = ndb.StringProperty(repeated = True)
    
class UserInfo(BaseInfo):
    user_id = ndb.StringProperty(required = True)
    user_name = ndb.StringProperty()
    oauth_type = ndb.StringProperty()
    
    