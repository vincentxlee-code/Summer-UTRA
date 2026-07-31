Journal of Geophysical Research: Oceans
RESEARCH ARTICLE An Emergent Sea Ice Floe Size Distribution in a Global Coupled
10.1029/2017JC013692 Ocean-Sea Ice Model
KeyPoints: LettieA.Roach1,2 ,ChristopherHorvat1,3 ,SamuelM.Dean1,andCeciliaM.Bitz4
(cid:2)Wedevelopthefirstglobalocean-sea
icemodeltoprognosticallysimulate 1NationalClimateCentre,NationalInstituteofWaterandAtmosphericResearch,Wellington,NewZealand,2Schoolof
aseaicefloesizedistribution Geography,EnvironmentandEarthSciences,VictoriaUniversityofWellington,Wellington,NewZealand,3Instituteat
(cid:2)Thefloesizedistributionemergesby
BrownforEnvironmentandSociety,BrownUniversity,Providence,RI,USA,4AtmosphericSciences,UniversityofWashington,
resolvingprocessesactingon
individualfloes Seattle,WA,USA
(cid:2)Floesize-dependentfeedbackshave
asignificantimpactonsimulatedsea
ice Abstract Seaiceiscomposedofdiscretefloes,whichrangeinsizeacrossordersofmagnitude.Herewe
presentamodelthatrepresentsthejointdistributionofseaicethicknessandfloesize.Unlikepreviousstud-
SupportingInformation: ies,wedonotimposeaparticularformonthesubgrid-scalefloesizedistribution.Floesizesaredetermined
(cid:2)FigureS1 prognosticallybytheinteractionoffivekeyphysicalprocesses:newiceformation,weldingoffloesinfreez-
ingconditions,lateralgrowthandmelt,andfractureoffloesbyoceansurfacewaves.Coupledmodelresults
Correspondenceto:
suggestthattheseprocessescapturefirst-ordercharacteristicsofthefloesizedistribution,includingdecay
L.Roach,
Lettie.Roach@niwa.co.nz inthedistributionwithincreasingfloesizeandbasin-widespatialvariabilityinrepresentativeradius.Lateral
meltandfloeweldingareparticularlyimportant,withwavefracturecreatingfloesatpreferredsizes.The
Citation: additionoffloesizedependencetotheexistingmodelphysicsresultsinsignificantreductionsinseaice
Roach,L.A.,Horvat,C.,Dean,S.M.,& concentration,particularlyinsummerandprincipallyduetofloesize-dependentlateralmelt.Theincreased
Bitz,C.M.(2018).Anemergentseaice
lateralmeltalterspartitioningofthemeltingpotential,whichreducesbasalmeltandincreasesseaicethick-
floesizedistributioninaglobal
coupledocean-seaicemodel.Journal nessinsomelocations.Theseresultssuggestthatincludingafloesizedistributionmaybeimportantfor
ofGeophysicalResearch:Oceans,123, accuratesimulationofthepolarclimatesystem.
4322–4337.https://doi.org/10.1029/
2017JC013692
Plain LanguageSummary Climatemodelssimulatecomplexinteractionsbetweentheocean,
Received7DEC2017 atmosphere,landsurface,andseaiceonverticalandhorizontalgrids.Withinamodelgridcell,whichistyp-
Accepted19APR2018
icallyaround18latitude/longitudehorizontalresolution,theseaicecomponentcurrentlyonlysimulatesthe
Acceptedarticleonline6MAY2018
differentthicknessesofanyicepresent.Real-lifeseaicecoverismadeupofdiscretepiecesoficecalled
Publishedonline30JUN2018
floes,whichcanhavewidelyvaryinghorizontalsizes.Herewepresentanewseaicemodelwhichsimulates
bothfloesizesaswellasthicknesses.Floesizeschangewhennewiceiscreated,icemeltsorfreezes,or
whenfloesarebrokenupbyoceanwaves.Thenewmodelaltersthesimulationoflarge-scaleseaice
properties,whichcouldbeimportantforaccuraterepresentationofpolarclimate.
1.Introduction
The Earth’s sea ice cover is a heterogeneous and variable medium, composed of myriad individual solid
pieces,calledfloes,eachidentifiablewithahorizontalsize.Sizesofindividualfloesvaryoveranextremely
broadrange,fromcentimeterstohundredsofkilometers.Thefloesizedistribution(FSD),F(r),isaprobabil-
ityfunctionthatcharacterizesthisvariability(Rothrock&Thorndike,1984).Overaregionoftheice-covered
ocean,FðrÞdr isthefractionofaregioncoveredbyfloeswithasizebetweenrandr1dr.Floesizehasan
important relationship with simulated sea ice evolution (Horvat et al., 2016; Rynders et al., 2016; Steele,
1992),whichmaybeparticularlyrelevantforthelargelyseasonalAntarcticseaicecover,andastheArctic
VC2018TheAuthors. oceantransitionsfromaperennialseaicecovertoaseasonalone(Aksenovetal.,2017).
Thisisanopenaccessarticleunderthe
termsoftheCreativeCommonsAttri- Current sea ice models are complex, incorporating multiple vertical layers in the snow and ice through
bution-NonCommercial-NoDerivs whichradiationscatters,variablesurfacetreatmentssuchassnowcoverandmeltponds,andviscoplastic
License,whichpermitsuseanddistri- orelastic-brittlematerialpropertiesthataffecttheicedeformationintoridges.Mostdescribethetimeevo-
butioninanymedium,providedthe
lutionoficeusingaprobabilitydistributionoficeinthicknesscategoriesfollowing(Thorndikeetal.,1975).
originalworkisproperlycited,theuse
TodatenomodernglobalclimatemodelssimulatefloesizeortheFSD.Recently,pan-Arctic(Zhangetal.,
isnon-commercialandnomodifica-
tionsoradaptationsaremade. 2016) and stand-alone (Bennetts et al., 2017) models which include floe size information have been
ROACHETAL. 4322

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
demonstrated,buttheseimposetheFSDshapeorbehaviorratherthanallowingittoemergefromphysical
processes acting on individual floes. Further, the power law FSD profiles used to develop these empirical
parametrizations may be inconsistent with observations (Herman, 2010) and the physics of sea ice floes
(Hermanetal.,2018;Horvat&Tziperman,2017).
In this study, we allowthe FSD to emergefrom theinteraction of a set of coupled processes, ratherthan
imposingaparticulardistributionalshape.Buildingfromthemodelofthejointfloesizeandthicknessdistri-
bution(FSTD)developedbyHorvatandTziperman(2015,2017),wepresentthefirstglobalocean-seaice
modeltoprognosticallysimulatetheseaiceFSD.Theschemeiscompatiblewithexistingseaicethickness
distributionmodelsandisimplementedwithintheLosAlamosseaicemodel,CICE5.1(Hunkeetal.,2015).
Themodelsimulatesthestatisticalevolutionoffloessubjecttolateralgrowthandmelt,weldingoffloesin
freezingconditions,newiceformation,andfractureoffloesbyoceansurfacewaves,withtheshapeofthe
FSD emerging from these processes. Using the model in coupled ocean-sea ice simulations, we examine
thecontributionofthoseprocessestoFSDevolutionatahemisphericscale.Wefurthershowthatincluding
floesizeinformationhasasignificantimpactonseaiceconcentrationandthicknessglobally.
Thispaperproceedsasfollows:wediscusstheincorporationofaprognosticFSDintoCICEinsection2.We
showresultsfromcoupledsimulationsinsection3;discusslimitations,comparetootherstudies,andmake
recommendationsforobservationsthatwouldadvanceFSDmodelsinsection4;andconcludeinsection5.
2.Model
2.1.StandardModel
The FSD model is implemented as a component of the Los Alamos sea ice model, CICE5.1 (Hunke et al.,
2015).CICEordinarilysimulatesanicethicknessdistribution(ITD),g(h)(unitsm21),wheregðhÞdhisdefined
asthefractionofoceansurfacecoveredbyicewiththicknessbetweenhandh1dh,suchthat
h ðmax
gðhÞdh51: (1)
0
Theseaiceconcentration,c,isobtainedbyintegratingoverallnonzerothicknesses,
h ðmax
gðhÞdh5c; (2)
hmin
whereh isthelowerboundofthesmallesticethicknessclassresolved.Theseaiceconcentration,c,and
min
theopenwaterfraction,/,sumtounity.TheevolutionoftheITDis,
@g @
52 ðlgÞ2r(cid:3)ðgvÞ1w; (3)
@t @t
wheretermsontheright-handside,respectively,representthechangeinthicknessduetothermodynamic
growth/meltatamelting/freezingratelðhÞ;advectionoftheicethicknessdistributionbyseaicedynamics
aticevelocityv;andredistributionoficebetweenthicknesscategoriescausedbyseaicedeformation,w.
WebrieflydescribethetreatmentofseaicethermodynamicsinCICEhere.
TheheatavailableinthesurfaceoceantomeltorfreezeseaiceisdenotedF (unitsW/m2),andwhen
frzmlt
F <0,theseaicemelts.Icethicknesschangesattheicebasearedeterminedbybalancingtheconduc-
frzmlt
tive heat flux at the bottom surface, F , and the net downward heat flux from the ice to the ocean, F
cb bot
(Maykut&McPhee,1995),
F 52cocnq C u ðT 2T Þ; (4)
bot p w h (cid:4) w f
wherecocnandq aretheoceanheatcapacityanddensity,C isaheattransfercoefficient,u istheocean-
p w h (cid:4)
icefrictionvelocity,T isthefreezingtemperature,andT istheoceansurfacetemperature.
f w
Lateralseaicemeltingisobtainedasafunctionofafixedfloesizeparameter,L.CICEusesasinglefloesize
ofL(cid:5)300m,whichisanorderofmagnitudelargerthanthescaleatwhichlateralmeltingisbelievedto
ROACHETAL. 4323
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 21699291, 2018, 6, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Journal | of Geophysical | Research: |     |     | Oceans |     |     |
| ------- | -------------- | --------- | --- | --- | ------ | --- | --- |
10.1029/2017JC013692
affectseaicevolumeevolution(Steele,1992).Thechangeinseaiceconcentrationduetolateralmeltfol-
lowsSteele(1992),
|     |     |     |     | dgðhÞ gðhÞ |       |     |     |
| --- | --- | --- | --- | ---------- | ----- | --- | --- |
|     |     |     |     | 5          | w ;   |     | (5) |
|     |     |     |     | dt         | L lat |     |     |
withaverticallyaveragedlateralmeltrate,w lat ,thatisassumedtobeuniformaroundtheperimeterofeach
floe,givenbyJosbergerandMartin(1981),
Þm2:
|     |     |     |     | w lat 5m 1 ðT | w 2T f |     | (6) |
| --- | --- | --- | --- | ------------- | ------ | --- | --- |
Thecoefficientsm andm arethebestfittodataquotedbyMaykutandPerovich(1987),measuredina
1 2
single static lead in the Canadian Arctic archipelago over a 3 week period. The sum of F bot and the heat
requiredtoeffectthechangeinconcentrationduetolateralmelt,F ,cannotexceedthemeltingpoten-
side
tial,F frzmlt ,andarereducedproportionallyifthisoccurs.
Duringfreezingconditions,whenF (cid:6)0,avolumeofseaice,V ,isproducedinproportiontoF .
|     |     | frzmlt |     |     |     | new | frzmlt |
| --- | --- | ------ | --- | --- | --- | --- | ------ |
=/(cid:7)0:9h0,whereh0
Thisvolumeisaddedtothethinnestcategory,providedV new 1 1 istheupperboundary
of the thinnest category. The fractional coverage of the thinnest category is increased by
minð/;V =0:05 mÞ.However,ifV =/>0:9h0,thenavolume0:9h0/isaddedtothethinnestcategory
|     | new | new |     | 1   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
and its fractional coverage is raised by /, and the surplus volume V 20:9h0/ is distributed to all other
new 1
thicknesscategoriesinproportiontotheirfractionalcoverage.
2.2.TheJointFloeSizeandIceThicknessDistribution
WeextendthedefinitionoftheicethicknessdistributionfollowingHorvatandTziperman(2015)toajoint
floe sizeand thickness distribution (FSTD). Individualfloes are identifiedwith a sizerand area x(r), where
xðrÞ54ar2 for a50:66<p=4 (Rothrock & Thorndike, 1984). The probability distribution fðr;hÞdrdh is the
fraction of grid surface area covered by ice with thickness between h and h1dh and lateral floe size
betweenrandr1dr.TheFSTDsatisfies
|     |     | ðrmax | ðhmax             |     | ð ð           |     |     |
| --- | --- | ----- | ----------------- | --- | ------------- | --- | --- |
|     |     |       | fðr;hÞdrdh(cid:5) |     | fðr;hÞdrdh51: |     | (7) |
|     |     | rmin  | 0                 |     | R H           |     |     |
IntegratingtheFSTDoverallfloesizesyieldstheITD,
ð
|     |     |     |     | fðr;hÞdr5gðhÞ; |     |     | (8) |
| --- | --- | --- | --- | -------------- | --- | --- | --- |
R
whereasintegratingtheFSTDoverallicethicknessesgivestheFSD,F(r),
ð
|     |     |     |     | fðr;hÞdh5FðrÞ: |     |     | (9) |
| --- | --- | --- | --- | -------------- | --- | --- | --- |
H
WecanalsodefinethenumberFSTD,fNðr;hÞ,wherefNðr;hÞdrdhisthenumberoffloesperunitoceansur-
faceareawiththicknessbetweenhandh1dhandlateralfloesizebetweenrandr1dr,
fðr;hÞ
|     |     |     |     | fNðr;hÞ5 | :   |     | (10) |
| --- | --- | --- | --- | -------- | --- | --- | ---- |
4ar2
ThenumberFSD,obtainedbyintegratingfNðr;hÞdhoverallicethicknesses,isoftenusedinobservational
studies(e.g.,Perovichetal.,2014).
FollowingHorvatandTziperman(2015),timeevolutionoftheFSTDisgivenby
@fðr;hÞ
|     |     |     | 52r(cid:3)ðfðr;hÞvÞ1L |     |     | 1L 1L : | (11) |
| --- | --- | --- | --------------------- | --- | --- | ------- | ---- |
|     |     |     | @t                    |     | T   | M W     |      |
Thetermsontheright-hand-siderepresentforcingofthedistributionf(r,h)byadvection,thermodynamics,
mechanical interactions between floes (ridging and rafting), and fracture by ocean surface waves,
respectively.
ROACHETAL. 4324

 21699291, 2018, 6, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Journal | of Geophysical |     | Research: |     | Oceans |     |     |
