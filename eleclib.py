import sqlite3
import sys

connection = sqlite3.connect("eleclib.db")
cursor = connection.cursor()


class Lib(object):
    def __init__(self, c):
        self.__c = c

    def ui(self):
        print("请输入需要的服务序号",
              "1：按书名查找",
              "2：按作者查找",
              "3：按类型查找",
              "0: 退出程序")
        num = input()
        if num == '1':   #功能1按照书名查找
            self.findbytitle()
        elif num == '2':    #功能2按照作者查找
            print("author")
            self.findbyauthor()
        elif num == '3':
            print("type")
            self.printtype()
        elif num == '0':
            sys.exit(0)
        else:
            print("useless input")
            self.ui()

    def continue_use(self):         #交互：是否继续使用
        print("是否继续使用？(yes/no)")
        command = input()
        if command == 'yes':
            self.ui()
        elif command == 'no':
            sys.exit(0)
        else:
            print("请输入正确的指令")
            self.continue_use()

    def findbytitle(self):              #按照书名查找
        con = []
        print("input the title")
        title = '《' + input() + '》'
        con.append(title)       #对输入加双引号后，转成list
        result = self.__c.execute("select * from mainstorage where title = ?;", con)   #sqlite查询
        x = 0
        for i in result:        #sqlite如果返回为空，则i为0，将显示无此项并提供返回主界面的询问；如果不为空则进入显示结果
            x = 1
        result = self.__c.execute("select * from mainstorage where title = ?;", con)
        if x == 1:          #查询结果不为空，显示结果
            for inf in result:
                print(1)
                print("title :" + inf[0] + '\n',
                      "author :" + inf[1] + '\n',
                      "type :" + inf[2] + '\n',
                      "introduction :" + inf[3] + '\n'
                      )
            self.continue_use()
        else:       #查询结果为空，返回主界面
            print("no such title in the mainstorage \n back to the main interface")
            self.continue_use()

    def findbyauthor(self):
        print("input the author")
        con = [input()]     #将输入转为list
        result = self.__c.execute("select title, type from mainstorage where author = ?;", con)
        x = 0
        for i in result:        #查询结果为空则为0，显示无此信息并询问是否返回主界面，否则为1，显示结果
            x = 1
        result = self.__c.execute("select title, type from mainstorage where author = ?;", con)
        if x == 1:              #查询结果不为空，循环显示所有结果
            for inf in result:
                print("title :", inf[0], '\n'
                      "type :", inf[1], '\n')
            self.continue_use()
        else:           #查询结果为空，询问是否返回主界面
            print("no suach author \n back to the main interface")
            self.continue_use()


test = Lib(cursor)
test.ui()

