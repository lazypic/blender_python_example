import bpy
ob = bpy.context.object

print("Name is", ob.name)
print("It is", ob.type)

print("Scale is", ob.scale)
print("Location is", ob.location)
print("Rotation is", ob.rotation_quaternion)