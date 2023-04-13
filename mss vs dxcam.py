import time
from mss import mss
import numpy as np
import dxcam


screenshot = 704

# MMS screenshot
screen_capture = mss()
screen_region = screen_capture.monitors[1]
screen_region['left'] = int((1920 / 2) - (screenshot / 2))
screen_region['top'] = int((1080 / 2) - (screenshot / 2))
screen_region['width'] = screenshot
screen_region['height'] = screenshot

start_time = time.time()
img_mms = np.array(screen_capture.grab(screen_region))
mms_time = time.time() - start_time
print("Tempo di cattura con MMS:", mms_time)

# DXCam screenshot
left, top = (1920 - screenshot) // 2, (1080 - screenshot) // 2
right, bottom = left + screenshot, top + screenshot
region = (left, top, right, bottom)
camera = dxcam.create(device_idx=0, output_idx=0,region=region,output_color="BGRA")
camera.start(target_fps=240, video_mode=True)

start_time = time.time()
img_dxcam = np.array(camera.get_latest_frame())
dxcam_time = time.time() - start_time
print("Tempo di cattura con DXCam:", dxcam_time)



# Compare results
print("Dimensioni screenshot:", screenshot, "x", screenshot)
print("Numero di pixel:", screenshot * screenshot)

print("Tempo di cattura con MMS:", mms_time)
print("Tempo di cattura con DXCam:", dxcam_time)


print("MMS / DXCam:", mms_time / dxcam_time)
print("DXCam /MMS :", dxcam_time / mms_time)

print("Media RGB MMS:", np.mean(img_mms))
print("Media RGB DXCam:", np.mean(img_dxcam))



