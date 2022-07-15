project (read_manager)

# Toolkit for working with NK parser.
include (platform/nk)

# Setting compilation flags.
project_header_default ("STANDARD_GNU_11:YES" "STRICT_WARNINGS:NO")
add_compile_options(-fexceptions)

add_executable (
        Hello
        "src/read_manager.cpp"
        "src/main.cpp"
        ${EDL_FILES})

add_dependencies (Hello hello_on_kos_read_manager)
target_link_libraries (Hello ${${PROJECT_NAME}_LIBS} ${vfs_CLIENT_LIB})

# We do not need default VFS entity here, which comes from ${vfs_CLIENT_LIB}.
set_target_properties (Hello PROPERTIES ${vfs_ENTITY}_REPLACEMENT "")