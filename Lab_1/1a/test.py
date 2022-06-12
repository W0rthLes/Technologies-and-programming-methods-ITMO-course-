import os
names = []
for root, dirs, files in os.walk("."):  
    for filename in files:
        names.append(filename)
print(names)