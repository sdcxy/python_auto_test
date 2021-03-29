import json
import test_api_udp


auto_test_dev_addr = ''


class DeviceInfo(object):
    def __init__(self, brand, dev_addr, dev_net_addr, dev_class_type, dev_key, dev_uptype, host_mac, riu_id):
        self.brand = brand
        self.dev_addr = dev_addr
        self.dev_net_addr = dev_net_addr
        self.dev_class_type = dev_class_type
        self.dev_key = dev_key
        self.dev_uptype = dev_uptype
        self.host_mac = host_mac
        self.riu_id = riu_id


def auto_test_control_device(dev_name):
    root = {}
    root["msg_type"] = "device_control"
    root["command"] = "control"
    root["from_role"] = "phone"
    root["from_account"] = "phone"
    root["dev_name"] = dev_name
    root["room_name"] = "默认房间"
    root["func_command"] = "on"
    root["func_value"] = ""
    root["cur_status"] = ""
    test_api_udp.auto_test_send_json(root)
    return


def auto_test_add_new_device(data):
    print("*** 新设备上报成功 ***")
    bItem = {}
    bItem["msg_type"] = "device_manager"
    bItem["from_role"] = "phone"
    bItem["from_account"] = "phone"
    bItem["command"] = "add"
    bItem["gateway_type"] = ""
    bItem["host_mac"] = data.host_mac
    bItem["room_name"] = "默认房间"
    bItem["riu_id"] = data.riu_id
    bItem["dev_uptype"] = data.dev_uptype
    bItem["dev_name"] = data.dev_addr + "_" + str(data.dev_key)
    bItem["dev_addr"] = data.dev_addr
    bItem["dev_net_addr"] = data.dev_net_addr
    bItem["dev_key"] = data.dev_key
    bItem["dev_class_type"] = data.dev_class_type
    bItem["brand_logo"] = ""
    bItem["brand"] = data.brand
    global auto_test_dev_addr
    auto_test_dev_addr = data.dev_addr
    test_api_udp.auto_test_send_json(bItem)
    return


def auto_test_wait_new_device_report(g_test_class_type):
    print('*** 等待新设备上报 ***')
    while True:
        read_data = test_api_udp.auto_test_recv_data()
        if read_data == "":
            return -1
        new_device = json.loads(read_data)
        msg_type_str = new_device["msg_type"]
        host_mac = new_device["from_account"]
        if msg_type_str != 'new_device_manager':
            continue

        obj = new_device["devices"]
        if len(obj) > 0:
            dev_class_type = obj[0]["dev_class_type"]
            if dev_class_type != g_test_class_type:
                continue
            print(len(obj))
            for i in range(len(obj)):
                dev_addr = obj[i]["dev_addr"]
                dev_net_addr = obj[i]["dev_net_addr"]
                brand = obj[i]["brand"]
                dev_key = obj[i]["dev_key"]
                dev_uptype = obj[i]["dev_uptype"]
                dev_class_type = obj[i]["dev_class_type"]
                riu_id = obj[i]["riu_id"]
                dev_info = DeviceInfo(brand, dev_addr, dev_net_addr, dev_class_type, dev_key, dev_uptype, host_mac, riu_id)
                auto_test_add_new_device(dev_info)
            return 0
    return 0


def auto_test_get_device_addr():
    return auto_test_dev_addr

