# FROM defines the base image
FROM tensorflow/tensorflow:latest-gpu-py3
MAINTAINER Ankur Gupta

# RUN executes a shell command
# You can chain multiple commands together with &&
# A \ is used to split long lines to help with readability
RUN apt-get update && apt-get install -y \
    # tools
    git \
    python-setuptools \
    python-virtualenv \
    graphviz

# Install keras and theano dependencies not included in
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/Dockerfile.gpu
RUN pip install -U pip && pip --no-cache-dir install --upgrade \
		numpy \
		matplotlib \
    pandas \
    h5py \
    pyyaml \
    virtualenv \
    graphviz \
    pydot \
    keras-tqdm

# Enable the widgetsnbextension for notebook
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension

# Install  keras
RUN pip --no-cache-dir install --no-deps \
    keras \
    git+https://www.github.com/farizrahman4u/keras-contrib.git

# Set keras backend to tensorflow by default
ENV KERAS_BACKEND tensorflow

# Add /root/workspace to PYTHONPATH for convenience
ENV PYTHONPATH /root/workspace:$PYTHONPATH

# Set the working directory
WORKDIR /root/workspace

# CMD defines the default command to be run in the container
# CMD is overridden by supplying a command + arguments to
# `docker run`, e.g. `nvcc --version` or `bash`
CMD ["/run_jupyter.sh"]
