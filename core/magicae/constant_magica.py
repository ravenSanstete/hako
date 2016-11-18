from .context import op
from .context import htype
from .core import Magica


# a constant one should be distinct from a linear one. Although they seems to be conceptually related
class ConstMagica(Magica):
    """docstring for ConstMagica."""
    # constructor
    def __init__(self, scale=1):
        super(ConstMagica, self).__init__()
    #
    # the restriction of using a constant magica is that only a prototype is needed
    # sub_measurements: a list of backend object
    def _measure(self, sub_measurements, parameters):
        assert(len(sub_measurements)==1);
        return op.scalar_mul(parameters['scale'], sub_measurements[0]);
    # return a list of the distributed difference list (same type as the sub_measurements)
    # prototypes passed for reference
    # diff may be a batch, thus the sublist should be a matrix maybe, along axis-0 do the arrangement
    def _distribute(self, prototypes, diff, parameters):
        return [op.div(diff,parameters['scale'])];
    # return parameters of the instance of this kind of magica for a certain monad
    # a dictionary with name is needed
    def _allocate(self,prototypes):
        return {
            'scale':htype.constant(self.__scale__,dtype=htype.float32)
        }
        
    
        
