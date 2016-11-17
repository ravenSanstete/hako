# an auxiliary method for displaying error
# which should never be used as a concrete method, please partial it
def _err(module_name,info):
    raise Exception("Module %s Error:%s" % module_name,info);
