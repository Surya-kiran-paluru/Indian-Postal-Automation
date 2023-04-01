import spacy

# nlp=spacy.load("D:\Surya\College\Major Project\Address Parser\models\models\model-best")

# address_list=["p 21 dgqa compex chennal"]

# for address in address_list:
#     doc=nlp(address)
#     ent_list=[(ent.text, ent.label_) for ent in doc.ents]
#     print("Address string -> "+address)
#     print("Parsed address -> "+str(ent_list))
#     print("******")


def parse_address(address):

    nlp=spacy.load("D:\Surya\College\Major Project\Address Parser\models\models\model-best")
    doc=nlp(address)
    ent_list=[(ent.text, ent.label_) for ent in doc.ents]
    for i in range(len(ent_list)):
        ent_list[i]+=('is',)
    return ent_list