Summary:	GCfilms - movies collection management
Summary(pl):	GCfilms - narzêdzie do zarz±dzania kolekcjami filmów
Name:		gcfilms
Version:	5.2
Release:	0.1
License:	GPL
Group:		Applications/Databases
Source0:	http://download.gna.org/gcfilms/%{name}-%{version}.tar.gz
# Source0-md5:	5b8954427e264998b8078bc0a0b1be6f
URL:		http://home.gna.org/gcfilms/
Requires:	perl-Gtk2 >= 1.054
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCfilms is a Gtk2 Movie Catalog. Application that can be used to
manage a movie collection.

%description -l pl
GCfilms to katalog filmów oparty na Gtk2. Mo¿e byæ u¿ywany do
zarz±dzania kolekcjami filmów.

%prep
%setup -q -n gcfilms

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir},%{_desktopdir}}

install bin/gcfilms $RPM_BUILD_ROOT%{_bindir}
cp -a lib/gcfilms $RPM_BUILD_ROOT%{_libdir}
cp -a share/gcfilms $RPM_BUILD_ROOT%{_datadir}
install share/applications/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

# FIXME
cp -a . $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%lang(fr) %doc CHANGELOG.fr README.fr
%attr(755,root,root) %{_bindir}/gcfilms
%{_libdir}/gcfilms
%{_datadir}/gcfilms
%{_desktopdir}/gcfilms.desktop
