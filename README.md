# cs244-verus

dependencies:
$ sudo apt-get install build-essential autoconf libasio-dev libalglib-dev libboost-system-dev libprotobuf-dev protobuf-compiler libtinfo-dev libtool apache2-dev libxcb-present-dev libcogl-pango-dev libtbb-dev apache2

Compile Sprout:
http://alfalfa.mit.edu/#code
 * cd alfalfa 
 * ./autogen.sh
 * ./configure --enable-examples
 * make
 
Compile mahimahi
  * cd mahimahi
  * ./autogen.sh
  * ./configure
  * make
  * sudo make install

Compile Verus
  * cd verus
  * ./bootstrap.sh
  * ./configure
  * make

Run Experiments:
  * cd cs244-verus
  * python run_experiment.py
