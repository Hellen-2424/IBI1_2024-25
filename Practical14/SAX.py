import xml.sax
from datetime import datetime
from collections import defaultdict

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.reset_state()
        self.max_info = defaultdict(lambda: {'term_name': '', 'is_a_count': 0})
    
    def reset_state(self):
        self.current_term = {
            'namespace': '',
            'name': '',
            'is_a': 0
        }
        self.in_name = False
        self.in_namespace = True  # Initial state assumption (adjust based on XML)
        self.temp_data = ""
    
    def startElement(self, tag, attrs):
        if tag == 'term':
            self.reset_state()
        elif tag == 'name':
            self.in_name = True
            self.temp_data = ""
        elif tag == 'namespace':
            self.in_namespace = True
            self.temp_data = ""
        elif tag == 'is_a':  # Count all <is_a> tags regardless of nesting
            self.current_term['is_a'] += 1
    
    def characters(self, content):
        if self.in_name or self.in_namespace:
            self.temp_data += content.strip()
    
    def endElement(self, tag):
        if tag == 'name':
            self.current_term['name'] = self.temp_data
            self.in_name = False
        elif tag == 'namespace':
            self.current_term['namespace'] = self.temp_data
            self.in_namespace = False
        elif tag == 'term':
            ns = self.current_term['namespace']
            target_ontologies = ['molecular_function', 'biological_process', 'cellular_component']
            if ns in target_ontologies:
                if self.current_term['is_a'] > self.max_info[ns]['is_a_count']:
                    self.max_info[ns] = {
                        'term_name': self.current_term['name'],
                        'is_a_count': self.current_term['is_a']
                    }

start_time = datetime.now()
handler = GOHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical14\\go_obo.xml")  # Replace with actual file path
sax_elapsed = (datetime.now() - start_time).total_seconds()

print("=== SAX Parser Results ===")
for ns in ['molecular_function', 'biological_process', 'cellular_component']:
    data = handler.max_info[ns]
    print(f"Ontology: {ns.capitalize()}")
    print(f"  Term with most is_a: {data['term_name']}")
    print(f"  is_a count: {data['is_a_count']}\n")
print(f"SAX parsing time: {sax_elapsed:.4f} seconds\n")