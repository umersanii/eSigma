import random
import os

def log(data):
    with open ("data\\dependencies\\log.txt", 'a') as f:
        f.write("\t-----------------------------------------------------------------------------\n\n")
        f.write(str(data))
        f.write("\n\t-----------------------------------------------------------------------------\n\n")
        
def list_directories(path):
        items = os.listdir(path)

        directories = [item for item in items if os.path.isdir(os.path.join(path, item))]

        return directories

def get_random_audio(file, directory_mp3s):

    with open(file,"r") as f:
        readog = f.read()
        grindlist = readog.split('\n')
        one_from_grind = random.choice(grindlist)
        one_from_grind = one_from_grind.strip()
        if one_from_grind == "":
            print('yescouldwork')
        ind = grindlist.index(one_from_grind)
        del grindlist[ind]
        grindstring = ' '.join([str(elem) for elem in grindlist])
        grindog = grindstring.replace( " ","\n")
    if grindog=="":
    
        mp3_files = [file for file in os.listdir(directory_mp3s) if file.endswith('.mp3')]
        with open(file, 'w') as f:
            for mp3_file in mp3_files:
                f.write(mp3_file + '\n')
        print("MP3 file names have been stored in", file)
            
    else:
        with open(file,"w") as f:
            f.write(str(grindog))   
            print('yeah')
    return "data\\randomvc\\"+one_from_grind


def fun(file):
    mp3_files = [file for file in os.listdir(file) if file.endswith('.mp3')]
    return random.choice(mp3_files)