| ------- | -------------- | --- | --------- | --- | ------ | --- | --- |
10.1029/2017JC013692
Toimplementthis modelin CICE,wedefinea modifiedareal FSTD(mFSTD),L(r,h), where,withina given
thickness range between h and h1dh; Lðr;hÞdr is the fraction of ice with lateral floe size between r and
r1dr.Bydefinition,thissatisfies
ð
|     |     |     |     | Lðr;hÞdr51; |     |     | (12) |
| --- | --- | --- | --- | ----------- | --- | --- | ---- |
R
and
|     |     |     |     | fðr;hÞ5gðhÞLðr;hÞ: |     |     | (13) |
| --- | --- | --- | --- | ------------------ | --- | --- | ---- |
ImplementationofthemFSTDallowspreservationofthestandardmodelformulationfortheITD.
We neglect the two-way relationship between floe size and mechanical redistribution, retaining the stan-
dardCICEschemeformechanicalredistributionusedtoevolvetheITD.Mechanicalredistributionreduces
theareafractionsofallfloesequally,withoutaffectingthemFSTD.TransportoftheFSTDisachievedusing
thestandardCICEschemefortraceradvection.Thesizesoffloesdonotappeardirectlyinanytermsinthe
momentum equation or constitutive law. In reality, we would expect floe sizes to affect both mechanical
redistribution and transport of the FSTD, but the precise relationships are uncertain and we assume that
theyareofsecond-orderimportancetosimulationoftheFSD.
Apart from advection, the processes which determine the FSTD are thermodynamics—lateral melt and
growth, freezing together of floes, and new ice formation—and mechanical wave fracture. These are
describedinmoredetailbelow.
2.3.Thermodynamics
ThermodynamicchangestotheFSTDaregivenby
2
|     |     | L ðr;hÞ52r | (cid:3)ðfðr;hÞGÞ1 | fðr;hÞG1dðr2r | Þdðh2h | ÞA_ 1b :   | (14) |
| --- | --- | ---------- | ----------------- | ------------- | ------ | ---------- | ---- |
|     |     | T          | ðr;hÞ             |               | r min  | min p weld |      |
r
Thefirsttwotermsontheright-handsideinequation(14)representgrowthandmeltofexistingfloesin
thicknessandlateralsize,atarateG5ðG;G Þ.Thethirdtermrepresentsgrowthofnewice:newfloesare
|     |     |     | r   | h   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
createdatarateA_
|     |     | inthesmallestthicknesscategoryh |     |     | ,andthesmallestlateralsizecategoryr |     | ,i.e., |
| --- | --- | ------------------------------- | --- | --- | ----------------------------------- | --- | ------ |
|     |     | p                               |     |     | min                                 |     | min    |
thatalliceformsinitiallyaspancakes.Toallowforthejoiningofindividualfloestooneanother,werepre-
|     | senttheweldingtogetheroffloesinfreezingconditionsviathefourthterm,b |     |     |     |     | .   |     |
| --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
weld
Inmeltingconditions,thelateralmeltrateis
|     |                                                 |     |     | G5w r | lat                           |     | (15) |
| --- | ----------------------------------------------- | --- | --- | ----- | ----------------------------- | --- | ---- |
|     | topreserveconsistencywiththestandardmodel,withw |     |     |       | lat determinedviaequation(6). |     |      |
Infreezingconditions,thelateralgrowthrateis
|     |     |     |     | G5A r lat V new | =Dt; |     | (16) |
| --- | --- | --- | --- | --------------- | ---- | --- | ---- |
whereDtisthetimestepandV new isthevolumeofnewicegrowthinDt,asperthestandardmodel.A lat is
thefractionofnewicegrowththatistakentoadheretofloeedges,representinglateralgrowthofexisting
floes.Thisisrelatedtothe‘‘leadregion,’’theareacomposedofallannuliofwidthr (Table1)aroundfloes.
lw
|     | Thefractionofthedomainbelongingtotheleadregion,/ |     |     |     | ,is |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
lead
|     |     |     | (cid:4)ð | ð (cid:2)2r | r2(cid:3) | (cid:5) |     |
| --- | --- | --- | -------- | ----------- | --------- | ------- | --- |
lw1
|     |     |     | / 5min | fðr;hÞ | lw drdh;/ | :   | (17) |
| --- | --- | --- | ------ | ------ | --------- | --- | ---- |
|     |     |     | lead   |        | r r2      |     |      |
R H
where/istheopenwaterfraction.Notingthatthecircumferenceofafloeis4a(cid:3)2r,thetotallateralsurface
areaoffloes,perunitareaoftheoceansurface,is,
ð ð
|     |     |     | 2hr5 | fNðr;hÞ8arhdrdh: |     |     |     |
| --- | --- | --- | ---- | ---------------- | --- | --- | --- |
R H
Thenthefractionofnewicegrowthadheringtofloeedges,A ,istheproductoftheleadregionwiththe
lat
fractionalcontributionoflateralsurfaceareatothetotalsurfacearea,
ROACHETAL. 4325

 21699291, 2018, 6, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Journal | of Geophysical |     | Research: | Oceans |     |     |
