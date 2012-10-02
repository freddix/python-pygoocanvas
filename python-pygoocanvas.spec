Summary:	Python bindings for GooCanvas library
Name:		python-pygoocanvas
Version:	0.14.1
Release:	4
License:	LGPL v2
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygoocanvas/0.14/pygoocanvas-%{version}.tar.bz2
# Source0-md5:	e0e7b694af2f81a78b0838555d150252
URL:		http://live.gnome.org/PyGoocanvas
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	goocanvas-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygobject-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GooCanvas library.

%package apidocs
Summary:	pygoocanvas API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygoocanvas API documentation.

%prep
%setup -qn pygoocanvas-%{version}

sed -i -e 's|codegen.py|codegen.pyc|g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLdir=%{_gtkdocdir}/pygoocanvas

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{py_sitedir}/goocanvasmodule.so

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pygoocanvas

