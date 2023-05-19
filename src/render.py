import bpy
import numpy as np
import argparse
from math import floor

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

def create_curve(coords):
    crv = bpy.data.curves.new('pCurve', 'CURVE')
    crv.dimensions = '3D'
    polyline = crv.splines.new('POLY')
    polyline.points.add(len(coords)-1)
    for i, coord in enumerate(coords):
        x,y,z = coord
        polyline.points[i].co = (x, y, z, 1)
    curveOB = bpy.data.objects.new('PrintCurve', crv)
    crv.bevel_depth = 0.0004 # approx nozzle size 0.4 mm.
    col = bpy.data.collections["Collection"]
    col.objects.link(curveOB)

# get how much of the 
parser=argparse.ArgumentParser()
parser.add_argument("percentage", nargs="?", default=100, help="Percentage of vertices to include.")
args = parser.parse_args()
percentage=args.percentage/100 #0-100 to 0-1

# load vertex data from file
verts=np.load("pointcloud.npy")

# strip away vertices according to arg
verts=verts[:floor(verts.shape[0]/percentage)]

# clear meshes in the scene
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)

# add mesh
create_curve(verts)
