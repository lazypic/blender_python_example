# print vertices location
import bpy

ob = bpy.data.objects['matrix']
vert = ob.data.vertices
for v in vert:
    print(v.co)