from mathutils import Vector, Quaternion
from math import radians

axis = Vector((1,0,0)) # x-axis(direction)
angle = radians(90) # 90 degrees in radians
quat = Quaternion(axis,angle) # 90 deg around x
print("The rotation is ", quat)