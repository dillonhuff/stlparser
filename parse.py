import sys
import struct

class Vec3:
    def __init__(self, x_coord, y_coord, z_coord):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

class Triangle:
    def __init__(self, normal, v0, v1, v2):
        self.normal = normal
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

class STLData:
    def __init__(self, header, tris):
        self.header = header
        self.tris = tris

def readFloat(f):
    float_bytes = f.read(4)
    return struct.unpack('f', float_bytes)[0]

def readVec3(f):
    x = readFloat(f)
    y = readFloat(f)
    z = readFloat(f)

    return Vec3(x, y, z)
    
def readUnsignedInt(f):
    uint_bytes = f.read(4)
    return struct.unpack('I', uint_bytes)[0]

def readTriangle(f):
    norm = readVec3(f)
    v0 = readVec3(f)
    v1 = readVec3(f)
    v2 = readVec3(f)

    return Triangle(norm, v0, v1, v2)

def printVec3(v):
    print '(', v.x, ', ', v.y, ', ', v.z, ')'

f = open(sys.argv[1], "rb")

header = f.read(80)

print "STL HEADER = ", header

num_tris = readUnsignedInt(f)

print "Num triangles = ", num_tris

tris = []

for i in range(num_tris):
    tris.append(readTriangle(f))

stlData = STLData(header, tris)

for triangle in stlData.tris:
    print "---- TRIANGLE ----"

    printVec3(triangle.normal)
    print
    printVec3(triangle.v0)
    print
    printVec3(triangle.v1)
    print
    printVec3(triangle.v2)

    print
    print
