import gcody
import numpy as np

import convert



gcode_file="../gcodes/0404_028_50T_O1_LRDRIVE_X2.g"

# convert the gcode file
converted=convert.convert_gcode(gcode_file)

gc=gcody.read(converted)

vertices=np.array(gc.history)

np.save("pointcloud.npy", vertices)

'''


def add_mesh(name, verts, faces, edges=None, col_name="Collection"):    
    if edges is None:
        edges = []
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections[col_name]
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    mesh.from_pydata(verts, edges, faces)

verts = [( 1.0,  1.0,  0.0), 
         ( 1.0, -1.0,  0.0),
         (-1.0, -1.0,  0.0),
         (-1.0,  1.0,  0.0),
         ]
faces = [[0, 1, 2, 3]]
add_mesh("myBeautifulMesh_1", verts, faces)

verts = [( 3.0,  1.0,  0.0), 
         ( 3.0, -1.0,  0.0),
         ( 2.0, -1.0,  0.0),
         ( 2.0,  1.0,  0.0),
         ]
add_mesh("myBeautifulMesh_2", verts, faces)
'''
