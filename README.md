# Printer Vision (WIP) (on hold)

Automated visual inspection of 3D prints.
The plan is to render the image we expect to see from the printer camera based on the print info, and then compare with the actual image to check for problems.

We'll initially test a naive approach where we try to get the expected image as close to reality as possible, and check for image differences.

## To-do

- [ ] Render expected camera scene in Blender
- [ ] Add postprocessing as necessary
- [ ] Test with successful and faulty print images