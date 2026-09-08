FROM ros:jazzy-ros-base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY src /workspace/src

RUN apt-get update && \
    rosdep update --rosdistro jazzy && \
    rosdep install --from-paths src --ignore-src -y -r --rosdistro jazzy && \
    rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/jazzy/setup.sh && colcon build --symlink-install

RUN echo "source /workspace/install/setup.bash" >> ~/.bashrc

CMD ["bash"]
