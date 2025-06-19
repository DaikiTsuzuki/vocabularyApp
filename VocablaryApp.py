import tkinter as tk
import random as rd
import csv

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.master.geometry("600x200")
        self.master.title("単語テスト")

        self.canvas = tk.Canvas(self.master, bg = "white", width = 50, height = 50)
        self.canvas.place(x = 30,y = 135)

        self.count = 1

        self.WordInput()
        self.SetVar()
        self.WordShuffle()
        self.widget()

        self.times = self.end - self.start

        self.judge_count = 1

        self.master.bind("<Return>", self.EnterJudge)
        self.master.bind("<KeyPress-z>", self.Insert1)
        self.master.bind("<KeyPress-x>", self.Insert2)
        self.master.bind("<KeyPress-c>", self.Insert3)
        self.master.bind("<KeyPress-v>", self.Insert4)
        self.master.bind("<KeyPress-1>", self.Insert1)
        self.master.bind("<KeyPress-2>", self.Insert2)
        self.master.bind("<KeyPress-3>", self.Insert3)
        self.master.bind("<KeyPress-4>", self.Insert4)

    def SetVar(self):
        self.judgeNum = -1
        self.num = 0
########出題範囲#####################################################
        self.start = 0
        self.end = self.start + 100
        #self.end = len(self.wordlist)
####################################################################
########ファイル選択##############################################
    def WordInput(self):
        #f = open("1dokken5Q.csv","r",encoding = "utf-8-sig") # 574
        #f = open("1dokken4Q.csv","r",encoding = "utf-8-sig") # 517
        #f = open("1GOETHE-ZERTIFIKAT A1.csv","r",encoding = "utf-8-sig") # 680
        f = open("1GOETHE-ZERTIFIKAT A2.csv","r",encoding = "utf-8-sig") # 590

        #f = open("2TOEFL_101_basic.csv","r",encoding = "utf-8-sig") #404
        #f = open("2TOEFL_102_basic.csv","r",encoding = "utf-8-sig") #404
        #f = open("2TOEFL_103_basic.csv","r",encoding = "utf-8-sig") #404
        #f = open("2TOEFL_104_basic.csv","r",encoding = "utf-8-sig") #404
        #f = open("2TOEFL_105_basic.csv","r",encoding = "utf-8-sig") #403
        #f = open("2TOEFL_111_intermediate.csv","r",encoding = "utf-8-sig") #486
        #f = open("2TOEFL_112_intermediate.csv","r",encoding = "utf-8-sig") #486
        #f = open("2TOEFL_113_intermediate.csv","r",encoding = "utf-8-sig") #485
        #f = open("2TOEFL_121_advanced.csv","r",encoding = "utf-8-sig") #439
        #f = open("2TOEFL_122_advanced.csv","r",encoding = "utf-8-sig") #439
        #f = open("2TOEFL_123_advanced.csv","r",encoding = "utf-8-sig") #439
        #f = open("2TOEFL_124_advanced.csv","r",encoding = "utf-8-sig") #438

        #f = open("2TOEIC1_basic1.csv","r",encoding = "utf-8-sig") #385
        #f = open("2TOEIC1_basic2.csv","r",encoding = "utf-8-sig") #385
        #f = open("2TOEIC1_basic3.csv","r",encoding = "utf-8-sig") #385
        #f = open("2TOEIC1_basic4.csv","r",encoding = "utf-8-sig") #384     
        #f = open("2TOEIC2_intermediate1.csv","r",encoding = "utf-8-sig") #386
        #f = open("2TOEIC2_intermediate2.csv","r",encoding = "utf-8-sig") #385
        #f = open("2TOEIC3_advanced1.csv","r",encoding = "utf-8-sig") #384 

        #f = open("2IELTS1_basic1.csv","r",encoding = "utf-8-sig") #878
        #f = open("2IELTS1_basic2.csv","r",encoding = "utf-8-sig") #878
        #f = open("2IELTS1_basic3.csv","r",encoding = "utf-8-sig") #878
        #f = open("2IELTS1_basic4.csv","r",encoding = "utf-8-sig") #879
        #f = open("2IELTS2_intermediate1.csv","r",encoding = "utf-8-sig") #523
        #f = open("2IELTS2_intermediate2.csv","r",encoding = "utf-8-sig") #522
        #f = open("2IELTS2_intermediate3.csv","r",encoding = "utf-8-sig") #522
        #f = open("2IELTS3_advanced1.csv","r",encoding = "utf-8-sig") #684 
        #f = open("2IELTS3_advanced2.csv","r",encoding = "utf-8-sig") #682 
        #f = open("2IELTS3_advanced3.csv","r",encoding = "utf-8-sig") #682

        #f = open("2eiken_pre1Q.csv","r",encoding = "utf-8-sig") #2184
        #f = open("2eiken_1Q.csv","r",encoding = "utf-8-sig") #2172

        self.wordlist = list(csv.reader(f))

        f.close()
