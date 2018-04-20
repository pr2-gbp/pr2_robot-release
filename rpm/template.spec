Name:           ros-kinetic-pr2-bringup
Version:        1.6.27
Release:        0%{?dist}
Summary:        ROS pr2_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-ethercat-trigger-controllers
Requires:       ros-kinetic-joint-trajectory-action
Requires:       ros-kinetic-joy
Requires:       ros-kinetic-microstrain-3dmgx2-imu
Requires:       ros-kinetic-ocean-battery-driver
Requires:       ros-kinetic-power-monitor
Requires:       ros-kinetic-pr2-calibration-controllers
Requires:       ros-kinetic-pr2-camera-synchronizer
Requires:       ros-kinetic-pr2-computer-monitor
Requires:       ros-kinetic-pr2-controller-configuration
Requires:       ros-kinetic-pr2-controller-manager
Requires:       ros-kinetic-pr2-dashboard-aggregator
Requires:       ros-kinetic-pr2-description
Requires:       ros-kinetic-pr2-ethercat
Requires:       ros-kinetic-pr2-gripper-action
Requires:       ros-kinetic-pr2-head-action
Requires:       ros-kinetic-pr2-machine
Requires:       ros-kinetic-pr2-power-board
Requires:       ros-kinetic-pr2-run-stop-auto-restart
Requires:       ros-kinetic-prosilica-camera
Requires:       ros-kinetic-robot-mechanism-controllers
Requires:       ros-kinetic-robot-pose-ekf
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-single-joint-position-action
Requires:       ros-kinetic-sound-play
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-stereo-image-proc
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-urg-node
Requires:       ros-kinetic-wge100-camera
Requires:       ros-kinetic-wifi-ddwrt
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rostest

%description
Launch files and scripts needed to bring a PR2 up into a running state.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Apr 20 2018 Dave Feil-Seifer <dave@cse.unr.edu> - 1.6.27-0
- Autogenerated by Bloom

