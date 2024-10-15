#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 19:04:55
import wave
import requests
import time
import base64
from pyaudio import PyAudio, paInt16
import webbrowser
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import pyautogui
from entity.VoiceInteraction import VoiceAction
import json
import jsonpickle

framerate = 16000  # 采样率
num_samples = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = 'speech.wav'

base_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"

APPID = 115593352

APIKey = 'hsNlfxLw6lq3zVz9kKOhn9c8'
SecretKey = 'jeo4zKQclqCZpnEWMEqLx6bueiPJRH1r'

# 语言模型 ， 可以修改为其它语言模型测试，如远场普通话19362
DEV_PID = 15372


HOST = base_url % (APIKey, SecretKey)


def getToken(host):
    res = requests.post(host)
    return res.json()['access_token']


def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def my_record(show_label=None):
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=channels,
                     rate=framerate, input=True, frames_per_buffer=num_samples)
    my_buf = []
    # count = 0
    t = time.time()
    show_label.setText('正在录音...')

    while time.time() < t + 3:  # 秒de
        string_audio_data = stream.read(num_samples)
        my_buf.append(string_audio_data)
    show_label.setText('录音结束.')
    save_wave_file(FILEPATH, my_buf)
    stream.close()


def get_audio(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data


def speech2text(speech_data, token, show_label, dev_pid=1537):
    FORMAT = 'wav'
    RATE = '16000'
    CHANNEL = 1
    CUID = '*******'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')

    data = {
        'format': FORMAT,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': token,
        'dev_pid': dev_pid
    }
    url = 'https://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}
    # r=requests.post(url,data=json.dumps(data),headers=headers)
    show_label.setText('正在识别...')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    if 'result' in Result:
        return Result['result'][0]
    else:
        return Result


def load_software_1(voice_action):
    """
    从 JSON 文件中加载 VoiceAction 实例
    """
    file_path = "./data2/" + voice_action.name + ".json"
    try:
        with open(file_path, "r", encoding="utf-8") as in_file:
            json_data = in_file.read()
            voice_action = VoiceAction.from_json(json_data)
            return voice_action
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return VoiceAction("", "", "", "", "")


def compare_and_open_website(voice_action, judge_data, result_data):
        """根据 JSON 数据中的 judge 数据与 result 进行对比，并在相等时打开对应网站"""
        if judge_data == result_data:
            # 解析 JSON 数据并获取 keys
            json_data = voice_action.to_json()
            data = json.loads(json_data)
            if 'keys' in data:
                website = data['keys']
                webbrowser.open(website)
                print("条件满足，已打开网站")
            else:
                print("JSON数据中没有找到 'url' 键")
        else:
            print("条件不满足，不打开网站")


VOICE_ACTION = VoiceAction("", "", "", "", "")
VOICE_ACTION = load_software_1(VOICE_ACTION)

def run(show_label):
        my_record(show_label)
        TOKEN = getToken(HOST)
        speech = get_audio(FILEPATH)
        result = speech2text(speech, TOKEN, show_label, 1537)
        show_label.setText(result)

        global VOICE_ACTION
        load_software_1(VOICE_ACTION)
        action = VoiceAction('', '', '', '', '')
        for i in range(len(VOICE_ACTION.actions)):
            action = VOICE_ACTION.actions[i]
            compare_and_open_website(action, action.judge, result)
        if result == '鼠标':
            pyautogui.click()
        if result == '截图。':
            pyautogui.screenshot('screenshot.png')





