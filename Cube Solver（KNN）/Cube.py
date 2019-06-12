import cv2
import numpy as np
import color_recognizer
import kociemba
import serial
import time
import binascii
import threading
vs = cv2.VideoCapture(0)
global turn_flag
global result
turn_flag=0
result=0
stickers = {
            'main': [
                [260, 150], [330, 150], [390, 150],
                [260, 216], [330, 216], [390, 216],
                [260, 280], [330, 280], [390, 280]
            ]}

color = {
            "Red":    (0,     0, 255),
            "Green":  (0,   255,   0),
            "Blue":   (255,   0,   0),
            "Yellow": (0,   255, 255),
            "Orange": (0,   127, 255),
            "White":  (255, 255, 255),

        }


def contrast_brightness_image(src, a, g):
    h, w, ch = src.shape
    src2 = np.zeros([h, w, ch], src.dtype)
    dst = cv2.addWeighted(src, a, src2, 1 - a, g)
    return dst

def change( x ):
  if x == "Red":
     y = "F"
  elif x == "Green":
        y = "R"
  elif x ==  "Blue":
        y = "L"
  elif x == "Yellow":
        y = "U"
  elif x == "Orange":
        y = "B"
  elif x == "White":
        y = "D"
  return y

class SerialPort:
    message = ''
    data = ''
    def __init__(self, port, buand):
        super(SerialPort, self).__init__()
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self,x,y):
        m = bytes.fromhex(x)  # 发送的数据
        n = bytes.fromhex(y)  # 发送的数据
        self.port.write(m)  # 串口写数
        print('You Send Data:', m)
        time.sleep(0.1)
        self.port.write(n)
        print('You Send Data:', n)
        return;
    def send_data2(self,x):
        m = bytes.fromhex(x)  # 发送的数据
        self.port.write(m)  # 串口写数
        print('You Send Data:', m)
        return;
    def send_data1(self,x):
        self.port.write(bytes(x, encoding='utf-8'))
        print('You Send Data:', x)
        return;

    def read_data(self):
        global turn_flag
        global result
        while True:
            time.sleep(5)
            count = self.port.inWaiting()
            if count > 0:
             self.data = str(binascii.b2a_hex(self.port.read(count )))[2:-1]
            if (self.data == 'fea1'):
                turn_flag = 1
                print('receive data is :', self.data)
            elif (self.data == 'fea2'):
                turn_flag = 1
                print('receive data is :', self.data)
            elif (self.data == 'fea3'):
                turn_flag = 1
                print('receive data is :', self.data)
            elif (self.data == 'fea4'):
                turn_flag = 1
                print('receive data is :', self.data)
            elif (self.data == 'fea5'):
                turn_flag = 1
                print('receive data is :', self.data)
            elif (self.data == 'fea6'):
                turn_flag = 1
                print('receive data is :', self.data)
            elif (self.data == 'fea7'):
                print('receive data is :', self.data)
                mSerial.send_data('FE', 'AA')
                turn_flag = 8
                if result != 0:
                 mSerial.send_data1(result)
                 time.sleep(0.1)
                 mSerial.send_data2('8A')  # 串口写数
            elif(self.data == 'feaa'):
                time_end = time.time()
                print('复原用时', time_end - time_start, 's')
                break

def colorre( ):
 color_list = []
 l1 = []
 l2 = []
 six = []
 count = 0
 flag = 0
 global turn_flag
 global result
 while True:
    ret, frame = vs.read()
    frame = contrast_brightness_image(frame, 0.8, 0.5)

    for x, y in stickers["main"]:
        cv2.rectangle(frame, (x, y), (x + 20, y + 20), (0, 0, 255), 1)

    frame_1 = frame[150:170, 260:280]
    frame_2 = frame[150:170, 330:350]
    frame_3 = frame[150:170, 390:410]

    frame_4 = frame[216:236, 260:280]
    frame_5 = frame[216:236, 330:350]
    frame_6 = frame[216:236, 390:410]

    frame_7 = frame[280:300, 260:280]
    frame_8 = frame[280:300, 330:350]
    frame_9 = frame[280:300, 390:410]

    res = color_recognizer.color_recognizer(cv2.resize(frame_1, (64, 36)))
    cv2.rectangle(frame, (262, 152), (278, 168), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_2, (64, 36)))
    cv2.rectangle(frame, (332, 152), (348, 168), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_3, (64, 36)))
    cv2.rectangle(frame, (392, 152), (408, 168), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_4, (64, 36)))
    cv2.rectangle(frame, (262, 218), (278, 234), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_5, (64, 36)))
    cv2.rectangle(frame, (332, 218), (348, 234), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_6, (64, 36)))
    cv2.rectangle(frame, (392, 218), (408, 234), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_7, (64, 36)))
    cv2.rectangle(frame, (262, 282), (278, 298), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_8, (64, 36)))
    cv2.rectangle(frame, (332, 282), (348, 298), color[res], -1)
    color_list.append(change(res))

    res = color_recognizer.color_recognizer(cv2.resize(frame_9, (64, 36)))
    cv2.rectangle(frame, (392, 282), (408, 298), color[res], -1)
    color_list.append(change(res))

    if count % 10 == 0:
        l1 = color_list[-9:]
    if count % 20 == 0:
        l2 = color_list[-9:]
        str1 = ''.join(l2)
    key = cv2.waitKey(1)
    if l1 == l2:
        if turn_flag == 1:
            print("________________________")
            print(str1)
            six.append(str1)
            color_list = []
            turn_flag = 0
            flag += 1
            if flag == 1:
                mSerial.send_data('FE', 'A2')
            elif flag == 2:
                mSerial.send_data('FE', 'A3')
            elif flag == 3:
                mSerial.send_data('FE', 'A4')
            elif flag == 4:
                mSerial.send_data('FE', 'A5')
            elif flag == 5:
                mSerial.send_data('FE', 'A6')
            elif flag == 6:
                mSerial.send_data('FE', 'A7')
    count += 1

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

    if  turn_flag == 8:
        result =''.join(six)
        str_F = result[0:9]
        str_D = result[9:18]
        str_B = result[18:27]
        str_U = result[27:36]
        str_L = result[36:45]
        str_R = result[45:54]
        str_x = str_B[::-1]
        str_b = str_x
        get_str = str_U + str_R + str_F + str_D + str_L + str_b
        print('当前颜色:' + get_str)
        solve_str = kociemba.solve(get_str)
        list = []
        list1 = solve_str.split()
        for x in list1:
            if x == "F":
                list.append("F1")
            elif x == "B":
                list.append("B1")
            elif x == "L":
                list.append("L1")
            elif x == "R":
                list.append("R1")
            elif x == "U":
                list.append("U1")
            elif x == "D":
                list.append("D1")
            elif x == "F'":
                list.append("F3")
            elif x == "B'":
                list.append("B3")
            elif x == "L'":
                list.append("L3")
            elif x == "R'":
                list.append("R3")
            elif x == "U'":
                list.append("U3")
            elif x == "D'":
                list.append("D3")
            else:
                list.append(x)
        result = "".join(list)
        break

if __name__=='__main__':
    serialPort = "COM7"  # 串口
    baudRate = 115200  # 波特率
    mSerial = SerialPort(serialPort, baudRate)
    t1 = threading.Thread(target=mSerial.read_data)
    t2 = threading.Thread(target=colorre)
    t1.start()
    t2.start()
    print('串口已打开')
    mSerial.send_data('FE', 'A1')
    time_start = time.time()