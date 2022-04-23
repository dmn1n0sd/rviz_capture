from setuptools import setup

package_name = 'rviz_capture'

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
    author='',
    author_email='',
    maintainer='',
    maintainer_email='',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: ',
        'License :: OSI Approved :: ',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal publishers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'record_starter = rviz_capture.record_starter:main',
            #'script = rviz_capture.script',
        ],
    },
)