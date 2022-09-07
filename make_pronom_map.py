import sys
import requests
import xmltodict
import json


def make_dict():
    default = "https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V108.xml"
    url = sys.argv[1] if sys.argv[1:] else default
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    formats = data["FFSignatureFile"]["FileFormatCollection"]["FileFormat"]
    format_map = {}
    for f in formats:
        format_map[f["@PUID"]] = f.get("@MIMEType", None)
    print(json.dumps(format_map, indent=4))


if __name__ == '__main__':
    make_dict()
