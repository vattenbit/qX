echo "Executing Api...";
virtualenv vqx;
source vqx/bin/activate;
pip install -r requirements.txt;
./api/run.py;