while true; do
  inotifywait -r -e modify,attrib,close_write,move,create,delete ./
  git add .
  git commit -m "Auto commit"au
  git push origin main
  inotifywait -r -e modify,attrib,close_write,move,create,delete ./
  git pull origin main
done