| ------- | -------------- | --- | --------- | ------ | --- | --- |
10.1029/2017JC013692
Table1
ParametersThatAreNotPresentinStandardCICE
|     | Parameter               | Description | Value |                            | Reference |     |
| --- | ----------------------- | ----------- | ----- | -------------------------- | --------- | --- |
|     | a Noncircularityoffloes |             | 0.66  | RothrockandThorndike(1984) |           |     |
|     | r lw Widthofleadregion  |             | r 1   | HorvatandTziperman(2015)   |           |     |
0.01m22s21
j Rateconstantformerging Roachetal.[2018a]andseesupportinginformation
331025
(cid:2) crit Criticalstrain HorvatandTziperman(2015),KohoutandMeylan(2008)
|     | t wave Smallestfloesize |     | 10m | Toyotaetal.(2011) |     |     |
| --- | ----------------------- | --- | --- | ----------------- | --- | --- |
affectedbywaves
Note.r denotesthesmallestfloesizeresolvedinthemodel.
1
2hr
|     |     |     | A lat 5/ | lead2hr1c : |     |     |
| --- | --- | --- | -------- | ----------- | --- | --- |
The volume that remains after lateral growth, ð12A ÞV , is distributed according to the standard CICE
lat new
newicegrowthformulationasdescribedinsection2.1.Wechoosetoplacenewlyformediceinthesmall-
estfloesizecategory,parametrizingthemaspancakefloes,asmentionedabove.Seesection4fordiscus-
sionofthischoice.
Floes that are determined to be in contact with one another while the upper ocean is being cooled may
freezetogether(Shen&Ackley,1991),aprocessthatisdominantintheSouthernOcean(Wadhamsetal.,
1987).Weconsiderseaicefloesrandomlyplacedonthemodeldomainandallowthemtoweldtogether
thermodynamicallyduringfreezingconditionsaccordingtotheprobabilitythattheyoverlap.Forsimplicity,
webrieflychangevariablestofloeareax54ar2
|     |     |     | definedonX5½x |     | min ;x max (cid:8),andpresumeseaiceisallofthe |     |
| --- | --- | --- | ------------- | --- | --------------------------------------------- | --- |
same thickness. We define the area number density function N(x) (units m24), with NðxÞdx equal to the
numberoffloesperunitareabetweenfloeareaxandx1dx,notingthattheareafractionoccupiedbyfloes
with area between x and x1dx is x(cid:3)NðxÞdx. The geometric probability of overlap is described using a
‘‘coagulationequation’’(Filbet&Laurenc¸ot,2004;Smoluchowski,1916),
|     |     |     | 1ð  | ð   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
@Nðx;tÞ
|     |     |     | 5 Kðx0;x2x0Þdx02 | Kðx;x0Þdx0: |     | (18) |
| --- | --- | --- | ---------------- | ----------- | --- | ---- |
@t 2
|     |     |     | X   | X   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
K(a,b)(unitsm26s21)isthe‘‘coagulationkernel,’’whereKða;bÞdadbdt isthenumberofmergersperunit
area of floes with area between a and a1da, and b and b1db over a period dt, and Kða;bÞ(cid:5)0 for any
a;b(cid:7)0.Thefirstintegralinequation(18)accountsfortheformationoffloesofareaxresultingfromthe
mergeroftwofloeswithrespectiveareasx0 andx2x0,wherex0 <x.Thesecondintegraldescribestheloss
offloeswithareaxbycoagulationwithotherfloes.WecomputethecoagulationkernelKðx;x0Þastheprod-
uctoftheareafractionoffloesofsizexandx0,
Kðx;x0Þ5j(cid:3)x(cid:3)x0(cid:3)NðxÞNðx0Þ;
(19)
wherejisarateperunitarea.Integratingequation(18)overallxleadstothetimechangeoffloenumber
perunitarea,N,
|     |     |     | (cid:4)ð ð (cid:2)1               |     | (cid:3) (cid:5) |     |
| --- | --- | --- | --------------------------------- | --- | --------------- | --- |
|     |     | @N  | x0ðx2x0ÞNðx0ÞNðx2x0Þ2xx0NðxÞNðx0Þ |     | dx0             |     |
|     |     | 5j  | dx                                |     |                 |     |
|     |     | @t  | 2                                 |     |                 |     |
X X
|     |     | j(cid:4)ðx | (cid:2)ð                   |     | (cid:3) (cid:5) |     |
| --- | --- | ---------- | -------------------------- | --- | --------------- | --- |
|     |     | 5          | dx0 x0ðx2x0ÞNðx0ÞNðx2x0Þdx |     | 22c2            |     |
2
xmin X
j
|     |     | 52  | c2; |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
2
Ð
wherewemakeuseofthefactthat xNðxÞdx5c.Therateperunitareajisthetotalnumberoffloesthat
weldwithanother,persquaremeter,perunittime,inthecaseofafullycoveredicesurface(c51),equalto
twicethereductionintotalfloenumber.Roachetal.(2018a)foundalowerboundonjof0.001m22s21in
observations of smallfloes freezingtogetherintheautumn ArcticOcean.Weuse a valueofj50:01m22
s21forthefloeweldingparameter.
ROACHETAL. 4326

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
2.4.WaveFracture
Following Horvat and Tziperman (2015), the change in the FSTD f(r, h), per unit time due to fracture by
oceansurfacewavesis,
ð ð
L ðr;hÞ52Xðr;hÞ1 Xðs;hÞfðr;h;s;hÞdsdh: (20)
W s s s
R H
Xðr;hÞdrdh is the fraction of ocean surface area covered by floes with size and thickness between ðr;hÞ
and ðr1dr;h1dhÞ that is fractured by waves per unit time. fðr;h;s;hÞdrdh is the fraction of ocean sur-
s
face area covered by floes with size and thickness between ðr;hÞ and ðr1dr;h1dhÞ formed due to the
fracture of floes with size and thickness between ðs;hÞ and ðs1ds;h1dhÞ. The first term on the right-
s s s
hand side in equation (20) thus represents the fracture of floes at a given size and thickness into smaller
sizes, and the second term represents the fracture of floes at larger sizes that result in floes at a given
size and thickness.
Weproceedbycalculatingthefracturesthatwouldoccurifwavesenterafullyice-coveredregiondefined
in one dimension in the direction of propagation, and then apply the outcome proportionally to the ice-
covered fractionin each gridcell. Notingthat floe sizeis halfitsdiameter, thesumof floe sizes in a one-
dimensional,fullyice-covereddomainisequaltothehalfthedomainlength,D=2.Weconsiderthehisto-
gramoffloesizes,W(r),formedduetothefractureofseaicebywaves,whereWðrÞdrisequaltothenum-
beroffractureswitharesultingfloesizebetweenrandr1dr,
ð
rWðrÞdr5D=2: (21)
R
Thefunctionfðr;h;s;hÞisthefractionofDcomposedoffracturesofsizer,equaltorW(r)ifr<s,andzero
s
otherwise,
rWðrÞ
fðr;h;s;hÞ5 dðh2hÞHðs2rÞ; (22)
s Ðs
rWðrÞdr
s
rmin
whereHistheHeavisidestepfunction.Bydefinition,
ð ð
fðr;h;s;hÞdrdh51; (23)
s
R H
soequation(20)conservesseaiceareaandvolume.Wecomputetheareaoffloesofsize(r,h)thatisfrac-
turedperunittimeas
c (cid:2) 1 ðr (cid:3)
Xðr;hÞ5fðr;hÞ g r0Wðr0Þdr0 ; (24)
D D=2
rmin
theproductofthreeterms:(1)thefractionofoceansurfaceareaoriginallycoveredbyfloesofsize(r,h);(2)
thefractionofthedomainthatisreachedbyoceansurfacewavesmovingattheirgroupvelocityc ,(c =D);
g g
and (3) the fraction of a fully ice-covered domain of width D that would be fractured into radii smaller
thanr.
ItremainstocomputethehistogramofnewfloesizesW(r),forwhichwerequiretheseasurfaceheightfield
gðxÞ. In the absence of a coupled wave model that simulates wave attenuation in ice, we construct an
approximate attenuated sea surface height field using hindcast wave data outside the sea ice region. We
neglect swell induced by winds within the ice pack and only draw in ocean swell along lines of constant
longitude. In each ice-covered grid cell, we find the closest equatorward nonice-covered grid cell along
linesofconstantlongitude.Ifthisgridcellisland,nowavefractureoccurs.Ifthisgridcellisnotland,we
selectthesignificantwaveheightandmeanperiodfromawavemodelhindcast.Theoceanwavespectrum
isthenconstructedasaBretschneiderspectrum,followingHorvatandTziperman(2015)andBennettsetal.
(2017). It is attenuated exponentially according to the number of floes in the grid cells between the ice-
coveredgridcellbeingconsideredandthenonice-coveredone.Theattenuationcoefficientisaquadratic
functionofseaicethicknessandwaveperiodfitbyHorvatandTziperman(2015)totheresultsofKohout
and Meylan (2008). Further information can be found in the supporting information of Horvat and
Tziperman(2015).
ROACHETAL. 4327
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
Fromthelocaloceansurfacewavespectrum,wegeneratearealizationoftheseasurfaceheightfieldusing
arandomphaseasinHorvatandTziperman(2015).Assumingthatseaiceflexeswiththeseasurfaceheight
fieldgðyÞ,strain(cid:2)isgivenby
h@2g
(cid:2)5 ; (25)
2@y2
whereyisthespatialcoordinate.Thederivativeiscomputedbetweensuccessiveextremaoftheseasurface
height,either (maximum,minimum,maximum) or (minimum,maximum, minimum). If thestrain between
successiveextremaexceedsacriticalvalue,(cid:2) (Table1),newfloesareformedwithdiametersequaltothe
crit
distance between the extrema. New floe radii resulting from fracture are collected into a histogram, W(r),
which depends only on the local sea surface height field. In the interests of computational expense, W(r)
and c are computed offline for different values of sea ice thickness, mean wave period, significant wave
g
height, and number of attenuating floes. This look-up table defines 5,000 attenuated sea surface height
fieldswhichcanbeusedtofractureiceduringcodeintegration.Givenaseasurfaceheightfield,thescheme
computes the new floe sizes generated by wave fracture explicitly, without requiring any assumptions
abouttheFSD.
3.Results
Theadditionalphysicsdescribedinsections2.2–2.4hasbeenimplementedinCICE5.1(Hunkeetal.,2015)
and coupled to the NEMO ocean model, using a configuration based on Rae et al. (2015). The ocean-sea
ice model is forced with the atmospheric reanalysis JRA-55 (Japan Meteorological Agency, 2013) and run
on a 18 tripolar grid. All simulations described here use repeated atmospheric forcing from a single year.
We choose a presatellite era year (1975), as these spin-up simulations will be used to initialize transient
simulations over the satellite era in later work. Wave forcing corresponding to the same year is taken
from a hindcast of the ocean surface wave model, Wavewatch III (Tolman, 2009), which was also forced
byJRA-55.
We present here two experiments: a simulation using the standard model (CICE5.1), and a simulation
includinga prognostic FSDas describedabove. Allanalysisusesmonthlymodel output. Floesizecatego-
ries follow a Gaussian spacing and span a similar range to those chosen by Zhang et al. (2015). Finite
differencinginfloesizespacefollowstheschemeusedbyHibler(1980)forfinitedifferencinginthickness
space.
ParameterswhicharenotpresentinstandardCICEandtheirvaluesareshowninTable1.Asglobalobserva-
tionsofseaiceFSDarenotavailable,parametervalueshavenotbeentunedorcalibratedtoreproducecer-
tainFSD behavior and are based on estimates from previous studies. More information on theparameter
values and their uncertainty can be found in thereferences provided in Table 1. In particular, Horvat and
Tziperman(2015) performedlocalsensitivity tests formost parameterslisted.AsRoachetal.(2018a)sug-
gest that their estimated lower bound for the floe welding parameter, j, is conservative, we use a value
thatisoneorderofmagnitudehigher.jistheonlynewparameterpresentedhere,soweincluderesults
from an experiment where its value is reduced in the supporting information. Grid-cell-average floe sizes
depend strongly on this parameter (see supporting information). Naturally, we expect floe sizes to also
depend on the choice of floe size categories. More investigation of parameter sensitivity is required, but
should occur in fully coupled atmosphere-ocean simulations where all feedbacks are included—a step
whichisbeyondthescopeofthismanuscript.
AkeytestofthenewmodelphysicsiswhetheraseaiceFSDshowingphysicallyreasonablecharacteristics
can be simulated in model experiments that begin without FSD initialization, sea ice cover and imposed
FSD shape. All simulations are initialized without sea ice cover. Sea ice volume stabilizes after 15 years in
the Arctic and after 45 years in the Antarctic. All further analysis is therefore conducted over the final 20
yearsofa65yearmodelrun.Whiledetailedinformationissimulatedatthesubgrid-scale,herewefocuson
resultingcharacteristicsatthehemisphericscaletogiveanoverallpictureofmodelbehaviorwithoutfocus-
ing on any particular region. Horvat and Tziperman (2015, 2017) describe behavior of most processes
included here at the subgrid-scale. We proceed by first describing overall behavior of simulated floe size
andthenexamininghowdifferentprocessescontributetoit.
ROACHETAL. 4328
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 21699291, 2018, 6, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Journal | of Geophysical | Research: |     | Oceans |     |     |     |     |     |
| ------- | -------------- | --------- | --- | ------ | --- | --- | --- | --- | --- |
10.1029/2017JC013692
Toshowfloesizecharacteristicsspatiallyatthehemisphericscale,we
averageoverfloesizes.Figure1showsthecell-averagearea-weighted
|     |     | ‘‘representative’’floeradius,r |     |     | a ,whichisdefinedusingthearealFSTD, |             |     |     |     |
| --- | --- | ------------------------------ | --- | --- | ----------------------------------- | ----------- | --- | --- | --- |
|     |     |                                |     |     | Ð Ð                                 | rfðr;hÞdrdh |     |     |     |
R H
|     |     |     |     | r   | a 5 Ð Ð |     | :   |     | (26) |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | ---- |
fðr;hÞdrdh
R H
TherepresentativefloeradiusclimatologyinFigure1isobtainedafter
|     |     | beginning                    | the simulation  |         | without    | sea                           | ice cover | and allowing   | it to      |
| --- | --- | ---------------------------- | --------------- | ------- | ---------- | ----------------------------- | --------- | -------------- | ---------- |
|     |     | spin-up.                     | In the Northern |         | Hemisphere |                               | (NH), the | representative | floe       |
|     |     | radiusislargestinthecenterof |                 |         |            | theicepackandsmallertowardthe |           |                |            |
|     |     | edges at                     | the winter      | maximum | in         | March                         | (Figure   | 1a). At        | the summer |
minimuminSeptember,therearefewerverysmallandverylargerep-
resentativeradii(Figure1b).Largerfloesareconcentratedaroundthe
coastneartheCanadianarchipelagoandEastSiberianSea.Generally,
|     |     | the representative |     | floe radius | is  | smaller | in the Southern |     | Hemisphere |
| --- | --- | ------------------ | --- | ----------- | --- | ------- | --------------- | --- | ---------- |
(SH)thantheNH(Figures1cand1d).Inthewinter,floesarelargestin
areasofcompactice,suchastheAmundsenandWeddellSeas(Figure
1d).Inthesummer,largefloesarefoundontheedgeoftheicecover
(Figure1c).
|     |     | Figures 2a–2d | show | total | hemispheric |     | number | distributions, | which |
| --- | --- | ------------- | ---- | ----- | ----------- | --- | ------ | -------------- | ----- |
fNðr;hÞ
|     |     | are obtained | by      | integrating |     | over    | sea ice     | thickness | and the  |
| --- | --- | ------------ | ------- | ----------- | --- | ------- | ----------- | --------- | -------- |
|     |     | ocean area   | in each | hemisphere, |     | for the | NH in March | (Figure   | 2a), the |
NHinSeptember(Figure2b),theSHinMarch(Figure2c),andtheSH
|     |     | in September(Figure |        | 2d).   | Thefour | totalnumberdistributions |          |     | have a        |
| --- | --- | ------------------- | ------ | ------ | ------- | ------------------------ | -------- | --- | ------------- |
|     |     | similar shape.      | A high | number | of      | small (<5                | m) floes | are | simulated all |
year,withmoreduringthewintermonthsthanthesummermonths,
|     |     | due to the | production | of  | new pancake |     | ice at the | smallest | resolved |
| --- | --- | ---------- | ---------- | --- | ----------- | --- | ---------- | -------- | -------- |
floesize.AllfourdistributionsinFigures2a–2dshowasignificantfrac-
|     |     | tion of floes | in the | largest | floe size | category | (>750 | m), | which arises |
| --- | --- | ------------- | ------ | ------- | --------- | -------- | ----- | --- | ------------ |
fromthetruncationoffloesizecategories.TheSHshowsgreatersea-
|     |     | sonal variation | than | the | NH, with | an order | of magnitude |     | more floes |
| --- | --- | --------------- | ---- | --- | -------- | -------- | ------------ | --- | ---------- |
perunitareaatnearlyallsizesinMarch(Figure2c)thaninSeptember
(Figure2d).TheNHhasmoreverylarge(>750m)floesperunitarea
thantheSH.Somebendinginthedistributionisvisibleatfloesizesof
around100m,particularlyintheSHinSeptember(Figure2d).
|     |     | Figures 2e–2h | show      | the         | tendencies | arising | from           | different | floe pro- |
| --- | --- | ------------- | --------- | ----------- | ---------- | ------- | -------------- | --------- | --------- |
|     |     | cesses in     | the total | hemispheric | number     |         | distributions, | where     | the ten-  |
dencyinthenumberFSTDduetosomeprocessisdefinedas
dfNðr;hÞ 1
|     |     |     |     | 5 ðfðr;hÞN |       |         | 2fðr;hÞN |         | Þ; (27) |
| --- | --- | --- | --- | ---------- | ----- | ------- | -------- | ------- | ------- |
|     |     |     |     |            | after | process | before   | process |         |
dt dt
andthemodelmonthlyoutputisthetimeaverageofdfðr;hÞ.Theten-
dt
denciesateachfloesizearethenetresultoffloesbeingaddedtoand
|     |     | removed | from each | floe | size. Figure | 2f  | shows the | NH in | September |
| --- | --- | ------- | --------- | ---- | ------------ | --- | --------- | ----- | --------- |
Figure1.Thesimulatedrepresentativefloeradius,averagedover20yearsfol-
andillustratesthegeneraltendenciesofthedifferentprocesses.New
lowingspin-up,in(aandc)Marchand(b,andd)September,in(aandb)the
NorthernHemisphereand(candd)theSouthernHemisphere.Therangedis- ice growth creates very small floes; lateral growth and melt, respec-
playedischosentodisplaybothhemispheresonthesamescale;darkpurple tively,acttoincreaseandreducethenumberatmostsizes;wavefrac-
maybegreaterthan600m.
|     |     | ture redistributes |     | large | floes to | smaller | sizes; | and | floe welding |
| --- | --- | ------------------ | --- | ----- | -------- | ------- | ------ | --- | ------------ |
redistributesallfloestolargersizes.
Floeweldinghasthelargestmagnitudetendencyofallfiveprocesses(Figures2e–2h).Weldingmovesthe
smallestfloes,createdduringnewiceformation,tolargersizesandisthedominantprocessinthecreation
ofverylargefloes.Fractureisaprocessthatdestroyslargefloesandproducessmallerfloes,soweexpect
thetendencyoffloeproductiontobenegativeforlargerfloes.Inoursimulation,thelargestsixfloesizes
ROACHETAL. 4329

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
Figure2.(a)TheNorthernHemispherefloenumberdistributioninMarchaveragedoverthe20yearsfollowingmodel
spin-up.(b–d)Sameas(a),fortheNorthernHemisphereinSeptember,theSouthernHemisphereinMarch,andtheSouth-
ernHemisphereinSeptember,respectively.(e)Thenettendencyinthefloenumberdistributionfromdifferentphysical
processesintheNorthernHemisphereinMarchaveragedoverthetwentyyearsfollowingmodelspin-up.TheaxisinFig-
ure2eislinearizedaroundzero.(f–h)Sameas(e),fortheNorthernHemisphereinSeptember,theSouthernHemisphere
inMarch,andtheSouthernHemisphereinSeptember,respectively.
showanetlossduetowavefracturewithashapethatissimilartotheirnumberdistribution(butinverted).
Sizesbelowaround150mshowanetgain,aslargefloesfractureintothem,drivingthebendinginthetotal
floenumberdistributionatthissize(Figures2a–2d).Peaksaround100minducedbywavefracturearebal-
ancedoutbystrongerfreezingtogetheroffloesatthatsizeinwinter(Figures2eand2h).Ofthefivepro-
cesses,wavefracturehasthemostsignificanthemisphericdifference,withnetlossesatsomesizesbelow
100mintheSH,unliketheNH.
ROACHETAL. 4330
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
Figure3.Seasonalandspatialvariabilityoftendenciesinrepresentativeradius,r .(a)Thehemisphericaveragetendencyinrepresentativeradiusduetolateral
a
meltfortheNH(solidline)andSH(dashedline).(b–e)as(a)butforlateralgrowth,newiceproduction,floewelding,andwavefracture,respectively.(f)Mapofthe
tendencyinr duetolateralmeltintheNHforthemonthwithmaximumaveragetendency,July(see(a),solidline).(k)Mapofthetendencyinr duetolateral a a
meltintheSHforthemonthwithmaximumaveragetendency,January(see(a),dashedline).(g–j)as(f)and(l–o)as(k)butforlateralgrowth,newiceproduction,
floewelding,andwavefracture,respectively.Notethatlateralgrowthhasunitsof1023md21,whileotherprocesseshaveunitsofmd21.
Lateralmeltisthedominantprocesstoreducefloesizes(Figures2e–2h).Itresultsinanetgaininthenext-
to-largestfloesizecategory,duetothelargenumberoffloesinthelargestfloesizecategory(Figures2a–
2d). Lateral melt is around two orders of magnitude more important than lateral growth (Figures 2e–2h).
ROACHETAL. 4331
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 21699291, 2018, 6, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Journal | of Geophysical | Research: |     | Oceans |     |     |     |     |     |     |
| ------- | -------------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
10.1029/2017JC013692
Notethatthemodelschemedirectlycoupleslateralgrowthandnew
iceformation,suchthatifalargerportionofnewicewentintolateral
growth,fewerverysmall(<5m)floeswouldbecreated.
Figures3a–3eshowthetendencyinrepresentativeradius,
|     |     |     |     |     | Ð Ð     |              |     |     |     |      |
| --- | --- | --- | --- | --- | ------- | ------------ | --- | --- | --- | ---- |
|     |     |     |     | dr  |         | rdfðr;hÞdrdh |     |     |     |      |
|     |     |     |     |     | a5Ð R H | dt           | ;   |     |     | (28) |
Ð
|     |     |     |     | dt  |     | fðr;hÞdrdh |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     | R H |            |     |     |     |     |
hemisphericallyaveragedforeachprocesstogiveasenseofthesea-
|     |     | sonality | of different | processes. | Wave | fracture |     | and lateral | melt | are |
| --- | --- | -------- | ------------ | ---------- | ---- | -------- | --- | ----------- | ---- | --- |
muchmoreimpactfulduringthesummermonthsthantherestofthe
year(Figures3aand3e).Duringthesummermonths,therearemore
|     |     | small floes | (Figures | 1b    | and 1c), exposing |        | more       | perimeter | to         | lateral |
| --- | --- | ----------- | -------- | ----- | ----------------- | ------ | ---------- | --------- | ---------- | ------- |
|     |     | melt and    | allowing | waves | to penetrate      | deeper | into       | the       | ice field. | New     |
|     |     | ice growth  | climbs   | from  | zero just         | before | the summer |           | minimum    | and     |
peaks2monthsafter(NovemberintheNH,AprilintheSH),gradually
decreasingovertheothermonths(Figure3b).Floeweldingisstrong
allyearoutsideofthesummermonths(JJAintheNH,DJFintheSH)
(Figure3d).
|     |     | Figures 3f–3o | show | the | spatial variability |     | of different | processes, |     | with |
| --- | --- | ------------- | ---- | --- | ------------------- | --- | ------------ | ---------- | --- | ---- |
eachsubplotshowingthemonthwheretheneteffectofeachprocess
|     |     | is largest | (according | to Figures | 3a–3e). | For | example, | Figure | 3f  | shows |
| --- | --- | ---------- | ---------- | ---------- | ------- | --- | -------- | ------ | --- | ----- |
lateralmeltintheNHinJuly,whichFigure3ashowsisthemonthof
largestimpact.Forallprocesses,thelargestimpactsoccuraroundthe
iceedge(Figures3f–3o).Floeweldingistheonlysize-increasingpro-
cesstohavesubstantialimpactsintheiceinterior(Figures3iand3n).
Itisthedominantdriverinthecreationoflargefloes(Figures2e–2h)
andthuscontrolsthebehavioroffloesizesinthecentralicepack(Fig-
ure1a).Floesizereductionsduetowavefractureoccuralonglinesof
constantlongitudewithfewimpactsinthecentralicepack(Figures3j
and3o).
OfthefiveprocessesthatdeterminetheFSTD,onlylateralmelt,new
|     |     | ice formation                        | and    | lateral | growth    | directly | change               | sea | ice concentra- |     |
| --- | --- | ------------------------------------ | ------ | ------- | --------- | -------- | -------------------- | --- | -------------- | --- |
|     |     | tion,withlateralgrowthbeingtheonlyof |        |         |           |          | thesenotparametrized |     |                | in  |
|     |     | the standard                         | model. | Yet     | even with | these    | similarities         | to  | the standard   |     |
model,theadditionofaFSDresultsinsignificantchangestothestan-
dardmodelseaiceclimatology.Figure4showstheseaiceconcentra-
tionsimulatedbythestandardmodelandthedifferencebetweenthe
|     |     | standard   | and FSTD | models.             | Only          | differences  | significant |       | at the    | 95%  |
| --- | --- | ---------- | -------- | ------------------- | ------------- | ------------ | ----------- | ----- | --------- | ---- |
|     |     | confidence | level    | are shown.          | The inclusion |              | of floe     | sizes | generally | acts |
|     |     | to lower   | sea      | ice concentrations, |               | particularly |             | in    | already   | low- |
Figure4.Monthlyseaiceconcentrationfields(outofmaximumof1)averaged
|     |     | concentration | areas. | The | average | sea ice | concentration |     | reduction | for |
| --- | --- | ------------- | ------ | --- | ------- | ------- | ------------- | --- | --------- | --- |
over20yearsintheNorthernandSouthernHemispheresforMarch(a,c,e,and
regionsthathavereductionssignificantatthe95%confidencelevelis
g)andSeptember(b,d,f,andh).Thefirstcolumn(a–d)showsthesimulation
fromthestandardmodelandthesecondcolumn(b–h)showsthedifference 210%inSeptemberintheNHand240%inMarchintheSH.Atthe
betweenthestandardandFSTDmodels,whereonlydifferencesthatare ice edge, some of these represent total removal of ice in a grid cell.
significantatthe95%confidencelevelareshown.
|     |     | There are | also | small areas | of increased |     | concentrations |     | at a | similar |
| --- | --- | --------- | ---- | ----------- | ------------ | --- | -------------- | --- | ---- | ------- |
magnitudetothedecreases,suchastheWeddellSea(Figure4g).The
smallareasofincreased concentrationstendtobenearareasofincreased iceadvection.Overall, impacts
arelargerintheSH(Figures4gand4h)thantheNH(Figures4eandf),andinsummermonths(Figures4f
and4g)thanwintermonths(Figures4eand4h).
Therearealsosignificantdifferenceswhenconsideringseaicethickness.Figure5showsthegrid-cellmean
thickness,whichisthevolumeoficeperunitarea,forthestandardmodelandthedifferencebetweenthe
standard and FSTD models. There are both increases and decreases in sea ice thickness relative to the
ROACHETAL. 4332

 21699291, 2018, 6, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Journal | of Geophysical | Research: | Oceans |     |     |     |     |     |     |
