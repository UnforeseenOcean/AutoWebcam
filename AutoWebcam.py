from webcam import Webcam
import configparser
import cv2
import screeninfo

config = configparser.ConfigParser()
config.read("settings.ini")

srcindex = config["Main"]["DeviceIndex"]
width = config["Main"]["Width"]
height = config["Main"]["Height"]
framerate = config["Main"]["MaxFrameRate"]
screenid = config["Main"]["WhichScreen"]

print(srcindex, width, height, framerate, screenid)

screen = screeninfo.get_monitors()[int(screenid)]
webcam = Webcam(src=int(srcindex), w=int(width), h=int(height), max_frame_rate=int(framerate))
print(f"Frame size: {webcam.w}, {webcam.h}")

WinName = "WebcamViewer"
cv2.namedWindow(WinName, cv2.WINDOW_NORMAL)
cv2.moveWindow(WinName, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(WinName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

for frame in webcam:
    cv2.imshow(WinName, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
