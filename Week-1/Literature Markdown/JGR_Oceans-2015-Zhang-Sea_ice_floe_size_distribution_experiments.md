PUBLICATIONS
Journal of Geophysical Research: Oceans
RESEARCH ARTICLE Sea ice floe size distribution in the marginal ice zone: Theory
10.1002/2015JC010770 and numerical experiments
KeyPoints: JinlunZhang1,AxelSchweiger1,MichaelSteele1,andHarryStern1
(cid:2)Atheoryisdevelopedtoexplicitly
modelseaicefloesizedistribution 1AppliedPhysicsLaboratory,PolarScienceCenter,UniversityofWashington,Seattle,Washington,USA
(FSD)
(cid:2)TheFSDtheoryiscoupledwithanice
thicknessdistributiontheory Abstract Tobetterdescribethestateofseaiceinthemarginalicezone(MIZ)withfloesofvaryingthick-
(cid:2)SimulatedFSDobeysapowerlawas
nessesandsizes,bothanicethicknessdistribution(ITD)andafloesizedistribution(FSD)areneeded.Inthis
observedinsatellitedata
work,wehavedevelopedaFSDtheorythatiscoupledtotheITDtheoryofThorndikeetal.(1975)inorder
toexplicitlysimulatetheevolutionofFSDandITDjointly.TheFSDtheoryincludesaFSDfunctionandaFSD
Correspondenceto:
J.Zhang, conservationequationinparallelwiththeITDequation.TheFSDequationtakesintoaccountchangesin
zhang@apl.washington.edu FSDduetoiceadvection,thermodynamicgrowth,andlateralmelting.ItalsoincludeschangesinFSD
becauseofmechanicalredistributionoffloesizeduetoiceridgingand,particularly,icefragmentation
Citation: inducedbystochasticoceansurfacewaves.Thefloesizeredistributionduetoicefragmentationisbasedon
Zhang,J.,A.Schweiger,M.Steele,and
theassumptionthatwave-inducedbreakupisarandomprocesssuchthatwhenanicefloeisbroken,floes
H.Stern(2015),Seaicefloesize
distributioninthemarginalicezone: ofanysmallersizeshaveanequalopportunitytoform,withoutbeingeitherfavoredorexcluded.Tofocus
Theoryandnumericalexperiments, onlyonthepropertiesofmechanicalfloesizeredistribution,theFSDtheoryisimplementedinasimplified
J.Geophys.Res.Oceans,120,3484–
ITDandFSDseaicemodelforidealizednumericalexperiments.Modelresultsshowthatthesimulated
3498,doi:10.1002/2015JC010770.
cumulativefloenumberdistribution(CFND)followsapowerlawasobservedbysatellitesandairbornesur-
veys.Thesimulatedvaluesoftheexponentofthepowerlaw,withvaryinglevelsoficebreakups,arealsoin
Received6FEB2015
Accepted20APR2015 therangeoftheobservations.ItisfoundthatfloesizeredistributionandtheresultingFSDandmeanfloe
Acceptedarticleonline24APR2015 sizedonotdependonhowfloesizecategoriesarepartitionedoveragivenfloesizerange.Theabilityto
Publishedonline12MAY2015 explicitlysimulatemulticategoryFSDandITDtogethermayhelptoincorporateadditionalmodelphysics,
suchasFSD-dependenticemechanics,surfaceexchangeofheat,mass,andmomentum,andwave-ice
interactions.
1.Introduction
SignificantdeclineofArcticseaicehasbeenobservedinrecentyears[e.g.,Meieretal.,2014].Thedecline
was particularly steep during summers 2007–2013, when the Arctic sea ice extent decreased to the low-
est levels observed in the satellite era [e.g., Comiso, 2012]. Severe summer melt back leads to increasing
areas of warming open water and marginal ice zone (MIZ) [e.g., Steele et al., 2010; Strong and Rigor,
2013]. The MIZ is generally defined as a transition region from open water to pack ice with low concen-
tration,low thickness, and diffuse seaice floesof varyingshapesand sizes [Rothrock and Thorndike,1984;
Wadhams, 1986]. This is in contrast to the thicker, more compact sea ice field in the central Arctic that
appears more as a continuum with pressure ridges and leads/cracks interspersed [e.g., Wadhams, 1981;
Hibler, 2001]. The state of sea ice in a given area, whether in MIZ or the central Arctic, may be described
by an ice thickness distribution (ITD) that gives the fractions of open water/leads and various ice thick-
nesses in that area [Thorndike et al., 1975; Hibler, 1980]. The Thorndike et al. [1975] ITD theory has been
increasingly incorporated in operational forecast and climate models. However, the ITD does not give a
complete picture of the MIZ that consists of ice floes with diameters ranging from meters to kilometers.
VC2015.TheAuthors. Such a character may be represented by a floe size distribution (FSD) [Rothrock and Thorndike, 1984; Holt
Thisisanopenaccessarticleunderthe
and Martin, 2001; Herman, 2010]. Thus both FSD and ITD are needed to better capture the state of sea
termsoftheCreativeCommonsAttri-
iceintheMIZ.
bution-NonCommercial-NoDerivs
License,whichpermitsuseanddistri- The evolution of FSD in the MIZ is controlled by dynamic and thermodynamic processes. These proc-
butioninanymedium,providedthe
esses differ significantly from those in the ice pack interior, including changes in ice-albedo feedbacks,
originalworkisproperlycited,theuse
modifications in surface exchanges of heat, mass, and momentum, alterations in sea ice mechanical
isnon-commercialandnomodifica-
tionsoradaptationsaremade. behavior, and variations in oceanic heat flux. While winds and currents may cause ice to deform and
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3484

Journal of Geophysical Research: Oceans
10.1002/2015JC010770
crack, ice in the MIZ is particularly vulnerable to ocean surface waves and swell that form in the open
water, resulting from strong winds and often storms, and propagate into the ice field [Squire et al., 1995;
Squire, 2007; Kohout et al., 2014]. While the ice tends to attenuate the incoming waves because of
wave-ice interactions [Wadhams et al., 1988; Meylan et al., 2014], the waves tend to bend ice repeatedly,
and the ice breaks if the bending-induced stresses exceed its flexural strength or if the repeated bend-
ing leads to fatigue failure [e.g., Langhorne et al., 1998]. Once an ice floe is broken, it becomes floes of
smaller sizes, a process of floe size redistribution via mechanical forcing. Thus wave conditions (wave
energy, frequency, direction, etc.) and wave-ice interactions play a prominent role in determining the
magnitude of ice breakups and mechanical floe size redistribution and therefore FSD in the MIZ.
TheFSDisoftendescribedastheareaorthenumberoffloesoverarangeoffloesizes.Ameasureofthe
size of a floe is the caliper diameter defined as the average over all angles of the distance between two
parallel lines (or calipers) that are set against the floe’s sidewalls [Rothrock and Thorndike, 1984; also see
Steele,1992].AnalysesofsatelliteimagesandaerialphotographsrevealthatFSDgenerallyobeysapower
law[RothrockandThorndike,1984;HoltandMartin,2001;Toyotaetal.,2006;Steeretal.,2008].Theseanal-
yses indicate that the number of floes per unit area with caliper diameters not smaller than l, or the
(reverse)cumulativefloenumberdistribution(CFND),canbedescribedbyapowerlawfunctionN(l)/l–a,
where N(l) is the CFND and l is the caliper diameter of a floe. The significance of the power law is the
scale invariance: there is no natural length scale, and the features look the same under arbitrary magnifi-
cation. The CFND is characterized by a single exponent a over all floe sizes. The power law function is a
straight line in a log-log plot and 2a is the slope of the line. The a values are often found to vary from
1.15to2.90[RothrockandThorndike,1984;HoltandMartin,2001;Toyotaetal.,2006;Steeretal.,2008;Per-
ovichandJones,2014],indicatingvaryingmagnitudesoficebreakupsdependingonwindandwaveforc-
ingandiceconditions.
TheFSDisconsideredimportanttovariousaspectsofMIZprocesses.Forexample,FSDinfluencesmechani-
cal properties of the ice and thus its response to winds and ocean waves and currents [e.g., Shen et al.,
1987; Feltham, 2005], which is likely to modify the air-sea momentum transfer. FSD also has a significant
roleinlateralmelting[e.g.,Steele,1992].Becauselateralmeltingoccursattheperimeteroficefloes,small
floesdisappearmorequicklythanlargefloes,sincetheyhavemoreperimeterperunitarea,andthismodi-
fiestheFSD.Lateralmeltingalsoexpandstheareaofopenwatermorerapidlythantoporbottommelting.
Morerapidshrinkingoficefloeswithrelativelyhighsurfacealbedoandexpansionofopenwaterwithlow
surfacealbedowouldcausepositiveice-albedofeedbackthattendstoenhancethesurfaceabsorptionof
solarenergy, elevate ocean surface warming, and accelerate iceretreat [Perovich etal., 2007,2008;Zhang
etal.,2008].Thelateralmeltingratedependsonthetotalperimeteroficefloesoccupyingagivenarea.For
powerlawFSDs,thevalueofthetotalperimeterisverysensitivetotheexponentoftheFSD[Toyotaetal.,
2006].Thatis,thelateralmeltingrateisverysensitivetoFSD.
Significant progress has been made in modeling FSD-related MIZ processes [e.g., Dumont et al., 2011;
Williamsetal.,2013a,b].Nevertheless,muchremainstobedonetheoreticallyandnumericallytorepresent
theMIZprocessesingeneralandtoexplicitlysimulatetheevolutionofFSDinparticular.Modelingtheevo-
lutionofFSDasaprognosticstatevariableishinderedbythefactthatmanyoftheMIZprocessesarenot
wellunderstood,suchaswave-iceinteractions,wave-inducedbreakupofpackice,andmechanicalfloesize
redistribution.TheknowledgegapsinMIZprocessesmakeitdifficulttoincorporateFSDintoamodel.This
iswhymanyoftheMIZ-relevantprocessesarenotincludedinoperationalforecastorclimatemodels.For
example, to our knowledge, no large-scale sea ice models are able to explicitly simulate the evolution of
FSDin theMIZ,notto mentionsimulatingFSDandITDjointly. Thecomplexityand difficulty of capturing
theMIZdynamicandthermodynamicprocessesandthecombinedevolutionofFSDandITDposeasignifi-
cantchallengetotheoperationalforecastingandclimatemodelingcommunity.
ThisstudyismeanttobeastepforwardtowardincorporatingFSDintolarge-scaledynamicthermodynamic
seaicemodelsthatarebasedontheITDtheoryofThorndikeetal.[1975].WeintroduceaFSDtheorythatis
closelycoupledwiththeITDtheory.TheFSDtheoryincludesaFSDfunctionandanassociatedFSDconser-
vation equation to describe the sea ice system in the MIZ, in conjunction with the ITD function and the
associated ITD conservation equation. An important component of the FSD theory is the description of
mechanical redistribution of floe size due to wave-induced ice fragmentation (breakup). To assess the
behavior of the FSD theory and, particularly, the properties of its mechanical floe size redistribution, the
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3485
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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

 21699291, 2015, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     | Journal | of Geophysical |     | Research: | Oceans |     |     |     |
