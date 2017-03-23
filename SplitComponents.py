import sublime
import sublime_plugin

class SplitComponents(sublime_plugin.EventListener):

	# type files
	extensions = ['vue', 'ng', 'md']
	# original layout
	original_layout = {'cells': [[0, 0, 1, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, 1.0]}
	# SplitComponents layout
	layout = {"cols": [0.0, 0.5, 1.0],"rows": [0.0, 0.7, 1.0],"cells": [[0, 0, 2, 1], [0, 1, 1, 2], [1, 1, 2, 2]]}

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
		print("handle")
		try:

			# verify available extensions
			for extension in self.extensions:

				try:
					#verify if is a known type file
					if extension == sublime.active_window().extract_variables()['file_extension']:
						print("debug setting layout")
						sublime.active_window().set_layout(self.layout)
						break

					if self.original_layout != sublime.active_window().get_layout():
						print("debug set original layout")
						sublime.active_window().set_layout(self.original_layout)

						# set new original layout
						self.original_layout = sublime.active_window().get_layout()
						break

				except KeyError as error:
					print("Error to change layout")

		except KeyError as error:
			print("Error to recognize file extension")

