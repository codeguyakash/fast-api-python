create a environment : python3 -m venv venv
activate env : source venv/bin/activate

install dependency : pip install fastapi uvicorn
make dep file : pip freeze > requirements.txt

run file wiht uvicorn : uvicorn main:app --reload
