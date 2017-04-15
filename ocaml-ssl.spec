Name:     ocaml-ssl


Version:  0.5.3
Release:  1
Summary:  OCaml bindings for the libssl
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-ssl
Source0:  https://github.com/savonet/ocaml-ssl/releases/download/%{version}/ocaml-ssl-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes
BuildRequires: ocaml-camlidl
BuildRequires: openssl-devel

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix}
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/ssl/
/usr/lib64/ocaml/stublibs/dllssl*

%description
OCaml bindings for libssl.

%changelog
* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch>
- Bump to version 0.5.4 and proper build

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-ssl.spec
