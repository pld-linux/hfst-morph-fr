Summary:	HFST morphological analysis transducer for French language
Summary(pl.UTF-8):	Automat HFST do analizy morfologicznej dla języka francuskiego
Name:		hfst-morph-fr
# or 20110316?
Version:	0
Release:	1
License:	Morphalou (http://www.cnrtl.fr/lexiques/morphalou/)
Group:		Applications/Text
# source is hfst-french.tar.gz, but it doesn't contain scripts
Source0:	http://downloads.sourceforge.net/hfst/hfst-french-installable.tar.gz
# Source0-md5:	a86f155b1cd4fe42228d3ac4aafecefe
Patch0:		%{name}-DESTDIR.patch
URL:		http://hfst.sourceforge.net/
Requires:	hfst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a French morphological transducer for HFST. It comes from
Morphalou project: <http://www.cnrtl.fr/lexiques/morphalou/>.

%description -l pl.UTF-8
Ten pakiet zawiera automat dla HFST do analizy morfologicznej języka
francuskiego. Pochodzi z projektu Morphalou:
<http://www.cnrtl.fr/lexiques/morphalou/>.

%prep
%setup -q -n hfst-french-installable
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/french-analyze.sh
%attr(755,root,root) %{_bindir}/french-generate.sh
%{_datadir}/hfst/fr
