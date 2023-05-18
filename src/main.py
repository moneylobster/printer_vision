import gcody
import numpy as np

import convert



gcode_file="../gcodes/0404_028_50T_O1_LRDRIVE_X2.g"

# convert the gcode file
converted=convert.convert_gcode(gcode_file)

gc=gcody.read(converted)

vertices=np.array(gc.history)

np.save("pointcloud.npy", vertices)
