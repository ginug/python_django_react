import os
from sys import argv
from sys import stderr
def make_at(path, dir_name):
    original_path=os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(test2,mode = 0o777)
    except OSError as e:
        print(e)
        raise
    finally:
        os.chdir(original_path)

def main(path, dir_name):
    make_at(path, dir_name)

if __name__=='__main__':
    test1='/Users/Ginu'
    test2='Ginu2'
    main(test1,test2)
        