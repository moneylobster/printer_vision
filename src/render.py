import bpy
import numpy as np
import argparse
import sys
import ast
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

def create_curve(coords, colorvec):
    #define material with specified color
    matf = bpy.data.materials.new("Filament")
    matf.use_nodes = True
    tree = matf.node_tree
    nodes = tree.nodes
    bsdf = nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = colorvec
    matf.diffuse_color = colorvec
    
    #create curve
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
    #apply Filament material to object
    curveOB.active_material=matf
    #add to scene
    col.objects.link(curveOB)
    

# get percentage of gcode to render
parser=argparse.ArgumentParser()
parser.add_argument("-p", "--percentage", nargs="?", default=100, help="Percentage of vertices to include.")
parser.add_argument("-c", "--color", default="(0, 1, 0, 1)", help="Filament color as vector (r,g,b,a)")
args=parser.parse_args(sys.argv[sys.argv.index("--")+1:])
percentage=float(args.percentage)/100 #0-100 to 0-1
colorvec=ast.literal_eval(args.color)

# load vertex data from file
verts=np.load("pointcloud.npy")

# strip away vertices according to arg
verts=verts[:floor(verts.shape[0]*percentage)]

# clear meshes in the scene
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)

# add mesh
create_curve(verts, colorvec)
