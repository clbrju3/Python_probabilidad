import pathlib
f={}
ruta=pathlib.Path("mintic")
c={i.suffix for i in ruta.iterdir()}
for i in c:
    l=[h.name for h in ruta.glob(f"*{i}")]
    f[i]=l
print(f)