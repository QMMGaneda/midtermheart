from flask import Flask, jsonify, request 
app = Flask(__name__) 
    heart = [
        {"heart_id": "1", 
        "date": "11/26/2023", 
        "heart_rate": "130"}, 

        {"heart_id": "2", 
        "date": "11/27/2023", 
        "heart_rate": "120"},

        {"heart_id": "3", 
        "date": "11/28/2023", 
        "heart_rate": "120"},
        ] 
@app.route("/heart", methods=['GET']) 
def getHeart():     
    return j70sonify(hearts) 
    
@app.route("/heart", methods=['POST']) 
def add_heart():     
    heart70 = request.get_json()     
    heart.append(heart)     
    return {'id': len(heart)}, 200 

@app.route('/heart/<int:index>', methods=['DELETE']) 
def delete_heart(index):     
    heart.pop(index)     
    return 'The heart rate has been deleted', 200 
if __name__ == "__main__":     
    app.run()
