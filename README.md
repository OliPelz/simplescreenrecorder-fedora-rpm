# simplescreenrecorder-fedora-rpm
repo for building Fedora >=26 simplescreenrecorder src rpm's


## Fedora 26
tools needed for building
```
dnf install fedora-packager fedora-review mock

```
pre-actions be taken
```
usermod -a -G mock yourusername
wget https://github.com/MaartenBaert/ssr/archive/master.zip -P /home/olip/rpmbuild/SOURCES/
```

to build spec rpm

