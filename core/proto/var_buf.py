"""
var_buf: provide an wrapper for buffering the parameters of a Model
assumed to provide a fast query for parameters with certain name

# why needs to isolate such a submodule?
since each prototype machine can be either simple or rather complicated
There is a need to provide such a structure to collect all the parameter pointers

"""

# performance is not within consideration right now 161117


import functools as $

from __init__ import utils

err=$.partial(utils._err,"VarBuffer");

class VarBuffer(object):
    """An accessible buffer for storing paramters and variables of a prototype model"""
    def __init__(self):
        super(VarBuffer, self).__init__();
        # use a dictionary as a stub firstly
        self.__dict__=dict();
    # is_update: True ignore name conflict. Otherwise, Name Conflict raise
    def put(self,var_name,var_ptr,is_update=False):
        self.__dict__[var_name]=var_ptr if self.__map__[var_name]==None or is_update else err("Naming Conflict");
    # return the variable with a specified name, None is thus raised. Since Computation becomes non-sense
    # allow lazy get ?
    def get(self,var_name):
        return self.__dict__[var_name];
    #  pull means you can at one time get all the variables you want
    def pull(self,*var_names):
        return list($.map(self.get,var_names));
