Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl.UTF-8):	Widget tekstowy rozszerzający standardowy z GTK+ 2.x
Name:		gtksourceview2
Version:	2.10.5
Release:	8
License:	GPL v2+ and LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/2.10/gtksourceview-%{version}.tar.bz2
# Source0-md5:	1219ad1694df136f126507466aeb41aa
Patch0:		build.patch
URL:		https://wiki.gnome.org/Projects/GtkSourceView
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.10.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires:	glib2 >= 1:2.24
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
BuildArch:	noarch

%description apidocs
GtkSourceView API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkSourceView.

%package devel
Summary:	Header files for GtkSourceView
Summary(pl.UTF-8):	Pliki nagłówkowe dla GtkSourceView
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libxml2-devel >= 1:2.6.31

%description devel
Header files for GtkSourceView.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla GtkSourceView.

%package static
Summary:	Static GtkSourceView library
Summary(pl.UTF-8):	Statyczna biblioteka GtkSourceView
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GtkSourceView library.

%description static -l pl.UTF-8
Statyczna biblioteka GtkSourceView.

%prep
%setup -q -n gtksourceview-%{version}
%patch -P0 -p1

%build
%{__autopoint}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtksourceview-2.0.la

%find_lang gtksourceview-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtksourceview-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtksourceview-2.0.so.0
%{_datadir}/gtksourceview-2.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtksourceview-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so
%{_includedir}/gtksourceview-2.0
%{_pkgconfigdir}/gtksourceview-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceview-2.0.a
