"""
A wrapper for buffer implemented with a set. Basically for monad usage and hako usage
monad: prototype ptrs
hako: monad ptrs

Intuitively, set buffer must be more efficient than dictionary buffer
"""


class SetBuffer(object):
    """class SetBuffer. which stores anonymous elements"""
    def __init__(self, arg):
        super(SetBuffer, self).__init__()
        self.__set__=set();
    # return the iterator of the set itself
    def get(self):
        return self._get();
    # internal method
    def _get(self):
        return enumerate(self.__set__);
    # no need for determining whether update or not, since set
    def put(self,new_item):
        self._put(new_item);
    # internal method
    def _put(self,new_item):
        self.add(new_item);
