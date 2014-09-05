No-Pendrive
===========
This script enables user to share files between users . It uses python SimpleHTTPServer to transfer files between users . 

Literature Survey: A large number of P2P file sharing programs  are increasingly popular. Shareaza, Bit Torrent, Ares
, BearShare, Kazaa, Morpheus, Limewire, eDonkey, eMute,WinMx  are  some of them. Each program is characterized by either
large setup size, slow speed, too much CPU usage, embedded advertising, grind to hault, wasted data downloaded, 
incompatibility.  Also, some of them run only on one or two platforms, do not allow surfing the Internet
or otherwise utilize the network  when files are uploaded or downloaded. 


File sharing using Python SimpleHTTPServer does not require any receiver side software.
Only a web browser is required at the receiver side which is readily available. The script for file sharing coded 
in Python 2.7 is stored at the sender side. Since Python is platform independent, this script is also platform 
independent. The sender only requires a fair knowledge of directory structure to send the files. The script generates
a URL which depends on the local IP address of the sender. If Internet is available at the time of file sharing,
URL shortening services like tinyURL can be used which generates a small and readable URL and if not then the 
URL generated by the script is conveyed  to the receiver side by any suitable means.

NoPendrive Script Usage 
=======================
Assume that we would like to share the directory /home/somedir and sender IP address is 192.168.10.2
Open up a terminal and type: $ nopendrive
The module requires port number and the directory name to share  as input.
The module will then  generate some URL such as  http://192.168.10.2:8000.  Convey this URL to the receiver
to receive the file sent. 