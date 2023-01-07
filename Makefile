pybabel-extract:
	pybabel extract . -F babel.cfg -o messages.pot

pybabel-init:
	pybabel init -i messages.pot -d locales -l hu

pybabel-update:
	pybabel update -i messages.pot -d locales

pybabel-compile:
	pybabel compile -d locales

css-compile:
	cd tailwindcss && tailwindcss -i input.css -o ../static/css/style.css --minify

compile:
	make pybabel-compile && make css-compile