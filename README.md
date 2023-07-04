# Project Description: INA-JIFFY URL Shortener

This is a capstone project for ALTSCHOOL

Brief is the new black, this is what inspires the team at Ina-Jiffy. In todays world, its important to keep things as short as possible, and this applies to more concepts than you may realize. From music,speeches, to wedding receptions, brief is the new black. Ina-Jiffy is a simple tool which makes URLs as short as possible.Ina-Jiffy thinks it can disrupt the URL shortening industry and give the likes of bit.ly and ow.ly a run for their money within 2 years.

## Built with:
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Get a copy
It is believed that you have python installed already. Open CMD or terminal
1. Clone this repo
```sh
git clone https://github.com/Unique-Red/url_shortner.git
```
2. Open the directory
```sh
cd url_shortner
```
3. Create Virtual Environment
```sh
python -m venv <your-venv-name>
```
4. Activate virtual environment on CMD or Powershell
```sh
<your-venv-name>\Scripts\activate.bat
```
On gitbash terminal
```sh
source <your-venv-name>/Scripts/activate.csh
```
5. Install project packages
```sh
pip install -r requirements.txt
```
6. Set environment variable
```sh
set FLASK_APP=app.py
```
On gitbash terminal
```sh
export FLASK_APP=run.py
```
7. Create database
```sh
flask shell
```
```sh
db.create_all()
quit()
```
8. Run program
```sh
python app.py
```
<hr>


<br/>
Live link: <a href="https://ina-jiffy-app.onrender.com/">Ina-Jiffy</a>
