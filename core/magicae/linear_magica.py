import functools as F

from .context import op
from .context import htype
from .core import Magica



# magica of common usage, with a linear combination of prototypes
# you can decide which type of constraints should be imposed on the weight parameters

# only one-dimension linear magica is implemented here
# two dimension one may be like the convolutional layer

# the dictionary each magica allocate should share concept with other functions of the magica


class LinearMagica(Magica):
    """docstring for LinearMagica."""
    def __init__(self,constraint=None):
        super(LinearMagica, self).__init__();
        self.__constraint__=constraint;
    # the restriction of using a constant magica is that only a prototype is needed
    # sub_measurements: a list of backend object
    # assume each sub_measurements have the same type
    # util I findout an efficient way to combine not homogeneous features
    def _measure(self, sub_measurements, parameters):
        return F.reduce(lambda i:op.add(op.scalar_mul(parameters['weights'][i],sub_measurements[i])),range(len(sub_measurements)));
    # return a list of the distributed difference list (same type as the sub_measurements)
    # prototypes passed for reference
    # diff may be a batch, thus the sublist should be a matrix maybe, along axis-0 do the arrangement
    def _distribute(self, prototypes, diff, parameters):
        return [op.div(diff,parameters['weight'][i]) for i in range(len(prototypes))];
    # return parameters of linear magica for a certain monad
    # a dictionary with name is needed
    def _allocate(self,prototypes):
        if(constraint==None or True):
            # the default behavior of random uniform is to sample each mixture weight from [0,1)
            return {
                'weight':htype.variable(htype.random_uniform([len(prototypes)]))
            }
        # unimplemented behavior
        
