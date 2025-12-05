import re

pattern = re.compile('name="(.+?)"')
names = []
with open("./robot.sdf") as f:
    content = f.read()
    names = re.findall(pattern, content)

with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

chinese = re.compile(r"[\u00ff-\uffff]+")
parts = set()
for name in names:
    parts = parts.union(set(re.findall(chinese, name)))

print(parts)
