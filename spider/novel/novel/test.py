import json


def test():
    f = open('./items.json', 'r', encoding='gbk')

    parsed_json = json.load(f)

    url_list = []

    for i in parsed_json["novel_items"]:
        url_list.append(i.get('link'))

    print(url_list)
    #
    # JsonPath = './items.json'
    # with open(JsonPath,'r',encoding='gbk') as f:
    #     data = json.load(f)
    # print(data)

test()