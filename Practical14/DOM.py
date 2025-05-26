import xml.dom.minidom
from datetime import datetime
from collections import defaultdict

# Initialize result storage
max_info_dom = defaultdict(lambda: {'term': '', 'count': 0})
start_time_dom = datetime.now()  # Start time recording

# Parse XML file
dom_tree = xml.dom.minidom.parse("D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical14\\go_obo.xml")  # Replace with actual file path
terms = dom_tree.getElementsByTagName('term')

for term in terms:
    # Extract namespace
    namespace_elem = term.getElementsByTagName('namespace')[0]
    namespace = namespace_elem.firstChild.data.strip()
    
    # Filter target ontologies
    if namespace not in ['molecular_function', 'biological_process', 'cellular_component']:
        continue
    
    # Extract term name
    name_elem = term.getElementsByTagName('name')[0]
    term_name = name_elem.firstChild.data.strip()
    
    # Count "is_a" elements
    is_a_count = len(term.getElementsByTagName('is_a'))
    
    # Update maximum count
    if is_a_count > max_info_dom[namespace]['count']:
        max_info_dom[namespace] = {'term': term_name, 'count': is_a_count}

# Calculate elapsed time
dom_elapsed = (datetime.now() - start_time_dom).total_seconds()

# Output DOM results
print("=== DOM Parser Results ===")
for ns in ['molecular_function', 'biological_process', 'cellular_component']:
    data = max_info_dom[ns]
    print(f"Ontology: {ns.capitalize()}")
    print(f"  Term with most 'is_a': {data['term']}")
    print(f"  Number of 'is_a': {data['count']}\n")
print(f"DOM parsing time: {dom_elapsed:.4f} seconds\n")