import sys
import struct

class Vec3:
    def __init__(self, x_coord, y_coord, z_coord):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord


def readFloat(f):
    float_bytes = f.read(4)
    return struct.unpack('f', float_bytes)[0]

def readUnsignedInt(f):
    uint_bytes = f.read(4)
    return struct.unpack('I', uint_bytes)[0]

f = open(sys.argv[1], "rb")

header = f.read(80)

print "HEADER = ", header

num_tris = readUnsignedInt(f)

print "Num triangles = ", num_tris

for i in range(num_tris):
    for j in range(12):
        print i, j
    
