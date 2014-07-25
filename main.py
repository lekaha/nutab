'''
Name: main
Created on Jul 6, 2014
Description:

@author: lekaha

History:
Who          When                  What
---------------------------------------
John         2014/7/25             Divide handler

'''
from secrets import SESSION_KEY
from webapp2 import WSGIApplication, Route
        

# webapp2 config
app_config = {
  'webapp2_extras.sessions': {
    'cookie_name': '_nutab_sess',
    'secret_key': SESSION_KEY
  },
  'webapp2_extras.auth': {
    'user_attributes': []
  }
}

# Map URLs to handlers
routes = [
  Route('/', handler='MainHandler.RootHandler')
#   ,Route('/xxx', handler='handlers.XXXHandler')
]

app = WSGIApplication(routes, config=app_config, debug=True)
