Summary:	GCfilms, movies collection management
Summary(pl):	GCfilms to narzêdzie do zarz±dzania kolekcjami filmów
Name:		gcfilms
Version:	5.1
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://download.gna.org/gcfilms/%{name}-%{version}.tar.gz
# Source0-md5:	d515ecce8b5aa5910d0705273a2058b7
URL:		http://home.gna.org/gcfilms/
Requires:	perl-Gtk2 >= 1.054
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCfilms - Gtk2 Movie Catalog. Application that can be used to manage a
movie collection.

%description -l pl
GCfilms - aplikacja bazuj±ca na Gtk2, a u¿ywana mo¿e byæ do
zarz±dzania kolekcjami filmów.

%prep
%setup -q -n gcfilms

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%__cp -a . "${RPM_BUILD_ROOT-/}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /bin/
%dir /lib/
%dir /lib/gcfilms/
%dir /lib/gcfilms/GCExport/
%dir /lib/gcfilms/GCImport/
%dir /lib/gcfilms/GCLang/
%dir /lib/gcfilms/GCPlugins/
%dir /share/
%dir /share/gcfilms/
/lib/gcfilms/*.pm
/lib/gcfilms/GCExport/*.pm
/lib/gcfilms/GCImport/*.pm
/lib/gcfilms/GCLang/*.pm
/lib/gcfilms/GCPlugins/*.pm
/share/gcfilms/**
%attr(0755,root,root) /bin/gcfilms
