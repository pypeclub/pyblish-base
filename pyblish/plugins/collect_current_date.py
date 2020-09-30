
import pyblish.api
import pyblish.lib


class CollectCurrentDate(pyblish.api.ContextPlugin):
    """Inject the current time into the Context"""

    order = pyblish.api.CollectorOrder
    label = "Current date"

    def process(self, context):
        if 'date' not in context.data:
            context.data['date'] = pyblish.lib.time()
