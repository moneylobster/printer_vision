import gcody
import numpy as np
import subprocess

import convert

# read blender path
with open('blender_cmd.config') as f:
    blender_cmd = f.read()

gcode_file="../gcodes/0404_028_50T_O1_LRDRIVE_X2.g"

# convert the gcode file
converted=convert.convert_gcode(gcode_file)

gc=gcody.read(converted)

vertices=np.array(gc.history)
# we don't track when the nozzle is extruding,
# so for now, to prevent lines to and from the home position,
# get rid of the first few and last few points.
vertices=vertices[10:-10]
# change units from mm to m.
vertices=vertices/1000

np.save("pointcloud.npy", vertices)


# run blender
percentage=75
colorvec=(1,1,0,1)
subprocess.call([blender_cmd, "--python", "render.py", "--", "-p", str(percentage), "-c", str(colorvec)])
