import pymysql


class DBHelper:
    # 构造函数
    def __init__(self, host='127.0.0.1', user='root', pwd='123456', db='test'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.user, self.pwd, self.db, charset='utf8')
        except:
            print(self.conn.Error)
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def closeDatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    #执行
    def function(self, sql):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql)
                self.conn.commit()
        except:
            # self.closeDatabase()
            print(self.cur.execute(sql))
            self.conn.rollback()
        finally:
            self.closeDatabase()
        return True

    # 查询数据
    def search_data(self, id):
        myid=''
        total = ''
        frontpath = ''
        backpath = ''
        sql = "select * from student where id='%s'" % (id)
        self.function(sql)
        # cur 操作游标
        result = self.cur.fetchall()
        # 遍历结果
        # print("学号", "总分", "试卷正面", "试卷背面")
        # id,total,blank,question1,question2,question3,question4,question5,question6,frontpath,backpath
        for row in result:
            myid = row[0]
            total = row[1]
            frontpath = row[2]
            backpath = row[3]
            print(id, total, frontpath, backpath)
        return myid, total, frontpath, backpath

        # 查询全部数据
    def search_all(self):
        myid=''
        total = ''
        frontpath = ''
        backpath = ''
        sql = "select id,total from student"
        self.function(sql)
        # cur 操作游标
        result = self.cur.fetchall()
        # 遍历结果
        # print("学号", "总分", "试卷正面", "试卷背面")
        # id,total,blank,question1,question2,question3,question4,question5,question6,frontpath,backpath
        return result

    # 添加数据
    def add_data(self, id, total, frontpath, backpath):
        flag, a, b, c = self.search_data(id)
        print(flag)
        if(flag == ''):
            sql = "insert into student(id, total, frontpath, backpath) values (%s, %s, '%s', '%s')" % (id, total, frontpath, backpath)
            print("added")
            self.function(sql)
            return True
        else:
            self.update_data(id, total, frontpath, backpath)
            print("update")
            return False

    # 删除数据
    def delete_data(self, id):
        sql = "delete from student where id = %s" % (id)
        self.function(sql)

    # 更新数据
    def update_data(self, id, total, frontpath, backpath):
        sql = "update student set  total = %s , frontpath='%s', backpath='%s' where id = %s" % (total, frontpath, backpath, id)
        self.function(sql)






