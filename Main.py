import random
from win11toast import notify

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import UI


class seat:
    def __init__(self):
        self.__state = "empty"
        self.__obj = None

    def setPeople(self,people):
        self.__state = "Yes"
        self.__obj = people



    def getState(self):
        return self.__state


    def getPeople(self):
        return self.__obj


def ShowGraph(seats):
    girl =  ["😘"]
    handsome = "😀"
    ugly = "😭"
    blank = "💺"
    result = ""
    AngerEmoj = ["🤮"]

    for a in range(0,len(seats)):
        for b in range(0,len(seats[a])):
            if seats[a][b].getState() == "empty":
                result += blank
            else:
                if seats[a][b].getPeople().getGender() == "M":
                    if seats[a][b].getPeople().getFace() == "一般":
                        result += ugly
                    else:
                        result += handsome
                else:
                    if seats[a][b].getPeople().getEmotion() =="Happy":
                        result += random.choice(girl)
                    else:
                        result += random.choice(AngerEmoj)

        result+="\n"

    return result

class Boy:
    def __init__(self,name):
        self.__face = ""
        self.gender = "M"
        self.__name = name


    def setFace(self,aFace):
        self.__face = aFace

    def getFace(self):
        return self.__face

    def getName(self):
        return self.__name

    def getGender(self):
        return self.gender

class Girl:
    def __init__(self):
        self.gender = "F"
        self.__ResponsePositive = ["嗨帅哥!","帅哥，认识一下","帅哥，加一下微信"]
        self.__ResponseNegative = ["切...","哦，你有事情吗","你可以往那边挪一下吗？"]
        self.__state = "stand"
        self.__seatIndex = 0
        self.__GirlsIdentity = random.randint(1000,2000)
        self.__wantIndex = 0
        self.__heatIndex = 0
        self.__emotion = ""

    def setEmotion(self,emo):
        self.__emotion = emo

    def getEmotion(self):
        return self.__emotion

    def getGender(self):
        return self.gender

    def getIdentity(self):
        return self.__GirlsIdentity

    def Behaviour(self,seats,Girl,allocate):
        ugly_seats = []
        handsome_seats = []
        direction = ["L","R","U","D","Rand"]

        row = len(seats)
        colum = len(seats[0])

        #获取横排
        for a in range(row):
            for b in range(colum):
                if seats[a][b].getState() == "Yes":
                    if seats[a][b].getPeople().getGender() == "M":
                        if seats[a][b].getPeople().getFace() == "一般":
                            if b == 0:
                                ugly_seats.append([a,b+1])
                            elif b == colum -1:
                                ugly_seats.append([a,b-1])
                            else:
                                ugly_seats.append([a, b + 1])
                                ugly_seats.append([a, b - 1])

        #获取竖排
        for a in range(row):
            for b in range(colum):
                if seats[a][b].getState() == "Yes":
                    if seats[a][b].getPeople().getGender() == "M":
                        if seats[a][b].getPeople().getFace() == "一般":
                            if a == 0:
                                ugly_seats.append([a+1,b])
                            elif a == row -1:
                                ugly_seats.append([a-1,b])
                            else:
                                ugly_seats.append([a - 1, b])
                                ugly_seats.append([a + 1, b])

        #所有帅哥位置
        for a in range(row):
            for b in range(colum):
                if seats[a][b].getState() == "Yes":
                    if seats[a][b].getPeople().getGender() == "M":
                        if seats[a][b].getPeople().getFace() == "帅":
                            handsome_seats.append([a,b])



        dir = random.choice(direction)
        goto = random.choice(handsome_seats)
        # print("选择方向: ",dir)
        # print("选择的帅哥",goto)

        isOk = False
        isFull = True
        for a in range(row):
            for b in range(colum):
                if seats[a][b].getState() == "empty":
                    isFull = False

        for a in range(row):
            for b in range(colum):
                if seats[a][b].getState() == "empty" and [a,b] not in ugly_seats:
                    isOk = True


        if not isFull:
            if isOk:
                Girl.setEmotion("Happy")

                if dir == "L":
                    isSeat = False

                    for a in range(goto[1] - 1, -1, -1):
                        if seats[goto[0]][a].getState() == "empty" and [goto[0], a] not in ugly_seats:
                            seats[goto[0]][a].setPeople(Girl)
                            print("坐在了: ", [goto[0], a])
                            isSeat = True
                            break
                    if not isSeat:
                        seat_a = 0
                        seat_b = 0
                        for a in range(row):
                            for b in range(colum):
                                if seats[a][b].getState() == "empty" and [a, b] not in ugly_seats:
                                    seat_a = a
                                    seat_b = b
                                    break
                        seats[seat_a][seat_b].setPeople(Girl)
                        print("坐在了: ", [seat_a, seat_b])
                elif dir == "R":
                    isSeat = False

                    for a in range(goto[1] + 1, row):
                        if seats[goto[0]][a].getState() == "empty" and [goto[0], a] not in ugly_seats:
                            seats[goto[0]][a].setPeople(Girl)
                            print("坐在了: ", [goto[0], a])
                            isSeat = True

                            break
                    if not isSeat:
                        seat_a = 0
                        seat_b = 0
                        for a in range(row):
                            for b in range(colum):
                                if seats[a][b].getState() == "empty" and [a, b] not in ugly_seats:
                                    seat_a = a
                                    seat_b = b
                                    break
                        seats[seat_a][seat_b].setPeople(Girl)
                        print("坐在了: ", [seat_a, seat_b])

                elif dir == "U":
                    isSeat = False
                    if goto[0] != 0:
                        for a in range(goto[0], -1, -1):
                            if seats[a][goto[1]].getState() == "empty" and [a, goto[1]] not in ugly_seats:
                                seats[a][goto[1]].setPeople(Girl)
                                print("坐在了: ", [a, goto[1]])
                                isSeat = True

                                break
                    if not isSeat:
                        seat_a = 0
                        seat_b = 0
                        for a in range(row):
                            for b in range(colum):
                                if seats[a][b].getState() == "empty" and [a, b] not in ugly_seats:
                                    seat_a = a
                                    seat_b = b
                                    break
                        seats[seat_a][seat_b].setPeople(Girl)
                        print("坐在了: ", [seat_a, seat_b])

                elif dir == "D":
                    isSeat = False
                    if goto[0] != 0:
                        for a in range(goto[0], colum):
                            if seats[a][goto[1]].getState() == "empty" and [a, goto[1]] not in ugly_seats:
                                seats[a][goto[1]].setPeople(Girl)
                                print("坐在了: ", [a, goto[1]])
                                isSeat = True
                                break
                    if not isSeat:
                        seat_a = 0
                        seat_b = 0
                        for a in range(row):
                            for b in range(colum):
                                if seats[a][b].getState() == "empty" and [a, b] not in ugly_seats:
                                    seat_a = a
                                    seat_b = b
                                    break
                        seats[seat_a][seat_b].setPeople(Girl)
                        print("坐在了: ", [seat_a, seat_b])



                elif dir == "Rand":
                    seat_a = 0
                    seat_b = 0
                    for a in range(row):
                        for b in range(colum):
                            if seats[a][b].getState() == "empty" and [a, b] not in ugly_seats:
                                seat_a = a
                                seat_b = b
                                break
                    seats[seat_a][seat_b].setPeople(Girl)
                    print("坐在了: ", [seat_a, seat_b])

            else:
                if allocate: #是否继续让丑男身边坐女孩？
                    seat_a = 0
                    seat_b = 0
                    for a in range(row):
                        for b in range(colum):
                            if seats[a][b].getState() == "empty":
                                seat_a = a
                                seat_b = b
                                break
                    Girl.setEmotion("Anger")
                    seats[seat_a][seat_b].setPeople(Girl)
                    print("坐在了: ", [seat_a, seat_b])
                else:
                    notify('女孩的消息','座位满了，没位置了！我也不想挨着长得不帅的男孩。看来我只能站着了')
        else:
            notify('系统', '所有座位已坐满')
        #
        # print("丑男旁边: ",ugly_seats)
        # print("帅哥位置: ",handsome_seats)

        ShowGraph(seats)
        return seats

    def ResponseToBoy(self):
        pass

