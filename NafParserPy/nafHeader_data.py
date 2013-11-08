from lxml import etree
import time

class CfileDesc:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('fileDesc')
        else:
            self.node = node
    
    #self.title=''    #self.author=''    #self.creationtime=''    #self.filename=''    #self.filetype=''    #self.pages=''
    
 
class Cpublic:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('public')
        else:
            self.node = node
            
        #self.publicId = ''
        #slf.uri = ''

   
class Clp:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('lp')
        else:
            self.node = node
            
    def set_name(self,name):
        self.node.set('name',name)
        
    def set_version(self,version):
        self.node.set('version',version)
        
    def set_timestamp(self,timestamp=None):
        if timestamp is None:
            import time
            timestamp = time.strftime('%Y-%m-%dT%H:%M:%S%Z')
        self.node.set('timestamp',timestamp)
        
    def get_node(self):
        return self.node
        
    
class ClinguisticProcessors:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('linguisticProcessors')
        else:
            self.node = node
            
    def get_layer(self):
        return self.node.get('layer')
    
    def set_layer(self,layer):
        self.node.set('layer',layer)
    
    def add_linguistic_processor(self,my_lp):
        self.node.append(my_lp.get_node())
        
    def get_node(self):
        return self.node

    
class CnafHeader:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('nafHeader')
        else:
            self.node = node
      
    def add_linguistic_processors(self,linpro):
        self.node.append(linpro.get_node())
        
    def add_linguistic_processor(self, layer ,my_lp):
        ## Locate the linguisticProcessor element for taht layer
        found_lp_obj = None
        for this_lp in self.node.findall('linguisticProcessors'):
            lp_obj = ClinguisticProcessors(this_lp)
            if lp_obj.get_layer() == layer:
                found_lp_obj = lp_obj
                break
        
        if found_lp_obj is None:    #Not found
            found_lp_obj = ClinguisticProcessors()
            found_lp_obj.set_layer(layer)
            self.add_linguistic_processors(found_lp_obj)
            
        found_lp_obj.add_linguistic_processor(my_lp)
        
        
            
    