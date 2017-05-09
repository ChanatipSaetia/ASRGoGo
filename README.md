# ASRGoGo
## Requirement
python 2.7.13

tornado 4.5.1 or later

docker

## Installation
#### ASR Server
Option 1
```
docker pull sirinthra/kaldi-gstreamer-server
```
Option 2

In case you already have kaldi-gstreamer-server docker, download files in 'model' directory and place it in your 'model' directory in your kaldi-gstreamer-server 
#### Web Application
```
pip install tornado
```


## Start Application
Start kaldi gstreamer server
```
/opt/start.sh -y /opt/models/sample_nnet2.yaml
```
Start web application
```
python webCore.py
```

## Features
- 0 Set alarm: e.g. "ตั้งปลุกตอนหกโมงนะ"
- 1 Ask for current time: e.g. "ตอนนี้กี่โมงแล้ว"
- 2 Pospone the alarm: e.g. "ขอนอนต่ออีก 5 นาที"
- 3 Report task: e.g. "วันนี้มีอะไรต้องทำบ้าง"
- 4 Stop alarming with "ตื่นแล้ว"
