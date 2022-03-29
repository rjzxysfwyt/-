import random
import redis
import datetime
import hashlib
from flask import Flask, request, jsonify, make_response, abort, Response, Blueprint

from pymongo import MongoClient

import create_yzm
import send_email

# 连接redis数据库
con = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    db=4,
    decode_responses=True
)
# 连接mongodb数据库
client = MongoClient(
    host='127.0.0.1',
    port=27017
)
app = Flask(__name__)


def check_yzm(uuid, val):
    yzm_number = con.get(uuid)
    return True if yzm_number == val else False


@app.route('/get_yzm', methods=['get'])  # 前端随机生成一个uuid来绑定验证码
def get_yzm():
    yzm_number, yzm_b64 = create_yzm.create()
    uuid = request.args.get('uuid')
    con.set(uuid, yzm_number)
    return jsonify({'status': 2000, 'img_b64': yzm_b64.decode('utf-8')})


@app.route('/login', methods=['post'])
def login():
    if not check_yzm(request.form.get('uuid'), request.form.get('val')):  # 先检查验证码正确性 val指的是用户填写的验证码
        return jsonify({'status': 1003})
    email_number = request.form.get('email')
    pwd = request.form.get('pwd')  # 这里的pwd可以先在前端哈希加盐再传过来
    user_col = client['db1']['user']  # 选择db1库下的user集合
    user = user_col.find_one({'email': email_number})
    if user is None:
        return jsonify({'status': 1000})  # status:1000代表该用户未注册
    return jsonify({'status': 1001, 'msg': {'error': True}}) if user.get('pwd') != pwd else jsonify({'status': 1002, 'msg': {'error': False, 'name': user.get('name'), 'img': user.get('img'), 'hobbies': user.get('hobbies'), 'kind': user.get('kind'), 'like': user.get('like')}})  # 登录成功后会返回用户信息 1001嗲表密码不正确，1002登陆成功


@app.route('/register1', methods=['post'])  # 前端 点击获取邮件验证码
def register_step1():
    email_number = request.form.get('email')
    content = ''.join([random.choice(create_yzm.lst) for j in range(4)])
    send_email.send(email_number, '注册认证', content)
    con.set(email_number, content.lower())
    con.expire(email_number, 900)  # 邮件验证码15分钟内有效
    return 'ok'


@app.route('/check_email', methods=['post'])  # 检查邮件验证码是否正确，正确就设置cookie以便进一步注册
def check_email():
    email = request.form.get('email')
    val = request.form.get('value').lower()
    if val == con.get(email):
        outdate = datetime.datetime.today() + datetime.timedelta(days=30)
        response = make_response('')
        rid = email + 'DQWJNDJSANFIEWURH'
        m = hashlib.md5()
        m.update(rid.encode('utf-8'))
        print(m.hexdigest())
        response.set_cookie('rid', m.hexdigest(), expires=outdate)
        return response
        # return jsonify({'status': 1004})  # 1004表示验证码正确
    return jsonify({'status': 1003})  # 1003验证码错误


@app.route('/register2', methods=['post', 'get'])  # 检查有无cookie，如果用户是正常操作的话能注册成功
def register_step2():
    rid = request.cookies.get('rid')
    # print(rid)
    email = request.form.get('email')
    # print(email)
    if not rid or not email:
        abort(403)
    m = hashlib.md5()
    email = request.form.get('email')
    m.update((email + 'DQWJNDJSANFIEWURH').encode('utf-8'))
    if rid != m.hexdigest():
        abort(403)
    user_info = {
        'name': request.form.get('name'),
        'tel': request.form.get('tel'),
        'email': email,
        'pwd': request.form.get('pwd'),
        'img': request.form.get('img'),
        'hobbies': request.form.get('hobbies'),
        'kind': request.form.get('kind'),
        'like': request.form.get('like')
    }
    client['db1']['user'].insert_one(user_info)
    return jsonify({'status': 1005})  # 1005注册成功


if __name__ == '__main__':
    app.run()

# 测试数据
# client['db1']['user'].insert_one({
#     'email': 'xxx@xx.xx',
#     'pwd': 'MD5',
#     'img': '',
#     'hobbies': ['睡觉', '音乐'],
#     'kind': '帅气',
#     'like': '温柔体贴'
# })
