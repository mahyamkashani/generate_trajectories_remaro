from __future__ import print_function
import rospy
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
from rospkg import RosPack
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
from collections import Counter
import roslib
import yaml

class ThrusterFailure:
    def __init__(self):
        self.PKG = 'uuv_tutorial_disturbances'
        self.ROSPACK_INST = RosPack()
        self.ROOT_PATH = self.ROSPACK_INST.get_path(self.PKG)
        self.DEFAULT_BAG = os.path.join(self.ROOT_PATH, 'output/rosbag')
        self.DEFAULT_YAML = os.path.join(self.ROOT_PATH, 'config/')
        self.csv_filename='/bagfile-_rexrov_ground_truth_to_tf_rexrov_pose.csv'
    
    def parse_yaml_file(self):
        with open(self.DEFAULT_YAML+"waypoints.yaml", 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        return data_loaded
            
        
    def load_packages(self):
        os.chdir(self.ROOT_PATH+"/output/recording3")

    def get_desired_points(self, data_loaded):
        waypoints=data_loaded['waypoints']
        points= list(map(lambda d: d['point'], waypoints))
        return points

    def extract_elements(self, lst, coord):
        return list(list(zip(*lst))[coord])



if __name__ == '__main__':
    thruster_failure=ThrusterFailure()
    data=thruster_failure.parse_yaml_file()
    desired_waypoints=thruster_failure.get_desired_points(data)

    X_points=thruster_failure.extract_elements(desired_waypoints, coord=0)
    Y_points=thruster_failure.extract_elements(desired_waypoints, coord=1)
    Z_points=thruster_failure.extract_elements(desired_waypoints, coord=2)


    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(X_points, Y_points, Z_points, 'gray')

    parser = argparse.ArgumentParser(description='Simple simulation runner')

    parser.add_argument(
        '--bag',
        type=str,
        default=thruster_failure.DEFAULT_BAG)

    df = pd.read_csv(thruster_failure.DEFAULT_BAG+ thruster_failure.csv_filename)
    Counter(df).most_common()

    x_pose=df["field.pose.position.x"]
    y_pose=df["field.pose.position.y"]
    z_pose=df["field.pose.position.z"]

    # Data for a three-dimensional line
    xdata = x_pose
    ydata = y_pose
    zdata = z_pose
    ax.plot3D(xdata, ydata, zdata, 'green')
    ax.set_xlabel('$X$', fontsize=20)
    ax.set_ylabel('$Y$', fontsize=20)
    ax.set_zlabel('$Z$', fontsize=20)
    ax.set_title('real positions/ desired main waypoints')
    plt.show()

