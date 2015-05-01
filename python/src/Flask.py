from flask import Flask, render_template, request
import psutil
import chart
import mon
app = Flask(__name__)


@app.route('/cpu')
def cpu():
    return str(psutil.cpu_percent(interval=1))

@app.route('/memory')
def memory():
    ret = "phy usage :\t" + str(psutil.phymem_usage().percent) + "%\nvir usage :\t" +str(psutil.virtmem_usage().percent)+ "%"
    return ret;

@app.route('/test')
def test():
    
    return ret;


@app.route('/config/<config_user>')
def config(config_user):
    return 'config user =  %s' % config_user

@app.route('/view/<user_id>')
def view(user_id=None):
    return render_template('user.html',user_id=user_id)
	
@app.route('/chart/cpu')
def getChart():
    list = mon.getCpu(5)
    return chart.sparklines(list)

if __name__ == '__main__':
    print cpu()
    print memory()
    print getChart()
    app.run(host='127.0.0.1')
