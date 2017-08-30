# to test building the rpm we use mock with 
```
# get all mock configs
ls /etc/mock
mock -r <configfile> --shell

```

# install rpmfusion in mock to test
```
cp /etc/mock/fedora-26-x86_64.cfg /tmp/fedora-26-x86_64-rpmfusion.cfg.tmp
head -n -1 /tmp/fedora-26-x86_64-rpmfusion.cfg.tmp > /etc/mock/fedora-26-x86_64-rpmfusion.cfg

echo '
[rpmfusion-nonfree]
name=RPM Fusion for Fedora $releasever - Nonfree
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=14d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=14d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
"""
' >> /etc/mock/fedora-26-x86_64-rpmfusion.cfg

```

# run mock
```
mock -r fedora-26-x86_64-rpmfusion --shell
```

# install deps for simplescreenrecord
```
dnf install ffmpeg-devel qt4-devel \
alsa-lib-devel pulseaudio-libs-devel jack-audio-connection-kit-devel \
gcc make gcc-c++ glibc-devel.i686 libgcc.i686 libX11-devel libX11-devel.i686 \
libXext-devel libXext-devel.i686 libXfixes-devel libXfixes-devel.i686 mesa-libGL-devel \
mesa-libGL-devel.i686 mesa-libGLU-devel mesa-libGLU-devel.i686 \
mesa-libGLU-devel.x86_64 qt4
```

# install and compile ssr
# latest master
```
git clone https://github.com/MaartenBaert/ssr.git
```

# or specific version
```
git clone 0.3.8 https://github.com/MaartenBaert/ssr.git
```

```
cd ssr
change stuff in simple-build-and-install : compile as root, delete sudo lines
./simple-build-and-install
```



