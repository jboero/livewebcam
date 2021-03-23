Name:           livewebcam
Version:        0.1.0
Release:        1%{dist}
Summary:        LiveWebCam for controlling notifications or lights based on webcam activity.
License:	GPLv3
Source0:	https://github.com/jboero/livewebcam.git
URL: 		https://github.com/jboero/livewebcam
Requires:	python3-wxpython4
%description
LiveWebCam for controlling notifications or lights based on webcam activity.

%global debug_package %{nil}
%prep
	%autosetup -c %{name}-%{version}
%build

%pre


%install
        mkdir -p %{buildroot}%{_bindir}
	mkdir -p %{buildroot}%{_datadir}/livewebcam
	
        cp -p livewebcam %{buildroot}%{_bindir}
        cp -p media/webcam.png %{buildroot}%{_datadir}/livewebcam
%files
        %{_bindir}/livewebcam
        %{_datadir}/livewebcam/webcam.png

%preun
%clean
    rm -rf %{buildroot}

%changelog
