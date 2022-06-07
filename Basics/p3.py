# This programme will fetch data from txt file each 10 seconds.
# And this programme never stops.


import time  # builtin
import os  # standard
import pandas  # third-party

while True:
    if os.path.exists("p3-related.txt."):
        with open("p3-related.txt", 'r') as MyFile:
            print(MyFile.read())
    elif os.path.exists("p3-related.csv"):
        data = pandas.read_csv("p3-related.csv")
        print(data.mean())
    else:
        print("File doesn't exist")
        # open("p3.txt")

    time.sleep(5)
