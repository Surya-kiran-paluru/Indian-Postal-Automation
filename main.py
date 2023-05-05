import OCR_model as ocr
import Address_parser as ap
import Knowledge_graph as kg
from spell_check import SpellCheck 
import Location as loc_api


model = ocr.load_model()
#visualkeras.layered_view(model).show() # display using your system viewer

output_ocr = ocr.get_text(model)
output_ocr = " ".join(output_ocr)

# print(output_ocr)


spell_check =  SpellCheck("data\citiesname.txt")

spell_check.check(output_ocr)

output_ocr = spell_check.correct()

output_ocr = output_ocr.capitalize()

print(output_ocr)

output_ap = ap.parse_address(output_ocr)

#print(output_ap)x

Knowledgde_Graph = kg.build_Kgraph(output_ap)

#kg.show_KG(Knowledgde_Graph)

city = kg.get_city(Knowledgde_Graph)[0]

print(loc_api.get_coordinates(city))

