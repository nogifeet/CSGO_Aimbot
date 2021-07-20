# CSGO_Aimbot

In this repo, I will try to demonstrate how it is possible to create a bot that is able to play an FPS game and make 0-minimum latency inferences. In the world of Computer Vision/AI/Robotics real-life FPS count is said to range from 23–25 and anything below 20 creates a bottleneck for FPS count and cannot be categorized as real-life FPS.

In the above table, you clearly see why running object detection models on the CPU is actually bad when it comes to any real-time applications. This is because any new-gen CPU might have 4–8 cores while GPU's can have 100's or 1000's cores. A GPU will break down a task into smaller steps and process them simultaneously. While a CPU is better off with serial processing.

There are many different methods to run inference on GPU in both windows and ubuntu for example (i)TensorRT has support for both Ubuntu and Windows platforms(TensorRT Windows currently does not support Python ) (ii)OpenCV is another great library for GPU inference across platforms. (iii)MatLab with its GPU Coder allows Cuda code generation for Nvidia GPU's. For the purpose of this project, I decided to go with OpenCV as it was supported cross-platform and easier to compile as compared to TensorRT.

## Environment Setup:
1. Cuda + cudNN
2. Python 3.7+ or Conda environment
3. Visual Studio with C++ Modules
4. OpenCV GPU
5. darknet
6. pynput
7. numpy
8. win32api
9. win32con
10. ffmpeg

* Cuda+Cudnn Guide(Windows): https://medium.com/analytics-vidhya/install-tensorflow-gpu-cuda-in-windows-10-with-easy-to-follow-instructions-614d79782d26
* OpenCV-GPU Build Guide: https://www.youtube.com/watch?v=YsmhKar8oOc&t=535s
* Darknet Build Guide: https://github.com/AlexeyAB/darknet
* Darknet Google collab Guide: https://github.com/nogifeet/Vehicle-License-Plate-

## Data Gathering:

Training an object detection model requires a large amount of data and precise and consistent labels in each image. For gathering images I downloaded CSGO Gameplay videos from youtube. Using the FFmpeg library to convert videos to images resulting in 1 image for every second 2000:500[train: Val] images.

```python
#one image for every second
ffmpeg -i input.mp4 -r 1 /images/%04d.jpg
```
