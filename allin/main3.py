import random
import re
import redis
import datetime
import hashlib
import create_yzm
import send_email
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()
from flask import Flask, request, jsonify, make_response, abort, render_template, Response, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from multiprocessing import Process, cpu_count

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


@app.route('/', methods=['get', 'post'])
def index():
    return 'index'
    # return render_template("index.html")


# 登陆注册开始
def check_yzm(uuid, val):
    yzm_number = con.get(uuid)
    return True if yzm_number == val else False


@app.route('/get_yzm', methods=['get'])  # 前端随机生成一个uuid来绑定验证码
def get_yzm():
    uuid = request.args.get('uuid')
    if uuid:
        if uuid.strip():
            yzm_number, yzm_b64 = create_yzm.create()
            con.set(uuid, yzm_number)
            return jsonify({'status': 2000, 'yzm_b64': yzm_b64.decode('utf-8')})
        else:
            return jsonify({'status': 2001, 'msg': '缺少必要参数'})
    else:
        return jsonify({'status': 2001, 'msg': '缺少必要参数'})


@app.route('/login', methods=['post', 'get'])
def login():
    if not check_yzm(request.form.get('uuid'), request.form.get('val')):  # 先检查验证码正确性 val指的是用户填写的验证码
        return jsonify({'status': 1003})
    email_number = request.form.get('email')
    pwd = request.form.get('pass')  # 这里的pwd可以先在前端哈希加盐再传过来
    user_col = client['db1']['user']  # 选择db1库下的user集合
    user = user_col.find_one({'email': email_number})
    if user is None:
        return jsonify({'status': 1000, 'msg': '无此用户信息'})  # status:1000代表该用户未注册
    return jsonify({'status': 1001, 'msg': '密码错误'}) if user.get('pwd') != pwd else jsonify(
        {'status': 1002, 'msg': '登陆成功', 'data': {
            'name': user.get('name'),
            'username': user.get('username'),
            'email': user.get('email'),
            'sex': user.get('sex'),
            'birthday': user.get('birthday'),
            'like': user.get('like'),
            'flike': user.get('flike'),
            'img': user.get('img')
        }})
    # 登录成功后会返回用户信息 1001代表密码不正确，1002登陆成功


@app.route('/register1', methods=['post', 'get'])  # 前端 点击获取邮件验证码
def register_step1():
    if request.form.get('email'):
        email_number = request.form.get('email')
        # email_number = request.values.get('email')
        content = ''.join([random.choice(create_yzm.lst) for j in range(4)])
        send_email.send(email_number, '注册认证', content)
        con.set(email_number, content.lower())
        con.expire(email_number, 900)  # 邮件验证码15分钟内有效
        return jsonify({'status': 1004, 'msg': '邮件验证码发送成功'})
    return jsonify({'status': 1005, 'msg': '邮件验证码发送失败'})


@app.route('/check_email', methods=['post', 'get'])  # 检查邮件验证码是否正确，正确就设置cookie以便进一步注册
def check_email():
    email = request.form.get('email')
    val = request.form.get('value').lower()
    if val == con.get(email):
        outdate = datetime.datetime.today() + datetime.timedelta(days=30)
        response = make_response('')
        rid = email + 'DQWJNDJSANFIEWURH'
        m = hashlib.md5()
        m.update(rid.encode('utf-8'))
        response.set_cookie('rid', m.hexdigest(), expires=outdate)
        return response
    return jsonify({'status': 1003})  # 1003验证码错误


@app.route('/register2', methods=['post', 'get'])  # 检查有无cookie，如果用户是正常操作的话能注册成功
def register_step2():
    # rid = request.cookies.get('rid')
    # email = request.form.get('email')
    # if not email or not rid:
    #     abort(403)
    # # 验证cookie
    # real_rid = email + 'DQWJNDJSANFIEWURH'
    # m = hashlib.md5()
    # m.update(real_rid.encode('utf-8'))
    # real_rid = m.hexdigest()
    # if real_rid != rid:
    #     return jsonify({'status': 4000, 'msg': 'cookie错误'})
    email = request.form.get('email')
    if not email:
        abort(403)
    user_info = {
        'name': request.form.get('name'),
        'username': request.form.get('username'),
        'email': email,
        'pwd': request.form.get('pass'),
        'birthday': request.form.get('birthday'),
        'like': request.form.get('like'),
        'flike': request.form.get('flike')
    }
    # mongodb
    client['db1']['user'].insert_one(user_info)
    return jsonify({'status': 1005, 'msg': '注册成功'})  # 1005注册成功


