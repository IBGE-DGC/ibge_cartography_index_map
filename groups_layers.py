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
                "Ortomosaico 1 _ 100 000",
                "Ortomosaico 1 _ 25 000"
            ],
            "Cartas Imagem": [
                "Carta Imagem 1 _ 100 000",
                "Carta Imagem 1 _ 25 000"            
            ],
            "Mapas Imagem": [
                "Mapa Imagem"
            ]
        }   
    },
    "Modelos Digitais de Superfícies": {
        "Modelo Digital de Elevação - MDE": [
            "Modelos Digitais de Elevação em ASCII",
            "Modelos Digitais de Elevação em TIFF"        
        ]
    },
    "Cartas e Mapas": {
        "Bases Cartográficas Contínuas" : [
            "Base Cartográfica Contínua da Amazônia Legal 1 _ 100 000",
            "Base Contínua Vetorial 1 _ 1 000 000 Versão 2010",
            "Base Contínua Vetorial 1 _ 1 000 000 Versão 2014",
            "Base Contínua Vetorial 1 _ 1 000 000 Versão 2016",
            "Base Contínua Vetorial 1 _ 100 000 Versão 2016",
            "Base Contínua Vetorial 1 _ 100 000 Versão 2018",
            "Base Contínua Vetorial 1 _ 100 000 Versão 2020",
            "Base Contínua Vetorial 1 _ 25 000 Versão 2016",
            "Base Contínua Vetorial 1 _ 25 000 Versão 2018",
            "Base Contínua Vetorial 1 _ 25 000 Versão 2020",
            "Base Contínua Vetorial 1 _ 250 000 Versão 2013",
            "Base Contínua Vetorial 1 _ 250 000 Versão 2015",
            "Base Contínua Vetorial 1 _ 250 000 Versão 2017",
            "Base Contínua Vetorial 1 _ 250 000 Versão 2019",
            "Base Contínua Vetorial do Estado de Roraima 1 _ 100 000"        
        ],
        "Folhas Topográficas": [
            "Folhas Topográficas 1 _ 1 000 000",
            "Folhas Topográficas 1 _ 100 000",
            "Folhas Topográficas 1 _ 25 000",
            "Folhas Topográficas 1 _ 250 000",
            "Folhas Topográficas 1 _ 50 000",
            "Folhas Topográficas Vetoriais 1 _ 1 000 000",
            "Folhas Topográficas Vetoriais 1 _ 100 000",
            "Folhas Topográficas Vetoriais 1 _ 25 000",
            "Folhas Topográficas Vetoriais 1 _ 250 000",
            "Folhas Topográficas Vetoriais 1 _ 50 000",
            "Fotolitos 1 _ 100 000",
            "Fotolitos 1 _ 25 000",
            "Fotolitos 1 _ 250 000",
            "Fotolitos 1 _ 50 000"        
        ],
        "Mapas do Brasil": {
            "Físico": [
                "Mapa Físico do Brasil 1 _ 2 500 000 Versão 2017",
                "Mapa Físico do Brasil 1 _ 5 000 000 Versão 2007",
                "Mapa Físico do Brasil 1 _ 5 000 000 Versão 2018"            
            ],
            "Político": [
                "Mapa Político do Brasil 1 _ 2 500 000 Versão 2005",
                "Mapa Político do Brasil 1 _ 2 500 000 Versão 2014",
                "Mapa Político do Brasil 1 _ 5 000 000 Versão 2004",
                "Mapa Político do Brasil 1 _ 5 000 000 Versão 2013",
                "Mapa Político do Brasil 1 _ 5 000 000 Versão 2015",
                "Mapa Político do Brasil 1 _ 5 000 000 Versão 2016",
                "Mapa Político do Brasil 1 _ 5 000 000 Versão 2020"            
            ],
            "Sociedade e Economia": [
                "Mapa Temático das Indicações Geográficas Versão 2015",
                "Mapa Temático das Indicações Geográficas Versão 2016",
                "Mapa Temático das Indicações Geográficas Versão 2017",
                "Mapa Temático das Indicações Geográficas Versão 2018",
                "Mapa Temático das Indicações Geográficas Versão 2019"                
            ]
        },
        "Mapas Regionais": {
            "Físico": [
                "Mapas Físicos Regionais  Versão 2013"            
            ],
            "Político": [
                "Mapas Políticos Regionais  Versão 2009",
                "Mapas Políticos Regionais  Versão 2017"
            ]
        },
        "Mapas Estaduais": {
            "Físico": [
                "Mapas Físicos Estaduais"            
            ],
            "Político": [
                "Mapas Políticos Estaduais Versão 2009",
                "Mapas Políticos Estaduais Versão 2015"
            ]            
        }
    }
}'''
    
groups_idxlayers = json.loads(json_groups_idxlayers, strict=False)



