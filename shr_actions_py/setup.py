from setuptools import setup

package_name = 'shr_actions_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pac48',
    maintainer_email='pac48@wildcats.unh.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
    'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
                            'read_script_action = shr_actions_py.read_script_action:main',
                            'make_call_action = shr_actions_py.make_call_action:main',
                            'send_text_action = shr_actions_py.send_text_action:main',
                            'play_audio_action = shr_actions_py.play_audio_action:main',
                            'open_image_action = shr_actions_py.open_image_action:main',
                            'deep_fake_action = shr_actions_py.deep_fake_action:main',
                            'client__ = shr_actions_py.client:main',
                            'client_dock = shr_actions_py.client_dock:main',
                            'undocking = shr_actions_py.undocking_action:main',
                            'localize = shr_actions_py.localize:main',
                            'cancel_docking = shr_actions_py.cancel_goal_client:main',
                            'action_display_interface = shr_actions_py.action_display_interface:main', ## combined previously
			                'play_video_action = shr_actions_py.play_video_action_display:main'
                            ],
    },
)
