# json server
# default port 5000
#  pip install flask-rest-jsonapi flask-sqlalchemy


from flask import Flask
from flask import json
 

app = Flask(__name__)


json_data = '''[{"name":"Bob1", "year":2021},
{"name":"Bob2", "year":2021},
{"name":"Bob3", "year":2023} ]'''

# the following is not json
#json_data = """[{'name':'Bob1', 'year':2021}]"""

 


@app.route('/data/', methods=['GET'])
def example():
    response = app.response_class(
        response= json_data ,
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()