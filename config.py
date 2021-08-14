from flask import Flask, jsonify
from flask.globals import request
#from flask_sqlalchemy import SQLAlchemy
from cardsnumbers import cards
from validation import checkLuhn
import json


""" Configuration file """


app = Flask(__name__)


#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root@localhost/validation_card'

#db = SQLAlchemy(app)

# Route for check the status of API
@app.route('/', strict_slashes=False, methods=['GET'])
def checking_url():
    """ Return status of API """
    return ("ok")


# Route for get all the cards available
@app.route('/cards', strict_slashes=False, methods=['GET'])
def getCards():
    return jsonify({'cards': cards})


# Route for insert a new credit card and validation proccess
@app.route('/cards', strict_slashes=False, methods=['POST'])
def addCard():
    new_card = {
        'cardNumber': request.json['cardNumber']
    }

    retrieves = new_card.get('cardNumber')

    if checkLuhn(retrieves):

        if retrieves[0] == '5':
            return ("MasterCard")

        if retrieves[0] == '4':
            return ("Visa")

        elif retrieves[0] == '3':
            return ("Diners Club")


        cards.append(new_card)

        return jsonify({'cards': cards})

    else:
        return ("Invalid credit card, try again.")


# Route for validate the credit card
@app.route('/validator/<string:cardNumber>', strict_slashes=False, methods=['GET'])
def validateCard(cardNumber):
    if checkLuhn(cardNumber):
        if cardNumber[0] == '5':
            return("MasterCard")

        if cardNumber[0] == '4':
            return("Visa")

        elif cardNumber[0] == '3':
            return("Diners Club")
    else:
        return ("Invalid credit card, try again.")


# Route for delete a credit card
@app.route('/cards/<string:card_id>', strict_slashes=False, methods=['DELETE'])
def delete_card(card_id):
    cardFound = [card for card in cards if card['id'] == card_id]
    if len(cardFound) > 0:
        cards.remove(cardFound[0])
        return jsonify({'message': 'Card deleted',
                        'cards': cards
        })


if __name__ == "__main__":
    app.run(debug=True)
