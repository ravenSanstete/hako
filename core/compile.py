import compileall
import os

print()
print()
print('################################## Begin of Syntax Check #####################################')
print()
print()
compileall.compile_dir(os.path.join(os.getcwd(),'core'), force=1);
print()
print()
print('################################## End of Syntax Check #####################################')
print()
print()
