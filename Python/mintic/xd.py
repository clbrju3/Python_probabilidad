import pathlib
ruta=pathlib.Path("mintic")
for i in ruta.glob("*.csv"):
    print(i)