Name:           ros-kinetic-pr2-robot
Version:        1.6.29
Release:        0%{?dist}
Summary:        ROS pr2_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-imu-monitor
Requires:       ros-kinetic-pr2-bringup
Requires:       ros-kinetic-pr2-camera-synchronizer
Requires:       ros-kinetic-pr2-computer-monitor
Requires:       ros-kinetic-pr2-controller-configuration
Requires:       ros-kinetic-pr2-ethercat
Requires:       ros-kinetic-pr2-run-stop-auto-restart
BuildRequires:  ros-kinetic-catkin

%description
This stack collects PR2-specific components that are used in bringing up a
robot.

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
* Sun Apr 22 2018 Dave Feil-Seifer <dave@cse.unr.edu> - 1.6.29-0
- Autogenerated by Bloom

* Sat Apr 21 2018 Dave Feil-Seifer <dave@cse.unr.edu> - 1.6.28-0
- Autogenerated by Bloom

* Fri Apr 20 2018 Dave Feil-Seifer <dave@cse.unr.edu> - 1.6.27-0
- Autogenerated by Bloom

