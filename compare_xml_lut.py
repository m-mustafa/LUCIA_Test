# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:22:27 2017

@author: musta
"""
import test2
import pandas as pd
from xml.etree import ElementTree



def compare_xml_lut():
    "Assign Lists"   
    NminTop = []
    KsatParent=[]
    PWeathered=[]
    KavSub = []
    PbrayTop = []
    PhTop = []
    StonesSub = []
    KWeathered = []
    PhSub = []
    SandSub = []
    ClayTop = []
    CorgTop = []
    pSorption = []
    SandTop = []
    WaterTop = []
    DensityFactorSub = []
    ThicknessSub = []
    NtTop = []
    NminSub = []
    ClaySub = []
    StonesTop = []
    CorgSub = []
    DensityFactorTop = []
    WaterSub = []
    NtSub = []
    ThicknessTop = []
    KavTop = []
    PbraySub = []


    "Read XML file and assign parameters to the lists above"    
    for s in test2.soil_tabs:
        for attr in s:
            if (attr.tag == "soilObject"):
                soil_para1= attr.get("paraNminTop")
                soil_para1 = float(soil_para1)
                NminTop.append(soil_para1)
                
                soil_para2= attr.get("paraKsatParent")
                soil_para2 = float(soil_para2)
                KsatParent.append(soil_para2)
                
                soil_para3= attr.get("paraPWeathered")
                soil_para3 = float(soil_para3)
                PWeathered.append(soil_para3)
                
                soil_para4= attr.get("paraKavSub")
                soil_para4 = float(soil_para4)
                KavSub.append(soil_para4)
                
                soil_para5= attr.get("paraThicknessTop")
                soil_para5 = float(soil_para5)
                ThicknessTop.append(soil_para5)
                
                soil_para6= attr.get("paraThicknessSub")
                soil_para6 = float(soil_para6)
                ThicknessSub.append(soil_para6)
                
                soil_para7= attr.get("paraStonesTop")
                soil_para7 = float(soil_para7)
                StonesTop.append(soil_para7)
                
                soil_para8= attr.get("paraStonesSub")
                soil_para8 = float(soil_para8)
                StonesSub.append(soil_para8)
                
                soil_para9= attr.get("paraDensityFactorTop")
                soil_para9 = float(soil_para9)
                DensityFactorTop.append(soil_para9)
                
                soil_para10= attr.get("paraDensityFactorSub")
                soil_para10 = float(soil_para10)
                DensityFactorSub.append(soil_para10)
                
                soil_para11= attr.get("paraSandTop")
                soil_para11 = float(soil_para11)
                SandTop.append(soil_para11)
                
                soil_para12= attr.get("paraSandSub")
                soil_para12 = float(soil_para12)
                SandSub.append(soil_para12)
                
                soil_para13= attr.get("paraClayTop")
                soil_para13 = float(soil_para13)
                ClayTop.append(soil_para13)
                
                soil_para14= attr.get("paraClaySub")
                soil_para14 = float(soil_para14)
                ClaySub.append(soil_para14)
                
                soil_para15= attr.get("paraCorgTop")
                soil_para15 = float(soil_para15)
                CorgTop.append(soil_para15)
                
                soil_para16= attr.get("paraCorgSub")
                soil_para16 = float(soil_para16)
                CorgSub.append(soil_para16)
                
                soil_para17= attr.get("paraNtTop")
                soil_para17 = float(soil_para17)
                NtTop.append(soil_para17)

                soil_para18= attr.get("paraNtSub")
                soil_para18 = float(soil_para18)
                NtSub.append(soil_para18)
                
                soil_para19= attr.get("paraNminSub")
                soil_para19 = float(soil_para19)
                NminSub.append(soil_para19)
                
                soil_para20= attr.get("paraPbrayTop")
                soil_para20 = float(soil_para20)
                PbrayTop.append(soil_para20)
                
                soil_para21= attr.get("paraPbraySub")
                soil_para21 = float(soil_para21)
                PbraySub.append(soil_para21)
                
                soil_para22= attr.get("paraKavTop")
                soil_para22 = float(soil_para22)
                KavTop.append(soil_para22)
                
                soil_para23= attr.get("paraPhTop")
                soil_para23 = float(soil_para23)
                PhTop.append(soil_para23)
                
                soil_para24= attr.get("paraPhSub")
                soil_para24 = float(soil_para24)
                PhSub.append(soil_para24)
                
                soil_para25= attr.get("paraWaterTop")
                soil_para25 = float(soil_para25)
                WaterTop.append(soil_para25)
                
                soil_para26= attr.get("paraWaterSub")
                soil_para26 = float(soil_para26)
                WaterSub.append(soil_para26)
                
                soil_para27= attr.get("parapSorption")
                soil_para27 = float(soil_para27)
                pSorption.append(soil_para27)
                
                soil_para28= attr.get("paraKWeathered")
                soil_para28 = float(soil_para28)
                KWeathered.append(soil_para28)


    "Read Look up table"
    soil_df = pd.read_csv(test2.file_path + r"maps/soil.lut", header=0, sep='\s+')
    soil_df.drop([0])
    
    soil_df1 = soil_df['1'].tolist()
    soil_df2 = soil_df['2'].tolist()
    soil_df3 = soil_df['3'].tolist()
    soil_df4 = soil_df['4'].tolist()
    soil_df5 = soil_df['5'].tolist()
    soil_df6 = soil_df['6'].tolist()
    soil_df7 = soil_df['7'].tolist()
    soil_df8 = soil_df['8'].tolist()
    soil_df9 = soil_df['9'].tolist()
    soil_df10 = soil_df['10'].tolist()
    soil_df11 = soil_df['11'].tolist()
    soil_df12 = soil_df['12'].tolist()
    soil_df13 = soil_df['13'].tolist()
    soil_df14 = soil_df['14'].tolist()
    soil_df15 = soil_df['15'].tolist()
    soil_df16 = soil_df['16'].tolist()
    soil_df17 = soil_df['17'].tolist()
    soil_df18 = soil_df['18'].tolist()
    soil_df19 = soil_df['19'].tolist()
    soil_df20 = soil_df['20'].tolist()
    soil_df21 = soil_df['21'].tolist()
    soil_df22 = soil_df['22'].tolist()
    soil_df23 = soil_df['23'].tolist()
    soil_df24 = soil_df['24'].tolist()
    soil_df25 = soil_df['25'].tolist()
    soil_df26 = soil_df['26'].tolist()
    soil_df27 = soil_df['27'].tolist()
    soil_df28 = soil_df['28'].tolist()



    "Copmpare XML to Look up table"
    print '  '
    print ' comparing Lookup table to XML'
    if soil_df1 == ThicknessTop:
        print u'\u2714', 'ThicknessTop'
    else:
        print u'\u2716', 'ThicknessTop'
        print "XML", ThicknessTop 
        print "LUT", soil_df1
    
    
    if soil_df2 == ThicknessSub: 
        print u'\u2714', 'ThicknessSub'
    else:
        print u'\u2716', 'ThicknessSub'
        print "XML", ThicknessSub 
        print "LUT", soil_df2
    
    
    if soil_df3 == StonesTop: 
        print u'\u2714', 'StonesTop'
    else:
        print u'\u2716', 'StonesTop'
        print "XML", StonesTop 
        print "LUT", soil_df3
    
    
    if soil_df4 == StonesSub: 
        print u'\u2714', 'StonesSub'
    else:
        print u'\u2716', 'StonesSub'
        print "XML", StonesSub 
        print "LUT", soil_df4
    
    
    if soil_df5 == DensityFactorTop: 
        print u'\u2714', 'DensityFactorTop'
    else:
        print u'\u2716', 'DensityFactorTop'
        print "XML", DensityFactorTop 
        print "LUT", soil_df5
 
    
    if soil_df6 == DensityFactorSub: 
        print u'\u2714', 'DensityFactorSub'
    else:
        print u'\u2716', 'DensityFactorSub'
        print "XML", DensityFactorSub 
        print "LUT", soil_df6


    if soil_df7 == SandTop: 
        print u'\u2714', 'SandTop'
    else:
        print u'\u2716', 'SandTop'
        print "XML", SandTop 
        print "LUT", soil_df7


    if soil_df8 == SandSub: 
        print u'\u2714', 'SandSub'
    else:
        print u'\u2716', 'SandSub'
        print "XML", SandSub 
        print "LUT", soil_df8
    
    
    if soil_df9 == ClayTop: 
        print u'\u2714', 'ClayTop'
    else:
        print u'\u2716', 'ClayTop'
        print "XML", ClayTop 
        print "LUT", soil_df9


    if soil_df10 == ClaySub: 
        print u'\u2714', 'ClaySub'
    else:
        print u'\u2716', 'ClaySub'
        print "XML", ClaySub 
        print "LUT", soil_df10
    

    if soil_df11 == CorgTop: 
        print u'\u2714', 'CorgTop'
    else:
        print u'\u2716', 'CorgTop'
        print "XML", CorgTop 
        print "LUT", soil_df11
    
    
    if soil_df12 == CorgSub: 
        print u'\u2714', 'CorgSub'
    else:
        print u'\u2716', 'CorgSub'
        print "XML", CorgSub 
        print "LUT", soil_df12
        
    if soil_df13 == NtTop: 
        print u'\u2714', 'NtTop'
    else:
        print u'\u2716', 'NtTop'
        print "XML", NtTop 
        print "LUT", soil_df13
        
    if soil_df14 == NtSub: 
        print u'\u2714', 'NtSub'
    else:
        print u'\u2716', 'NtSub'
        print "XML", NtSub 
        print "LUT", soil_df14

    if soil_df15 == NminTop: 
        print u'\u2714', 'NminTop'
    else:
        print u'\u2716', 'NminTop'
        print "XML", NminTop
        print "LUT", soil_df15
        
    if soil_df16 == NminSub: 
        print u'\u2714', 'NminSub'
    else:
        print u'\u2716', 'NminSub'
        print "XML", NminSub
        print "LUT", soil_df16
        
    if soil_df17 == PbrayTop: 
        print u'\u2714', 'PbrayTop'
    else:
        print u'\u2716', 'PbrayTop'
        print "XML", PbrayTop
        print "LUT", soil_df17
        
    if soil_df18 == PbraySub: 
        print u'\u2714', 'PbraySub'
    else:
        print u'\u2716', 'PbraySub'
        print "XML", PbraySub 
        print "LUT", soil_df18
        
    if soil_df19 == KavTop: 
        print u'\u2714', 'KavTop'
    else:
        print u'\u2716', 'KavTop'
        print "XML", KavTop
        print "LUT", soil_df19
    
    
    if soil_df20 == KavSub: 
        print u'\u2714', 'KavSub'
    else:
        print u'\u2716', 'KavSub'
        print "XML", KavSub
        print "LUT", soil_df20
        
    if soil_df21 == PhTop: 
        print u'\u2714', 'PhTop'
    else:
        print u'\u2716', 'PhTop'
        print "XML", PhTop
        print "LUT", soil_df21
        
    if soil_df22 == PhSub: 
        print u'\u2714', 'PhSub'
    else:
        print u'\u2716', 'PhSub'
        print "XML", PhSub
        print "LUT", soil_df22
    
    
    if soil_df23 == KsatParent: 
        print u'\u2714', 'KsatParent'
    else:
        print u'\u2716', 'KsatParent'
        print "XML", KsatParent
        print "LUT", soil_df23
        
        
    if soil_df24 == WaterTop: 
        print u'\u2714', 'WaterTop'
    else:
        print u'\u2716', 'WaterTop'
        print "XML", WaterTop
        print "LUT", soil_df24
        
    
    if soil_df25 == WaterSub: 
        print u'\u2714', 'WaterSub'
    else:
        print u'\u2716', 'WaterSub'
        print "XML", WaterSub
        print "LUT", soil_df25
        
    
    if soil_df26 == pSorption: 
        print u'\u2714', 'pSorption'
    else:
        print u'\u2716', 'pSorption'
        print "XML", pSorption
        print "LUT", soil_df26
    
    
    if soil_df27 == PWeathered: 
        print u'\u2714', 'PWeathered'
    else:
        print u'\u2716', 'PWeathered'
        print "XML", PWeathered
        print "LUT", soil_df27
        
    if soil_df28 == KWeathered: 
        print u'\u2714', 'KWeathered'
    else:
        print u'\u2716', 'KWeathered'
        print "XML", KWeathered
        print "LUT", soil_df27
        
if __name__ == '__main__':
    compare_xml_lut()