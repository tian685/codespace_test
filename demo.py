# import torch
# from openchemie import OpenChemIE

# # model = OpenChemIE(device=torch.device('cpu')) # change to cuda for gpu
# model = OpenChemIE()
# pdf_path = 'data_literature/acs.joc.2c00749.pdf'  # Change it to the path of your PDF
# # Figure analysis
# figure_results = model.extract_molecules_from_figures_in_pdf(pdf_path)
# # Text analysis
# text_results = model.extract_molecules_from_text_in_pdf(pdf_path)

import torch
from openchemie import OpenChemIE
import cv2
from PIL import Image

model = OpenChemIE()

img1 = cv2.imread('data_literature/img1.png')
img2 = cv2.imread('data_literature/img2.png')
# img3 = Image.open('example/img3.png')
images = [img1, img2] # supports both cv2 and PIL images

molecule_results = model.extract_molecules_from_figures(images)
# reaction_results = model.extract_reactions_from_figures(images)
# bbox_results = model.extract_molecule_bboxes_from_figures(images)
# coref_results = model.extract_molecule_corefs_from_figures(images)