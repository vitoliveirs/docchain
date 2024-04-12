# docchain
search-exams:
Endpoint da home, retorna todos os exames do PACIENTE, parâmetro enviado via HEADER:
nome parâmetro: docchain_anti_csrfm contendo o documento do paciente

show-exam:
Quando clicar em um exame em específico, vai retornar os dados específico do exame:
Necessário: parâmetro id, que está dentro de data.
docchain_anti_csrf via HEADER, contendo o documento do paciente.

search-exams-doctor:
Retorna os exames que um paciente tem, é apenas para MÉDICOS, retorna uma lista:
parâmetro necessário: documento do paciente

register-exam:
Registra o novo exame, body:
{
  "document": "string",
  "doctor_crm": "string",
  "exam_name": "string",
  "description": "string",
  "attachment": "string"
}

update-exam:
Faz update do exame, body:
{
  "document": "string",
  "exam_name": "string",
  "description": "string",
  "id": "string"
}