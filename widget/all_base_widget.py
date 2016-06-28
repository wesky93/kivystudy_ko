import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.slider import Slider

"""
kivy에서 가장 기본적으로 사용되는 위젯들을 모두 구현한 것입니다.
add_widget()을 이용하여 화면에 추가하였으며
다음 강좌는 이렇게 한것을 kv언어로 구현하는것을 보여 드릴 예정입니다.
"""

# 프로그램에 사용할 소스입니다.
font = "./fonts/NanumBarunGothic.ttf"
img = "./data/python.png"
video = ""
def Wname(wname):
    """
    위젯 이름을 넘겨주면 자동으로 설명 라벨을 만들어줌
    :param wname:
    :return:
    """
    l = Label(text="이것은 {} 위젯입니다.".format(wname),font_name=font)
    return l


class MyApp(App):
    def build(self):
        # 테스트에 사용할 위젯 불러오기
        W_label = Label(text="텍스트를 띄울떈\n라벨위젯을 쓰세요.",font_name=font)
        W_button = Button(text="이벤트를 유발시킬땐\n버튼위젯이 제격이죠.",font_name=font)
        W_checkbox_T = CheckBox(active=True)
        W_checkbox_F = CheckBox(active=False)
        W_radio1 = CheckBox(active=True,group="radio")
        W_radio2 = CheckBox(active=False,group="radio")
        W_image = Image(source=img)
        W_slider = Slider(min=0,max=100,value=30)

        """
        W_pbar =
        W_input =
        W_toggle =
        W_switch =
        W_video =
        """

        # 레이아웃 구성
        layout = GridLayout(cols=3, row_default_height=40)

        layout.add_widget(Label(text="1행",font_name=font))
        layout.add_widget(W_label)
        layout.add_widget(Wname("라벨"))

        layout.add_widget(Label(text="2행", font_name=font))
        layout.add_widget(W_button)
        layout.add_widget(Wname("버튼"))

        layout.add_widget(Label(text="3행", font_name=font))
        layout.add_widget(W_checkbox_T)
        layout.add_widget(Wname("기본값이 참인 \n체크박스"))

        layout.add_widget(Label(text="4행", font_name=font))
        layout.add_widget(W_checkbox_F)
        layout.add_widget(Wname("기본값이 거짓인 \n체크박스"))

        layout.add_widget(Label(text="5행", font_name=font))
        W_radiobox = BoxLayout()
        W_radiobox.add_widget(W_radio1)
        W_radiobox.add_widget(W_radio2)
        layout.add_widget(W_radiobox)
        layout.add_widget(Wname("체크박스를 그룹으로 묶은 \n라디오버튼"))

        layout.add_widget(Label(text="6행", font_name=font))
        layout.add_widget(W_image)
        layout.add_widget(Wname("이미지를 뿌리는\n이미지"))

        layout.add_widget(Label(text="7행", font_name=font))
        layout.add_widget(W_slider)
        layout.add_widget(Wname("{}을 가르키는\n슬라이더".format(W_slider.value_pos)))
        # 그리드 레이아웃으로 컬럼 2개로 잡음
        # add_widget으로 각종 위젯들을 차례대로 넣어줌
        return layout

if __name__ == '__main__':
    MyApp().run()
