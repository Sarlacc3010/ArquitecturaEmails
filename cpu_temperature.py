'''import pyuac
import clr #package pythonnet, not clr

#   Instalar pywin32, pyuac, pythonnet
# Try python 3.6.5


import clr # the pythonnet module.
clr.AddReference(r'YourdllPath')
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()
while True:
    for a in range(0, len(c.Hardware[0].Sensors)):
        # print(c.Hardware[0].Sensors[a].Identifier)
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print(c.Hardware[0].Sensors[a].get_Value())
            c.Hardware[0].Update()
'''
