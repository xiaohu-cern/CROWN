cmake_minimum_required(VERSION 3.20)
# Unset some cached variables
unset(CMAKE_BUILD_TYPE CACHE)
unset(CMAKE_CXX_FLAGS_RELEASE CACHE)

# include cmake modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
# parse args
include(ParseArguments)

# Set the default install directory to the build directory
set(CMAKE_INSTALL_PREFIX
    ${CMAKE_BINARY_DIR}
    CACHE STRING "Set default install prefix to the build directory")
message(STATUS "Creating Project")
# Create the project
project(CROWN CXX)
message(STATUS "Finding Packages")
# Find ROOT and print details
find_package(ROOT 6.26 REQUIRED COMPONENTS ROOTVecOps ROOTDataFrame RooFit GenVector RIO Physics)
# add OpenMP and MPI
find_package(OpenMP)
find_package(MPI)
# add nlohmann json
find_package(nlohmann_json)

message(STATUS "")
message(STATUS "Found ROOT with following settings:")
message(STATUS "  Version: ${ROOT_VERSION}")
message(STATUS "  ROOT executable: ${ROOT_EXECUTABLE}")
message(STATUS "  Include directories: ${ROOT_INCLUDE_DIRS}")
message(STATUS "  Compiler flags: ${ROOT_CXX_FLAGS}")
message(STATUS "")

# Add ROOT flags to compile options, e.g. we have to use the same C++ standard
# Note that the flags from the build type, e.g. CMAKE_CXX_FLAGS_RELEASE, are
# automatically appended. You can check this during build time by enabling
# the verbose make output with "VERBOSE=1 make".
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${ROOT_CXX_FLAGS}")

# Use -fconcepts with g++ to silence following warning:
# warning: use of 'auto' in parameter declaration only available with '-fconcepts
if (CMAKE_CXX_COMPILER_ID STREQUAL GNU)
    message(STATUS "Attach -fconcepts to the compiler flags to silence warnings.")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fconcepts")
endif()

# Find the C++ standard from ROOT and set it as the standard of this project
# We require the C++ standard 17 or 20 and don't want to fall back to lower versions.
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if (${ROOT_CXX_FLAGS} MATCHES "\\-std\\=c\\+\\+17")
    message(STATUS "Set c++17 as the C++ standard.")
    set(CMAKE_CXX_STANDARD 17)
elseif (${ROOT_CXX_FLAGS} MATCHES "\\-std\\=c\\+\\+20")
    message(STATUS "Set c++20 as the C++ standard.")
    set(CMAKE_CXX_STANDARD 20)
elseif (${ROOT_CXX_FLAGS} MATCHES "\\-std\\=c\\+\\+14")
    message(STATUS "c++14 found, setting c++17 as the C++ standard.")
    set(CMAKE_CXX_STANDARD 17)
else ()
    message(FATAL_ERROR "The standard c++17 or higher is required but not found in the ROOT flags: ${ROOT_CXX_FLAGS}")
endif()

message(STATUS "Including spdlog.")
# Build the logging library
include(ExternalProject)
ExternalProject_Add(spdlog
    PREFIX          spdlog
    GIT_REPOSITORY  https://github.com/gabime/spdlog.git
    GIT_SHALLOW     1
    GIT_TAG         v1.8.5
    CMAKE_ARGS      -DCMAKE_CXX_STANDARD=${CMAKE_CXX_STANDARD}
                    -DCMAKE_BUILD_TYPE=Release
                    -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}
                    -DCMAKE_CXX_FLAGS=-fpic
    LOG_DOWNLOAD 1 LOG_CONFIGURE 1 LOG_BUILD 1 LOG_INSTALL 1
    BUILD_BYPRODUCTS ${CMAKE_INSTALL_PREFIX}/lib64/libspdlog.a
    BUILD_BYPRODUCTS ${CMAKE_INSTALL_PREFIX}/lib/libspdlog.a
)

message(STATUS "Configuring spdlog.")
# Make an imported target out of the build logging library
add_library(logging STATIC IMPORTED)
file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/include") # required because the include dir must be existent for INTERFACE_INCLUDE_DIRECTORIES
include(GNUInstallDirs) # required to populate CMAKE_INSTALL_LIBDIR with lib or lib64 required for the destination of libspdlog.a
set_target_properties(logging PROPERTIES
    IMPORTED_LOCATION "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR}/libspdlog.a"
    INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_BINARY_DIR}/include")
add_dependencies(logging spdlog) # enforces to build spdlog before making the imported target

# Print settings of the executable
string(TOUPPER ${CMAKE_BUILD_TYPE} CMAKE_BUILD_TYPE_UPPER)
message(STATUS "")
message(STATUS "The executable is configured with following flags:")
message(STATUS "  Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  C++ compiler: ${CMAKE_CXX_COMPILER}")
message(STATUS "  Base compiler flags: ${CMAKE_CXX_FLAGS}")
message(
  STATUS
    "  Compiler flags from build type: ${CMAKE_CXX_FLAGS_${CMAKE_BUILD_TYPE_UPPER}}"
)
message(STATUS "")

