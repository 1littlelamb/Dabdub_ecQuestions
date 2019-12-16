# Kivy Code to help visualize the problem

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout

class MyWidget(Widget):

	pass


class ChessBoardApp(App):

	def build(self):

#		x = 0
#		y = 0.1
#
		layout = FloatLayout()
#
#		buttons = [b11,b12,b13,b14,b15,b16,b17,b18,
#					b21,b22,b23,b24,b25,b26,b27,b28,
#					b31,b32,b33,b34,b35,b36,b37,b38,
#					b41,b42,b43,b44,b45,b46,b47,b48,
#					b51,b52,b53,b54,b55,b56,b57,b58,
#					b61,b62,b63,b64,b65,b66,b67,b68,
#					b71,b72,b73,b74,b75,b76,b77,b78,
#					b81,b82,b83,b84,b85,b86,b87,b88]
#
#		for i in buttons:
#			x += 0.1
#
#			if x % 0.8 == 0:
#				y += 0.1

#			i = ToggleButton(size_hint=(.1, .1), pos_hint={'x':x, 'y':y})
#			layout.add_widget(i)

		b11 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.1})
		layout.add_widget(b11)
		
		b12 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.2})
		layout.add_widget(b12)

		b13 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.3})
		layout.add_widget(b13)

		b14 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.4})
		layout.add_widget(b14)

		b15 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.5})
		layout.add_widget(b15)
		
		b16 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.6})
		layout.add_widget(b16)

		b17 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.7})
		layout.add_widget(b17)

		b18 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.1, 'y':.8})
		layout.add_widget(b18)

		b21 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.1})
		layout.add_widget(b21)
		
		b22 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.2})
		layout.add_widget(b22)

		b23 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.3})
		layout.add_widget(b23)

		b24 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.4})
		layout.add_widget(b24)

		b25 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.5})
		layout.add_widget(b25)
		
		b26 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.6})
		layout.add_widget(b26)

		b27 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.7})
		layout.add_widget(b27)

		b28 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.2, 'y':.8})
		layout.add_widget(b28)

		b31 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.1})
		layout.add_widget(b31)
		
		b32 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.2})
		layout.add_widget(b32)

		b33 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.3})
		layout.add_widget(b33)

		b34 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.4})
		layout.add_widget(b34)

		b35 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.5})
		layout.add_widget(b35)
		
		b36 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.6})
		layout.add_widget(b36)

		b37 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.7})
		layout.add_widget(b37)

		b38 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.3, 'y':.8})
		layout.add_widget(b38)

		b41 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.1})
		layout.add_widget(b41)
		
		b42 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.2})
		layout.add_widget(b42)

		b43 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.3})
		layout.add_widget(b43)

		b44 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.4})
		layout.add_widget(b44)

		b45 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.5})
		layout.add_widget(b45)
		
		b46 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.6})
		layout.add_widget(b46)

		b47 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.7})
		layout.add_widget(b47)

		b48 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.4, 'y':.8})
		layout.add_widget(b48)

		b51 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.1})
		layout.add_widget(b51)
		
		b52 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.2})
		layout.add_widget(b52)

		b53 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.3})
		layout.add_widget(b53)

		b54 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.4})
		layout.add_widget(b54)

		b55 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.5})
		layout.add_widget(b55)
		
		b56 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.6})
		layout.add_widget(b56)

		b57 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.7})
		layout.add_widget(b57)

		b58 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.5, 'y':.8})
		layout.add_widget(b58)

		b61 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.1})
		layout.add_widget(b61)
		
		b62 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.2})
		layout.add_widget(b62)

		b63 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.3})
		layout.add_widget(b63)

		b64 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.4})
		layout.add_widget(b64)

		b65 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.5})
		layout.add_widget(b65)
		
		b66 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.6})
		layout.add_widget(b66)

		b67 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.7})
		layout.add_widget(b67)

		b68 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.6, 'y':.8})
		layout.add_widget(b68)

		b71 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.1})
		layout.add_widget(b71)
		
		b72 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.2})
		layout.add_widget(b72)

		b73 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.3})
		layout.add_widget(b73)

		b74 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.4})
		layout.add_widget(b74)

		b75 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.5})
		layout.add_widget(b75)
		
		b76 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.6})
		layout.add_widget(b76)

		b77 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.7})
		layout.add_widget(b77)

		b78 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.7, 'y':.8})
		layout.add_widget(b78)

		b81 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.1})
		layout.add_widget(b81)
		
		b82 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.2})
		layout.add_widget(b82)

		b83 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.3})
		layout.add_widget(b83)

		b84 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.4})
		layout.add_widget(b84)

		b85 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.5})
		layout.add_widget(b85)
		
		b86 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.6})
		layout.add_widget(b86)

		b87 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.7})
		layout.add_widget(b87)

		b88 = ToggleButton(size_hint=(.1, .1), pos_hint={'x':.8, 'y':.8})
		layout.add_widget(b88)


		return layout


if __name__ == '__main__':
	ChessBoardApp().run()