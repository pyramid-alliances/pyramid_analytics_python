import sys
import os
import re
import shutil

from bs4 import BeautifulSoup
import requests
import jinja2
from pprint import pprint
import keyword
from pathlib import Path
from time import sleep

res = requests.get("https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/objects.htm")
doc = BeautifulSoup(res.text, features="html.parser")
tbl = doc.find("table", {"class": "fxlist"})
classes = [x.get("href").replace("definitions/","").replace(".htm","") for x in tbl.find_all("a")]
# fix, why is this not in the index?
classes = [
    "ApiModifierResult",
    "ApiResultTaskStatus",
    "MemberDataApi",
    "EnumerationOutput",
    "CalcProps",
    "CmsTreeNodeMetadata",
    "ExternalServerData", 
    "OdbcDirectQueryOptions", 
    "TenantSettings", 
    "TenantInfo",
    "ConnectionStringProperties",
    "ConnectionStringData",
    "SearchCriteria",
    "RelatedItemData",
    "ApiModifierResultString",
    "ModelingServerInfo",
    "FormData",
    "RegistrationData",
    "UserWorkspaceSettings",
    "CmsLayoutSettings",
    "UserSettingsData",
    "AddUserRoleData",
    "ApiResultLicenseStatus",
] + classes + [
    "MasterFlowValidationResult",
    "MasterFlowSourceObject"
]
base_url = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/{classname}.htm"


res = requests.get("https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/enums.htm")
doc = BeautifulSoup(res.text, features="html.parser")
tbl = doc.find("table", {"class": "fxlist"})
enum_classes = [x.get("href").replace("definitions/","").replace(".htm","") for x in tbl.find_all("a")]



methods = dict(
    auth = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth.htm",
    access = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access.htm",
    content = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content.htm",
    query = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/query.htm",
    dataSources = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources.htm",
    tasks = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks.htm",
    notification = "https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/notification.htm"
)

general_imports = """
from typing import (
    Any,
    Dict,
    List,
    Optional
)
"""

tpl = '''
class {{ classname }}(BaseModel):
    """ 
    generated from {{ url }}
    """
    {% for attr in classattrs -%}
    {% if attr.Default -%}
    {{ attr.Name }}: {{ attr.PythonType }} = {{ attr.Default }} # Format:"{{ attr.Format}}" Descr:"{{ attr.Description}}"
    {% else -%}
    {{ attr.Name }}: {{ attr.PythonType }}  # Format:"{{ attr.Format}}" Descr:"{{ attr.Description}}"
    {% endif -%}
    {% endfor %}

'''

tpl_enum = '''
class {{ classname }}(IntEnum):#
    """ 
    generated from  {{ url }}
    """
    {% for attr in classattrs -%}
    {{ attr.Name }} = {{ attr.Value }}
    {% endfor %}

'''

tpl_method = '''
def {{ methodname }}({{ inputs }}) -> {{ response_type }}:
    """
    Description:
        {{description}}
    {% if in_attrs %}
    Input:
        {% for in_attr in in_attrs -%}
        {% for k,v in in_attr.items() -%}
        {{ k }}: {{ v }}
        {% endfor %}
        {% endfor %}
    {% endif %}
    Output:
        {% for k,v in out_attrs.items() -%}
        {{ k }}: {{ v }}
        {% endfor %}

    generated from {{ url }}
    """
    {% if is_complex_type -%}
    data = { "{{inputname}}" : {{inputname}} }
    {% else %}
    {% if in_attrs -%}
    data = { {%- for in_attr in in_attrs -%}
            "{{in_attr.Name}}" : {{in_attr.Name}},
            {%- endfor -%}
    }
    {% endif -%}
    {% endif -%}

    return call_api("{{method_url}}",
                data={% if in_attrs %}data{% else %}None{% endif -%}, 
                response_type={{ response_type }}
           )



'''

env = jinja2.Environment()


