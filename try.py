import pandas as pd

df = pd.read_json("resources/examples/format.json")

print(df.shape)

print(dir(df))

# df = pd.DataFrame(listobject)
# df.max("datumkolumn")
# klassen innehåller en körning som kolla om datan finns tidigare. Första körningen tar längre tid

