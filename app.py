from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def indexCh():
    return render_template("index-ch.html")

@app.route('/index-ch')
def home():
    return indexCh()

@app.route('/index-en')
def home_en():
    return render_template("index-en.html")

@app.route('/movie-ch')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie-ch.html", movies = datalist)

@app.route('/Douban_Flask/movie-en.html')
def movie_en():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie-en.html", movies = datalist)

@app.route('/score-ch')
def score():
    scoreList = []
    numberList = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score, count (score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scoreList.append(item[0])
        numberList.append(item[1])
    cur.close()
    con.close()
    return render_template("score-ch.html", scoreList = scoreList, numberList = numberList)

@app.route('/score-en')
def score_en():
    scoreList = []
    numberList = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score, count (score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scoreList.append(item[0])
        numberList.append(item[1])
    cur.close()
    con.close()
    return render_template("score-en.html", scoreList = scoreList, numberList = numberList)

@app.route('/word-ch')
def word():
    return render_template("word-ch.html")

@app.route('/word-en')
def word_en():
    return render_template("word-en.html")


if __name__ == '__main__':
    app.run()