class Mainwindow(QMainWindow, UI.Ui_MainWindow):
    aSeats = []
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.manyGirlSeat)
        self.pushButton_2.clicked.connect(self.singleGirlSeat)
        self.pushButton_3.clicked.connect(self.resetSeats)

        #丑男数量
        self.lineEdit.setText("3")
        #帅哥数量
        self.lineEdit_2.setText("5")


        #网格数量
        self.lineEdit_3.setText("8")
        self.lineEdit_5.setText("8")

        self.lineEdit_4.setText("2")



        inf = "图例:\n普男:😭\n帅哥:😀\n女孩:😘\n座椅:💺\n呕吐:🤮"
        self.label_7.setText(inf)

    def functions(self):
        print("OK")

    def manyGirlSeat(self):
        if self.checkBox.isChecked():
            for a in range(int(self.lineEdit_4.text())):
                aGirl = Girl()
                Mainwindow.aSeats = aGirl.Behaviour(Mainwindow.aSeats, aGirl,True)
            self.textEdit.setText(ShowGraph(Mainwindow.aSeats))
        else:
            for a in range(int(self.lineEdit_4.text())):
                aGirl = Girl()
                Mainwindow.aSeats = aGirl.Behaviour(Mainwindow.aSeats, aGirl,False)
            self.textEdit.setText(ShowGraph(Mainwindow.aSeats))



    def singleGirlSeat(self):
        if self.checkBox.isChecked():
            aGirl = Girl()
            Mainwindow.aSeats = aGirl.Behaviour(Mainwindow.aSeats, aGirl,True)
            self.textEdit.setText(ShowGraph(Mainwindow.aSeats))
        else:
            aGirl = Girl()
            Mainwindow.aSeats = aGirl.Behaviour(Mainwindow.aSeats, aGirl,False)
            self.textEdit.setText(ShowGraph(Mainwindow.aSeats))



    def resetSeats(self):
        Mainwindow.aSeats = []

        #生成座位
        for a in range(int(self.lineEdit_3.text())):
            temp = []
            for b in range(int(self.lineEdit_5.text())):
                seatObj = seat()
                temp.append(seatObj)
            Mainwindow.aSeats.append(temp)

        for a in range(int(self.lineEdit.text()) ):
            ugly = Boy("Jhon")
            ugly.setFace("一般")
            Mainwindow.aSeats[random.randint(0, int(self.lineEdit_3.text())-1)][random.randint(0,int(self.lineEdit_5.text())-1)].setPeople(ugly)

        for a in range(int(self.lineEdit_2.text())):
            handsome = Boy("Geo")
            handsome.setFace("帅")
            Mainwindow.aSeats[random.randint(0, int(self.lineEdit_3.text())-1)][random.randint(0,int(self.lineEdit_5.text())-1)].setPeople(handsome)



        self.textEdit.setText(ShowGraph(Mainwindow.aSeats))
        font = QFont("Arial", 15)  # 设置字体为 Arial，大小为 12
        self.textEdit.setFont(font)


def run():
    app = QApplication(sys.argv)
    mainWindow = Mainwindow()
    mainWindow.show()
    sys.exit(app.exec_())
run()
