from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import yaml

app = Flask(__name__)
CORS(app)
# Load database configuration from db.yaml
#db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

# Configure database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='blogdb'
)

@app.route('/blogs', methods=['GET'])
def get_blogs():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sample_data_authors")
    blogs = cursor.fetchall()
    cursor.close()
    if blogs:
        return jsonify(blogs)
    else:
        return jsonify({"message": "No blogs found"}), 404

@app.route('/blogs/<int:id>', methods=['GET'])
def get_blog(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM blogs WHERE id = %s", (id,))
    blog = cursor.fetchone()
    cursor.close()
    if blog:
        return jsonify(blog)
    else:
        return jsonify({"message": "Blog not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6500,debug=True)