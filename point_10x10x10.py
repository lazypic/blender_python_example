import bpy

mesh = bpy.data.meshes.new("matrix")
objects = bpy.data.objects.new("matrix", mesh)
bpy.context.scene.collection.objects.link(objects)
points = []
for x in range(0,10):
    for y in range(0, 10):
        for z in range(0,10):
            points.append((x,y,z))
mesh.from_pydata(points, [], [])
