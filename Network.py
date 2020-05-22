#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

#from netifaces import interfaces
#import winreg as wr
import wmi
import platform
#定义获取Windows系统网卡接口的在注册表的键值的函数

class Network(object):

    def __init__(self):
        self.network_info = []

    def get_info(self):
        if platform.system().lower() == "windows":
            return self.win_network_info()
        else:
            return self.linux_network_info()
    #这种方法只能获取到IP，MAC地址之类的，无法获取DNS之类的，改用WMI
    # def win_network_info(self):
    #     #获取所有网络接口卡的键值
    #     id = interfaces()
    #     #存放网卡键值与键值名称的字典
    #     key_name = {}
    #     try:
    #         #建立链接注册表，"HKEY_LOCAL_MACHINE"，None表示本地计算机
    #         reg = wr.ConnectRegistry(None,wr.HKEY_LOCAL_MACHINE)
    #         # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'，固定的
    #         reg_key = wr.OpenKey(reg , r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    #     except :
    #         return ('路径出错或者其他问题，请仔细检查')

    #     for i in id:
    #         try:
    #             #尝试读取每一个网卡键值下对应的Name
    #             reg_subkey = wr.OpenKey(reg_key , i + r'\Connection')
    #             #如果存在Name，写入key_name字典
    #             key_name[wr.QueryValueEx(reg_subkey , 'Name')[0]] = i
    #             # print(wr.QueryValueEx(reg_subkey , 'Name')[0])
    #         except FileNotFoundError:
    #             pass
    #     # print('所有接口信息字典列表： ' + str(key_name) + '\n')
    #     return key_name
    def win_network_info(self):
        wmiService = wmi.WMI ()
        colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
        if len(colNicConfigs) >= 1:
            for item in colNicConfigs:
                attr_dic={}
                attr_dic["Device"] = item.Caption
                attr_dic["Gateway"] = item.DefaultIPGateway
                attr_dic["DNS"] = item.DNSServerSearchOrder
                attr_dic["IP"] = item.IPAddress
                attr_dic["MAC"] = item.MACAddress
                attr_dic["DHCPEnabled"] = item.DHCPEnabled
                attr_dic["DHCPServer"] = item.DHCPServer
                attr_dic["IPSubnet"] = item.IPSubnet
                self.network_info.append(attr_dic)
        else:
            print("Not Device Found")
        return self.network_info

    def linux_network_info(self):
        return []