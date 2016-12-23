#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : soletta
Version  : 1
Release  : 36
URL      : https://github.com/solettaproject/soletta/archive/v1.tar.gz
Source0  : https://github.com/solettaproject/soletta/archive/v1.tar.gz
Source1  : https://github.com/01org/tinycbor/archive/v0.2.tar.gz
Source2  : https://github.com/mavlink/c_library/archive/master.tar.gz
Source3  : https://github.com/solettaproject/duktape-release/archive/duktape_v1_beta2.tar.gz
Source4  : https://github.com/spark/tinydtls/archive/release-0.8.2.tar.gz
Summary  : A tiny CBOR encoder and decoder library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 MIT Python-2.0
Requires: soletta-bin
Requires: soletta-lib
Requires: soletta-data
BuildRequires : check
BuildRequires : chrpath-bin
BuildRequires : curl-dev
BuildRequires : glib-dev
BuildRequires : graphviz
BuildRequires : gtk+-dev
BuildRequires : icu4c-dev
BuildRequires : jsonschema
BuildRequires : mosquitto-dev
BuildRequires : mosquitto-lib
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(libmicrohttpd)
BuildRequires : python3
BuildRequires : systemd-dev

%description
The tests are regular FBP files with comments that describe what is
expected from them. While they can be executed using regular
sol-fbp-runner, it's more convenient to use 'tools/run-fbp-tests',
from the source root directory.

%package bin
Summary: bin components for the soletta package.
Group: Binaries
Requires: soletta-data

%description bin
bin components for the soletta package.


%package data
Summary: data components for the soletta package.
Group: Data

%description data
data components for the soletta package.


%package dev
Summary: dev components for the soletta package.
Group: Development
Requires: soletta-lib
Requires: soletta-bin
Requires: soletta-data
Provides: soletta-devel

%description dev
dev components for the soletta package.


%package lib
Summary: lib components for the soletta package.
Group: Libraries
Requires: soletta-data

%description lib
lib components for the soletta package.


