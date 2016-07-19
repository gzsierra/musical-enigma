#!/usr/bin/python3
import psutil, sendInfo

while 1==1 :
    # Every second, it will fetch data
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent

    sendInfo.update(str(cpu), str(mem))

    # For debug
    # print("CPU : " + str(cpu) + "   Mem : " + str(mem), end='\r')
