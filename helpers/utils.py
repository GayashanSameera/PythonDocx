from pptx import Presentation
from pptx.util import Inches
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.oxml.xmlchemy import OxmlElement
import math
import re
import pydash

def check_tag_exist(tag, paragraph):
    matches = tag in paragraph.text
    return matches

def replace_tags(replaced_for,replaced_text, paragraph):
    if replaced_for in paragraph.text:
        paragraph.text = paragraph.text.replace(replaced_for, replaced_text)
        # inline = paragraph.runs
        # for item in range(len(inline)):
        #     print("item",inline[item])
        #     print("item",replaced_for in inline[item].text)
        #     if replaced_for in inline[item].text:
        #         inline[item].text = inline[item].text.replace(replaced_for, replaced_text)

def get_tag_content(pattern,paragraph):
    matches = re.findall(pattern, paragraph.text)
    return matches

def get_tag_from_string(pattern,string):
    matches = re.findall(pattern, string)
    return matches

def eval_executor(logic, replacements):
    return eval(logic,replacements)

def find(datam, key , value):
    for data in datam:
        if(data and data[key] and data[key] == value ):
            return data
            break

    return False

def get_value_array_using_array_and_key(datam, key):
    arr = []
    for data in datam:
        try:
            if(data and data[key]) :
                arr.append(data[key])
        except:
            print("An exception occurred")
        
    return arr

def get_value_array_of_keys_using_object(datam):
    arr = []
    for key,value in datam.items():
        arr.append(key)
    return arr


