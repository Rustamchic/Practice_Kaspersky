cmake_minimum_required (VERSION 3.12)

project(Hello_on_KOS)
# Initialize the CMake library for the KasperskyOS SDK.
include (platform)
initialize_platform ()

# Connect artifact installation functions.
include (platform/install)

include (platform/nk)
nk_build_edl_files (hello_on_kos_hello NK_MODULE "hello_on_kos" EDL "resources/edl/Hello.edl")
nk_build_edl_files (hello_on_kos_vfs_user  NK_MODULE "hello_on_kos" EDL "resources/edl/VfsUser.edl")

# Connect a package which imports components
# to work with the virtual file system.
find_package (vfs REQUIRED COMPONENTS FS_LIB CLIENT_LIB SERVER_LIB)
include_directories (${vfs_INCLUDE})

# Connect a package that imports components
# to work with the ext2/ext3/ext4 file systems.
find_package (LWEXT4 REQUIRED)
include_directories (${LWEXT4_INCLUDE})

# Attach a directory with a header containing file name definitions.
include_directories (common)

add_subdirectory (hello)
add_subdirectory (vfs_user)

# Binary image of the KasperskyOS.
add_subdirectory (einit)