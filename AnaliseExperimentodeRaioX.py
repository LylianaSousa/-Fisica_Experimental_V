#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:08:10 2022

@author: lyliana
"""
import pandas as pd
import scipy.interpolate

#Dados Molibdênio
dados = pd.read_csv('atenuacaovsenergia.txt', delimiter = "\t")
dadosMO = dados[['u_Mo [cm²/g]', 'Energy_Mo [eV]']].drop_duplicates(subset='Energy_Mo [eV]')

atenuação_Mo = dadosMO['u_Mo [cm²/g]']
energy_Mo = dadosMO['Energy_Mo [eV]']

dadosinterp = pd.read_csv('ernegyabsortancy.txt', delimiter = "\t")
dadosinterpENERGY = dadosinterp[['Energia[eV]']]

new_energy = dadosinterpENERGY['Energia[eV]']
new_atenuação_Mo = scipy.interpolate.interp1d(energy_Mo , atenuação_Mo , kind='cubic')(new_energy)
dadosinterp['Atenuação_Mo'] = new_atenuação_Mo

#Dados Zircônio
dadosZR = dados[['u_Zr[cm²/g]', 'Energy_Zr [eV]']].drop_duplicates(subset='Energy_Zr [eV]')

atenuação_Zr = dadosZR['u_Zr[cm²/g]']
energy_Zr= dadosZR['Energy_Zr [eV]']

new_atenuação_Zr = scipy.interpolate.interp1d(energy_Zr , atenuação_Zr , kind='cubic')(new_energy)
dadosinterp['Atenuação_Zr'] = new_atenuação_Zr

#Dados Prata
dadosAG = dados[['u_Ag [cm²/g]', 'Energy_Ag [eV]']].drop_duplicates(subset='Energy_Ag [eV]')

atenuação_Ag = dadosAG['u_Ag [cm²/g]']
energy_Ag= dadosAG['Energy_Ag [eV]']

new_atenuação_Ag = scipy.interpolate.interp1d(energy_Ag , atenuação_Ag , kind='cubic')(new_energy)
dadosinterp['Atenuação_Ag'] = new_atenuação_Ag

#Dados Alumínio
dadosAL= dados[['u_Al [cm²/g]', 'Energy_Al [eV]']].drop_duplicates(subset='Energy_Al [eV]')

atenuação_Al = dadosAL['u_Al [cm²/g]']
energy_Al= dadosAL['Energy_Al [eV]']

new_atenuação_Al = scipy.interpolate.interp1d(energy_Al , atenuação_Al , kind='cubic')(new_energy)
dadosinterp['Atenuação_Al'] = new_atenuação_Al

print(dadosinterp)

dadosinterp.to_csv(r'dadosinterpolados.txt', header=True, index=None, sep='\t', mode='a')