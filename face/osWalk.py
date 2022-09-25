from dis import dis
# from importlib.metadata import files
import os 


imgDirs = ('/home/shary/Desktop/AI/paul/face/demoImages/known')
name = []
for root,dirs,filesz in os.walk(imgDirs):
    print('root is :',root)
    # print('dirs inside the root is :',dirs)
    # print('file inside this roots :',filesz)
    for nm in filesz:
        path = os.path.join(root,nm)
        nm1 = nm.strip('.jpg')
        name.append(nm1)
        print(path)
# print(path)
