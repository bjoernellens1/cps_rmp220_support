#!/usr/bin/env python

import rospy
from tf.transform_broadcaster import TransformBroadcaster
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

def odom_callback(msg):
    # Create TransformStamped message
    odom_trans = TransformStamped()
    odom_trans.header.stamp = msg.header.stamp
    odom_trans.header.frame_id = msg.header.frame_id
    odom_trans.child_frame_id = msg.child_frame_id

    # Set translation
    odom_trans.transform.translation.x = msg.pose.pose.position.x
    odom_trans.transform.translation.y = msg.pose.pose.position.y
    odom_trans.transform.translation.z = msg.pose.pose.position.z

    # Set rotation
    odom_trans.transform.rotation = msg.pose.pose.orientation

    # Broadcast the transform
    tf_broadcaster.sendTransformMessage(odom_trans)

if __name__ == "__main__":
    rospy.init_node("tf_broadcaster")

    # Create a TransformBroadcaster
    tf_broadcaster = TransformBroadcaster()

    # Subscribe to the /odom topic
    rospy.Subscriber("/odom", Odometry, odom_callback)

    rospy.loginfo("TF broadcaster node is running...")

    # Keep the node running
    rospy.spin()
