#!/bin/sh

# install AICSHP just to make sure this is done uncomment if the rest of the AICSHP github is not installed
# git clone https://github.com/VigilantBag/AICSHP.git 

# install honeyd & dependencies
sudo apt-get install libevent-dev libdumbnet-dev libpcap-dev libpcre3-dev libedit-dev bison flex libtool automake python2.7 automake build-essential zlibc zlib1g-dev

git clone https://github.com/Nevsor/Honeyd.git --branch fix-python-version-bug
cd Honeyd/
bash ./autogen.sh
bash ./configure
make 
sudo make install
cd ../

# install farpd & fix the script paths so they match the absolute paths of file system
sudo apt install farpd

# install ICSpot
#git clone https://github.com/VigilantBag/ICSpot.git

echo ""
echo "Change ICSpot/honeyd.conf to the actual filepath pointing to the files in the scripts folder (lines 20-22)."
echo "After that, Run the second install script."
echo ""
