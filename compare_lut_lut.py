# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:28:15 2017

@author: musta
"""

import pandas as pd
import test2
read_succ = True
debug = False
def compare_lut_lut():
    
    soil_df = pd.read_csv(test2.file_path + "maps/soil.lut", header=0, sep='\s+')
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
    
    soil2_df = pd.read_csv(test2.file_path2 + "maps/soil.lut", header=0, sep='\s+')
    soil2_df.drop([0])
    
    soil2_df1 = soil2_df['1'].tolist()
    soil2_df2 = soil2_df['2'].tolist()
    soil2_df3 = soil2_df['3'].tolist()
    soil2_df4 = soil2_df['4'].tolist()
    soil2_df5 = soil2_df['5'].tolist()
    soil2_df6 = soil2_df['6'].tolist()
    soil2_df7 = soil2_df['7'].tolist()
    soil2_df8 = soil2_df['8'].tolist()
    soil2_df9 = soil2_df['9'].tolist()
    soil2_df10 = soil2_df['10'].tolist()
    soil2_df11 = soil2_df['11'].tolist()
    soil2_df12 = soil2_df['12'].tolist()
    soil2_df13 = soil2_df['13'].tolist()
    soil2_df14 = soil2_df['14'].tolist()
    soil2_df15 = soil2_df['15'].tolist()
    soil2_df16 = soil2_df['16'].tolist()
    soil2_df17 = soil2_df['17'].tolist()
    soil2_df18 = soil2_df['18'].tolist()
    soil2_df19 = soil2_df['19'].tolist()
    soil2_df20 = soil2_df['20'].tolist()
    soil2_df21 = soil2_df['21'].tolist()
    soil2_df22 = soil2_df['22'].tolist()
    soil2_df23 = soil2_df['23'].tolist()
    soil2_df24 = soil2_df['24'].tolist()
    soil2_df25 = soil2_df['25'].tolist()
    soil2_df26 = soil2_df['26'].tolist()
    soil2_df27 = soil2_df['27'].tolist()
    soil2_df28 = soil2_df['28'].tolist()
    
    print '  '
    print ' comparing Lookup table to benchmark dataset '
    
    if soil_df1 == soil2_df1:
        read_succ = True
    else:
        read_succ = False
        
    if debug == True and read_succ == True:
        print u'\u2714', 'ThicknessTop'
    elif debug == True and read_succ == False :
        print u'\u2716', 'ThicknessTop'
        print "XML", soil2_df1 
        print "LUT", soil_df1
    else: pass
    

    if soil_df2 == soil2_df2: 
        read_succ = True
    else:
        read_succ = False
        
    if debug == True and read_succ == True:
        print u'\u2714', 'ThicknessSub'
    elif debug == True and read_succ == False:
        print u'\u2716', 'ThicknessSub'
        print "XML", soil2_df2 
        print "LUT", soil_df2        
    else: pass

        
    
    if soil_df3 == soil2_df3: 
        print u'\u2714', 'StonesTop'
    else:
        print u'\u2716', 'StonesTop'
        print "XML", soil2_df3 
        print "LUT", soil_df3
    
    
    if soil_df4 == soil2_df4: 
        print u'\u2714', 'StonesSub'
    else:
        print u'\u2716', 'StonesSub'
        print "XML", soil2_df4 
        print "LUT", soil_df4
    
    
    if soil_df5 == soil2_df5: 
        print u'\u2714', 'DensityFactorTop'
    else:
        print u'\u2716', 'DensityFactorTop'
        print "XML", soil2_df5 
        print "LUT", soil_df5
 
    
    if soil_df6 == soil2_df6: 
        print u'\u2714', 'DensityFactorSub'
    else:
        print u'\u2716', 'DensityFactorSub'
        print "XML", soil2_df6 
        print "LUT", soil_df6


    if soil_df7 == soil2_df7: 
        print u'\u2714', 'SandTop'
    else:
        print u'\u2716', 'SandTop'
        print "XML", soil2_df7 
        print "LUT", soil_df7


    if soil_df8 == soil2_df8: 
        print u'\u2714', 'SandSub'
    else:
        print u'\u2716', 'SandSub'
        print "XML", soil2_df8 
        print "LUT", soil_df8
    
    
    if soil_df9 == soil2_df9: 
        print u'\u2714', 'ClayTop'
    else:
        print u'\u2716', 'ClayTop'
        print "XML", soil2_df9 
        print "LUT", soil_df9


    if soil_df10 == soil2_df10: 
        print u'\u2714', 'ClaySub'
    else:
        print u'\u2716', 'ClaySub'
        print "XML", soil2_df10 
        print "LUT", soil_df10
    

    if soil_df11 == soil2_df11: 
        print u'\u2714', 'CorgTop'
    else:
        print u'\u2716', 'CorgTop'
        print "XML", soil2_df11 
        print "LUT", soil_df11
    
    
    if soil_df12 == soil2_df12: 
        print u'\u2714', 'CorgSub'
    else:
        print u'\u2716', 'CorgSub'
        print "XML", soil2_df12 
        print "LUT", soil_df12
        
    if soil_df13 == soil2_df13: 
        print u'\u2714', 'NtTop'
    else:
        print u'\u2716', 'NtTop'
        print "XML", soil2_df13 
        print "LUT", soil_df13
        
    if soil_df14 == soil2_df14: 
        print u'\u2714', 'NtSub'
    else:
        print u'\u2716', 'NtSub'
        print "XML", soil2_df14 
        print "LUT", soil_df14

    if soil_df15 == soil2_df15: 
        print u'\u2714', 'NminTop'
    else:
        print u'\u2716', 'NminTop'
        print "XML", soil2_df15
        print "LUT", soil_df15
        
    if soil_df16 == soil2_df16: 
        print u'\u2714', 'NminSub'
    else:
        print u'\u2716', 'NminSub'
        print "XML", soil2_df16
        print "LUT", soil_df16
        
    if soil_df17 == soil2_df17: 
        print u'\u2714', 'PbrayTop'
    else:
        print u'\u2716', 'PbrayTop'
        print "XML", soil2_df17
        print "LUT", soil_df17
        
    if soil_df18 == soil2_df18: 
        print u'\u2714', 'PbraySub'
    else:
        print u'\u2716', 'PbraySub'
        print "XML", soil2_df18 
        print "LUT", soil_df18
        
    if soil_df19 == soil2_df19: 
        print u'\u2714', 'KavTop'
    else:
        print u'\u2716', 'KavTop'
        print "XML", soil2_df19
        print "LUT", soil_df19
    
    
    if soil_df20 == soil2_df20: 
        print u'\u2714', 'KavSub'
    else:
        print u'\u2716', 'KavSub'
        print "XML", soil2_df20
        print "LUT", soil_df20
        
    if soil_df21 == soil2_df21: 
        print u'\u2714', 'PhTop'
    else:
        print u'\u2716', 'PhTop'
        print "XML", soil2_df21
        print "LUT", soil_df21
        
    if soil_df22 == soil2_df22: 
        print u'\u2714', 'PhSub'
    else:
        print u'\u2716', 'PhSub'
        print "XML", soil2_df22
        print "LUT", soil_df22
    
    
    if soil_df23 == soil2_df23: 
        print u'\u2714', 'KsatParent'
    else:
        print u'\u2716', 'KsatParent'
        print "XML", soil2_df23
        print "LUT", soil_df23
        
        
    if soil_df24 == soil2_df24: 
        print u'\u2714', 'WaterTop'
    else:
        print u'\u2716', 'WaterTop'
        print "XML", soil2_df24
        print "LUT", soil_df24
        
    
    if soil_df25 == soil2_df25: 
        print u'\u2714', 'WaterSub'
    else:
        print u'\u2716', 'WaterSub'
        print "XML", soil2_df25
        print "LUT", soil_df25
        
    
    if soil_df26 == soil2_df26: 
        print u'\u2714', 'pSorption'
    else:
        print u'\u2716', 'pSorption'
        print "XML", soil2_df26
        print "LUT", soil_df26
    
    
    if soil_df27 == soil2_df27: 
        print u'\u2714', 'PWeathered'
    else:
        print u'\u2716', 'PWeathered'
        print "XML", soil2_df27
        print "LUT", soil_df27
        
    if soil_df28 == soil2_df28: 
        print u'\u2714', 'KWeathered'
    else:
        print u'\u2716', 'KWeathered'
        print "XML", soil2_df28
        print "LUT", soil_df28



if __name__ == '__main__':
    compare_lut_lut()