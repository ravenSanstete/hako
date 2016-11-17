""""
Base class for one basic component monad

"""
from .context import utils
from .context import magicae


class Monad(object):
    """Monad.
    <Abstract Base Class or Interface> <!!Important Conceptual Class>
    """
    ## Be carefule, prototypes should be a list of prototypes.
    ## And magica is a concept for mixing prototypes, which returns something that is measurable
    ## whether should we allow magica to be lazy?　
    # magica here should be a pointer to a global defined magica
    # options can be None. A list for meta-infos to measure each prototype-dedicated monad
    # you are not allowed to modify the measure options once determined
    def __init__(self, prototypes, magica, options=None):
        super(Monad, self).__init__();
        assert(isinstance(magica,magicae.Magica));
        self._propagte,self._measure=magica.mix(prototypes);
    # override. define the behavior of measuring a monad with some certain external factors
    # which can be DIY-ed by users. Timestamp seems a rational factor.
    # the composition can be happened here or just
    def measure(self,options):
        return self._measure(options);
    # propagate the difference of the measurement and the observed information to prototypes
    def propagate(self, diff):
        self._propagte(self,diff);
