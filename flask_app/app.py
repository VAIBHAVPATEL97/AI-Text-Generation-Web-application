from flask import Flask,render_template,request,jsonify
from transformers import pipeline

server = Flask(__name__)

@server.route('/')
def form():
    return render_template('form.html')
 
@server.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        text_generate = pipeline("text-generation")
        data = request.get_json()
        print("------------------------",data)
        #print(request.form)
        #generated_txt = text_generate(request.form["Ideas"], max_length = 50, do_sample=False)[0]
        generated_txt = text_generate(data, max_length = 50, do_sample=False)[0]
        print('--------------------', generated_txt['generated_text'])
        #form_data = {"output":generated_txt["generated_txt"]}
        #print(type(generated_txt['generated_txt'])
        #return render_template('data.html', form_data = generated_txt['generated_text'])  
        return jsonify(generated_txt)
    return "This input is not working"
