import os
import pprint

from conans import ConanFile, CMake, tools
from conans.util import files

class OpenCascadeConan(ConanFile):
    name = "OpenCascade"
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
        #buildDir = "_build"
        #files.mkdir(buildDir)
        #with tools.chdir(buildDir):
            cmake = CMake(self)
            cmake.verbose = True
            cmake.definitions['OCE_INSTALL_PREFIX'] = "."
            cmake.definitions['OCE_INSTALL_INCLUDE_DIR'] = "include"
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
            cmake.configure(build_dir=".", source_dir="%s" % self.ZIP_FOLDER_NAME)
            cmake.build(build_dir=".")
            cmake.install()

    def package(self):
        self.copy("*.h", dst=".")
        self.copy("*.hxx", dst=".")
        self.copy("*.lxx", dst=".")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def get_lib_file_extension(self):
        if self.settings.os == "Windows":
            return "lib"

        return "a"

    def lib(self, filename):
        return "%s.%s" % (filename, self.get_lib_file_extension())

    def package_info(self):
        #self.cpp_info.include_dirs = ["include"]
        self.cpp_info.src_dirs = ["src"]
        #self.cpp_info.bin_dirs = ["bin"]
        #self.cpp_info.lib_dirs = ["lib"]

        self.cpp_info.libs = [
            self.lib("FWOSPlugin"),
            self.lib("PTKernel"),
            self.lib("TKBin"),
            self.lib("TKBinL"),
            self.lib("TKBinTObj"),
            self.lib("TKBinXCAF"),
            self.lib("TKBO"),
            self.lib("TKBool"),
            self.lib("TKBRep"),
            self.lib("TKCAF"),
            self.lib("TKCDF"),
            self.lib("TKernel"),
            self.lib("TKFeat"),
            self.lib("TKFillet"),
            self.lib("TKG2d"),
            self.lib("TKG3d"),
            self.lib("TKGeomAlgo"),
            self.lib("TKGeomBase"),
            self.lib("TKHLR"),
            self.lib("TKIGES"),
            self.lib("TKLCAF"),
            self.lib("TKMath"),
            self.lib("TKMesh"),
            self.lib("TKOffset"),
            self.lib("TKPCAF"),
            self.lib("TKPLCAF"),
            self.lib("TKPrim"),
            self.lib("TKPShape"),
            self.lib("TKService"),
            self.lib("TKShapeSchema"),
            self.lib("TKShHealing"),
            self.lib("TKStdLSchema"),
            self.lib("TKStdSchema"),
            self.lib("TKSTEP"),
            self.lib("TKSTEP209"),
            self.lib("TKSTEPAttr"),
            self.lib("TKSTEPBase"),
            self.lib("TKSTL"),
            self.lib("TKTObj"),
            self.lib("TKTopAlgo"),
            self.lib("TKV3d"),
            self.lib("TKVRML"),
            self.lib("TKXCAF"),
            self.lib("TKXCAFSchema"),
            self.lib("TKXDEIGES"),
            self.lib("TKXDESTEP"),
            self.lib("TKXMesh"),
            self.lib("TKXml"),
            self.lib("TKXmlL"),
            self.lib("TKXmlTObj"),
            self.lib("TKXmlXCAF"),
            self.lib("TKXSBase"),
            ]


        pass
