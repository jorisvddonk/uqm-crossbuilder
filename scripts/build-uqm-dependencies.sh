#! /bin/sh

# Takes care of cross-building the different UQM depencencies.
#
# This script is merely a wrapper, it specifies envvars for the scripts that do
# the actual work, then launches them. Only this script should be called directly.

# Uncomment the following line to keep build directories intact.
export KEEP_TEMP="1"

# envvar HOST_TRIPLET
#
# This is used as the host triplet for the cross toolchain.
# Autoconf-using packages will get this in their --host option,
# and packages will be installed to /usr/$HOST_TRIPLET.
# Do not change unless you have changed the cross toolchain to be used
# in base-cross-toolchain.list.
export HOST_TRIPLET="i686-w64-mingw32"

# envvar LIBICONV_URL
#
# Specifies the URL of the libiconv source tarball you want to use.
export LIBICONV_URL="http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz"

# envvar ZLIB_URL
#
# Specifies the URL of the zlib source tarball you want to use.
export ZLIB_URL="http://zlib.net/zlib-1.2.7.tar.gz"

# envvar LIBOGG_URL
#
# Specifies the URL of the libogg source tarball you want to use.
export LIBOGG_URL="http://downloads.xiph.org/releases/ogg/libogg-1.3.0.tar.gz"

# envvar LIBVORBIS_URL
#
# Specifies the URL of the libvorbis source tarball you want to use.
export LIBVORBIS_URL="http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.3.tar.gz"

# envvar LIBSDL_URL
#
# Specifies the URL of the libsdl source tarball you want to use.
export LIBSDL_URL="http://www.libsdl.org/release/SDL-1.2.15.tar.gz"

# envvar LIBSDL_IMAGE_URL
#
# Specifies the URL of the libsdl_image source tarball you want to use.
export LIBSDL_IMAGE_URL="http://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz"

echo "Building UQM dependencies"
echo ""

. /uqmdev/scripts/crossbuild/crossbuild_libiconv.sh
. /uqmdev/scripts/crossbuild/crossbuild_zlib.sh
. /uqmdev/scripts/crossbuild/crossbuild_libogg.sh
. /uqmdev/scripts/crossbuild/crossbuild_libvorbis.sh
. /uqmdev/scripts/crossbuild/crossbuild_libsdl.sh
. /uqmdev/scripts/crossbuild/crossbuild_libsdl-image.sh

echo ""
echo "Finished building UQM dependencies"

if [ ! ${KEEP_TEMP} ]; then
	rm /tmp/*
fi
