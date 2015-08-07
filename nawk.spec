Name:		nawk
Version:	20121220
Release:	3%{?dist}
Summary:	"The one true awk" descended from UNIX V7
Group:		Applications/Text
License:	MIT
URL:		http://www.cs.princeton.edu/~bwk/btl.mirror/index.html
# the author does not provide a way to download specifc versions
Source0:	http://www.cs.princeton.edu/~bwk/btl.mirror/awk.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-%{release}-root-%(%{__id_u} -n)
# remove obsolete macros and change name from awk to nawk 
Patch0:		nawk-manpage.patch
BuildRequires:	bison

%description
This is the version of awk described in "The AWK Programming Language", by Al 
Aho, Brian Kernighan, and Peter Weinberger. (Addison-Wesley, 1988, ISBN 
0-201-07981-X).

%prep
%setup -q -c %{name}
%patch0 -p1 -b .manpage

%build
make CFLAGS="%{optflags}" YACC='bison -y -d' CC="%{__cc}"

%install
rm -rf %{buildroot}

# the nawk binary is saved as a.out so we need to make our directory
# and give the binary a good name
mkdir -p %{buildroot}%{_bindir}
cp a.out %{buildroot}%{_bindir}/nawk

mkdir -p %{buildroot}%{_mandir}/man1/
cp awk.1 %{buildroot}%{_mandir}/man1/nawk.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FIXES README
%{_bindir}/nawk
%{_mandir}/man1/nawk.1.*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121220-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Mark Mckinstry <mmckinst@nexcess.net> - 20121220-1
- upgrade to 20121220
- fix YACC variable to match update makefile

* Tue Nov 15 2011 Mark McKinstry <mmckinst@nexcess.net> 20110810-2
- take out smp in make

* Sun Aug 14 2011 Mark McKinstry <mmckinst@nexcess.net> 20110810-1
- upgrade to 20110810 version

* Wed May 11 2011 Mark McKinstry <mmckinst@nexcess.net> 20110506-1
- upgrade to 20110506 version

* Thu Oct 7 2010 Mark McKinstry <mmckinst@nexcess.net> 20100523-3
- define CC in the make

* Tue Oct 5 2010 Mark McKinstry <mmckinst@nexcess.net> 20100523-2
- don't compress the man page
- remove un-needed optimization from the makefile
- add comments explaining the patches

* Tue Sep 28 2010 Mark McKinstry <mmckinst@nexcess.net> 20100523-1
- initial build 
