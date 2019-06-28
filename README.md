# ros_whillpy
Unofficial ROS package for  WHILL Model CK control

## Dependencies
1. [whillpy](https://github.com/ShibataLab/whillpy)
    * Installation steps are provided [here](https://github.com/ShibataLab/whillpy#installation-steps)

whill
```
rosservice list | grep whill
/ros_whillpy/connect
/ros_whillpy/get_loggers
/ros_whillpy/move
/ros_whillpy/power
/ros_whillpy/set_logger_level
```

connect
```
rosservice info /ros_whillpy/connect
Node: /ros_whillpy
URI: rosrpc://172.17.69.112:40843
Type: ros_whillpy/Connect
Args: port
```
## Usage
Please check the `example` folder.
