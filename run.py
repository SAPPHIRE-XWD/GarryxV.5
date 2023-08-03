import re,os,sys
try:
    os.mkdir('Garry')
    os.mkdir('/sdcard/Garry')
except:
    pass
try:
    download_link = "https://github.com/SAPPHIRE-XWD/GarryxV.5/blob/main/Garryx.so"
    if not os.path.exists("pycrypto_Garryx.so"):
        os.system("chmod 777 $HOME/Garry")
        os.system(f'curl -L {download_link} > pycrypto_Garryx.so')
        import Garryx
        Garryx.sagar()
    else:
        import Garryx
        Garryx.sagar()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)