#################################################################

    def WordShuffle(self):
        self.wordlist = self.wordlist[self.start:self.end]
        rd.shuffle(self.wordlist)
        self.wrongword = []

    #部品の配置↓

    def widget(self):

        self.txt1 = tk.Entry(self.master, width = 33)
        self.txt1.place(x = 50, y = 30)

        self.txt1.insert(0,self.wordlist[self.num][0])

        self.txt2 = tk.Entry(self.master, width = 33)
        self.txt2.place(x = 50, y = 90)

        self.BtnJudge = tk.Button(self.master, text = "判定", command = self.ClickJudge, width = 10)
        self.BtnJudge.place(x = 110, y = 148)

        self.BtnNext = tk.Button(self.master, text = "次の単語", command = self.Next, width = 10)
        self.BtnNext.place(x = 215, y = 148)

        self.counter = tk.Label(self.master, text = str(self.count) + "問目")
        self.counter.place(x = 80, y = 6)

        self.select4()#4択


    #部品の配置↑


    #4択の表示↓
    def select4(self):

        rdNum = rd.randint(0,3)
        lbl_x = 280
        lbl_y = 15

        self.Rdlist()

        for i in range(4):

            if i == 0:
                if i == rdNum:
                    self.lbl1 = tk.Label(self.master, text = str(1)  + " . " + self.wordlist[self.num][1])
                    self.lbl1.place(x = lbl_x, y = lbl_y + i * 30)
                    self.answerNum = 1
                else:
                    self.lbl1 = tk.Label(self.master, text = str(1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl1.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 1:
                if i == rdNum:
                    self.lbl2 = tk.Label(self.master, text = str(2)  + " . " + self.wordlist[self.num][1])
                    self.lbl2.place(x = lbl_x, y = lbl_y + i * 30)
                    self.answerNum = 2
                else:
                    self.lbl2 = tk.Label(self.master, text = str(2) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl2.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 2:
                if i == rdNum:
                    self.lbl3 = tk.Label(self.master, text = str(3) + " . " + self.wordlist[self.num][1])
                    self.lbl3.place(x = lbl_x, y = lbl_y + i * 30)
                    self.answerNum = 3
                else:
                    self.lbl3 = tk.Label(self.master, text = str(3) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl3.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 3:
                if i == rdNum:
                    self.lbl4 = tk.Label(self.master, text = str(4) + " . " + self.wordlist[self.num][1])
                    self.lbl4.place(x = lbl_x, y = lbl_y + i * 30)
                    self.answerNum = 4
                else:
                    self.lbl4 = tk.Label(self.master, text = str(4) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl4.place(x = lbl_x, y = lbl_y + i * 30)


    def Rdlist(self):
        self.rdlist = list(range(len(self.wordlist)))
        rd.shuffle(self.rdlist)
        self.rdlist.remove(self.wordlist.index(self.wordlist[self.num]))

    def select4_destroy(self):
        self.lbl1.destroy()
        self.lbl2.destroy()
        self.lbl3.destroy()
        self.lbl4.destroy()

    #4択の表示↑

    def Insert1(self, event):
        self.txt2.delete(0,tk.END)
        self.txt2.insert(0,1)
    def Insert2(self, event):
        self.txt2.delete(0,tk.END)
        self.txt2.insert(0,2)
    def Insert3(self, event):
        self.txt2.delete(0,tk.END)
        self.txt2.insert(0,3)
    def Insert4(self, event):
        self.txt2.delete(0,tk.END)
        self.txt2.insert(0,4)

    #判定↓

    def Judge(self):
        ans = int(self.txt2.get())
        if ans == self.answerNum:
            self.marupro()
        else:
            self.batsupro()

    def ClickJudge(self):
        self.Judge()
        #print("ClickJudge" , self.judgeNum)

    def EnterJudge(self, event):
        #print("EnterJudge", self.judgeNum)
        if self.judgeNum == -1:
            self.Judge()
        elif self.judgeNum == 2 and self.miss > 0:
            self.Retry()
        elif self.judgeNum == 2 and self.miss == 0:
            self.Finish()
        else:
            self.Next()

    def marupro(self):
        self.canvas.delete("batsu1")
        self.canvas.delete("batsu2")
        self.judgeNum = 1
        #print("正解")
        self.canvas.create_oval(10,10,43,43,outline = "red", width = 5, tag = "maru")

        self.judge_count = 1

    def batsupro(self):
        #print("不正解")
        self.canvas.create_line(10,10,43,43,fill = "black", width = 5, tag = "batsu1")
        self.canvas.create_line(10,43,43,10,fill = "black", width = 5, tag = "batsu2")
        self.txt2.delete(0,tk.END)

        if self.judge_count == 1:
            self.wrongword.append(self.wordlist[self.num])
            self.judge_count = -1


    #判定↑


    def Next(self):
        if self.count < self.times:
            if self.judgeNum == 1:
                self.canvas.delete("maru")

                self.num += 1

                self.txt1.delete(0,tk.END)
                self.txt2.delete(0,tk.END)
                self.txt1.insert(0,self.wordlist[self.num][0])

                self.select4_destroy()
                self.select4()

                self.judgeNum = -1
                self.count += 1

                self.counter.destroy()
                self.counter = tk.Label(self.master, text = str(self.count) + "問目")
                self.counter.place(x = 80, y = 6)

        else:
            self.BtnFinish = tk.Button(self.master, text = "終了", command = self.Finish, width = 10)
            self.BtnFinish.place(x = 110, y = 148)
            self.BtnNext.destroy()
            self.miss = len(self.wrongword)
            self.miss_count = tk.Label(self.master, text = str(self.miss) + "問ミス")
            self.miss_count.place(x = 110, y = 118)

            self.judgeNum = 2

            if self.miss > 0:
                self.BtnRetry = tk.Button(self.master, text = "間違えた問題をもう一度", command = self.Retry, width = 20)
                self.BtnRetry.place(x = 215, y = 148)


    def Finish(self):
        self.master.destroy()

    def Retry(self):

        self.times = len(self.wrongword)
        self.count = 0
        self.num = -1
        self.miss = 0
        self.judgeNum = 1

        self.miss_count.destroy()
        self.BtnFinish.destroy()
        self.BtnRetry.destroy()
        self.counter.destroy()

        self.wordlist1 = self.wrongword + self.wordlist
        self.wordlist = []
        for line in self.wordlist1:
            if line not in self.wordlist:
                self.wordlist.append(line)
        self.wrongword.clear()

        self.Next()
        
        self.BtnJudge = tk.Button(self.master, text = "判定", command = self.ClickJudge, width = 10)
        self.BtnJudge.place(x = 110, y = 148)

        self.BtnNext = tk.Button(self.master, text = "次の単語", command = self.Next, width = 10)
        self.BtnNext.place(x = 215, y = 148)

        self.counter = tk.Label(self.master, text = str(self.count) + "問目")
        self.counter.place(x = 80, y = 6)

    

def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()


if __name__ == "__main__":

    main()
