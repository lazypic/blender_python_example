# print vertices location
import bpy
from mathutils import Vector

ob = bpy.data.objects['matrix']
vert = ob.data.vertices
for v in vert:
    v.co = v.co + Vector((1,0,0))