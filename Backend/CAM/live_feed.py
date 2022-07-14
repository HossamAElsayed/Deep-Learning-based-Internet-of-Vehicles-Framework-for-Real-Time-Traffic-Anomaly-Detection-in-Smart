from flask import Flask, Response
import cv2

app = Flask(__name__)
video = cv2.VideoCapture('vid1.mp4')

def make_1080p():
    video.set(3, 1920)
    video.set(4, 1080)

def make_720p():
    video.set(3, 1280)
    video.set(4, 720)

def make_480p():
    video.set(3, 640)
    video.set(4, 480)

def change_res(width, height):
    video.set(3, width)
    video.set(4, height)

@app.route('/')
def index():
    return "Default Message"

def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    make_480p()
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 80, threaded=True)


