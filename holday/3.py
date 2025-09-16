import platform
import psutil

def system_info():
    print("操作系统:", platform.system(), platform.release())
    print("主机名:", platform.node())
    print("CPU 核心数:", psutil.cpu_count(logical=True))
    print("内存大小: {:.2f} GB".format(psutil.virtual_memory().total / (1024 ** 3)))

system_info()
