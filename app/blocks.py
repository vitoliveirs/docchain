from fastapi import FastAPI, APIRouter, HTTPException
import blockchain as _blockchain

router = APIRouter()
blockchain = _blockchain.Blockchain()

@router.get('/chains')
def get_chains(document: str):
    matching_blocks = []
    for block in blockchain.chain:
        if isinstance(block.data, dict) and 'document' in block.data and block.data['document'] == document:
            matching_blocks.append(block)
    if matching_blocks:
        return {'blocks': matching_blocks}
    else:
        raise HTTPException(status_code=404, detail="Documento não encontrado (Document not found)")
        

    if matching_blocks:
        return {'blocks': matching_blocks}
    else:
        raise HTTPException(status_code=404, detail="Documento não encontrado (Document not found)")

@router.get('/exams-chain')
def get_chains_exams(document: str):
    matching_blocks = []
    id_set = set()
    id_latest_block = {}

    for block in blockchain.chain:
        if isinstance(block.data, dict) and 'document' in block.data and block.data['document'] == document:
            block_id = block.data['id']
            if block_id not in id_set:
                id_set.add(block_id)
                id_latest_block[block_id] = block
            else:
                # Se já encontrou o id, substitui o bloco antigo pelo mais recente
                id_latest_block[block_id] = block
    
    for block_id, block in id_latest_block.items():
        matching_blocks.append(block)

    if matching_blocks:
        return {'blocks': matching_blocks}
    else:
        raise HTTPException(status_code=404, detail="Documento não encontrado (Document not found)")

@router.get('/unique-chain')
def get_unique_chain(document: str, id: str):
    matching_blocks = []
    for block in blockchain.chain:
        if isinstance(block.data, dict) and 'document' in block.data and block.data['document'] == document:
            if 'id' in block.data and block.data['id'] == id:
                matching_blocks.append(block)
    
    if matching_blocks:
        return {'blocks': matching_blocks}
    else:
        raise HTTPException(status_code=404, detail="Documento não encontrado (Document not found)")

@router.get('/all-chains')
def get_all_chains():
    return {'blocks': blockchain.chain}

@router.post('/mine-block')
def new_block(data: dict):
    
    new_block = _blockchain.Block(
        index=blockchain.chain[-1].index + 1,
        timestamp=_blockchain.date.datetime.now(),
        data=data,
        previous_hash=blockchain.chain[-1].hash
    )
    
    #Minera o bloco com a dificuldade 2
    new_block.mine_block(2)

    # Adiciona o novo bloco à blockchain
    blockchain.add_block(new_block)

    return new_block