from dataclasses import dataclass

@dataclass
class PatientInput:
    document: str
    doctor_crm: str
    exam_name: str
    description: str 
    attachment: str


@dataclass
class PatientModify:
    document: str
    exam_name: str
    description: str
    id: str