Summary:	An X Window System based window manager
Summary(es.UTF-8):   Administrador de Ventanas: Feeble (Fine?) Virtual Window Manager
Summary(de.UTF-8):   Feeble (Fine?) Virtual Window Manager
Summary(fr.UTF-8):   Feeble (Fine ?) Virtual Window Manager
Summary(pl.UTF-8):   Zarządca okien dla X Window System
Summary(pt.UTF-8):   Gerenciador de Janelas: Feeble (Fine?) Virtual Window Manager
Summary(tr.UTF-8):   X11 için pencere denetleyicisi
Name:		fvwm
Version:	1.24r
Release:	28
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-1/%{name}-%{version}.tar.gz
# Source0-md5:	875733e77e285566197f4b50746aefc6
Source1:	%{name}-system.%{name}rc
Source2:	%{name}.desktop
Source3:	%{name}.RunWM
Source5:	%{name}-xsession.desktop
Patch0:		%{name}-fsstnd.patch
Patch1:		%{name}-imake.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-%{name}man.patch
Patch4:		%{name}-enable-m4.patch
Patch5:		%{name}-maxpopups.patch
Patch6:		%{name}-man.patch
URL:		http://www.fvwm.org/
BuildRequires:	XFree86
BuildRequires:	XFree86-devel
BuildRequires:	imake
Requires(post):	vfmg >= 0.9.95
Requires:	fvwm2-icons
Requires:	m4
Requires:	vfmg >= 0.9.18-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_sysconfdir	/etc/X11/fvwm

%description
FVWM (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is a window manager for the X Window System.
FVWM was derived from the twm window manager. FVWM is designed to
minimize memory consumption, to provide window frames with a 3D look,
and to provide a simple virtual desktop. FVWM can be configured to
look like Motif.

%description -l es.UTF-8
fvwm es un administrador de ventanas pequeño, rápido y muy flexible.
Puede ser configurado para parecer con Motif, y posee una útil "barra
de botones".

%description -l pl.UTF-8
FVWM (za F można sobie podstawić co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualny zarządca
okien) to zarządca okien dla systemu X Window. FVWM pochodzi od twm.
Zaprojektowano go tak, by zminimalizować wymagania pamięciowe,
udostępnić ramki okien sprawiające wrażenie trójwymiarowych i proste
biurko wirtualne. Można tez skonfigurować FVWM tak, by miał wygląd
podobny do Motifa.

%description -l pt.UTF-8
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
%patch5 -p1
%patch6 -p1

%build
xmkmf
%{__make} Makefiles
%{__make} \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	LOCAL_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_sysconfdir},/etc/sysconfig/wmstyle} \
	$RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_libdir}/fvwm1 \
	MANDIR=%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/system.fvwmrc
install %{SOURCE2} $RPM_BUILD_ROOT%{_wmpropsdir}

install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

install -d $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_libdir}/fvwm1/fvwm $RPM_BUILD_ROOT%{_bindir}/fvwm1

mv $RPM_BUILD_ROOT%{_mandir}/man1/fvwm{,1}.1x
touch $RPM_BUILD_ROOT%{_sysconfdir}/fvwm.menu

%clean
rm -rf $RPM_BUILD_ROOT

%post
# generate initial menu
[ -f /etc/sysconfig/vfmg ] && . /etc/sysconfig/vfmg
[ "$FVWM" = yes -o "$FVWM" = 1 -o ! -f /etc/X11/fvwm/fvwm.menu ] && \
	vfmg fvwm >/etc/X11/fvwm/fvwm.menu 2>/dev/null ||:

%files
%defattr(644,root,root,755)
%doc sample.fvwmrc/*
%dir %{_sysconfdir}
%config %{_sysconfdir}/system.fvwmrc
%ghost %{_sysconfdir}/fvwm.menu
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
%dir %{_libdir}/fvwm1
%attr(755,root,root) %{_libdir}/fvwm1/*
%attr(755,root,root) %{_bindir}/fvwm1
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/fvwm.desktop
%{_mandir}/*/*
