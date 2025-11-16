import xmltodict
from typing import Any, Dict

def parse_xml(xml_string: str) -> Dict[str, Any]:

    try:
        parsed = xmltodict.parse(xml_string)
        return parsed
    except Exception as e:
        raise ValueError(f'Failed to parse XML: {e}')