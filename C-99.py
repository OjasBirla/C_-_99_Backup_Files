import time, os, shutil

path = "C:/Users/Ojas/Dropbox/My PC (DESKTOP-MGULJTT)/Pictures/Camera Roll"
days = 30
todays_time = time.time()

def get_ctime(path):
    return os.stat(path).st_ctime

if(os.path.exists(path)):
    index = 0

    start = True

    while(start):
        for (root, dirs, files) in os.walk(path):
            if(index < len(dirs)):
                if(todays_time - get_ctime(path + dirs[index]) > days * 60 * 60 * 24):
                    shutil.rmtree(path + dirs[index])

            if(index < len(files)):
                if(todays_time - get_ctime(path + "/" + files[index]) > days * 60 * 60 * 24):
                    os.remove(path + "/" + files[index])

            index += 1

        if(index > len(files) and index > len(dirs)):
            start = False
            
    print("Done")

else:
    print("Path not found")
