# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mochibot_perception_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mochibot_perception_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mochibot_perception_FOUND FALSE)
  elseif(NOT mochibot_perception_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mochibot_perception_FOUND FALSE)
  endif()
  return()
endif()
set(_mochibot_perception_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mochibot_perception_FIND_QUIETLY)
  message(STATUS "Found mochibot_perception: 0.0.0 (${mochibot_perception_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mochibot_perception' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT mochibot_perception_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mochibot_perception_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mochibot_perception_DIR}/${_extra}")
endforeach()
