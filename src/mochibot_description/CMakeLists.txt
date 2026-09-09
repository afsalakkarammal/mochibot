cmake_minimum_required(VERSION 3.22)
project(mochibot_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY urdf launch config rviz meshes
  DESTINATION share/${mochibot_description}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

install(
  DIRECTORY urdf launch
  DESTINATION share/${PROJECT_NAME}
)
