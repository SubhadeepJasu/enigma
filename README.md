<div align="center">
  <div align="center">
    <img src="data/icons/128/com.github.subhadeepjasu.enigma.svg" width="64">
  </div>
  <h1 align="center">Enigma</h1>
  ![screenshot](screenshots/screenshot_home.png)
  <div align="center">A classic 3-rotor Enigma Machine emulator</div>
</div>

<br/>

## Get it on elementary OS Appcenter
TBD
<!-- [![Get it on AppCenter](https://appcenter.elementary.io/badge.svg)](https://appcenter.elementary.io/com.github.subhadeepjasu.pebbles) -->

## Install from source
You can install Enigma by compiling it from source, here's a list of required dependencies:
 - `gtk+-3.0>=3.18`
 - `granite>=5.3.0`
 - `glib-2.0`
 - `gobject-2.0`
 - `meson`
 - `python3`


Clone repository and change directory
```
git clone https://github.com/SubhadeepJasu/enigma.git
cd enigma
```
Compile, install and start Enigma on your system
```
meson _build --prefix=/usr
cd _build
sudo ninja install
com.github.subhadeepjasu.enigma
```

<sup>**Based on**: Elementary Python Template by Mirko Brombin</sup>
<sup>**License**: GNU GPLv3</sup>