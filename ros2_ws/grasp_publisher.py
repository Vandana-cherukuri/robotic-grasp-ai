import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GraspPublisher(Node):
    def __init__(self):
        super().__init__('grasp_publisher')
        self.publisher_ = self.create_publisher(String, 'grasp_cmd', 10)
        self.timer = self.create_timer(2.0, self.publish_command)
        self.get_logger().info("Grasp Publisher started...")

    def publish_command(self):
        msg = String()
        msg.data = "GRASP_OBJECT"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")

def main():
    rclpy.init()
    node = GraspPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
