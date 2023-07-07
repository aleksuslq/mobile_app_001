from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Розрахунок гіпсу"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

        OneLineListItem:
            text: "Розрахунок смоли"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"

        OneLineListItem:
            text: "Розрахунок модулів"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"

MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "Калькулятор Протезиста"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDBoxLayout:
			        orientation: "vertical"
			        spacing: "20dp"
			        adaptive_height: True
			        size_hint_x: .8
			        pos_hint: {"center_x": .5, "center_y": .5}

			        MDTextField:
			        	id:a
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір проксимального відділу кукси у см"

						on_text_validate : app.con()

                    MDTextField:
			            hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір дистального відділу кукси у см"



			        MDTextField:
			        	id:b
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір висоти кукси + 5 см при литті у см"

					    on_text_validate : app.con()			  






                MDLabel:
                    id:c
                    text: "Розрахунок гіпсу"
                    pos_hint: {"center_x": .7, "center_y": .9}


                MDLabel:

                    text: "Частка гіпсу"
                    pos_hint: {"center_x": .6, "center_y": .2}

                MDLabel:
                    id: c
                    text:  "грам"
                    pos_hint: {"center_x": .6, "center_y": .1}

                MDLabel:

                    text: "Частка води"
                    pos_hint: {"center_x": .9, "center_y": .2}

                MDLabel:
                    id: d
                    text: "грам"
                    pos_hint: {"center_x": .9, "center_y": .1}

            MDScreen:
                name: "scr 2"

                MDBoxLayout:
			        orientation: "vertical"
			        spacing: "20dp"
			        adaptive_height: True
			        size_hint_x: .8
			        pos_hint: {"center_x": .5, "center_y": .5}

			        MDTextField:
			        	id:aa
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір проксимального відділу кукси у см"

						on_text_validate : app.consm()

                    MDTextField:
                    	id:bb
			            hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір дистального відділу кукси у см"
			            on_text_validate : app.consm()


			        MDTextField:
			        	id:dd
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір висоти кукси + 5 см при литті у см"

					    on_text_validate : app.consm()
				    MDTextField:
			        	id:cc
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Вага пацієнта"

					    on_text_validate : app.consm()			  






                MDLabel:
                    id:ff
                    text: "Розрахунок смоли"
                    pos_hint: {"center_x": .7, "center_y": .9}


                MDLabel:

                    text: "Об'єм смоли"
                    pos_hint: {"center_x": .6, "center_y": .2}

                MDLabel:
                    id: ff
                    text: "грам"
                    pos_hint: {"center_x": .6, "center_y": .1}

                MDLabel:

                    text: "Частка затверджувача"
                    pos_hint: {"center_x": .9, "center_y": .2}

                MDLabel:
                    id: gg
                    text: "грам"
                    pos_hint: {"center_x": .9, "center_y": .1}







            MDScreen:
                name: "scr 3"

                MDBoxLayout:
			        orientation: "vertical"
			        spacing: "20dp"
			        adaptive_height: True
			        size_hint_x: .8
			        pos_hint: {"center_x": .5, "center_y": .5}

			        MDTextField:
			        	id:aaa
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір висоти туберу у см"

						on_text_validate : app.concl()

                    MDTextField:
                    	id:bbb
			            hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір висоти підлога-коліно у см"
					    on_text_validate : app.concl()



			        MDTextField:
			        	id:ccc
					    hint_text: "Введіть"
					    mode: "round"
					    max_text_length: 15
					    helper_text: "Замір висоти кукси у см"

					    on_text_validate : app.concl()			  






                MDLabel:

                    text: "Розрахунок висоти між куксоприймачем та підлога-коліно"
                    pos_hint: {"center_x": .7, "center_y": .9}


                MDLabel:

                    text: "Висота модулів"
                    pos_hint: {"center_x": .6, "center_y": .2}

                MDLabel:
                    id: ddd
                    text: "См."
                    pos_hint: {"center_x": .6, "center_y": .1}







        MDNavigationDrawer:
            id: nav_drawer
        	a:a
			b:b
			c:c
			d:d

			aa:aa
			bb:bb
			cc:cc
			dd:dd
			ff:ff
			gg:gg


			aaa:aaa
			bbb:bbb
			ccc:ccc
			ddd:ddd
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
            	a:a
				b:b
				c:c
				d:d

				aa:aa
				bb:bb
				cc:cc
				dd:dd
				ff:ff
				gg:gg


		        aaa:aaa
		        bbb:bbb
		        ccc:ccc
		        ddd:ddd

'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


#    a=ObjectProperty()
#    b=ObjectProperty()
#    c=ObjectProperty()
# def con(self):
#    	self.c.text=str(float(self.a.text)+float(self.b.text))


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        #   return Builder.load_string(KV)
        self.root = Builder.load_string(KV)

    a = ObjectProperty(None)
    b = ObjectProperty(None)
    c = ObjectProperty()
    d = ObjectProperty()

    aa = ObjectProperty(None)  # dl okr
    bb = ObjectProperty(None)  # 2dl okr
    cc = ObjectProperty(None)  # wes pac
    dd = ObjectProperty(None)  # visot
    ee = ObjectProperty(None)
    ff = ObjectProperty()
    gg = ObjectProperty()

    aaa = ObjectProperty(None)  # visota tuber
    bbb = ObjectProperty(None)  # pol koleno
    ccc = ObjectProperty(None)  # dlina ulkulti
    ddd = ObjectProperty()

    def con(self):
        # self.root.ids.c.text =str(float(self.root.ids.a.text )+float(self.root.ids.b.text ))
        self.root.ids.c.text = str(
            round(((((float(self.root.ids.a.text) / 3.14) / 2) ** 2) * 3.14 * float(self.root.ids.b.text)) * 0.5714))
        self.root.ids.d.text = str(
            round(((((float(self.root.ids.a.text) / 3.14) / 2) ** 2) * 3.14 * float(self.root.ids.b.text)) * 0.4286))

    def consm(self):
        self.root.ids.ff.text = str(round((((float(self.root.ids.aa.text) / 3.14) + (
                    float(self.root.ids.bb.text) / 3.14)) - (2 * ((float(self.root.ids.cc.text) / 20) / 10))) * 1.57 * (
                                                      float(self.root.ids.dd.text) * (
                                                          (float(self.root.ids.cc.text) / 20) / 10))))  # new solutio

        self.root.ids.gg.text = str(round(((((float(self.root.ids.aa.text) / 3.14) + (
                    float(self.root.ids.bb.text) / 3.14)) - (2 * ((float(self.root.ids.cc.text) / 20) / 10))) * 1.57 * (
                                                       float(self.root.ids.dd.text) * (
                                                           (float(self.root.ids.cc.text) / 20) / 10))) * 0.02))  ##

    def concl(self):
        self.root.ids.ddd.text = str(
            float(self.root.ids.aaa.text) - float(self.root.ids.bbb.text) - float(self.root.ids.ccc.text))  # n

    def lol(self, *args):
        self.root.ids.c.text = self.c
        self.root.ids.d.text = self.d
        self.root.ids.ff.text = self.ff
        self.root.ids.gg.text = self.gg


Example().run()