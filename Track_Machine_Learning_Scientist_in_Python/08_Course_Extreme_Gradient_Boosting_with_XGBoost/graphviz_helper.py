import os
os.environ["PATH"] += os.pathsep + "C:\\Program Files\\Graphviz\\bin"

import graphviz
print(graphviz.__version__)  # Should still print 0.20.3