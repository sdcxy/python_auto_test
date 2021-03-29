# -*-coding:utf-8-*-
from dl import test_api_scene
from dl import test_api_get_from_es
from dl import test_api_dev_join
from dl import test_api_constant
from dl import test_api_udp
from dl import test_api_dev_manager
from dl import test_api_case_id
from dl import test_api_smart_link

# -------------------------* 需修改的类容 *---------------------------
g_case_id = "B04"                   # 自动测试的用例ID
g_gateway_ip = '192.168.5.105'      # 自动测试的主机IP
g_gateway_port = 8100               # 自动测试的主机端口
g_riu_id = test_api_constant.G_RIU_ID                                   # 自动测试的网关类型
g_test_room_name = '默认房间'                                            # 自动测试的房间名
g_test_class_type = test_api_constant.DEV_CLASS_TYPE_LIGHT_FOUR         # 自动测试的设备类型
g_test_brand = test_api_constant.AUTOTEST_GEM_BRAND_M9                  # 自动测试的设备品牌
# ------------------------------------------------------------------


class AutoTestGlobalInfo(object):
    def __init__(self, riu_id, case_id, auto_test_dev_addr, auto_test_class_type):
        self.riu_id = riu_id
        self.case_id = case_id
        self.scene_id = 0
        self.smart_link_id = 0
        self.auto_test_dev_addr = auto_test_dev_addr
        self.auto_test_class_type = auto_test_class_type
        self.auto_test_room_name = g_test_room_name


g_testInfo = AutoTestGlobalInfo(g_riu_id, g_case_id, '', g_test_class_type)


def auto_test_gateway(sid, caseName):
    """
    网关自动化测试函数
    """

    while True:

        if test_api_case_id.auto_test_set_sid(sid, caseName) == -1:
            print('*** 测试用例ID设置失败 ***')
            return

        test_api_dev_join.auto_test_allow_join(g_riu_id, "allow", g_test_brand)
        if test_api_get_from_es.auto_test_join_result(sid) == -1:
            test_api_get_from_es.auto_test_join_result(sid)

        if test_api_dev_manager.auto_test_wait_new_device_report(g_test_class_type) == -1:
            print("*** 未有新设备上报! ***")
            return

        if test_api_get_from_es.auto_test_device_add_result(sid) == -1:
            if test_api_get_from_es.auto_test_device_add_result(sid) == -1:
                print("*** 新设备添加失败! ***")
                return

        g_testInfo.auto_test_dev_addr = test_api_dev_manager.auto_test_get_device_addr()

        test_api_dev_manager.auto_test_control_device(g_testInfo.auto_test_dev_addr+'_1')

        if test_api_get_from_es.auto_test_smarthome_control_result(sid) == -1:
            if test_api_get_from_es.auto_test_smarthome_control_result(sid) == -1:
                print('*** 业务层设备控制失败！***')
                return

        if test_api_get_from_es.auto_test_devicehub_control_result(sid) == -1:
            if test_api_get_from_es.auto_test_devicehub_control_result(sid) == -1:
                print('*** 设备层设备控制失败！***')
                return

        test_api_scene.auto_test_scene_add_manager(g_testInfo.auto_test_class_type, g_testInfo.auto_test_dev_addr, "on")
        scene_id = test_api_get_from_es.auto_test_scene_add_result(sid)
        if scene_id == -1:
            scene_id = test_api_get_from_es.auto_test_scene_add_result(sid)
            if scene_id == -1:
                print("*** 场景添加失败！***")

        if scene_id != -1:
            test_api_scene.auto_test_scene_delete(scene_id)
        if test_api_get_from_es.auto_test_scene_delete_result(sid) == -1:
            if test_api_get_from_es.auto_test_scene_delete_result(sid) == -1:
                print("*** 删除场景失败! ***")

        test_api_smart_link.auto_test_smart_linkage_add_manager(g_testInfo.auto_test_dev_addr,
                                                                g_testInfo.auto_test_class_type,
                                                                g_testInfo.auto_test_room_name)
        linkage_id = test_api_get_from_es.auto_test_smart_linkage_add_result(sid)
        if linkage_id == -1:
            linkage_id = test_api_get_from_es.auto_test_smart_linkage_add_result(sid)
            if linkage_id == -1:
                print("*** 联动添加失败！ ***")

        if linkage_id != -1:
            test_api_smart_link.auto_test_smart_linkage_delete_manager(linkage_id)

        if test_api_get_from_es.auto_test_smart_linkage_delete_result(sid) == -1:
            if test_api_get_from_es.auto_test_smart_linkage_delete_result(sid) == -1:
                print("*** 删除联动失败! ***")

        return


if __name__ == '__main__':
    print('********************** 开始测试 **********************')

    test_api_udp.auto_test_udp_init(g_gateway_ip, g_gateway_port)
    auto_test_gateway(g_case_id, g_case_id)
    test_api_dev_join.auto_test_allow_join(g_riu_id, "stop", g_test_brand)

    print("********************** 测试完成 *************************")
