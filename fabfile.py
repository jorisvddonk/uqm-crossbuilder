from fabric.api import *

"""
Set up uqmdev session
"""
env.user = 'vagrant'
env.password = 'vagrant'
env.hosts = ['127.0.0.1:2222']

##################################################################################################

def init():
  local("vagrant up")
  _fix_crosscompile_toolchain()
  _fix_scripts_line_endings()
  _build_deps()

def halt():
  local("vagrant halt")


def download_uqm_src():
  with cd("/uqmdev"):
    run("mkdir -p projects")
    with cd("/uqmdev/projects"):
      run("wget http://downloads.sourceforge.net/project/sc2/UQM/0.7/uqm-0.7.0-source.tgz")
      run("tar -xvzf uqm-0.7.0-source.tgz")

def build_uqm():
  with cd("/uqmdev/projects/uqm-0.7.0"):
    run("/uqmdev/scripts/cross-build.sh uqm")

##################################################################################################

def _build_deps():
  sudo("/uqmdev/scripts/build-uqm-dependencies.sh")

def _fix_scripts_line_endings():
  run("dos2unix /uqmdev/scripts/*.sh")
  run("dos2unix /uqmdev/scripts/crossbuild/*.sh")

def _fix_crosscompile_toolchain():
  #Link tools
  sudo("mkdir -p /usr/i686-w64-mingw32/bin")
  sudo("ln -s /usr/bin/i686-w64-mingw32-addr2line /usr/i686-w64-mingw32/bin/addr2line")
  sudo("ln -s /usr/bin/i686-w64-mingw32-ar /usr/i686-w64-mingw32/bin/ar")
  sudo("ln -s /usr/bin/i686-w64-mingw32-as /usr/i686-w64-mingw32/bin/as")
  sudo("ln -s /usr/bin/i686-w64-mingw32-c++ /usr/i686-w64-mingw32/bin/c++")
  sudo("ln -s /usr/bin/i686-w64-mingw32-c++filt /usr/i686-w64-mingw32/bin/c++filt")
  sudo("ln -s /usr/bin/i686-w64-mingw32-cpp /usr/i686-w64-mingw32/bin/cpp")
  sudo("ln -s /usr/bin/i686-w64-mingw32-dlltool /usr/i686-w64-mingw32/bin/dlltool")
  sudo("ln -s /usr/bin/i686-w64-mingw32-dllwrap /usr/i686-w64-mingw32/bin/dllwrap")
  sudo("ln -s /usr/bin/i686-w64-mingw32-elfedit /usr/i686-w64-mingw32/bin/elfedit")
  sudo("ln -s /usr/bin/i686-w64-mingw32-g++ /usr/i686-w64-mingw32/bin/g++")
  sudo("ln -s /usr/bin/i686-w64-mingw32-gcc /usr/i686-w64-mingw32/bin/gcc")
  sudo("ln -s /usr/bin/i686-w64-mingw32-gcc-4.6 /usr/i686-w64-mingw32/bin/gcc-4.6")
  sudo("ln -s /usr/bin/i686-w64-mingw32-gcov /usr/i686-w64-mingw32/bin/gcov")
  sudo("ln -s /usr/bin/i686-w64-mingw32-gprof /usr/i686-w64-mingw32/bin/gprof")
  sudo("ln -s /usr/bin/i686-w64-mingw32-ld /usr/i686-w64-mingw32/bin/ld")
  sudo("ln -s /usr/bin/i686-w64-mingw32-ld.bfd /usr/i686-w64-mingw32/bin/ld.bfd")
  sudo("ln -s /usr/bin/i686-w64-mingw32-ld.nm /usr/i686-w64-mingw32/bin/ld.nm")
  sudo("ln -s /usr/bin/i686-w64-mingw32-objcopy /usr/i686-w64-mingw32/bin/objcopy")
  sudo("ln -s /usr/bin/i686-w64-mingw32-objdump /usr/i686-w64-mingw32/bin/objdump")
  sudo("ln -s /usr/bin/i686-w64-mingw32-ranlib /usr/i686-w64-mingw32/bin/ranlib")
  sudo("ln -s /usr/bin/i686-w64-mingw32-readelf /usr/i686-w64-mingw32/bin/readelf")
  sudo("ln -s /usr/bin/i686-w64-mingw32-size /usr/i686-w64-mingw32/bin/size")
  sudo("ln -s /usr/bin/i686-w64-mingw32-strings /usr/i686-w64-mingw32/bin/strings")
  sudo("ln -s /usr/bin/i686-w64-mingw32-strip /usr/i686-w64-mingw32/bin/strip")
  sudo("ln -s /usr/bin/i686-w64-mingw32-windmc /usr/i686-w64-mingw32/bin/windmc")
  sudo("ln -s /usr/bin/i686-w64-mingw32-windres /usr/i686-w64-mingw32/bin/windres")
  #Link libraries
  sudo("ln -s /usr/i686-w64-mingw32/libogg.lib /usr/i686-w64-mingw32/lib/ogg.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libogg_d.lib /usr/i686-w64-mingw32/lib/ogg_d.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libogg_static.lib /usr/i686-w64-mingw32/lib/ogg_static.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libogg_static_d.lib /usr/i686-w64-mingw32/lib/ogg_static_d.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbis.lib /usr/i686-w64-mingw32/lib/vorbis.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbis_d.lib /usr/i686-w64-mingw32/lib/vorbis_d.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbis_static.lib /usr/i686-w64-mingw32/lib/vorbis_static.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbis_static_d.lib /usr/i686-w64-mingw32/lib/vorbis_static_d.l")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbisfile.lib /usr/i686-w64-mingw32/lib/vorbisfile.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbisfile_d.lib /usr/i686-w64-mingw32/lib/vorbisfile_d.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbisfile_static.lib /usr/i686-w64-mingw32/lib/vorbisfile_static.lib")
  sudo("ln -s /usr/i686-w64-mingw32/libvorbisfile_static_d.lib /usr/i686-w64-mingw32/lib/vorbisfile_static_d.lib")

