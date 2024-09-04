# class dataset

import numpy as np

# class dataset
# In this dataset:
# 4 type of patients and 39 types of cells (specifications, or features)
#
# data has a label group of 4(patients): HC, DC, ARI and RA
#
# raw data has 39 features:
# Treg, Tfr, Tfr Tfh Ratio,
# Th1, Th2, Th17, Tph,
# Th1 Treg Ratio, Treg Th17 Ratio, Th1 Th2 Ratio
# Tfh, Tfh1, Tfh2, Tfh17,
# Tfh17 of parent, Tfh2 of parent, Tfh1 of parent,
# UswM of CD19B cells, SwM of CD19B cells,	DN of CD19B cells,
# Naïve B of CD19B cells, CD19B cells, CD27posCD24hi B10 of CD19B cells,
# CD11c pos of CD19B cells, ASC of CD19B cells, CD24hiCD38hi TrB of CD19B cells,
# DN1 of CD19B cells, DN2 of CD19B cells, CD24hiCD38hi Tr USwM Ratio,
# NonClasMono of parent, InterMono of parent, ClasMono of parent, LDG of CD45,
# CD14 of CD45, M2 of CD45, Dendrite cell of CD45, NonClasMono of CD45,	InterMono of CD45, ClasMono of CD45
#