python_types = {
    "string" : "str",
    "integer" : "int",
    "boolean" : "bool",
    "object"  : "dict",
    "array"   : "List[str]"

}

def gen_enum(basedir="pyramid_api"):
    with open(f"{basedir}/enum.py", "w") as out:
        t = env.from_string(tpl_enum)
        out.write("from enum import IntEnum\n")
        out.write(general_imports)
        for classname in enum_classes:
            print(f"processing enum: {classname}")

            url = base_url.format(classname=classname)
            
            soup = None
            cachename = "cache/{}.htm".format(classname)
            if os.path.exists(cachename):
                with open(cachename, "r") as f:
                    soup = BeautifulSoup(f.read(), features="html.parser")
            else:
                attrs_html = requests.get(url)
                soup = BeautifulSoup(attrs_html.text, features="html.parser")
                with open(cachename, "w") as f:
                    f.write(attrs_html.text)

            api_tbl = soup.find("table", {"class" : "apiCode"})

            header = [x.text.strip() for x in api_tbl.select("tr th p")]
            attrs = []
            for row in api_tbl.select("tr")[1:]:
                attr = dict(zip(header,[a.text.strip() for a in row.select("td")]))
                #if attrs["Type"] == "string": attrs["Type"] = "str"
                attr_type = attr.get("Type", "unknown")
                name = attr["Enumerated Name"]
                if name in keyword.kwlist:
                    name = name + "_"
                name = attr["Name"] = name

                attrs.append(attr)
            if classname in ("QueryResultMessageExtraData", ):
                # skip problematic classes for now
                continue
            out.write(t.render(classname=classname, classattrs=attrs, url=url))

def reorder_definition(data, offsets):
    """
    offset the key name for dependent definitions
    """

    result = list(data)
    for key, before in offsets:
        index = result.index(key)
        if index >= 0:
            result.pop(index)
        before_index = result.index(before)
        result.insert(before_index-1, key)
    return result


