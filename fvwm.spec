Summary:	An X Window System based window manager
Summary(es):	Administrador de Ventanas: Feeble (Fine?) Virtual Window Manager
Summary(de):	Feeble (Fine?) Virtual Window Manager 
Summary(fr):	Feeble (Fine ?) Virtual Window Manager
Summary(pt):	Gerenciador de Janelas: Feeble (Fine?) Virtual Window Manager
Summary(tr):	X11 için pencere denetleyicisi
Name:		fvwm
Version:	1.24r
Release:	23
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Requires:	fvwm2-icons
Source0:	ftp://sunsite.unc.edu:/pub/Linux/X11/window-managers/%{name}-%{version}.tar.gz
Source1:	%{name}-system.%{name}rc
Source2:	%{name}.desktop
Source3:	%{name}.RunWM
Source4:	%{name}.wm_style
Patch0:		%{name}-fsstnd.patch
Patch1:		%{name}-imake.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-%{name}man.patch
Patch4:		%{name}-enable-m4.patch
Requires:	wmconfig >= 0.9.9-5
Requires:	m4
Requires:	xinitrc >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
FVWM (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is a window manager for the X Window System.
FVWM was derived from the twm window manager. FVWM is designed to
minimize memory consumption, to provide window frames with a 3D look,
and to provide a simple virtual desktop. FVWM can be configured to
look like Motif.

%description -l es
fvwm es un administrador de ventanas pequeño, rápido y muy flexible.
Puede ser configurado para parecer con Motif, y posee una útil "barra
de botones".

%description -l pl
FVWM (za F mo¿na sobie podstawic co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualnego mened¿era
okien) to mened¿er okien dla systemu X Window. FVWM pochodzi od twm.
Zaprojektowano go tak, by zminimalizowaæ wymagania pamiêciowe,
udostêpniæ ramki okien sprawiaj±ce wra¿enie trójwymiarowych i proste
biurko wirtualne. Mo¿na tez skonfigurowaæ FVWM tak, by mia³ motiffowy
wygl±d.

%description -l pt
fvwm é um gerente de janelas pequeno, rápido e muito flexível. Ele
pode ser configurado para parecer com Motif, e possui uma útil "barra
de botões".

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export PATH=$PATH:%{_bindir}
xmkmf
%{__make} Makefiles
%{__make} \
	BOOTSTRAPCFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	CCOPTIONS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	CXXOPTIONS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	LOCAL_LDFLAGS="%{!?debug:-s}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig/wmstyle,X11/fvwm} \
	$RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fvwm/system.fvwmrc
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sample.fvwmrc/*
%dir %{_sysconfdir}/X11/fvwm
%config %{_sysconfdir}/X11/fvwm/system.fvwmrc
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%dir %{_libdir}/X11/fvwm
%attr(755,root,root) %{_libdir}/X11/fvwm/*
%attr(755,root,root) %{_bindir}/fvwm
%{_datadir}/gnome/wm-properties/fvwm.desktop
%{_mandir}/*/*
