import os

files = ["../binary/models/cross_validation/pre.py",
        "../multiclass_categorical/models/cross_validation/pre.py",
        "../multiclass_one_vs_one/models/cross_validation/pre.py",
        "../multiclass_one_vs_rest/models/cross_validation/pre.py"]

print("\n" + "#"*50)
print("\tTraining Preprocessing Classifiers")
print("#"*50 + "\n")

for file in files:
    home = os.getcwd()
    os.chdir(os.path.dirname(file))
    os.system("python ./" + os.path.basename(file))
    os.chdir(home)