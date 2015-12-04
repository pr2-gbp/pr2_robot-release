Name:           ros-indigo-pr2-ethercat
Version:        1.6.10
Release:        1%{?dist}
Summary:        ROS pr2_ethercat package

Group:          Development/Libraries
License:        BSD
URL:            http://pr.willowgarage.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-ethercat-hardware
Requires:       ros-indigo-pr2-controller-manager
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-ethercat-hardware
BuildRequires:  ros-indigo-pr2-controller-manager
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-srvs

%description
Main loop that runs the robot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Dec 04 2015 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-1
- Autogenerated by Bloom

* Wed Sep 16 2015 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-0
- Autogenerated by Bloom

* Tue Sep 01 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.9-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.7-0
- Autogenerated by Bloom

