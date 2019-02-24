from flask import Flask, jsonify, request
import os
import json
import subprocess
import random
import librosa
import boto3

app = Flask(__name__)

def danceCreaterMain():
    bgm = ['music/128_1.mp3', 'music/128_2.mp3']
    filename = str(bgm[random.randint(0, 1)])
    #ランダムで曲を見ている！

    #bpm, time = bpmTimeGetter(filename)
    bpm = 128
    time = 32
    # print(bpm)
    # print(time)

    danceMaker(filename, time, bpm)

    return "https://s3.amazonaws.com/rechack-dance/output.mp4"

def bpmTimeGetter(filename):
    # bpm、およびTime(音楽の時間)を計測、返り値は[bpm,time]
    y, sr = librosa.load(filename)
    bpm, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    bpm = int(bpm)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return (bpm, int(beat_times[-1]))


def danceMaker(filename, time, bpm):
    num = 1
    limit = int(time / 4 - 2)

    combo = 'movie/a1.mp4 -i '

    for i in range(limit):
        num += 1
        combo += 'movie/a' + str(random.randint(2, 7)) + '.mp4 -i '

    combo += 'movie/a8.mp4 '
    num += 1

    cmd = 'ffmpeg -y -i ' + combo + '-strict ' + str(num) + ' -filter_complex "concat=n=' + str(
        num) + ':v=1:a=1 " convideo.mp4'
    # ffmpeg -y -i movie/a1.mp4 -strict + 2 + ' -filter_complex "concat=n=2:v=1:a=1" convideo.mp4
    res1 = subprocess.call(cmd, shell=True)
    print(res1)

    cmd2 = 'ffmpeg -y -i convideo.mp4 -i ' + filename + ' -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 /tmp/output.mp4'

    res2 = subprocess.call(cmd2, shell=True)

    bucket_name = "rechack-dance"

    s3 = boto3.client('s3', 'ap-northeast-1', aws_access_key_id="AKIAJPHLEFPV2NL236UQ", aws_secret_access_key="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")

    s3.upload_file('/tmp/output.mp4', bucket_name, 'output.mp4', ExtraArgs={"ContentType": "mp4", 'ACL':'public-read'})






@app.route('/api/test', methods=['POST'])
def api_test():
    print("api")
    deta = request.get_json()
    level = deta["level"]
    genre = deta["genre"]
    name = deta["name"]
    #res = {"url": music(level, genre, bpm=100)}
    #return jsonify(res)
    url = danceCreaterMain()


    data = {"url":url}
    return jsonify(data)
def music(level, genre, bpm):
    if level==1:
        if genre==pop:
            if 80<=bpm<100:
                return ["a1", "a2", "a3", "a4"]
            elif 60<=bpm<80:
                return ["a1", "a2", "a3", "a4"]
            elif bpm<60:
                return ["a1", "a2", "a3", "a4"]
            elif 100<=bpm:
                return ["a1", "a2", "a3", "a4"]
        if genre==edm:
            if bpm==128:
                return ["a1", "a2", "a3", "a4"]
            elif bpm<128:
                return ["a1", "a2", "a3", "a4"]
            elif bpm>128:
                return ["a1", "a2", "a3", "a4"]
        if genre==rock:
            if 60<bpm:
                return ["a1", "a2", "a3", "a4"]
            elif 60<=bpm<80:
                return ["a1", "a2", "a3", "a4"]
            elif 80<=bpm<100:
                return ["a1", "a2", "a3", "a4"]
            elif 100<=bpm<120:
                return ["a1", "a2", "a3", "a4"]
            elif 120<=bpm:
                return ["a1", "a2", "a3", "a4"]
    if level==2:
        if genre==pop:
            if 80<=bpm<100:
                return ["a1", "a2", "a3", "a4"]
            elif 60<=bpm<80:
                return ["a1", "a2", "a3", "a4"]
            elif bpm<60:
                return ["a1", "a2", "a3", "a4"]
            elif 100<=bpm:
                return ["a1", "a2", "a3", "a4"]
        if genre==edm:
            if bpm==128:
                return ["a1", "a2", "a3", "a4"]
            elif bpm<128:
                return ["a1", "a2", "a3", "a4"]
            elif bpm>128:
                return ["a1", "a2", "a3", "a4"]
        if genre==rock:
            if 60<bpm:
                return ["a1", "a2", "a3", "a4"]
            elif 60<=bpm<80:
                return ["a1", "a2", "a3", "a4"]
            elif 80<=bpm<100:
                return ["a1", "a2", "a3", "a4"]
            elif 100<=bpm<120:
                return ["a1", "a2", "a3", "a4"]
            elif 120<=bpm:
                return ["a1", "a2", "a3", "a4"]
    if level==3:
        if genre==pop:
            if 80<=bpm<100:
                return ["a1", "a2", "a3", "a4"]
            elif 60<=bpm<80:
                return ["a1", "a2", "a3", "a4"]
            elif bpm<60:
                return ["a1", "a2", "a3", "a4"]
            elif 100<=bpm:
                return ["a1", "a2", "a3", "a4"]
        if genre==edm:
            if bpm==128:
                return ["a1", "a2", "a3", "a4"]
            elif bpm<128:
                return ["a1", "a2", "a3", "a4"]
            elif bpm>128:
                return ["a1", "a2", "a3", "a4"]
        if genre==rock:
            if 60<bpm:
                return ["a1", "a2", "a3", "a4"]
            elif 60<=bpm<80:
                return ["a1", "a2", "a3", "a4"]
            elif 80<=bpm<100:
                return ["a1", "a2", "a3", "a4"]
            elif 100<=bpm<120:
                return ["a1", "a2", "a3", "a4"]
            elif 120<=bpm:
                return ["a1", "a2", "a3", "a4"]
if __name__ == '__main__':
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
