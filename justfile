start-dev-server:
  python app/main.py

start-css-compiler:
	tailwindcss -i tailwindcss/input.css -c tailwind.config.js -o static/css/style.css --watch

