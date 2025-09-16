import zmq
import rclpy
from shr_actions_py.play_audio_action import PlayAudioActionServer
from shr_actions_py.read_script_action import ReadScriptActionServer
from convros_bot.question_test_action import SpeechRecognitionActionServer  # ✅ Import the updated class
from shr_actions_py.play_video_action_display import SimpleZmqSenderAction
import os

def main():
    # Initialize ZeroMQ context and shared socket
    try:
        ip_list = os.popen('hostname -I').read().strip().split()
        ip_address = next(ip for ip in ip_list if ip.startswith('192.'))
    except StopIteration:
        # Fallback default IP if no suitable IP found
        ip_address = "10.21.194.221"
        print("⚠️ Could not detect 192.* IP. Falling back to default:", ip_address)
    else:
        print("✅ ZMQ LOCAL IP Address detected:", ip_address)

    # Initialize ROS 2
    rclpy.init()
   
    # Create action servers with shared ZeroMQ socket
    play_audio_action_server = PlayAudioActionServer()
    read_script_action_server = ReadScriptActionServer()
    question_response_action_server = SpeechRecognitionActionServer()  # ✅ Added Question Response Server
    video_play = SimpleZmqSenderAction()

  
    # Spin the action servers
    while True:
        rclpy.spin_once(play_audio_action_server, timeout_sec=0.1)
        rclpy.spin_once(read_script_action_server, timeout_sec=0.1)
        rclpy.spin_once(question_response_action_server, timeout_sec=0.1)  # ✅ Added to the loop
        rclpy.spin_once(video_play, timeout_sec=0.1)
