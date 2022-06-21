
from flask import Flask
app = Flask(__name__)  # 用來定位目前載入資料夾的位置，判別template_folder或static_folder資料夾位置


@app.route("/")  # decorator是用來讓Flask監聽此URL，並返回結果
def home_view():
    return "<h1>Welcome Dashboard</h1>"
