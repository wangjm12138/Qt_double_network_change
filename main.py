import os
import re
import sys
import time
import ctypes
import signal
import socket
import platform
import subprocess
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont,QPainter,QIntValidator
from PyQt5.QtCore import QTimer,QThread
from PyQt5.QtGui import QIcon
from De_socks5_ui import Ui_Form
from Network import Network
from queue import Queue

from PyQt5.QtCore import pyqtSignal

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# class Socket_Client_Thread(QThread):

#     def __init__(self, input_queue,out_queue,parent=None):
#         super(Socket_Client_Thread, self).__init__(parent)
#         self.input_queue = input_queue
#         self.out_queue = out_queue
#         self.send_on = False

#     def run(self):
#         while self.send_on:
#             if self.out_queue.empty() == False:
#                 self.client = socket.socket()
#                 self.client.connect(('127.0.0.1',1081))
#                 self.client.send(self.out_queue.get().encode('utf-8'))
#                 self.data = self.client.recv(1024)
#                 print(self.data)
#                #print("empty")
#                 self.send_on = False
#                 #pass
#             else:
#                 pass


class My_socks(QWidget):
    
    def __init__(self):
        super().__init__()
        self.wired_enable = False
        self.wifi_enable = False
        self.wired_info = None
        self.wifi_info = None
        self.IP = None
        self.DNS = None
        self.GW = None
        self.PORT = None
        self.socks5 = None
        self.count = 0

        self.ui = Ui_Form()
        ##server for behind process
        #self.input_queue = Queue()
        #self.out_queue = Queue()
        #self.socket_send = Socket_Client_Thread(self.input_queue,self.out_queue)
        #第一次调用是需要的，因为要让isfinish设置默认值
        #elf.socket_send.start()

        self.ui.setupUi(self)
        self.setWindowTitle('MyLogo')
        self.setWindowIcon(QIcon("./img/window.jpg"))


        self.ip_list = [self.ui.IP1, self.ui.IP2, self.ui.IP3, self.ui.IP4]
        self.dns_list = [self.ui.DNS1, self.ui.DNS2, self.ui.DNS3, self.ui.DNS4]
        self.gw_list = [self.ui.GW1, self.ui.GW2, self.ui.GW3, self.ui.GW4]
        self.start_stop_bn_enable(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.process_poll_check)

        Port_Intvalidator = QIntValidator()
        Port_Intvalidator.setRange(1001,65535)
        self.ui.port.setValidator(Port_Intvalidator)
        Intvalidator = QIntValidator()
        Intvalidator.setRange(0,255)
        for item in self.ip_list:
            item.setValidator(Intvalidator)
        for item in self.dns_list:
            item.setValidator(Intvalidator)
        for item in self.gw_list:
            item.setValidator(Intvalidator)

        self.ui.GetInfo.setStyleSheet("QPushButton{border-image: url(img/before.png)}")
        self.ui.wired.setStyleSheet("QPushButton{border-image: url(img/wired_before.png)}")
        self.ui.wifi.setStyleSheet("QPushButton{border-image: url(img/wifi_before.png)}")
        self.ui.GetInfo.clicked.connect(self.background_change)
        self.ui.wired.clicked.connect(self.wired_bg_change)
        self.ui.wifi.clicked.connect(self.wifi_bg_change)
        self.ui.start.clicked.connect(self.start_socks5)
        self.ui.stop.clicked.connect(self.stop_socks5)
        self.ui.dect.clicked.connect(self.port_check)
        self.ui.clear.clicked.connect(self.clear_text)

    def check_ipv4(self,items):
        m = None
        result = None
        regular = r'^(((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))\.){3}((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))$'
        pattern = re.compile(regular)
        if isinstance(items,list) or isinstance(items,tuple):
            for item in items:
                m = pattern.match(item)
                if m is not None:
                    result = item
                    break
        else:
            m = pattern.match(items)
            if m is not None:
                result = items
                
        return result


    def process_poll_check(self):
        if self.socks5 is not None:
            if self.socks5.poll() is None:
                pass
            else:
                if self.count < 5:
                    self.ui.textBrowser.append("Socks5 is close!!!")
                    self.count = self.count + 1
                else:
                    self.ui.textBrowser.append("Max count=5 is reach")
                    self.stopTimer()


    def port_check(self):
        try:
            self.PORT = int(self.ui.port.text())
        except ValueError:
            self.ui.textBrowser.append("port is not base 10")
            return False
        if self.IP is None:
            self.ui.textBrowser.append("IP is None")
            return False
        Tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            Tcp_sock.bind((self.IP,self.PORT))
            Tcp_sock.close()
            self.ui.textBrowser.append("ip %s port %s is free"%(self.IP,self.PORT))
            return True
        except OSError:
            self.ui.textBrowser.append("ip %s port %s is using!!!"%(self.IP,self.PORT))
            return False


    def startTimer(self):
        self.ui.textBrowser.append("Start Timer for check")
        self.timer.start(100)

    def stopTimer(self):
        self.ui.textBrowser.append("Stop Timer for check")
        self.timer.stop()

    def start_socks5(self):
        # if self.socket_send.isFinished():
        #     self.out_queue.queue.clear()
        #     self.out_queue.put("start")
        #     self.socket_send.send_on = True
        #     self.socket_send.start()
        self.ui.start.setEnabled(False)
        if self.port_check():
            str_cmd = "python ./socks5_main.py --dns {0} --ip {1} --port {2}"
            if self.IP is not None and self.DNS is not None and self.PORT is not None:
                cmd = str_cmd.format(self.DNS,self.IP,self.PORT)
                self.ui.textBrowser.append(cmd)
            self.socks5 = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            #self.socks5.stdin.close()
            #self.socks5.stdout.close()
            self.startTimer()
        else:
            self.ui.textBrowser.append("port is using or valid!!!")

    def stop_socks5(self):
        self.ui.start.setEnabled(True)
        self.stopTimer()
        if platform.system().lower() == "windows":
            p_socks = subprocess.Popen('netstat -aon| findstr "1080"',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            result = p_socks.stdout.readlines()
            if len(result) >0:
                result = str(result[0],encoding="utf-8").strip('\r\n')
                s_pid = result.split()[-1]
                handle = ctypes.windll.kernel32.OpenProcess(1, False, int(s_pid)) # 同上（pid类型为int！）
                ctypes.windll.kernel32.TerminateProcess(handle, -1)
                ctypes.windll.kernel32.CloseHandle(handle)
                self.ui.textBrowser.append("process %s is terminate"%(s_pid))
        else:
            if self.socks5 is not None:
                f_pid = self.socks5.pid
                os.killpg(os.getpgid(f_pid),9)
        self.socks5 = None
        #self.ui.textBrowser.append("all process in %s is terminate"%(f_pid))

    def set_value(self,item_list,value_list):
        if value_list == None:
            for item in item_list:
                item.clear()
        else:
            for i, item in enumerate(item_list):
                item.setText(value_list[i])


    def show_ip_gw_dns(self, data):
        self.IP = self.check_ipv4(data["IP"])
        self.DNS = self.check_ipv4(data["DNS"])
        self.GW = self.check_ipv4(data["Gateway"])
        if self.IP is not None:
            ip_list = self.IP.split(".")
            self.set_value(self.ip_list,ip_list)
        if self.DNS is not None:
            dns_list = self.DNS.split(".")
            self.set_value(self.dns_list,dns_list)
        if self.GW is not None:
            gw_list = self.GW.split(".")
            self.set_value(self.gw_list,gw_list)

    def clear_text(self):
        self.ui.textBrowser.clear()
        self.socks5 = subprocess.Popen("python ./test.py")

    def start_stop_bn_enable(self, Flag):
        self.ui.start.setEnabled(Flag)
        self.ui.stop.setEnabled(Flag)

    def clear_ip_dns_gw(self):
        self.set_value(self.ip_list,None)
        self.set_value(self.dns_list,None)
        self.set_value(self.gw_list,None)
        self.wired_enable = False
        self.wifi_enable = False
        self.wired_info = None
        self.wifi_info = None
        self.IP = None
        self.DNS = None
        self.GW = None
        self.PORT = None
        self.socks5 = None 

    def all_stop(self):
        self.stop_socks5()
        self.start_stop_bn_enable(False)
        self.clear_ip_dns_gw()

    def wired_bg_change(self):
        if self.wired_enable:
            self.start_stop_bn_enable(True)
            if self.ui.wired.isChecked():
                self.ui.wired.setStyleSheet("QPushButton{border-image: url(img/wired_press.png)}")
                self.show_ip_gw_dns(self.wired_info)
            else:
                #self.clear_ip_dns_gw()
                self.ui.wired.setStyleSheet("QPushButton{border-image: url(img/wired_after.png)}")

    def wifi_bg_change(self):
        if self.wifi_enable:
            self.start_stop_bn_enable(True)
            if self.ui.wifi.isChecked():
                self.ui.wifi.setStyleSheet("QPushButton{border-image: url(img/wifi_press.png)}")
                self.show_ip_gw_dns(self.wifi_info)
            else:
                #self.clear_ip_dns_gw()
                self.ui.wifi.setStyleSheet("QPushButton{border-image: url(img/wifi_after.png)}")


    #@pyqtSlot()
    def background_change(self):
        if self.ui.GetInfo.isChecked():
            self.ui.GetInfo.setStyleSheet("QPushButton{border-image: url(img/press.png)}")
            network = Network()
            result = network.get_info()
            self.network_show_control(result)
            if self.wired_enable:
                self.ui.wired.setStyleSheet("QPushButton{border-image: url(img/wired_after.png)}")
            else:
                self.ui.wired.setStyleSheet("QPushButton{border-image: url(img/wired_before.png)}")
            if self.wifi_enable:
                self.ui.wifi.setStyleSheet("QPushButton{border-image: url(img/wifi_after.png)}")
            else:
                self.ui.wifi.setStyleSheet("QPushButton{border-image: url(img/wifi_before.png)}")
            #info = {"a":"b","c":"d"}
            #self.ui.textBrowser.append(str(result))
        else:
            self.all_stop()
            self.ui.GetInfo.setStyleSheet("QPushButton{border-image: url(img/before.png)}")
            self.ui.wired.setStyleSheet("QPushButton{border-image: url(img/wired_before.png)}")
            self.ui.wifi.setStyleSheet("QPushButton{border-image: url(img/wifi_before.png)}")
            self.clean_network_info()
    
    def clean_network_info(self):
        self.wired_info = None
        self.wifi_info = None
        self.wired_enable = False
        self.wifi_enable = False

    def network_show_control(self, network_info):
        self.clean_network_info()
        if len(network_info) > 0:
            for i,item in enumerate(network_info):
                if ("Ethernet" in item["Device"] or "Realtek" in item["Device"] ) and self.wired_info is None:
                    self.wired_info = item
                    self.wired_enable = True
                if "Wireless" in item["Device"] and self.wifi_info is None:
                    self.wifi_info = item
                    self.wifi_enable = True

                self.ui.textBrowser.append("========Device%s============="%(str(i))) 
                for key,value in  item.items():
                    #print(key,value)
                    self.ui.textBrowser.append(str(key)+":"+str(value))  
            #print(self.wired_info,self.wired_enable) 
        else:
            self.ui.textBrowser.append("Not Device Found")

#    def paintEvent(self,event):
#    	qp.begin(self)
#    	g_x = self.ui.verticalLayout.geometry().x()
 #   	g_y = self.ui.verticalLayout.geometry().y()
    	#print(1111)
 #   	print(self.ui.IP1.x(),self.ui.IP1.y())
 #   	print(self.ui.IP1.x(),self.ui.IP1.y())
    	#print(222)
    	#print(g_x,g_y)
    	#qp.drawRect(self.ui.IP1.geometry().x()+g_x,self.ui.IP1.geometry().y()+g_y,381,30)
#    	qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_socks = My_socks()
    my_socks.show()
    sys.exit(app.exec_())
