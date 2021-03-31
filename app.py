from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/services')
def service_page():
    return render_template('services.html')

@app.route('/barbers')
def barbers_page():
    return render_template('barbers.html')

@app.route('/appointment')
def appointment_page():
    return render_template('appointment.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
