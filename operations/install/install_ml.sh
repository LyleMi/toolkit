#!/bin/sh

pip install --upgrade Pillow
pip install --upgrade opencv-python
pip install --upgrade numpy
pip install --upgrade matplotlib
pip install --upgrade tensorflow
pip install --upgrade pandas
pip install --upgrade seaborn
pip install --upgrade scipy
pip install --upgrade sklearn
pip install --upgrade keras
pip install --upgrade jupyter

# https://github.com/kaggle/docker-python
docker run --rm -it gcr.io/kaggle-images/python
