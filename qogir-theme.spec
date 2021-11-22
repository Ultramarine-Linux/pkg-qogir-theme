%undefine _disable_source_fetch

Name:           qogir-theme
Version:        git020821
Release:        1%{?dist}
Summary:        Qogir is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell.

License:        GPLv3
URL:            https://github.com/vinceliuice/Qogir-theme/
Source0:        ${url}/archive/refs/tags/2021-08-02.tar.gz#/Qogir-theme-2021-08-02.tar.gz

BuildRequires:  sassc
Requires:       gtk-murrine-engine gtk2-engines

%description
Qogir is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Cinnamon Pantheon, XFCE, Mate, etc.

%prep
%autosetup -n Qogir-theme-2021-08-02


#%build
#./parse-sass.sh



%install
./parse-sass.sh
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -d %{buildroot}%{_datadir}/themes

%files
%license COPYING
%doc README.md

%{_datadir}/themes/Qogir/
%{_datadir}/themes/Qogir-light/
%{_datadir}/themes/Qogir-dark/
%{_datadir}/themes/Qogir-win/
%{_datadir}/themes/Qogir-win-light/
%{_datadir}/themes/Qogir-win-dark/
%{_datadir}/themes/Qogir-manjaro/
%{_datadir}/themes/Qogir-manjaro-light/
%{_datadir}/themes/Qogir-manjaro-dark/
%{_datadir}/themes/Qogir-manjaro-win/
%{_datadir}/themes/Qogir-manjaro-win-light/
%{_datadir}/themes/Qogir-manjaro-win-dark/
%{_datadir}/themes/Qogir-ubuntu/
%{_datadir}/themes/Qogir-ubuntu-light/
%{_datadir}/themes/Qogir-ubuntu-dark/
%{_datadir}/themes/Qogir-ubuntu-win/
%{_datadir}/themes/Qogir-ubuntu-win-light/
%{_datadir}/themes/Qogir-ubuntu-win-dark/

%changelog
* Sat Nov 13 2021 korewaChino <cappy@cappuchino.xyz>
- initial release
