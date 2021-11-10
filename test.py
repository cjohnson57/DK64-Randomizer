import struct

lst = [0,1,2,3];

print(struct.pack(len(lst)*"B",*lst))