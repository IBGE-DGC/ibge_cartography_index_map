# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:50:00 2021

@author: Marcel
"""

import json

json_groups_idxlayers = r'''
{
    "Imagens do Território": {
        "Imagens Corrigidas": {
            "Imagens Ortorretificadas": [
                "Imagens Ortorretificadas"
            ],
            "Ortomosaicos": [
                "Ortomosaicos_100k",
                "Ortomosaicos_25k"
            ],
            "Cartas Imagem": [
                "Cartas Imagem_100k",
                "Cartas Imagem_25k"            
            ],
            "Mapas Imagem": [
                "Mapa Imagem do Distrito Federal_100k"
            ]
        }   
    },
    "Modelos Digitais de Superfícies": {
        "Modelo Digital de Elevação - MDE": [
            "Modelos Digitais de Elevação_ASCII",
            "Modelos Digitais de Elevação_TIFF"        
        ]
    },
    "Cartas e Mapas": {
        "Bases Cartográficas Contínuas" : [
            "Base Cartográfica Contínua da Amazônia Legal_100k_versão_2011",
            "Base Cartográfica Contínua do Brasil_1M_versão_2010",
            "Base Cartográfica Contínua do Brasil_1M_versão_2014",
            "Base Cartográfica Contínua do Brasil_1M_versão_2016",
            "Base Cartográfica Contínua do Brasil_250k_versão_2013",
            "Base Cartográfica Contínua do Brasil_250k_versão_2015",
            "Base Cartográfica Contínua do Brasil_250k_versão_2017",
            "Base Cartográfica Contínua do Brasil_250k_versão_2019",
            "Base Cartográfica Contínua do Estado de GO e do DF_100k_versão_2016",
            "Base Cartográfica Contínua do Estado de RR_100k_versão_2011",
            "Base Cartográfica Contínua do Estado de SC_25k_versão_2020",
            "Base Cartográfica Contínua do Estado de SE_100k_versão_2019",
            "Base Cartográfica Contínua do Estado do ES_100k_versão_2018",
            "Base Cartográfica Contínua do Estado do RJ_25k_versão_2016",
            "Base Cartográfica Contínua do Estado do RJ_25k_versão_2018"   
        ],
        "Folhas Topográficas": [
            "Folhas da Carta Internacional do Mundo ao Milionésimo Editoradas",
            "Folhas da Carta Internacional do Mundo ao Milionésimo Vetoriais",
            "Folhas Topográficas Editoradas_100k",
            "Folhas Topográficas Editoradas_250k",
            "Folhas Topográficas Editoradas_25k",
            "Folhas Topográficas Editoradas_50k",
            "Folhas Topográficas Fotolitos_100k",
            "Folhas Topográficas Fotolitos_250k",
            "Folhas Topográficas Fotolitos_25k",
            "Folhas Topográficas Fotolitos_50k",
            "Folhas Topográficas Vetoriais_100k",
            "Folhas Topográficas Vetoriais_250k",
            "Folhas Topográficas Vetoriais_25k",
            "Folhas Topográficas Vetoriais_50k"     
        ],
        "Mapas do Brasil": {
            "Físico": [
                "Mapa Físico do Brasil_2500k_versão_2017",
                "Mapa Físico do Brasil_5M_versão_2007",
                "Mapa Físico do Brasil_5M_versão_2018"            
            ],
            "Político": [
                "Mapa Político do Brasil_2500k_versão_2005",
                "Mapa Político do Brasil_2500k_versão_2014",
                "Mapa Político do Brasil_5M_versão_2004",
                "Mapa Político do Brasil_5M_versão_2013",
                "Mapa Político do Brasil_5M_versão_2015",
                "Mapa Político do Brasil_5M_versão_2016",
                "Mapa Político do Brasil_5M_versão_2020"            
            ],
            "Sociedade e Economia": [
                "Mapa Temático das Indicações Geográficas do Brasil_versão_2015",
                "Mapa Temático das Indicações Geográficas do Brasil_versão_2016",
                "Mapa Temático das Indicações Geográficas do Brasil_versão_2017",
                "Mapa Temático das Indicações Geográficas do Brasil_versão_2018",
                "Mapa Temático das Indicações Geográficas do Brasil_versão_2019"                
            ]
        },
        "Mapas Regionais": {
            "Físico": [
                "Mapas Físicos Regionais_versão_2013"            
            ],
            "Político": [
                "Mapas Políticos Regionais_versão_2009",
                "Mapas Políticos Regionais_versão_2017"
            ]
        },
        "Mapas Estaduais": {
            "Físico": [
                "Mapas Físicos Estaduais"            
            ],
            "Político": [
                "Mapas Políticos Estaduais_versão_2009",
                "Mapas Políticos Estaduais_versão_2015"
            ]            
        }
    },
    "Informações sobre Organização do Território": {
        "Malhas Territoriais": [
            "Limites das Unidades da Federação_versão_2020"
        ]
    }
}'''
    
groups_idxlayers = json.loads(json_groups_idxlayers, strict=False)



