Summary:	An X Window System based window manager.
Name:		fvwm
Version:	1.24r
Release:	18
Copyright:	GPL
Group:		User Interface/Desktops
Requires:	fvwm2-icons
Source0:	ftp://sunsite.unc.edu:/pub/Linux/X11/window-managers/fvwm-1.24r.tar.gz
Source1:	fvwm-1.24r-system.fvwmrc
Patch0:		fvwm-1.24r-fsstnd.patch
Patch1:		fvwm-1.24r-imake.patch
Patch2:		fvwm-1.24r-security.patch
Patch3:		fvwm-1.24r-fvwmman.patch
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
FVWM (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is a window manager for the X Window System. 
FVWM was derived from the twm window manager.  FVWM is designed to
minimize memory consumption, to provide window frames with a 3D look, and
to provide a simple virtual desktop.  FVWM can be configured to look like
Motif.

Install the fvwm package if you'd like to use the FVWM window manager.  If
you install fvwm, you'll also need to install fvwm2-icons.

%description -l pl
FVWM (za F mo¿na sobie podstawic co kto woli, lecz VWM pochodzi od pierwszych
liter "Virtual Window Manager", czyli wirtualnego mened¿era okien) to mened¿er
okien dla systemu X Window. FVWM pochodzi od twm. Zaprojektowano go tak,
by zminimalizowaæ wymagania pamiêciowe, udostêpniæ ramki okien sprawiaj±ce 
wra¿enie trójwymiarowych i proste biurko wirtualne. Mo¿na tez skonfigurowaæ
FVWM tak, by mia³ motiffowy wygl±d.

Nale¿y zainstalowaæ pakiet fvwm jesli chce siê uzywaæ mened¿era okien FVWM.
Instaluj±c fvwm nalezy równiez zainstalowaæ pakiet fvwm2-icons.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export PATH=$PATH:/usr/X11R6/bin
xmkmf
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/fvwm/

make install install.man DESTDIR=$RPM_BUILD_ROOT
install $RPM_SOURCE_DIR/fvwm-1.24r-system.fvwmrc $RPM_BUILD_ROOT/etc/X11/fvwm/system.fvwmrc
strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/fvwm \
	$RPM_BUILD_ROOT%{_libdir}/X11/fvwm/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc sample.fvwmrc/*
%dir /etc/X11/fvwm
%config /etc/X11/fvwm/system.fvwmrc
%{_libdir}/X11/fvwm
%{_bindir}/fvwm
%{_mandir}/*/*
