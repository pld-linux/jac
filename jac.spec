Summary:	jac - Just Another Cd player
Summary(pl):	jac - Jeszcze jeden odtwarzacz Cd
Name:		jac
Version:	0.15
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sourceforge/jac/%{name}-%{version}.tar.gz
# Source0-md5:	ff8603ee2150e9f8dd0901f0a5f19d04
URL:		http://jac.sourceforge.net
Buildrequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jac is a command line Cd player that allows you to listen your CDs in
any way, without having a console dedicated to that. Since release
0.11 a small text console was born, for those who like better a
console than a background process. Jac can set the volume (using the
mixer device, if present) and give you detailed information about CD.
Jac can download cd info from CDDB (www.cddb.com) and from CdIndex
(www.cdindex.org) and read CDDB files downloaded from other CD Player.

%description -l pl
Jac jest dzia³aj±cym z lini poleceñ odtwarzaczem CD, który pozwala Ci 
s³uchaæ twoich CD, przez ca³y czas, bez potrzeby utrzymywania 
specjalnej konsoli do tego. Od wersji 0.11 stworzono ma³± tekstow± 
konsole, dla tych co wol± konsle od procesu w tle. Jac potrafi regulowaæ
g³o¶no¶æ (u¿ywaj±c urz±dzenie(sic!) mixer, je¶li jest) oraz podaje ci 
dok³adne informacje o twoim CD. Jac potrafi pobraæ informacje o p³ycie 
z baz CDDB(www.cddb.com) i z CdIndex(www.cdindex.org) oraz czytac CDDB 
pliki pobrane przez innego odtwarzacza CD.

%prep
%setup -q 

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
