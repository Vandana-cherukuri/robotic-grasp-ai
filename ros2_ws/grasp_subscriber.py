import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GraspSubscriber(Node):
    def __init__(self):
        super().__init__('grasp_subscriber')
        self.subscription = self.create_subscription(
            String,
            'grasp_cmd',  # Must match your publisher
            self.listener_callback,
            10)
    
    def listener_callback(self, msg):
        self.get_logger().info(f'Received grasp command: {msg.data}')
        # TODO: Trigger robot grasp here

def main(args=None):
    rclpy.init(args=args)
    node = GraspSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
