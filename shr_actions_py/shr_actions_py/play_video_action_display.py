import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from shr_msgs.action import PlayVideoRequest  # Replace with your actual action import
from std_msgs.msg import String
import time
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup


class SimpleZmqSenderAction(Node):
    def __init__(self):
        super().__init__('video_action')
        self.display_cb_group = MutuallyExclusiveCallbackGroup()

        self.display_pub = self.create_publisher(String, 'display_tx', 10)
        self.display_sub = self.create_subscription(String, 'display_rx', self.display_callback, 10, callback_group=self.display_cb_group)

        self._action_server = ActionServer(
            self,
            PlayVideoRequest,
            'play_video',
            execute_callback=self.execute_callback,  # sync version
        )


    def display_callback(self, msg):
       
        # print(f"[Received] {msg.data}")  # print the message content
        if "RES:video_finished" in msg.data:
            self.video_finished = True
            print("callback self.video_finished", self.video_finished)
            self.get_logger().info("Video finished received!")


    def execute_callback(self, goal_handle):
        video_path = goal_handle.request.file_name
        self.get_logger().info(f"Received video goal: {video_path}")
        
        # Optional feedback
        feedback = PlayVideoRequest.Feedback()
        feedback.running = True
        goal_handle.publish_feedback(feedback)

        # Send video path 
        self.display_pub.publish(String(data=video_path))

        ## set to false whenever a video is recieved
        self.video_finished = False
        # Wait for 3 minutes or when video returns finished
        # self.get_logger().info("⏳ Waiting for seconds before returning success...")
        # time.sleep(55)

        ## todo check what to do when video fails, if the rx takes that then we are all good.
        # Wait for up to 5 minutes for video to finish, check every second
        start_time = self.get_clock().now()
        timeout = rclpy.time.Duration(seconds=3*60)  # 3 minutes
        while not self.video_finished:
            # print("In while")
            # print(" self.video_finished", self.video_finished)

            # rclpy.spin_once(self, timeout_sec=1.0)  # allow callbacks to run
            time.sleep(1)
            if self.get_clock().now() - start_time > timeout:
                self.get_logger().warn(" Video did not finish in 5 minutes, aborting")
                goal_handle.abort()
                result = PlayVideoRequest.Result()
                result.status = "video failed or timeout"
                return result

        
        self.get_logger().info("Video finish, success")

        goal_handle.succeed()
        result = PlayVideoRequest.Result()
        result.status = "video sent"
        return result


def main(args=None):
    rclpy.init(args=args)
    node =  SimpleZmqSenderAction()

    executor = MultiThreadedExecutor()
    executor.add_node(node)
    # node = SimpleZmqSenderAction()

    # try:
    #     rclpy.spin(node)
    # except KeyboardInterrupt:
    #     node.get_logger().info(" Shutting down...")
    # finally:
    #     node.destroy_node()
    #     rclpy.shutdown()
    
    try:
        
        node.get_logger().info('Beginning server, shut down with CTRL-C')
        executor.spin()
    except (KeyboardInterrupt):
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