def gen_object(basedir="pyramid_api"):
    with open(f"{basedir}/objects.py", "w") as out:
        out.write(general_imports)
        out.write("from pydantic import BaseModel\nfrom .enum import *\n\n")
        t = env.from_string(tpl)



        # reorder definitions
        reordered_classes =  reorder_definition(classes, [
            ("TaskViewData", "ExecutionViewData"),
            ("MasterFlowValidationResult", "ExecuteMasterFlowResult"),
            ("MasterFlowSourceObject", "MasterFlowValidationResult"),
            ("MasterFlowOtherObject", "MasterFlowValidationResult"),
            ("MasterFlowTargetObject", "MasterFlowValidationResult"),
            ("MasterFlowVariableObject", "MasterFlowValidationResult"),
            ("FilterParameter", "ExternalParameters"),
            ("TargetParameter", "ExternalParameters"),
            ("ModelingHierarchyLevel", "ModelingHierarchy"),
            ("ModelingProperty","ModelingHierarchyLevel"),
            ("ModelingRelationship","ModelingModel"),
            ("ModelDataFlowSourceInfo","ModelingModel"),
            ("ModelDataFlowSourceInfo","MeasureGroup"),
            ("ModelingTable","ModelingModel"),
            ("ModelingRelationshipColumnPair","ModelingRelationship"),
            ("ModelingMeasure","ModelingTable"),
            ("ProfilePermissionHolder","ProfileApiData")

        ])
        for classname in reordered_classes:
            print(f"processing object: {classname}")
            #if "ImportApiResultObject" in classname:
            #     import ipdb;ipdb.set_trace()
            url = base_url.format(classname=classname)
            
            soup = None
            cachename = "cache/{}.htm".format(classname)
            if os.path.exists(cachename):
                with open(cachename, "r") as f:
                    soup = BeautifulSoup(f.read(), features="html.parser")
            else:
                attrs_html = requests.get(url)
                soup = BeautifulSoup(attrs_html.text, features="html.parser")
                with open(cachename, "w") as f:
                    f.write(attrs_html.text)
            
            api_tbl = soup.find("table", {"class" : "apiCode"})

            header = [x.text.strip() for x in api_tbl.select("tr th p")]
            #print(header)
            attrs = []

            for row in api_tbl.select("tr")[1:]:
                attr = dict(zip(header,[a.text.strip() for a in row.select("td")]))
                #if attrs["Type"] == "string": attrs["Type"] = "str"
                attr_type = attr.get("Type", "unknown").strip()
                attr["Default"] = ""
                # special cases
                if attr_type == "[UUID]\n[UUID]":
                    attr_type = "Dict[str,str]"
                elif attr_type == '[string]\n[[ConnStringDscApiObject]]':
                    attr_type = "Optional[Dict[str,List[ConnStringDscApiObject]]]"
                else:
                    attr_format = attr.get("Format", "").strip()
                    attr_type_req = attr.get("Required", "").strip()
                    if attr_type_req and attr_type_req != "-" and attr_type_req != "Y":
                        # inconsistent html
                        attr_type = attr_type_req

                    if attr_type == "number":
                        if attr_format == "float":
                            attr_type = "float"
                        elif attr_format == "int32":
                            attr_type = "int"


                    

                    if m:= re.search("(\w+)\s*\[\s*\]", attr_type):
                        attr_type="List[{}]".format(m.group(1))

                python_type  = python_types.get(attr_type,attr_type)
                if attr.get("Required") != "Y":
                    python_type = "Optional[{}]".format(python_types.get(attr_type,attr_type))
                else:
                    attr["Default"] = ""
                
                # deal with self-references
                if 'RelatedItemData' in python_type:
                    python_type = python_type.replace("RelatedItemData", "'RelatedItemData'")
                elif 'ModelingProperty' in python_type:
                    python_type = python_type.replace("ModelingProperty", "'ModelingProperty'")


                attr["PythonType"] =  python_type

                descr = attr.get("Description","").lower()
                if re.search("default:false", descr):
                    attr["Default"] = "False"
                elif re.search("default:true", descr):
                    attr["Default"] = "True"

                attrs.append(attr)
            #if "ImportApiResultObject" in classname:
            #     import ipdb;ipdb.set_trace()
            #pprint(attrs)
            out.write(t.render(classname=classname, classattrs=attrs, url=url))
            


