nawk for z/OS
=============
The source for nawk was initially downloaded from 
ftp://ftp.pbone.net/mirror/download.fedora.redhat.com/pub/fedora/linux/releases/22/Everything/source/SRPMS/n/nawk-20121220-3.fc21.src.rpm
I processed it by doing:
    rpm2cpio <nawk-20121220-3.fc21.src.rpm | cpio -dium
This contained the file awk.tar.gz, which I unwound and then deleted, leaving only the source.
That was then make the initial commit.
