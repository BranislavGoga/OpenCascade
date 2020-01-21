import os

from conans import ConanFile, CMake, tools
from conans.util import files

class OpenCascadeConan(ConanFile):
    name = "occ"
    version = "0.18.3"
    ZIP_FOLDER_NAME = "oce-OCE-%s" % version
    license = "https://github.com/tpaviot/oce/blob/master/LICENSE_LGPL_21.txt"
    description = "C++ 3D modeling library for CAD/CAM systems including import/export of CAD formats."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        zip_name = "OCE-%s.zip" % self.version
        url = "https://github.com/tpaviot/oce/archive/%s" % zip_name
        tools.download(url, zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        buildDir = "_build"
        files.mkdir(buildDir)
        with tools.chdir(buildDir):
            cmake = CMake(self)
            cmake.verbose = True
            cmake.definitions['OCE_DATA_EXCHANGE'] = True
            cmake.definitions['OCE_DRAW'] = False
            cmake.definitions['OCE_MODEL'] = True
            cmake.definitions['OCE_MULTITHREADED_BUILD'] = False
            cmake.definitions['OCE_OCAF'] = False
            cmake.definitions['OCE_TESTING'] = False
            cmake.definitions['OCE_VISUALIZATION'] = False
            cmake.definitions['OCE_USE_BUNDLE'] = False
            cmake.definitions['OCE_DISABLE_TKSERVICE_FONT'] = True
            cmake.definitions['OCE_WITH_FREE_IMAGE'] = False
            cmake.definitions['OCE_WITH_GL2PS'] = False
            cmake.definitions['OCE_WITH_VTK'] = False
            cmake.configure(build_dir=".", source_dir="../%s" % self.ZIP_FOLDER_NAME)
            cmake.build(build_dir=".")
            cmake.install()

    def package(self):
        #self.copy("*.h", dst="include", src="oce")
        #self.copy("*oce.lib", dst="lib", keep_path=False)
        #self.copy("*.dll", dst="bin", keep_path=False)
        #self.copy("*.so", dst="lib", keep_path=False)
        #self.copy("*.dylib", dst="lib", keep_path=False)
        #self.copy("*.a", dst="lib", keep_path=False)
        pass

    def package_info(self):
        #self.cpp_info.libs = ["oce"]
        pass
