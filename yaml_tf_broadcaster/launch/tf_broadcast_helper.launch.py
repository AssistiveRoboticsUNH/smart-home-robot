from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    ld = LaunchDescription()

    pkg_path = get_package_share_directory('yaml_tf_broadcaster') + "/config/"
 
    helper_file = DeclareLaunchArgument(
        "helper_location",
        default_value=pkg_path + "helpers.yaml",
        description="helper location"
    )

    ld.add_action(helper_file)

    helpers = Node(
        package="yaml_tf_broadcaster",
        executable="yaml_broadcaster_node",
        name="helper_launch_ll",
        parameters=[
            {"yaml_file_name": LaunchConfiguration("helper_location")}
        ]
    )
    ld.add_action(helpers)

    return ld
