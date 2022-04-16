from pymongo import MongoClient
from flask import Flask, request, jsonify, make_response, abort, Response, Blueprint

app = Flask(__name__)

# 连接mongodb
client = MongoClient(
    host='127.0.0.1',
    port=27017
)


@app.route('/putPost', methods=['get', 'post'])
def put_post():
    if not request.form.get('email'):
        return jsonify({'status': 3000})  # 3000代表无效用户
    email_number = request.form.get('email')
    username = request.form.get('username')
    msg = request.form.get('message')
    time = request.form.get('time')  # 传时间戳过来！！！
    post_data = {
        'email': email_number,
        'name': username,
        'msg': msg,
        'time': int(time)
    }
    client['db1']['post'].insert_one(post_data)
    return jsonify({'status': 3001})  # 3001代表发布动态成功


@app.route('/getPost', methods=['get', 'post'])
def get_post():
    post_col = client['db1']['post']
    if request.args.get('oldTime'):
        # 提供一个参数时间戳，暂时先支持查询该时间戳往后的动态
        old_time = int(request.args.get('oldTime'))
        data = post_col.find({'time': {'$gte': old_time}})
        data_list = []
        for i in data:
            del i['_id']
            data_list.append(i)
        return jsonify({'status': 3002, 'data': data_list})
    elif request.args.get('email'):
        email = request.args.get('email')
        data = post_col.find({'email': email})
        data_list = []
        for i in data:
            del i['_id']
            data_list.append(i)
        return jsonify({'status': 3002, 'data': data_list})
    return jsonify({'status': 3003})


if __name__ == '__main__':
    app.run()
