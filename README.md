# AutoWebcam
A configurable automatic fullscreen webcam viewer
---
## Requires Python 3.11 or higher!
Does what it says on the tin. I forgot I made this and I'm just uploading this right now.

## Troubleshooting
1. Webcam light turns on then the program exits, the screen says something about not being able to grab the frame

Please check the base width and height parameters (the viewing window is always resized automatically to fit the monitor you selected)
Setting them to an unsupported mode (i.e. setting them to 1920x1080 while the webcam only supports up to 1280x720) will cause this error.

2. Index out of range error while starting (program closes without webcam light turning on)

**Check webcam and/or screen index** (0 being the "1" in the Windows screen configurator for the screen, and the first webcam the system detects)
Try setting both to 0 if there's only one screen and one webcam (or a webcam-compatible device such as a capture card) connected.

3. How do I exit?

**Press Q.** If it doesn't work, click on the window, then press Q.
