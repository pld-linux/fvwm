Summary:	An X Window System based window manager
Name:		fvwm
Version:	1.24r
Release:	18
License:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Requires:	fvwm2-icons
Source0:	ftp://sunsite.unc.edu:/pub/Linux/X11/window-managers/%{name}-%{version}.tar.gz
Source1:	fvwm-1.24r-system.fvwmrc
Patch0:		fvwm-1.24r-fsstnd.patch
Patch1:		fvwm-1.24r-imake.patch
Patch2:		fvwm-1.24r-security.patch
Patch3:		fvwm-1.24r-fvwmman.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
FVWM (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is a window manager for the X Window System.
FVWM was derived from the twm window manager. FVWM is designed to
minimize memory consumption, to provide window frames with a 3D look,
and to provide a simple virtual desktop. FVWM can be configured to
look like Motif.

%description -l pl
FVWM (za F mo¿na sobie podstawic co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualnego mened¿era
okien) to mened¿er okien dla systemu X Window. FVWM pochodzi od twm.
Zaprojektowano go tak, by zminimalizowaæ wymagania pamiêciowe,
udostêpniæ ramki okien sprawiaj±ce wra¿enie trójwymiarowych i proste
biurko wirtualne. Mo¿na tez skonfigurowaæ FVWM tak, by mia³ motiffowy
wygl±d.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export PATH=$PATH:%{_bindir}
xmkmf
%{__make} Makefiles
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/fvwm/

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT
install $RPM_SOURCE_DIR/fvwm-1.24r-system.fvwmrc $RPM_BUILD_ROOT%{_sysconfdir}/X11/fvwm/system.fvwmrc
strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/fvwm \
	$RPM_BUILD_ROOT%{_libdir}/X11/fvwm/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sample.fvwmrc/*
%dir %{_sysconfdir}/X11/fvwm
%config %{_sysconfdir}/X11/fvwm/system.fvwmrc
%{_libdir}/X11/fvwm
%attr(755,root,root) %{_bindir}/fvwm
%{_mandir}/*/*
