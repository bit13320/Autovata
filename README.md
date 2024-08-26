# Autovata
make DJI Avata drone fly autonomously
Check out the demonstration video of the current progress:

[![Watch the video](https://img.youtube.com/vi/by5izqqeP98/maxresdefault.jpg)](https://www.youtube.com/watch?v=by5izqqeP98)

---
avata无人机有保护圈，无线连接稳定，室内依靠光流和激光雷达可精准定高定点，摄像头分辨率高，因此适合作为室内巡检无人机使用。但是DJI没有开放其SDK，因此我突发奇想，使用舵机控制遥控器，用机器视觉来使Avata实现全自主飞行。 注意：本项目并未开发完成，本项目目前只实现了两个部分：1.使用Scrcpy将DJI Fly界面无线串流到windows电脑，aruco2.py将检测串流画面中的Aruco Marker并进行方位估计。 2.Micropyton文件夹中的文件用于控制Micropython设备（我用的是ESP32）实现舵机控制DJI FPV Controller

The Avata drone has protective guards, stable wireless connection, and can accurately maintain altitude and position indoors using optical flow and LiDAR. It also has a high-resolution camera, making it suitable for indoor inspection purposes. However, since DJI hasn’t released its SDK, I had the idea of using servos to control the remote controller and machine vision to achieve fully autonomous flight with the Avata.

Note: This project is not yet fully developed. So far, it has completed two parts:

Using Scrcpy to wirelessly stream the DJI Fly interface to a Windows PC, with Aruco2.py detecting Aruco Markers in the streamed footage for position estimation.
Using Micropython to control servos on a Micropython device (I used an ESP32) to operate the DJI FPV Controller.
