import rclpy
import pyautogui

from rclpy.node import Node

from rcl_interfaces.msg import Log

class RecordStarter(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Log,
            '/rosout',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"\n' % msg.msg)
        # #print (f'I heard: {msg.msg}')
        if msg.msg ==  'rosbag_play is started.' :
            print (f'start capture!!')
            #pyautogui.hotkey('ctrl','shift','R')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            pyautogui.press('r')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('shift')
            
        if msg.msg == 'rosbag_play was finished.' :
            print (f'stop capture!!')
            #pyautogui.hotkey('ctrl','shift','R')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            pyautogui.press('r')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('shift')
            
            
            
def main(args=None):
    rclpy.init(args=args)

    record_starter = RecordStarter()

    rclpy.spin(record_starter)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
