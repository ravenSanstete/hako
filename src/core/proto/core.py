"""
Base Concept of Prototype defined with a python class
Prototype is always able to provide all the internal information for the invoker
Prototype can be derived as NN(Neural Network) Proto and GM(Graphical Model) Proto

"""

from .context import utils

# prototype itself should be self-explainable
class Prototype(object):
    """<!!!Important base class>"""
    # constructor, since abstract. No extra parameters are passed into
    def __init__(self):
        super(Prototype, self).__init__();
        self.__var__=utils.VarBuffer();
    # get internal parameters with a certain name
    def select(self,var_list):
        return self.__var__.get(var_list);
    # an abstract method, which provides enough structure information for the upper layer
    # <Override> is needed
    def structure_info(self):
        utils.require_override(); # force subclass to override it
    """ measurement for each model. Although prototypes seem to be not able to be measured. It can be
        considered as a convenience for implementation.
        Conceptually, this can be considered as how to measure it when prototypes and monads 1-to-1 corres
    """
    # options can be considered as a customized dictionary
    def measure(self, options):
        return self._measure(options);
    # <override> internal method
    # if batched, always along axis-0 do the arrangement
    def _measure(self, options):
        utils.require_override();
    # how to propagate the difference backwards based on the backend we use. Thus abstract it
    def propagate(self, diff):
        self._propagte(diff);
    # <override> internal method, diff may be a batch
    def _propagte(self, diff):
        utils.require_override();
