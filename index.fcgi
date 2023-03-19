import os, sys
 
from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application
 
sys.path.insert(0, "/home/CONTA/mydjango")
os.environ['DJANGO_SETTINGS_MODULE'] = "mydjango.settings"
 
WSGIServer(get_wsgi_application()).run()