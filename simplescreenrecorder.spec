Name:           simplescreenrecorder
Version:        0.3.8
Release:        1%{?dist}
License:        GPLv3
Summary:        A feature-rich screen recorder that supports X11 and OpenGL
Url:            http://www.maartenbaert.be/simplescreenrecorder
Group:          Applications/Multimedia


BuildRequires: ffmpeg-devel
BuildRequires: qt4-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: glibc-devel.i686
BuildRequires: libgcc.i686
BuildRequires: libX11-devel
BuildRequires: libX11-devel.i686
BuildRequires: libXext-devel
BuildRequires: libXext-devel.i686
BuildRequires: libXfixes-devel
BuildRequires: libXfixes-devel.i686
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGL-devel.i686
BuildRequires: mesa-libGLU-devel
BuildRequires: mesa-libGLU-devel.i686
BuildRequires: mesa-libGLU-devel.x86_64
BuildRequires: qt4
Buildroot:      %{_builddir}
Source:         %{_specdir}/master.zip


%description
SimpleScreenRecorder is a program to record programs and games.

The original goal was to create a program that was just really simple to
use, the result is actually a pretty powerful program. It's 'simple' in
the sense that it's easier to use than ffmpeg/avconv or VLC, because it
has a straightforward user interface.

Features:
 * Graphical user interface (Qt-based).
 * Faster than VLC and ffmpeg/avconv.
 * Records the entire screen or part of it, or records OpenGL applications
   directly (similar to Fraps on Windows).
 * Synchronizes audio and video properly (a common issue with VLC and
   ffmpeg/avconv).
 * Reduces the video frame rate if your computer is too slow (rather than
   using up all your RAM like VLC does).
 * Fully multithreaded: small delays in any of the components will never
   block the other components, resulting is smoother video and better
   performance on computers with multiple processors.
 * Pause and resume recording at any time (either by clicking a button or by
   pressing a hotkey).
 * Shows statistics during recording (file size, bit rate, total recording
   time, actual frame rate, ...).
 * Can show a preview during recording, so you don't waste time recording
   something only to figure out afterwards that some setting was wrong.
 * Uses libav/ffmpeg libraries for encoding, so it supports many different
   codecs and file formats (adding more is trivial).
 * Sensible default settings: no need to change anything if you don't want to.
 * Tooltips for almost everything: no need to read the documentation to find
   out what something does.

%prep

%build

%install

%files

%changelog
