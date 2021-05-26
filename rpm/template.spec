%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-pr2-bringup
Version:        1.6.32
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS pr2_bringup package

License:        BSD
URL:            http://ros.org/wiki/pr2_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-diagnostic-aggregator
Requires:       ros-noetic-ethercat-trigger-controllers
Requires:       ros-noetic-imu-monitor
Requires:       ros-noetic-joint-trajectory-action
Requires:       ros-noetic-joy
Requires:       ros-noetic-microstrain-3dmgx2-imu
Requires:       ros-noetic-ocean-battery-driver
Requires:       ros-noetic-power-monitor
Requires:       ros-noetic-pr2-calibration-controllers
Requires:       ros-noetic-pr2-camera-synchronizer
Requires:       ros-noetic-pr2-computer-monitor
Requires:       ros-noetic-pr2-controller-configuration
Requires:       ros-noetic-pr2-controller-manager
Requires:       ros-noetic-pr2-dashboard-aggregator
Requires:       ros-noetic-pr2-description
Requires:       ros-noetic-pr2-ethercat
Requires:       ros-noetic-pr2-gripper-action
Requires:       ros-noetic-pr2-head-action
Requires:       ros-noetic-pr2-machine
Requires:       ros-noetic-pr2-power-board
Requires:       ros-noetic-pr2-run-stop-auto-restart
Requires:       ros-noetic-prosilica-camera
Requires:       ros-noetic-robot-mechanism-controllers
Requires:       ros-noetic-robot-pose-ekf
Requires:       ros-noetic-robot-state-publisher
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-single-joint-position-action
Requires:       ros-noetic-sound-play
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-stereo-image-proc
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-urg-node
Requires:       ros-noetic-wge100-camera
Requires:       ros-noetic-wifi-ddwrt
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roslaunch
BuildRequires:  ros-noetic-rostest
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Launch files and scripts needed to bring a PR2 up into a running state.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed May 26 2021 Dave Feil-Seifer <dave@cse.unr.edu> - 1.6.32-1
- Autogenerated by Bloom

