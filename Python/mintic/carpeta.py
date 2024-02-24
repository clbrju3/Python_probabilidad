import pathlib
ruta=pathlib.Path("mintic")
archivo=ruta/"mi.txt"
carpeta=ruta/"txt"
carpeta.mkdir()
archivo.replace(carpeta/"siuuu")
