import os
filePath = '/home/somedir/Documents/python/logs'

if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")
