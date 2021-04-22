<div align="center">
  <div align="center">
    <img src="data/icons/128/com.github.subhadeepjasu.enigma.svg" width="128">
  </div>
  <h1 align="center">Enigma</h1>
  <div align="center">
    <img src="screenshots/screenshot.png" width="500">
  </div>
  <div align="center">A classic 3-rotor Enigma Machine emulator</div>
</div>

[![Build Status](https://travis-ci.com/SubhadeepJasu/enigma.svg?branch=main)](https://travis-ci.com/SubhadeepJasu/enigma)

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

<sup>**Based on**: [Elementary Python Template](https://github.com/mirkobrombin/ElementaryPython) by Mirko Brombin</sup>
<br>
<sup>**License**: GNU GPLv3</sup>
