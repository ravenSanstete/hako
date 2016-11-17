"""
<Abstract Base Class or Interface>

!!! Concept of Tangle will be defined here in a machine language

Modification with little consideration is not allowed here

No library should be used here.

Concept should be independent from implementations
"""
import functools as F


from .context import monad
from .context import utils



Monad=monad.Monad;
err=F.partial(utils.err,"Tangle_Core");



class Tangle(object):
    """<Abstract Base Class or Interface> <!!Important Conceptual Class>"""
    def __init__(self):
        super(Tangle, self).__init__();
    # measurements of the type of numpy
    def eval(self,*measurements):
        # TODO: check the types
        self.__eval(measurements);
    # this should be a private routine for processing the evaluation
    # here monads is a determined length list
    def __eval(self,measurements):
        utils.require_override();
