import json
import elasticsearch
from time import sleep
import test_api_constant


def get_info_from_es(case_id):
    """
    从ES获取数据
    """
    query = json.dumps({
        "query": {
            "term": {
                "sid": case_id
            }
        },
        "sort": [
            {
                "@timestamp": {
                    "order": "asc"
                }
            }
        ]
    })
    # print(query)
    es = elasticsearch.Elasticsearch(['192.192.10.10'])
    res = es.search(index='testlog', body=query)
    sleep(5)
    docs = res['hits']['hits']
    for doc in docs:
        print(doc.get('_source').get('result'))
    return docs


def auto_test_devicehub_control_result(sid):
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_DEVICE_CONTROL_DEV_SUCCESS:
            print('*** 设备层控制设备成功 ***')
            return 0
    return -1


def auto_test_smarthome_control_result(sid):
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_DEVICE_CONTROL_SMART_SUCCESS:
            print('*** 业务层控制设备成功 ***')
            return 0
    return -1


def auto_test_device_add_result(sid):
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_DEVICE_ADD_MANAGER_SUCCESS:
            print('*** 添加设备成功 ***')
            return 0
        elif item.get('_source').get('result') == test_api_constant.AUTOTEST_DEVICE_ADD_MANAGER_SAME:
            print('*** 有相同名设备 ***')
            return 0

    return -1


def auto_test_join_result(sid):
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_COORDINATOR_OPEN_NETWORK_SUCCESS:
            print('*** 允许入网打开成功 ***')
            return 0
    return -1


def auto_test_scene_add_result(sid):
    scene_id = -1
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_SCENE_ADD_MANAGER_SUCCESS:
            msg = item.get('_source').get('message')
            print("linkage_add.msg = ", msg)
            root = json.loads(msg)
            scene_id = root['value']
            print("*** 联动添加成功 ***'")
            print("*** scene_id = ", scene_id)
            return scene_id
    return scene_id


def auto_test_smart_linkage_add_result(sid):
    linkage_id = -1
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_SMART_LINKAGE_ADD_MANAGER_SUCCESS:
            msg = item.get('_source').get('message')
            print("linkage_add.msg = ", msg)
            root = json.loads(msg)
            linkage_id = root['value']
            print("*** 联动添加成功 ***'")
            print("*** id = '", linkage_id)
            return linkage_id

    return linkage_id


def auto_test_smart_linkage_delete_result(sid):
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_SMART_LINKAGE_DELETE_MANAGER_SUCCESS:
            print("*** 删除联动成功 ***")
            return 0
    return -1


def auto_test_scene_delete_result(sid):
    result_msg = get_info_from_es(sid)
    for item in result_msg:
        if item.get('_source').get('result') == test_api_constant.AUTOTEST_SCENE_DELETE_MANAGER_SUCCESS:
            print("*** 删除场景成功 ***")
            return 0
    return -1