import fastapi as _fastapi
from . import blockchain as _blockchain   

app = _fastapi.FastAPI()
blockchain = _blockchain.Blockchain()

def new_block(data: str):
    block = _blockchain.Block(
        index=blockchain.chain[-1].index + 1,
        timestamp=_blockchain.date.datetime.now(),
        data=data,
        previous_hash=blockchain.chain[-1].hash
    )

    valid = _blockchain.is_chain_valid(block)
    return 0

@app.get('/chains')
def get_chains():
    return {'length': (blockchain.chain)}

@app.post('/mine-block')
def mine_block(data: str):
    new_block = _blockchain.Block(
        index=blockchain.chain[-1].index + 1,
        timestamp=_blockchain.date.datetime.now(),
        data=data,
        previous_hash=blockchain.chain[-1].hash
    )
    new_block.mine_block(blockchain.difficulty)
    if new_block != success:
        return {'message': 'Block not mined'}
    blockchain.chain.append(new_block)
    return {'message': new_block}