| --- | ------- | -------------- | --- | --------- | ------ | --- | --- | --- |
10.1002/2015JC010770
FSD conservation equation is incorporated into a simplified zero-dimensional ITD and FSD sea ice model,
whichisintegratedforaseriesofnumericalexperiments.TheFSDtheoryispresentedinsection3,aftera
brief description of the ITD equation in section 2. The design of the idealized numerical experiments is
presentedinsection4.Insection5,resultsfromtheseexperimentsareexamined.Conclusionsaregivenin
section6.
2.BriefReviewoftheITDEquation
BeforeintroducingFSDtheory,itisusefultobrieflyreviewtheThorndikeetal.[1975]ITDtheory.IntheITD
theory,theicemassconservationisdescribedbyanITDequation
|     |     |     |     | @g h52r(cid:3)ðug | @ðf h g | h Þ |     |     |
| --- | --- | --- | --- | ----------------- | ------- | --- | --- | --- |
|     |     |     |     |                   | Þ2      | 1W; |     | (1) |
|     |     |     |     | @t                | h @h    |     |     |     |
whereg h istheicethicknessdistributionfunction,tistime,uisicevelocityvector,f h isicegrowthrate,his
icethickness,andWisamechanicalthicknessredistributionfunctionforridging.Thethicknessredistribu-
|     | tionfunctionconsistsoftwotermsW5W |     |     | 0 1W,whichdescribethemechanicalchangesinITDduetoopen | r   |     |     |     |
| --- | --------------------------------- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
watercreation(W )andridging(W)thattransfersthinicetothickicecategories[Hibler,1980].Thesetwo
|     |     |     | 0   | r   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
termscanbewrittenas[Thorndikeetal.,1975;Hibler,1980]
|     |     |     |     | W   | 5ðP(cid:4)21r e_ 1e_ ÞdðhÞ |     |     | (2) |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
0 ij ij kk
and
ð1
|     |     |     |     |                              | cðh0;hÞPðh0Þg      | ðh0Þdh0(cid:5)   |     |     |
| --- | --- | --- | --- | ---------------------------- | ------------------ | ---------------- | --- | --- |
|     |     |     |     | P(cid:4)21r ij e_ ij ½2PðhÞg | h ðhÞ1             | h                |     |     |
|     |     |     |     | W5                           | 0                  |                  | ;   | (3) |
|     |     |     |     | r ð1                         | ð1                 |                  |     |     |
|     |     |     |     | ½PðhÞg                       | ðhÞ2 cðh0;hÞPðh0Þg | ðh0Þdh0(cid:5)dh |     |     |
|     |     |     |     |                              | h                  | h                |     |     |
|     |     |     |     | 0                            | 0                  |                  |     |     |
where P* is the ice strength, r is the ice stress tensor, e_ is the ice strain rate tensor, d is the Dirac delta
|     |     |     |     | ij  | ij  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
function,Pistheredistributionprobabilityfunctionspecifyingwhichcategoriesoficeparticipateinridging,
and cðh0;hÞ is a redistributor of the ITD. The redistribution probability function P is formulated such that
[Thorndikeetal.,1975;Hibler,1980]
ðh
ðh0Þdh0=cÞ;0(cid:5);
|     |     |     |     | PðhÞ5max½ð12 | g h | r   |     | (4) |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
0
whereconstantc r isaparticipationfactorthatspecifiesanareafractionofthinicetoparticipateinridging.
Asshownin(1),theThorndikeetal.ITDtheoryassumesthatchangesintheITDareduetoiceadvection,
thermodynamicgrowthordecay,leadopening(openwatercreation),andridging.TheITDtheoryisaug-
mented by an ice enthalpy distribution theory to conserve thermal energy of ice [Zhang and Rothrock,
2001,2003].Thethicknessandenthalpydistribution(TED)seaicemodelcanbeusedtointegrateovermul-
tiple subgrid categories each for ice thickness and ice enthalpy [e.g., Zhang et al., 2012]. The TED sea ice
modelintegrationalsoincludesmultiplecategoriesofsnowdepthfollowingFlatoandHibler[1995;alsosee
ZhangandRothrock,2003].
3.TheoryofFSD
ToderiveaFSDequation,wefirstdefineFSDasthefractionofareacoveredbyicefloeswithacaliperdiam-
eterbetweenlandl1dl,suchthat
l1dl
ð 1
|     |     |     |     |     | gðlÞdl5 rðl;l1dlÞ; |     |     | (5) |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
l l
R
l
whereg istheFSDfunction,listhecaliperdiameter,RisthetotalareaofsomefixedregionXaboutthe
l
pointofinterest,andr istheareainXcoveredbyopenwaterandicefloeswithcaliperdiametersbetween
l
landl1dl.Integrating(5)overallfloesizesgives
| ZHANGETAL. |     |     | MODELINGFLOESIZEDISTRIBUTION |     |     |     |     | 3486 |
| ---------- | --- | --- | ---------------------------- | --- | --- | --- | --- | ---- |

 21699291, 2015, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     | Journal | of Geophysical | Research: | Oceans |     |     |
