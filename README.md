create a environment : python3 -m venv venv
activate env : source venv/bin/activate

install dependency : pip install fastapi uvicorn
make dep file : pip freeze > requirements.txt

pip3 install requests or pip install requests

run file wiht uvicorn : uvicorn main:app --reload

git commit --allow-empty -m "trigger build"
git push origin main

For PROD : export ENV=production

For DEV : export ENV=development

uvicorn app.main:app --reload

on server
pm2 restart fast-api-python --update-env

kill -9 $(lsof -t -i:8000)

pm2 start /var/www/fast-api-python/venv/bin/uvicorn \
--name fast-api-python \
--cwd /var/www/fast-api-python \
--interpreter none \
-- \
app.main:app --host 0.0.0.0 --port 8000

final working

pm2 delete fast-api-python

pm2 start "venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000" --name fast-api-python

pm2 save

see the logs : pm2 logs fast-api-python

pm2 logs fast-api-python --lines 20
