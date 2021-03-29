import json
import test_api_udp
import test_api_constant


class SmartLinkAddManager(object):
    def __init__(self, linkage_name, conds, actions):
        self.msg_type = 'smart_linkage_manager'
        self.command = 'add'
        self.from_role = 'phone'
        self.from_account = ''
        self.linkage_name = linkage_name
        self.state = 1
        self.retrigger_time = 0
        self.conditions = '||'
        self.dev_conds = conds
        self.exe_actions = actions


class SmartLinkCond(object):
    def __init__(self, type, room_name, dev_name, scene_name, func_cmd):
        self.type = type
        self.conds = ''
        self.obj_id = 0
        self.room_name = room_name
        self.dev_name = dev_name
        self.scene_name = scene_name
        self.security_mode = ''
        self.func_cmd = func_cmd
        self.func_value = '{}'
        self.value = 0
        self.year = 0
        self.month = 0
        self.date = 0
        self.week = 0
        self.time = 0
        self.area = 0
        self.param_type = 0
        self.seq = 0


class SmartLinkActions(object):
    def __init__(self, type, room_name, dev_name, scene_name, func_cmd, func_value):
        self.type = type
        self.seq = 0
        self.obj_id = 0
        self.room_name = room_name
        self.dev_name = dev_name
        self.scene_name = scene_name
        self.func_cmd = func_cmd
        self.func_value = func_value
        self.value = 0
        self.content = ''
        self.alarm_type = 0
        self.alarm_level = 0
        self.valid = 0
        self.inter_time = 0
        self.param_type = 0

class SmartLinkageDeleteManager(object):
    def __init__(self, linkage_id):
        self.msg_type = 'smart_linkage_manager'
        self.command = 'delete'
        self.from_role = 'phone'
        self.from_account = ''
        self.linkage_id = linkage_id


def auto_test_smart_linkage_add_conds(room_name, dev_name, scene_name, func_cmd):
    cond_type = 1
    if scene_name != '':
        cond_type = 2

    cond = SmartLinkCond(cond_type, room_name, dev_name, scene_name, func_cmd)
    return cond


def auto_test_smart_linkage_add_actions(room_name, dev_name, scene_name, func_cmd):
    action_type = 1
    if scene_name != '':
        action_type = 2

    actions = SmartLinkActions(action_type, room_name, dev_name, scene_name, func_cmd, '')
    return actions


def auto_test_smart_linkage_add_manager(dev_addr, dev_class_type, room_name):

    exe_actions = []
    linkage_name = '联动+'+dev_addr

    cond = [
        auto_test_smart_linkage_add_actions(room_name, dev_addr + '_1', '', 'on').__dict__
    ]
    if dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_ONE:
        exe_actions = [
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_1', '', 'off').__dict__,
        ]
    elif dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_TWO:
        exe_actions = [
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_1', '', 'off').__dict__,
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_2', '', 'off').__dict__,
        ]
    elif dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_THREE:
        exe_actions = [
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_1', '', 'off').__dict__,
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_2', '', 'off').__dict__,
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_3', '', 'off').__dict__,
        ]
    elif dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_FOUR:
        exe_actions = [
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_1', '', 'off').__dict__,
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_2', '', 'off').__dict__,
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_3', '', 'off').__dict__,
            auto_test_smart_linkage_add_actions(room_name, dev_addr + '_4', '', 'off').__dict__,
        ]

    data = SmartLinkAddManager(linkage_name, cond, exe_actions)
    json_data = json.dumps(data.__dict__, ensure_ascii=False)
    test_api_udp.auto_test_send_class(json_data)


def auto_test_smart_linkage_delete_manager(linkage_id):
    data = SmartLinkageDeleteManager(linkage_id)
    json_data = json.dumps(data.__dict__, ensure_ascii=False)
    test_api_udp.auto_test_send_class(json_data)

