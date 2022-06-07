with open("new-text.txt", "a+") as MyFile:
    OpenedDoc = MyFile.read()
    MyFile.write("Written via Python")
