import streamlit as st

"Hello from conda"

b = st.button("Click me")

if b:
  st.balloons()


import py3Dmol
from psikit import Psikit
from rdkit import Chem
pk = Psikit()
pk.read_from_smiles('O')
pk.energy()
pk.create_cube_files(gridspace=0.5)

homo_voldata = open("Psi_a_5_1-A\"_HOMO.cube", "r").read()
lumo_voldata = open("Psi_a_6_5-A\'_LUMO.cube", "r").read()

v = py3Dmol.view()
v.addVolumetricData(homo_voldata, "cube", {'isoval': -0.03, 'color': "red", 'opacity': 0.75})
v.addVolumetricData(homo_voldata, "cube", {'isoval': 0.03, 'color': "blue", 'opacity': 0.75})
v.addModel(Chem.MolToMolBlock(pk.mol), 'mol')
v.setStyle({'stick':{}})
v.zoomTo()
v.show()