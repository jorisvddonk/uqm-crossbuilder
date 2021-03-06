#! /bin/sh
#
# Builds and installs libsdl for the cross toolchain.
# Sourced from build-uqm-dependencies.chroot

echo "***********************************************************************************************"
echo "--- BEGIN: crossbuild_libsdl ---"

cd /tmp

wget --output-document=/tmp/libsdl.tar.gz ${LIBSDL_URL}

if [ -f libsdl.tar.gz ]; then

	if [ ! -d libsdl ]; then 
		mkdir libsdl
	fi

	tar -zxf libsdl.tar.gz -C libsdl
	cd libsdl/*
	pwd
else
	echo "crossbuild_libsdl failed: Could not get/extract libsdl source"
	exit 1
fi

if [ -f configure ]; then
	./configure\
		--host=${HOST_TRIPLET}\
		--build=i686-linux-gnu\
		--prefix=/usr/${HOST_TRIPLET}
else
	echo "crossbuild_libsdl failed: Could not find ./configure (is libsdl source tarball sane?)"
	exit 1
fi

if [ -f Makefile ]; then
	make clean
	make
	make install
else
	echo "crossbuild_libsdl failed: Could not find Makefile (did ./configure fail?)"
	exit 1
fi

echo "--- END: crossbuild_libsdl ---"
echo "***********************************************************************************************"
