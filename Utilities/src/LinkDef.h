#include "FinalStateAnalysis/Utilities/interface/GraphSmoother.h"

//From FinalStateAnalysis/StatTools
#include "FinalStateAnalysis/StatTools/interface/RooDataHistEffBuilder.h"
#include "FinalStateAnalysis/StatTools/interface/RooCruijff.h"
#include "FinalStateAnalysis/StatTools/interface/TEfficiencyBugFixed.h"

//From FinalStateAnalysis/TagAndProbe
#include "FinalStateAnalysis/TagAndProbe/interface/MuonPOG2011HLTEfficiencies.h"
#include "FinalStateAnalysis/TagAndProbe/interface/ScaleFactorsMuEG201253X.h"

#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;
#pragma link C++ nestedclasses;

#pragma link C++ function smooth;
#pragma link C++ function smoothWithErrors;
#pragma link C++ function smoothBandUtils;
#pragma link C++ function smoothBandUtilsWithErrors;

//From FinalStateAnalysis/StatTools
#pragma link C++ class RooDataHistEffBuilder;
#pragma link C++ class RooCruijff;
#pragma link C++ class TEfficiencyBugFixed;

//From FinalStateAnalysis/TagAndProbe
#pragma link C++ function Eff_HLT_Mu13_Mu8_2011_TPfit_RunAB_EtaEta_DATA;
#pragma link C++ function Eff_HLT_Mu13_Mu8_2011_TPfit_RunAB_EtaEta_MC;
#pragma link C++ function Eff_HLT_Mu13_Mu8_2011_TPfit_RunAB_EtaEta_DATAoverMC;
#pragma link C++ function Eff_HLT_Mu17_Mu8_2011_TPfit_RunAB_EtaEta_DATA;
#pragma link C++ function Eff_HLT_Mu17_Mu8_2011_TPfit_RunAB_EtaEta_MC;
#pragma link C++ function Eff_HLT_Mu17_Mu8_2011_TPfit_RunAB_EtaEta_DATAoverMC;

#pragma link C++ function muTrigScale_MuEG_2012_53X;
#pragma link C++ function eleTrigScale_MuEG_2012_53X;
#pragma link C++ function muTrigEff_MuEG_2012_53X;
#pragma link C++ function eleTrigEff_MuEG_2012_53X;
#pragma link C++ function muIDscale_MuEG_2012_53X;
#pragma link C++ function eleIDscale_MuEG_2012_53X;

#endif
