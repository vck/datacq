from flask import Flask
from flask import render_template
from flask import Response
from flask import request
import lib.search as search
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def IndexPage():
    #cron_status = subprocess.check_output(['service','cron','status']).strip('\n')
    #f = open('/var/log/datacq/error.log')
    #error = f.read().strip('\n')
    #"""index page containes several basic information like system uptime etc"""
    return render_template('data.html')

@app.route('/files', methods=["GET", "POST"])
def ExploreFiles():
    """explore generated CSV files"""
    filelist = search.locate_with_folder('/home/pi/datacq/static', '.csv')
    info = [len(file) for file in filelist[1]]
    if request.method == "POST":
        if request.form['hapus']:
            os.system('rm static/%s'%request.form['hapus'])
            return render_template('readfile.html', filelist=filelist, info=info)
    return render_template('readfile.html', filelist=filelist, info=info)

@app.route('/downloads')
def DownloadFiles():
    zip_files = search.locate_with_folder('static','.zip')
    return render_template('download.html', filelist=zip_files)

@app.route('/test')
def TestPage():
    return render_template('data.html')

@app.route('/search', methods=['GET', 'POST'])
def SearchFiles():
    """laman pencarian berkas berdasarkan kriteria masukan pengguna"""
    if request.method == 'POST':
        query = request.form['search']
        if query:
            return render_template('search.html', filelist=search.locate_with_folder('/home/pi/datacq/static/', request.form['search'])) 
    return render_template('search.html')

@app.route('/reset', methods=['POST', 'GET'])
def ResetFile():
    """simillar to rm -rf but not that fast"""
    file = search.locate_with_folder('/home/pi/datacq/static', '.csv')
    file_info = len(file)
    if request.method == 'POST':
        cmd = request.form['hapus']
        if cmd:
            for csv in file:
                filename = csv[0]+'/'+csv[1]
                search.delete_file(filename)
                return render_template('reset.html', file_info=file_info)
    return render_template('reset.html', file_info=file_info)

@app.route('/status')
def SystemStatus():
    """summarize system status on this page"""
    zip_file = "{0:.0f}%".format(len(search.locate_with_folder('./static', '.zip'))/100 * 100)   
    csv_file = "{0:.0f}%".format(len(search.locate_with_folder('./static', '.csv'))/100 * 100)
    return render_template('status.html', zip_file=zip_file, csv_file=csv_file)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
