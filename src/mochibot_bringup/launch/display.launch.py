import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

def generate_launch_description():
    desc_share = get_package_share_directory('mochibot_description')
    bringup_share = get_package_share_directory('mochibot_bringup')
    
    urdf_file = os.path.join(desc_share, 'urdf', 'mochibot.urdf.xacro')
    rviz_config_file = os.path.join(desc_share, 'config', 'mochibot.rviz')
    controllers_file = os.path.join(bringup_share, 'config', 'ros2_controllers.yaml')

    is_sim_arg = DeclareLaunchArgument(
        'is_sim',
        default_value='false',
        description='Set to true if running inside Gazebo simulation'
    )
    is_sim = LaunchConfiguration('is_sim')
    use_sim_time = ParameterValue(is_sim, value_type=bool)
    
    robot_description_content = Command(['xacro ', urdf_file, ' is_sim:=', is_sim])
    robot_description = {
        'robot_description': ParameterValue(robot_description_content, value_type=str),
        'use_sim_time': use_sim_time
    }

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description]
    )

    ros2_control_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            robot_description,
            controllers_file,
            {'use_sim_time': use_sim_time}
        ],
        output='screen'
    )

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
    )

    diff_drive_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_drive_controller'],
    )

    delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[diff_drive_controller_spawner],
        )
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        is_sim_arg,
        robot_state_publisher_node,
        ros2_control_node,
        joint_state_broadcaster_spawner,
        delayed_diff_drive_spawner,
        rviz_node
    ])
