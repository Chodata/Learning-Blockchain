# Module 1 - Create a Blcokchain
import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {"index": len(self.chain) + 1,
                 "timestamp" : str(datetime.datetime.now()),
                 "proof" : proof,
                 "previous_hash" : previous_hash,
                 }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = self.proofing(new_proof, previous_proof)
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof+=1
        
        return new_proof
    
    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def proofing(self,new_proof,previous_proof):
        return hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        
        for i in chain[1:]:
            if i['previous_hash'] != self.hash_block(previous_block):
                return False
            
            if self.proofing(i["proof"],previous_block["proof"])[:4] != '0000':
                return False
            previous_block = i
            
        return True
    
