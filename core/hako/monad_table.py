""" 
    this should be implemented as a high-performance look-up table for the ptrs
    to the prototypes and together the extra information of each monad passing to the 
    magica to do the mixing
    
    which should support batch search of informations of each monad
    
    A c implementation is welcomed
    
    And overloading of operator is better
""" 


class Monad_T(object):
    """monad table."""
    def __init__(self, arg):
        super(Monad_T, self).__init__();
        
