device = {"아이폰":5, "윈도우":10}
print(device)
print(len(device))
print(device["아이폰"])

device["맥북"]=15

print(device)
print(len(device))
print(device["아이폰"])

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

device['xxx'] =20

for item in device.items():
    print(item)
