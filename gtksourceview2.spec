Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl.UTF-8):	Widget tekstowy rozszerzający standardowy z GTK+ 2.x
Name:		gtksourceview2
Version:	2.10.1
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/2.10/gtksourceview-%{version}.tar.bz2
# Source0-md5:	1ed3eae620ec95b82baae9de6600af22
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.10.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
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
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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

%find_lang gtksourceview-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtksourceview-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtksourceview-2.0.so.0
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
