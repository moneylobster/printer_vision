import gcody
import numpy as np

import convert



gcode_file="../gcodes/0404_028_50T_O1_LRDRIVE_X2.g"

# convert the gcode file
converted=convert.convert_gcode(gcode_file)

gc=gcody.read(converted)

vertices=np.array(gc.history)
# change units from mm to m.
vertices=vertices/1000

np.save("pointcloud.npy", vertices)

# points=pv.wrap(vertices[::1])

# surf=points.reconstruct_surface(nbr_sz=8,progress_bar=True)

# faces=list(surf.faces)
# facelis=[faces[i+1:i+4] for i in range(0, len(faces), 4)]

# np.save("verts.npy",surf.points)
# np.save("faces.npy",facelis)
