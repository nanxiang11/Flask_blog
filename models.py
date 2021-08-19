#encoding:utf-8
# 刘文豪
# 大帅哥
from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    studentName = db.Column(db.String(100), nullable=False)
    studentPassword = db.Column(db.String(100), nullable=False)
    studentEmail = db.Column(db.String(100), nullable=False)
    imgurl = db.Column(db.String(100))
    aboutme = db.Column(db.String(200))
    postTime = db.Column(db.DateTime, default=datetime.now)

def dimquery(name):
    jiegu = User.query.filter(User.studentName.like('%{}%'.format(name))).all()
    return jiegu

def queryStudent(name, password):
    select = User.query.filter(User.studentName == name, User.studentPassword == password).all()
    return select

def queryStudent2():
    select = User.query.all()
    return select

def queryStudent3(a):
    message = Match.query.order_by(Match.postTime.desc()).paginate(a, per_page=10,  error_out=False)
    return message

def queryEmail(email):
    select = User.query.filter(User.studentEmail == email).all()
    return len(select)

def addstudent(name, password, email):
    newstudent = User(studentName=name, studentPassword=password, studentEmail=email)
    db.session.add(newstudent)  # 添加数据
    db.session.commit()  # 提交事务

def editPassword(email, password):
    p1 = User.query.filter(User.studentEmail == email).first()
    p1.studentPassword = password
    db.session.commit()

def editPassword2(name, password, imgurl, aboutme):
    p1 = User.query.filter(User.studentName == name and User.studentPassword == password).first()
    p1.imgurl = imgurl
    p1.aboutme = aboutme
    db.session.commit()

class VP(db.Model):
    __tablename__ = 'vip'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))  # 外键
    vip = db.Column(db.String(10))
    ding = db.Column(db.String(10))
    tui = db.Column(db.String(10))
    manage = db.Column(db.String(10))
    postTime = db.Column(db.DateTime, default=datetime.now)


class QueryVP:
    def query(self):
        message = VP.query.all()
        return message
    def add(self, user_id, vip, ding, tui, manage):
        newvp = VP(user_id=user_id, vip=vip, ding=ding, tui=tui, manage=manage)
        db.session.add(newvp)  # 添加数据
        db.session.commit()  # 提交事务


class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))  # 外键
    vp_id = db.Column(db.Integer, db.ForeignKey(VP.id))  # 外键
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    love = db.Column(db.String(100))
    disnum = db.Column(db.String(100))
    seenum = db.Column(db.String(100))
    imgurl = db.Column(db.String(50))
    postTime = db.Column(db.DateTime, default=datetime.now)


class QueryMatch:
    def query(self, a):
        message = Match.query.order_by(Match.postTime.desc()).paginate(a, per_page=10,  error_out=False)
        return message

    def query2(self, a):
        message = Match.query.filter(Match.id == a).first()
        return message

    def queryseenum(self, a):
        message = Match.query.filter(Match.id == a).first()
        return message

    def queryall(self):
        message = Match.query.all()
        return message

    def dimquery(self, title, a):
        jiegu = Match.query.filter(Match.title.like('%{}%'.format(title))).paginate(a, per_page=10,  error_out=False)
        return jiegu

    def add(self, user_id, vp_id, title, body, love, disnum, seenum, imgurl):
        newmatch = Match(user_id=user_id, vp_id=vp_id, title=title, body=body, love=love, disnum=disnum, seenum=seenum, imgurl=imgurl)
        db.session.add(newmatch)  # 添加数据
        db.session.commit()  # 提交事务

    def editseenum(self, match_id, seenum):
        e = Match.query.filter(Match.id == match_id).first()
        e.seenum = seenum
        db.session.commit()

    def editreply(self, match_id, replyum):
        e = Match.query.filter(Match.id == match_id).first()
        e.disnum = replyum
        db.session.commit()

class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))  # 外键
    replymatch_id = db.Column(db.Integer, db.ForeignKey(Match.id))  # 外键
    replyuser_id = db.Column(db.Integer)
    replyself_id = db.Column(db.Integer)
    body = db.Column(db.TEXT)
    postTime = db.Column(db.DateTime, default=datetime.now)

