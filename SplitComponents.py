import sublime
import sublime_plugin

class SplitComponents(sublime_plugin.EventListener):

	# type files ###Extension 'md' is used for test
	extensions = ['vue', 'ng', 'md']
	# original layout
	original_layout = sublime.active_window().get_layout()
	# SplitComponents layout
	layout = {"cols": [0.0, 0.5, 1.0],"rows": [0.0, 0.6, 1.0],"cells": [[0, 0, 2, 1], [0, 1, 1, 2], [1, 1, 2, 2]]}

	# show console message
	print("............::::::::| SplitComponents | Started |::::::::............")

	# listeners of user actions
	def on_activated_async(self, view):
	    self.handle()

	def on_load_async(self, view):
		self.handle()

	def on_clone_async(self, view):
		self.handle()

	def on_new_async(self, view):
		self.handle()

	# controller
	def handle(self):
		print("debug handle")

		# flag to indicate known extension
		known_extension = False

		try:

			# verify available extensions
			for extension in self.extensions:
				print(sublime.active_window().get_layout())
				try:
					#verify if is a known type file
					if extension == sublime.active_window().extract_variables()['file_extension'] and self.layout != sublime.active_window().get_layout():
						print("debug setting layout")

						# save actual layout
						self.original_layout = sublime.active_window().get_layout()

						# set Split layout
						sublime.active_window().set_layout(self.layout)

						# set new files in the tabs and set names
						known_extension = True
						break

				except KeyError as error:
					print(error)
					print("Error to change layout")

			# if isn't a known extension and split layout is set, back to original layout
			if False == known_extension and self.layout == sublime.active_window().get_layout():
				print("debug set original layout")
				sublime.active_window().set_layout(self.original_layout)

		except KeyError as error:
			print(error)
			print("Error to recognize file extension")

