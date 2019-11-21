__author__ = 'shikun'
import math
from math import floor
import subprocess
import os
import re


class ApkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath

    # 得到app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkpath) / (1024 * 1000))
        return str(size) + "M"

    # 得到版本
    def get_apk_version(self):
        # cmd = "aapt dump badging " + self.apkpath + " | grep versionName"
        cmd = "aapt dump badging " + self.apkpath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            # result = output.split()[3].decode()[12:]
            result = re.findall(re.compile(r"versionName='([0-9.]+?)'"), str(output, encoding="utf-8"))[0]
        return result

    # 得到应用名字
    def get_apk_name(self):
        # cmd = "aapt dump badging " + self.apkpath + " | grep application-label: "
        cmd = "aapt dump badging " + self.apkpath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            # result = output.split()[0].decode()[18:]
            result = re.findall(re.compile(r"application-label:'([A-Za-z.]+?)'"), str(output, encoding="utf-8"))[0]
        return result

    # 得到包名
    def get_apk_pkg(self):
        # cmd = "aapt dump badging " + self.apkpath + " | grep package:"    #windows cmd不支持grep
        cmd = "aapt dump badging " + self.apkpath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            # result = output.split()[1].decode()[6:-1]
            result = re.findall(re.compile(r"package: name='([A-Za-z.]+?)'"), str(output, encoding="utf-8"))[0]
        return result

    # 得到启动类
    def get_apk_activity(self):
        # cmd = "aapt dump badging " + self.apkpath + " | grep launchable-activity:"
        cmd = "aapt dump badging " + self.apkpath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            # result = output.split()[1].decode()[6:-1]
            page = self.get_apk_pkg()
            activity = re.findall(re.compile(r"launchable-activity: name='([A-Za-z.]+?)'"), str(output, encoding="utf-8"))[0]
            result = activity.replace(page, "")
        return result


if __name__ == '__main__':
    ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_pkg()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_version()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_name()
    ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
