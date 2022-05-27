# `Generating various trajectories by using disturbance via UUV Simulator tutorials`

In order to have various plans for an UUV (Unmanned Underwater Vehicle), we utilize multiple trajectories inspired from UUV Simulator.

 **Environment Configuration:**
> OS: Ubuntu 20.04, Ros: Ros1, Noetic, Gazebo: 11

# Installation

Once the `ros-<distro>-desktop-full` package for the desired distribution is installed, the uuv_simulator can be installed as:
- Create a ros workspace like [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
- Clone the `Field-Robotics-Lab_uuv_simulator` repository [here](https://github.com/Field-Robotics-Lab/uuv_simulator) in your ros workspace. Then, build your workspace.
- Do not forget: `source ~/<your workspace>/devel/setup.bash`

In case you have issue in installation you can refer to the installation pages of uuv simulator [instructions page](https://uuvsimulator.github.io/installation/)

> **Gazebo world models**

- Existing in the uuv_gazebo_worlds [(e.g. Hercule WreckedShip)](https://github.com/Field-Robotics-Lab/uuv_simulator/tree/master/uuv_gazebo_worlds)
- Remaro worlds [here](https://github.com/remaro-network/remaro_worlds)

> **Vehicle models**
- [`eca_a9`](https://github.com/uuvsimulator/eca_a9)
- [`lauv_gazebo`](https://github.com/uuvsimulator/lauv_gazebo)
- [`rexrov2`](https://github.com/uuvsimulator/rexrov2)


> **Controllers**

- For AUVs
    - Geometric tracking PD controller
- For ROVs
    - Thruster manager with computation of the thruster allocation matrix based on the thruster frames available in `/tf`
    - Non-model-based sliding mode controller ([`García-Valdovinos el al., 2014`](https://journals.sagepub.com/doi/full/10.5772/56810) and [`Salgado-Jiménez et al., 2011`](http://cdn.intechopen.com/pdfs/15221.pdf))
    - PD controller with restoration forces compensation 
- Teleoperation nodes for AUVs and ROVs
 

# Purpose of the project

This software is a part of [REMARO](http://remaro.eu/) for European Union's EU Framework Programme for Research and Innovation Horizon 2020 under Grant Agreement No 956200 and we inspired by UUV simulator developed for the EU ECSEL Project 662107 [SWARMs](http://swarms.eu/).


