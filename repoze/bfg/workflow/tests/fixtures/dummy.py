from zope.interface import Interface
from zope.interface import implements

from repoze.bfg.workflow import Workflow # imported

class IContent(Interface):
    pass

class Content(object):
    implements(IContent)

def callback(context, transition):
    pass

def elector(context):
    return True

def has_permission(permission, context, request):
    pass