import psutil
import time

class CpuWatcher:

    def __init__(self,cpu_probing_freq,cpu_probing_time):
        self.last_cpu_load = 100
        self.cpu_freq = cpu_probing_freq
        self.cpu_time = cpu_probing_time

    def watch(self):
        while True:
            self.last_cpu_load = psutil.cpu_percent(self.cpu_time*60)
            time.sleep(self.cpu_freq*60)