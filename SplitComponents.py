import sublime
import sublime_plugin

class SplitComponents(sublime_plugin.EventListener):

	# type files ###Extension 'md' is used for test
	extensions = ['vue', 'ng', 'md']
	# extens? usada nos arquivos abertos nas abas, quando houver o split
	group_extension = '.sc'
	# original layout
	original_layout = sublime.active_window().get_layout()

	# nome e extensão do arquivo original .vue ou .ng
	original_file = {'name':'', 'ext':''}

	# SplitComponents layout
	layout = {"cols": [0.0, 0.5, 1.0],"rows": [0.0, 0.6, 1.0],"cells": [[0, 0, 2, 1], [0, 1, 1, 2], [1, 1, 2, 2]]}

	# conteúdo do arquivo .vue ou .ng
	file_content = {'js':[], 'template':[], 'css':[]}

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

			# @TODO
			# fazer uma verificação se a extensao do arquivo aberto é diferente aos arquivos abertos nas abas (.sc)
			if sublime.active_window().extract_variables()['file_extension'] != self.group_extension:

			# se sim, não entra para mudar a tela, se não é necessáio:
			# - Salvar o conteúdo das 3 abas em uma variável
			# - Apagar o conteúdo do arquivo original .vue ou .ng
			# - Injetar o conteúdo das 3 abas que está na variavel e salvar
			# - Fechar sem salvar os 3 arquivos que est? um em cada aba
			# - Retirar o split de 3 grupos (abas), deixando somente 1

				# verify available extensions
				for extension in self.extensions:
					# print(sublime.active_window().get_layout())

					try:
						#verify if is a known type file
						if extension == sublime.active_window().extract_variables()['file_extension'] and self.layout != sublime.active_window().get_layout():
							# print("debug setting layout")

							# @TODO talvez não será preciso guardar o layout anterior
							# save actual layout
							self.original_layout = sublime.active_window().get_layout()

							# @TODO
							# Salvar o nome do arquivo atual numa variáel ou num dicionario
							# Salvar a extensão do arquivo atual numa variável ou dicionario
							self.original_file['name'] = sublime.active_window().extract_variables()['file_base_name']
							self.original_file['ext'] = sublime.active_window().extract_variables()['file_extension']

							# Ler o arquivo atual e salvar em uma variavel
							file = open(sublime.active_window().extract_variables()['file'], 'r')
							content = file.readlines()

							js = None
							template = None
							css = None
							# print(content)

							# Identificar as partes no arquivo template, css e js
							for linha in content:

								# @TODO ajustar essas flags para um modelo mais moderno, ficou muito extenso
								#  Flags para ajudar na separacao do arquivo
								if linha.find('<template>') >= 0 :
									template =  True

								if linha.find('</template>') >= 0 :
									template =  False

								if linha.find('<style>') >= 0:
									css = True

								if linha.find('</style>') >= 0:
									css = False

								if linha.find('<script>') >= 0:
									js = True

								if linha.find('</script>') >= 0:
									js = False

								# Salva as linhas separadamente
								if True == js:
									self.file_content['js'].append(linha)

								if True == template:
									self.file_content['template'].append(linha)

								if True == css:
									self.file_content['css'].append(linha)

							file.close()

							print('arquivo js')
							print(self.file_content['js'])
							print()
							print('arquivo template')
							print(self.file_content['template'])
							print()
							print('arquivo css')
							print(self.file_content['css'])

							# Fechar o arquivo atual

							# Fazer o split na tela 3 grupos
							sublime.active_window().set_layout(self.layout)

							# Criar 3 arquivos com a extensao .sc (splitcomponents). Um em cada group (aba). Os arquivos dao nome a aba
							# Injetar os dados que foram separados, um em cada aba

							# @TODO talvez n? preciso guardar na flag se ja tem um arquivo do tipo .vue, .ng aberto
							# set new files in the tabs and set names
							known_extension = True
							break

					except KeyError as error:
						print(error)
						print("Error to change layout")

			# if isn't a known extension and split layout is set, back to original layout
			if False == known_extension and self.layout == sublime.active_window().get_layout():
				# print("debug set original layout")
				sublime.active_window().set_layout(self.original_layout)

		except KeyError as error:
			print(error)
			print("Error to recognize file extension")