%prep
tar -xf %{SOURCE3}
tar -xf %{SOURCE1}
tar -xf %{SOURCE4}
tar -xf %{SOURCE2}
cd ..
%setup -q -n soletta-1
mkdir -p %{_topdir}/BUILD/soletta-1/src/thirdparty/duktape/
mv %{_topdir}/BUILD/duktape-release-duktape_v1_beta2/* %{_topdir}/BUILD/soletta-1/src/thirdparty/duktape/
mkdir -p %{_topdir}/BUILD/soletta-1/src/thirdparty/tinycbor/
mv %{_topdir}/BUILD/tinycbor-0.2/* %{_topdir}/BUILD/soletta-1/src/thirdparty/tinycbor/
mkdir -p %{_topdir}/BUILD/soletta-1/src/thirdparty/tinydtls/
mv %{_topdir}/BUILD/tinydtls-release-0.8.2/* %{_topdir}/BUILD/soletta-1/src/thirdparty/tinydtls/
mkdir -p %{_topdir}/BUILD/soletta-1/src/thirdparty/mavlink/
mv %{_topdir}/BUILD/c_library_v1-master/* %{_topdir}/BUILD/soletta-1/src/thirdparty/mavlink/

%build
make V=1  %{?_smp_mflags} -h; export LIBDIR=%{_libdir}/; make V=1 alldefconfig; make V=1

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sol-aio
/usr/bin/sol-fbp-generator
/usr/bin/sol-fbp-runner
/usr/bin/sol-fbp-to-dot
/usr/bin/sol-flow-node-type-aliases-gen.py
/usr/bin/sol-flow-node-type-gen.py
/usr/bin/sol-flow-node-type-validate.py
/usr/bin/sol-gpio
/usr/bin/sol-oic-gen.py

%files data
%defattr(-,root,root,-)
/usr/share/gdb/auto-load/libsoletta.so.1.0.0-gdb.py
/usr/share/gdb/auto-load/libsoletta.so.1.0.0-gdb.pyc
/usr/share/gdb/auto-load/libsoletta.so.1.0.0-gdb.pyo
/usr/share/soletta/boards/50-default.json
/usr/share/soletta/flow/aliases/50-default.json
/usr/share/soletta/flow/descriptions/aio.json
/usr/share/soletta/flow/descriptions/am2315.json
/usr/share/soletta/flow/descriptions/app.json
/usr/share/soletta/flow/descriptions/boolean.json
/usr/share/soletta/flow/descriptions/byte.json
/usr/share/soletta/flow/descriptions/calamari.json
/usr/share/soletta/flow/descriptions/color.json
/usr/share/soletta/flow/descriptions/compass.json
/usr/share/soletta/flow/descriptions/console.json
/usr/share/soletta/flow/descriptions/constant.json
/usr/share/soletta/flow/descriptions/converter.json
/usr/share/soletta/flow/descriptions/evdev.json
/usr/share/soletta/flow/descriptions/file.json
/usr/share/soletta/flow/descriptions/filter-repeated.json
/usr/share/soletta/flow/descriptions/float.json
/usr/share/soletta/flow/descriptions/flower-power.json
/usr/share/soletta/flow/descriptions/form.json
/usr/share/soletta/flow/descriptions/format.json
/usr/share/soletta/flow/descriptions/gpio.json
/usr/share/soletta/flow/descriptions/grove.json
/usr/share/soletta/flow/descriptions/http-client.json
/usr/share/soletta/flow/descriptions/http-server.json
/usr/share/soletta/flow/descriptions/iio.json
/usr/share/soletta/flow/descriptions/int.json
/usr/share/soletta/flow/descriptions/jhd1313m1.json
/usr/share/soletta/flow/descriptions/json.json
/usr/share/soletta/flow/descriptions/keyboard.json
/usr/share/soletta/flow/descriptions/led-7seg.json
/usr/share/soletta/flow/descriptions/led-strip.json
/usr/share/soletta/flow/descriptions/location.json
/usr/share/soletta/flow/descriptions/mqtt.json
/usr/share/soletta/flow/descriptions/network.json
/usr/share/soletta/flow/descriptions/oauth.json
/usr/share/soletta/flow/descriptions/oic.json
/usr/share/soletta/flow/descriptions/persistence.json
/usr/share/soletta/flow/descriptions/piezo-speaker.json
/usr/share/soletta/flow/descriptions/platform.json
/usr/share/soletta/flow/descriptions/power-supply.json
/usr/share/soletta/flow/descriptions/process.json
/usr/share/soletta/flow/descriptions/pwm.json
/usr/share/soletta/flow/descriptions/random.json
/usr/share/soletta/flow/descriptions/regexp.json
/usr/share/soletta/flow/descriptions/servo-motor.json
/usr/share/soletta/flow/descriptions/string.json
/usr/share/soletta/flow/descriptions/switcher.json
/usr/share/soletta/flow/descriptions/temperature.json
/usr/share/soletta/flow/descriptions/test.json
/usr/share/soletta/flow/descriptions/thingspeak.json
/usr/share/soletta/flow/descriptions/timer.json
/usr/share/soletta/flow/descriptions/timestamp.json
/usr/share/soletta/flow/descriptions/trigonometry.json
/usr/share/soletta/flow/descriptions/twitter.json
/usr/share/soletta/flow/descriptions/udev.json
/usr/share/soletta/flow/descriptions/unix-socket.json
/usr/share/soletta/flow/descriptions/update.json
/usr/share/soletta/flow/descriptions/wallclock.json
/usr/share/soletta/flow/schemas/node-type-genspec.schema
/usr/share/soletta/web-inspector/web-inspector.css
/usr/share/soletta/web-inspector/web-inspector.html
/usr/share/soletta/web-inspector/web-inspector.js

%files dev
%defattr(-,root,root,-)
/usr/include/soletta/sol-aio.h
/usr/include/soletta/sol-arena.h
/usr/include/soletta/sol-atomic.h
/usr/include/soletta/sol-bluetooth.h
/usr/include/soletta/sol-buffer.h
/usr/include/soletta/sol-certificate.h
/usr/include/soletta/sol-coap.h
/usr/include/soletta/sol-common-buildopts.h
/usr/include/soletta/sol-efivarfs-storage.h
/usr/include/soletta/sol-file-reader.h
/usr/include/soletta/sol-flow-builder.h
/usr/include/soletta/sol-flow-buildopts.h
/usr/include/soletta/sol-flow-inspector.h
/usr/include/soletta/sol-flow-metatype.h
/usr/include/soletta/sol-flow-packet.h
/usr/include/soletta/sol-flow-parser.h
/usr/include/soletta/sol-flow-resolver.h
/usr/include/soletta/sol-flow-simple-c-type.h
/usr/include/soletta/sol-flow-single.h
/usr/include/soletta/sol-flow-static.h
/usr/include/soletta/sol-flow.h
/usr/include/soletta/sol-flow/aio.h
/usr/include/soletta/sol-flow/am2315.h
/usr/include/soletta/sol-flow/app.h
/usr/include/soletta/sol-flow/boolean.h
/usr/include/soletta/sol-flow/byte.h
/usr/include/soletta/sol-flow/calamari.h
/usr/include/soletta/sol-flow/color.h
/usr/include/soletta/sol-flow/compass.h
/usr/include/soletta/sol-flow/console.h
/usr/include/soletta/sol-flow/constant.h
/usr/include/soletta/sol-flow/converter.h
/usr/include/soletta/sol-flow/evdev.h
/usr/include/soletta/sol-flow/file.h
/usr/include/soletta/sol-flow/filter-repeated.h
/usr/include/soletta/sol-flow/float.h
/usr/include/soletta/sol-flow/flower-power.h
/usr/include/soletta/sol-flow/form.h
/usr/include/soletta/sol-flow/format.h
/usr/include/soletta/sol-flow/gpio.h
/usr/include/soletta/sol-flow/grove.h
/usr/include/soletta/sol-flow/http-client.h
/usr/include/soletta/sol-flow/http-server.h
/usr/include/soletta/sol-flow/iio.h
/usr/include/soletta/sol-flow/int.h
/usr/include/soletta/sol-flow/jhd1313m1.h
/usr/include/soletta/sol-flow/json.h
/usr/include/soletta/sol-flow/keyboard.h
/usr/include/soletta/sol-flow/led-7seg.h
/usr/include/soletta/sol-flow/led-strip.h
/usr/include/soletta/sol-flow/location.h
/usr/include/soletta/sol-flow/mqtt.h
/usr/include/soletta/sol-flow/network.h
/usr/include/soletta/sol-flow/oauth.h
/usr/include/soletta/sol-flow/oic.h
/usr/include/soletta/sol-flow/persistence.h
/usr/include/soletta/sol-flow/piezo-speaker.h
/usr/include/soletta/sol-flow/platform.h
/usr/include/soletta/sol-flow/power-supply.h
/usr/include/soletta/sol-flow/process.h
/usr/include/soletta/sol-flow/pwm.h
/usr/include/soletta/sol-flow/random.h
/usr/include/soletta/sol-flow/regexp.h
/usr/include/soletta/sol-flow/servo-motor.h
/usr/include/soletta/sol-flow/string.h
/usr/include/soletta/sol-flow/switcher.h
/usr/include/soletta/sol-flow/temperature.h
/usr/include/soletta/sol-flow/test.h
/usr/include/soletta/sol-flow/thingspeak.h
/usr/include/soletta/sol-flow/timer.h
/usr/include/soletta/sol-flow/timestamp.h
/usr/include/soletta/sol-flow/trigonometry.h
/usr/include/soletta/sol-flow/twitter.h
/usr/include/soletta/sol-flow/udev.h
/usr/include/soletta/sol-flow/unix-socket.h
/usr/include/soletta/sol-flow/update.h
/usr/include/soletta/sol-flow/wallclock.h
/usr/include/soletta/sol-flower-power.h
/usr/include/soletta/sol-fs-storage.h
/usr/include/soletta/sol-gatt.h
/usr/include/soletta/sol-glib-integration.h
/usr/include/soletta/sol-gpio.h
/usr/include/soletta/sol-http-client.h
/usr/include/soletta/sol-http-server.h
/usr/include/soletta/sol-http.h
/usr/include/soletta/sol-i2c.h
/usr/include/soletta/sol-iio.h
/usr/include/soletta/sol-json.h
/usr/include/soletta/sol-list.h
/usr/include/soletta/sol-log.h
/usr/include/soletta/sol-lwm2m.h
/usr/include/soletta/sol-macros.h
/usr/include/soletta/sol-mainloop.h
/usr/include/soletta/sol-mavlink.h
/usr/include/soletta/sol-memdesc.h
/usr/include/soletta/sol-memmap-storage.h
/usr/include/soletta/sol-message-digest.h
/usr/include/soletta/sol-mqtt.h
/usr/include/soletta/sol-netctl.h
/usr/include/soletta/sol-network.h
/usr/include/soletta/sol-oic-client.h
/usr/include/soletta/sol-oic-server.h
/usr/include/soletta/sol-oic.h
/usr/include/soletta/sol-pin-mux-modules.h
/usr/include/soletta/sol-pin-mux.h
/usr/include/soletta/sol-platform-linux.h
/usr/include/soletta/sol-platform.h
/usr/include/soletta/sol-power-supply.h
/usr/include/soletta/sol-pwm.h
/usr/include/soletta/sol-reentrant.h
/usr/include/soletta/sol-socket.h
/usr/include/soletta/sol-spi.h
/usr/include/soletta/sol-str-slice.h
/usr/include/soletta/sol-str-table.h
/usr/include/soletta/sol-types.h
/usr/include/soletta/sol-uart.h
/usr/include/soletta/sol-update-modules.h
/usr/include/soletta/sol-update.h
/usr/include/soletta/sol-util-file.h
/usr/include/soletta/sol-util.h
/usr/include/soletta/sol-vector.h
/usr/include/soletta/sol-worker-thread.h
/usr/include/soletta/soletta.h
/usr/lib/*.so
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib/*.so.*
/usr/lib/soletta/modules/flow-metatype/http-composed-client.so
/usr/lib/soletta/modules/flow-metatype/http-composed-server.so
/usr/lib/soletta/modules/flow-metatype/js.so
/usr/lib/soletta/modules/flow/am2315.so
/usr/lib/soletta/modules/flow/calamari.so
/usr/lib/soletta/modules/flow/compass.so
/usr/lib/soletta/modules/flow/evdev.so
/usr/lib/soletta/modules/flow/file.so
/usr/lib/soletta/modules/flow/flower-power.so
/usr/lib/soletta/modules/flow/form.so
/usr/lib/soletta/modules/flow/format.so
/usr/lib/soletta/modules/flow/grove.so
/usr/lib/soletta/modules/flow/http-client.so
/usr/lib/soletta/modules/flow/http-server.so
/usr/lib/soletta/modules/flow/iio.so
/usr/lib/soletta/modules/flow/jhd1313m1.so
/usr/lib/soletta/modules/flow/json.so
/usr/lib/soletta/modules/flow/keyboard.so
/usr/lib/soletta/modules/flow/led-strip.so
/usr/lib/soletta/modules/flow/location.so
/usr/lib/soletta/modules/flow/mqtt.so
/usr/lib/soletta/modules/flow/network.so
/usr/lib/soletta/modules/flow/oauth.so
/usr/lib/soletta/modules/flow/oic.so
/usr/lib/soletta/modules/flow/persistence.so
/usr/lib/soletta/modules/flow/piezo-speaker.so
/usr/lib/soletta/modules/flow/power-supply.so
/usr/lib/soletta/modules/flow/process.so
/usr/lib/soletta/modules/flow/servo-motor.so
/usr/lib/soletta/modules/flow/test.so
/usr/lib/soletta/modules/flow/thingspeak.so
/usr/lib/soletta/modules/flow/twitter.so
/usr/lib/soletta/modules/flow/udev.so
/usr/lib/soletta/modules/flow/unix-socket.so
/usr/lib/soletta/modules/flow/update.so
/usr/lib/soletta/modules/pin-mux/intel-edison-rev-c.so
/usr/lib/soletta/modules/pin-mux/intel-galileo-rev-d.so
/usr/lib/soletta/modules/pin-mux/intel-galileo-rev-g.so
/usr/lib64/*.so.*
/usr/lib64/soletta/modules/flow-metatype/http-composed-client.so
/usr/lib64/soletta/modules/flow-metatype/http-composed-server.so
/usr/lib64/soletta/modules/flow-metatype/js.so
/usr/lib64/soletta/modules/flow/am2315.so
/usr/lib64/soletta/modules/flow/calamari.so
/usr/lib64/soletta/modules/flow/compass.so
/usr/lib64/soletta/modules/flow/evdev.so
/usr/lib64/soletta/modules/flow/file.so
/usr/lib64/soletta/modules/flow/flower-power.so
/usr/lib64/soletta/modules/flow/form.so
/usr/lib64/soletta/modules/flow/format.so
/usr/lib64/soletta/modules/flow/grove.so
/usr/lib64/soletta/modules/flow/http-client.so
/usr/lib64/soletta/modules/flow/http-server.so
/usr/lib64/soletta/modules/flow/iio.so
/usr/lib64/soletta/modules/flow/jhd1313m1.so
/usr/lib64/soletta/modules/flow/json.so
/usr/lib64/soletta/modules/flow/keyboard.so
/usr/lib64/soletta/modules/flow/led-strip.so
/usr/lib64/soletta/modules/flow/location.so
/usr/lib64/soletta/modules/flow/mqtt.so
/usr/lib64/soletta/modules/flow/network.so
/usr/lib64/soletta/modules/flow/oauth.so
/usr/lib64/soletta/modules/flow/oic.so
/usr/lib64/soletta/modules/flow/persistence.so
/usr/lib64/soletta/modules/flow/piezo-speaker.so
/usr/lib64/soletta/modules/flow/power-supply.so
/usr/lib64/soletta/modules/flow/process.so
/usr/lib64/soletta/modules/flow/servo-motor.so
/usr/lib64/soletta/modules/flow/test.so
/usr/lib64/soletta/modules/flow/thingspeak.so
/usr/lib64/soletta/modules/flow/twitter.so
/usr/lib64/soletta/modules/flow/udev.so
/usr/lib64/soletta/modules/flow/unix-socket.so
/usr/lib64/soletta/modules/flow/update.so
/usr/lib64/soletta/modules/pin-mux/intel-edison-rev-c.so
/usr/lib64/soletta/modules/pin-mux/intel-galileo-rev-d.so
/usr/lib64/soletta/modules/pin-mux/intel-galileo-rev-g.so
