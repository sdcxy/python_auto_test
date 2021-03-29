import json
import test_api_constant
import test_api_udp

g_test_room_name = '默认房间'


class SceneActionItem(object):
    def __init__(self, room_name, dev_name, func_cmd):
        self.type = 1
        self.conditions = '||'
        self.conds = []
        self.obj_id = 0
        self.security_mode = ''
        self.room_name = room_name
        self.dev_name = dev_name
        self.func_value = ''
        self.func_cmd = func_cmd
        self.value = 0
        self.time = 0
        self.valid = 0
        self.seq = 0
        self.inter_time = 0
        self.param_type = 0


class SceneAddManager(object):
    def __init__(self, room_name, scene_name, actions):
        self.msg_type = 'scene_control_manager'
        self.command = 'add'
        self.from_role = 'phone'
        self.room_name = str("默认房间")
        self.scene_id = 0
        self.icon = 0
        self.scene_type = 1
        self.func_cmd = 'add'
        self.from_account = ''
        self.scene_name = scene_name
        self.actions = actions


class SceneControlManager(object):
    def __init__(self, scene_id):
        self.msg_type = 'scene_control_manager'
        self.command = 'start'
        self.from_role = 'phone'
        self.from_account = ''
        self.scene_id = scene_id


class SceneDeleteManager(object):
    def __init__(self, scene_id):
        self.msg_type = 'scene_control_manager'
        self.command = 'delete'
        self.from_role = 'phone'
        self.from_account = ''
        self.scene_id = scene_id


def auto_test_scene_actions_light_one(dev_addr, func_cmd):
    root = [
        SceneActionItem(g_test_room_name, dev_addr+'_1', func_cmd).__dict__
    ]
    return root


def auto_test_scene_actions_light_two(dev_addr, func_cmd):
    root = [
        SceneActionItem(g_test_room_name, dev_addr + '_1', func_cmd).__dict__,
        SceneActionItem(g_test_room_name, dev_addr + '_2', func_cmd).__dict__,
    ]
    return root


def auto_test_scene_actions_light_three(dev_addr, func_cmd):
    root = [
        SceneActionItem(g_test_room_name, dev_addr + '_1', func_cmd).__dict__,
        SceneActionItem(g_test_room_name, dev_addr + '_2', func_cmd).__dict__,
        SceneActionItem(g_test_room_name, dev_addr + '_3', func_cmd).__dict__,
    ]
    return root


def auto_test_scene_actions_light_fore(dev_addr, func_cmd):
    root = [
        SceneActionItem(g_test_room_name, dev_addr + '_1', func_cmd).__dict__,
        SceneActionItem(g_test_room_name, dev_addr + '_2', func_cmd).__dict__,
        SceneActionItem(g_test_room_name, dev_addr + '_3', func_cmd).__dict__,
        SceneActionItem(g_test_room_name, dev_addr + '_4', func_cmd).__dict__,
    ]
    return root


def auto_test_scene_get_id():
    print("auto_test_scene_get_id")
    while True:
        read_data = test_api_udp.auto_test_recv_data()
        if read_data == '':
            return -1
        scene_obj = json.loads(read_data)
        msg_type = scene_obj['msg_type']
        if msg_type != 'scene_control_manager':
            continue
        scene_id = scene_obj['scene_id']
        return scene_id
    return 0


def auto_test_scene_add_manager(dev_class_type, dev_addr, func_cmd):
    print("------auto_test_scene_add_manager----")
    actions = []
    if dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_ONE:
        actions = auto_test_scene_actions_light_one(dev_addr, func_cmd)
    elif dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_TWO:
        actions = auto_test_scene_actions_light_two(dev_addr, func_cmd)
    elif dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_THREE:
        actions = auto_test_scene_actions_light_three(dev_addr, func_cmd)
    elif dev_class_type == test_api_constant.DEV_CLASS_TYPE_LIGHT_FOUR:
        actions = auto_test_scene_actions_light_fore(dev_addr, func_cmd)

    data = SceneAddManager(g_test_room_name, dev_addr, actions)
    send_data = json.dumps(data.__dict__, ensure_ascii=False)
    test_api_udp.auto_test_send_class(send_data)


def auto_test_scene_control(scene_id):
    print("auto_test_scene_control")
    scene_control_data = SceneControlManager(scene_id)
    json_data = json.dumps(scene_control_data.__dict__, ensure_ascii=False)
    test_api_udp.auto_test_send_class(json_data)


def auto_test_scene_delete(scene_id):
    data = SceneDeleteManager(scene_id)
    json_data = json.dumps(data)
    test_api_udp.auto_test_send_class(json_data)




