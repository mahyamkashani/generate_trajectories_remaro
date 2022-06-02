
import rosbag
from geometry_msgs.msg import Point
import pandas as pd
from rospkg import RosPack
import os


# The bag file should be in the same directory as your terminal
PKG = 'wreckedship_survey'
ROSPACK_INST = RosPack()
ROOT_PATH = ROSPACK_INST.get_path(PKG)
DEFAULT_BAG = os.path.join(ROOT_PATH, 'output/rosbag/')
bag = rosbag.Bag(DEFAULT_BAG+'scenario.bag')
topic = '/rexrov/ground_truth_to_tf_rexrov/pose'
column_names = ['x', 'y', 'z']
df = pd.DataFrame(columns=column_names)


if __name__ == '__main__':
    for topic, msg, t in bag.read_messages(topics=topic):
        # print(topic)
        print(msg)
        x = msg.pose.position.x
        y = msg.pose.position.y
        z = msg.pose.position.z
        clock = msg.header.stamp.secs

        df = df.append(
            {'x': x,
            'y': y,
            'z': z,
            'clock': clock
            },
            ignore_index=True
        )

    df.to_csv('scenario-_rexrov_ground_truth_to_tf_rexrov_pose.csv')
