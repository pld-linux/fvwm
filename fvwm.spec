Summary: An X Window System based window manager.
Name: fvwm
Version: 1.24r
Release: 17
Copyright: GPL
Group: User Interface/Desktops
Requires: fvwm2-icons
Source0: sunsite.unc.edu:/pub/Linux/X11/window-managers/fvwm-1.24r.tar.gz
Source1: fvwm-1.24r-system.fvwmrc
Patch0: fvwm-1.24r-fsstnd.patch
Patch1: fvwm-1.24r-imake.patch
Patch2: fvwm-1.24r-security.patch
Patch3: fvwm-1.24r-fvwmman.patch
Buildroot: /var/tmp/fvwm-root

%description
FVWM (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is a window manager for the X Window System. 
FVWM was derived from the twm window manager.  FVWM is designed to
minimize memory consumption, to provide window frames with a 3D look, and
to provide a simple virtual desktop.  FVWM can be configured to look like
Motif.

Install the fvwm package if you'd like to use the FVWM window manager.  If
you install fvwm, you'll also need to install fvwm2-icons.

%prep
%setup
%patch0 -p1 -b .fsstnd
%patch1 -p1 -b .imake
%patch2 -p1 -b .security
%patch3 -p1 -b .fvwmman

%build
export PATH=$PATH:/usr/X11R6/bin
xmkmf
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/fvwm/
install $RPM_SOURCE_DIR/fvwm-1.24r-system.fvwmrc $RPM_BUILD_ROOT/etc/X11/fvwm/system.fvwmrc
strip $RPM_BUILD_ROOT/usr/X11R6/bin/fvwm
strip $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fvwm/* || :

%files
/usr/X11R6/lib/X11/fvwm
/usr/X11R6/bin/fvwm
%dir /etc/X11/fvwm
%config /etc/X11/fvwm/system.fvwmrc
/usr/X11R6/man/*/*
%doc sample.fvwmrc/*

%clean
rm -rf $RPM_BUILD_ROOT
