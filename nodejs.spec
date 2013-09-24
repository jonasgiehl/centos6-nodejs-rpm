Name:          nodejs
Version:       @@VERSION@@
Release:       @@RELEASE@@
Summary:       Node.js programs
Group:         Applications/Internet
License:       Copyright Joyent, Inc. and other Node contributors.
URL:           http://nodejs.org

Source0:       http://nodejs.org/dist/v$(version)/node-v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python >= 2.4, openssl-devel

Provides: nodejs
Obsoletes: nodejs

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model. This allows Node.js to get excellent performance based on
the architectures of many Internet applications.

%prep
%setup -q -n node-v%{version}

%build
export JOBS=@@JOBS@@
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README.md

/usr/bin/node
/usr/bin/npm
/usr/share/man/man1/node.1.gz
/usr/lib/node_modules
/usr/lib/dtrace/node.d

%changelog
* Thu Apr 12 2012 Vibol Hou <vibol@hou.cc> 0.6.15-1
- RPM using upstream v0.6.15

* Thu Apr 14 2011 Chris Abernethy <cabernet@chrisabernethy.com> 0.4.6-1
- Initial rpm using upstream v0.4.6
