echo "Executing Api...";
pip3 install virtualenv
virtualenv vqx;
source vqx/bin/activate;
pip3 install -r requirements.txt;
./api/run.py;