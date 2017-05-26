from lxml import etree
from lxml.builder import E
import traceback
import yaml
import sys

def traverse(dic, path=None):
    if not path:
        path=[]
    if isinstance(dic,dict):
        for x in dic.keys():
            local_path = path[:]
            local_path.append(x)
            for b in traverse(dic[x], local_path):
                 yield b
    else:
        yield path,dic

def patch_from_patchdef(differences):
    operations = []
    for difference in traverse(differences):
        path = difference[0]
        value = difference[1]
        print(difference)
        xpath = '/ThingDefs/ThingDef[defName="'+path[0]+'"]'
        if(path[-2] == 'shoot'):
            xpath += '/verbs/li[verbClass="Verb_Shoot"]/' + path[-1]
        else:
            xpath += '/' + '/'.join(path[1:])
        node_name = path[-1]
        update_op = E('Operation', E('xpath', xpath), E('value', E(node_name, str(value))
        ), Class="PatchOperationReplace")
        operations.append(update_op)

    root = etree.Element('Patch')
    for operation in operations:
        root.append(operation)
    doc = etree.ElementTree(root)
    with open(sys.argv[2], 'wb') as of:
        of.write(etree.tostring(doc, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

def main():
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            patchdef = yaml.safe_load(f.read())
            print(patchdef)
            patch_from_patchdef(patchdef)
    except Exception as e:
        traceback.print_exc()
    finally:
        input('Waiting to close window')

if __name__ == '__main__':
    main()
