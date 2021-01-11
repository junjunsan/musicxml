import os
print(os.getcwd())

for name in os.listdir(os.getcwd()):
    print(name)
for name in os.listdir(os.path.join(os.getcwd(),"csv")):
    print(name)
    