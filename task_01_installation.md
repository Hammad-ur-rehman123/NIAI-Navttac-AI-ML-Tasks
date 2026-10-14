# Task 1 - Software Installation (NAVTTC Week 1)

Platform: Windows 10. Anaconda was installed on the E: drive because C: had little free space.

## Anaconda3

Downloaded from anaconda.com/download and installed to `E:\Anaconda`. Verified from Anaconda Prompt:

```
(base) C:\Users\HAMMAD>python --version
Python 3.14.6
```

## PyTorch

```
(base) C:\Users\HAMMAD>pip install torch torchvision torchaudio
...
Successfully installed torch-2.14.0 torchaudio-2.11.0 torchvision-0.29.0
```

## TensorFlow

TensorFlow does not yet publish a build for Python 3.14, so pip could not find one:

```
(base) C:\Users\HAMMAD>pip install tensorflow
ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow
```

Planned fix: create a separate conda environment with Python 3.11 and install TensorFlow there:

```
conda create -n tf_env python=3.11
conda activate tf_env
pip install tensorflow
```

## Git Bash

Installed from git-scm.com to get a Linux-style terminal on Windows (used for Task 2).

## Still to do

- VS Code and PyCharm (both are available to install from Anaconda Navigator)
- TensorFlow in the Python 3.11 environment