| --- | ------- | -------------- | --------- | ------ | --- | --- |
10.1002/2015JC010770
1
ð
|     |     |     |     | gðlÞdl51: l |     | (6) |
| --- | --- | --- | --- | ----------- | --- | --- |
0
We consider that FSD, like ITD, is subject to changes caused by ice advection, thermodynamic growth or
decay, lead opening, and ridging. With a focus on the MIZ, we further consider that FSD is subject to
changesduetofragmentationinducedbywavesandswellintheMIZ.Thus,wecanderiveamathematical
equationtodescribetheFSDevolutionintheMIZsuchthat
|     |     |     | @g               | @ðfgÞ |       |     |
| --- | --- | --- | ---------------- | ----- | ----- | --- |
|     |     |     | l52r(cid:3)ðugÞ2 | l     | l 1U; | (7) |
|     |     |     | @t               | l @l  |       |     |
wheref istherateofchangeinfloesize(caliperdiameterl)andUisthemechanicalfloesizeredistribution
l
function.Thesecondtermin(7)describesthechangeinFSDduetoiceadvection.Thethirdtermdescribes
thechangeinFSDduetothermodynamicgrowthordecayrepresentedbyfreezingorlateralmelting.The
fourthterm,themechanicalfloesizeredistributionfunction,describesthechangeinFSDduetoopenwater
creationorleadopening,ridging,andfragmentation.
A
The mechanical floe size redistribution function is subject to a strong constraint. By integrating each
termin(7)overallfloesizesandrecalling(6),wecanobtain
1 ð
|     |     |     |     | Udl5r(cid:3)u: |     | (8) |
| --- | --- | --- | --- | -------------- | --- | --- |
0
Theintegralofthethirdtermin(7)representsthechangeoftotalarea(openwaterandice)bythermody-
namicswhichmustbezero[Thorndikeetal.,1975].Theconstraintimposedby(8)allowsthemodeltocon-
serveareasoficeandopenwaterduringaneventoficedeformationoricebreakup.
ThefloesizeredistributionfunctionmaybeseparatedintothreetermsU5U 1U 1U,representingthe
0 r f
mechanicalchangesinFSDduetoopenwatercreation(U ),ridging(U),andwave-inducedicefragmenta-
|     |     |     |     | 0   | r   |     |
| --- | --- | --- | --- | --- | --- | --- |
tion (U), respectively. In order to be consistent with the open water creation term in the ITD theory (see
f
|     | (2)),U | 0 mustbegivenas |                 |               |     |     |
| --- | ------ | --------------- | --------------- | ------------- | --- | --- |
|     |        |                 | U 5ðP(cid:4)21r | e_ 1e_ ÞdðlÞ: |     | (9) |
|     |        |                 | 0               | ij ij kk      |     |     |
Equation(9),togetherwith(2),ensuresthattheamountofopenwatercreatedisthesameinbothITDand
FSDequations.
To deriveU,we assume that, in each grid cell,all floes of different sizes have thesame ITD. Thisis likely
r
truewhenalargefloeisbrokenintosmallerfloesbywaves.(Observationsareneededtotestthisassump-
tion).Thisassumptionsuggeststhatridgingreducestheareafractionsofallfloesequally.Wealsoassume
thatridging-inducedicethicknessredistributionallcontributestothechangesintheareafractionsoffloes
orFSD.Fromtheseassumptionsorsimplifications,wecanderive
ð1
|     |     |     | U5 Wdh(cid:3)g52P(cid:4)21r |     | e_ g;   | (10) |
| --- | --- | --- | --------------------------- | --- | ------- | ---- |
|     |     |     | r r                         | l   | ij ij l |      |
0
wheretheintegralofW overallicethicknessesresultsin2P(cid:4)21r e_ ,when(3)isconsidered.
r ij ij
TheicefragmentationtermU isalsosubjecttoaconstraint.Becausethereisnochangeintotalareawhen
f
iceisfractured,itmustsatisfy
ð1
|     |     |     |     | U dl50: |     | (11) |
| --- | --- | --- | --- | ------- | --- | ---- |
f
0
Toderivetheicefragmentationterm,weconsiderthatarearedistributionoccursduringicebreakupsuch
thattheareaofagivenfloesizecategorylosessomeamounttootherfloesizecategoriesandatthesame
timegainssomeamountfromothercategories.Thiscanbedescribedby
ð1
bðl0;lÞQðl0Þgðl0Þdl0;
|     |     |     | U f 52QðlÞgðlÞ1 l |     | l   | (12) |
| --- | --- | --- | ----------------- | --- | --- | ---- |
0
| ZHANGETAL. |     | MODELINGFLOESIZEDISTRIBUTION |     |     |     | 3487 |
| ---------- | --- | ---------------------------- | --- | --- | --- | ---- |

