from fastapi import FastAPI, APIRouter, HTTPException, Header
from typing import List, Dict, Any
from datetime import datetime
from . import PatientModel, blocks, ipfsService, blockchain, proccessBlocks
import uuid, json

router = APIRouter()
ipfs = ipfsService

@router.get('/search-exams')
def busca_todos_exames(docchain_anti_csrf: str):
    document = docchain_anti_csrf

    # Verifica se o documento é nulo
    if document is None:
        raise HTTPException(status_code=400, detail="Documento não enviado via Header")

    exames = blocks.get_chains_exams(document)

    return {'status': 'Success', 'data': exames}

@router.get('/show-exam')
def mostra_exame(id: str, docchain_anti_csrf: str = Header(None)):
    document = docchain_anti_csrf

    if document is None:
        raise HTTPException(status_code=400, detail="Documento não enviado via Header")

    if id is None:
        raise HTTPException(status_code=400, detail="Id não enviado")

    exame = blocks.get_unique_chain(document, id)

    return {'status': 'Success', 'data': exame}

@router.post('/search-exams-doctor')
def busca_exame_especifico(document: str):
    # Busca o documento nos blocos
    blocos = blocks.get_chains_exams(document)

    if not blocos:
        raise HTTPException(status_code=404, detail="Não há exames para esse paciente")

    return {'status': 'Success', 'data': blocos}


@router.post('/register-exam')
def cadastrar_exame(patient: PatientModel.PatientInput):
    patient.__setattr__('date_created', str(datetime.now()))
    patient.__setattr__('id', str(uuid.uuid4()))
    patientDict = vars(patient)
    
    try:
        # Cria um novo bloco
        NewBlock = blocks.new_block(patientDict)
        Hash = NewBlock.hash

        # Adiciona os dados do novo bloco ao IPFS
        chain = ipfs.addData(patientDict, Hash)

    except Exception as e:
        raise HTTPException(status_code=400,
                            detail=f"Erro ao criar novo bloco/salvar no IPFS. Detalhes: {str(e)}")

    return {'status': 'Success', 'data': patient}


@router.put('/update-exam')
def atualizar_exame(patient: PatientModel.PatientModify):
    patient.__setattr__('date_created', str(datetime.now()))
    patientDict = vars(patient)

    try:
        # Cria um novo bloco
        NewBlock = blocks.new_block(patientDict)
        Hash = NewBlock.hash

        # Adiciona os dados do novo bloco ao IPFS
        chain = ipfs.addData(patientDict, Hash)

    except Exception as e:
        raise HTTPException(status_code=400,
                            detail=f"Erro atualizar bloco/salvar no IPFS. Detalhes: {str(e)}")

    return {'status': 'Success', 'data': patient}

@router.delete('/delete-exam')
def deletar_exame():

    return {'status': 'Success', 'data': 'Welcome to the blockchain'}


