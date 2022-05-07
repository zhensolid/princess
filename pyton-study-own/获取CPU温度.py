
# 有了这个Python脚本，你将不需要任何软件来了解CPU的温度

import psutil
psutil.cpu_count() # CPU逻辑数量
psutil.cpu_count(logical=False) # CPU物理核心
psutil.virtual_memory()
psutil.virtual_memory().percent #获取内存使用率
psutil.swap_memory()
psutil.disk_partitions() # 磁盘分区信息
psutil.disk_usage('/') # 磁盘使用情况
psutil.disk_io_counters() # 磁盘IO


# ! 获取CPU温度  模块问题等待解决
# from time import sleep
# from pyspectator.processor import Cpu
# cpu = Cpu(monitoring_latency=1)
# with cpu:
#     while True:
#         print(f'Temp: {cpu.temperature} °C')
#         sleep(2)
