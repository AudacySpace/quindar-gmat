# Install script for directory: /GMAT-R2015a/plugins

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/GMAT-R2015a/GMAT-R2015a-Linux-x64")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "0")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  INCLUDE("/GMAT-R2015a/plugins/CInterfacePlugin/src/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/DataInterfacePlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/EphemPropagatorPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/EstimationPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/EventLocatorPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/ExtraPropagatorsPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/FormationPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/GeometricMeasurementPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/GmatFunctionPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/MatlabInterfacePlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/NewParameterPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/PolyhedronGravityPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/ProductionPropagatorPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/PythonInterfacePlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/SaveCommandPlugin/src/base/cmake_install.cmake")
  INCLUDE("/GMAT-R2015a/plugins/StationPlugin/src/base/cmake_install.cmake")

ENDIF(NOT CMAKE_INSTALL_LOCAL_ONLY)

