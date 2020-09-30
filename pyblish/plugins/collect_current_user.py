
import getpass
import pyblish.api


class CollectCurrentUser(pyblish.api.ContextPlugin):
    """Inject the currently logged on user into the Context"""

    order = pyblish.api.CollectorOrder
    label = "Current user"

    def process(self, context):
        if 'user' not in context.data:
            context.data['user'] = getpass.getuser()
