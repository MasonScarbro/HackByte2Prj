import numpy as np
import pandas as pd
import json
df = pd.read_csv('CO2_Emissions_Canada.csv')



df.pop('Fuel Consumption Comb (mpg)')
df.pop('Fuel Consumption Comb (L/100 km)')
df.pop('Vehicle Class')
df.pop('Fuel Consumption Hwy (L/100 km)')
df.pop('Fuel Consumption City (L/100 km)')
df.pop('Engine Size(L)')
df.pop('Transmission')
df.pop('Cylinders')
df.pop('Fuel Type')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



#USER INPUT HERE: Input pulled from the HTML dropdown list form 

#truedf = df[ (df['Make'] == "USER INPU VALUE HERE") & (df['Model'] == 'USER INPUT VALUE HERE')]

#truedf.set_index('Make', inplace=True)
#print(truedf.iloc[0]['CO2 Emissions(g/km)'])

'''
The code used to get the specific model:

truedf = df[ (df['Make'] == 'ALFA ROMEO')]
print(truedf['Model'].unique())

Unique Values For Make Dropdown List:

'ACURA' 'ALFA ROMEO' 'ASTON MARTIN' 'AUDI' 'BENTLEY' 'BMW' 'BUICK'
 'CADILLAC' 'CHEVROLET' 'CHRYSLER' 'DODGE' 'FIAT' 'FORD' 'GMC' 'HONDA'
 'HYUNDAI' 'INFINITI' 'JAGUAR' 'JEEP' 'KIA' 'LAMBORGHINI' 'LAND ROVER'
 'LEXUS' 'LINCOLN' 'MASERATI' 'MAZDA' 'MERCEDES-BENZ' 'MINI' 'MITSUBISHI'
 'NISSAN' 'PORSCHE' 'RAM' 'ROLLS-ROYCE' 'SCION' 'SMART' 'SRT' 'SUBARU'
 'TOYOTA' 'VOLKSWAGEN' 'VOLVO' 'GENESIS' 'BUGATTI'

'''

