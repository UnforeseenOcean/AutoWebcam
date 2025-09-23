from webcam import Webcam
import configparser
import cv2
import screeninfo

config = configparser.ConfigParser()
config.read("settings.ini")

srcindex = config.getint("Main", "DeviceIndex", fallback=0)
width = config.getint("Main", "Width", fallback=640)
height = config.getint("Main", "Height", fallback=480)
framerate = config.getint("Main", "MaxFrameRate", fallback=30)
screenid = config.getint("Main", "WhichScreen", fallback=0)
backend = config.get("Main", "Backend", fallback="msmf").lower()

print(srcindex, width, height, framerate, screenid, backend)

backends = {
    "msmf": cv2.CAP_MSMF,
    "dshow": cv2.CAP_DSHOW,
    "vfw": cv2.CAP_VFW,
    "any": cv2.CAP_ANY
}

fallback_order = ["dshow", "msmf", "vfw", "any"]

if backend in fallback_order:
    fallback_order.remove(backend)
fallback_order.insert(0, backend)

cap = None
used_backend = None

screen = screeninfo.get_monitors()[int(screenid)]

for bname in fallback_order:
    backend = backends[bname]
    print(f"Trying backend: {bname.upper()}...")
    cap = cv2.VideoCapture(srcindex, backend)

    if cap.isOpened():
        used_backend = bname
        print(f"Opened camera {srcindex} using {bname.upper()} backend.")
        break
    else:
        print(f"Failed with backend: {bname.upper()}")
        cap.release()

if cap is None or not cap.isOpened():
    print("Could not open video device with any backend. What's up with that?")
    sys.exit(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, framerate)

print("Camera settings in use:")
print(f"Backend : {used_backend.upper()}")
print(f"Width   : {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"Height  : {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"FPS     : {cap.get(cv2.CAP_PROP_FPS)}")

WinName = "WebcamViewer"
cv2.namedWindow(WinName, cv2.WINDOW_NORMAL)
cv2.moveWindow(WinName, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(WinName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame!")
        break

    cv2.imshow(WinName, frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
