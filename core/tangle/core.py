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


# a tangle class should take the same paradigm as the magica class
class Tangle(object):
    """<Abstract Base Class or Interface> <!!Important Conceptual Class>"""
    def __init__(self):
        super(Tangle, self).__init__();
    # measurements of the type of numpy
    def eval(self, measurements, batched=True):
        # TODO: check the types
        self._batch_eval(measurements) if batched else self._eval(measurements);
    # this should be a private routine for processing the evaluation
    # here monads is a determined length list
    # batched method
    def _eval(self,measurements):
        utils.require_override();
    # a batch-oriented eval interface, always along axis-0 do the slicing
    def _batch_eval(self,measurements):
        utils.require_override();
    """ 
        to distribute the error, actually there is no need for a tangler to know what kind of the prototype
        behind the hides. The distribution of the difference only depends on the formula of itself
        in other words, the _eval routine 
        
        options is used to control the runtime distribution by the hako
        
        E.g. the coupled tangle UV' is always optimized by alternatively descent. options is
        used to control this time whether to update the U factor or the V factor
        
        It's better to automatically do the distribution according to some outside factors
        
        return a dictionary of differences for each part.
    """
    def _distribute(self,diff,options):
        utils.require_override();