# 登陆注册结束


# 修改信息
@app.route('/reset', methods=['post', 'get'])
def reset():
    if not request.form.get('email'):
        return jsonify({'status': 1006, 'msg': '缺乏邮箱参数'})
    email = request.form.get('email')
    user_col = client['db1']['user']
    user = user_col.find_one({'email': email})
    if not user:
        return jsonify({'status': 1009, 'msg': '没有该用户'})
    if request.form.get('name'):
        name = request.form.get('name')
        user_col.update({'email': email}, {'$set': {'name': name}})
    if request.form.get('username'):
        username = request.form.get('username')
        user_col.update({'email': email}, {'$set': {'username': username}})
    if request.form.get('pass'):
        pwd = request.form.get('pass')
        user_col.update({'email': email}, {'$set': {'pwd': pwd}})
    if request.form.get('birthday'):
        birthday = request.form.get('birthday')
        user_col.update({'email': email}, {'$set': {'birthday': birthday}})
    if request.form.get('like'):
        like = request.form.get('like')
        user_col.update({'email': email}, {'$set': {'like': like}})
    if request.form.get('flike'):
        flike = request.form.get('flike')
        user_col.update({'email': email}, {'$set': {'flike': flike}})
    if request.form.get('img'):
        img = request.form.get('img')
        user_col.update({'email': email}, {'$set': {'img': img}})
    if request.form.get('location'):
        location = request.form.get('location')
        user_col.update({'email': email}, {'$set': {'location': location}})
    if request.form.get('introduction'):
        introduction = request.form.get('introduction')
        user_col.update({'email': email}, {'$set': {'introduction': introduction}})
    user = user_col.find_one({'email': email})
    return jsonify(
        {'status': 1002, 'msg': '修改成功', 'data': {
            'name': user.get('name'),
            'username': user.get('username'),
            'email': user.get('email'),
            'sex': user.get('sex'),
            'birthday': user.get('birthday'),
            'like': user.get('like'),
            'flike': user.get('flike'),
            'img': user.get('img'),
            'location': user.get('location'),
            'introduction': user.get('introduction')
        }})


# 添加好友
@app.route('/set_friend', methods=['get'])
def set_friend():
    email, femail, group = request.args.get('email'), request.args.get('femail'), request.args.get('group')
    if not email or not femail or not group:
        return jsonify({'status': 5000, 'msg': '缺乏参数'})
    if group not in ['1', '2', '3', '4']:
        return jsonify({'status': 5000, 'msg': '组别不存在'})
    user_col = client['db1']['user']
    user = user_col.find_one({'email': email})
    if not user:
        return jsonify({'status': 5001, 'msg': '无此用户'})
    fuser = user_col.find_one({'email': femail})
    if not fuser:
        return jsonify({'status': 5002, 'msg': '添加的用户不存在'})
    friends = user.get('friends')
    if not friends:
        friends = []
    if femail not in friends:
        friends.append(femail)
    group1 = [] if not user.get('group1') else user.get('group1')
    group2 = [] if not user.get('group2') else user.get('group2')
    group3 = [] if not user.get('group3') else user.get('group3')
    group4 = [] if not user.get('group4') else user.get('group4')
    if femail in group1:
        group1.remove(femail)
    if femail in group2:
        group2.remove(femail)
    if femail in group3:
        group3.remove(femail)
    if femail in group4:
        group4.remove(femail)
    if group == '1':
        group1.append(femail)
    elif group == '2':
        group2.append(femail)
    elif group == '3':
        group3.append(femail)
    elif group == '4':
        group4.append(femail)
    user_col.update({'email': email}, {
        '$set': {'friends': friends, 'group1': group1, 'group2': group2, 'group3': group3, 'group4': group4}})
    return jsonify({'status': 5003, 'msg': '添加成功'})


