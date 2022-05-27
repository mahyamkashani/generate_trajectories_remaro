from __future__ import print_function
from hashlib import _BlakeHash
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
from pandas_profiling import ProfileReport
import roslib
import yaml

class ThrusterFailure:
    def __init__(self):
        self.PKG = 'uuv_tutorial_disturbances'
        self.ROSPACK_INST = RosPack()
        self.ROOT_PATH = self.ROSPACK_INST.get_path(self.PKG)
        self.DEFAULT_BAG = os.path.join(self.ROOT_PATH, 'output/recording3')
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
        # print(points)
        return points


if __name__ == '__main__':
    thruster_failure=ThrusterFailure()
    data=thruster_failure.parse_yaml_file()
    desired_waypoints=thruster_failure.get_desired_points(data)

    fig1 = plt.figure()
    ax1 = plt.axes(projection='3d')
    ax1.plot3D(desired_waypoints[0], desired_waypoints[1], desired_waypoints[2], 'green')
    ax1.set_xlabel('$X$', fontsize=20)
    ax1.set_ylabel('$Y$', fontsize=20)
    ax1.set_zlabel('$Z$', fontsize=20)
    ax1.set_title('desired way points')


    parser = argparse.ArgumentParser(description='Simple simulation runner')

    initial_waypoints=thruster_failure.parse_yaml_file()

    parser.add_argument(
        '--bag',
        type=str,
        default=thruster_failure.DEFAULT_BAG)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # df = pd.read_csv(DEFAULT_BAG+'/bagfile-_rexrov_pose_gt_ned.csv')
    df = pd.read_csv(thruster_failure.DEFAULT_BAG+ thruster_failure.csv_filename)
    Counter(df).most_common()

    # profile.to_file("analysis_task.html")
    x_pose=df["field.pose.position.x"]
    y_pose=df["field.pose.position.y"]
    z_pose=df["field.pose.position.z"]

    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    xdata = x_pose
    ydata = y_pose
    zdata = z_pose
    ax.plot3D(xdata, ydata, zdata, 'green')
    ax.set_xlabel('$X$', fontsize=20)
    ax.set_ylabel('$Y$', fontsize=20)
    ax.set_zlabel('$Z$', fontsize=20)
    ax.set_title('real positions')
    plt.show()


    # with open(DEFAULT_BAG+'/bagfile-_rexrov_pose_gt_ned.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     line_count = 0
    #     cs
    #     for row in csv_reader:
    #         if line_count == 0:
    #             # print(f'Column names are {", ".join(row)}')
    #             line_count += 1
    #         else:
    #             # print(f'\t time is: {row[0]} :: positions and orientations: {row[5:10]}.')
    #             print(f'\t pose x: {row[5]} :: pose y: {row[6]}.')

    #             line_count += 1
    #             ax = plt.axes(projection='3d')

    #             # Data for a three-dimensional line
    #             xdata = row[5]
    #             ydata = row[6]
    #             zdata = row[7]
    #             # ax.plot3D(xdata, ydata, zdata, 'gray')
    #             plt.show()

                
    #     print(f'Processed {line_count} lines.')

