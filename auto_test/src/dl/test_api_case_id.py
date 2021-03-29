import test_api_udp
import test_api_constant


class SidSet(object):
    def __init__(self, msg_type, command, from_role, from_account, sid, caseName):
        self.msg_type = msg_type
        self.command = command
        self.from_role = from_role
        self.from_account = from_account
        self.sid = sid
        self.caseName = caseName


def auto_test_set_sid(sid, case_name):
    sid_data = SidSet('dev_sid_set', 'control', test_api_constant.FROM_ROLE, test_api_constant.FROM_ROLE, sid, case_name)
    test_api_udp.auto_test_send_data(sid_data)
    read_data = test_api_udp.auto_test_recv_data()
    if read_data.decode('utf-8') == 'ok':
        print('*** 测试用例ID设置成功 ***')
        return 0
    else:
        return -1



