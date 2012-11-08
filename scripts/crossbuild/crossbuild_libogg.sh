#! /bin/sh
#
# Builds and installs libogg for the cross toolchain.
# Sourced from build-uqm-dependencies.chroot

echo "***********************************************************************************************"
echo "--- BEGIN: crossbuild_libogg ---"

cd /tmp

wget --output-document=/tmp/libogg.tar.gz ${LIBOGG_URL}

if [ -f libogg.tar.gz ]; then

	if [ ! -d libogg ]; then 
		mkdir libogg
	fi

	tar -zxf libogg.tar.gz -C libogg
	cd libogg/libogg*
else
	echo "crossbuild_libogg failed: Could not get/extract libogg source"
	exit 1
fi

if [ -f configure ]; then
	./configure\
		--host=${HOST_TRIPLET}\
		--build=i686-linux-gnu\
		--prefix=/usr/${HOST_TRIPLET}
else
	echo "crossbuild_libogg failed: Could not find ./configure (is libogg source tarball sane?)"
	exit 1
fi

if [ -f Makefile ]; then
	make clean
	make
	make install
else
	echo "crossbuild_libogg failed: Could not find Makefile (did ./configure fail?)"
	exit 1
fi

echo "--- END: crossbuild_libogg ---"
echo "***********************************************************************************************"
