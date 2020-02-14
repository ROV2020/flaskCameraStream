from flask import Flask, request, render_template, Response
from .camera import Camera

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

cam1=None
cam2=None
init1=False
init2=False

@app.route('/')
def index():
    path="index.html"
    return render_template(path)

@app.route('/cams')
def cams():
    path="cams.html"
    return render_template(path)

@app.route('/testStream')
def test():
    path="testStream.html"
    return render_template(path)

@app.route('/streamCam1')
def SC1():
    cam1=Camera(0)
    init1=True
    return str(cam1.isOpened)

@app.route('/streamCam2')
def SC2():
    cam2=Camera(1)
    init2=True
    return str(cam2.isOpened)

@app.route('/watchCam1')
def WC1():
    if(init1):return Response(cam1.captureVideo())
    return "False"

@app.route('/watchCam2')
def WC2():
    if(init2):return Response(cam2.captureVideo())
    return "False"

@app.route('/stopCam1')
def stopC1():
    if(init1):return cam1.stopVideo()
    return "False"

@app.route('/stopCam2')
def stopC2():
    if(init2):return cam2.stopVideo()
    return "False"

@app.route('/resumeCam1')
def RC1():
    if(init1):return cam1.resumeVideo()
    return "False"

@app.route('/resumeCam1')
def RC2():
    if(init2):return cam2.resumeVideo()
    return "False"

@app.route('/resumeCam1')
def PC1():
    if(init1):return cam1.pauseVideo()
    return "False"

@app.route('/pauseCam2')
def PC2():
    if(init2):return cam2.pauseVideo()
    return "False"

@app.route('/listCam')
def LC():
    if(init1):return cam1.listCameras()
    return "False"

if __name__ == '__main__':
    setdb()
    app.run(host='0.0.0.0')
