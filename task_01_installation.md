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

TensorFlow does not yet publish a build for Python 3.14, so pip could not find one in the base environment:

```
(base) C:\Users\HAMMAD>pip install tensorflow
ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow
```

Fix: created a separate conda environment with Python 3.11 and installed TensorFlow there:

```
conda create -n tf_env python=3.11
conda activate tf_env
pip install tensorflow
```

Verified inside `tf_env`:

```
(tf_env) C:\Users\HAMMAD>python --version
Python 3.11.16

(tf_env) C:\Users\HAMMAD>python -c "import tensorflow as tf; print(tf.__version__)"
2.21.0
```

(TensorFlow also prints some oneDNN info messages on import; these are informational, not errors, and are left out above.)

TensorFlow is used from `tf_env`, while PyTorch and the rest are in the base environment.

## Git Bash

Installed from git-scm.com to get a Linux-style terminal on Windows (used for Task 2).

## VS Code

Installed and verified from Anaconda Prompt:

```
(base) C:\Users\HAMMAD>code --version
1.141.0
2a59476c9bfcb90b3ddc372c36762471b7dfad1c
x64
```

## PyCharm

Installed.

## Summary

| Software | Status | Environment |
|---|---|---|
| Anaconda3 | Installed | base |
| PyTorch | Installed | base |
| TensorFlow 2.21.0 | Installed | tf_env (Python 3.11) |
| Git Bash | Installed | - |
| VS Code 1.141.0 | Installed | - |
| PyCharm | Installed | - |
