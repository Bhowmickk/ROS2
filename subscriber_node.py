import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
class NumberSubscribr(Node):
	 def __init__(self):
	 	super().__init__('number_subscribr')
	 	self.subscription= self.create_subscription(Int32,'nos',self.red_ano,10)
	 def red_ano(self,msg):
	 	no=msg.data
	 	if no%2==0:
	 		self.get_logger().info(f"{no} is even")
	 	else:
	 		self.get_logger().info(f"{no} is odd")	
def main(args=None):
	rclpy.init(args=args)
	node=NumberSubscribr()
	rclpy.spin(node)	 	
			 
