start-dev-server:
  python app/main.py

start-css-compiler:
  cd tailwindcss && tailwindcss -i input.css -c ../tailwind.config.js -o ../static/css/style.css --watch
