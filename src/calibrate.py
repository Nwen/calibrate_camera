#!/usr/bin/env python
import os, sys
import rospy

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import cv2

class Calibrator:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("nao_driver/camera/ir/image_raw",Image,self.callback)

    def callback(self, data):
        try: 
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("SOURCE", cv_image)
        cv2.waitKey(3)

def main(args):
    ic = Calibrator()
    rospy.init_node("image")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)