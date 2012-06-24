Summary:	jac - just Another CD player
Summary(pl):	jac - jeszcze jeden odtwarzacz CD
Name:		jac
Version:	0.15
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/jac/%{name}-%{version}.tar.gz
# Source0-md5:	ff8603ee2150e9f8dd0901f0a5f19d04
Patch0:		%{name}-am.patch
URL:		http://jac.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jac is a command line CD player that allows you to listen your CDs in
any way, without having a console dedicated to that. Since release
0.11 a small text console was born, for those who like better a
console than a background process. Jac can set the volume (using the
mixer device, if present) and give you detailed information about CD.
Jac can download cd info from CDDB (www.cddb.com) and from CdIndex
(www.cdindex.org) and read CDDB files downloaded from other CD Player.

%description -l pl
Jac jest dzia�aj�cym z linii polece� odtwarzaczem CD, kt�ry pozwala
s�ucha� p�yt CD przez ca�y czas, bez potrzeby utrzymywania do tego
specjalnej konsoli. Od wersji 0.11 stworzono ma�� tekstow� konsol� dla
tych, co wol� konsol� od procesu w tle. Jac potrafi regulowa� g�o�no��
(u�ywaj�c urz�dzenia(sic!) mixer, je�li jest) oraz podaje dok�adne
informacje o danym CD. Jac potrafi pobra� informacje o p�ycie z baz
CDDB (www.cddb.com) i z CdIndex (www.cdindex.org) oraz czyta� pliki
CDDB pobrane przez innego odtwarzacza CD.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
%{_mandir}/man1/%{name}.1*
