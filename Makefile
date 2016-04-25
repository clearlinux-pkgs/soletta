PKG_NAME := soletta
URL := https://github.com/solettaproject/soletta/archive/v1_beta19.tar.gz
ARCHIVES := https://github.com/solettaproject/duktape-release/archive/duktape_v1_beta2.tar.gz src/thirdparty/duktape/ https://github.com/01org/tinycbor/archive/v0.2.tar.gz src/thirdparty/tinycbor/ http://downloads.sourceforge.net/tinydtls/tinydtls-0.8.2.tar.gz src/thirdparty/tinydtls/ https://github.com/mavlink/c_library/archive/master.tar.gz src/thirdparty/mavlink/

include ../common/Makefile.common
