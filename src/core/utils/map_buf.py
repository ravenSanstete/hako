"""
var_buf: provide an wrapper for buffering the parameters of a Model
assumed to provide a fast query for parameters with certain name

# why needs to isolate such a submodule?
since each prototype machine can be either simple or rather complicated
There is a need to provide such a structure to collect all the parameter pointers

"""

# performance is not within consideration right now 161117

# trivial data structures

import functools as F
from types import *
from .core import *



err=F.partial(err,"MapBuffer");

class MapBuffer(object):
    """buffer implemented with hashmap as its back end"""
    def __init__(self):
        super(MapBuffer, self).__init__();
        # use a dictionary as a stub firstly
        self.__dict__=dict();
    # is_update: True ignore name conflict. Otherwise, Name Conflict raise
    def put(self,var_name,var_ptr,is_update=False):
        self.__dict__[var_name]=var_ptr if self.__map__[var_name]==None or is_update else err("Naming Conflict");
    # return the variable with a specified name, None is thus raised. Since Computation becomes non-sense
    # allow lazy get ?
    def _get(self,var_name):
        return self.__dict__[var_name];
    #  pull means you can at one time get all the variables you want
    def _pull(self,var_names):
        return list(F.map(self.get,var_names));
    # var_names should be a list or a single string, or nothing, which return the numerator
    def get(self,var_names):
        if(var_names==None): return enumerate(self.__dict__);
        return self._get(var_names) if type(var_names)==StringType else self._pull(var_names);
