text = "A patient with chest pain had hyperthyroidism."
entity_1 = "chest pain"
entity_2 = "hyperthyroidism"

# Store annotated data information in the correct format
annotated_data = {"sentence": text, "entities": [{"label": "SYMPTOM", "value": entity_1}, {"label": "DISEASE", "value": entity_2}]}

# Extract start and end characters of each entity
entity_1_start_char = text.find(entity_1)
entity_1_end_char = entity_1_start_char + len(entity_1)
entity_2_start_char = text.find(entity_2)
entity_2_end_char = entity_2_start_char + len(entity_2)

# Store the same input information in the proper format for training
training_data = [(text, {"entities": [(entity_1_start_char,entity_1_end_char,"SYMPTOM"), 
                                      (entity_2_start_char,entity_2_end_char,"DISEASE")]})]
print(training_data)

print("After collecting data, you can annotate data in the required format for a spaCy model. In this instance, you successfully completed an annotated data and formatted training data correctly for a NER task.")