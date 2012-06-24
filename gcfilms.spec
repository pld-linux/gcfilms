%include	/usr/lib/rpm/macros.perl
Summary:	GCfilms - movies collection management
Summary(pl):	GCfilms - narz�dzie do zarz�dzania kolekcjami film�w
Name:		gcfilms
Version:	5.3
Release:	0.14
License:	GPL
Group:		Applications/Databases
Source0:	http://download.gna.org/gcfilms/%{name}-%{version}.tar.gz
# Source0-md5:	58743009cb2d5a821f33205efa8d4346
Patch0:		%{name}-path.patch
URL:		http://home.gna.org/gcfilms/
Requires:	perl-Gtk2 >= 1.054
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# provided by this package itself.
%define		_noautoreq	'perl(GC.*)'

%description
GCfilms is a Gtk2 Movie Catalog. Application that can be used to
manage a movie collection.

%description -l pl
GCfilms to katalog film�w oparty na Gtk2. Mo�e by� u�ywany do
zarz�dzania kolekcjami film�w.

%prep
%setup -q -n gcfilms
%patch0 -p1 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/lib,%{_desktopdir}}

install bin/gcfilms $RPM_BUILD_ROOT%{_bindir}
cp -a lib/gcfilms/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
cp -a share/gcfilms $RPM_BUILD_ROOT%{_datadir}
install share/applications/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%lang(fr) %doc CHANGELOG.fr README.fr
%attr(755,root,root) %{_bindir}/gcfilms
%{_datadir}/gcfilms
%{_desktopdir}/gcfilms.desktop
