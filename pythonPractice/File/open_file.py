f = open("/Users/tabriji/Documents/GitHub/Intro-to-Python-Data-Structure/pythonPractice/File/basics.ipynb",
         "r")  # Let's open this notebook file,
# which is essentially a text file.
# So you can open it in a texteditor as well.

for i in range(100):  # And read the first five lines
    line = f.readline()
    print(f"Line {i}: {line}", end="")
f.close()