class QueryReply:

    def query(self):
        message = Reply.query.all()
        return message

    def query2(self, a):
        message = Reply.query.filter(Reply.replymatch_id == a).all()
        return len(message)

    def add(self, user_id, replymatch_id, replyuser_id, replyself_id, body):
        newReply = Reply(user_id=user_id, replymatch_id=replymatch_id, replyuser_id=replyuser_id, replyself_id=replyself_id, body=body)
        db.session.add(newReply)  # 添加数据
        db.session.commit()  # 提交事务

class Date(db.Model):
    __tablename__ = 'userdate'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    disnum = db.Column(db.String(100), default=0, server_default="0")
    matchnum = db.Column(db.String(100), default=0, server_default="0")
    seenum = db.Column(db.String(100), default=0, server_default="0")
    lovenum = db.Column(db.String(100), default=0, server_default="0")
    online = db.Column(db.String(10), default=0, server_default="0")
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    # user = db.relationship('Date', back_populates='user', uselist=False)


class QueryDate:
    def queryuser(self, a):
        query = Date.query.filter(Date.user_id == a).first()
        return query

    def queryuser2(self):
        query = Date.query.all()
        return query

    def add(self, user_id):
        newDate = Date(user_id=user_id)
        db.session.add(newDate)  # 添加数据
        db.session.commit()  # 提交事务

    def addall(self, user_id, disnum, matchnum, seenum, lovenum, online):
        newDate = Date(user_id=user_id, disnum=disnum, matchnum=matchnum, seenum=seenum, lovenum=lovenum, online=online)
        db.session.add(newDate)  # 添加数据
        db.session.commit()  # 提交事务

    def edit(self, disnum, matchnum, seenum, lovenum, user_id):
        newDate = Date.query.filter(Date.user_id == user_id).first()
        newDate.disnum = disnum
        newDate.matchnum = matchnum
        newDate.seenum = seenum
        newDate.lovenum = lovenum
        db.session.add(newDate)  # 添加数据
        db.session.commit()  # 提交事务

    def edit2(self, online, user_id):
        newDate = Date.query.filter(Date.user_id == user_id).first()
        newDate.online = online
        db.session.add(newDate)  # 添加数据
        db.session.commit()  # 提交事务


class PrivateMessage(db.Model):
    __tablename__ = 'ptmsg'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    recevice_id = db.Column(db.Integer)
    body = db.Column(db.TEXT)
    onlySigns = db.Column(db.String(50))
    tfred = db.Column(db.Integer)
    postTime = db.Column(db.DateTime, default=datetime.now)


class QueryPM:
    def queryself(self, recevice_id, a):
        query = PrivateMessage.query.filter(PrivateMessage.recevice_id == recevice_id).paginate(a, per_page=10,  error_out=False)
        return query

    def querySign(self, sign):
        query = PrivateMessage.query.filter(PrivateMessage.onlySigns == sign).all()
        return query

    def queryall(self):
        query = PrivateMessage.query.all()
        return query

    def add(self, user_id, recevice_id, body, onlySigns, tfred):
        newDate = PrivateMessage(user_id=user_id, recevice_id=recevice_id, body=body, onlySigns=onlySigns, tfred=tfred)
        db.session.add(newDate)  # 添加数据
        db.session.commit()  # 提交事务

    def edit(self, PMid, user_id, recevice_id, tfred):
        newDate = PrivateMessage.query.filter(PrivateMessage.user_id == user_id and
                                              PrivateMessage.recevice_id == recevice_id and PrivateMessage.id == PMid).first()
        newDate.tfred = tfred
        db.session.add(newDate)  # 添加数据
        db.session.commit()  # 提交事务


class Livelift(db.Model):
    __tablename__ = 'livelift'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user_name = db.Column(db.String(50))
    body = db.Column(db.TEXT)
    imgurl = db.Column(db.String(200))
    postTime = db.Column(db.DateTime, default=datetime.now)


class QueryLvLf:
    def queryall(self):
        query = Livelift.query.all()
        return query

    def add(self, user_id, user_name, body, imgurl):
        newData = Livelift(user_id=user_id, user_name=user_name, body=body, imgurl=imgurl)
        db.session.add(newData)  # 添加数据
        db.session.commit()  # 提交事务

    def query(self, a):
        query = Livelift.query.order_by(Livelift.postTime.desc()).paginate(a, per_page=3,  error_out=False)
        return query



