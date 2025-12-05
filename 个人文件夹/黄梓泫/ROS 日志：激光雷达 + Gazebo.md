# Livox mid 360 ladar devops log

#### 1. 目标（Goal Setting）：我们现在要干什么？


流程概览：

连接硬件（Livox Mid-360 雷达） -
安装 Livox SDK 和 ROS2 驱动   -
配置 ROS2 中的 Livox 驱动     -

启动 ROS2 节点，接收点云数据 - 
验证数据流（使用 RViz 或其他工具查看点云数据） -
use pcl to filter pointcloud data:
  - filter, amplify process raw data
  - construct map
  - path finding algorithm, rounting

simlulation using gazebo

sims: issac sim / mojoco / 



##### 2. 核心决定（Decision Log）：我们决定了什么？

tech stack:
use Ubuntu 22.04 ROS2 Humble + gazebo Fortress(https://gazebosim.org/docs/all/ros_installation/)
livox driver use : livox_ros_driver2 (not ros2_driver!!!!!!!)

---

##### 3. 研发过程（Development Log）：我是怎么做到的？

an ros2 module install process (use livox mid360 as example)
go to :(https://github.com/Livox-SDK/livox_ros_driver2)
official command is `git clone https://github.com/Livox-SDK/livox_ros_driver2.git ws_livox/src/livox_ros_driver2`
but don't follow it. the above command copy copy the repo to a wrong directory. you need to copy the repo to `ros2_user_space/src/` 

then follow the repo instruction to install it. remember using ros2 humble instructions!
for the ip addr, config it. for host machine change your eth card, for ladar, the ip addr should be 192.168.1.1xx, xx is last two digit of broadcast code



---

##### 4. 理论知识（Knowledge Base）：我学会了什么？


ros2: distribution system, don't have a main nodes. it exist on your disk, has a server framework:
below is ros2 mainframe structure
before using remember to `source /opt/ros/humble/setup.sh` to locate ros2 executable
/opt/ros/humble/
├── bin/       # 可执行文件
├── include/   # 头文件
├── lib/       # 库文件
├── share/     # 配置文件和文档


and user defined node: you put all your nodes/modules/packages here
it can exist anywhere on your computer.
~/ros2_user_space/
├── src/     # 源代码目录
├── build/   # 编译输出目录
├── install/ # 安装目录
└── log/     # 日志文件

before running node run ` source ~/ros2_ws/ws_livox/install/setup.zsh` to find the executable/launch script in `install`
change above dir into your ros user worksapce path!
usually the ros userspace looks like above structure.
In this article we called `ros2_user_space` as ros2 userspace/workspace

ros2 package directory example:
my_ros2_package/
├── CMakeLists.txt         # CMake 配置文件
├── package.xml            # ROS2 包的元数据
├── src/                   # 源代码目录
│   └── my_node.cpp        # 例如驱动节点的实现
├── include/               # 头文件目录
│   └── my_ros2_package/   # 包含 ROS2 节点相关的头文件
│       └── my_node.hpp
├── msg/                   # 自定义消息定义目录
│   └── PointCloudMsg.msg   # 例如自定义的点云消息
├── srv/                   # 自定义服务定义目录
│   └── StartCapture.srv   # 例如控制雷达采集的服务
├── launch/                # 启动文件目录
│   └── livox_driver_launch.py  # 启动文件，用于启动 ROS2 节点
├── config/                # 配置文件目录
│   └── livox_config.yaml  # 雷达配置文件
└── log/                   # 日志文件目录


a live example: assume we already have serval nodes deployed
~/ros2_ws/
├── build/                    # 编译输出目录，存放 colcon 编译过程中的中间文件
├── install/                  # 存放编译后的可执行文件、库、消息和其他安装文件
│   ├── lib/                  # 可执行文件、库文件目录
│   │   ├── livox_ros2_driver/  # `livox_ros2_driver` 包的可执行文件
│   │   ├── navigation2/         # `navigation2` 包的可执行文件
│   │   └── ...                 # 其他包的可执行文件
│   ├── share/                # 包资源、配置文件等
│   │   ├── livox_ros2_driver/  # `livox_ros2_driver` 包的配置文件
│   │   ├── navigation2/         # `navigation2` 包的资源文件
│   │   └── ...                 # 其他包的资源文件
│   └── ...                    # 其他与包相关的文件
├── log/                      # 存放 ROS2 运行时日志
├── src/                      # 源代码目录，包含你开发的 ROS2 包
│   ├── livox_ros2_driver/     # 你自定义的 `livox_ros2_driver` 包源码
│   │   ├── CMakeLists.txt     # CMake 构建文件
│   │   ├── package.xml        # ROS2 包描述文件
│   │   ├── src/               # 包含源代码的子目录
│   │   │   └── livox_driver.cpp  # 节点源代码文件
│   │   ├── include/           # 头文件目录
│   │   └── launch/            # 启动文件
│   │       └── livox_driver_launch.py  # 启动文件，启动 livox_ros2_driver 节点
│   ├── navigation2/           # `navigation2` 包源码
│   │   ├── CMakeLists.txt
│   │   ├── package.xml
│   │   ├── src/               # `navigation2` 源代码
│   │   ├── include/           # 头文件目录
│   │   └── launch/            # 启动文件目录
│   │       └── navigation_launch.py  # 启动文件
│   ├── rclcpp/                # ROS2 C++ 客户端库源码
│   ├── sensor_msgs/           # `sensor_msgs` 包源码
│   └── ...                    # 其他包的源码
├── install/                  # 安装后可执行文件和依赖包
└── ...                       # 其他与 ROS2 工作空间相关的文件


ros concept: package -> nodes
packages contains serval nodes. nodes are actual robot components/server. 
for example: fire-control is a node, radar is a node, ai module is also a node.

after installing ros2 to your ubuntu, we bootstrap our robot like using terminal + nohop + `ros2 launch xxxnode`

if building a package failed with msg like `cmake fail to find_package pcl`
run `export PCL_DIR=/usr/lib/x86_64-linux-gnu/cmake/pcl` then build again
colcon is a bigger cmake wrapper, under apt system cmake can't find pcl path, use above command
then run `colcon build`
Warning: your terminal must under ros userspace to run above command.



ros2 command list
```
ROS2 常用指令速查：

启动:
  ros2 run <pkg> <exe>
  ros2 launch <pkg> <launch.py>

节点:
  ros2 node list
  ros2 node info <node>

Topic:
  ros2 topic list
  ros2 topic info <topic>
  ros2 topic echo <topic>
  ros2 topic hz <topic>
  ros2 topic bw <topic>

参数:
  ros2 param list
  ros2 param get <node> <param>
  ros2 param set <node> <param> <value>

Service:
  ros2 service list
  ros2 service call <srv> <type>

Action:
  ros2 action list

Package:
  ros2 pkg list
  ros2 pkg executables <pkg>

Bag:
  ros2 bag record <topics>
  ros2 bag play <folder>

诊断:
  ros2 doctor

```


---

##### 5. 链接（References）：资源都在哪里？


ros2 simple intro:
https://docs.ultralytics.com/zh/guides/ros-quickstart/

ros2 structure explain:
https://zhuanlan.zhihu.com/p/670462456



ros2 complete introduction (third party)
https://zhuanlan.zhihu.com/p/639234090
这教程卖课味冲我脸上了都, 但是写的还不错其实
ros2 node explain:
https://zhuanlan.zhihu.com/p/639240328

ros2 official cn docs
http://fishros.org/doc/ros2/humble/Tutorials/Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes.html


gazebo:

short intro to gazebo: https://bbs.huaweicloud.com/blogs/284569

gazebo models:
https://app.gazebosim.org/dashboard

misc:
https://zhuanlan.zhihu.com/p/367660310





---

##### 6. 反思（Reflection/Inspiration）：意外的收获和想法

**模板包含：一个灵活的思考空间**

这个区域是留给那些“**灵光一闪**”的想法。

*   你可能在调试 A 功能时，突然想到 B 功能的一种全新实现方式，但现在还不是实现它的时机。
*   你可能对项目的整体架构产生了新的质疑或更宏大的规划。
*   你甚至可以写下对整个开发过程的感受：哪个环节做得不好，下次要如何改进。

“反思”鼓励你跳出当前任务的局限，进行批判性思考或创新思维捕获。这些想法往往是未来项目或个人成长的起点。

