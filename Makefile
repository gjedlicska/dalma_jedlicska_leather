pybabel-extract:
	pybabel extract . -F babel.cfg -o messages.pot

pybabel-init:
	pybabel init -i messages.pot -d locales -l hu

pybabel-update:
	pybabel update -i messages.pot -d locales

pybabel-compile:
	pybabel compile -d locales

css-compile:
	tailwindcss -i tailwindcss/input.css -c tailwind.config.js -o ./static/css/style.css --minify

compile:
	make pybabel-compile && make css-compile
