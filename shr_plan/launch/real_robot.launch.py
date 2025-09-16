from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch.conditions import IfCondition


def generate_launch_description():

    ld = LaunchDescription()

    smartthings_node_plug = Node(
        package='smartthings_ros',
        executable='smartplug_node',
        output='screen'
    )

    protocol_time_node = Node(
        package='shr_plan',
        executable='time_publisher_node',
        output='screen'
    )

    docking_data_manager = Node(
        package='shr_docking',
        executable='docking_data_manager',
        output='screen'
    )

    discord_logger = Node(
        package='simple_logger',
        executable='simple_logger_discord',
        output='screen'
    )

    apriltags_realsense_loc = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            get_package_share_directory('apriltag_ros'), 'launch', 'tag_realsense_loc.launch.py']))
    )


    tf_broadcast = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            get_package_share_directory('yaml_tf_broadcaster'), 'launch', 'tf_broadcast.launch.py']))
    )


    charger = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            get_package_share_directory('charger_description'), 'launch', 'view_charger.launch.py']))
    )


    display_node = Node(
        package='shr_display',
        executable='display_node',
        output='screen'
    )

    ld.add_action(charger)
    ld.add_action(apriltags_realsense_loc)
    ld.add_action(tf_broadcast)
    ld.add_action(smartthings_node_plug)
    ld.add_action(protocol_time_node)
    ld.add_action(docking_data_manager)
    ld.add_action(discord_logger)
    ld.add_action(display_node)

    return ld