# 删除好友
@app.route('/rm_friend', methods=['get'])
def rm_friend():
    email, femail = request.args.get('email'), request.args.get('femail')
    if not email or femail:
        return jsonify({'status': 5000, 'msg': '缺乏参数'})
    user_col = client['db1']['user']
    user = user_col.find_one({'email': email})
    fuser = user_col.find_one({'email': femail})
    if not user or fuser:
        return jsonify({'status': 5001, 'msg': '用户不存在'})
    friends = [] if not user.get('friends') else user.get('friends')
    if femail not in friends:
        return jsonify({'status': 5004, 'msg': '删除成功'})
    group1 = [] if not user.get('group1') else user.get('group1')
    group2 = [] if not user.get('group2') else user.get('group2')
    group3 = [] if not user.get('group3') else user.get('group3')
    group4 = [] if not user.get('group4') else user.get('group4')
    if femail in group1:
        group1.remove(femail)
    if femail in group2:
        group2.remove(femail)
    if femail in group3:
        group3.remove(femail)
    if femail in group4:
        group4.remove(femail)
    user_col.update({'email': email}, {
        '$set': {'friends': friends, 'group1': group1, 'group2': group2, 'group3': group3, 'group4': group4}})
    return jsonify({'status': 5004, 'msg': '删除成功'})


# 返回交友数据
def search(email='', username='', sex='', like='', flike='', limit=20, start=0):
    user_col = client['db1']['user']
    info_list, user_list = [], []
    if sex and username and like and flike:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'username': re.compile(username)},
                {'like': re.compile(like)},
                {'flike': re.compile(flike)}
            ]
        })
    elif sex and username and like:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'username': re.compile(username)},
                {'like': re.compile(like)}
            ]
        })
    elif sex and username and flike:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'username': re.compile(username)},
                {'flike': re.compile(flike)}
            ]
        })
    elif sex and like and flike:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'like': re.compile(like)},
                {'flike': re.compile(flike)}
            ]
        })
    elif username and like and flike:
        user_list = user_col.find({
            '$and': [
                {'username': re.compile(username)},
                {'like': re.compile(like)},
                {'flike': re.compile(flike)}
            ]
        })
    elif sex and username:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'username': re.compile(username)}
            ]
        })
    elif sex and like:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'like': re.compile(like)}
            ]
        })
    elif sex and flike:
        user_list = user_col.find({
            '$and': [
                {'sex': sex},
                {'flike': re.compile(flike)}
            ]
        })
    elif username and like:
        user_list = user_col.find({
            '$and': [
                {'username': re.compile(username)},
                {'like': re.compile(like)}
            ]
        })
    elif username and flike:
        user_list = user_col.find({
            '$and': [
                {'username': re.compile(username)},
                {'flike': re.compile(flike)}
            ]
        })
    elif like and flike:
        user_list = user_col.find({
            '$and': [
                {'like': re.compile(like)},
                {'flike': re.compile(flike)}
            ]
        })
    elif sex:
        user_list = user_col.find({'sex': sex})
    elif username:
        user_list = user_col.find({'username': re.compile(username)})
    elif like:
        user_list = user_col.find({'like': re.compile(like)})
    elif flike:
        user_list = user_col.find({'flike': re.compile(flike)})
    elif email:
        user_list = user_col.find({'email': email})
    else:
        user_list = user_col.find()
    user_list = user_list.limit(limit).skip(start)
    for info in user_list:
        info['_id'] = info['_id'].__str__()
        info_list.append(info)
    return info_list


