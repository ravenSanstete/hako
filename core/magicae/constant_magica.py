from .context import op
from .core import Magica


# a constant one should be distinct from a linear one. Although they seems to be conceptually related
class ConstMagica(Magica):
    """docstring for ConstMagica."""
    # constructor
    def __init__(self, scale=1):
        super(ConstMagica, self).__init__()
        self.__scale__=scale;
    #
    # the restriction of using a constant magica is that only a prototype is needed
    # sub_measurements: a list of backend object
    def _measure(self, sub_measurements):
        assert(len(sub_measurements)==1);
        return op.scalar_mul(self.__scale__,sub_measurements[0]);
    # return a list of the distributed difference list (same type as the sub_measurements)
    # prototypes passed for reference
    # diff may be a batch, thus the sublist should be a matrix maybe, along axis-0 do the arrangement
    def _distribute(self, prototypes, diff):
        return [op.div(diff,self.__scale__)];
        
