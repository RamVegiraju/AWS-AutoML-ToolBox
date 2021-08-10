import boto3

#Using boto3 to call the Comprehend API
comprehendClient = boto3.client('comprehend', region_name = "us-east-1")

#lol ik its a dumb sentence
sampleText = "I am very happy in New York City, super excited to be working in the East, I can see the Statue of Liberty."

#Entity Extraction
entities = comprehendClient.detect_entities(Text = sampleText, LanguageCode = 'en') #API call for entity extraction
entities = entities['Entities'] #all entities
print(entities)
textEntities = [dict_item['Text'] for dict_item in entities] #the text that has been identified as entities
typeEntities = [dict_item['Type'] for dict_item in entities] #the type of entity the text is
print(textEntities)
print(typeEntities)