@app.route('/get_data', methods=['get'])
def get_data():
    if not request.args.get('limit') or not request.args.get('start') or not request.args.get('email'):
        return jsonify({'status': 1007, 'msg': '缺乏必要参数'})
    username, sex, like, flike = request.args.get('username'), request.args.get('sex'), request.args.get(
        'like'), request.args.get('flike')
    femail = request.args.get('femail')
    # 存关键字，方便推荐用户
    email = request.args.get('email')
    if like:
        client['db1']['user'].update({'email': email}, {'$set': {'k1': like}})
    if flike:
        client['db1']['user'].update({'email': email}, {'$set': {'k2': flike}})
    limit, start = request.args.get('limit'), request.args.get('start')
    user_info = search(femail, username, sex, like, flike, int(limit), int(start))
    return jsonify({'status': 1008, 'data': user_info})


# 返回交友数据结束


# 根据like和flike推荐
@app.route('/recommend', methods=['get'])
def recommend():
    if not request.args.get('email'):
        return jsonify({'status': 1007, 'msg': '缺乏必要参数'})
    email = request.args.get('email')
    user_col = client['db1']['user']
    info = user_col.find({'email': email})
    data = []
    for i in info:
        data.append(i)
    data = {} if not data else data[0]
    k1, k2 = data.get('k1'), data.get('k2')
    data, k1_list, k2_list = [], [], []
    fin = [email]
    if not k1 and not k2:
        return jsonify({'status': 1008, 'data': data})
    if k1:
        k1_list = user_col.find({'like': re.compile(k1)})
    if k2:
        k2_list = user_col.find({'flike': re.compile(k2)})
    for i in k1_list:
        if i.get('email') in fin:
            continue
        i['_id'] = i['_id'].__str__()
        data.append(i)
        fin.append(i.get('email'))
    for i in k2_list:
        if i.get('email') in fin:
            continue
        i['_id'] = i['_id'].__str__()
        data.append(i)
        fin.append(i.get('email'))
    return jsonify({'status': 1008, 'data': data})


# 动态发布开始
@app.route('/putPost', methods=['get', 'post'])
def put_post():
    if not request.form.get('email'):
        return jsonify({'status': 3000, 'msg': '缺少有效参数'})  # 3000代表无效用户
    email_number = request.form.get('email')
    if not client['db1']['user'].find_one({'email': email_number}):
        return jsonify({'status': 3000, 'msg': '缺少有效参数'})
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


@app.route('/get_friend_post', methods=['get', 'post'])
def get_friend_post():
    email = request.args.get('email')
    user_col = client['db1']['user']
    user = user_col.find_one({'email': email})
    if not user:
        return jsonify({'status': 3000, 'msg': '缺少有效参数'})
    post_col = client['db1']['post']
    friends = user.get('friends') if user.get('friends') else []
    if not friends:
        return jsonify({'status': 3002, 'data': []})
    post_list = []
    for i in friends:
        data = post_col.find({'email': i})
        if not data:
            continue
        for d in data:
            d['_id'] = d['_id'].__str__()
            post_list.append(d)
    post_list = sorted(post_list, key=get_time)
    post_list.reverse()
    return jsonify({'status': 3002, 'data': post_list})


def get_time(post):
    return post.get('time')


@app.route('/getPost', methods=['get', 'post'])
def get_post():
    post_col = client['db1']['post']
    if request.args.get('oldTime'):
        # 提供一个参数时间戳，暂时先支持查询该时间戳往后的动态
        old_time = int(request.args.get('oldTime'))
        data = post_col.find({'time': {'$gte': old_time}})
        data_list = []
        for i in data:
            i['_id'] = i['_id'].__str__()
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


@app.route('/comment', methods=['get', 'post'])
def comment():
    if not request.form.get('comment') or not request.form.get('username') or not request.form.get('email'):
        return jsonify({'status': 3006, 'msg': '评论为空或缺乏用户信息'})
    elif not request.form.get('id'):
        return jsonify({'status': 3006, 'msg': '缺乏id'})
    else:
        comm = request.form.get('comment')
        if not comm.strip():
            return jsonify({'status': 3006, 'msg': '评论为空'})
        post_col = client['db1']['post']
        pid = ObjectId(request.form.get('id'))
        data = post_col.find_one({'_id': pid})
        if not data:
            return jsonify({'status': 3006, 'msg': '没有该动态信息'})
        comment_list = data.get('comment_list') if data.get('comment_list') else []
        comm = {
            'username': request.form.get('username'),
            'comment': request.form.get('comment').strip(),
            'email': request.form.get('email')
        }
        data['comment_list'] = comment_list.append(comm)
        post_col.update({'_id': pid}, {'$set': {'comment_list': comment_list}})
        return jsonify({'status': 3007, 'msg': '评论成功'})


