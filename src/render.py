import bpy
import numpy as np

# from https://blender.stackexchange.com/questions/61879/create-mesh-then-add-vertices-to-it-in-python
def add_mesh(name, verts, faces, edges=None, col_name="Collection"):    
    if edges is None:
        edges = []
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections[col_name]
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    mesh.from_pydata(verts, edges, faces)

"""
verts = [( 1.0,  1.0,  0.0), 
         ( 1.0, -1.0,  0.0),
         (-1.0, -1.0,  0.0),
         (-1.0,  1.0,  0.0),
         ]
faces = [[0, 1, 2, 3]]
add_mesh("PlaneMesh", verts, faces)
#"""

vert_hop=1
face_hop=5

verts=np.load("pointcloud.npy")
verts=verts[::vert_hop]
#faces=[list(np.arange(verts.shape[0])[::face_hop])]
faces=[]
edges=[[i,i+1] for i in range(verts.shape[0])][:-1]
add_mesh("PrintMesh",verts,faces,edges)