def gen_methods(basedir="pyramid_api"):

    t = env.from_string(tpl_method)

    for groupname, url in methods.items():
        res = requests.get(methods[groupname])
        doc = BeautifulSoup(res.text, features="html.parser")
        tbl = doc.find("table", {"class": "fxlist"})
        definitions = [x.get("href").replace("definitions/","").replace(".htm","") for x in tbl.find_all("a")]
        with open(f"{basedir}/{groupname}.py", "w") as out:
            out.write(general_imports)
            out.write("from .objects import *\nfrom .enum import *\n")
            out.write("from .api_interface import call_api\n")
            for methodname in definitions:
                print(f"processing method: {methodname}")
                #if "getAllNonPrivateRoles" in methodname:
                #    import ipdb;ipdb.set_trace()
                inputs = []
                in_nodes = []
                out_nodes = []
                in_attrs = []
                out_attrs = {}
                cachename = "cache/method/{}.htm".format(methodname)
                p = Path(cachename).parent
                if not p.exists():
                    p.mkdir()
                url = f"https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/{methodname}.htm"
                soup = None
                if os.path.exists(cachename):
                    with open(cachename, "r") as f:
                        soup = BeautifulSoup(f.read(), features="html.parser")
                else:
                    #print(url)
                    res = requests.get(url)
                    content = res.text
                    #print(res.status_code)
                    soup = BeautifulSoup(content, features="html.parser")
                    with open(cachename, "w") as f:
                        f.write(soup.prettify())

                method_url = soup.find("div", {"class": "apiCode"}).text.strip()
                description = soup.find("h1").text.strip()
                details = [x.text.strip() for x in soup.select("li")]
                spec = dict([(n.text.strip(), n) for n in soup.select("h5")])
                
                if "Input Parameters" in spec:
                    input_header = spec["Input Parameters"]
                    
                    node = input_header.find_next_sibling("div")
                    #import ipdb;ipdb.set_trace()
                    while 1:
                        if not node:
                            break
                        if node.name == "h5": break
                        if node.attrs.get("style") == "clear:left":
                            node = node.find_next_sibling()
                            continue
                        if "apihead" in node.attrs.get("class",{}) or "apidetail" in node.attrs.get("class",{}):
                            in_nodes.append(node.text.strip())
                        else:
                            break
                        node = node.find_next_sibling()
                    it = iter(in_nodes)
                    in_attr = dict(zip(it, it))
                    in_attrs.append(in_attr)

                if "Output Response" in spec:
                    header = spec["Output Response"]
                    
                    node = header.find_next_sibling("div")
                    #import ipdb;ipdb.set_trace()
                    while 1:
                        if not node:
                            break
                        if node.name == "h5": break
                        if node.attrs.get("style") == "clear:left":
                            node = node.find_next_sibling()
                            continue
                        if "apihead" in node.attrs.get("class",{}) or "apidetail" in node.attrs.get("class",{}):
                            out_nodes.append(node.text.strip())
                        else:
                            break
                        node = node.find_next_sibling()
                    it = iter(out_nodes)
                    out_attrs = dict(zip(it, it))

                response_type = out_attrs.get("Response Type")
                if not response_type:
                    response_type = out_attrs.get("Response List Type", "None")
                    out_descr = out_attrs.get("Description of Response Type","")
                    if m:= re.search("(\w+)\s*\[\s*\]", response_type):
                        response_type = "List[{}]".format(m.group(1))

                    if  "The response is the security token as a base64 string" in out_descr:
                        response_type = "str"


                inputtype = ""
                inputname = "data"
                is_complex_type = False

                if in_attrs:
                    inputs = []
                    for in_attr in in_attrs:
                        inputname = in_attr.get("Name","data")
                        api_type = in_attr.get("Type", "")
                        if not api_type:
                            if inputname == "itemIds":
                                api_type = "List[str]"
                        if api_type:
                            is_complex_type = False
                        else:
                            api_type =  in_attr.get("Object Type", "")
                            if api_type:
                                is_complex_type = True
                        if m:= re.search("(\w+)\s*\[\s*\]", api_type):
                            api_type = "List[{}]".format(m.group(1))
                        inputtype = "{}: {}".format(
                            in_attr.get("Name","data"),
                            python_types.get(api_type,api_type)
                            )
                        if "Default" in in_attr:
                            inputtype = "{}={}".format(inputtype, in_attr.get("Default"))
                        inputs.append(inputtype)

                out.write(t.render(
                        methodname=methodname.split("/")[-1], 
                        url=url, method_url=method_url,
                        description=description,
                        inputname=inputname,
                        inputs=", ".join(inputs),
                        in_attrs=in_attrs,
                        out_attrs=out_attrs,
                        response_type=response_type,
                        is_complex_type=is_complex_type
                        ))




def main():
    basedir = "pyramid_api"
    output_dir = Path(basedir)
    if not output_dir.exists():
        output_dir.mkdir()

    cache_dir = Path("cache")
    if not cache_dir.exists():
        cache_dir.mkdir()
        (cache_dir / Path("method")).mkdir()

    # base functionality
    shutil.copy2("api_base/__init__.py", f"{basedir}/__init__.py")
    shutil.copy2("api_base/api_interface.py", f"{basedir}/api_interface.py")

    gen_enum(basedir=basedir)
    gen_object(basedir=basedir)
    gen_methods(basedir=basedir)

if __name__ == '__main__':
    main()