#-----------------------
# 匯入Flask類別
#-----------------------
from flask import Flask,render_template

#-----------------------
# 產生一個Flask物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 用裝飾器定義app的路由
#-----------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer/test')
def customer_test():
    ''' #註解 方法1
    data = {} #空的字典data
    data['name'] = '王大明' #包在data裡面.變數名稱
    data['name'] = '王小明' #包在data裡面.變數名稱
    data['gender'] = '男'
    '''
    data={'name':'王小明', 'gender':'男', 'age':20} #別種方法
    
    return render_template('test.html', data=data) #連過去名稱=變數名稱,dt=ata=data(都包在data裡面)

@app.route('/customer/list')
def customer_list():
    data=[{'name':'王小明天', 'gender':'男', 'age':20},
          {'name':'王小明日', 'gender':'男', 'age':21},
          {'name':'王小明星', 'gender':'女', 'age':22},
          {'name':'王小明確', 'gender':'男', 'age':23},
          {'name':'王小明年', 'gender':'男', 'age':24}] #別種方法
    
    return render_template('list.html', data=data) #連過去名稱=變數名稱,dt=ata=data(都包在data裡面)

#-----------------------
# 執行app
#-----------------------
if __name__ == '__main__':
    app.run(port=5000, debug=True)