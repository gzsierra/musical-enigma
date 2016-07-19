import psutil, sendInfo

while 1==1 :
    cpu = psutil.cpu_percent(interval=5)
    mem = psutil.virtual_memory().percent

    # print("CPU : " + str(cpu) + "   Mem : " + str(mem), end='\r')

    sendInfo.sendInfo(cpu, mem)
