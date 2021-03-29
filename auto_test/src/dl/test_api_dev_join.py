import test_api_udp
import test_api_constant


class AllowJoin(object):
    def __init__(self, msg_type, command, from_role, from_account, riu_id, brand):
        self.msg_type = msg_type
        self.command = command
        self.from_role = from_role
        self.from_account = from_account
        self.riu_id = riu_id
        self.brand = brand


def auto_test_allow_join(riu_id, cmd, brand):
    allow_data = AllowJoin('device_join_control', cmd, test_api_constant.FROM_ROLE, test_api_constant.FROM_ROLE, riu_id, brand)
    test_api_udp.auto_test_send_data(allow_data)
    return

