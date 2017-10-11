import time
import os

class LedControler:

	def __init__(self):
		print('init')

	def on(self):
		print('on')

	def off(self):
		print('off')

	def ll(self):
		data = os.listdir('.')
		return data
