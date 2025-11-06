from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    ld = LaunchDescription()

    pkg_path = get_package_share_directory('yaml_tf_broadcaster') + "/config/"

    room_file = DeclareLaunchArgument(
        "rooms_location",
        default_value=pkg_path + "olson_rooms.yaml",
        description="rooms location"
    )
    ld.add_action(room_file)

    rooms = Node(
        package="yaml_tf_broadcaster",
        executable="yaml_broadcaster_node",
        name="rooms_launch",
        parameters=[
            {"yaml_file_name": LaunchConfiguration("rooms_location")}
        ]
    )
    ld.add_action(rooms)

    return ld