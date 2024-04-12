import json

def process_multiple_exams(blocos):
    
    unique_exams = set()

    for bloco in blocos:
        # Check if bloco is a dictionary before accessing data
        if isinstance(bloco, dict):
            block_data = bloco.get('data')
            if block_data:
                block_id = block_data.get('id')
                timestamp = block_data.get('timestamp')

                if block_id and timestamp:
                    composite_key = (block_id, timestamp)

                    # Check if the exam is already in the set
                    if composite_key not in unique_exams:
                        # Add the exam to the set if not already present
                        unique_exams.add(composite_key)

    return list(unique_exams)