Journal of Geophysical Research: Oceans
10.1002/2015JC010770
where Q(l) is the redistribution probability function specifying whether ice fragmentation takes place and
whatcategoriesaretoparticipateinthebreakupprocesses,andb(l ,l )isaredistributorofFSD.Similarto
1 2
theredistributorofITDc(h ,h )in(3),theredistributorofFSDb(l ,l )specifieshowiceistransferredfrom
1 2 1 2
onefloe sizecategoryto another bybreaking, andb(l ,l )dl can betakenasthearea ofice putinto the
1 2 2
floesizeinterval[l ,l 1dl ]whenaunitareaoficeoffloesizel isusedup.Tosatisfy(11),bissubjectto
2 2 2 1
thefollowingconstraint:
ð1
bðl0;lÞdl51: (13)
0
Once(11)issatisfied,(8)isautomaticallysatisfied,whichcanbeverifiedbytheintegralofU 1U 1U over
0 r f
allfloesizes.
TheredistributorofFSDbisanunknownintheredistributiontheory,exceptthatitmustsatisfy(13)mathe-
matically.However,satelliteimagesandaerialphotographsoficefloesofvaryingsizes[e.g.,Rothrockand
Thorndike,1984;HoltandMartin,2001;Steeretal.,2008;Toyotaetal.,2006,2011]indicatethaticefragmen-
tationcausedbystochasticoceansurfacewavesislikelytobearandomprocesssuchthatwhenapieceof
iceisbroken,itislikelytobecomefloesofanysizesmallerthantheoriginalfloesize.Noparticularsizecate-
goryisfavoredagainstothersizecategoriesduringthebreakupprocesses.Inotherwords,whenanareaof
a given floe size category is destroyed, the area is redistributed equally to all other categories of smaller
size.Thisleadsustoconstructaredistributorthatallowstheareaofagivenfloesizel tobetransferredto
1
theareaofanyfloesizel betweenc l andc l duringbreakupsuchthat
2 11 21
( 1=ðc l 2c l Þ; if c l (cid:6)l (cid:6)c l
21 11 11 2 21
bðl ;l Þ5 (14)
1 2
0; if l <c l orl >c l
2 11 2 21
wherec andc arethelower-endandhigher-endfloesizeredistributioncutoffconstants,respectively.
1 2
Thefloesizeredistributioncutoffconstantssatisfy0<c <c <1toreflectthefactthat,whenicefragmen-
1 2
tationoccurs,biggerfloesarebrokenintosmallerones.Todeterminethevaluesoftheseconstants,werely
ontheassumptionthaticebreakupandtheensuingfloesizeredistributionisarandomprocessthatdoes
notfavororexcludeanysizecategories.Thisassumptionrequiresthatwhenfloesofanysizearebroken,
floesofanysmallersizesmustbeabletoform.Inotherwords,inaseaicemodelthatinvolvesafinitenum-
beroffloesizecategories,theminimumsizeconsideredinthemodelmustbeabletoform.Thissuggests
thatc 5l /l ,wherel isthecenterofthesmallestsizecategoryinthemodelandl isthatofthe
1 min max min max
largest size category. Furthermore, for simplicity we allow c 51 – c to ensure that a range of other floe
2 1
sizecategorieswouldalsobenefitfromthebreakup.
Asmentionedabove,theredistributionprobabilityfunctionQin(12)specifieswhethericebreaksand,ifso,
whichcategoriesaretoparticipateintheredistributionofFSD.Itisanotherunknownintheredistribution
theory. However, the use of the redistribution probability function P for ridging in (4) suggests that Q be
givenby
ð1
QðlÞ5max½ð12 gðl0Þdl0=c Þ;0(cid:5); (15)
l b
l
where constant c is a participation factor that specifies an area fraction of ice to participate in breaking.
b
Here weconsider therange of the participation factor generally to be 01(cid:6)c <1, where 01 is a positive b
number approaching zero, say, 10212. When c 501, Q becomes zero, and no ice fragmentation occurs.
b
Whenthevalueofc isgreaterthan01,itallowsanareafractionoficetobreakandtoparticipateinthe
b
redistributionofFSD.
While describing two different physical processes, the formulas for P and Q are similar in form. However,
when ridging occurs, P gives a higher probability for thinner ice to transfer to thicker ice. When breakup
occurs, on the other hand, Q gives a higher probability for ice of larger sizes to transfer to ice of smaller
sizes.Infact,(15)specifiesthatac areafractionoficewiththelargestfloesizesispreferentiallyfragmented b
duringabreakupevent.Thispreferenceisbasedonfieldobservationsormodelanalysesthatwhenwaves
propagate into ice, larger floes are easier to break because they are subject to larger flexure-induced
stresses or strains, while smaller floes are likely to ride with waves with little bending [e.g., Meylan and
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3488
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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

 21699291, 2015, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     | Journal | of  | Geophysical | Research: | Oceans |     |     |     |
| --- | ------- | --- | ----------- | --------- | ------ | --- | --- | --- |
10.1002/2015JC010770
|     |     |     |     |     | Squire, 1994; | Squire et | al., 1995]. | It is also |
| --- | --- | --- | --- | --- | ------------- | --------- | ----------- | ---------- |
Table1.TheLowerandUpperLimits,Widths,andCenters,Allinm,of
|     |     |     |     |     | based on | simple reasoning: | in a given | area |
| --- | --- | --- | --- | --- | -------- | ----------------- | ---------- | ---- |
theFloeSizeCategoriesPartitionedFollowingaGaussianDistributiona
Category Lower Upper under the forcing of waves, winds, and cur-
Number Limit Limit Width Center rents,largerfloeshavehigherarealcoverage
|     |     |     |          |     | and therefore | higher | probability | to break |
| --- | --- | --- | -------- | --- | ------------- | ------ | ----------- | -------- |
|     |     | 1   | 20.1 0.1 | 0.2 | 0.0           |        |             |          |
2 0.1 10.2 10.1 5.2 than smaller floes, assuming all floes have
|     |     | 3   | 10.2 40.2    | 30.0  | 25.2 thesameITD.             |                     |               |         |
| --- | --- | --- | ------------ | ----- | ---------------------------- | ------------------- | ------------- | ------- |
|     |     | 4   | 40.2 99.8    | 59.6  | 70.0                         |                     |               |         |
|     |     | 5   | 99.8 199.1   | 99.3  | 149.5                        |                     |               |         |
|     |     |     |              |       | Thus,theparticipationfactorc |                     | b intheredis- |         |
|     |     | 6   | 199.1 347.9  | 148.8 | 273.5                        |                     |               |         |
|     |     |     |              |       | tribution                    | probability         | function Q    | plays a |
|     |     | 7   | 347.9 556.0  | 208.1 | 451.9                        |                     |               |         |
|     |     |     |              |       | prominent                    | role in determining |               | whether |
|     |     | 8   | 556.0 833.1  | 277.1 | 694.5                        |                     |               |         |
|     |     | 9   | 833.1 1189.2 | 356.1 | 1011.2                       |                     |               |         |
wave-inducedicefragmentationtakesplace
|     |     | 10  | 1189.2 1633.9 | 444.7 | 1411.5   |               |              |          |
| --- | --- | --- | ------------- | ----- | -------- | ------------- | ------------ | -------- |
|     |     |     |               |       | and what | area fraction | of ice floes | of large |
|     |     | 11  | 1633.9 2176.8 | 542.9 | 1905.3   |               |              |          |
12 2176.8 2827.7 650.9 2502.2 sizes is allocated to participate in the
mechanicalfloesizeredistribution.Needless
aFloesizeisdescribedbycaliperdiameterl.
|     |     |     |     |     | tosay,thevalueofc | dependsonwavecon- |     |     |
| --- | --- | --- | --- | --- | ----------------- | ----------------- | --- | --- |
b
|     |     |     |     |     | ditions, | which in turn | depend | on wind |
| --- | --- | --- | --- | --- | -------- | ------------- | ------ | ------- |
speedandfetch(thedistanceofopenwateroverwhichwindsisblowing)[e.g.,Squireetal.,1995;Thomson
andRogers,2014].Italsodependsonseaiceconditionsbecausewavepropagationandattenuationunder
iceareaffectedbyITDandFSDwhichalsocontroltheflexuralstrengthandhencethebendingfailureof
seaiceintheMIZ[Wadhamsetal.,1988;Squireetal.,1995,2009;KohoutandMeylan,2008;Dumontetal.,
2011;Meylanetal.,2014].Inotherwords,thevalueofc isafunctionofITD,FSD,waves,andwave-iceinter-
b
actions.Inparticular,undercertainconditionssuchascalmwinds,smallwaves,oriceofsufficientlystrong
wouldbesetto01toreflectthefactthatnoicebreakupoccurs.
|     |     | flexuralstrength,thevalueofc | b   |     |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
4.NumericalExperiments
In this study, we donot attempt to quantify therelationship between theparticipation factor c and ITD,
b
FSD, waves, and wave-ice interactions. Rather, through a series of simplified numerical experiments, we
exploretheFSDtheory’sbehaviorinmechanicalfloesizeredistributionandresultingFSDinvariousideal-
izedscenariosoficefragmentationassociatedwithdifferentvaluesofc .Thisgivesaqualitativepictureof
b
whetherthetheoryanditsnumericalimplementationareabletocreatefeaturesoficefloesoftenobserved
intheMIZ.Itwouldalsogiveuscluesaboutthepossiblerangeofc valuesintherealworldundervarying
b
seaiceandwindandwaveforcingconditions.Wealsoexploreotherpropertiesofthemechanicalfloesize
redistribution in the FSD theory, including model sensitivity to the partition of the floe size categories, to
|     |     | thefloesizeredistributioncutoffconstantc |     | ,andtoridgingandopenwatercreation. |     |     |     |     |
| --- | --- | ---------------------------------------- | --- | ---------------------------------- | --- | --- | --- | --- |
1
Inordertofocusonthepropertiesofmechanicalfloesizeredistributionduetowave-inducedicefragmentation,
theiceadvection(thesecond)andthermodynamic(third)termsin(7)areignored.Futureworkneedstocon-
sideradvectiveandthermodynamiccontributions.Thesimplified(7)(withoutadvectionandthermodynamics)is
thenimplementednumericallyinanidealizedzero-dimensionalITDandFSDseaicemodelwhichaimsonlyat
theprocessesofmechanicalfloesizeredistributiondescribedbyU.Inthenumericalexperimentswiththeideal-
izedseaicemodel,theITDequation(1)isnotactuallycomputed.However,weassume(1)providestheareafrac-
tionofopenwaterandridgingterm(W)fortheintegrationofthesimplified(7).Thenumericalimplementation
of (7) requires discretization in the floe size (l) domain to create floe size categories. To examine the model
behaviorwiththepartitionoffloesizecategories,(7)isdiscretizedintheldomainfollowingtwopartitions.
Partition 1 has M512 floe size categories, partitioned following a Gaussian distribution [see Hibler, 1980,
AppendixC]toobtainafloesizemeshthatvariessmoothlyinspace(Table1).HereMisthetotalnumberof
categoriesusedinthemodel.Usingthismethod,thewidthsandcentersofthefloesizecategoriesincrease
towardthehighendofthepartitionfollowingtheGaussiandistribution.Thefirstfloesizecategoryhasazero
center,l 50,representingtheopenwatercategory(Table1).Thesecondfloesizecategoryhasthesmallest
1
nonzero center, l 5l 55.2 m. The 12th category, or category M, has the largest center,
2 min
l 12 5l max 52502.2m.Thus,using12categories,Partition1isabletoresolverelativelysmallfloeswhileinclud-
inglargefloesupto(cid:7)2.5kmincaliperdiameter.Asshowninsection3,thecentersofthesmallestandlargest
categories(categories2andM)areusedtodeterminetheredistributioncutoffconstantc in(14).
1
| ZHANGETAL. |     |     | MODELINGFLOESIZEDISTRIBUTION |     |     |     |     | 3489 |
| ---------- | --- | --- | ---------------------------- | --- | --- | --- | --- | ---- |

Journal of Geophysical Research: Oceans
10.1002/2015JC010770
Someobservationalstudiespartitionedfloesizecategorieswithauniformwidth[e.g.,RothrockandThorn-
dike,1984].ThisisfollowedforPartition2whichhasM528floesizecategories.Withtheexceptionofthe
first category that is the same as Partition 1 for open water, all the other categories with Partition 2 are
specifiedtohaveauniformwidthof100m.Asaresult,thesecondfloesizecategoryhasthesmallestcen-
ter, l 5l 550.1 m, while the 28th category (category M) has the largest center, l 5l 52650.1 m.
2 min 28 max
ThismeansthatthefloesizerangecoveredbyPartition2isclosetothatcoveredbyPartition1whoselarg-
estcategorycenterisl 52502.2m,asshownabove.AlthoughPartition2hasmorecategories,itsl is
max min
almost10timeslargerthanthel inPartition1,thushavingacoarserresolutionforsmallfloesandlarger
min
redistributioncutoffconstantc .Bothpartitionsareimplementedinthesimplified(7)foraseriesofideal-
1
izednumericalexperimentslistedbelow:
1.Toexaminethemodelsensitivitytovaryingvaluesofparticipationfactorc ,representingvaryingmagni-
b
tudes of ice breakups, the model is integrated with three different values of c 50.05, 0.10, and 0.50,
b
whichremainunchangedinallicebreakupevents(section5.1).
2.Additionalexperimentsrelatedtoc areconductedtomimicvaryingfragmentationscenariosthatmight
b
occurinthewakeofstorms,inwhichthevaluesofc decreaseinsomebreakupeventsbecauseof,for
b
example,weakeningwinds(section5.2).
3.Toexaminethemodelsensitivitytovaryingdegreesofridgingdescribedin(10),twonumericalexperi-
mentsareconducted.OneassumesthatinagivenMIZareathereisa10%reductioniniceareadueto
ridging,andtheother20%(section5.3).
4.Toexaminethemodelsensitivitytovaryingredistributioncutoffconstantc ,twomorenumericalexperi- 1
mentsareconductedinwhichc ischosentobel /l andl /l ,respectively(section5.4).
1 3 max 4 max
5.Results
In all the numerical experiments mentioned above, the simplified (7) (without advection and thermody-
namics) is integrated over a succession of ice breakup events, with the initial ice floe condition specified
toconsistofonlythosewithincategoryMwithacenterofl .Otherinitialicefloeconditionsarepossi-
max
ble,suchasthosewithfloesinanumberofcategories.However,inthesimplifiednumericalexperiments,
we are focusing on the spring-to-summer breakup of the ice, when the ice cover often starts out as one
big plate and breaks into pieces under mechanical forcing. Different ice floe conditions are represented
in the evolution of FSD associated with the succession of ice breakups. The ice breakup events are
assumed to occur in a typical, fixed MIZ area, which consists of a fraction of open water, with the rest
covered by sea ice. Here for simplicity the area fraction of open water is fixed to be a constant of 0.2 for
all numerical experiments. This number was chosen based on Doble and Bidlot [2013] who use it as a
threshold below which pack ice is allowed to break in their wave model simulations. Note, however, that
choosing a different area fraction of open water does not fundamentally change the outcome of the
experiments.
5.1.ModelBehaviorWithVaryingParticipationFactorsandPartitionsofFloeSizeCategories
Figure1showschangesinFSDafter varyingnumbersoficebreakupeventsfromthoseexperimentsthat
use different values of participation factor c .After thefirst ice breakup (black colorin Figure1), thearea
b
fractionofthefloesincategoryM,withacenterofl ,isreducedfromtheinitialvalueof0.8.Therateof
max
decreasedepends onthelevelsof ice fragmentationrepresented by differentvalues ofc used.The area
b
lost in category M is redistributed to other categories of smaller sizes. In the following breakups (colors
otherthanblackinFigure1),theareaincategoryMcontinuestoshrink,redistributedfurthertoothercate-
gories.Meanwhilesomeareasofothercategoriesthatalsohavefloesofrelativelylargesizes,suchascate-
goriesM21andM22,arealsotransferredtothoseofsmallersizes.
As more breakups occur, the area fraction of category M would be depleted, followed by category M21,
category M22, and so on (Figure 1). Eventually, the region would be dominated by those categories of
smallerfloesizes.Thisisillustratedbythecaseofc 50.5thatrapidlyredistributesfloesizefromthehigh
b
endofFSDtothelowerend(Figures1cand1f).Infact,theicefieldisleftwithonlythosefloesincategory
2,thesmallestfloesallowedinthemodel,after(cid:6)30breakups.Forsmallerlevelsoffragmentation(c 50.05
b
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3490
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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
10.1002/2015JC010770
Figure1.FSDinareafraction,gDl,aftervaryingnumbersoficebreakups,calculatedwithdifferentfloesizecategorypartitionsandparticipationfactorsoffloesizeredistribution.Black,
l
blue,green,yellow-green,andredlinesandcirclesrepresentthefirst(initial),10th,20th,30th,and40thicebreakup,respectively.Theareafractionofopenwatercategory(l1 50)isnot
plotted.
and0.10),additionalbreakupsarenecessarytoreachthestageinwhichfloesbecomesmallenoughtobe
allincludedincategory2.
Becausethecenterandwidthofcategory2withPartition1aresmallerthanthosewithPartition2(section
4),thecaseofPartition1generallyneedsmorebreakupstoreachthatstageinwhichareasoffloesofdiffer-
ent sizes are all redistributed into category 2. Using c 50.5, for example, it takes (cid:7)30 breakups with the
b
case of Partition 1 to reachthat stage (Figure 1c,red coloroverlappinggreen-yellow color), whileit takes
(cid:7)20breakupswiththecaseofPartition2(Figure1f,redcoloroverlappinggreenandgreen-yellowcolors).
Oncereachingthatstage,thecaseofPartition1wouldhavefloeswithameansizeof(cid:7)5m,whilethecase
ofPartition2wouldhavefloeswithameansizeof(cid:7)50m.
Note that in the case of Partition 1, whenthe area of thelargest category, category M, is reduced dueto
fragmentation,mostofthelostareaisredistributedtothesecondlargestcategory,categoryM21(Figures
1a–1c).IfthereisarealostincategoryM21,mostofitistransferredtocategoryM22,andsoon.WithParti-
tion 2, on the other hand, area lost in a category benefits all categories of smaller sizes almost equally
becauseoftheuniformwidthofthefloesizecategorypartition(Figures1d–1f).Thisbehaviorreflectsthe
principleintheFSDtheorythatwhenafloeisbroken,itdisintegratesintofloesofanysizesmallerthanthe
originalsizewithoutfavoringorexcludinganyparticularsize.AlthoughappearingdifferentfromPartition2,
themechanicalfloesizeredistributionwithPartition1doesnotviolatethisprinciplebecausethewidthsof
its categories increase toward the high end of the partition, with wider categories gaining more area (or
morefloes)thannarrowonesinabreakupevent.
CorrespondingtoFigure1,Figure2showschangesin(reverse)cumulativeFSDaftervaryingnumbersofice
breakupevents.ThecumulativeFSD(CFSD)isdefinedastheareadistributionoffloeswithcaliperdiameter
notsmallerthanl,orCFSD5
Ð1gðl0Þdl0.UnlikeFSDcurves(Figure1),CFSDcurvesdifferlittleinappearance
l l
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3491
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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
10.1002/2015JC010770
Figure2.SimilartoFigure1,butwithcumulativeFSDinareafraction.
betweenthetwosetsofpartitioncases(Figure2).ThisisbecauseCFSDisanintegrationofFSDandtherefore
doesnotdependonthewidthsofthecategories,whileFSD(inareafractiondescribedbygDl)does.
l
Corresponding to Figures 1 and 2, Figure 3 shows changes in CFND or N after varying numbers of ice
breakupevents.CFNDisnotamodelprognosticvariable,butadiagnosticparametercalculatedbasedon
FSD,suchthatNðlÞ5 Ð1gðl0Þ=ð0:66l02 Þdl0,where0.66l2istheareaofafloewithcaliperdiameterlfollowing
l l
RothrockandThorndike[1984].Thelog-logplotsinFigure3indicatethatthesimulatedCFNDcurvesmostly
obeyapowerlaw,whetherafteraninitialbreakup(blackcolor),oraftervaryingnumbersofbreakupevents
(colorsotherthanblack),witheitherpartitioncases.Thisqualitativelyagreeswithobservations[e.g.,Roth-
rockandThorndike,1984;HoltandMartin,2001;Toyotaetal.,2006;Steeretal.,2008].Thisisalsoconsistent
withthepowerlawbehaviorsinsomerandom-breakingmodels[e.g.,Newman,2005].Ourpowerlawmodel
resultsareadirectconsequenceofthebreakupschemethatredistributeslargefloestosmallerfloes.
Excepttheinitialbreakup(blackcolor),theCFNDcurvesgenerallyshowasteeperdescentatornearthehigh
endofthefloesizerange(Figure3).This‘‘falloff’’fromapowerlawinthemodelisduetodecreasingnumber,
andultimatelydisappearance,offloesoflargesizesasicecontinuestobreak.ObservationsofCFNDoftenshow
asteeperdescentalso,whichislikelyduetothesamereasonorduetolimitationsofdatasampling[Pickering
etal.,1995;BurroughsandTebbens,2001;Luetal.,2008].AsteeperdescentinCFNDatthehighendofthefloe
sizerangemaybedescribedbyanuppertruncatedpowerlaw[Pickeringetal.,1995;BurroughsandTebbens,
2001;Luetal.,2008].Awayfromthefalloffzones,themodelsimulatedCFNDcurvesfollowapowerlawwithgen-
erallystraightlinesofvaryingslopes,dependingonparticipationfactorsandfloesizecategorypartitions.
Becausethepropertyofapowerlawisuniquelydefinedbytheabsolutevalueofitsexponenta(orslopein
log-log space), here we examine a to assess the behavior of the simulated power law. Figure 4 shows
changesinslopeinaseriesofconsecutiveicebreakupevents.Toavoidthefalloffzonesasmuchaspossi-
ble,theslopeineachcaseiscalculatedoverthefirstfourfloesizecategories(categories2–5)ifthereareat
least five categories (categories 2–6) that have floes (not depleted). In other words, as the categories of
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3492
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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

 21699291, 2015, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     | Journal | of Geophysical | Research: | Oceans |     |
| --- | ------- | -------------- | --------- | ------ | --- |
10.1002/2015JC010770
Figure3.SimilartoFigure1,butwithcumulativefloenumberdistribution(CFND,N).
Figure4.Changesinainasuccessionoficebreakups,calculatedusingdifferentfloesizecategorypartitionsandparticipationfactorsoffloesizeredistribution.
| ZHANGETAL. |     | MODELINGFLOESIZEDISTRIBUTION |     |     | 3493 |
| ---------- | --- | ---------------------------- | --- | --- | ---- |

Journal of Geophysical Research: Oceans
10.1002/2015JC010770
Figure5.Changesinmeancaliperdiameterinasuccessionoficebreakups,calculatedusingdifferentfloesizecategorypartitions,andparticipationfactorsoffloesizeredistribution.
largefloesaredestroyedonebyoneintheconsecutivebreakupevents,theslopecalculationstopswhen-
evercategory6hasnofloes.ThisiswhymostofslopecurvesstopshortinFigure4.Thecalculatedslope
values generally fall into the range of 1.15–2.90 found by observational studies [Rothrock and Thorndike,
1984;HoltandMartin,2001;Toyotaetal.,2006;Steeretal.,2008;PerovichandJones,2014].Forsmallerlevels
offragmentation(c 50.05and0.10),theslopevaluesarebelow1.0inthefirstfewbreakupeventsbefore
b
climbingabove1.0(Figures4a,4b,4d, and4e).For astrong levelof breakup(c 50.50), theslopevalues
b
areclosertoorabove1.0rightafterthefirstbreakupandwouldincreaserapidlyafterward,butstillremain-
ingbelow2.0or2.5withintheobservationalrange(Figures4cand4f).
Figure 5 shows the evolution of mean floe size or caliper diameter in a series of consecutive ice breakup
events. Here mean floe size is defined by l 5
Ð1gðlÞldl.
Like mean ice thickness h 5
Ð1g
ðhÞhdh, mean
m 0 l m 0 h
floesizeisanimportantmeasure,inadditiontoFSD,todescribevariablefloesizesinagivenarea.Asice
continuestobreak,l decreases,approachingthecenterofcategory2(l )atavaryingpace,dependingon
m 2
thelevelofeachbreakupevent.Ultimately,theicefieldisleftwiththesmallestfloeswithincategory2.
Animportantfeatureisthattheevolutionofthemeanfloesizel ineitherpartitionisbasicallythesame
m
(two curves almost overlapping in each panel of Figure 5). This indicates that the simulation of floe size
redistributionandtheresultingFSDandmeanfloesizedonotdependonfloesizecategorypartitions,as
longasthefloesizerangescoveredbythepartitionsareaboutthesame.Infact,ifweregrouptheFSDscal-
culatedwithPartition1(Figures1a–1c)intothecategoriesofPartition2,theregroupedFSDswouldbesim-
ilartothosecalculatedwithPartition2(Figures1d–1f).Thisisnottrue,however,ifthefloesizerangesin
thesetwopartitionsdiffersubstantially.
5.2.ModelSensitivitytoVaryingBreakupScenariosintheWakeofaStorm
Therapidfloesizeredistributionwithc 50.50isanindicationofstrongfragmentation(Figures1–5),whichis
b
mostlikelytooccurduringstorms.Hereweconductthreenumericalexperimentstomimicdifferentbreakupsce-
nariosthatmightoccurinthewakeofastorm.Intheseexperiments,theinitialbreakupisallcalculatedwiththe
valueofc 50.5,representingalarge-scalebreakupeventattheheightofastorm.However,thevalueshould
b
decreaseafterwardtorepresentpossiblechangesintheair-ice-oceanconditionsintheaftermathofastorm,such
asreducedwindsorwavesandsmallerfloesthataresubjecttolessbending.Inthefirstexperimentofvaryingc b
(calledV1here),thesecondthroughfourthbreakupsarecalculatedwithc valuesof0.4,0.3,and0.2,respectively,
b
andallthefollowingbreakupsarecalculatedwith0.1.Inthesecondexperiment(V2),thesecondthroughfifth
breakupsarethesameasV1,butallthefollowingbreakupsarecalculatedwithavalueof0.05.Inthethirdexperi-
ment(V3),thesecondthroughsixthbreakupsarethesameasV2;afterthat,nobreakupsareallowedbysetting
c 501.SincetheevolutionofmeanfloesizeintheFSDtheorydoesnotdependonfloesizecategorypartitions
b
(Figure4),onlyPartition1isusedintheseexperimentsaswellasthosepresentedinfollowingsections.
Withvaryingvaluesofc mimickingthedifferentfragmentationscenariosinthewakeofastorm,theslope b
curvesfromthesethreecasesdriftapartafteraninitialoverlap(Figure6).ItisexpectedthatV1hasalargest
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3494
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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

 21699291, 2015, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770, Wiley Online Library on [22/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     | Journal | of Geophysical |     | Research: | Oceans |     |     |     |     |
| --- | ------- | -------------- | --- | --------- | ------ | --- | --- | --- | --- |
10.1002/2015JC010770
|     |     |     |     |     | slope than | the other | two cases | because | of the largest |
| --- | --- | --- | --- | --- | ---------- | --------- | --------- | ------- | -------------- |
c value(0.1)usedforthefollow-upbreakupsafterthe
b
|     |     |     |     |     | storm. However, | most | of the | slope values | stay above |
| --- | --- | --- | --- | --- | --------------- | ---- | ------ | ------------ | ---------- |
1.0andbelow1.3.TheV3caseisofparticularinterest.
|     |     |     |     |     | This is because | it                   | shows the      | model is       | able to prevent |
| --- | --- | --- | --- | --- | --------------- | -------------------- | -------------- | -------------- | --------------- |
|     |     |     |     |     | ice breakup     | from                 | happening,     | as designed    | in the FSD      |
|     |     |     |     |     | theory, through | the                  | redistribution | probability    | function        |
|     |     |     |     |     | Q with          | a zero participation |                | factor. This   | allows the      |
|     |     |     |     |     | model to        | effectively          | handle         | the conditions | under           |
|     |     |     |     |     | which no        | ice fragmentation    |                | would take     | place, such as  |
calmwindsandsmallwavesorstrongflexuralstrength
ofice.
5.3.ModelSensitivitytoVaryingDegreesofIce
Figure6.Changesinainasuccessionoficebreakupsfrom
Ridging
threenumericalexperimentsusingdifferentvaluesofredis-
tributionparticipationfactor,decreasingfromtheinitialvalue In addition to ice fragmentation, ice deformation-
of0.5,tomimicdifferentscenariosoficefragmentationin
|     |     |     |     |     | induced | ridging | may also | cause | mechanical |
| --- | --- | --- | --- | --- | ------- | ------- | -------- | ----- | ---------- |
thewakeofastorm.
|     |     |     |     |     | redistribution | of floe | size (described |     | in (10)), while |
| --- | --- | --- | --- | --- | -------------- | ------- | --------------- | --- | --------------- |
open water creation affects the area fraction of the open water category (described in (9)). As
described in section 4, two numerical experiments are conducted under the assumption that ice ridg-
ing causes a reduction of ice area by 10% and 20%. Note that ridging and open water creation are
normally calculated by (1). However, in the simplified sea ice model, (1) is not actually integrated. We
just assume that the ridging-induced changes in ice area are provided by (1) in these experiments.
The ridging-induced reduction in ice area means an open water creation by an equal amount. In other
words, in thesetwo experiments, thearea fraction in the openwater category of theFSD is increased by
10%or20%fromtheoriginalvalueof0.2.Theridging-inducedreductioninicearealeadstoareductionin
areafractionofallfloesizecategories(Figure7).Theamountofareareductionineachcategoryispropor-
tionaltotheareafractionofthatcategory,asdescribedin(10).Thecaseofstrongerridging(20%reduction
inicearea)leadstomoreareareductionacrossallcategories,asexpected(Figure7b).Notethat,unlikefloe
sizeredistributionduetoicebreakup,theiceridging-inducedfloesizeredistributionassumesnotransferof
areasfromcategoriesoflargersizestothoseofsmallersizes.Inotherwords,nofloesoflargersizesbreak
intosmallerfloesduringridging.Becauseridgingdoesnotchangefloenumbers,thereisnochangeinthe
valueoftheexponenta.
5.4.ModelSensitivitytoVaryingRedistributionCutoffConstants
IntheFSDtheory,theredistributioncutoffconstantc determinestherangeoffloesizeredistributionincase
1
oficefragmentationandissettoc 1 5l min /l max 5l 2 /l max .Thisensuresthat,whenanicefloeisbroken,catego-
riesofsmallersizesallgainfloes fromthebreakup,includingthesmallestfloesizecategory(Figure8a).As
describedinsection4,twomorenumericalexperimentsareconductedinwhichc ischosentobel /l and
|     |     |     |     |     |     |     | 1   |     | 3 max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Figure7.ChangesinFSD(dottedline)dueto(a)10%and(b)20%reductionsiniceareainducedbyridging.
| ZHANGETAL. |     |     | MODELINGFLOESIZEDISTRIBUTION |     |     |     |     |     | 3495 |
| ---------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | ---- |

Journal of Geophysical Research: Oceans
10.1002/2015JC010770
Figure8.SimilartoFigure3,butwithdifferentredistributioncutoffconstantsc andthesameparticipationfactorc andPartition1.Forcomparison,Figure8aisarepeatofFigure3b.
1 b
l /l . Thismeans thatfor thecaseofc 5l /l , thesecondfloe sizecategorywiththesmallestcenterl 4 max 1 3 max 2
maynotgainfloeswhenlargefloesarebroken.Fromthestandpointofphysics,thisrepresentsascenarioin
whichlargefloesarebrokenintofloesofmanysmallersizes,butnotintofloesofthesmallestsizes.Thisis
reflectedina‘‘flattening-out’’fromcategory3tocategory2inthelog-logplotofCFND(Figure8b).Forthe
caseofc 5l /l ,boththesecondandthirdcategoriesmaynotgainfloeswhenlargerfloesarebroken.This
1 4 max
isreflectedinaflattening-outfromcategory4tocategory2(Figure8c).Thisflattening-outatthelowerend
offloesizerange leads toa local deviation froma powerlaw.Insatelliteorairborneimageanalyses ofice
floes, similar flattening-out may occur if small floes within a prescribed floe size range are not identified
becauseoflimitationsofimageresolution[HoltandMartin,2001].Inotherwords,excludingcategoriesatthe
lowerendofthefloesizerangemimicstheresolutionlimitationsinobservations,whichneedstobeavoided
wheneverpossible.
6.ConcludingRemarks
SeaiceintheMIZconsistsoffloesofvaryingthicknessesandsizesandthereforeisbetterrepresentedby
both ITD and FSD. We have developed a FSD theory that is coupled to the ITD theory of Thorndike et al.
[1975] in order to explicitly simulate the evolution of FSD and ITD jointly. The FSD theory includes a FSD
functionandanFSDconservationequationinparallelwiththeThorndikeetal.ITDequation.TheFSDequa-
tiondescribeschangesinFSDcausedbyiceadvection,thermodynamicgrowth,andlateralmelting.Italso
incorporateschangesinFSDcausedbymechanicalfloesizeredistributionduetoiceridginginducedbyice
deformationandfragmentationinducedbystochasticoceansurfacewaves.
Thedescription of mechanicalfloe sizeredistribution due to ice ridging and fragmentationis challenging
because of our knowledge gaps in various MIZ processes such as ice deformation, wave-ice interactions,
propertiesoficeflexuralstrength,andpatternsoficebreakup.ThisFSDtheoryisbasedonthreefundamen-
talassumptions:
1.Iceridging-inducedfloesizeredistributionisbasedontheassumptionthat,atagivenareaofinterest,all
floesofdifferentsizeshavesameITD,whichislikelytruewhenalargefloeisbrokenintosmallerfloesby
waves.Thisassumptionsuggeststhatridgingreducestheareafractionsofallfloesequally,withoutarea
transferfromcategoriesoflargefloesizestothoseofsmallersizes.
2.Icefragmentation-inducedfloesizeredistributionisbasedontheassumptionthatwave-inducedbreakup
isarandomprocesssuchthatwhenanicefloeisbroken,floesofanysmallersizeshaveanequaloppor-
tunitytoform,withoutbeingeitherfavoredorexcluded.
3. Ice fragmentation-induced floe size redistribution is also based on the assumption that floes of larger
sizes are easier to break because they are subject to larger flexure-induced stresses and strains; larger
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3496
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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
10.1002/2015JC010770
floesalsohavehigherarealcoveragesandthereforehigherprobabilitiestobreakthansmallerfloes.(This
iscontrolledbytheparticipationfactorc .)
b
OnefeatureoftheFSDtheoryisthatthereisonlyonetunableparameter,theparticipationfactorc .Thepartici-
b
pationfactorc playsaprominentroleindeterminingwhetherwave-inducedicebreakupoccursand,ifso,how
b
manyfloesoflargesizesaretoparticipateinthemechanicalfloesizeredistribution.Thevalueofc islinkedto
b
waveconditionsthatdependonwindspeed,fetch,andwave-iceinteractions.Itisalsolinkedtoseaicecondi-
tionsbecauseITDandFSDnotonlyaffectwavepropagationandattenuationundericebutalsocontroltheflex-
uralstrengthandhencethebendingfailureofseaiceintheMIZ.Thus,c isafunctionofITD,FSD,waves,and
b
wave-iceinteractions.Therelationshipbetweenc andITD,FSD,waves,andwave-iceinteractionsneedstobe
b
establishedthroughobservationsormodelexperiments.Thisstudyisnotaimedtoquantifysucharelationship.
ItisaimedtoexploretheFSDtheory’sbehaviorinmechanicalfloesizeredistributionandresultingFSDinvarious
scenariosoficefragmentationassociatedwithdifferentvaluesofc .Thisgivesusideasqualitativelyonwhether
b
thetheoryisabletocreatefeaturesoficefloesoftenobservedintheMIZ.Italsogiveuscluesaboutthepossible
rangeofc valuesintherealworldundervaryingseaiceandwindandwaveforcingconditions.
b
Tothisend,theFSDtheoryisimplementedinasimplifiedITDandFSDseaicemodel(noadvectionorthermo-
dynamics)foraseriesofidealizednumericalexperimentswithdifferentc valuesandfloesizecategoryparti-
b
tions. The model results show that the simulated CFND follows a power law as observed by satellites and
airbornesurveys.ThesimulatedCFNDobeysapowerlawwhetherafteraninitialbreakuporaftervaryingnum-
berofbreakups.Mostimportantly,thesimulatedvaluesoftheexponentofthepowerlaw,withvaryingscenar-
iosoficefragmentationrepresentedbydifferentc values,aregenerallyintherangeoftheobservations.This
b
indicatesthattheFSDtheoryisinapositiontorealisticallysimulatepowerlawobeyingFSDintheMIZ.
The assumption that wave-induced breakup is a random process without favoring or excluding floes of any
smaller sizes plays a key role in obtaining the FSD obeying a power law, as is often the case with random-
breakingmodels.Itisfound,however,thatthesimulatedCFNDwoulddeviatefromapowerlawifcategoriesat
thelowerendofthefloesizerangeareexcludedfromparticipatinginredistribution.Inotherwords,ifthecate-
goriesofsmallestfloesdonotgainfloeswhenlargerfloesarebroken,adeviationfromapowerlawislikelyto
occurlocally,withCFNDcurvesflatteningoutoverthosecategories.Asimilardeviationmayoccurinsatelliteor
airborneimageanalysesoficefloesifsmallfloeswithinaprescribedfloesizerangearenotidentifiedbecauseof
thelimitationsofimageresolution.Thissuggeststhenecessitytoresolveasmanysmallfloesaspossibletoavoid
adeviationfromapowerlawbehavior,eitherinobservationalanalysesorinmodelsimulations.
It is also found that the simulated CFND deviates from a power law by showing a steeper descent at the
highendofthefloesizerange.Thisisanormalmodeloutcomebecauseofdecreasingnumber,andulti-
matelydisappearance,offloesoflargesizesasicecontinuestobreak.Thefallofffromapowerlawisoften
seeninobservation-derivedCFND,whichislikelyduetothesamereasonorduetolimitationsofdatasam-
pling. In some previous studies, the observed falloff behavior at the high end of the floe size range is
describedbyanuppertruncatedpowerlaw.Heretheuppertruncatedpowerlawisreplicatedinthemodel.
Another feature of the FSD theory is that mechanical floe size redistribution and the resulting FSD and
meanfloesizedonotdependonhowfloesizecategoriesarenumericallypartitionedoveragivenfloesize
range.Thetheory’sindependencefromfloesizecategorypartitionsoveragivenfloesizerangeandpartic-
ularlyitscreationofthepowerlawobeyingFSDseeninnaturepavethewaytoincorporateitintolarge-
scaledynamic thermodynamic sea ice modelsthat arebased onthe ITDtheory ofThorndike et al. [1975].
The ability to explicitly simulate multicategory FSD and ITD together may open a door for incorporating
additionalmodelphysics,suchasFSD-dependenticemechanicsandsurfaceexchangeofheat,mass,and
momentum. The FSD equations also provide a general framework for developing next generation sea ice
models to include modeling components to explicitly simulate waves, wave-ice interactions, and wave-
inducedicefragmentationinandaroundtheMIZ.
Acknowledgments
Wegratefullyacknowledgethe
supportoftheOfficeofNavalResearch References
(grantN00014-12-1-0112).Wethank
twoanonymousreviewersfortheir Burroughs,S.M.,andS.F.Tebbens(2001),Upper-truncatedpowerlawsinnaturesystems,PureAppl.Geophys.,158,741–757.
constructivecomments.Modelresults Comiso,J.C.(2012),LargedecadaldeclineoftheArcticmultilayericecover,J.Clim.,25,1176–1193.
areavailablebycontacting Doble,M.J.,andJ.-R.Bidlot(2013),WavebuoymeasurementsattheAntarcticseaiceedgecomparedwithanenhancedECMWFWAM:
zhang@apl.washingon.edu. Progresstowardsglobalwaves-in-icemodeling,OceanModell.,70,166–173.
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3497
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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
10.1002/2015JC010770
Dumont,D.,A.Kohout,andL.Bertino(2011),Awave-basedmodelforthemarginalicezoneincludingafloebreakingparameterization,
J.Geophys.Res.,116,C04001,doi:10.1029/2010JC006682.
Feltham,D.L.(2005),Granularflowinthemarginalicezone,Philos.Trans.R.Soc.A,363,1677–1700.
Flato,G.M.,andW.D.HiblerIII(1995),RidgingandstrengthinmodelingthethicknessdistributionofArcticseaice,J.Geophys.Res.,100,
18,611–18,626.
Herman,A.(2010),Sea-icefloe-sizedistributioninthecontextofspontaneousscalingemergenceinstochasticsystems,Phys.Rev.E,81,
066123.
Hibler,W.D.,III(1980),Modelingavariablethicknessseaicecover,Mon.WeatherRev.,1,1943–1973.
Hibler,W.D.,III(2001),Seaicefracturingonthelargerscale,Eng.Fract.Mech.,68,2013–2043.
Holt,B.,andS.Martin(2001),Theeffectofastormonthe1992summerseaicecoveroftheBeaufort,Chukchi,andEastSiberian
seas,J.Geophys.Res.,106,1017–1032.
Kohout,A.L.,andM.H.Meylan(2008),Anelasticplatemodelforwaveattenuationandicefloebreakinginthemarginalicezone,J.Geo-
phys.Res.,113,C09016,doi:10.1029/2007JC004434.
Kohout,A.L.,M.J.M.Williams,S.Dean,andM.H.Meylan(2014),Storm-inducedseaicebreakupandtheimplicationsforiceextent,Nature,
509,604–607.
Langhorne,P.J.,V.A.Squire,C.Fox,andT.G.Haskell(1998),Break-upofseaicebyoceanwaves,ColdReg.Sci.Technol.,27,438–442.
Lu,P.,Z.J.Li,Z.H.Zhang,andX.L.Dong(2008),AerialobservationsoffloesizedistributioninthemarginalicezoneofsummerPrydzBay,
J.Geophys.Res.,113,C02011,doi:10.1029/2006JC003965.
Meier,W.N.,etal.(2014),Arcticseaiceintransformation:Areviewofrecentobservedchangesandimpactsonbiologyandhumanactiv-
ity,Rev.Geophys.,52,185–217,doi:10.1002/2013RG000431.
Meylan,M.H.,andV.A.Squire(1994),Theresponseoficefloestooceanwaves,J.Geophy.Res.,99,891–900.
Meylan,M.H.,L.G.Bennetts,andA.L.Kohout(2014),InsitumeasurementsandanalysisofoceanwavesintheAntarcticmarginalice
zone,Geophys.Res.Lett.,41,5046–5051,doi:10.1002/2014GL060809.
Newman,M.E.J.(2005),Powerlaws,ParetodistributionsandZipf’slaw,Contemp.Phys.,46,323–351.
Perovich,D.K.,andK.F.Jones(2014),Theseasonalevolutionofseaicefloesizedistribution,J.Geophys.Res.Oceans,119,8767–8777,doi:
10.1002/2014JC010136.
Perovich,D.K.,B.Light,H.Eicken,K.F.Jones,K.Runciman,andS.V.Nghiem(2007),IncreasingsolarheatingoftheArcticOceanandadja-
centseas,1979–2005:Attributionandroleintheice-albedofeedback,Geophys.Res.Lett.,34,L19505,doi:10.1029/2007GL031480.
Perovich,D.K.,J.A.Richter-Menge,andK.F.Jones(2008),Sunlight,water,andice:ExtremeArcticseaicemeltduringthesummerof2007,
Geophys.Res.Lett.,35,L11501,doi:10.1029/2008GL034007.
Pickering,G.,J.M.Bull,andD.J.Sanderson(1995),Samplingpower-lawdistribution,Tectonophysics,248,1–20.
Rothrock,D.A.,andA.S.Thorndike(1984),Measuringtheseaicefloesizedistribution,J.Geophys.Res.,89,6477–6486.
Shen,H.H.,W.D.Hibler,andM.Lepp€aranta(1987),Theroleoffloecollisionsinseaicerheology,J.Geophys.Res.,92,7085–7096.
Squire,V.A.(2007),Ofoceanwavesandsea-icerevisited,ColdReg.Sci.Technol.,49(2),110–133.
Squire,V.A.,J.P.Dugan,P.Wadhams,P.J.Rottier,andA.K.Liu(1995),Ofoceanwavesandsea-ice,Annu.Rev.FluidMech.,27,115–168.
Squire,V.A.,G.L.Vaughan,andL.G.Bennetts(2009),OceansurfacewaveevolvementintheArcticBasin,Geophys.Res.Lett.,36,L22502,
doi:10.1029/2009GL040676.
Steele,M.(1992),Seaicemeltingandfloegeometryinasimpleice-oceanmodel,J.Geophys.Res.,97,17,729–17,738.
Steele,M.,J.Zhang,andW.Ermold(2010),MechanismsofsummertimeupperArcticOceanwarmingandtheeffectonseaicemelt,J.Geo-
phys.Res.,115,C11004,doi:10.1029/2009JC005849.
Steer,A.,A.Worby,andP.Heil(2008),Observedchangesinsea-icefloesizedistributionduringearlysummerinthewesternWeddellSea,
DeepSeaRes.,PartII,55,933–942.
Strong,C.,andI.G.Rigor(2013),Arcticmarginalicezonetrendingwiderinsummerandnarrowerinwinter,Geophys.Res.Lett.,40,
4864–4868,doi:10.1002/grl.50928.
Thomson,J.,andW.E.Rogers(2014),SwellandseaintheemergingArcticOcean,Geophys.Res.Lett.,41,3136–3140,doi:10.1002/
2014GL059983.
Thorndike,A.S.,D.A.Rothrock,G.A.Maykut,andR.Colony(1975),Thethicknessdistributionofseaice,J.Geophys.Res.,80,4501–4513.
Toyota,T.,S.Takatsuji,andM.Nakayama(2006),Characteristicsofseaicefloesizedistributionintheseasonalicezone,Geophys.Res.Lett.,
33,L02616,doi:10.1029/2005GL024556.
Toyota,T.,C.Haas,andT.Tamura(2011),Sizedistributionandshapepropertiesofrelativelysmallsea-icefloesintheAntarcticmarginal
icezoneinlatewinter,DeepSeaRes.,PartII,58,1182–1193,doi:10.1016/j.dsr2.2010.10.034.
Wadhams,P.(1981),Sea-icetopographyoftheArcticOceanintheregion708Wto258E,Philos.Trans.R.Soc.LondonA,302,45–85.
Wadhams,P.(1986),Theseasonalicezone,inTheGeophysicsofSeaIce,editedbyN.Untersteiner,pp.825–991,Plenum,N.Y.
Wadhams,P.,V.A.Squire,D.J.Goodman,A.M.Cowan,andS.C.Moore(1988),Theattenuationratesofoceanwavesinthemarginalice
zone,J.Geophys.Res.,93,6799–6818.
Williams,T.D.,L.G.Bennetts,V.A.Squire,D.Dumont,andL.Bertino(2013a),Wave–iceinteractionsinthemarginalicezone.Part1:Theo-
reticalfoundations,OceanModell.,doi:10.1016/j.ocemod.2013.05.010.
Williams,T.D.,L.G.Bennetts,V.A.Squire,D.Dumont,andL.Bertino(2013b),Wave–iceinteractionsinthemarginalicezone.Part2:numer-
icalimplementationandsensitivitystudiesalong1Dtransectsoftheoceansurface,OceanModell.,doi:10.1016/j.ocemod.2013.05.011.
Zhang,J.,andD.A.Rothrock(2001),Athicknessandenthalpydistributionsea-icemodel,J.Phys.Oceanogr.,31,2986–3001.
Zhang,J.,andD.A.Rothrock(2003),Modelingglobalseaicewithathicknessandenthalpydistributionmodelingeneralizedcurvilinear
coordinates,Mon.WeatherRev.,131(5),681–697.
Zhang,J.,R.W.Lindsay,M.Steele,andA.Schweiger(2008),WhatdrovethedramaticretreatofArcticseaiceduringsummer2007?,Geo-
phys.Res.Lett.,35,L11505,doi:10.1029/2008GL034005.
Zhang,J.,R.Lindsay,A.Schweiger,andI.Rigor(2012),RecentchangesinthedynamicpropertiesofdecliningArcticseaice:Amodelstudy,
Geophys.Res.Lett.,39,L20503,doi:10.1029/2012GL053545.
ZHANGETAL. MODELINGFLOESIZEDISTRIBUTION 3498
21699291,
2015,
5,
Downloaded
from
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JC010770,
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
