######################
# Hardcode PLF build
%define build_plf 0
######################

%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif

Summary:	An audio converter
Name:		audiokonverter
Version:	5.9.5
Release:	1%{?extrarelsuffix}
License:	GPLv2
Group:		Sound
URL:		http://www.kde-apps.org/content/show.php?content=12608
Source0:	http://www.kde-apps.org/CONTENT/content-files/%{name}-%{version}.tar.bz2
#Patch0:		audiokonverter-noflac.patch
BuildRequires:	kde4-macros
Requires:	dolphin
Requires:	mplayer
Requires:	flac
Requires:	wavpack
Requires:	id3lib
Requires:	vorbis-tools
%if %{build_plf}
Requires:	lame
Requires:	faac
Requires:	faad2
%endif
BuildArch:	noarch

%description
audiokonverter is a small utility to easily convert from OGG, MP3,
AAC, M4A, FLAC, WMA, RealAudio, Musepack, Wavpack, WAV and movies to
MP3, OGG, M4A, WAV and FLAC in Konqueror by right-clicking on them.

%if %{build_plf}
This package is in restricted because it requires packages that are
in restricted (lame, faac, faad2).
%endif

%prep
%setup -q
%if !%{build_plf}
#patch0 -p0 -b .plf
%endif

%install
mkdir -p %{buildroot}%{_kde_services}/ServiceMenus
install -m 644 *4.desktop %{buildroot}%{_kde_services}/ServiceMenus
mkdir -p %{buildroot}%{_kde_appsdir}/dolphin/servicemenus
install -m 644 *4.desktop %{buildroot}%{_kde_appsdir}/dolphin/servicemenus
mkdir -p %{buildroot}%{_kde_bindir}
install -m 755 anytowav4 audioconvert4 movie2sound4 oggdrop-lx %{buildroot}%{_kde_bindir}

%files
%doc README Changelog
%{_kde_bindir}/*
%{_kde_services}/ServiceMenus/*.desktop
%{_kde_appsdir}/dolphin/servicemenus/*.desktop


