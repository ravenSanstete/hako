"""
Base Concept of Prototype defined with a python class
Prototype is always able to provide all the internal information for the invoker
Prototype can be derived as NN(Neural Network) Proto and GM(Graphical Model) Proto

"""


class Prototype(object):
    """<!!!Important base class>"""
    # constructor, since abstract. No extra parameters are passed into
    def __init__(self):
        super(Prototype, self).__init__();
    # get internal parameters with a certain name
    def select(self,var_name):
