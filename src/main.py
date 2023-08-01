import gcody
import numpy as np
import subprocess
import os

import convert

# read blender path
print("reading blender path config...")
with open('blender_cmd.config') as f:
    blender_cmd = f.read()
print("read blender path.")

gcode_file="../gcodes/test_part-Body.g"

# convert the gcode file
print("converting gcode file...")
converted=convert.convert_gcode(gcode_file)

print("reading processed gcode file...")
gc=gcody.read(converted)

vertices=np.array(gc.history)
# we don't track when the nozzle is extruding,
# so for now, to prevent lines to and from the home position,
# get rid of the first few and last few points.
vertices=vertices[10:-10]
# change units from mm to m.
vertices=vertices/1000

np.save("pointcloud.npy", vertices)


print("starting blender render...")
# run blender
percentage=75
colorvec=(1,1,0,1)
subprocess.call([blender_cmd,"--background", "--python", "render.py", "--", "-p", str(percentage), "-c", str(colorvec), "-o", os.path.join(os.getcwd(),"render.png")])