@app.route('/delPost', methods=['get', 'post'])
def del_post():
    # 接收用户的邮箱和发布动态时的时间戳
    if request.args.get('email') and request.args.get('time'):
        res = client['db1']['post'].delete_one(
            {'$and': [{'email': request.args.get('email')}, {'time': int(request.args.get('time'))}]})
        if res.deleted_count == 0:
            return jsonify({'status': 3004, 'msg': '无此数据'})
        return jsonify({'status': 3005, 'msg': '删除成功'})
    else:
        return jsonify({'status': 3006})  # 删除失败，缺乏必要参数


# 获取好友列表
@app.route('/get_friends', methods=['get'])
def get_friends():
    email = request.args.get('email')
    if not email:
        return jsonify({'status': 6000, 'msg': '缺少有效参数'})
    user = client['db1']['user'].find_one({'email': email})
    if not user:
        return jsonify({'status': 6000, 'msg': '缺少有效参数'})
    friends = [] if not user.get('friends') else user.get('friends')
    group1 = [] if not user.get('group1') else user.get('group1')
    group2 = [] if not user.get('group2') else user.get('group2')
    group3 = [] if not user.get('group3') else user.get('group3')
    group4 = [] if not user.get('group4') else user.get('group4')
    return jsonify({'status': 6001, 'data': {
        'friends': friends,
        'group1': group1,
        'group2': group2,
        'group3': group3,
        'group4': group4
    }})


# 判断是否为好友
@app.route('/is_friend', methods=['get'])
def is_friend():
    email = request.args.get('email')
    femail = request.args.get('femail')
    if not email or femail:
        return jsonify({'status': 6000, 'msg': '缺少有效参数'})
    user = client['db1']['user'].find_one({'email': email})
    if not user:
        return jsonify({'status': 6000, 'msg': '缺少有效参数'})
    friends = [] if not user.get('friends') else user.get('friends')
    if femail in friends:
        return jsonify({'status': 6001, 'res': 0})
    return jsonify({'status': 6001, 'res': 1})


# 获取个人信息
@app.route('/get_info', methods=['get'])
def get_info():
    email = request.args.get('email')
    if not email:
        return jsonify({'status': 6000, 'msg': '缺少有效参数'})
    user = client['db1']['user'].find_one({'email': email})
    if not user:
        return jsonify({'status': 6000, 'msg': '缺少有效参数'})
    return jsonify({'status': 6001, 'data': user})


# 获取文案
@app.route('/article', methods=['get'])
def article():
    articles = client['db1']['article'].find()
    if articles:
        article_list = []
        for a in articles:
            a['_id'] = a['_id'].__str__()
            article_list.append(a)
        return jsonify({'status': 3007, 'data': article_list})
    return jsonify({'status': 3008, 'msg': '无文章数据'})


# 获取图片
@app.route('/pic', methods=['get'])
def pic():
    images = client['db1']['pic'].find()
    if images:
        img_list = []
        for i in images:
            i['_id'] = i['_id'].__str__()
            img_list.append(i)
        return jsonify({'status': 3007, 'data': img_list})
    return jsonify({'status': 3008, 'msg': '无图片数据'})


def run(MULTI_PROCESS):
    if not MULTI_PROCESS:
        WSGIServer(('0.0.0.0', 5000), app).serve_forever()
    else:
        mulserver = WSGIServer(('0.0.0.0', 5000), app)
        mulserver.start()

        def server_forever():
            mulserver.start_accepting()
            mulserver._stop_event.wait()

        for i in range(cpu_count()):
            p = Process(target=server_forever)
            p.run()
            # p.start()


if __name__ == '__main__':
    # 单进程 + 协程
    # run(False)
    # 多进程 + 协程
    run(True)