# Find Python 3
find_package(Python 3.9 REQUIRED COMPONENTS Interpreter)

# detect virtualenv and set Pip args accordingly
if(DEFINED ENV{VIRTUAL_ENV} OR DEFINED ENV{CONDA_PREFIX})
  set(_pip_args)
else()
  set(_pip_args "--user")
endif()

function(find_python_package PYPINAME NAME MIN_VERSION)
    execute_process(COMMAND "${Python_EXECUTABLE}" "-c" "import ${NAME}; print(${NAME}.__version__)"
                    RESULT_VARIABLE PACKAGE_NOT_FOUND
                    OUTPUT_VARIABLE PACKAGE_VERSION
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
    if(${PACKAGE_NOT_FOUND} EQUAL 1)
        execute_process(COMMAND ${Python_EXECUTABLE} -m pip install ${PYPINAME} ${_pip_args})
        execute_process(COMMAND "${Python_EXECUTABLE}" "-c" "import ${NAME}; print(${NAME}.__version__)"
                    RESULT_VARIABLE PACKAGE_NOT_FOUND
                    OUTPUT_VARIABLE PACKAGE_VERSION
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
        if(${PACKAGE_NOT_FOUND} EQUAL 1)
            message(FATAL_ERROR "Failed to import ${PYPINAME} or get version.")
        endif()
    endif()
# xiaohu: since 202210 GitPython provides a git with version "git" not a number
# this fails the check in CMake, thus comment it out
#    if(PACKAGE_VERSION VERSION_LESS MIN_VERSION)
#        message(FATAL_ERROR "The version of Python package ${PYPINAME} is too old (found ${PACKAGE_VERSION}, require at least ${MIN_VERSION}).")
#    endif()
    message(STATUS "Found Python package ${PYPINAME} (require ${MIN_VERSION}, found ${PACKAGE_VERSION})")
endfunction()

function(install_correctionlib)
    execute_process(COMMAND "${Python_EXECUTABLE}" "-c" "import correctionlib; print(correctionlib.__version__)"
                    RESULT_VARIABLE PACKAGE_NOT_FOUND
                    OUTPUT_VARIABLE PACKAGE_VERSION
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
    if(${PACKAGE_NOT_FOUND} EQUAL 1)
        execute_process(COMMAND ${Python_EXECUTABLE} -m pip install ${_pip_args} git+https://github.com/cms-nanoAOD/correctionlib.git)
    endif()
    message(STATUS "Found correctionlib !")
endfunction()

# Adding correctionlib for scale factor evaluation
# for now the official pip package has some problem
# in the future "find_python_package(correctionlib correctionlib X.X)" should hopefully work
install_correctionlib()
message(STATUS "Setting up correctionlib ...")
execute_process(COMMAND correction config --cmake
    OUTPUT_VARIABLE CORRECTION_LIB_ARGS
    OUTPUT_STRIP_TRAILING_WHITESPACE)
string(REPLACE -Dcorrectionlib_DIR= "" CORRECTIONLIBPATH ${CORRECTION_LIB_ARGS})
# if correctionlib comes from cvmfs, change the correctionlibpath accordingly
if (${CORRECTIONLIBPATH} MATCHES "^/cvmfs/")
    message(STATUS "Setting up correctionlib from cvmfs ...")
    set(USING_CVMFS TRUE)
    find_package(correctionlib)
    find_library(CORRECTION_LIB_PATH correctionlib)
else()
    message(STATUS "Setting up correctionlib from local setup ...")
    set(USING_CVMFS FALSE)
    find_package(correctionlib REQUIRED PATHS ${CORRECTIONLIBPATH})
    set(CORRECTION_LIB_PATH "${CORRECTIONLIBPATH}/../lib/libcorrectionlib.so")
endif()
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads)
find_package(ZLIB)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
message(STATUS "Correctionlib library path: ${CORRECTION_LIB_PATH}")

# Generate the C++ code
if (NOT DEFINED INSTALLDIR)
    message(STATUS "No -DINSTALLDIR specified, using default: ${CMAKE_CURRENT_BINARY_DIR}/bin")
    set(INSTALLDIR ${CMAKE_CURRENT_BINARY_DIR}/bin)
message(STATUS "Finding Packages")
# add the different dependencies
include(AddBaseDependencies)
include(AddRoot)
include(AddLogging)
include(AddCorrectionlib)
include(AddOnnxruntime)
include(ConfigurePython)

# installdir
if(NOT DEFINED INSTALLDIR)
  message(
    STATUS
      "No -DINSTALLDIR specified, using default: ${CMAKE_CURRENT_BINARY_DIR}/bin"
  )
  set(INSTALLDIR ${CMAKE_CURRENT_BINARY_DIR}/bin)
endif()
set(GENERATE_CPP_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

# crownlib setup
include(ConfigureCrownlib)
if (BUILD_CROWNLIB_ONLY)
  # exit if only crownlib is being built
  return()
endif()
# run the code generation
include(CodeGeneration)

# build a shared lib from all CROWN functions
include_directories(${CMAKE_SOURCE_DIR}/src)
include_directories(${CMAKE_SOURCE_DIR}/include)
file(GLOB SOURCES_1 ${CMAKE_SOURCE_DIR}/src/*.cxx)
file(GLOB SOURCES_2
    ${CMAKE_SOURCE_DIR}/src/utility/*.cxx
    ${CMAKE_SOURCE_DIR}/src/RecoilCorrections/*.cxx
    ${CMAKE_SOURCE_DIR}/src/SVFit/*.cxx)
set(SOURCES ${SOURCES_1} ${SOURCES_2})
add_library(CROWNLIB SHARED ${SOURCES})
target_include_directories(CROWNLIB PRIVATE ${CMAKE_SOURCE_DIR} ${ROOT_INCLUDE_DIRS})
target_link_libraries(CROWNLIB ROOT::ROOTVecOps ROOT::ROOTDataFrame ROOT::RooFit ROOT::GenVector ROOT::RIO ${ROOT_LIBRARIES} logging correctionlib nlohmann_json::nlohmann_json)

# Iterate over files from output filelist and add build and install targets
FILE(READ ${GENERATE_CPP_OUTPUT_FILELIST} FILELIST)
STRING(REGEX REPLACE "\n" ";" FILELIST ${FILELIST})
set(TARGET_NAMES "")
# copy all correction files into the install location
install(DIRECTORY data/ DESTINATION ${INSTALLDIR}/data)
install(TARGETS CROWNLIB DESTINATION ${INSTALLDIR}/lib)

# also copy inish script needed for job tarball
install(FILES init.sh DESTINATION ${INSTALLDIR})
foreach(FILENAME ${FILELIST})
    # STRING(REGEX REPLACE ".cxx" "" TARGET_NAME ${FILENAME})
    cmake_path(GET FILENAME RELATIVE_PART RELATIVE_PATH)
    cmake_path(GET FILENAME FILENAME TARGET_FILENAMENAME)
    STRING(REGEX REPLACE ".cxx" "" TARGET_NAME ${TARGET_FILENAMENAME})
    STRING(REGEX REPLACE "/${TARGET_FILENAMENAME}" "" GENERATED_CODEBASE ${RELATIVE_PATH})

    list(APPEND TARGET_NAMES ${TARGET_NAME})
    set(FULL_PATH "${GENERATE_CPP_OUTPUT_DIRECTORY}/${FILENAME}")

    # Add build target
    message(STATUS "Add build target for file ${FILENAME}.")

    # message(STATUS "FULL_PATH: ${FULL_PATH} / TARGET_NAME: ${TARGET_NAME}")
    # message(STATUS "Adding header files from ${GENERATE_CPP_OUTPUT_DIRECTORY}/${GENERATED_CODEBASE}/include/*")
    file(GLOB GENERATED_HEADERS LIST_DIRECTORIES true "${GENERATE_CPP_OUTPUT_DIRECTORY}/${GENERATED_CODEBASE}/include/*")
    file(GLOB GENERATED_CXX_FILES "${GENERATE_CPP_OUTPUT_DIRECTORY}/${GENERATED_CODEBASE}/src/*/*.cxx")
    # message(STATUS "GENERATED_HEADERS ${GENERATED_HEADERS}")
    add_executable(${TARGET_NAME} ${FULL_PATH} ${GENERATED_CXX_FILES})
    # Adds a pre-build event to the Target copying the correctionlib.so file into the /lib folder in the install directory
    target_include_directories(${TARGET_NAME} PRIVATE ${CMAKE_SOURCE_DIR} ${ROOT_INCLUDE_DIRS} $ORIGIN/lib/ lib/)
    target_link_libraries(${TARGET_NAME} ROOT::ROOTVecOps ROOT::ROOTDataFrame ROOT::RooFit ROOT::GenVector ROOT::RIO ${ROOT_LIBRARIES} logging correctionlib nlohmann_json::nlohmann_json CROWNLIB)

    add_custom_command(TARGET ${TARGET_NAME} PRE_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CORRECTION_LIB_PATH}"
        ${INSTALLDIR}/lib/libcorrectionlib.so)
    # Find shared libraries next to the executable in the /lib folder
    set_target_properties(${TARGET_NAME} PROPERTIES
        BUILD_WITH_INSTALL_RPATH FALSE
        LINK_FLAGS "-Wl,-rpath,$ORIGIN/lib")
    # Add install target, basically just copying the executable around relative to CMAKE_INSTALL_PREFIX
    install(TARGETS ${TARGET_NAME} DESTINATION ${INSTALLDIR})
    install(CODE "execute_process(COMMAND ${CMAKE_SOURCE_DIR}/checks/get-diff.sh ${CMAKE_SOURCE_DIR} ${ANALYSIS} ${INSTALLDIR}/diff )")

endforeach()
# run the build
include(Build)

# tests Include tests
enable_testing()
add_subdirectory(tests)
