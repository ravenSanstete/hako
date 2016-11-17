"""
<Abstract Base Class or Interface>

!!! Concept of Tangle will be defined here in a machine language

Modification with little consideration is not allowed here

No library should be used here.

Concept should be independent from implementations
"""
import functools as $


from __init__ import monad
from __init__ import utils



Monad=monad.Monad;
err=$.partial(utils._err,"Tangle_Core");



class Tangle(object):
    """<Abstract Base Class or Interface> <!!Important Conceptual Class>"""
    def __init__(self):
        super(Tangle, self).__init__();
    def eval(self,*monads):
        # check the types
        check_type=$.reduce(lambda x,y:x and y, [isinstance(m,Monad) for m in monads],True);
        if(not check_type):
            err("Bad Parameter");
            raise
        self.__eval__(monads);
    # this should be a private routine for processing the evaluation
    # here monads is a determined length list
    def __eval__(self,monads):
        pass;
