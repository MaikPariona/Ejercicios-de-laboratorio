
try:
    import numpy as np
except ImportError:
    print("Error al importar NumPy.")
    raise  

assert hasattr(np, 'array'), "NumPy no se ha importado correctamente"

print("El módulo NumPy se ha importado correctamente.")
