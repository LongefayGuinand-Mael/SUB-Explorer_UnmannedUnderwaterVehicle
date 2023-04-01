import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')
if not device_folder:
    print('Error: No DS18B20 devices found')
    exit(1)
device_folder = device_folder[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        print(temp_c)
        return temp_c
    
#while True:
#    temp = read_temp()
#    if temp:
#        print(temp)
#    time.sleep(0.5)

PAGE="""\
<html>
  <head>
    <title>Unmanned Underwater Vehicle</title>
    <style>
      /* Center the title */
      h1 {
        text-align: center;
        margin-bottom: 20px;
      }
      /* Add spacing between title and table */
      table {
        margin-top: 20px;
      }
      td {
        padding: 10px;
      }
    </style>
  </head>
  <body>
    <h1>Unmanned Underwater Vehicle</h1>
    <img src="stream.mjpg" width="1080" height="720" />
    <table>
      <tr>
        <td>Temperature:</td>
        <td>25°C</td>
      </tr>
      <tr>
        <td>Pressure:</td>
        <td>1013 hPa</td>
      </tr>
    </table>
  </body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    ThreadTemp = threading.Thread(target = read_temp, args =[])
                    ThreadTemp.start()
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

# 4 fps = 6 Mbps
#24 fps = 18 Mbps
with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    camera.rotation = 180
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()