# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socks52.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 807)
        Form.setMinimumSize(QtCore.QSize(750, 0))
        Form.setMaximumSize(QtCore.QSize(750, 850))
        self.GetInfo = QtWidgets.QPushButton(Form)
        self.GetInfo.setGeometry(QtCore.QRect(20, 10, 160, 160))
        self.GetInfo.setAutoFillBackground(False)
        self.GetInfo.setStyleSheet("background: transparent")
        self.GetInfo.setText("")
        self.GetInfo.setIconSize(QtCore.QSize(160, 160))
        self.GetInfo.setCheckable(True)
        self.GetInfo.setChecked(False)
        self.GetInfo.setFlat(False)
        self.GetInfo.setObjectName("GetInfo")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 520, 691, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 390, 691, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.proxy = QtWidgets.QComboBox(self.layoutWidget)
        self.proxy.setObjectName("proxy")
        self.proxy.addItem("")
        self.proxy.addItem("")
        self.horizontalLayout_4.addWidget(self.proxy)
        self.port = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setMaximumSize(QtCore.QSize(87, 30))
        self.port.setObjectName("port")
        self.horizontalLayout_4.addWidget(self.port)
        self.dect = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dect.setFont(font)
        self.dect.setObjectName("dect")
        self.horizontalLayout_4.addWidget(self.dect)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.start = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.horizontalLayout_4.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.horizontalLayout_4.addWidget(self.stop)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 200, 481, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.IP1 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP1.sizePolicy().hasHeightForWidth())
        self.IP1.setSizePolicy(sizePolicy)
        self.IP1.setMinimumSize(QtCore.QSize(0, 0))
        self.IP1.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.IP1.setFont(font)
        self.IP1.setFrame(False)
        self.IP1.setObjectName("IP1")
        self.horizontalLayout.addWidget(self.IP1)
        self.IP_dot1 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_dot1.sizePolicy().hasHeightForWidth())
        self.IP_dot1.setSizePolicy(sizePolicy)
        self.IP_dot1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.IP_dot1.setFont(font)
        self.IP_dot1.setAutoFillBackground(False)
        self.IP_dot1.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.IP_dot1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.IP_dot1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.IP_dot1.setTextFormat(QtCore.Qt.AutoText)
        self.IP_dot1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.IP_dot1.setWordWrap(False)
        self.IP_dot1.setObjectName("IP_dot1")
        self.horizontalLayout.addWidget(self.IP_dot1)
        self.IP2 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP2.sizePolicy().hasHeightForWidth())
        self.IP2.setSizePolicy(sizePolicy)
        self.IP2.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.IP2.setFont(font)
        self.IP2.setFrame(False)
        self.IP2.setObjectName("IP2")
        self.horizontalLayout.addWidget(self.IP2)
        self.IP_dot2 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_dot2.sizePolicy().hasHeightForWidth())
        self.IP_dot2.setSizePolicy(sizePolicy)
        self.IP_dot2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.IP_dot2.setFont(font)
        self.IP_dot2.setAutoFillBackground(False)
        self.IP_dot2.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.IP_dot2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.IP_dot2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.IP_dot2.setTextFormat(QtCore.Qt.AutoText)
        self.IP_dot2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.IP_dot2.setWordWrap(False)
        self.IP_dot2.setObjectName("IP_dot2")
        self.horizontalLayout.addWidget(self.IP_dot2)
        self.IP3 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP3.sizePolicy().hasHeightForWidth())
        self.IP3.setSizePolicy(sizePolicy)
        self.IP3.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.IP3.setFont(font)
        self.IP3.setFrame(False)
        self.IP3.setObjectName("IP3")
        self.horizontalLayout.addWidget(self.IP3)
        self.IP_dot3 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_dot3.sizePolicy().hasHeightForWidth())
        self.IP_dot3.setSizePolicy(sizePolicy)
        self.IP_dot3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.IP_dot3.setFont(font)
        self.IP_dot3.setAutoFillBackground(False)
        self.IP_dot3.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.IP_dot3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.IP_dot3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.IP_dot3.setTextFormat(QtCore.Qt.AutoText)
        self.IP_dot3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.IP_dot3.setWordWrap(False)
        self.IP_dot3.setObjectName("IP_dot3")
        self.horizontalLayout.addWidget(self.IP_dot3)
        self.IP4 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP4.sizePolicy().hasHeightForWidth())
        self.IP4.setSizePolicy(sizePolicy)
        self.IP4.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.IP4.setFont(font)
        self.IP4.setFrame(False)
        self.IP4.setObjectName("IP4")
        self.horizontalLayout.addWidget(self.IP4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.GW1 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW1.sizePolicy().hasHeightForWidth())
        self.GW1.setSizePolicy(sizePolicy)
        self.GW1.setMinimumSize(QtCore.QSize(0, 0))
        self.GW1.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.GW1.setFont(font)
        self.GW1.setFrame(False)
        self.GW1.setObjectName("GW1")
        self.horizontalLayout_2.addWidget(self.GW1)
        self.GW_dot1 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW_dot1.sizePolicy().hasHeightForWidth())
        self.GW_dot1.setSizePolicy(sizePolicy)
        self.GW_dot1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GW_dot1.setFont(font)
        self.GW_dot1.setAutoFillBackground(False)
        self.GW_dot1.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.GW_dot1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GW_dot1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.GW_dot1.setTextFormat(QtCore.Qt.AutoText)
        self.GW_dot1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.GW_dot1.setWordWrap(False)
        self.GW_dot1.setObjectName("GW_dot1")
        self.horizontalLayout_2.addWidget(self.GW_dot1)
        self.GW2 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW2.sizePolicy().hasHeightForWidth())
        self.GW2.setSizePolicy(sizePolicy)
        self.GW2.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.GW2.setFont(font)
        self.GW2.setFrame(False)
        self.GW2.setObjectName("GW2")
        self.horizontalLayout_2.addWidget(self.GW2)
        self.GW_dot2 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW_dot2.sizePolicy().hasHeightForWidth())
        self.GW_dot2.setSizePolicy(sizePolicy)
        self.GW_dot2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GW_dot2.setFont(font)
        self.GW_dot2.setAutoFillBackground(False)
        self.GW_dot2.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.GW_dot2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GW_dot2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.GW_dot2.setTextFormat(QtCore.Qt.AutoText)
        self.GW_dot2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.GW_dot2.setWordWrap(False)
        self.GW_dot2.setObjectName("GW_dot2")
        self.horizontalLayout_2.addWidget(self.GW_dot2)
        self.GW3 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW3.sizePolicy().hasHeightForWidth())
        self.GW3.setSizePolicy(sizePolicy)
        self.GW3.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.GW3.setFont(font)
        self.GW3.setFrame(False)
        self.GW3.setObjectName("GW3")
        self.horizontalLayout_2.addWidget(self.GW3)
        self.GW_dot3 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW_dot3.sizePolicy().hasHeightForWidth())
        self.GW_dot3.setSizePolicy(sizePolicy)
        self.GW_dot3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GW_dot3.setFont(font)
        self.GW_dot3.setAutoFillBackground(False)
        self.GW_dot3.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.GW_dot3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GW_dot3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.GW_dot3.setTextFormat(QtCore.Qt.AutoText)
        self.GW_dot3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.GW_dot3.setWordWrap(False)
        self.GW_dot3.setObjectName("GW_dot3")
        self.horizontalLayout_2.addWidget(self.GW_dot3)
        self.GW4 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW4.sizePolicy().hasHeightForWidth())
        self.GW4.setSizePolicy(sizePolicy)
        self.GW4.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.GW4.setFont(font)
        self.GW4.setFrame(False)
        self.GW4.setObjectName("GW4")
        self.horizontalLayout_2.addWidget(self.GW4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.DNS1 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS1.sizePolicy().hasHeightForWidth())
        self.DNS1.setSizePolicy(sizePolicy)
        self.DNS1.setMinimumSize(QtCore.QSize(0, 0))
        self.DNS1.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DNS1.setFont(font)
        self.DNS1.setFrame(False)
        self.DNS1.setObjectName("DNS1")
        self.horizontalLayout_3.addWidget(self.DNS1)
        self.DNS_dot1 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS_dot1.sizePolicy().hasHeightForWidth())
        self.DNS_dot1.setSizePolicy(sizePolicy)
        self.DNS_dot1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DNS_dot1.setFont(font)
        self.DNS_dot1.setAutoFillBackground(False)
        self.DNS_dot1.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.DNS_dot1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DNS_dot1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DNS_dot1.setTextFormat(QtCore.Qt.AutoText)
        self.DNS_dot1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.DNS_dot1.setWordWrap(False)
        self.DNS_dot1.setObjectName("DNS_dot1")
        self.horizontalLayout_3.addWidget(self.DNS_dot1)
        self.DNS2 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS2.sizePolicy().hasHeightForWidth())
        self.DNS2.setSizePolicy(sizePolicy)
        self.DNS2.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DNS2.setFont(font)
        self.DNS2.setFrame(False)
        self.DNS2.setObjectName("DNS2")
        self.horizontalLayout_3.addWidget(self.DNS2)
        self.DNS_dot2 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS_dot2.sizePolicy().hasHeightForWidth())
        self.DNS_dot2.setSizePolicy(sizePolicy)
        self.DNS_dot2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DNS_dot2.setFont(font)
        self.DNS_dot2.setAutoFillBackground(False)
        self.DNS_dot2.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.DNS_dot2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DNS_dot2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DNS_dot2.setTextFormat(QtCore.Qt.AutoText)
        self.DNS_dot2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.DNS_dot2.setWordWrap(False)
        self.DNS_dot2.setObjectName("DNS_dot2")
        self.horizontalLayout_3.addWidget(self.DNS_dot2)
        self.DNS3 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS3.sizePolicy().hasHeightForWidth())
        self.DNS3.setSizePolicy(sizePolicy)
        self.DNS3.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DNS3.setFont(font)
        self.DNS3.setFrame(False)
        self.DNS3.setObjectName("DNS3")
        self.horizontalLayout_3.addWidget(self.DNS3)
        self.DNS_dot3 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS_dot3.sizePolicy().hasHeightForWidth())
        self.DNS_dot3.setSizePolicy(sizePolicy)
        self.DNS_dot3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DNS_dot3.setFont(font)
        self.DNS_dot3.setAutoFillBackground(False)
        self.DNS_dot3.setStyleSheet("background:rgb(255, 255, 255)\n"
"")
        self.DNS_dot3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DNS_dot3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DNS_dot3.setTextFormat(QtCore.Qt.AutoText)
        self.DNS_dot3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.DNS_dot3.setWordWrap(False)
        self.DNS_dot3.setObjectName("DNS_dot3")
        self.horizontalLayout_3.addWidget(self.DNS_dot3)
        self.DNS4 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DNS4.sizePolicy().hasHeightForWidth())
        self.DNS4.setSizePolicy(sizePolicy)
        self.DNS4.setMaximumSize(QtCore.QSize(87, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DNS4.setFont(font)
        self.DNS4.setFrame(False)
        self.DNS4.setObjectName("DNS4")
        self.horizontalLayout_3.addWidget(self.DNS4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.wired = QtWidgets.QPushButton(Form)
        self.wired.setGeometry(QtCore.QRect(330, 20, 130, 132))
        self.wired.setAutoFillBackground(False)
        self.wired.setStyleSheet("background: transparent")
        self.wired.setText("")
        self.wired.setIconSize(QtCore.QSize(160, 160))
        self.wired.setCheckable(True)
        self.wired.setChecked(False)
        self.wired.setFlat(False)
        self.wired.setObjectName("wired")
        self.wifi = QtWidgets.QPushButton(Form)
        self.wifi.setGeometry(QtCore.QRect(560, 20, 130, 132))
        self.wifi.setAutoFillBackground(False)
        self.wifi.setStyleSheet("background: transparent")
        self.wifi.setText("")
        self.wifi.setIconSize(QtCore.QSize(160, 160))
        self.wifi.setCheckable(True)
        self.wifi.setChecked(False)
        self.wifi.setFlat(False)
        self.wifi.setObjectName("wifi")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(600, 760, 112, 34))
        self.clear.setObjectName("clear")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 171, 151))
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 350, 61, 31))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 61, 31))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Network"))
        self.proxy.setItemText(0, _translate("Form", "socks5"))
        self.proxy.setItemText(1, _translate("Form", "https/http"))
        self.dect.setText(_translate("Form", "dect"))
        self.start.setText(_translate("Form", "start"))
        self.stop.setText(_translate("Form", "stop"))
        self.label.setText(_translate("Form", "IP:"))
        self.IP1.setText(_translate("Form", "0"))
        self.IP_dot1.setText(_translate("Form", "."))
        self.IP2.setText(_translate("Form", "0"))
        self.IP_dot2.setText(_translate("Form", "."))
        self.IP3.setText(_translate("Form", "0"))
        self.IP_dot3.setText(_translate("Form", "."))
        self.IP4.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "GW:"))
        self.GW1.setText(_translate("Form", "0"))
        self.GW_dot1.setText(_translate("Form", "."))
        self.GW2.setText(_translate("Form", "0"))
        self.GW_dot2.setText(_translate("Form", "."))
        self.GW3.setText(_translate("Form", "0"))
        self.GW_dot3.setText(_translate("Form", "."))
        self.GW4.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", "DNS:"))
        self.DNS1.setText(_translate("Form", "0"))
        self.DNS_dot1.setText(_translate("Form", "."))
        self.DNS2.setText(_translate("Form", "0"))
        self.DNS_dot2.setText(_translate("Form", "."))
        self.DNS3.setText(_translate("Form", "0"))
        self.DNS_dot3.setText(_translate("Form", "."))
        self.DNS4.setText(_translate("Form", "0"))
        self.clear.setText(_translate("Form", "clear"))
        self.label_3.setText(_translate("Form", "网卡信息"))
        self.label_4.setText(_translate("Form", "模式1"))
        self.label_5.setText(_translate("Form", "模式2"))
