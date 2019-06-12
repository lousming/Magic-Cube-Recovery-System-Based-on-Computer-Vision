import net
import cv2

try:
    clf = net.learn()
except:
    print('No source image to learn. Annotate some first.')

def color_recognizer(src):
    dst = str(net.identify_color(src, clf))
    return dst
