import os
import sys 
import tabulate 
import psutil 
import platform 
import time 
import datetime 
from datetime import datetime 

os.system(' clear ')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("="*40, "Disk Information", "="*40)
time.sleep(0.1)
print("Partitions and Usage:")
partitions = psutil.disk_partitions()
for partition in partitions:
    time.sleep(0.1)
    print(f"=== Device: {partition.device} ===")
    time.sleep(0.1)
    print(f"  Mountpoint: {partition.mountpoint}")
    time.sleep(0.1)
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    time.sleep(0.1)
    print(f"  Total Size: {get_size(partition_usage.total)}")
    time.sleep(0.1)
    print(f"  Used: {get_size(partition_usage.used)}")
    time.sleep(0.1)
    print(f"  Free: {get_size(partition_usage.free)}")
    time.sleep(0.1)
    print(f"  Percentage: {partition_usage.percent}%")
disk_io = psutil.disk_io_counters()
time.sleep(0.1)
print(f"Total read: {get_size(disk_io.read_bytes)}")
time.sleep(0.1)
print(f"Total write: {get_size(disk_io.write_bytes)}")