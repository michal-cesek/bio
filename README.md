#### TODO
http://docs.python-guide.org/en/latest/writing/structure/


#### SETUP

https://github.com/pyenv/pyen
sudo apt install python3-venv

##### create .venvs in ~/ 
 
python3 -m venv bio

##### activate venv
source ~/.venvs/bio/bin/activate

##### install and freeze package
###### opencv-contrib-python contains opencv python bindings and also ear cascades
pip install opencv-contrib-python && pip freeze > requirements.txt

#### SETUP
./run.sh








