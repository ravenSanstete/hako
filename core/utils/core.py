import functools as F
# an auxiliary method for displaying error
# which should never be used as a concrete method, please partial it
def err(module_name,info):
    raise Exception("Module %s Error:%s" % module_name,info);

def require_override():
    raise NotImplementedError;

# check a list of instance, whether they share the same types

# more complicated check routines will be defined after finishing the type system module
def check_types(instance_list,class_ptr):
    return F.reduce(lambda x,y:x and y, [isinstance(m,class_ptr) for m in instance_list],True);


# entry ports for other modules
from .map_buf import MapBuffer
from .set_buf import SetBuffer
