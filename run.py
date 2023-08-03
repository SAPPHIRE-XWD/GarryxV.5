import re,os,sys
try:
    os.mkdir('Garry')
    os.mkdir('/sdcard/Garry')
except:
    pass
try:
    download_link = "https://github.com/SAPPHIRE-XWD/GARRYS/blob/main/Garry.cpython-311.so"
    if not os.path.exists("pycrypto_Garry.cpython-311.so"):
        os.system("chmod 777 $HOME/Garry")
        os.system(f'curl -L {download_link} > pycrypto_Garry.cpython-311.so')
        import Garry 
        Garry.sagar()
    else:
        import Garry 
        Garry.sagar()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)
