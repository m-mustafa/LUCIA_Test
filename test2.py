# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:14:21 2017

@author: musta
"""
from xml.etree import ElementTree

import compare_xml_lut
import compare_lut_lut


file_path = "Sabatia_Watershed - Kopie/Plant5Control/"
file_path2 = "Sabatia_Watershed - Kopie/Plant5Control/"
settings_path = file_path + "settings.xml"


root = ElementTree.parse(settings_path).getroot()
soil_tabs = root.findall("scenario/tab")

compare_lut_lut.debug = False


print "Hi"




if __name__ == '__main__':
    compare_lut_lut.compare_lut_lut()
    compare_xml_lut.compare_xml_lut()



