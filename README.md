figleaf
=======

Privacy tools for robotics.

**Dependencies**

* ROS Groovy
* ROS workspaces located at `${HOME}/catkin_ws` and `${HOME}/rosbuild_ws`
* [PR2/pr2_pbd](https://github.com/PR2/pr2_pbd)

**For UW CSE users**

For help setting up ROS, see https://sites.google.com/site/humancenteredrobotics/internal/set-up-to-work-on-pbd-in-014 .

**Install**

Install PBD in ~/rosbuild_ws on the workstation and the robot.
```
git clone git@github.com:PR2/pr2_pbd.git
rosmake
```

Clone this repo to your home folder, ~/figleaf. Run scripts/install.py to create symbolic links in your catkin and rosbuild workspaces. Run `catkin_make` in your catkin workspace.

On the robot, you will need to modify PBD to remove the social gaze. To do this, modify the update method in pr2_pbd_interaction/src/arms.py, leaving just the two arm updates:
```
def update(self):
  '''Periodic update for the two arms.

  This is called regularly by the update loop in interaction.
  '''
  for side in [Side.RIGHT, Side.LEFT]:
    Arms.arms[side].update(self.is_executing())
```

Then, run `rosmake`.

**Running the experiment**
On the robot, run the modified version of PBD: `roslaunch pr2_pbd_interaction pbd_backend.launch`

On the workstation, run `scripts/experiment.sh 123 clean`, where 123 is the user ID, and "clean" is the filter to use. The filters are:
* *clean*: No filters at all
* *blur*: A blurry RGB image
* *box*: A filter which shows no information at all. Users must click "Record object pose" to see bounding boxes of objects on the table.

The experiment script will save rosbag recordings to ~/experiment_data. Modify the script if you want to change it.

To change what topics get logged, run `rosed figleaf_2d experiment.launch` to change the launch file.
