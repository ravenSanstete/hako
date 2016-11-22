import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
path_1=os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT));
sys.path.append(os.path.join(path_1,'src'));


from src.core import *

import hako.core as hako
import monad.core as monad
import tangle.core as tangle
import magicae.core as magica
import preproc.core as feeder
import proto.core as prototype
#

# the movie-lens world structure

concepts=["u","v","r"];

# relations should be dictionary from concept_name to tuple_name
relations={
    "r":("u","v")
};
