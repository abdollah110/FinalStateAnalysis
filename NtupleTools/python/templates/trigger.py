'''

Ntuple branch template sets for trigger selections

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

IMPORTANT NOTE: If you want the logical OR of several paths, separate them 
by '|' rather than by ','. 
(When the Smart Trigger gets a group of paths separated by commas, it uses 
the one with the lowest prescale (taking the first in case of a tie).

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

_trig_template = PSet(
    namePass = 'evt.hltResult("paths")',
    nameGroup = 'evt.hltGroup("paths")',
    namePrescale = 'evt.hltPrescale("paths")',
)

singleLepton_25ns_MC = PSet(
    _trig_template.replace(
        name='IsoMu20',
        paths=r'HLT_IsoMu20_v\\d+'
        ),
    _trig_template.replace(
        name='IsoMu27',
        paths=r'HLT_IsoMu27_v\\d+'
        ),
    )

singleLepton_25ns = PSet(
        _trig_template.replace(
        name='IsoMu20',
        paths=r'HLT_IsoMu20_v\\d+'
        ),
    _trig_template.replace(
        name='IsoMu27',
        paths=r'HLT_IsoMu27_v\\d+'
        ),
    )

doubleLepton_25ns = PSet(
    _trig_template.replace(
        name='doubleMu',
        paths=r'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v\\d+|HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='doubleE_23_12',
        paths=r'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24Tau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20Tau27',
        paths=r'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1__v\\d+'
        ),
    )

tripleLepton = PSet(
    _trig_template.replace(
        name='tripleE',
        paths=r'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v\\d+'
        ),
    _trig_template.replace(
        name='tripleMu12_10_5',
        paths=r'HLT_TripleMu_12_10_5_v\\d+'
        ),
    )

