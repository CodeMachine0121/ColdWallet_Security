import bluetooth


print("Search target bluetooth device with address ...")
nearby_devices = bluetooth.discover_devices(duration=3,lookup_names = True) #Search device nearby

print ("There are %d devices" %(len(nearby_devices)))
for addr, name in nearby_devices:
    print("  %s - %s" %(addr, name)) #print device address and name
    device_name = name

