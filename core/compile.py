import compileall
import os



compileall.compile_dir(os.path.join(os.getcwd(),'core'), force=1);
