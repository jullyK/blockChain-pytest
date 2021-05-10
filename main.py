from blockChain import BlockChain

if __name__ == '__main__':
  blockchain = BlockChain(1337)

  print("----Testing BlockChain----")
  print(blockchain.chain)
  last_block = blockchain.latest_block
  last_proof_no = last_block.proof_no
  proof_no = blockchain.proof_of_work(last_proof_no)

  blockchain.new_data(
    sender="blockchain",
    recipient="Juma lober",
    quantity=1
  )

  block = blockchain.construct_block(proof_no, last_block.calculate_hash)

  print("----Success Block----")
  print(blockchain.chain)