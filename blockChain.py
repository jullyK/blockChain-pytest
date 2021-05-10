import hashlib

from block import Block

class BlockChain:

  def __init__(self, seed):
    self.chain = []
    self.current_data = []
    self.nodes = set()
    self.construct_genesis(seed)


  @property
  def latest_block(self):
    return self.chain[-1]


  def construct_genesis(self, seed):
    self.construct_block(proof_no=seed, prev_hash=seed)


  def construct_block(self, proof_no, prev_hash):
    block = Block(
      index = len(self.chain),
      proof_no=proof_no,
      prev_hash=prev_hash,
      data=self.current_data)
    self.current_data = []

    self.chain.append(block)
    return block


  @staticmethod
  def check_validity(block, prev_block):
    if prev_block.index + 1 != block.index:
      return False

    if prev_block.calculate_hash != block.prev_hash:
      return False
    
    if not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
      return False
    
    if block.timestamp <= prev_block.timestamp:
      return False
    
    return True

  def new_data(self, sender, recipient, quantity):
    self.current_data.append({
      'sender': sender,
      'recipient': recipient,
      'quantity': quantity
    })
    return True


  @staticmethod
  def proof_of_work(last_proof):
    proof_no = 0
    while BlockChain.verifying_proof(proof_no, last_proof) is False:
      proof_no += 1
    
    return proof_no


  @staticmethod
  def verifying_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "1337"
