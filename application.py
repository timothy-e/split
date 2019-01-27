from flask import Flask, render_template, request

application = Flask(__name__)

#########################################
#                                       #
#  define models here (python classes)  #
#                                       #
#########################################

@application.route("/")
def main():
    return render_template('index.html', id=None)

@application.route("/add_purchase/", methods=["POST"]) # pass in params by cURL: name, cost, item
def add_purchase():
    name = request.args.get('name')
    cost = request.args.get('cost')
    item = request.args.get('item')
    # add a purchase to the Roommate with name=name
    pass


@application.route("/settle_debts/", methods=["POST"])
def settle_debts():
    # reset all balances to 0
    pass

@application.route("/get_balance/<name>", methods=["GET"])
def get_balance(name):
    # create a page with all debt info for Roommate with name=name
    # query for Roommate
    # pass into a render template
    return name

if __name__ == "__main__":
    application.run(debug=True)
