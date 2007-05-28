#
Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl.UTF-8):	Widget tekstowy rozszerzający standardowy z GTK+ 2.x
Name:		gtksourceview2
Version:	1.90.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/1.90/gtksourceview-%{version}.tar.bz2
# Source0-md5:	982a67ff00dd33742c2a77aec780a9ce
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
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

%description apidocs
GtkSourceView API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkSourceView.

%package devel
Summary:	Header files for gtktextview
Summary(pl.UTF-8):	Pliki nagłówkowe dla gtktextview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.9
%{?with_gnome:Requires:	libgnomeprint-devel >= 2.17.92}
Requires:	libxml2-devel >= 1:2.6.27

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
%{_gtkdocdir}/gtksourceview

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so
%{_libdir}/libgtksourceview-2.0.la
%{_includedir}/gtksourceview-2.0
%{_pkgconfigdir}/gtksourceview-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceview-2.0.a
