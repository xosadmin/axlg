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
  
Note: AXLG does not support other platforms like Windows.  
  