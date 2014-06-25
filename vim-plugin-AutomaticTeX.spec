# TODO
# - doesn't work perfect, got error on editing tex-files
Summary:	Background compilation, completion, bib serch, toc and other nice features
Name:		vim-plugin-AutomaticTeX
Version:	8.3
Release:	0.3
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.xz
# Source0-md5:	b6ba1dde0d3fb6441ab791c1d1ad2f62
URL:		http://www.vim.org/scripts/script.php?script_id=2945
Requires(post,postun):	/usr/bin/vim
Requires:	vim-rt >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim
%define		_vimfiles	%{_vimdatadir}/vimfiles

%description
Background compilation, completion, bib serch, toc and other nice
features.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_vimdatadir},%{_vimfiles}}
cp -r autoload colors $RPM_BUILD_ROOT%{_vimdatadir}
cp -r doc ftplugin syntax $RPM_BUILD_ROOT%{_vimfiles}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%postun
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%files
%defattr(644,root,root,755)
%{_vimdatadir}/autoload/atplib.vim
%{_vimdatadir}/colors/coots-beauty-256.vim
%{_vimfiles}/doc/*
%{_vimfiles}/ftplugin/ATP_files
%{_vimfiles}/ftplugin/*.vim
%{_vimfiles}/syntax/*atp.vim
