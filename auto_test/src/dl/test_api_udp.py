import socket
import json
import test_api_constant
SERVER_ADDR = ''
udpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpClientSocket.settimeout(120)


def auto_test_udp_init(gateway_ip, gateway_port):
    global SERVER_ADDR
    SERVER_ADDR = (gateway_ip, gateway_port)


def auto_test_recv_data():
    try:
        rcv_data, addr = udpClientSocket.recvfrom(test_api_constant.BUF_SIZE)
    except socket.timeout:
        print("socket timeout !!!")
        return ""
    #print('recv = ', rcv_data.decode('utf-8'))
    return rcv_data


def auto_test_send_data(data):
    send_data = (json.dumps(data, default=lambda obj: obj.__dict__))
    #print(send_data)
    udpClientSocket.sendto(test_api_constant.MSG_HEAD.encode('utf-8') + send_data.encode('utf-8'), SERVER_ADDR)


def auto_test_send_json(data):
    send_data = json.dumps(data, ensure_ascii=False)
    #print(send_data)
    udpClientSocket.sendto(test_api_constant.MSG_HEAD.encode('utf-8') + send_data.encode('utf-8'), SERVER_ADDR)


def auto_test_send_class(data):
    udpClientSocket.sendto(test_api_constant.MSG_HEAD.encode('utf-8') + data.encode('utf-8'), SERVER_ADDR)