| ------- | -------------- | --------- | ------ | --- | --- | --- | --- | --- | --- |
10.1029/2017JC013692
|     |     | standard | model. The average | reduction |     | in the | thickness | of  | the ice- |
| --- | --- | -------- | ------------------ | --------- | --- | ------ | --------- | --- | -------- |
coveredportionofgridcells(forregionsthathavereductionssignifi-
cantatthe95%confidencelevel)is25%(10cm)inSeptemberinthe
|     |     | NH and   | 212% (13 cm)  | in March     | in the | SH.    | Likewise, | the     | average |
| --- | --- | -------- | ------------- | ------------ | ------ | ------ | --------- | ------- | ------- |
|     |     | increase | is 6% (13 cm) | in September | in     | the NH | and       | 25% (23 | cm) in  |
MarchintheSH.Maximumincreasesandreductionsinthicknessare
muchgreateratsomelocations.
DifferencesinlateralmeltratesbetweenthestandardandFSTDmod-
els,whichoccurviathereplacementofL5300minequation(5)with
|     |     | the distribution-integrated |     | factor | from | equation |     | (14), are | near- |
| --- | --- | --------------------------- | --- | ------ | ---- | -------- | --- | --------- | ----- |
universallypositiveandcoincidewithareasofconcentrationdecrease.
Summinghemispherically,thetotallateralmeltrateincreasesapprox-
imatelythreefoldinbothhemispheresrelativetothestandardmodel
|     |     | (in September | in the NH | and March | in  | the SH). | This | acts to | reduce |
| --- | --- | ------------- | --------- | --------- | --- | -------- | ---- | ------- | ------ |
concentrations,andalsoallowssomeareasofincreasedfrazilgrowth
intothenewopenwater.
Drawingalargerheatfluxtomelticelaterallyfromtheoceanicmelt-
|     |     | ing potential | means that      | less is | available         | for basal | melt, | which | may  |
| --- | --- | ------------- | --------------- | ------- | ----------------- | --------- | ----- | ----- | ---- |
|     |     | contribute    | to thicker ice. | The     | total hemispheric |           | basal | melt  | rate |
decreasesby20%and30%intheNHinMarchandtheSHinSeptem-
|     |     | ber, respectively | relative           | to the   | standard | model. | This       | reduction | in     |
| --- | --- | ----------------- | ------------------ | -------- | -------- | ------ | ---------- | --------- | ------ |
|     |     | basal melt        | occurs principally | in areas | of       | thick  | ice, where | there     | is not |
muchmeltingpotentialavailabletodividebetweenbasalandlateral
|     |     | melt. Therefore, | areas of | thick ice | experience |     | less basal | melt | in the |
| --- | --- | ---------------- | -------- | --------- | ---------- | --- | ---------- | ---- | ------ |
FSTDmodelcomparedtothestandardmodel,andsoremainthicker
|     |     | throughout | the year compared | to  | the standard |     | model. | Areas | of thin |
| --- | --- | ---------- | ----------------- | --- | ------------ | --- | ------ | ----- | ------- |
ice,wherethereisahighermeltingpotential,donotexperiencethis
basalmeltreduction.
4.Discussion
Theresultspresentedheredemonstratethattheinclusionoffloesize
|     |     | information | has a significant | impact     | on  | sea        | ice concentration |          | and    |
| --- | --- | ----------- | ----------------- | ---------- | --- | ---------- | ----------------- | -------- | ------ |
|     |     | thickness,  | in agreement      | with Zhang | et  | al. (2016) | and               | Bennetts | et al. |
(2017).TheincreaseinlateralmeltduetoincludingaprognosticFSD
reducesseaiceconcentrationsinbothhemispheres,inanocean-sea
icemodelwithcyclicatmosphericforcing.Thisexpandedmodelphys-
icshasthepotentialtoalterseaicefeedbacks,climatesensitivityand
theseaiceresponsetostorms—impactswhichwillbeinvestigatedin
futurework.
|     |     | The response    | of sea ice            | concentration |             | and         | thickness | to including |          |
| --- | --- | --------------- | --------------------- | ------------- | ----------- | ----------- | --------- | ------------ | -------- |
|     |     | prognostic      | floe size information |               | in previous | studies     |           | differ       | to those |
|     |     | shown here,with | both Zhanget          |               | al. (2016)  | andBennetts |           | et al.       | (2017)   |
Figure5.AsFigure4,butforseaicevolumeperunitarea(inm). findingonlyreductionsinseaicethickness,andBennettsetal.(2017)
|     |     | finding | larger reductions | in sea | ice concentration |     | than | the | present |
| --- | --- | ------- | ----------------- | ------ | ----------------- | --- | ---- | --- | ------- |
study.Differencesbetweenmodelconfigurationsandforcingscenariosinthevariousstudiesmeanthatwe
cannotdirectlycomparetheimpactsonseaiceconcentrationandthicknessresultsatthisstage.
The sea ice model described here includes a more comprehensive description of physical processes that
affectseaicefloesizethanthoseincludedinotherstudies.ThelackofobservationsoftheFSDcoveringa
region and time period large enough for global model validation means that we cannot discern which
modelsimulatesthemostrealisticFSD.Thislackofobservationaldataispreciselywhatmotivatesourfully
prognosticapproach,ratherthanconstrainingtheFSDbasedonminimaldataasinZhangetal.(2016)and
Bennettsetal.(2017).Thatweareabletocapturesomefirst-ordercharacteristicsoftheFSDinourmodel
ROACHETAL. 4333

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
experiments,whichbeginwithoutinitializationandallowthedistributiontoevolvefreely,suggeststhatwe
have implemented some of the key physics that drive the FSD. These first-order characteristics include a
variedspatialdistributionofrepresentativeradius(Figure1),andamultiscalenumberFSD(Figures2a–2d)
inlinewithobservationalstudies(e.g.,Steeretal.,2008).
Ourprocess-basedapproachtomodeldevelopmentallowsustoexaminethecontributionofdifferentpro-
cesses to the FSD, with insights that are useful for future model development. Such results cannot be
obtainedfromreducedcomplexitymodelswhichtuneparametrizationstoreproduceacertainFSDshape
or behavior. While introducing additional uncertain parameters, we hope that consideration of individual
physicalprocesses willmotivatefurtherstudyand helpprioritizeparametersthat requirefurtherobserva-
tionalconstraints. Modelresultscouldinformdevelopmentofparametrizationsusedinsimplermodelsin
thefuture.Below,wediscussthecontributionofdifferentprocessestotheFSDandtheirrepresentationin
currentmodels,aswellashighlightingareasthatrequirefurtherwork.
We find that the freezing together of floes is a key process in determining the evolution of floe size
(Figures 2 and 3). In previous modeling studies, the choice of how to include floe merging or welding
has been ad hoc: Horvat and Tziperman (2015) do not discuss welding; Zhang et al. (2016) move all
floes into the largest category if the ice growth rate exceeds a threshold determined by tuning model
output to observations in the western Arctic; and Bennetts et al. (2017) double the floe diameter in a
grid cell if the ocean freezing potential is positive. Floe welding has only recently been quantified in
the field for the first time by Roach et al. (2018a), who found observational support for use of the
geometric floe welding model described here, but additional observations are required to better con-
strain the floe welding parameter.
Thefracture of iceby oceanwaves is also important, with preferredfracture sizes (e.g., Figure2h)driving
behaviorinthenumberFSD(e.g.,Figure2d).Wecomputethenewfloesizesgeneratedbywavefracture
explicitly, without requiring any assumptions about the FSD. In other parametrizations of wave fracture,
Zhangetal.(2016)assumethatwave-fracturediceisredistributedequallytoallothercategoriesofsmaller
size as a power law distribution. Their model depends strongly on a floe size redistribution ‘‘participation
factor,’’ which they parametrize as a function of wind speed and open water fraction, fitting tuning con-
stantsintheirmodeltocumulativenumberdistributionsobservedinsatelliteimagesinthewesternArctic.
InBennettsetal.(2017),floesfractureaccordingtoastraincriterionsimilartoours,butthechangeinthe
FSDiscalculatedassuminga‘‘splitpowerlaw’’distributionoffloessizesbasedonobservationsfromToyota
etal. (2011). Zhangetal. (2016) and Bennetts et al.(2017) impose behavior onfractured floe sizes that is
inconsistent with results from a small-scale model (Montiel & Squire, 2017) and laboratory observations
(Hermanetal.,2018),whichindicatepreferredsizesintheFSDresultingfromwavefracture.Developingor
tuning models to explicitly match ‘‘split power law’’ shapes may be misleading, as many observations do
notshowthisdistribution(e.g.,Inoueetal.,2004;Pagetetal.,2001;Wangetal.,2016).Further,observations
ofa‘‘splitpowerlaw’’distributioncouldbeinterpretedasagradualbendingofcurvesratherthananabrupt
transition(Herman,2010).
Infuturework,theseaicemodelshouldbecoupledtoafullspectrumoceanwavemodelwithanappropri-
ate treatment of wave energy damping by sea ice. There are certainly limitations with our attenuation
scheme,whichmaynotbesuitableforsmallfloes(Meylan,2002)andneglectswavedirection,unlikeBen-
nettsetal.(2017).Sensitivityofthedepthofwavepenetrationintothepackiceusingdifferentattenuation
parametrizations such as Meylan et al. (2014]) could be tested with our model, either using forcing data
fromawavemodelhindcastorcoupledtoawavemodel.Wavemodelcouplingwouldalsoallowturbulent
mixingduetooceanwavestooccurwithintheseaiceregion,influencingtheheatfluxesavailableforsea
icemeltandgrowth.Morerealisticsimulationofwavesinicecouldalsoenableadvancesintherepresenta-
tionofseaicegrowth(Roachetal.,2018a).
Thechoiceoffloesizeassignedtonewfloesstronglyimpactsthesimulatedfloenumberdistribution(Fig-
ure2).Inourmodel,newiceisplacedinthesmallestfloesizecategory,representingpancakeiceformation.
Thisresultsinlargenumbersofsmallfloesduringwinter,aseasonalityoppositetothatobtainedbyZhang
etal.(2016).Inreality,newfraziliceisherdedintopancakefloesonlyinthepresenceofsurfacewavesand/
or winds, while in the absence of wind and wave action frazil crystals freeze together to form large thin
sheetsofseaicecallednilas(Weeks&Ackley,1986).Zhangetal.(2016)donotspecifyhowtheyinitialize
ROACHETAL. 4334
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
floesizesatthestartoftheirsimulation,northefloesizesatwhichnewiceforms.Zhangetal.(2015)per-
form simple experiments that are initialized at the largest floe size. Bennetts et al. (2017) initialize their
modelusingaconstantfloediameterof300m,anddonotexplainhowtheformationofnewiceimpacts
the representative floe diameter. These models and the standard version of CICE could be considered to
includenilasgrowthonly.Incontrast,ourmodelincludespancakegrowthonly,althoughtheinitialthick-
nessoficemaycorrespondbettertonilasgrowththanpancakes.Futuremodelsshouldideallyincorporate
both nilas and pancake growth, perhaps using some critical value of the tensile stress mode arising from
thewavefield(Shenetal.,2004)todeterminewhichgrowthtypeoccurs.
Of the five processes that determine the FSD, only new ice formation and lateral melt and growth cause
changestoseaiceconcentrationinourmodel.Wefindthatlateralgrowth,whichwasnotincludedineither
Zhangetal.(2016)orBennettsetal.(2017),isaroundtwoordersofmagnitudesmalleroverallthanlateral
melt (Figures 2e–2h). Roach et al. (2018a) find that the lateral growth model used here underestimates
growthratesofsmallicefloesobservedintheArcticOceanduringfall.Moreobservationsarerequiredto
determinewhetherthemodelunderestimateslateralgrowthratesinotherconditions.
HerelateralmeltingisasignificantprocessforevolutionoftheseaiceFSD(Figures2e–2h)andisafunction
oftheFSDitself.Incontrast,thelateralmeltformulationinZhangetal.(2016)assumesallfloesizecatego-
rieshavethesameITD,anddoesnotparametrizetheeffectoflateralmeltingontheFSD(thesecondterm
inequation(14)).Bennettsetal.(2017)useasinglerepresentativefloesizeineachgridcell,neglectingthe
subgrid-scaledistributionoffloesizes,whichcouldvaryoverabroadrange.Allthreemodelsdemonstrate
thatlateralmelthaslargeimpactonsimulatedseaiceconcentration,alsomotivatingfurtherobservational
validation.AsnotedbyRoachetal.(2018b),theparametrizationoflateralmeltrateusedinourmodeland
standardCICE5.1,aswellasothermodels,isbasedonasinglefieldstudyofasinglefloe(Maykut&Pero-
vich, 1987). Further constraints on individual processes like this, which strongly impact the sea ice FSD,
couldgreatlyassistmodeldevelopment,particularlyintheabsenceofglobalobservationsoffloesizes.
5.Conclusions
Inthisstudy,wehavepresentedaschemeformodelingafullyprognosticjointseaicefloesizeandthick-
nessdistribution.Wehaveexaminedmodelresultsinbothhemispheresobtainedwithoutinitializationor
tuningparameterstoobtainaparticularfloesizedistribution,unlikepreviousstudies.Wefindthatthefive
processesimplementedhere—lateralmeltandgrowthoffloes,floeweldinginfreezingconditions,newice
formationandfractureoffloesbyoceansurfacewaves—capturesomefirst-ordercharacteristicsofthefloe
sizedistribution.
However,definitestatementsontherealismofthesimulateddistributionarehinderedbyalackofglobal
observationsoffloesizedistribution.Observationswhichcoveralargespatialandtemporalregionatsmall
enoughresolutionarenotyetavailable.Thislackofobservationsisthemotivationforconstructingamodel
which does not assume a priori distributions for simulated floe sizes. This general framework makes any
additions or modifications to physical processes straightforward to implement. Future additions may
include dynamics more appropriate for the marginal ice zone (e.g., Rynders et al., 2016), floe size-
dependent mechanical redistribution (e.g., Horvat & Tziperman, 2015), dependence of form drag on the
simulated floe size distribution, two clearly defined sea ice growth pathways (nilas and pancake growth),
andcouplingwithanoceanwavemodel.
Inspiteofourchoicestokeepmuchofthephysicsconsistentwiththestandardmodel,impactsonseaice
concentrationandthicknesscausedbytheadditionofafloesizedistributionaresignificant.Thissuggests
thatsmall-scaleprocesses associatedwithindividualfloesmaybeimportantforthepolarclimatesystem.
The observed predominance of sea ice growth via pancake formation in the Antarctic (Wadhams et al.,
1987)suggeststhattheseprocessesmaybeparticularly relevantfortheSouthernHemisphere.Moreover,
the predicted increase in the Arctic marginal ice zone (Aksenov et al., 2017) implies that processes at the
seaicefloescalemaybecomemoreimportantforsimulationofseaiceinthefuture.Themodelpresented
herecouldhelptoanswerquestionsontheseasonalevolutionoffloesizeinthepolaroceans,thepossibil-
ityofpowerlawemergencefrominteractionsatthefloescaleinaclimatemodel,andthedegreetowhich
seaicemeltingisinfluencedbyfracturedseaicecover.
ROACHETAL. 4335
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
Acknowledgments References
LRandSDwerefundedviaMarsden
contractVUW-1408.CHwassupported Aksenov,Y.,Popova,E.E.,Yool,A.,Nurser,A.J.G.,Williams,T.D.,Bertino,L.,etal.(2017).OnthefuturenavigabilityofArcticsearoutes:
bytheFrankKnoxMemorial High-resolutionprojectionsoftheArcticOceanandseaice.MarinePolicy,75,300–317.https://doi.org/10.1016/j.marpol.2015.12.027
Fellowshipduringpartsofthiswork. Bennetts,L.G.,O’farrell,S.,&Uotila,P.(2017).Briefcommunication:Impactsofocean-wave-inducedbreakupofAntarcticseaiceviather-
CMBwassupportedbytheUS modynamicsinastand-aloneversionoftheCICEsea-icemodel.TheCryosphere,11(3),1035–1040.https://doi.org/10.5194/tc-11-1035-
NationalScienceFoundationPLR- 2017
1643431.Theauthorswouldliketo Filbet,F.,&Laurenc¸ot,P.(2004).NumericalsimulationoftheSmoluchowskicoagulationequation.SIAMJournalonScientificComputing,
thankRichardGormanforproducing 25(6),2004–2028.https://doi.org/10.1137/S1064827503429132
thewavemodelhindcast,ErikBehrens Herman,A.(2010).Sea-icefloe-sizedistributioninthecontextofspontaneousscalingemergenceinstochasticsystems.PhysicalReviewE,
forsettingupthestandardmodel 81(6),66,123.https://doi.org/10.1103/PhysRevE.81.066123.
NEMO-CICEconfiguration,and Herman,A.,Evers,K.-U.,&Reimer,N.(2018).Floe-sizedistributionsinlaboratoryicebrokenbywaves.TheCryosphere,12,685–699.https://
ElizabethHunkeandananonymous doi.org/10.5194/tc-12-685-2018
reviewerfortheirconsiderationofthe Hibler,W.D.III(1980).Modelingavariablethicknessseaicecover.MonthlyWeatherReview,108(12),1943–1973.https://doi.org/10.1175/
manuscript.Theauthorsalsowishto 1520-0493(1980)108<1943:MAVTSI>2.0.CO;2
acknowledgethecontributionofNeSI Horvat,C.,&Tziperman,E.(2015).Aprognosticmodelofthesea-icefloesizeandthicknessdistribution.TheCryosphere,9(6),2119–2134.
high-performancecomputingfacilities https://doi.org/10.5194/tc-9-2119-2015.
totheresultsofthisresearch.NZ’s Horvat,C.,&Tziperman,E.(2017).Theevolutionofscalinglawsintheseaicefloesizedistribution.JournalofGeophysicalResearch:Ocean,
nationalfacilitiesareprovidedbythe 122,7630–7650.https://doi.org/10.1002/2016JC012573
NZeScienceInfrastructureandfunded Horvat,C.,Tziperman,E.,&Campin,J.-M.(2016).Interactionofseaicefloesize,oceaneddiesandseaicemelting.GeophysicalResearchLet-
jointlybyNeSI’scollaborator ters,43,8083–8090.https://doi.org/10.1002/2016GL069742
institutionsandthroughtheMinistry Hunke,E.C.,Lipscomb,W.H.,Turner,A.K.,Jeffery,N.,&Elliott,S.(2015).CICE:TheLosAlamosSeaicemodeldocumentationandsoftware
ofBusiness,Innovation& user’smanualversion5(Tech.Rep.LA-CC-06–012).LosAlamos,NM:LosAlamosNationalLaboratory.
Employment’sResearchInfrastructure Inoue,J.,Wakatsuchi,M.,&Fujiyoshi,Y.(2004).IcefloedistributionintheSeaofOkhotskintheperiodwhensea-iceextentisadvancing.
programme.Modeloutputusedinthis GeophysicalResearchLetters,31,L20303.https://doi.org/10.1029/2004GL020809
manuscriptispubliclyavailablevia JapanMeteorologicalAgency(2013).JRA-55:Japanese55-yearreanalysis,daily3-hourlyand6-hourlydata(Tech.Rep.).Boulder,CO:Japan
Zenodo(https://doi.org/10.5281/ MeteorologicalAgency.https://doi.org/10.5065/D6HH6H41
zenodo.1193929).Accesstothecode Josberger,E.G.,&Martin,S.(1981).Alaboratoryandtheoreticalstudyoftheboundarylayeradjacenttoaverticalmeltingicewallinsalt
viaaGithubrepositoryisavailable water.JournalofFluidMechanics,111,439–473.
fromthecorrespondingauthorupon Kohout,A.L.,&Meylan,M.H.(2008).Anelasticplatemodelforwaveattenuationandicefloebreakinginthemarginalicezone.Journalof
request. GeophysicalResearch,113,C09016.https://doi.org/10.1029/2007JC004434
Maykut,G.A.,&McPhee,M.G.(1995).SolarheatingoftheArcticmixedlayer.JournalofGeophysicalResearch,100(C12),24624–24703.
https://doi.org/10.1029/95JC02554
Maykut,G.A.,&Perovich,D.K.(1987).Theroleofshortwaveradiationinthesummerdecayofaseaicecover.JournalofGeophysical
Research,92(C7),7032–7044.https://doi.org/10.1029/JC092iC07p07032
Meylan,M.H.(2002).Waveresponseofanicefloeofarbitrarygeometry.JournalofGeophysicalResearch,107(C1),3005.https://doi.org/10.
1029/2000JC000713
Meylan,M.H.,Bennetts,L.G.,&Kohout,A.L.(2014).InsitumeasurementsandanalysisofoceanwavesintheAntarcticmarginalicezone.
GeophysicalResearchLetters,41,5046–5051.https://doi.org/10.1002/2014GL060809
Montiel,F.,&Squire,V.A.(2017).Modellingwave-inducedseaicebreakupinthemarginalicezone.ProceedingsoftheRoyalSocietyofLon-
donA,473,1–32.https://doi.org/10.1098/rspa.2017.0258
Paget,M.J.,Worby,A.P.,&Michael,K.J.(2001).Determiningthefloe-sizedistributionofEastAntarcticseaicefromdigitalaerialphoto-
graphs.AnnalsofGlaciology,33(1),94–100.
Perovich,D.,Richter-Menge,J.,Polashenski,C.,Elder,B.,Arbetter,T.,&Brennick,O.(2014).Seaicemassbalanceobservationsfromthe
NorthPoleEnvironmentalObservatory.GeophysicalResearchLetters,41,2019–2025.https://doi.org/10.1002/2014GL059356
Rae,J.G.L.,Hewitt,H.T.,Keen,A.B.,Ridley,J.K.,West,A.E.,Harris,C.M.,etal.(2015).DevelopmentoftheGlobalSeaIce6.0CICEconfigu-
rationfortheMetOfficeGlobalCoupledmodel.GeoscientificModelDevelopment,8(7),2221–2230.https://doi.org/10.5194/gmd-8-2221-
2015
Roach,L.A.,Dean,S.M.,&Renwick,J.A.(2018b).ConsistentbiasesinAntarcticseaiceconcentrationsimulatedbyclimatemodels.The
Cryosphere,12,365–383.https://doi.org/10.5194/tc-12-365-2018
Roach,L.A.,Smith,M.M.,&Dean,S.M.(2018a).Quantifyinggrowthofpancakeseaicefloesusingimagesfromdriftingbuoys.Journalof
GeophysicalResearch:Ocean,123,2851–2866.https://doi.org/10.1002/2017JC013693
Rothrock,D.A.,&Thorndike,A.S.(1984).Measuringtheseaicefloesizedistribution.JournalofGeophysicalResearch,89(C4),6477–6486.
https://doi.org/10.1029/JC089iC04p06477
Rynders,S.,Aksenov,Y.,Feltham,D.,Nurser,G.,&NaveiraGarabato,A.(2016).ModellingMIZdynamicsinaglobalmodel.InEGUgeneral
assemblyconference(Vol.18,1004pp.).Vienna,Austria:EGUGeneralAssembly.
Shen,H.H.,&Ackley,S.F.A.(1991).Aone-dimensionalmodelforwave-inducedice-floecollisions.AnnalsofGlaciology,15(1),87–95.
Shen,H.H.,Ackley,S.F.,&Yuan,Y.(2004).Limitingdiameterofpancakeice.JournalofGeophysicalResearch,109,C12035.https://doi.org/
10.1029/2003JC002123
Smoluchowski,M.V.(1916).ZurTheoriederZustandsgleichungen.AnnalenDerPhysik,353(24),1098–1102.https://doi.org/10.1002/andp.
19163532407
Steele,M.(1992).Seaicemeltingandfloegeometryinasimpleice-oceanmodel.JournalofGeophysicalResearch,97(C11),17729–17738.
Steer,A.,Worby,A.,&Heil,P.(2008).Observedchangesinsea-icefloesizedistributionduringearlysummerinthewesternWeddellSea.
DeepSeaResearch,PartII,55(8–9),933–942.https://doi.org/10.1016/j.dsr2.2007.12.016
Thorndike,A.S.,Rothrock,D.A.,Maykut,G.A.,&Colony,R.(1975).Thethicknessdistributionofseaice.JournalofGeophysicalResearch,
80(33),4501–4513.https://doi.org/10.1029/JC080i033p04501
Tolman,H.L.(2009).UsermanualandsystemdocumentationofWAVEWATCHIIITMversion3.14(MMABContributionNo.276).Camp
Springs,MD:EnvironmentalModelingCenter,NCEP.
Toyota,T.,Haas,C.,&Tamura,T.(2011).Sizedistributionandshapepropertiesofrelativelysmallsea-icefloesintheAntarcticmarginalice
zoneinlatewinter.DeepSeaResearch,PartII,58(9),1182–1193.https://doi.org/10.1029/10.1016/j.dsr2.2010.10.034
Wadhams,P.,Lange,M.,&Ackley,S.F.(1987).TheicethicknessdistributionacrosstheAtlanticsectoroftheAntarcticOceaninmidwinter.
JournalofGeophysicalResearch,92(C13),14535–14552.https://doi.org/10.1029/10.1029/JC092iC13p14535
ROACHETAL. 4336
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Journal of Geophysical Research: Oceans
10.1029/2017JC013692
Wang,Y.,Holt,B.,Rogers,E.,Thomson,J.,&Shen,H.H.(2016).WindandwaveinfluencesonseaicefloesizeandleadsintheBeaufortand
ChukchiSeasduringthesummer-falltransition2014.JournalofGeophysicalResearch:Oceans,121,1502–1525.https://doi.org/10.1029/
10.1002/2015JC011349
Weeks,W.F.S.,&Ackley,S.F.(1986).Thegrowth,structure,andpropertiesofseaice(Vol.146,pp.9–164).Boston,MA:Springer.https://doi.
org/10.1002/9781444317145.ch2
Zhang,J.,Schweiger,A.,Steele,M.,&Stern,H.(2015).Seaicefloesizedistributioninthemarginalicezone:Theoryandnumericalexperi-
ments.JournalofGeophysicalResearch:Oceans,120,3484–3498.https://doi.org/10.1002/2015JC010770
Zhang,J.,Stern,H.,Hwang,B.,Schweiger,A.,Steele,M.,Stark,M.,&Graber,H.C.(2016).ModelingtheseasonalevolutionoftheArcticsea
icefloesizedistribution.Elementa:ScienceoftheAnthropocene,4(1),126.https://doi.org/10.12952/journal.elementa.000126
ROACHETAL. 4337
21699291,
2018,
6,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2017JC013692,
Wiley
Online
Library
on
[22/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License