'''
Code used to get specific models for each make:

models = df['Make'].unique()
for model in models:
	truedf = df[ (df['Make'] == model)]
	print('Unique Models for :', model, '\n')
	print(truedf['Model'].unique())

JSON FORMAT CODE:
models = df['Make'].unique()
for model in models:
    truedf = df[ (df['Make'] == model)]
    print('],','"',model, '": [', '\n')
    models_list = truedf['Model'].unique()
    models_string = "', '".join(models_list)
    print("'" + models_string + "'")
    print('\n')

'''
car_data = {

    "ACURA": [ 

    'ILX', 'ILX HYBRID', 'MDX 4WD', 'RDX AWD', 
    'RLX', 'TL', 'TL AWD', 'TSX', 'MDX SH-AWD', 
    'RLX HYBRID', 'TLX', 'TLX SH-AWD', 'MDX SH-AWD ELITE', 
    'MDX HYBRID AWD', 'NSX', 'TLX A-SPEC', 'TLX SH-AWD A-SPEC', 
    'MDX SH-AWD A-SPEC', 'MDX Hybrid AWD', 'RDX AWD A-SPEC', 
    'RLX Hybrid', 'TLX SH-AWD A-SPEC/Limited Edition'


    ], 
    "ALFA ROMEO": [ 

    '4C', '4C SPIDER', 'GIULIA', 'GIULIA AWD', 'GIULIA QUADRIFOGLIO', 
    '4C COUPE', 'STELVIO AWD', 'STELVIO QUADRIFOGLIO', '4C Coupe', '4C Spider', 
    'Giulia', 'Giulia AWD', 'Giulia Quadrifoglio', 'Stelvio', 'Stelvio AWD', 
    'Stelvio AWD Quadrifoglio'


    ], 
    "ASTON MARTIN": [ 

    'DB9', 'RAPIDE', 'V8 VANTAGE', 'V8 VANTAGE S', 
    'VANQUISH', 'RAPIDE S', 'V12 VANTAGE S', 'VANTAGE GT', 
    'DB9 GT', 'DB11 V12', 'DB11 V8', 'DB11 AMR', 'DBS Superleggera', 
    'Rapide AMR', 'Vanquish Zagato', 'Vantage V8'


    ],
    "AUDI": [ 

    'A4', 'A4 QUATTRO', 'A5 CABRIOLET QUATTRO', 
    'A5 QUATTRO', 'A6 QUATTRO', 'A6 QUATTRO TDI (modified)', 
    'A7 QUATTRO', 'A7 QUATTRO TDI (modified)', 'A8', 'A8 TDI (modified)', 
    'A8L', 'A8L TDI (modified)', 'ALLROAD QUATTRO', 'Q5', 'Q5 TDI (modified)', 
    'Q5 HYBRID', 'Q7', 'Q7 TDI (modified)', 'R8', 'R8 SPYDER', 'RS 5', 'RS 5 CABRIOLET', 
    'RS 7', 'S4', 'S5', 'S5 CABRIOLET', 'S6', 'S7', 'S8', 'SQ5', 'TT COUPE QUATTRO', 
    'TT ROADSTER QUATTRO', 'TTS COUPE QUATTRO', 'TTS ROADSTER QUATTRO', 'A3', 
    'A3 TDI (modified)', 'A3 QUATTRO', 'A3 CABRIOLET QUATTRO', 'A4 ALLROAD QUATTRO', 
    'Q3', 'Q3 QUATTRO', 'S3', 'A8 QUATTRO', 'A8 QUATTRO TDI (modified)', 'A8L QUATTRO', 
    'Q5 QUATTRO', 'Q5 QUATTRO TDI (modified)', 'Q5 HYBRID QUATTRO', 'RS 7 QUATTRO', 
    'S3 QUATTRO', 'S4 QUATTRO', 'S5 QUATTRO', 'S5 CABRIOLET QUATTRO', 'S6 QUATTRO', 
    'S7 QUATTRO', 'S8 QUATTRO', 'SQ5 QUATTRO', 'A4 ULTRA', 'A5 SPORTBACK QUATTRO', 
    'R8 QUATTRO', 'RS 3', 'S5 SPORTBACK', 'TT RS', 'TTS COUPE', 'A3 quattro', 
    'A3 Cabriolet quattro', 'A4 quattro', 'A4 allroad quattro', 'A5 quattro', 
    'A5 Cabriolet quattro', 'A5 Sportback quattro', 'A6 quattro', 'A7 quattro', 
    'Q3 quattro', 'Q8', 'RS 5 Coupe', 'RS 5 Sportback', 'S5 Cabriolet', 'S5 Sportback', 
    'TT Coupe quattro', 'TT Roadster quattro', 'TT RS Coupe', 'TTS Coupe', 'A6 allroad', 
    'R8 Coupe', 'R8 Spyder'


    ], 
    "BENTLEY": [ 

    'CONTINENTAL GT', 'CONTINENTAL GTC', 'CONTINENTAL GT SPEED CONVERTIBLE', 'FLYING SPUR', 
    'MULSANNE', 'CONTINENTAL GT CONVERTIBLE', 'CONTINENTAL GT3-R', 'BENTAYGA', 'MULSANNE EWB', 
    'CONTINENTAL SUPERSPORTS', 'Bentayga', 'Mulsanne', 'Continental GT', 'Continental GT Convertible', 
    'Flying Spur'


    ], 
    "BMW": [ 

    '320i', '320i xDRIVE', '328d xDRIVE', '328d xDRIVE TOURING', '328i', '328i xDRIVE', 
    '328i xDRIVE GRAN TURISMO', '328i xDRIVE TOURING', '335i', '335i xDRIVE', 
    '335i xDRIVE GRAN TURISMO', '428i COUPE', '428i xDRIVE COUPE', '435i COUPE', 
    '435i xDRIVE COUPE', '528i', '528i xDRIVE', '535d xDRIVE', '535i xDRIVE', 
    '535i xDRIVE GRAN TURISMO', '550i xDRIVE', '550i xDRIVE GRAN TURISMO', 
    '640i xDRIVE GRAN COUPE', '650i xDRIVE CABRIOLET', '650i xDRIVE COUPE', 
    '650i xDRIVE GRAN COUPE', '740Li xDRIVE', '750i xDRIVE', '750Li xDRIVE', 
    '760Li', 'ACTIVEHYBRID 3', 'ACTIVEHYBRID 5', 'ACTIVEHYBRID 7L', 'ALPINA B7 xDRIVE LWB', 
    'ALPINA B7 xDRIVE SWB', 'M5', 'M6', 'M6 CABRIOLET', 'M6 GRAN COUPE', 'X1 xDRIVE28i', 
    'X1 xDRIVE35i', 'X3 xDRIVE28i', 'X3 xDRIVE35i', 'X5 xDRIVE35i', 'X5 xDRIVE50i', 'X6 M', 
    'X6 xDRIVE35i', 'X6 xDRIVE50i', 'Z4 sDRIVE28i', 'Z4 sDRIVE35i', 'Z4 sDRIVE35is', 
    '228i CABRIOLET', '228i COUPE', '228i xDRIVE CABRIOLET', '228i xDRIVE COUPE', 
    '320i SEDAN', '320i xDRIVE SEDAN', '328d xDRIVE SEDAN', '328i SEDAN', '328i xDRIVE SEDAN', 
    '335i SEDAN', '335i xDRIVE SEDAN', '428i CABRIOLET', '428i GRAN COUPE', 
    '428i xDRIVE CABRIOLET', '428i xDRIVE GRAN COUPE', '435i CABRIOLET', '435i GRAN COUPE', 
    '435i xDRIVE CABRIOLET', '435i xDRIVE GRAN COUPE', '528i SEDAN', '528i xDRIVE SEDAN', 
    '535d xDRIVE SEDAN', '535i xDRIVE SEDAN', '550i xDRIVE SEDAN', '640i xDRIVE CABRIOLET', 
    '740Ld xDRIVE SEDAN', '740Li xDRIVE SEDAN', '750i xDRIVE SEDAN', '750Li xDRIVE SEDAN', 
    '760Li SEDAN', 'ALPINA B6 xDRIVE GRAN COUPE', 'M235i CABRIOLET', 'M235i COUPE', 
    'M235i xDRIVE COUPE', 'M3 SEDAN', 'M4 CABRIOLET', 'M4 COUPE', 'M5 SEDAN', 'M6 COUPE', 
    'X3 xDRIVE28d', 'X4 xDRIVE28i', 'X4 xDRIVE35i', 'X5 M', 'X5 xDRIVE35d', '228i', 
    '228i xDRIVE', '340i', '340i xDRIVE', 'M2', 'M235i', 'M235i xDRIVE', 'M235i xDRIVE CABRIOLET', 
    'M3', 'X4 M40i', '230i CABRIOLET', '230i COUPE', '230i xDRIVE CABRIOLET', '230i xDRIVE COUPE', 
    '330i xDRIVE', '330i xDRIVE GRAN TURISMO', '330i xDRIVE TOURING', '340i xDRIVE GRAN TURISMO', 
    '430i xDRIVE CABRIOLET', '430i xDRIVE COUPE', '430i xDRIVE GRAN COUPE', '440i COUPE', 
    '440i xDRIVE CABRIOLET', '440i xDRIVE COUPE', '440i xDRIVE GRAN COUPE', '530i xDRIVE', 
    '540i xDRIVE', 'ALPINA B7 xDRIVE', 'M240i CABRIOLET', 'M240i COUPE', 'M240i xDRIVE CABRIOLET', 
    'M240i xDRIVE COUPE', 'M760i xDRIVE', '640i xDRIVE GRAN TURISMO', '750i xDRIVE SWB', 'M550i xDRIVE', 
    'X2 xDRIVE28i', 'X3 xDRIVE30i', 'X3 M40i', '230i xDrive Cabriolet', '230i xDrive Coupe', 
    '330i xDrive', '330i xDrive Gran Turismo', '330i xDrive Touring', '430i xDrive Cabriolet', 
    '430i xDrive Coupe', '430i xDrive Gran Coupe', '440i Coupe', '440i xDrive Cabriolet', 
    '440i xDrive Coupe', '440i xDrive Gran Coupe', '530i xDrive', '540i xDrive', 
    '640i xDrive Gran Coupe', '640i xDrive Gran Turismo', '650i xDrive Gran Coupe', 
    '750i xDrive', '750Li xDrive', 'Alpina B6 xDrive Gran Coupe', 'Alpina B7 xDrive', 
    'M2 Competition', 'M240i Cabriolet', 'M240i Coupe', 'M240i Coupe M Performance', 
    'M240i xDrive Cabriolet', 'M240i xDrive Coupe', 'M240i xDrive Coupe M Performance', 
    'M4 Cabriolet', 'M4 Cabriolet Competition', 'M4 Coupe', 'M4 Coupe Competition', 'M4 CS', 
    'M5 Competition', 'M550i xDrive', 'M6 Gran Coupe', 'M760Li xDrive', 'M850i xDrive Cabriolet', 
    'M850i xDrive Coupe', 'X1 xDrive28i', 'X2 xDrive28i', 'X3 xDrive30i', 'X4 xDrive30i', 
    'X5 xDrive40i', 'X5 xDrive50i', 'X6 xDrive35i', 'X6 xDrive50i', 'X7 xDrive40i', 'X7 xDrive50i', 
    '230i Cabriolet', '230i Coupe', '330i xDrive Sedan', '430i Coupe', '530i xDrive Sedan', 
    '540i xDrive Sedan', '750i xDrive Sedan', '750Li xDrive Sedan', 'M340i xDrive Sedan', 'M5 Sedan',
    'M550i xDrive Sedan', 'M760i xDrive Sedan', 'M8 Cabriolet', 'M8 Cabriolet Competition', 
    'M8 Coupe', 'M8 Coupe Competition', 'M8 Gran Coupe', 'M8 Gran Coupe Competition', 
    'M850i xDrive Gran Coupe', 'X2 M35i', 'X3 M', 'X3 M Competition', 'X4 M', 'X4 M Competition', 
    'X5 M50i', 'X6 xDrive40i', 'X6 M50i', 'X7 M50i', 'Z4 sDrive30i', 'Z4 M40i'


    ],
    "BUICK": [ 

    'ENCLAVE', 'ENCLAVE AWD', 'ENCORE', 'ENCORE AWD', 'LACROSSE', 'LACROSSE AWD', 'LACROSSE eASSIST',
    'REGAL', 'REGAL AWD', 'REGAL eASSIST', 'VERANO', 'ENCORE SPORT TOURING', 'ENCORE SPORT TOURING AWD',
    'ENVISION AWD', 'LACROSSE FFV', 'LACROSSE AWD FFV', 'Enclave', 'Enclave AWD', 'Encore', 'Encore AWD',
    'Envision AWD', 'LaCrosse', 'LaCrosse eAssist', 'LaCrosse AWD', 'Regal', 'Regal AWD',
    'Encore GX', 'Encore GX AWD'


    ],
    "CADILLAC": [ 

    'ATS', 'ATS AWD', 'CTS COUPE', 'CTS COUPE AWD', 'CTS SEDAN', 'CTS SEDAN AWD', 'CTS SEDAN Vsport', 
    'CTS SPORT WAGON', 'CTS SPORT WAGON AWD', 'CTS-V COUPE', 'CTS-V SEDAN', 'CTS-V SPORT WAGON', 
    'ESCALADE AWD', 'ESCALADE ESV AWD', 'SRX', 'SRX AWD', 'XTS', 'XTS AWD', 'XTS Vsport AWD',
    'CTS', 'CTS AWD', 'CTS Vsport', 'ESCALADE 4WD', 'ESCALADE ESV 4WD', 'ATS-V', 'CT6', 'CT6 AWD', 
    'CTS-V', 'XT5', 'XT5 AWD', 'Escalade 4WD', 'XT4', 'XT4 AWD', 'CT4', 'CT4 AWD', 'CT4-V', 'CT4-V AWD', 
    'CT5', 'CT5 AWD', 'CT5-V', 'CT5-V AWD', 'XT6 AWD'


    ],
    "CHEVROLET": [ 

    'CAMARO', 'CAMARO 2LS', 'CAMARO SS', 'CAMARO ZL1', 'CORVETTE', 
    'CRUZE', 'CRUZE DIESEL', 'CRUZE ECO', 'EQUINOX', 'EQUINOX AWD', 
    'EXPRESS 1500 CARGO', 'EXPRESS 1500 CARGO AWD', 'EXPRESS 1500 CARGO CONV', 
    'EXPRESS 1500 CARGO CONV AWD', 'EXPRESS 1500 PASSENGER', 'EXPRESS 1500 PASSENGER AWD', 
    'EXPRESS 2500 PASSENGER', 'EXPRESS 3500 PASSENGER', 'IMPALA', 'IMPALA ECO', 'MALIBU', 'ORLANDO', 
    'SILVERADO', 'SILVERADO 4WD', 'SONIC', 'SONIC RS', 'SONIC 5', 'SONIC 5 RS', 'SPARK', 'SUBURBAN', 
    'SUBURBAN 4WD', 'TAHOE', 'TAHOE 4WD', 'TRAVERSE', 'TRAVERSE AWD', 'TRAX', 'TRAX AWD', 'CAMARO Z/28', 
    'CITY EXPRESS', 'COLORADO', 'COLORADO 4WD', 'CORVETTE Z06', 'EQUINOX FFV', 'EQUINOX AWD FFV', 
    'EXPRESS 2500 PASSENGER FFV', 'EXPRESS 3500 PASSENGER FFV', 'CRUZE PREMIER', 'CRUZE LIMITED', 
    'CRUZE LIMITED ECO', 'IMPALA FFV', 'IMPALA DUAL FUEL', 'MALIBU LIMITED', 'MALIBU HYBRID', 
    'SILVERADO FFV', 'SILVERADO 4WD FFV', 'SILVERADO eASSIST 4WD', 'SUBURBAN FFV', 'SUBURBAN 4WD FFV', 
    'TAHOE FFV', 'TAHOE 4WD FFV', 'TRAX 4WD', 'COLORADO ZR2 4WD', 'CRUZE HATCHBACK', 
    'CRUZE HATCHBACK PREMIER', 'CRUZE HATCHBACK DIESEL', 'SILVERADO eASSIST', 'Blazer', 
    'Blazer AWD', 'Camaro', 'Camaro SS', 'Camaro ZL1', 'Colorado', 'Colorado 4WD', 'Colorado ZR2 4WD', 
    'Corvette', 'Corvette Z06', 'Corvette ZR1', 'Cruze', 'Cruze Premier', 'Cruze Diesel', 
    'Cruze Hatchback', 'Cruze Hatchback Premier', 'Cruze Hatchback Diesel', 'Equinox', 'Equinox AWD', 
    'Impala', 'Malibu', 'Malibu Hybrid', 'Silverado', 'Silverado FFV', 'Silverado 4WD', 
    'Silverado 4WD Trail Boss', 'Silverado 4WD FFV', 'Silverado LD', 'Silverado LD 4WD', 
    'Spark', 'Suburban', 'Suburban FFV', 'Suburban 4WD', 'Suburban 4WD FFV', 'Tahoe', 
    'Tahoe FFV', 'Tahoe 4WD', 'Tahoe 4WD FFV', 'Traverse', 'Traverse AWD', 'Trax', 
    'Trax 4WD', 'Silverado WT', 'Silverado WT 4WD', 'Silverado 4WD Custom Trail Boss', 
    'Silverado 4WD LT Trail Boss', 'Trax AWD'


    ],
    "CHRYSLER": [ 

    '300', '200 CONVERTIBLE', '200 CONVERTIBLE FFV', '200 SEDAN', '200 SEDAN FFV', '300 (MDS)', 
    '300 AWD', '300 AWD (MDS)', '300 AWD FFV', '300 FFV', '300 SRT (MDS)', 'TOWN & COUNTRY FFV', 
    '200', '200 FFV', '200 AWD', '200 AWD FFV', 'PACIFICA', 'PACIFICA (Stop-Start)', 'Pacifica', 
    'Pacifica (Stop-Start)', 'Voyager (Stop-Start)'


    ],
    "DODGE": [ 

    'AVENGER', 'AVENGER FFV', 'CHALLENGER', 'CHALLENGER (MDS)', 'CHALLENGER SRT', 
    'CHALLENGER SRT (MDS)', 'CHARGER', 'CHARGER (MDS)', 'CHARGER AWD', 'CHARGER AWD (MDS)', 
    'CHARGER AWD FFV', 'CHARGER FFV', 'CHARGER SRT (MDS)', 'DART', 'DART FFV', 'DART GT', 
    'DART TURBO AERO', 'DURANGO AWD (MDS)', 'DURANGO AWD FFV', 'GRAND CARAVAN FFV', 'JOURNEY', 
    'JOURNEY AWD', 'JOURNEY FFV', 'CHALLENGER SRT HELLCAT', 'CHARGER SRT 392 HEMI', 
    'CHARGER SRT HELLCAT', 'VIPER SRT COUPE', 'DURANGO AWD', 'VIPER SRT', 'CHALLENGER GT', 
    'VIPER', 'CHALLENGER GT AWD', 'CHALLENGER GT AWD FFV', 'CHALLENGER SRT DEMON', 'DURANGO AWD SRT', 
    'Challenger', 'Challenger (MDS)', 'Challenger GT AWD', 'Challenger SRT Hellcat', 
    'Challenger SRT Hellcat Redeye', 'Charger', 'Charger FFV', 'Charger (MDS)', 'Charger AWD', 
    'Charger AWD FFV', 'Charger AWD (MDS)', 'Charger SRT Hellcat', 'Durango AWD', 'Durango AWD SRT', 
    'Grand Caravan FFV', 'Journey', 'Journey FFV', 'Journey AWD', 'Challenger AWD', 
    'Challenger Widebody (MDS)', 'Challenger SRT Hellcat Widebody', 'Charger Widebody (MDS)', 
    'Charger SRT Hellcat Widebody', 'Grand Caravan'


    ],
    "FIAT": [ 

    '500 ABARTH CABRIO', '500 ABARTH HATCHBACK', '500 CABRIO', '500 CABRIO TURBO', '500 HATCHBACK', 
    '500 HATCHBACK TURBO', '500L TURBO', '500L', '500X', '500X AWD', '124 SPIDER', '500', '500 ABARTH', 
    '124 Spider'


    ],
    "FORD": [ 

    'C-MAX HYBRID', 'E150 VAN FFV', 'E150 WAGON FFV', 'E350 WAGON', 'E350 WAGON FFV', 'EDGE', 'EDGE AWD',
    'ESCAPE', 'ESCAPE AWD', 'EXPEDITION 4X4 FFV', 'EXPLORER', 'EXPLORER AWD', 'EXPLORER FFV', 
    'EXPLORER FFV AWD', 'F-150', 'F-150 4X4', 'F-150 FFV', 'F-150 FFV 4X4', 'F-150 RAPTOR 4X4', 
    'FIESTA', 'FIESTA SFE', 'FIESTA ST', 'FLEX', 'FLEX AWD', 'FLEX AWD (EcoBoost)', 'FOCUS', 
    'FOCUS FFV', 'FOCUS SFE FFV', 'FUSION', 'FUSION (Start/Stop)', 'FUSION AWD', 'FUSION HYBRID', 
    'MUSTANG', 'MUSTANG CONVERTIBLE', 'TAURUS', 'TAURUS AWD', 'TAURUS FFV', 'TAURUS FFV AWD', 
    'TRANSIT CONNECT', 'TRANSIT CONNECT TAXI', 'TRANSIT CONNECT WAGON', 'EDGE (Start/Stop)', 
    'EDGE SPORT AWD', 'EXPEDITION 4X4', 'EXPEDITION MAX 4X4', 'EXPLORER AWD (EcoBoost)', 'T-150 WAGON', 
    'T-150 WAGON FFV', 'TRANSIT CONNECT VAN', 'TRANSIT CONNECT WAGON TAXI', 'EXPEDITION EL 4X4', 
    'F-150 (Payload Pkg)', 'F-150 FFV (Payload Pkg)', 'F-150 4X4 (Payload Pkg)', 
    'F-150 FFV 4X4 (Payload Pkg)', 'FLEX AWD GTDI', 'FOCUS RS AWD', 'FOCUS ST', 'SHELBY GT350 MUSTANG', 
    'TRANSIT CONNECT VAN FFV', 'TRANSIT CONNECT WAGON FFV', 'TRANSIT CONNECT WAGON LWB', 
    'TRANSIT CONNECT WAGON LWB FFV', 'ESCAPE FFV', 'F-150 (LT Tire Pkg)', 'F-150 4X4 (LT Tire Pkg)', 
    'F-150 FFV 4X4 (LT Tire Pkg)', 'FOCUS (Start/Stop)', 'GT', 'MUSTANG (Performance Pkg)', 
    'ECOSPORT', 'ECOSPORT AWD', 'F-150 FFV (LT Tire Pkg)', 'F-150 4X4 XL/XLT', 'F-150 RAPTOR 4WD', 
    'EcoSport', 'EcoSport AWD', 'Edge', 'Edge AWD', 'Escape', 'Escape FFV', 'Escape AWD', 
    'Expedition 4X4', 'Expedition MAX 4X4', 'Explorer AWD', 'Explorer FFV AWD', 'F-150 4X4 Limited', 
    'F-150 Raptor 4X4', 'Flex', 'Flex AWD', 'Flex AWD GTDI', 'Fiesta', 'Fiesta ST', 'Fusion', 
    'Fusion Hybrid', 'Mustang', 'Mustang (Performance Pkg)', 'Mustang Bullitt', 'Mustang Convertible', 
    'Ranger 4WD', 'Shelby GT350 Mustang', 'T-150 Wagon', 'Taurus FFV', 'Taurus AWD', 'Taurus FFV AWD', 
    'Transit Connect Van', 'Transit Connect Van FFV', 'Transit Connect Wagon LWB', 
    'Transit Connect Wagon LWB FFV', 'Escape Hybrid', 'Escape Hybrid AWD', 'Explorer Hybrid AWD', 
    'Mustang Convertible (Performance Pkg)', 'Shelby GT500 Mustang', 'T-150 Wagon FFV', 
    'T-150 Wagon FFV 4WD', 'Transit Connect Van LWB'


    ],
    "GMC": [ 

    'ACADIA', 'ACADIA AWD', 'SAVANA 1500 CARGO', 'SAVANA 1500 CARGO AWD', 'SAVANA 1500 CARGO CONV', 
    'SAVANA 1500 CARGO CONV AWD', 'SAVANA 1500 PASSENGER', 'SAVANA 1500 PASSENGER AWD', 
    'SAVANA 2500 PASSENGER', 'SAVANA 3500 PASSENGER', 'SIERRA', 'SIERRA 4WD', 'TERRAIN', 
    'TERRAIN AWD', 'YUKON', 'YUKON 4WD', 'YUKON DENALI AWD', 'YUKON DENALI XL AWD', 'YUKON XL', 
    'YUKON XL 4WD', 'CANYON', 'CANYON 4WD', 'SAVANA 2500 PASSENGER FFV', 'SAVANA 3500 PASSENGER FFV', 
    'TERRAIN FFV', 'YUKON DENALI 4WD', 'YUKON XL DENALI 4WD', 'SIERRA FFV', 'SIERRA 4WD FFV', 
    'SIERRA eASSIST 4WD', 'YUKON FFV', 'YUKON 4WD FFV', 'YUKON XL FFV', 'YUKON XL 4WD FFV', 
    'SIERRA eASSIST', 'Acadia', 'Acadia AWD', 'Canyon', 'Canyon 4WD', 'Sierra', 'Sierra FFV', 
    'Sierra 4WD', 'Sierra 4WD FFV', 'Sierra 4WD AT4', 'Sierra LTD', 'Sierra LTD 4WD', 'Terrain', 
    'Terrain AWD', 'Yukon', 'Yukon FFV', 'Yukon 4WD', 'Yukon 4WD FFV', 'Yukon XL', 'Yukon XL FFV', 
    'Yukon XL 4WD', 'Yukon XL 4WD FFV', 'Sierra WT', 'Sierra WT 4WD'


    ], 
    "HONDA": [ 

    'ACCORD', 'ACCORD HYBRID', 'CIVIC', 'CROSSTOUR AWD', 'CR-V', 'CR-V AWD', 'CR-Z', 'FIT', 'ODYSSEY', 
    'PILOT', 'PILOT AWD', 'RIDGELINE AWD', 'CIVIC Si', 'CIVIC HYBRID', 'PILOT 4WD', 'ACCORD COUPE', 
    'ACCORD SEDAN', 'ACCORD SPORT', 'CIVIC COUPE', 'CIVIC SEDAN', 'HR-V', 'HR-V AWD', 'CIVIC HATCHBACK', 
    'ACCORD SPORT/TOURING', 'CIVIC COUPE Si', 'CIVIC HATCHBACK SPORT', 'CIVIC SEDAN Si', 'CIVIC TYPE R', 
    'ODYSSEY TOURING', 'Accord', 'Accord Sport/Touring', 'Accord Hybrid', 'Civic Coupe', 'Civic Coupe Si', 'Civic Hatchback', 'Civic Hatchback Sport', 'Civic Sedan', 'Civic Sedan Si', 'Civic Type R', 'Fit', 'Insight EX', 'Insight Touring', 'Odyssey', 'Odyssey Touring', 'Passport AWD', 'Pilot', 'Pilot AWD', 'Ridgeline AWD', 'Insight EX/Touring'


    ], 
    "HYUNDAI": [ 

    'ACCENT', 'ELANTRA GT', 'EQUUS', 'GENESIS', 'SANTA FE', 'SANTA FE 4WD', 'SANTA FE SPORT', 
    'SANTA FE SPORT 4WD', 'SONATA', 'SONATA HYBRID', 'SONATA HYBRID LIMITED', 'TUCSON', 'TUCSON 4WD', 
    'VELOSTER', 'VELOSTER TURBO', 'ELANTRA', 'ELANTRA COUPE', 'GENESIS AWD', 'GENESIS COUPE', 
    'SANTA FE AWD', 'SANTA FE SPORT AWD', 'SANTA FE ULTIMATE AWD', 'SONATA SPORT/LIMITED', 'TUCSON AWD', 
    'IONIQ', 'IONIQ BLUE', 'SONATA HYBRID SE', 'KONA', 'KONA AWD', 'SANTA FE SPORT ULTIMATE AWD', 
    'Accent', 'Elantra', 'Elantra GT', 'IONIQ Blue', 'Kona', 'Kona AWD', 'Santa Fe', 'Santa Fe AWD', 
    'Santa Fe XL', 'Santa Fe XL AWD', 'Santa Fe XL Ultimate AWD', 'Sonata', 'Sonata SE', 'Sonata Hybrid', 
    'Sonata Hybrid SE', 'Tucson', 'Tucson AWD', 'Veloster', 'Veloster N', 'Veloster Turbo', 'Palisade',
    'Palisade AWD', 'Venue'


    ], 
    "INFINITI": [ 

    'Q50', 'Q50 AWD', 'Q50 HYBRID', 'Q50 HYBRID AWD', 'Q60 AWD COUPE', 'Q60 CONVERTIBLE', 'Q60 COUPE', 
    'Q70', 'Q70 AWD', 'Q70 HYBRID', 'QX50 AWD', 'QX60', 'QX60 AWD', 'QX60 HYBRID AWD', 'QX70 AWD', 
    'QX80 4WD', 'Q60', 'Q60 AWD', 'Q50S AWD', 'Q50S RED SPORT', 'Q50S RED SPORT AWD', 
    'Q60S RED SPORT AWD', 'QX30', 'QX30 AWD', 'Q50 AWD RED SPORT', 'Q60 AWD RED SPORT', 
    'Q50 AWD Red Sport', 'Q60 AWD Red Sport'


    ], 
    "JAGUAR": [ 

    'F-TYPE CONVERTIBLE', 'F-TYPE S CONVERTIBLE', 'F-TYPE V8 S CONVERTIBLE', 'XF', 'XF 3.0L AWD', 
    'XFR', 'XFR-S', 'XJ AWD', 'XJ SUPERCHARGED', 'XJL AWD PORTFOLIO', 'XJL SUPERCHARGED', 
    'XJR', 'XJR LWB', 'XK CONVERTIBLE', 'XK COUPE', 'XKR CONVERTIBLE', 'XKR COUPE', 
    'XKR-S CONVERTIBLE', 'XKR-S COUPE', 'F-TYPE COUPE', 'F-TYPE S COUPE', 'F-TYPE V8 R COUPE', 
    'XF AWD', 'F-TYPE PROJECT 7 CONVERTIBLE', 'F-TYPE R AWD CONVERTIBLE', 'F-TYPE R AWD COUPE', 
    'F-TYPE S CONVERTIBLE AWD', 'F-TYPE S COUPE AWD', 'XF AWD ', 'XJ R-SPORT 3.0 AWD', 
    'XJL 3.0 AWD PORTFOLIO', 'F-PACE 35t', 'F-TYPE R CONVERTIBLE AWD', 'F-TYPE R COUPE AWD', 
    'XE 20d AWD', 'XE 35t AWD', 'XF 20d AWD', 'XF 35t AWD', 'XJL PORTFOLIO 3.0 AWD', 'XJR  LWB', 
    'F-PACE 20d', 'F-PACE 25t', 'F-TYPE CONVERTIBLE R-DYNAMIC', 'F-TYPE CONVERTIBLE R-DYNAMIC AWD', 
    'F-TYPE COUPE R-DYNAMIC', 'F-TYPE COUPE R-DYNAMIC AWD', 'XE 25t AWD', 'XF 25t AWD', 
    'XJ R-SPORT AWD', 'XJL PORTFOLIO AWD', 'E-PACE P250', 'F-TYPE Convertible', 
    'F-TYPE Convertible R-Dynamic', 'F-TYPE Convertible R-Dynamic AWD', 'F-TYPE Coupe', 
    'F-TYPE Coupe R-Dynamic', 'F-TYPE Coupe R-Dynamic AWD', 'F-TYPE R AWD Convertible', 
    'F-TYPE R AWD Coupe', 'XJ R-Sport AWD', 'XJL Portfolio AWD', 'E-PACE P300', 'F-PACE 30t', 
    'F-PACE S', 'F-PACE SVR', 'F-TYPE P300 Convertible', 'F-TYPE SVR AWD Convertible', 
    'F-TYPE P300 Coupe', 'F-TYPE SVR AWD Coupe', 'XE P250 AWD', 'XE P300 AWD', 'XF 30t AWD', 'XF S AWD'


    ], 
    "JEEP": [ 

    'CHEROKEE', 'CHEROKEE 4X4', 'CHEROKEE 4X4 ACTIVE DRIVE II', 'CHEROKEE TRAILHAWK 4X4', 'COMPASS', 
    'COMPASS 4X4', 'COMPASS 4X4 TRAIL RATED', 'GRAND CHEROKEE 4X4 (MDS)', 'GRAND CHEROKEE 4X4 DIESEL', 
    'GRAND CHEROKEE 4X4 FFV', 'GRAND CHEROKEE SRT 4X4 (MDS)', 'PATRIOT', 'PATRIOT 4X4', 
    'PATRIOT 4X4 TRAIL RATED', 'WRANGLER 4X4 (2-DOOR)', 'WRANGLER UNLIMITED 4X4 (4-DOOR)', 
    'CHEROKEE FFV', 'CHEROKEE 4X4 FFV', 'RENEGADE', 'RENEGADE FFV', 'RENEGADE 4X4', 'WRANGLER 4X4', 
    'WRANGLER UNLIMITED 4X4', 'GRAND CHEROKEE 4X4', 'CHEROKEE 4X4 ACTIVE DRIVE I', 
    'CHEROKEE 4X4 ACTIVE DRIVE LOCK', 'GRAND CHEROKEE SRT8', 'NEW COMPASS', 'NEW COMPASS 4X4', 
    'CHEROKEE 4X4 ACTIVE DRIVE I FFV', 'GRAND CHEROKEE 4X4 SRT', 'GRAND CHEROKEE 4X4 TRACKHAWK', 
    'NEW WRANGLER 4X4', 'NEW WRANGLER UNLIMITED 4X4', 'WRANGLER JK 4X4', 'WRANGLER JK UNLIMITED 4X4', 
    'Cherokee', 'Cherokee 4X4 Active Drive I', 'Cherokee 4X4 Active Drive II', 
    'Cherokee 4X4 Active Drive Lock', 'Compass', 'Compass 4X4', 'Grand Cherokee 4X4', 
    'Grand Cherokee 4X4 EcoDiesel', 'Grand Cherokee 4X4 SRT', 'Grand Cherokee 4X4 Trackhawk', 
    'Renegade', 'Renegade 4X4', 'Renegade 4X4 Trailhawk', 'Wrangler JL 4X4', 
    'Wrangler JL Unlimited 4X4', 'Gladiator 4X4', 'Wrangler 4X4', 'Wrangler 4X4 eTorque', 
    'Wrangler Unlimited 4X4', 'Wrangler Unlimited 4X4 eTorque', 'Wrangler Unlimited 4X4 EcoDiesel'


    ], 
    "KIA": [ 

    'CADENZA', 'FORTE', 'FORTE 5', 'FORTE KOUP', 'OPTIMA', 'OPTIMA HYBRID', 'OPTIMA HYBRID EX', 'RIO', 
    'RIO ECO', 'RONDO', 'SEDONA', 'SORENTO', 'SORENTO 4WD', 'SOUL', 'SOUL ECO Dynamics', 'SPORTAGE', 
    'SPORTAGE AWD', 'K900', 'SEDONA SX', 'SEDONA SXL', 'SORENTO AWD', 'SOUL ECO DYNAMICS', 'FORTE (MPI)', 
    'FORTE (GDI)', 'NIRO', 'NIRO FE', 'NIRO TOURING', 'OPTIMA FE', 'OPTIMA TURBO', 'SORENTO AWD FE', 
    'SOUL TURBO', 'STINGER AWD', 'Cadenza', 'Forte', 'Niro', 'Niro FE', 'Niro Touring', 'Optima', 
    'Optima Hybrid', 'Rio', 'Sedona', 'Sorento', 'Sorento AWD', 'Soul', 'Sportage', 'Sportage AWD', 
    'Stinger AWD', 'Forte 5', 'Telluride AWD'


    ], 
    "LAMBORGHINI": [ 

    'AVENTADOR COUPE', 'GALLARDO COUPE', 'AVENTADOR ROADSTER', 'HURACAN', 'VENENO ROADSTER', 
    'HURACAN SPYDER', 'AVENTADOR COUPE LP 740', 'AVENTADOR ROADSTER LP 740', 'AVENTADOR S COUPE', 
    'AVENTADOR S ROADSTER', 'HURACAN AWD', 'HURACAN SPYDER AWD', 'Aventador Coupe', 'Aventador Roadster', 
    'Huracan Coupe', 'Huracan Coupe AWD', 'Huracan Spyder', 'Huracan Spyder AWD', 
    'Huracan Performante Coupe', 'Huracan Performante Spyder', 'Urus'


    ], 
    "LAND ROVER": [ 

    'LR2', 'LR4', 'RANGE ROVER EVOQUE', 'RANGE ROVER EVOQUE COUPE', 'RANGE ROVER LWB V8 5.0 SC', 
    'RANGE ROVER LWB V8 5.0 SC FFV', 'RANGE ROVER SPORT V6 3.0 SC', 'RANGE ROVER SPORT V6 3.0 SC FFV', 
    'RANGE ROVER SPORT V8 5.0 SC', 'RANGE ROVER SPORT V8 5.0 SC FFV', 'RANGE ROVER V6 3.0 SC', 
    'RANGE ROVER V6 3.0 SC FFV', 'RANGE ROVER V8 5.0 SC', 'RANGE ROVER V8 5.0 SC FFV', 
    'RANGE ROVER', 'RANGE ROVER SUPERCHARGED', 'RANGE ROVER SUPERCHARGED LWB', 'RANGE ROVER SPORT', 
    'RANGE ROVER SPORT SUPERCHARGED', 'DISCOVERY SPORT', 'RANGE ROVER TD6 DIESEL', 
    'RANGE ROVER SPORT TD6 DIESEL', 'RANGE ROVER EVOQUE CONVERTIBLE', 'RANGE ROVER VELAR', 'Discovery', 
    'Discovery TD6 Diesel', 'Discovery Sport', 'Range Rover 3.0', 'Range Rover TD6 Diesel', 
    'Range Rover 5.0 Supercharged', 'Range Rover SVAutobiography LWB', 'Range Rover Sport 3.0', 
    'Range Rover Sport TD6 Diesel', 'Range Rover Sport Supercharged', 'Range Rover Evoque', 
    'Range Rover Evoque Convertible', 'Range Rover Velar D180', 'Range Rover Velar P300', 
    'Range Rover Velar P380', 'Discovery Sport P250', 'Discovery Sport P290', 
    'Range Rover 5.0 Supercharged LWB', 'Range Rover SVAutobiography Dynamic', 
    'Range Rover Sport SVR', 'Range Rover Evoque P250', 'Range Rover Evoque P300', 
    'Range Rover Velar P250', 'Range Rover Velar P340', 'Range Rover Velar SVAutobiography Dynamic'


    ], 
    "LEXUS": [ 

    'CT 200h', 'ES 300h', 'ES 350', 'GS 350', 'GS 350 AWD', 'GS 450h', 'GX 460', 'IS 250', 'IS 250 AWD', 
    'IS 250 C', 'IS 350', 'IS 350 AWD', 'IS 350 C', 'IS F', 'LS 460', 'LS 460 AWD', 'LS 460 L AWD', 
    'LS 600h L', 'LX 570', 'RX 350 AWD', 'RX 450h AWD', 'NX 200t AWD', 'NX 200t AWD F SPORT', 
    'NX 300h AWD', 'RC 350', 'RC 350 AWD', 'RC F', 'GS 200t', 'GS 200t F SPORT', 'GS 350 F SPORT', 
    'GS F', 'IS 200t', 'IS 300 AWD', 'RC 200t', 'RC 300 AWD', 'IS 300', 'LC 500', 'LC 500h', 'LS 500', 
    'LS 500 AWD', 'LS 500h', 'LS 500h AWD', 'NX 300 AWD', 'NX 300 AWD F SPORT', 'RX 350 L AWD', 
    'ES 350 F SPORT', 'RX 450h L AWD', 'UX 200', 'UX 250h', 'UX 250h AWD'


    ], 
    "LINCOLN": [ 

    'MKS AWD', 'MKT AWD', 'MKT LIVERY', 'MKT LIVERY AWD', 'MKX AWD', 'MKZ', 'MKZ AWD', 'MKZ HYBRID', 
    'NAVIGATOR 4X4 FFV', 'MKC AWD', 'NAVIGATOR 4X4', 'NAVIGATOR L 4X4', 'CONTINENTAL AWD', 
    'MKC AWD (Start/Stop)', 'Continental AWD', 'MKT Livery AWD', 'MKZ Hybrid', 'Nautilus', 
    'Navigator 4X4', 'Aviator', 'Corsair AWD', 'Nautilus AWD'


    ], 
    "MASERATI": [ 

    'GHIBLI', 'GHIBLI AWD', 'GRANTURISMO', 'GRANTURISMO CONVERTIBLE', 'QUATTROPORTE GTS', 
    'QUATTROPORTE SQ4', 'GHIBLI S', 'GHIBLI SQ4', 'QUATTROPORTE S', 'LEVANTE', 'LEVANTE S', 
    'Ghibli', 'Ghibli S', 'Ghibli SQ4', 'GranTurismo Convertible', 'Levante', 'Levante S', 
    'Levante GTS', 'Levante Trofeo', 'Quattroporte S', 'Quattroporte SQ4', 'Quattroporte GTS', 
    'Ghibli S Q4', 'Quattroporte S Q4'


    ], 
    "MAZDA": [ 

    'CX-5', 'CX-5 4WD', 'CX-9', 'CX-9 4WD', 'MAZDA2', 'MAZDA3 4-DOOR', 'MAZDA3 4-DOOR (i-ELOOP)', 
    'MAZDA3 4-DOOR (SIL)', 'MAZDA3 5-DOOR', 'MAZDA3 5-DOOR (i-ELOOP)', 'MAZDA3 5-DOOR (SIL)', 
    'MAZDA5', 'MAZDA6', 'MAZDA6 (i-ELOOP)', 'MX-5', 'CX-3', 'CX-3 4WD', 'CX-5 (SIL)', 'MAZDA6 (SIL)', 
    'MX-5 (SIL)', 'CX-5 ', 'CX-5 (Cylinder Deactivation)', 'CX-5 4WD (Cylinder Deactivation)', 
    'MAZDA6 TURBO', 'CX-5 Turbo 4WD', 'CX-5 Diesel 4WD', 'Mazda3 4-Door', 'Mazda3 4-Door (SIL)', 
    'Mazda3 4-Door (Cylinder Deactivation)', 'Mazda3 4-Door 4WD', 'Mazda3 5-Door', 'Mazda3 5-Door (SIL)', 
    'Mazda3 5-Door 4WD', 'Mazda6', 'Mazda6 Turbo', 'CX-3 (SIL)', 'CX-30', 'CX-30 4WD', 
    'CX-30 4WD (Cylinder Deactivation)'


    ], 
    "MERCEDES-BENZ": [ 

    'B 250', 'C 250', 'C 250 COUPE', 'C 300 4MATIC FFV', 'C 350', 'C 350 4MATIC', 'C 350 4MATIC COUPE', 
    'C 350 COUPE', 'C 63 AMG', 'C 63 AMG COUPE', 'CL 550 4MATIC', 'CL 63 AMG', 'CLA 250', 
    'CLA 45 AMG 4MATIC', 'CLS 550 4MATIC', 'CLS 63 AMG 4MATIC', 'CLS 63 AMG S 4MATIC', 
    'E 250 BLUETEC 4MATIC', 'E 300 4MATIC', 'E 350 4MATIC', 'E 350 4MATIC COUPE', 
    'E 350 4MATIC WAGON', 'E 350 CABRIOLET', 'E 350 COUPE', 'E 400 HYBRID', 'E 550 4MATIC', 
    'E 550 CABRIOLET', 'E 550 COUPE', 'E 63 AMG 4MATIC', 'E 63 AMG 4MATIC WAGON', 
    'E 63 AMG S 4MATIC', 'E 63 AMG S 4MATIC WAGON', 'G 550', 'G 63 AMG', 'GL 350 BLUETEC 4MATIC', 
    'GL 450 4MATIC', 'GL 550 4MATIC', 'GL 63 AMG', 'GLK 250 BLUETEC 4MATIC', 'GLK 350 4MATIC', 
    'ML 350 4MATIC FFV', 'ML 350 BLUETEC 4MATIC', 'ML 550 4MATIC', 'ML 63 AMG 4MATIC', 
    'S 550 4MATIC LWB', 'S 550 4MATIC SWB', 'S 63 AMG 4MATIC', 'SL 550', 'SL 63 AMG', 
    'SL 65 AMG', 'SLK 250', 'SLK 350', 'SLK 55 AMG', 'SLS AMG BLACK SERIES COUPE', 'SLS AMG GT COUPE', 
    'SLS AMG ROADSTER', 'B 250 4MATIC', 'C 300 4MATIC', 'C 400 4MATIC', 'CLA 250 4MATIC', 
    'CLA 45 AMG', 'CLS 400 4MATIC', 'E 400 4MATIC', 'E 400 4MATIC WAGON', 'E 400 CABRIOLET', 
    'E 400 COUPE', 'GLA 250 4MATIC', 'GLA 45 AMG 4MATIC', 'ML 400 4MATIC', 'S 400 4MATIC', 
    'S 550 4MATIC COUPE', 'S 600', 'S 63 AMG COUPE', 'S 65 AMG', 'S 65 AMG COUPE', 
    'SLS AMG GT ROADSTER', 'AMG C 63', 'AMG C 63 S', 'AMG CLA 45', 'AMG CLS 63 S 4MATIC', 
    'AMG E 63 S 4MATIC', 'AMG E 63 S 4MATIC WAGON', 'AMG G 63', 'AMG G 65', 'AMG GL 63 S', 
    'AMG GLA 45', 'AMG GLE 63 S 4MATIC', 'AMG GLE 63 S COUPE 4MATIC', 'AMG GT S', 'AMG S 63', 
    'AMG S 63 COUPE', 'AMG S 65', 'AMG S 65 COUPE', 'AMG SL 63', 'AMG SL 65', 'AMG SLK 55', 
    'C 450 AMG SPORT 4MATIC', 'CLA 250 4MATIC FFV', 'E 400 4MATIC COUPE', 'GLE 350d 4MATIC', 
    'GLE 350d 4MATIC COUPE', 'GLE 400 4MATIC', 'GLE 450 AMG SPORT 4MATIC COUPE', 'GLE 550 4MATIC', 
    'MAYBACH S 600', 'METRIS CARGO', 'METRIS PASSENGER', 'S 400 4MATIC SWB', 'SLK 300', 
    'AMG C 63 CABRIOLET', 'AMG C 63 COUPE', 'AMG C 63 S CABRIOLET', 'AMG C 63 S COUPE', 
    'AMG GLA 45 4MATIC', 'AMG GLC 43 4MATIC COUPE', 'AMG GLE 43 4MATIC', 'AMG GLE 43 4MATIC COUPE', 
    'AMG GLE 63 S 4MATIC COUPE', 'AMG GLS 63', 'AMG GT COUPE', 'AMG GT S COUPE', 'AMG S 63 4MATIC', 
    'AMG S 63 CABRIOLET', 'AMG S 65 CABRIOLET', 'AMG SLC 43', 'C 300 4MATIC CABRIOLET', 
    'C 300 4MATIC COUPE', 'GLC 300 4MATIC', 'GLS 450 4MATIC', 'GLS 550 4MATIC', 
    'S 550 4MATIC CABRIOLET', 'SL 450', 'SLC 300', 'AMG C 43 4MATIC', 'AMG C 43 4MATIC CABRIOLET', 
    'AMG C 43 4MATIC COUPE', 'AMG CLA 45 4MATIC', 'AMG E 43 4MATIC', 'AMG GLC 43 4MATIC', 
    'AMG GLS 63 4MATIC', 'AMG GT ROADSTER', 'AMG GT C COUPE', 'AMG GT C ROADSTER', 'AMG GT R COUPE', 
    'AMG S 63 4MATIC CABRIOLET', 'AMG S 63 4MATIC COUPE', 'C 300 4MATIC WAGON', 
    'E 400 4MATIC CABRIOLET', 'GLC 300 4MATIC COUPE', 'MAYBACH S 650', 'S 450 4MATIC SWB', 
    'S 560 CABRIOLET', 'S 560 4MATIC', 'S 560 4MATIC SWB', 'S 560 4MATIC COUPE', 'A 220', 
    'A 220 4MATIC', 'A 250', 'A 250 4MATIC', 'AMG C 43 4MATIC Cabriolet', 'AMG C 43 4MATIC Coupe', 
    'AMG C 43 4MATIC Wagon', 'AMG C 63 S Cabriolet', 'AMG C 63 S Coupe', 'AMG CLS 53 4MATIC+', 
    'AMG E 53 4MATIC+', 'AMG E 53 4MATIC+ Cabriolet', 'AMG E 53 4MATIC+ Coupe', 
    'AMG E 53 4MATIC+ Wagon', 'AMG E 63 S 4MATIC+', 'AMG E 63 S 4MATIC+ Wagon', 
    'AMG GLC 43 4MATIC Coupe', 'AMG GLC 63 S 4MATIC+', 'AMG GLC 63 S 4MATIC+ Coupe', 
    'AMG GLE 43 4MATIC Coupe', 'AMG GLE 63 S 4MATIC Coupe', 'AMG GT 53 4MATIC+ Coupe', 
    'AMG GT 63 4MATIC+ Coupe', 'AMG GT 63 S 4MATIC+ Coupe', 'AMG GT C Coupe', 
    'AMG GT C Roadster', 'AMG GT R Coupe', 'AMG S 63 4MATIC+', 'AMG S 63 4MATIC+ Cabriolet', 
    'AMG S 63 4MATIC+ Coupe', 'AMG S 65 Cabriolet', 'AMG S 65 Coupe', 
    'C 300 4MATIC Cabriolet', 'C 300 4MATIC Coupe', 'C 300 4MATIC Wagon', 'CLS 450 4MATIC', 
    'E 450 4MATIC', 'E 450 4MATIC Cabriolet', 'E 450 4MATIC Coupe', 'E 450 4MATIC Wagon', 
    'GLC 300 4MATIC Coupe', 'Maybach S 560 4MATIC', 'Maybach S 650', 'Metris Cargo', 
    'Metris Cargo LWB', 'Metris Passenger', 'S 560 Cabriolet'


    ], 
    "MINI": [ 

    'COOPER CLUBMAN', 'COOPER CONVERTIBLE', 'COOPER COUNTRYMAN', 'COOPER COUPE', 'COOPER PACEMAN', 
    'COOPER ROADSTER', 'COOPER S CLUBMAN', 'COOPER S CONVERTIBLE', 'COOPER S COUNTRYMAN ALL4', 
    'COOPER S COUPE', 'COOPER S PACEMAN ALL4', 'COOPER S ROADSTER', 'JOHN COOPER WORKS CLUBMAN', 
    'JOHN COOPER WORKS CONVERTIBLE', 'JOHN COOPER WORKS COUNTRYMAN ALL4', 'JOHN COOPER WORKS COUPE', 
    'JOHN COOPER WORKS PACEMAN ALL4', 'JOHN COOPER WORKS ROADSTER', 'COOPER 3 DOOR', 'COOPER 5 DOOR', 
    'COOPER S 3 DOOR', 'COOPER S 5 DOOR', 'JOHN COOPER WORKS', 'COOPER CLUBMAN ALL4', 
    'COOPER COUNTRYMAN ALL4', 'COOPER S CLUBMAN ALL4', 'COOPER S COUNTRYMAN  ALL4', 
    'JOHN COOPER WORKS 3 DOOR', 'JOHN COOPER WORKS CLUBMAN ALL4', 'Cooper 3 Door', 'Cooper 5 Door', 
    'Cooper Clubman ALL4', 'Cooper Convertible', 'Cooper Countryman ALL4', 'Cooper S 3 Door', 
    'Cooper S 5 Door', 'Cooper S Clubman ALL4', 'Cooper S Convertible', 'Cooper S Countryman ALL4', 
    'John Cooper Works 3 Door', 'John Cooper Works Clubman ALL4', 'John Cooper Works Convertible', 
    'John Cooper Works Countryman ALL4'


    ],
    "MITSUBISHI": [ 

    'LANCER', 'LANCER AWD', 'LANCER EVOLUTION', 'LANCER RALLIART', 'LANCER SPORTBACK', 'MIRAGE', 
    'OUTLANDER', 'OUTLANDER 4WD', 'RVR', 'RVR 4WD', 'LANCER 4WD', 'MIRAGE G4', 'ECLIPSE CROSS', 
    'ECLIPSE CROSS 4WD', 'Eclipse Cross 4WD', 'Mirage', 'Mirage G4', 'Outlander 4WD'


    ], 
    "NISSAN": [ 

    '370Z', '370Z ROADSTER', 'ALTIMA', 'ARMADA 4WD', 'FRONTIER', 'FRONTIER 4WD', 'GT-R', 'JUKE', 
    'JUKE AWD', 'MAXIMA', 'MURANO AWD', 'NV200 CARGO VAN', 'PATHFINDER', 'PATHFINDER 4WD', 
    'PATHFINDER HYBRID 4WD', 'QUEST', 'ROGUE', 'ROGUE AWD', 'SENTRA', 'TITAN', 'TITAN 4WD', 
    'VERSA', 'XTERRA 4WD', '370Z COUPE', 'JUKE NISMO RS', 'JUKE NISMO RS AWD', 'MICRA', 'MURANO', 
    'PATHFINDER 4WD PLATINUM', 'ALTIMA 3.5', 'ALTIMA SR', 'QASHQAI', 'QASHQAI AWD', 
    'SENTRA (Turbo)', 'SENTRA NISMO', 'TITAN 4WD PRO-4X', 'KICKS', '370Z Roadster', 'Altima', 
    'Altima SR/Platinum', 'Altima AWD', 'Altima AWD SR/Platinum', 'Armada 4WD', 
    'Frontier', 'Frontier 4WD', 'Kicks', 'Maxima', 'Micra', 'Murano', 'Murano AWD', 'NV200 Cargo Van', 
    'Pathfinder', 'Pathfinder 4WD', 'Pathfinder 4WD Platinum', 'Qashqai', 'Qashqai AWD', 
    'Rogue', 'Rogue AWD', 'Sentra', 'Sentra (Turbo)', 'Sentra Nismo', 'Titan', 'Titan 4WD', 
    'Titan 4WD Pro-4X', 'Versa', 'Sentra SR'


    ], 
    "PORSCHE": [ 

    '911 CARRERA', '911 CARRERA 4', '911 CARRERA 4 CABRIOLET', '911 CARRERA 4S', 
    '911 CARRERA 4S CABRIOLET', '911 CARRERA CABRIOLET', '911 CARRERA S', 
    '911 CARRERA S CABRIOLET', '911 GT3', '911 TURBO', '911 TURBO CABRIOLET', 
    '911 TURBO S', '911 TURBO S CABRIOLET', 'BOXSTER', 'BOXSTER S', 'CAYENNE', 
    'CAYENNE DIESEL (modified)', 'CAYENNE GTS', 'CAYENNE S', 'CAYENNE S HYBRID', 
    'CAYENNE TURBO', 'CAYENNE TURBO S', 'CAYMAN', 'CAYMAN S', 'PANAMERA', 
    'PANAMERA 4', 'PANAMERA 4S', 'PANAMERA 4S EXECUTIVE', 'PANAMERA GTS', 
    'PANAMERA S', 'PANAMERA TURBO', 'PANAMERA TURBO EXECUTIVE', 
    '911 CARRERA 4 GTS', '911 CARRERA 4 GTS CABRIOLET', '911 CARRERA GTS', 
    '911 CARRERA GTS CABRIOLET', '911 TARGA 4', '911 TARGA 4S', 'BOXSTER GTS', 
    'CAYMAN GTS', 'MACAN S', 'MACAN TURBO', 'PANAMERA TURBO S', 'PANAMERA TURBO S EXECUTIVE', 
    '911 GT3RS', 'BOXSTER SPYDER', 'CAYMAN GT4', 'CAYENNE PLATINUM', 'MACAN', 'MACAN GTS', 
    '911 TARGA 4 GTS', '911 TURBO S EXCLUSIVE', 'MACAN TURBO KIT', 'PANAMERA 4 EXECUTIVE', 
    'PANAMERA 4 ST', 'PANAMERA 4S ST', 'PANAMERA TURBO ST', '911 Carrera', 
    '911 Carrera Cabriolet', '911 Carrera GTS', '911 Carrera GTS Cabriolet', 
    '911 Carrera S', '911 Carrera S Cabriolet', '911 Carrera T', '911 Carrera 4', 
    '911 Carrera 4 Cabriolet', '911 Carrera 4 GTS', '911 Carrera 4 GTS Cabriolet', 
    '911 Carrera 4S', '911 Carrera 4S Cabriolet', '911 GT2 RS', '911 GT3 RS', 
    '911 GT3 Touring', '911 Speedster', '911 Targa 4', '911 Targa 4 GTS', 
    '911 Targa 4S', '911 Turbo', '911 Turbo Cabriolet', '911 Turbo S', 
    '911 Turbo S Cabriolet', '911 Turbo S Exclusive Cabriolet', 'Boxster', 
    'Boxster GTS', 'Boxster S', 'Cayenne', 'Cayenne S', 'Cayenne Turbo', 
    'Cayman', 'Cayman GTS', 'Cayman S', 'Macan', 'Macan S', 'Panamera', 
    'Panamera 4', 'Panamera 4 Executive', 'Panamera 4 ST', 'Panamera 4S', 
    'Panamera 4S Executive', 'Panamera 4S ST', 'Panamera GTS', 'Panamera GTS ST', 
    'Panamera Turbo', 'Panamera Turbo Executive', 'Panamera Turbo ST'


    ], 
    "RAM": [ 

    '1500 (MDS)', '1500 4X4 (MDS)', '1500 4X4 DIESEL', '1500 4X4 FFV', '1500 DIESEL', '1500 FFV', 
    '1500 HFE', 'CARGO VAN FFV', '1500', '1500 ECODIESEL', '1500 ECODIESEL HFE', '1500 4X4', 
    '1500 4X4 ECODIESEL', 'PROMASTER CITY', '1500 eTorque', '1500 HFE eTorque', '1500 4X4 eTorque', 
    '1500 Classic EcoDiesel', '1500 Classic FFV', '1500 Classic', '1500 Classic 4X4 EcoDiesel', 
    '1500 Classic 4X4 FFV', '1500 Classic 4X4', 'ProMaster City', '1500 EcoDiesel', '1500 4X4 EcoDiesel'


    ], 
    "ROLLS-ROYCE": [ 

    'GHOST', 'GHOST EWB', 'PHANTOM', 'PHANTOM COUPE', 'PHANTOM DROPHEAD COUPE', 'PHANTOM EWB', 
    'WRAITH', 'DAWN', 'Cullinan', 'Dawn', 'Ghost', 'Ghost EWB', 'Phantom', 'Phantom EWB', 
    'Wraith', 'Cullinan Black Badge'


    ], 
    "SCION": [ 

    'FR-S', 'iQ', 'tC', 'xB', 'xD', 'iM'


    ], 
    "SMART": [ 

    'FORTWO CABRIOLET', 'FORTWO COUPE'


    ], 
    "SRT": [ 

    'VIPER COUPE', 'VIPER GTS COUPE'


    ], 
    "SUBARU": [ 

    'BRZ', 'FORESTER AWD', 'IMPREZA AWD', 'IMPREZA WAGON AWD', 'LEGACY AWD', 'OUTBACK AWD', 
    'TRIBECA AWD', 'XV CROSSTREK AWD', 'XV CROSSTREK HYBRID AWD', 'WRX', 'CROSSTREK AWD', 
    'IMPREZA 4-DOOR AWD', 'IMPREZA 5-DOOR AWD', 'WRX AWD', 'BRZ tS', 'WRX STI AWD', 
    'WRX STI AWD TYPE RA', 'Ascent AWD', 'Crosstrek AWD', 'Forester AWD', 
    'Impreza 4-Door AWD', 'Impreza 5-Door AWD', 'Legacy AWD', 'Outback AWD'


    ], 
    "TOYOTA": [ 

    '4RUNNER (Part-Time 4WD)', '4RUNNER 4WD', 'AVALON', 'CAMRY', 
    'CAMRY HYBRID LE', 'CAMRY HYBRID XLE/SE', 'COROLLA', 'COROLLA LE ECO (1-mode)', 
    'COROLLA LE ECO (2-mode)', 'COROLLA MATRIX', 'FJ CRUISER 4WD', 'HIGHLANDER', 
    'HIGHLANDER AWD', 'HIGHLANDER HYBRID AWD', 'HIGHLANDER HYBRID AWD LE', 
    'PRIUS', 'PRIUS c', 'PRIUS v', 'RAV4', 'RAV4 AWD', 'RAV4 LIMITED AWD', 
    'SEQUOIA 4WD', 'SIENNA', 'SIENNA AWD', 'TACOMA', 'TACOMA 4WD', 'TUNDRA', 
    'TUNDRA 4WD', 'VENZA', 'VENZA 4WD', 'YARIS', '4RUNNER 4WD (Part-Time 4WD)', 
    'RAV4 LE/XLE', 'RAV4 HYBRID AWD', 'RAV4 LIMITED/SE AWD', 'TACOMA 4WD D-CAB OFF-ROAD', 
    'YARIS (SIL)', 'YARIS HATCHBACK', '86', 'COROLLA iM', 'HIGHLANDER AWD (Start/Stop System)', 
    'HIGHLANDER AWD LE', 'CAMRY LE/SE', 'CAMRY XLE/XSE', 'CAMRY XSE', 'C-HR', '4Runner 4WD', 
    '4Runner 4WD (Part-Time 4WD)', 'Avalon', 'Camry', 'Camry LE/SE', 'Camry XLE/XSE', 'Camry XSE', 
    'Camry Hybrid LE', 'Camry Hybrid XLE/SE', 'Corolla', 'Corolla LE Eco', 'Corolla Hatchback', 
    'Highlander', 'Highlander AWD', 'Highlander AWD (Start/Stop System)', 'Highlander AWD LE', 
    'Highlander Hybrid AWD', 'Prius', 'Prius AWD', 'Prius c', 'RAV4 Hybrid AWD', 'Sequoia 4WD', 
    'Sienna', 'Sienna AWD', 'Tacoma', 'Tacoma 4WD', 'Tacoma 4WD D-Cab Off-Road', 'Tundra', 
    'Tundra 4WD', 'Yaris', 'Yaris (SIL)', 'Yaris Hatchback', 'Camry TRD', 'Camry AWD LE/SE', 
    'Camry AWD XLE/XSE', 'Corolla XLE', 'Corolla XSE', 'Corolla Hybrid', 'GR Supra', 
    'Highlander Hybrid AWD Limited/Platinum', 'RAV4 AWD TRD Off-Road', 'Tacoma 4WD D-Cab TRD Off-Road/Pro'


    ], 
    "VOLKSWAGEN": [ 

    'BEETLE', 'BEETLE TDI (modified)', 'BEETLE CONVERTIBLE', 'CC', 'CC 4MOTION', 'EOS', 'GOLF WAGON', 
    'GOLF WAGON TDI (modified)', 'JETTA', 'JETTA TDI (modified)', 'JETTA GLI', 'JETTA TURBO HYBRID', 
    'PASSAT', 'PASSAT TDI (modified)', 'ROUTAN', 'TIGUAN', 'TIGUAN 4MOTION', 'TOUAREG', 
    'TOUAREG TDI (modified)', 'GOLF', 'GOLF TDI (modified)', 'GOLF GTI', 'GOLF SPORTWAGON', 
    'GOLF SPORTWAGON TDI (modified)', 'JETTA HYBRID', 'BEETLE DUNE', 'GOLF R', 'GOLF ALLTRACK', 
    'GOLF SPORTWAGEN', 'GOLF SPORTWAGEN 4MOTION', 'ATLAS', 'ATLAS 4MOTION', 'BEETLE DUNE CONVERTIBLE', 
    'Arteon 4MOTION', 'Atlas', 'Atlas 4MOTION', 'Beetle', 'Beetle Convertible', 'Beetle Dune', 
    'Beetle Dune Convertible', 'Golf', 'Golf GTI', 'Golf R', 'Golf Alltrack', 'Golf SportWagen', 
    'Golf SportWagen 4MOTION', 'Jetta', 'Jetta GLI', 'Passat', 'Tiguan', 'Tiguan 4MOTION', 
    'Atlas Cross Sport 4MOTION'


    ], 
    "VOLVO": [ 

    'S60', 'S60 AWD', 'S80', 'S80 AWD', 'XC60', 'XC60 AWD', 'XC70 AWD', 'XC90 AWD', 
    'S60 POLESTAR AWD', 'S60 T5 ', 'S60 T5 AWD', 'S60 T6   ', 'S60 T6 AWD', 'S80 T5', 'S80 T6 AWD', 
    'V60 CC', 'V60 CC AWD', 'V60 POLESTAR AWD', 'V60 T5', 'V60 T5 AWD', 'V60 T6 AWD', 'XC60 3.2 AWD', 
    'XC60 T5', 'XC60 T5 AWD', 'XC60 T6  ', 'XC60 T6 AWD', 'XC70 3.2 AWD', 'XC70 T5', 'XC70 T6 AWD', 
    'S60 CC T5 AWD', 'S60 INSCRIPTION', 'S60 INSCRIPTION T5 AWD', 'S60 T5', 'S60 T6', 'S60 3.0T AWD', 
    'S60 POLESTAR', 'V60 CC T5 AWD', 'V60 3.0T AWD', 'V60 POLESTAR', 'XC60 T6', 'XC60 3.0T AWD', 
    'XC70 T5 AWD', 'XC90 T5', 'XC90 T5 AWD', 'XC90 T6 AWD', 'S60 INSCRIPTION T5', 'S90 T5', 
    'S90 T6 AWD', 'V90 T5', 'V90 T6 AWD', 'V90 CC T6 AWD', 'S90 T5 AWD', 'V90 CC T5 AWD', 'XC40 T5 AWD', 
    'XC40 T4 AWD'


    ], 
    "GENESIS": [ 

    'G80 AWD', 'G90 AWD', 'G70', 'G70 AWD'


    ],
    "BUGATTI": [ 

    'CHIRON', 'Chiron'
    ]

}

with open("car_data.json", "w") as file:
    json.dump(car_data, file)
