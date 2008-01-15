#
# Conditional build:
%bcond_without	gnome	# disable gnomeprint support
#
Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl.UTF-8):	Widget tekstowy rozszerzający standardowy z GTK+ 2.x
Name:		gtksourceview2
Version:	2.1.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/2.1/gtksourceview-%{version}.tar.bz2
# Source0-md5:	1793b2eaac40208f78757e49ac06e30f
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.8
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.36.1
%{?with_gnome:BuildRequires:	libgnomeprint-devel >= 2.18.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceView is a text widget that extends the standard GTK+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

%description -l pl.UTF-8
GtkSourceView to widget tekstowy rozszerzający standardowy widget
tekstowy GtkTextView z GTK+ 2.x. Ulepsza GtkTextView poprzez
zaimplementowanie podświetlania składni i innych możliwości typowych
dla edytora źródeł.

%package apidocs
Summary:	GtkSourceView API documentation
Summary(pl.UTF-8):	Dokumentacja API GtkSourceView
Group:		Documentation
Requires:	gtk-doc-common
Conflicts:	gtksourceview-apidocs

%description apidocs
GtkSourceView API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkSourceView.

%package devel
Summary:	Header files for gtktextview
Summary(pl.UTF-8):	Pliki nagłówkowe dla gtktextview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0
%{?with_gnome:Requires:	libgnomeprint-devel >= 2.18.0}
Requires:	libxml2-devel >= 1:2.6.30

%description devel
Header files for gtktextview.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gtktextview.

%package static
Summary:	Static gtksourceview library
Summary(pl.UTF-8):	Statyczna biblioteka gtksourceview
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtksourceview library.

%description static -l pl.UTF-8
Statyczna biblioteka gtksourceview.

%prep
%setup -q -n gtksourceview-%{version}

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang gtksourceview-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtksourceview-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so.*.*.*
%{_datadir}/gtksourceview-2.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtksourceview-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so
%{_libdir}/libgtksourceview-2.0.la
%{_includedir}/gtksourceview-2.0
%{_pkgconfigdir}/gtksourceview-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceview-2.0.a
