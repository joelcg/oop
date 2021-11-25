import psutil as psu

class monitor1:

  def __mem_swap(self):
    print(self.psu.swap_memory())

  def _nic_addr(self):
    print(self.psu.net_if_addrs())

  def _nic_info(self):
    print(self.psu.net_if_stats())
  
  def __list_users(self):
    print(self.psu.users())

  def __list_disks(self):
  	print(self.psu.disk_partitions())

  def cpu_usage(self):
  	print(self.psu.cpu_percent() + " %")

  def _cpu_freq(self):
  	print(self.psu.cpu_freq())
    
class monitor2:

  def _vmem(self):
    print(self.psu.virtual_memory())

  def cpu1(self):
    print(self.psu.cpu_percent(1), "%")

  def cpu2(self):
    print(self.psu.cpu_percent(2), "%")
  
  def cpu3(self):
    print(self.psu.cpu_percent(3), "%")

  def cpustat(self):
    print(self.psu.cpu_stats())

  def diskC(self):
    print("Disk C:", self.psu.disk_usage("C:"))
    self.__diskD()

  def __diskD(self):
    print("Disk D:", self.psu.disk_usage("D:"))
