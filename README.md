# OpenCascade
Conan recipe for build of the Open Cascade library. On Windows platform you may need to force the use of short_paths or disable the 260 character limit for path lengts in settings of the operating system. For more info see.: https://docs.conan.io/en/latest/reference/conanfile/attributes.html#short-paths
 
## Build
```
cd 0.18.3
conan create . -s compiler.version=12
```
