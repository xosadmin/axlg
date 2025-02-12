# axlg
AX Looking Glass Server - A simple looking glass server  
  
### How to deploy
- By using Docker Container: Use following command to deploy AXLG:
``docker run -d --name axlg -p 5000:5000 xosadmin/axlg``  
- By deploy manually:  
1. Clone this project  
2. Use ``pip install -r requirements.txt`` to install all dependencies  
3. Update ``conf.py`` with your hostname, location and iperf3, etc.  
4. Use Flask Engine or any WSGI engine (e.g. uWSGI and Gunicorn) to run this project  
  
#### Notes:   
- AXLG does not support other platforms like Windows.
- You can pass your own ``conf.py`` to ``/opt/axlg/conf.py`` to adopt custom config.  
- The docker image does not include iperf3. You may need to host your own before deploy AXLG.  
  
