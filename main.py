from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def slash():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return 'Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>Человечеству мала одна планета.<br>Присоединяйся!'


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/mars.jpeg')}">'''


@app.route('/image_mars')
def image_mars():
    return '''<h1>Жди нас, Марс!</h1><br><img src="/static/img/mars.jpeg" height="600" width="1000">
            <br>Вот она какая, красная планета.<br>
            <title>Привет, Марс!</title>'''


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" height="400" width="700">
                    <p class="bg-danger text-dark" style="max-width: 35rem;">Человечество вырастает из детства.</p>
                    <p class="bg-info text-dark" style="max-width: 35rem;">Человечеству мала одна планета.</p>
                    <p class="bg-success text-dark" style="max-width: 35rem;">Мы сделаем обитаемыми безжизненные пока планеты</p>
                    <p class="bg-warning text-dark" style="max-width: 35rem;">И начнем с Марса!</p>
                    <p class="bg-secondary text-dark" style="max-width: 35rem;">Присоединяйся!</p>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h2 align="center">Анкета претендента</h2>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                 <div class="form-group mb-4">
                                    <input type="surn" class="form-control" id="surn" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surn">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                </div>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group mb-4">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>

                                     <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="job" id="enj" value="enj">
                                          <label class="form-check-label" for="enj">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="job" id="enjst" value="enjst">
                                          <label class="form-check-label" for="enjst">
                                           Инженер-строитель
                                          </label>
                                        </div>

                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="job" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                           Пилот
                                          </label>
                                        </div>

                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="job" id="mete" value="mete">
                                          <label class="form-check-label" for="mete">
                                           Метеоролог
                                          </label>
                                        </div>

                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="job" id="enjlife" value="enjlife">
                                          <label class="form-check-label" for="enjlife">
                                           Инженер по жизнеобеспечению
                                          </label>
                                        </div>

                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="job" id="doc" value="doc">
                                          <label class="form-check-label" for="doc">
                                           Врач
                                          </label>
                                        </div>

                                    

                                        <div class="form-check mb-4">
                                            <input class="form-check-input" type="checkbox"  name="job" id="ekz" value="ekz">
                                            <label class="form-check-label" for="ekz">
                                            Экзобиолог
                                            </label>
                                        </div>
                                        
                                        <div class="form-group mb-4">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        

                                    <div class="form-group mb-2">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group mb-2">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group form-check mb-2">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surn'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['job'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        print(request.form)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
