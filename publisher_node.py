import rclpy #import the required dependencies 
from rclpy.node import Node
import random
from std_msgs.msg import Int32
class NumberPublishr(Node):	
    def __init__(self):
        super().__init__('number_publishr') #initializing the node
        self.publisher_ = self.create_publisher(Int32, 'nos', 10) # self.publisher = self.create_publisher(msg_type,topic,queue size)
        self.timer = self.create_timer(1, self.write_ano) #sets a timer of 1 second for publishing each number.
    def write_ano(self):
    	msg=Int32()# Creating a field of signed integer of 32 bit to specify to ros the type of data the message is.
    	msg.data=random.randint(1,100) #generates a random integer  between 1 and 100 ,assigns the value to the field msg.
    	self.publisher_.publish(msg) #sends the message to the topic nos.
    	self.get_logger().info(f"Publishing {msg.data}") #printing what no is being published at the moment. 
def main(args=None): #defines the entry point of the whole node
	rclpy.init(args=args) #Starts up the Ros2 system for the whole publishing process
	node= NumberPublishr()
	rclpy.spin(node) #keeps the node alive for some time.
	   		    
