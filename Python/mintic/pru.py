import pathlib
r=pathlib.Path("Users")
for i in r.glob("*.csv"):
    print(i)
