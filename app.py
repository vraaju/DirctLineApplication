from flask import Flask, jsonify

app = Flask(__name__)

def sum_of_list_of_numbers(nList):  # pass a number list to this function example sum_of_list_of_numbers([1,2,3])
    numberlist=list(nList)
    total=sum(numberlist) # used default sum method from list
    return total



@app.route("/total")
def total():
    nList=list(range(10000001))
    return jsonify(total=sum_of_list_of_numbers(nList))


if __name__ == "__main__":
    app.run()