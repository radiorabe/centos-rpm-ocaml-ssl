Name:     ocaml-ssl

Version:  0.5.2
Release:  1
Summary:  OCaml bindings for the libssl
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-ssl
Source0:  https://github.com/savonet/ocaml-ssl/releases/download/0.5.2/ocaml-ssl-0.5.2.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes
BuildRequires: ocaml-camlidl
BuildRequires: openssl-devel

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/ssl/META
/usr/lib64/ocaml/ssl/ssl.a
/usr/lib64/ocaml/ssl/ssl.cma
/usr/lib64/ocaml/ssl/ssl.cmi
/usr/lib64/ocaml/ssl/ssl.cmx
/usr/lib64/ocaml/ssl/ssl.cmxa
/usr/lib64/ocaml/ssl/ssl.mli

%description
OCaml bindings for libssl.

%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-ssl.spec
