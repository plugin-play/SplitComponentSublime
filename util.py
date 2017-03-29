from io import StringIO
from lxml import etree

def parser(content):
	output = {
		'template': [],
		'script': [],
		'style': []
	}

	# parser
	parser = etree.HTMLParser()

	# an object dom
	fragment = etree.parse(StringIO(content), parser).getroot().find('body')

	for node in fragment:
		type = node.tag
		src = node.get('src')
		content = node.text
		
		if(type == 'template'):
			content = "".join([etree.tostring(e).decode('utf-8') for e in node])

		if( type not in output ):
			break

		if(type in ['script', 'template'] and len(output[type]) > 0):
			print('Only on script or tempalte tag is allowed')

		if(src):
			content = 'Should find file content...'

		output[type].append(content)

	return output