import OCR_model as ocr
import Address_parser as ap
import Knowledge_graph as kg

model = ocr.load_model()
output_ocr = ocr.get_text(model)
output_ocr = " ".join(output_ocr)

output_ap = ap.parse_address(output_ocr)

kg.build_Kgraph(output_ap)

