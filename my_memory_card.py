from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QRadioButton,QPushButton, QGroupBox,QButtonGroup
from random import shuffle

class Question():
    def __init__(self,question1,right_answer,wrong1,wrong2,wrong3):
        self.question = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list=[]

question_list.append(Question("Koliko je 3+3?","6","3","4","5"))
question_list.append(Question("Kada je poceo prvi sv. rat?","1914","1918","1256","1915"))
question_list.append(Question("Kog dana je praznik rada?","1.maj","5.maj","8.maj","19.maj"))




app = QApplication([])
my_win = QWidget()

my_win.setWindowTitle("Memory Card")

question = QLabel("Which nationality does not exist?")
answer_btn = QPushButton("Answer")

RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton("Enets")
rbtn_2 = QRadioButton("Smurfs")
rbtn_3 = QRadioButton("Chulyms")
rbtn_4 = QRadioButton("Aleuts")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)





vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
hline = QHBoxLayout()

vline1.addWidget(rbtn_1)
vline1.addWidget(rbtn_2)
vline2.addWidget(rbtn_3)
vline2.addWidget(rbtn_4)

hline.addLayout(vline1)
hline.addLayout(vline2)

RadioGroupBox.setLayout(hline)


AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel("Are you correct or not?")
lb_Correct = QLabel("the answer will be here!")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()




hl1 = QHBoxLayout()
hl2 = QHBoxLayout()
hl3 = QHBoxLayout()
vl1 = QVBoxLayout()


hl1.addWidget(question, alignment = (Qt.AlignHCenter| Qt.AlignVCenter))
hl2.addWidget(RadioGroupBox)
hl2.addWidget(AnsGroupBox)


hl3.addStretch(1)
hl3.addWidget(answer_btn, stretch=2)
hl3.addStretch(1)

vl1.addLayout(hl1,stretch=2)
vl1.addLayout(hl2,stretch=8)
vl1.addStretch(1)
vl1.addLayout(hl3,stretch=1)
vl1.addStretch(1)

vl1.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer_btn.setText("Next question")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer_btn.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_asnwer():
    if answers[0].isChecked():
        show_correct("Correct")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect")

def next_question():
    my_win.cur_question = my_win.cur_question + 1
    if my_win.cur_question >= len(question_list):
        my_win.cur_question = 0
    q= question_list[my_win.cur_question]
    ask(q)

def click_OK():
    if answer_btn.text() == "Answer":
        check_asnwer()
    else:
        next_question()



my_win.setLayout(vl1)
my_win.cur_question = -1
answer_btn.clicked.connect(click_OK)
my_win.show()
app.exec()
