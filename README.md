create a environment : python3 -m venv venv
activate env : source venv/bin/activate

install dependency : pip install fastapi uvicorn
make dep file : pip freeze > requirements.txt

pip3 install requests or pip install requests

run file wiht uvicorn : uvicorn main:app --reload

git commit --allow-empty -m "trigger jenkins build"
git push origin main

For PROD : export ENV=production

For DEV : export ENV=development

uvicorn main:app --reload

on server
pm2 restart fastapi-api --update-env
