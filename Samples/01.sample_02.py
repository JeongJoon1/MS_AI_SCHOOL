from email.mime import application
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from os import link
from pyexpat import model
import socket
from ssl import SSLSession

in_addr = socket.gethostbyname(socket.gethostname())   
# 서버의이름(hostname) / gethostname = 내 pc의 이름 / gethostbyname = 이름가지고 pc의 ip adress를 확인

print(in_addr)   # -> 내 ip adress : 10.104.196.51



# 7 layers of the osi model
    # 7.application : http, 보안탐지
    # 6.presentation : email protocol
    # 5.Session
    # 4.transport  : TCP - 데이터 어떻게 컨트롤 할건지
    # 3.NETWORK    : IP - 데이터 보내기위한 패키징방법
    #                ip adress = 8비트*4자리(32비트)=2의34승=46 => IPv4 / IPv6 = 8비트 * 6
    # 2.data link
    # 1.physical 물리계층