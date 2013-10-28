from openerp.osv import fields
from booking_chart.mixin import mixin
    
class task(mixin.resource):
    _inherit = "project.task"
    
    # ref to the booking_chart xml_id (if you have created the booking chart manually, you have to override the mixin.resource.get_chart_id method)
    _booking_chart_ref = 'demo_task.users_booking_chart'
    
    _booking_resource_map = {
        # simple mapping, booking.resource field = task field 
        'name':        'name',
        'message':     'description',
        'date_start':  'date_start',
        'date_end':    'date_end',
        # object mapping, booking.resource field = "task.field._name,task.field.id" 
        'resource_id': 'user_id',
        'target_id':   'project_id',
        # custom mapping, set booking.resource.css_class field when priority is updated with the value of task.booking_css_class
        'css_class':   'priority:booking_css_class'
    }
    
    
    def _get_booking_custom_fields(self, cr, uid, ids, field_names, arg, context=None):
        # booking resource color mapping with task.priority
        colors = {
            '0': 'red', '1': 'orange', '2': 'dark-blue',  '3': 'blue', '4': 'light-blue'
        }
        res = {}
        
        for task in self.browse(cr, uid, ids):
            res[task.id] = colors[task.priority] if task.priority in colors else ""
        
        return res
    
    # add a custom field to get the booking class css according to current status
    _columns = {
        'booking_css_class': fields.function(_get_booking_custom_fields, method=True, type='char', string='Booking CSS Class', readonly=True),
    }
       
task()