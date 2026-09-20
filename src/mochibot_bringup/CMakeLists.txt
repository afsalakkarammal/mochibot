cmake_minimum_required(VERSION 3.8)
project(mochibot_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
# find_package(rclcpp REQUIRED) - REMOVED: Bringup packages typically do not contain C++ source code.
# find_package(mochibot_description REQUIRED) - REMOVED: Build-time dependency is unnecessary; it is a run-time execution dependency.

install(
  DIRECTORY launch config rviz
  DESTINATION share/${PROJECT_NAME}
  )

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_lint_auto_find_test_dependencies_EXISTS TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
