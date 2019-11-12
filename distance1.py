import datetime
import math
from bluepy.btle import Scanner, DefaultDelegate
from filterdemo import kalman_filter_rssi


# part of UUID
# uuid="8856"
class ScanDelegate(DefaultDelegate):
    def _int_(self):
        DefaultDelegate.__init__(self)

    def handleDiscoverry(self, dev, isNewDev, isNewData):
        if isNewData:
            print("Discovered new data from", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(0.3)


def CalculateDistance(rssi, onerssi):
    " calculate the distance between Receiver and Transmitter "
    # 1rssi:rssi of 1 meter away
    ratio = rssi / onerssi
    if ratio < 1:
        return math.pow(ratio, 10)
    else:
        distance = (0.89976) * math.pow(ratio, 7.7095) + 0.111
        return distance


for dev in devices:
    for (adtype, desc, value) in dev.getScanData():
        if str(value).find("8856") != -1:
            # output current time
            device_rssi=kalman_filter_rssi(dev.rssi)
            print(datetime.datetime.now().strftime('%H:%M:%S'))
            print("Devices %s (%s),RSSI=%d dB" % (dev.addr, dev.addrType, device_rssi))
            print("%s= %s" % (desc, value))
            distance = CalculateDistance(device_rssi, -60)
            print("distance is %s" % distance)
