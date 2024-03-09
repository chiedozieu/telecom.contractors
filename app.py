from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'LAN Installation',
    'location': 'Nigeria',
    'cost': 'NGN 1,500,000' 
  },
  {
    'id': 2,
    'title': 'Fiber Installion',
    'location': 'Nigeria',
    'cost': 'NGN 70,000'
  },
    
  
  {
    'id': 3,
    'title': 'Radio Installation',
    'location': 'Nigeria',
    'cost': 'NGN 500,000'
  
  },
  {
   'id': 4,
   'title': 'PABX Installation',
   'location': 'Nigeria',
   'cost': 'NGN 850,000'

  }
]
 
@app.route('/')
def hello_telecom():
  return render_template('home.html', jobs = JOBS)
    



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)

