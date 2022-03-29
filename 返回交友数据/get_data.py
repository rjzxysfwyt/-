import re


from flask import Flask, request, jsonify, abort

from pymongo import MongoClient


# 连接mongodb数据库
client = MongoClient(
    host='127.0.0.1',
    port=27017
)
app = Flask(__name__)


def search(sex='', age=[], hobbies='', location='', limit=20, start=0):
    user_col = client['db2']['user']
    info_list, user_list = [], []
    if sex and age and hobbies and location:
        user_list = user_col.find(
            {'$and': [
                {'$and': [{'sex': sex}, {'age': {'$gte': age[0]}}, {'hobbies': re.compile(hobbies)},
                          {'location': location}]},
                {'$and': [{'sex': sex}, {'age': {'$lte': age[1]}}, {'hobbies': re.compile(hobbies)},
                          {'location': location}]}
            ]
            }).limit(limit).skip(start)
    elif sex and age and hobbies:
        user_list = user_col.find(
            {'$and': [
                {'$and': [{'sex': sex}, {'age': {'$gte': age[0]}}, {'hobbies': re.compile(hobbies)}]},
                {'$and': [{'sex': sex}, {'age': {'$lte': age[1]}}, {'hobbies': re.compile(hobbies)}]}
            ]
            }).limit(limit).skip(start)
    elif sex and age and location:
        user_list = user_col.find(
            {'$and': [
                {'$and': [{'sex': sex}, {'age': {'$gte': age[0]}}, {'location': location}]},
                {'$and': [{'sex': sex}, {'age': {'$lte': age[1]}}, {'location': location}]}
            ]
            }).limit(limit).skip(start)
    elif sex and location and hobbies:
        user_list = user_col.find(
                {'$and': [{'sex': sex}, {'location': location}, {'hobbies': re.compile(hobbies)}]}
            ).limit(limit).skip(start)
    elif age and location and hobbies:
        user_list = user_col.find(
            {'$and': [
                {'$and': [{'location': location}, {'age': {'$gte': age[0]}}, {'hobbies': re.compile(hobbies)}]},
                {'$and': [{'location': location}, {'age': {'$lte': age[1]}}, {'hobbies': re.compile(hobbies)}]}
            ]
            }).limit(limit).skip(start)
    elif sex and age:
        user_list = user_col.find({'$and': [
                {'$and': [{'sex': sex}, {'age': {'$gte': age[0]}}]},
                {'$and': [{'sex': sex}, {'age': {'$lte': age[1]}}]}
            ]}).limit(limit).skip(start)
    elif sex and hobbies:
        user_list = user_col.find(
            {'$and': [{'sex': sex}, {'hobbies': re.compile(hobbies)}]}
        ).limit(limit).skip(start)
    elif sex and location:
        user_list = user_col.find(
            {'$and': [{'sex': sex}, {'location': location}]}
        ).limit(limit).skip(start)
    elif age and hobbies:
        user_list = user_col.find(
            {'$and': [
                {'$and': [{'age': {'$gte': age[0]}}, {'hobbies': re.compile(hobbies)}]},
                {'$and': [{'age': {'$lte': age[1]}}, {'hobbies': re.compile(hobbies)}]}
            ]
            }).limit(limit).skip(start)
    elif age and location:
        user_list = user_col.find(
            {'$and': [
                {'$and': [{'location': location}, {'age': {'$gte': age[0]}}]},
                {'$and': [{'location': location}, {'age': {'$lte': age[1]}}]}
            ]
            }).limit(limit).skip(start)
    elif hobbies and location:
        user_list = user_col.find(
            {'$and': [{'hobbies': re.compile(hobbies)}, {'location': location}]}
        ).limit(limit).skip(start)
    elif sex:
        user_list = user_col.find({'sex': sex}).limit(limit).skip(start)
    elif age:
        user_list = user_col.find(
            {'$and': [
                {'age': {'$gte': age[0]}}, {'age': {'$lte': age[1]}}
            ]
            }).limit(limit).skip(start)
    elif location:
        user_list = user_col.find({'location': location}).limit(limit).skip(start)
    elif hobbies:
        user_list = user_col.find({'hobbies': re.compile(hobbies)})
    else:
        user_list = user_col.find().limit(limit).skip(start)
    for info in user_list:
        info_list.append(info)
    return info_list


@app.route('/get_data', methods=['get'])
def get_data():
    print(request.args, len(request.args))
    if len(request.args) <= 1:
        abort(403)
    sex, age1, age2, hobbies, location = request.args.get('sex'), request.args.get('age1'), request.args.get('age2'), request.args.get(
        'hobbies'), request.args.get('location')
    limit, start = request.args.get('limit'), request.args.get('start')
    age = []
    if age1 and age2:
        age1, age2 = int(age1), int(age2)
        age = [age1, age2]
    user_info = search(sex, age, hobbies, location, int(limit), int(start))
    return jsonify({'data': user_info})


if __name__ == '__main__':
    app.run()
# test = [{'_id': 1, 'name': 'John', 'address': 'Highway37', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27', 'age': 19, 'sex': '女', 'location': '广州'},
#         {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652', 'age': 20, 'sex': '女', 'location': '广州'},
#         {'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 5, 'name': 'Michael', 'address': 'Valley 345', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2', 'age': 21, 'sex': '女', 'location': '广州'},
#         {'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1', 'age': 26, 'sex': '女', 'location': '广州'},
#         {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 9, 'name': 'Susan', 'address': 'One way 98', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 12, 'name': 'William', 'address': 'Central st 954', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989', 'age': 18, 'sex': '女', 'location': '广州'},
#         {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633', 'age': 18, 'sex': '女', 'location': '广州'}]
# client['db2']['user'].insert_many(test)