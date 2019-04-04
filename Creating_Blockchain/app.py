# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 00:00:34 2019

@author: TATA
"""

from blockchain import Blockchain

from flask import Flask, jsonify

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash_block(previous_block)
    block = blockchain.create_block(proof,previous_hash)
    
    response = {'message':"Congratulations, you just mined a block!",
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof': block['proof'],
                'previous_hash':block['previous_hash']}
    return jsonify(response), 200


@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'lenght' : len(blockchain.chain)}
    return jsonify(response),200

@app.route('/is_valid', methods = ['GET'])
def is_valid():
    response = {"validity" : blockchain.is_chain_valid(blockchain.chain)}
    return jsonify(response),200

    


app.run(host = "0.0.0.0", port = 5000)

