# cs244-verus

dependencies:
$ sudo apt-get install build-essential autoconf libasio-dev libalglib-dev libboost-system-dev libprotobuf-dev protobuf-compiler libtinfo-dev libtool apache2-dev libxcb-present-dev libcogl-pango-dev libtbb-dev apache2 gnuplot-x11

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
  * sudo sysctl -w net.ipv4.ip_forward=1
  * cd cs244-verus
  * ./cleanup_results.sh 
  * python run_experiment.py
