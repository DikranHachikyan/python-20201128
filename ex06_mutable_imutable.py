# %%
s1 = 'Hello'
s2 = 'Hello'

id(s1) == id(s2)
# %%
class Point:
    def __init__(self, x):
        self.x = x
# %%

p1 = Point(x = 10)
p2 = Point(x = 10)
# %%
id(p1) == id(p2)
# %%
id(p1.x) == id(p2.x)

# %%
s1 = 'Hello' * 300
s2 = 'Hello' * 300

id(s1) == id(s2)
# %%
