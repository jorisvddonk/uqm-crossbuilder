#! /bin/sh
#
# Builds and installs libiconv for the cross toolchain.
# Sourced from build-uqm-dependencies.chroot

echo "***********************************************************************************************"
echo "--- BEGIN: crossbuild_libiconv ---"

cd /tmp

wget --output-document=/tmp/libiconv.tar.gz ${LIBICONV_URL}

if [ -f libiconv.tar.gz ]; then

	if [ ! -d libiconv ]; then 
		mkdir libiconv
	fi

	tar -zxf libiconv.tar.gz -C libiconv
	cd libiconv/libiconv*
else
	echo "crossbuild_libiconv failed: Could not get/extract libiconv source"
	exit 1
fi

if [ -f configure ]; then
	./configure\
		--host=${HOST_TRIPLET}\
		--build=i686-linux-gnu\
		--prefix=/usr/${HOST_TRIPLET}
else
	echo "crossbuild_libiconv failed: Could not find ./configure (is libiconv source tarball sane?)"
	exit 1
fi

if [ -f Makefile ]; then
	make clean
	make
	make install
else
	echo "crossbuild_libiconv failed: Could not find Makefile (did ./configure fail?)"
	exit 1
fi

echo "--- END: crossbuild_libiconv ---"
echo "***********************************************************************************************"
