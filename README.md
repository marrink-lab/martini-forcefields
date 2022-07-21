# Martini Force Fields

[![DOI:10.1038/s41592-021-01098-3](https://zenodo.org/badge/DOI/10.1038/s41592-021-01098-3.svg)](https://doi.org/10.1038/s41592-021-01098-3)

## Summary

This repository contains parameters of the Martini force field for version 3 and higher, released by the Marrink lab and collaborators. 
Details on parametrization of the bead-bead interactions and rules for creating new molecules can be found in the [recent publication](https://doi.org/10.1038/s41592-021-01098-3). 
The files, which contain the interaction and molecule definitions, are in GROMACS [itp/top format](https://manual.gromacs.org/current/reference-manual/topologies/topology-file-formats.html).In addition, files [in vermouth-format](https://vermouth-martinize.readthedocs.io/en/latest/file_formats.html)
are present, which can be used by programs such as martinize2 or polyply. Such files store the definitions of the protein model
for example. In the future this repsoitory will expose python entry points for reading in and handling datafiles, both itp and ff with the vermouth
python library. The python aspect of this package is currently under construction.

Force field interaction parameters are defined by the major releases (i.e. `v3.X.Y`) and follow a versioning scheme, which defines 
compatibility, as outlined below. Molecule parameters are defined by the major release and a single version indicator 
(e.g. `martini_v3.0.0_ions_v1`). Different versions typically refer to more refined models, where mapping, bead assigment or bonded 
interactions were updated.

To cite the Martini3 line of force fields (`v3.X.Y`) please use [this citation](https://doi.org/10.1038/s41592-021-01098-3). Please note 
that molecule parameters have been optimized in separate publications by great efforts of many people. To give appropriate credit, please
also cite the applicable publications for the molecules you used (see Table below).

## General versioning guidelines

Force fields moving forward will be called `martini_vX.Y.Z`

* `X` denotes some major change in bead-bead interaction levels and parametrization strategy
* `Y` denotes some changes in the interaction levels between beads
* `Z` is a bug fix version -- e.g. something we've caught and corrected.

Molecule .itp file definitions moving forward will be called `martini_vX.Y.Z_molecule_v.Q.itp`
All molecules are associated with a particular force field version they are compatible with.

* `molecule` denotes a particular class of molecules (e.g. ions, sugars, etc.)
* `Q` indicates different versions of molecule parameters in terms of mapping, bonded interactions, or bead assigment
  `Q` increases with the new parameters but does not get reset when changeing the minor version

Vermouth ff file definitions moving forward will be stored in a directory named `martiniXYZV`

* `moleculeXYZ` referes to the major version the ff-files are compatible with
* `V` denotes changes made in the input files, similar to Q in the molecule files

## References
A collection of references for specific and general molecule parameters for the Martini force-field. 

| Filename | Paper | Major Version | Release Date | Comments |
| -------- | --- | -------- | --- | --- |
| `martini_v3.X.Y` | [DOI](https://doi.org/10.1038/s41592-021-01098-3) | 3 | March 29th, 2021 | version 3 interaction parameters |
| `martini_v3.X.Y_small_molecules_v1.itp` | [DOI](https://doi.org/10.1002/adts.202100391) | 3 | December 30th, 2021 | additional molecules & validation |
| `martini_v3.X.Y_sugars_v2.itp` | submitted | 3 | XXXXX | imporved sugar parameters & additional molecules |

