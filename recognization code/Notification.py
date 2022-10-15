from plyer import notification
import time

while True:
    time.sleep(2)
    notification.notify(
        title='Alert From Police HQ',
        message='Suspected person found in your area',
        app_icon="Notif.ico",
        timeout=8,
    )
# cv2.imshow(images/Het.jpg)
# cv2.imshow(images/RDJ.jpg)
# cv2.waitKey(0)
