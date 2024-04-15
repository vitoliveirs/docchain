import unittest
from datetime import datetime
import uuid
from fastapi import FastAPI, APIRouter, HTTPException, Header
from typing import List, Dict, Any
from PatientModel import PatientInput, PatientModify 
import ipfsService
import blockchain
import json
import blocks
import exams

class ExamsTestCase(unittest.TestCase):
    def test_cadastrar_exame(self):
        # Create a test case
        test_patient = PatientInput(
            document='07956700915',
            doctor_crm='256498',
            exam_name='Hemograma',
            description='Exame de sangue',
            attachment='UBAWAUSBWYKUvuyDCURTaurutVAIAyvbatibAIbyaiAUBAuiyVAtvIOUABUAybaOYubAYOUboUBYAoaNBYUODVTRscaYREAcyaRCaruyaUVayoNpMpomIOPmpiBYbYKUVBKUYVBUTykbkuybtyvrtdyreTCtVYbOULnNJnLBl=' #PDF criptografado em base64
        )

        # Call the function to be tested
        result = exams.cadastrar_exame(test_patient)

        # Assert the expected output
        expected_keys = ['status', 'data']
        self.assertEqual(set(result.keys()), set(expected_keys))
        self.assertEqual(result['status'], 'Success')
        self.assertEqual(result['data'], test_patient)

#Inserir testes a partir daqui


# Manter intacto
if __name__ == '__main__':
    unittest.main()