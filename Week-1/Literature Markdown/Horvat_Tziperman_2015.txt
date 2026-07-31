TheCryosphere,9,2119–2134,2015
www.the-cryosphere.net/9/2119/2015/
doi:10.5194/tc-9-2119-2015
©Author(s)2015.CCAttribution3.0License.
A prognostic model of the sea-ice floe size and thickness distribution
C.HorvatandE.Tziperman
SchoolofEngineeringandAppliedSciencesandDepartmentofEarthandPlanetarySciences,HarvardUniversity,
Cambridge,MA,USA
Correspondenceto:C.Horvat(horvat@fas.harvard.edu)
Received:30April2015–PublishedinTheCryosphereDiscuss.:28May2015
Revised:14October2015–Accepted:29October2015–Published:18November2015
Abstract.Seaiceexhibitsconsiderableseasonalandlonger- tion(Strongetal.,2009),theAntarcticOscillation(Wuand
term variations in extent, concentration, thickness, and age, Zhang, 2011), and the Madden–Julian Oscillation (Hender-
and is characterized by a complex and continuously chang- sonetal.,2014).Overthepastfewdecades,Arcticseaicehas
ingdistributionoffloesizesandthicknesses,particularlyin becomethinner,lessextensive,andmoreseasonal(Cavalieri
themarginalicezone(MIZ).Modelsofseaiceusedincur- andParkinson,2012).Regionsthatwereoncecoveredbyice
rentclimatemodelskeeptrackofitsconcentrationandofthe year-round now are ice-free in the summer (Stroeve et al.,
distributionoficethicknesses,butdonotaccountforthefloe 2012),andtheArcticmarginalicezone,definedaseitherthe
sizedistributionanditspotentialeffectsonair–seaexchange regionoftheoceanoverwhichwavesleadtothefractureof
andsea-iceevolution.Accuratelycapturingsea-icevariabil- ice (e.g. Williams et al., 2013b), or as the area of ice with
ity in climate models may require a better understanding concentrationbetween15and80%,whichhasbeenwiden-
andrepresentationofthedistributionoffloesizesandthick- ing during the summer season (Strong and Rigor, 2013).
nesses. We develop and demonstrate a model for the evolu- High-latitude storms are capable of breaking thinning pack
tion of the joint sea-ice floe size and thickness distribution iceintosmallerfloes,changingoceancirculationandair–sea
thatdependsonatmosphericandoceanicforcingfields.The exchange (Asplin et al., 2012; Zhang et al., 2013; Kohout
modelaccountsforeffectsduetomultipleprocessesthatare etal.,2015),withevidencesuggestingthatthesestormswill
activeintheMIZandseasonalicezones:freezingandmelt- becomemoreprevalentinthefuture(Vavrusetal.,2012).
ingalongthelateralsideandbaseoffloes,mechanicalinter- Sea-ice cover is heterogeneous, composed of a distribu-
actions due to floe collisions (ridging and rafting), and sea- tion of floes of different areas and thicknesses. Floes can
icefractureduetowavepropagationintheMIZ.Themodel vary dramatically in size, ranging from newly formed frazil
is then examined and demonstrated in a series of idealized crystalsmillimetersinsize,topackiceintheCanadianArc-
testcases. tic with floes up to 10m thick in places and hundreds of
|     |     |     |     |     |     |     | kilometers     | wide. The | most  | dramatic | intra-annual |                 | variability |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ----- | -------- | ------------ | --------------- | ----------- |
|     |     |     |     |     |     |     | in sea-ice     | cover is  | found | in the   | MIZ,         | and in seasonal | ice         |
|     |     |     |     |     |     |     | zones, regions | which     | range | from     | being        | ice-covered     | to ice-     |
1 Introduction
|     |     |     |     |     |     |     | free over | the year.       | As summer | sea-ice       | cover | becomes     | thin-   |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --------- | ------------- | ----- | ----------- | ------- |
|     |     |     |     |     |     |     | ner and   | more fractured, |           | these regions |       | will become | larger, |
Sea ice is a major component of the climate system, cover- and the distribution of these floes and their size, shape, and
ingabout12%oftheoceansurface.Itdrivestheice-albedo
|                |             |            |            |             |         |           | properties | may change.   |          | Events that | generate       | surface | waves,    |
| -------------- | ----------- | ---------- | ---------- | ----------- | ------- | --------- | ---------- | ------------- | -------- | ----------- | -------------- | ------- | --------- |
| feedback,      | a potential | source     | of climate | instability |         | and polar |            |               |          |             |                |         |           |
|                |             |            |            |             |         |           | such as a  | fortuitously  | observed |             | Arctic cyclone | in      | 2011, the |
| amplification, | and         | it affects | deep water | formation   |         | and air–  |            |               |          |             |                |         |           |
|                |             |            |            |             |         |           | so-called  | “Great Arctic |          | Cyclone”    | of 2012,       | and an  | energetic |
| sea fluxes     | of heat,    | fresh      | water, and | momentum    | between | the       |            |               |          |             |                |         |           |
waveeventobservedintheBarentsSea,canleadtothefrac-
atmosphereandocean.Itspresencealsoprovidesaplatform turingoffloes(Asplinetal.,2012;Zhangetal.,2013;Collins
| for high-latitude     |     | ecosystems | and determines         |     | polar | shipping |                |       |           |             |       |               |            |
| --------------------- | --- | ---------- | ---------------------- | --- | ----- | -------- | -------------- | ----- | --------- | ----------- | ----- | ------------- | ---------- |
|                       |     |            |                        |     |       |          | et al., 2015). | The   | fractured | sea-ice     | cover | has increased | floe       |
| routes. Additionally, |     | sea        | ice is well-correlated |     | with  | patterns |                |       |           |             |       |               |            |
|                       |     |            |                        |     |       |          | perimeter,     | which | may lead  | to enhanced |       | melting       | and a more |
ofatmosphericvariabilitysuchastheNorthAtlanticOscilla-
PublishedbyCopernicusPublicationsonbehalfoftheEuropeanGeosciencesUnion.

2120 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
rapid reduction in sea-ice area compared to an unfractured Table 1. Variables appearing in several components of the FSTD
| sea-icecover.Steele(1992)indeeddemonstratedanincreas- |                    |                      |              | model.   |             |     |         |
| ----------------------------------------------------- | ------------------ | -------------------- | ------------ | -------- | ----------- | --- | ------- |
| ing sensitivity                                       | of the             | ice cover to lateral | melting with | de-      |             |     |         |
|                                                       |                    |                      |              | Variable | Description |     | Section |
| creasing                                              | floe size, finding | that below           | 30m, lateral | melting  |             |     |         |
wascriticallyimportant.Smallerfloesizesmayadditionally
|     |     |     |     | g(h) | Icethicknessdistribution(ITD) |     | 1   |
| --- | --- | --- | --- | ---- | ----------------------------- | --- | --- |
lead to changes in the mechanical response of the sea-ice u Icevelocityvector 1
covertoforcingfromtheoceanandatmosphere,asfloesize ψ Icethicknessredistributionfunction 1
is a parameter in collisional models of ice rheology (Shen n(r) Icefloesizedistribution(FSD) 1
r=(r,h)
et al., 1986, 1987; Feltham, 2005, 2008). As sea ice atten- Floesizeandthickness 1
uates wave energy, the diminished ice fraction may lead to f(r) Jointfloesizeand 1
thicknessdistribution(FSTD)
| further surface | wave propagation | into                   | the ice field,    | enhanc- |                   |     |     |
| --------------- | ---------------- | ---------------------- | ----------------- | ------- | ----------------- | --- | --- |
|                 |                  |                        |                   | φ       | Openwaterfraction |     | 2.1 |
| ing fracturing  | farther from     | the sea-ice            | edge, and leading | to      |                   |     |     |
|                 |                  |                        |                   | c       | Iceconcentration  |     | 2.1 |
| further sea-ice | area loss        | in a positive feedback | loop              | (Asplin |                   |     |     |
N(r)
|                |            |                 |                  |      | Floenumberdistribution           |     | 2.1 |
| -------------- | ---------- | --------------- | ---------------- | ---- | -------------------------------- | --- | --- |
| et al., 2014). | Floe sizes | can also affect | the surface drag | co-  |                                  |     |     |
|                |            |                 |                  | C(r) | Cumulativefloenumberdistribution |     | 2.1 |
efficientandthereforeair–seafluxes(BirnbaumandLüpkes,
2002).Alongfloeedges,oceaneddiesmaybegenerateddue
| to the gradient | in surface | heat and stress | boundary | condi- |     |     |     |
| --------------- | ---------- | --------------- | -------- | ------ | --- | --- | --- |
tionsbetweeniceedgeandopenwater(Niebauer,1982;Jo- (Thorndike et al., 1975; Semtner, 1976; Hibler, 1979). This
hannessenetal.,1987).Theseeddiesmaymorerapidlymix approximation may not suffice, because it does not account
air–seaheatfluxabsorbedbyopenwatertounderneathsea- forthedistributionoffloesizesandthereforefortheabove-
ice floes when floe sizes are comparable to the eddy length mentionedrelatedeffects.
scale, but not when floe sizes are much larger. This in turn Weaimtodescribethesubgrid-scalevariabilityofthesea-
mayhaveconsequencesforicemeltratesandoceancircula- icecoverbyextendingtheicethicknessdistributiontoajoint
tion(HorvatandTziperman,2014). distribution that includes both ice thickness and floe size.
Given that it is not computationally practical to simu- RothrockandThorndike(1984)wereamongthefirsttode-
late all individual floes, properties of the ice cover can in- scribe the distribution of lateral floe sizes, defining the floe
stead be described using statistical distributions. This ap- size distribution (FSD) n(r) dr as the fractional area of the
proach was pioneered by Thorndike et al. (1975), who de- seasurfacecoveredbyfloeswithlateralsizebetweenr and
r+dr.
velopedaframeworkforsimulatingtheicethicknessdistri- The size of a √ floe with area a is represented by its
bution(ITD),g(h),definedsuchthatg(h)dhisthefractional effectiveradius,r = a/π,whichrepresentsfloesascylin-
areaoftheseasurfacecoveredbyicewiththicknessbetween ders of radius r. Modeling of the lateral floe size distribu-
h and h+dh. The Thorndike model evolves the prognostic tion is hampered by the difficulty of measurement, as floe
equation sizes vary over many orders of magnitude. Even with suf-
|       |     |     |     | ficient imagery, | algorithms | that identify | and measure floes |
| ----- | --- | --- | --- | ---------------- | ---------- | ------------- | ----------------- |
| ∂g(h) |     | ∂   |     |                  |            |               |                   |
=−∇·(gu)− (g(h)G )+ψ, (1) must overcome many obstacles, such as submerged floes,
h
∂t ∂h melt ponds, and clouds. In spite of these challenges, many
whereuisthehorizontalicevelocity,G h istherateofchange observationsofthefloesizedistributionhavebeenmade,of-
oficethicknessduetomeltingandfreezing(thermodynam- ten using helicopter or ship-board cameras, notably in the
ψ,
ics), and the “redistribution function”, describes the cre- AlaskanandRussianArctic(HoltandMartin,2001),Seaof
ationoficeofthicknesshbymechanicalcombinationofice Okhotsk (Toyota and Enomoto, 2002; Toyota et al., 2006),
of different thicknesses. Measurements of ice thickness are PrydzBay(Luetal.,2008),andWeddellSea(Herman,2010;
madepossiblebyavarietyofremotesensingtechniquessuch Toyota et al., 2011). These studies have focused on deriv-
as submarine sonar, fixed moorings, helicopter borne elec- ing and fitting scaling relationships measured distributions,
tromagnetic induction, and satellite measurements (Bourke leadingtopower-law(Toyotaetal.,2006),Pareto(Herman,
andGarrett,1987;YuandRothrock,1996;RennerandGer- 2010),orjoinedpower-law(Toyotaetal.,2011)distributions
land,2014),whichmaybeusedtotestmodelskill.Variants offloesizes.Thetemporalevolutionofthefloesizedistribu-
of the Thorndike model have been implemented in several tion has been examined in a small number of observational
generalcirculationmodels(GCMs,Bitz,2008;Hunkeetal., studies (Holt and Martin, 2001; Steer et al., 2008; Perovich
2013),andhavebeenusedtounderstandsea-icebehaviorand and Jones, 2014), that analyzed the change in the floe size
predictability(Bitzetal.,2001;ChevallierandSalas-Mélia, distribution over several weeks or seasonally, but these ob-
2012). servations,particularlyinthemarginalicezone,arelimited.
ModernapproachestomodelingseaiceinGCMs,suchas Herman(2010)modeledtheFSDasageneralizedLotka–
thecommunityicemodel(Hunkeetal.,2013),generallyap- Volterra system, which exhibits a Pareto distribution of floe
proximateicecoverasanon-Newtonianfluidwithvertically sizesasasolution,andsuggestedthatthisdistributionmight
layered thermodynamics, and simple thickness distribution fitobservedFSDs.Toyotaetal.(2011)showedthatobserved
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2121
FSDsintheWeddellSeamaybefitbyapowerlawandthat thejointfloesizeandthicknessdistribution.Inaddition,each
suchascalingrelationshipmaybeobtainedbyassumingthat ofthetermsinEq.(2) asdevelopedbelowcontainsanovel
icefractureisaself-similarprocess,followingarenormaliza- formulation of the corresponding process that is physically
tiongroupmethod.Zhangetal.(2015)developedamodelfor basedandlessheuristicthanusedinpreviousstudies.
thefloesizedistributionevolution,assumingthatallfloesof The paper proceeds as follows: we first develop explicit
different sizes have the same ITD. The present paper, how- representationsforthedifferentprocessesaffectingthejoint
ever, develops a model for the joint floe size and thickness floe size and thickness distribution in response to atmo-
distribution,allowingfordifferenticethicknessdistribution spheric and oceanic forcing in Sect. 2. The model response
for each horizontal size class. The Zhang et al. (2015) pa- toindividualforcingfields,intheformofair–seaheatfluxes,
per shares many of our goals and we refer to it below, fur- iceflowthatleadstofloecollisions,andsurfacewaves,isan-
ther elaborating on additional differences between the two alyzedinSect.3.WeconcludeinSect.4.
studies in the treatment of thermodynamics, mechanical in-
teractions, and wave fracturing. Other modeling studies in-
volving the temporal evolution of the floe size distribution 2 Representingprocessesthataffectthejointfloesize
havemainlyfocusedonunderstandingoceanwavepropaga- andthicknessdistribution
tionandattenuationinthemarginalicezone(Dumontetal.,
2.1 Thermodynamics
2011; Williams et al., 2013a, b). These studies developed
models of ocean wave propagation, attenuation and associ-
Air-sea heat fluxes in the polar oceans lead to the freezing
atedicebreakage,andmodeledtheFSDusingtherenormal-
and melting of ice. In regions of open water, cooling pro-
izationgroupmethodofToyotaetal.(2011).
duces frazil ice which may consolidate with other floes or
Thepurposeofthepresentpaperistodevelopanddemon-
form“pancakes”.Whenfloesgrowduetotheaccumulation
strate a framework for modeling the joint distribution of
of frazil crystals, or by congelation growth at their bases,
floe sizes and thicknesses (referred to below as the FSTD)
theirsizeandthicknesswillchange,butthetotalnumberof
f(r,h), with f(r,h) dr dh being the fraction of the ocean
floeswillnot.Supposethattheonlysourceorsinkoficevol-
surface area covered by floes of thickness between h and
ume is due to freezing and melting of existing floes, which
h+dh and lateralsize between r and r+dr (a listof vari-
causesthemtochangetheirsizeataratewedenoteasG and
ablenamesanddescriptionsareprovidedinTable1).Theice r
thicknessatarateG ,andwedefineG≡(G ,G ).LetN be
thicknessdistributiong(h)andfloesizedistributionn(r)are h r h
thenumberdistribution,suchthatN(r)dhdr isthenumber
obtainedbyintegratingoverthejointdistributionf(r,h):
offloesintherange(h,h+dh),(r,r+dr)(alistofthevari-
∞ ablesusedtodescribeFSTDthermodynamicsisprovidedin
Z
g(h)= f(r,h)dr, Table2).Thecumulativenumberdistributionisdefinedas
0 r r
Z Z
Z ∞ C(r)= N(r (cid:48) )dr (cid:48)= (f(r (cid:48) )/πr (cid:48)2 )dr (cid:48) ,
n(r)= f(r,h)dh.
0 0
0
Theprognosticequationforthejointfloesizeandthickness with ∂2 (C)=N(r)=f(r)/πr2,anditobeystheconser-
∂r∂h
distributionhastheform vationequation
∂f(r) =−∇·(f(r)u)+L +L +L , (2) C(r,t)=C(r+Gdt,t+dt),
T M W
∂t
sincefloeswithafinitesizeandthicknessr =(r,h)are,by
where r =(r,h), and ∇=( ∂ , ∂ ) is the two-dimensional
∂x ∂y assumption,neithercreatednordestroyedbythermodynamic
Laplacian. The two-dimensional spatial domain may be
growthandmelting.Expandingtheright-handsideandrear-
thought of as corresponding to a single grid cell of a cli-
ranginginthelimitasdt →0leadstothetimerateofchange
matemodel,ontheorderoftensofkilometersonaside.The
ofthecumulativenumberdistribution
term ∇·(f(r)u) describes advection of the floe size distri-
bution by the flow of ice. L T is the time rate of change of ∂C(r,t)
=−G·∇ C, (3)
the floe size distribution due to thermodynamic effects. L M ∂t r
isthetimerateofchangeduetomechanicalinteraction(raft-
ingandridgingoffloes).L isthetimerateofchangedueto where ∇ =(∂ , ∂ ) is the vector of partial derivatives in
W r ∂r ∂h
floesbeingfracturedbysurfaceoceanwaves.Weparameter- (size, thickness) space. Changes to the cumulative number
ize each of the above processes, forced by grid-scale atmo- distributionareduetothetransferoficetolargerorsmaller
spheric and oceanic forcing fields. The major contributions sizesbythermodynamicgrowthandmelting.Wenextmake
of this paper are, first, that it presents the first treatment of the assumption that thickness changes due to melting and
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2122 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
Table2.VariablesusedintherepresentationofthermodynamicalprocessesintheFSTDmodel.
|     |     |     | Variable |     |     | Description                       |     |     |     | Section |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- |
|     |     |     | LT       |     |     | ThermodynamiccomponentofFSTDmodel |     |     |     | 1       |     |     |     |     |
|     |     |     | G=(Gr,G  |     | )   | Icesizeandthicknessgrowthrate     |     |     |     | 2.1     |     |     |     |     |
h
|     |     |     | (r  | ,h   | )   | Sizeofsmallesticepancakes |     |     |     | 2.1 |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | min  | min |                           |     |     |     |     |     |     |     |     |
|     |     |     | r   | lw   |     | Widthofleadregion         |     |     |     | 2.1 |     |     |     |     |
|     |     |     | A   | lead |     | Leadareafraction          |     |     |     | 2.1 |     |     |     |     |
|     |     |     | Q   |      |     | Leadareaheatflux          |     |     |     | 2.1 |     |     |     |     |
lead
|     |     |     | Qo  |     |     | Openwaterheatflux       |     |     |     | 2.1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | A˙  |     |     | Rateofpancakeareagrowth |     |     |     | 2.1 |     |     |     |     |
p
|     |     |     | Q   | l,l |     | Fractionofleadheatfluxtransmittedtofloesides |     |     |     | 2.1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | Q   | l,b |     | Fractionofleadheatfluxtransmittedtofloebases |     |     |     | 2.1 |     |     |     |     |
freezing do not depend on the floe radius, and that hori- The floe size and thickness change rate vector G=
zontal size changes do not depend on the thickness, i.e., (G r ,G h )isdeterminedusingthebalanceofheatfluxesatthe
∂ (G )= ∂ (G )=0. The time evolution of the floe size ocean–ice–atmosphereinterface.Notethatourfocushereis
| ∂h  | r   | ∂r h |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distribution solely due to freezing and melting of existing the impact of thermodynamic forcing on the FSTD: we are
floes is derived by taking derivatives with respect to both not modeling internal ice thermodynamics explicitly. In an
thicknessandsizeofEq.(3): applicationoftheFSTDmodel,afullthermodynamicmodel
oftheoceanmixedlayerandseaicewouldsimulatetheice
|     | (cid:12) |     |     | (cid:18) | (cid:19) |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂f ( r)(cid:12) ∂ f ( r ) ∂f ( r) e n er g y bu dg e t . N e t h e a t fl ux in o c ea n r e g io n s a d j ac e n t t o
|     | (cid:12) | =−πr2 |     |     | G − |     | G , |     |     |     |     |     |     |     |
| --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂ t (cid:12) ∂ r π r 2 r ∂ h h ic e fl o es (w h i c h w e re f e r to as le a d re gi o n s ) i s a s s u m e d t o
melt/freeze
2 affect the development of adjacent floes laterally and verti-
=−∇ ·(f(r)G)+ f(r)G . (4) cally, while cooling in open water away from existing floes
|     |     |     | r   |     | r   | r   |     |          |            |               |     |            |      |         |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------- | --- | ---------- | ---- | ------- |
|     |     |     |     |     |     |     |     | may lead | to pancake | ice formation |     | (the model | does | not re- |
Without loss of generality, consider the interpretation of solve frazil ice, nor arbitrarily small pancake ice). The lead
thisequationforthecaseoffreezinginwhichexistingfloes region is defined as the annulus around each floe of width
get thicker and larger. This implies that some of the area r lw ,andthedivisionofoceanareaintoleadandopenwater
f(r)nowmovestolargericeclasses,representedbythefirst areas is shown as the blue and white regions in Fig. 1, (see
term in Eq. (4). Note that the integral over all size classes also Parkinson and Washington, 1979). The total lead area,
andthicknessofthefirsttermvanishes,andthereforeitdoes A ,isapproximatedas
lead
notdescribeiceareagrowth.Thetotaliceareaaddedorre-
|                                                    |     |                                       |     |     |     |     |     |         |    |           |     |            |          |    |
| -------------------------------------------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --------- | --- | ---------- | -------- | --- |
| movedthatbelongstofloesofsizer,N(r)d/dt(πr2),equal |     |                                       |     |     |     |     |     |         | Z   |           |     |            |          |     |
|                                                    |     |                                       |     |     |     |     |     |         |     | (cid:16)  |     |            | (cid:17) |     |
|                                                    |     |                                       |     |     |     |     |     | A =min |     | N(r)π(r+r |     | )2−N(r)πr2 | dr,φ    |     |
| toN(r)2πrG                                         |     | ,whichisequaltothesecondterminEq.(4). |     |     |     |     |     | lead    |     |           | lw  |            |          |     |
r
|     | Zhang et | al. (2015) | include | the | effects | of melting | and |     | r   |     |     |     |     |     |
| --- | -------- | ---------- | ------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |          |            |         |     |         |            |     |     |    |     |     |    |     |     |
freezing on the FSD, in a way that depends on the lateral Z   !
|     |     |     |     |     |     |     |     |     |     | 2r  | r2  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
growthrate(ourG ),butwithoutevaluatingthisrateinterms =min f(r) lw + lw dr,φ,
r
|     |               |     |          |                   |     |       |         |     |     | r   | r   | 2   |     |     |
| --- | ------------- | --- | -------- | ----------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
| of  | thermodynamic |     | forcing. | Their formulation |     | seems | to lack |     |     |     |     |     |     |     |
r
| the | second | term on | the right-hand |     | side of | Eq. (4). | The for- |     |     |     |     |     |     |     |
| --- | ------ | ------- | -------------- | --- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
whereφistheopenwaterfraction,andtheaboveintegration
mulationpresentedhereisforthejointFSTD,andtherefore
isovertheentirerangesofeffectiveradiusandthicknessrep-
| dependsonbothG |     |     | andG | .Wefurtherevaluatetheserates |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | ---- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                |     |     | r h  |                              |     |     |     |     |     |     |     |     |     |     |
belowintermsofair–seafluxes. resentedinthemodel.Anetair–seaheatfluxQattheocean
|     |     |     |     |     |     |     |     | surfaceisthereforepartitionedintoaleadheatfluxQ |     |     |     |     |     | =   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
In addition to melting and freezing of existing floes, we lead
|     |     |     |     |     |     |     | ˙   | A Q | and an open | water | heat | flux Q =(φ−A |     | )Q. If |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ------------ | --- | ------ |
mustalsoconsidertherateofgrowthofpancakeice,A ,due lead o lead
p
thewaterisatitsfreezingpoint,acoolingheatfluxleadsto
totheflocculationoffrazilcrystalsinpatchesofopenwater
|                                                     |     |     |     |     |     |     |     | freezingofpancakesoficeofradiusr |     |     |     | andthicknessh |     | ,   |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ------------- | --- | --- |
| awayfromexistingfloes.Pancakesareassumedtobecreated |     |     |     |     |     |     |     |                                  |     |     |     | min           |     | min |
˙
by freezing at the smallest size and thickness accounted for producing the area A p of ice pancakes per unit time where
therewasformerlyopenwater:
| inthemodel,withaneffectiveradiusr |     |     |     |     | p andthicknessh |     | min . |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Thefullexpressionfortherateofchangeofthefloesizeand
|           |     |              |        |                 |     |     |             | ˙   | Q o   |     |     |     |     |     |
| --------- | --- | ------------ | ------ | --------------- | --- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
| thickness |     | distribution | due to | thermodynamics, |     | L   | , is there- | A = |       | .   |     |     |     |     |
|           |     |              |        |                 |     |     | T           | p ρ | L h   |     |     |     |     |     |
|           |     |              |        |                 |     |     |             | 0   | f min |     |     |     |     |     |
fore
|     |     |     |     |     |     |     |     | The lead | region | heat flux, | Q   | , is further | partitioned | into |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | ------------ | ----------- | ---- |
lead
|     |     |     | 2   | +δ(r−rmin)δ(h−hmin)A˙ |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LT =−∇ r ·(f(r)G)+ f(r)Gr p. (5) a part that leads to basal freezing or melting of existing
r
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2123
theicebaseandiceedgesistherefore
Lead Region
|     |     |     |     |     | O p e n |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | W a te  | r   |     |     |     |     |     |     |     |
Contact Zoner
|     |     |               |     |     |      |     |     |       |      | (cid:18) c | (cid:19)−1 |     |     |
| --- | --- | ------------- | --- | --- | ---- | --- | --- | ----- | ---- | ---------- | ---------- | --- | --- |
|     |     |               |     |     |      |     |     |       | =Q   | 1+         | ;          |     |     |
|     |     | A             |     |     | w    |     |     | Q l,l | lead |            |            |     |     |
|     |     | core          |     |     | l    |     |     |       |      | 2h/r       |            |     |     |
|     |     |               |     |     |      |     |     |       |      |            | !−1        |     |     |
|     |     | (cid:7574)c z |     |     | A    |     |     |       |      | 2h/r       |            |     |     |
|     |     | -             | r   |     |      |     |     | Q     | =Q   | 1+         | .          |     |     |
|     |     | r             |     |     | lead |     |     | l,b   | lead |            |            |     |     |
c
A
Core
cz
Figure 1. A section of a floe, showing the division of a floe and The rate of change of ice thickness can be found using a
thesurroundingseasurfaceforthethermodynamicandmechanical modeloficethermodynamics,giventheabove-derivedopen
interactioncomponentsoftheFSTDmodel.Thefloeitself,ofradius waterair–seafluxcontributionQ totheheatbudgetatthe
l,b
r,isdividedintothecorewhichisunaffectedbyridgingandrafting
|     |     |     |     |     |     |     |     | ice | base. For | example, ignoring | ice heat capacity, | ice | thick- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | ------------------ | --- | ------ |
r−δcz)
(blue, width and contact zone which participates in these ness changes due to melting and freezing are related to the
interactions(green,widthδcz).Thefloeissurroundedbythelead
|                |                                             |     |     |     |     |     |     | net | heat flux | into the ice | from the surface above, | Q   | surf (de- |
| -------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ----------------------- | --- | --------- |
| regionofwidthr | lwwherenetheatfluxesleadtofreezingormelting |     |     |     |     |     |     |     |           |              |                         |     |           |
finednegativeupward),andfrombelow(wherenegativeflux
ofthefloeitself(blue)andthenbyopenwaterwherecoolingmay
meansoceancooling):
leadtonewpancakeiceformation(white).
ice floes, Q l,b , and a component that leads to lateral freez- ρ L G =−(Q +Q ). (6)
|                                              |     |     |     |     |     |     |       | i   | f h | l,b surf |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | -------- | --- | --- | --- |
| ingormeltingalongperimetersofexistingfloes,Q |     |     |     |     |     |     | .Mul- |     |     |          |     |     |     |
l,l
| tiple choices | for | this | partitioning |     | are possible, |     | including |     |     |     |     |     |     |
| ------------- | --- | ---- | ------------ | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
a binary partition (Washington et al., 1976) with Q = Therateofchangeofthelateralfloesizeiscalculatedfrom
l,b
| Q ,Q | =0orQ |     | =Q  | ,Q  | =0,aparameterization |     |     |     |     |     |     |     |     |
| ---- | ----- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
lead l,l l,l lead l,b thecorrespondingcontributionoftheair–seaheatfluxfrom
∝
with a quadratic dependence on open water fraction Q l,l theleadregionQ :
l,l
| A2 (Parkinson |     | and | Washington, |     | 1979), | and diffusive | and |     |     |     |     |     |     |
| ------------- | --- | --- | ----------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
lead
| molecular-sublayer |             | parameterizations |     |          | based | on      | the temper- |       |       |       |     |     |     |
| ------------------ | ----------- | ----------------- | --- | -------- | ----- | ------- | ----------- | ----- | ----- | ----- | --- | --- | --- |
| ature of           | the surface | waters            |     | (Steele, | 1992; | McPhee, | 1992).      |       | =−Q   |       |     |     |     |
|                    |             |                   |     |          |       |         |             | ρ i L | f G r | l,l . |     |     | (7) |
Whiletheseparameterizationshavebeentestedinsomede-
tail(Harvey,1990;Steele,1992),sensitivityanalysesinpre-
| vious studies | have | fixed | (either | explicitly |     | or implicitly) | the |     |     |     |     |     |     |
| ------------- | ---- | ----- | ------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Theaboveequationscannowbeusedtoexpressthethermo-
| floe size | distribution, |     | and the | impact | of  | this assumption | on  |     |     |     |     |     |     |
| --------- | ------------- | --- | ------- | ------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
dynamicfloegrowthratevector,G=(G
r ,G h ).
| the results | is unclear. |     | We choose | to  | simply | assume | that the |     |     |     |     |     |     |
| ----------- | ----------- | --- | --------- | --- | ------ | ------ | -------- | --- | --- | --- | --- | --- | --- |
leadheatfluxismixeduniformlyovertheexposedsurfaceof
afloe,partitionedaccordingtotheratiooficebasalandlat- 2.2 Mechanicalinteractions
eralsurfaceareas,whereitcontributestoicegrowthormelt.
| The total | fractional | lateral | surface |     | area (that | is, | the area of |     |     |     |     |     |     |
| --------- | ---------- | ------- | ------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Windandoceancurrentscandriveindividualfloecollisions,
theverticaledgesoficefloes,perunitoceanarea)is
andthereforemergethemtogether.Whenonefloeoverrides
anotherwhileremainingintact,theinteractionisreferredto
Z
asrafting.Iftheiceatthepointofcontactdisintegratesinto
| N(r)2πrhdr |     | =   |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arubblepile,forminga“sail”anda“keel”,andthetwofloes
r consolidate, the interaction is referred to as ridging. To de-
Z 2h
|      | =2h/r, |     |     |     |     |     |     | scribetheseprocesses,openwaterinthefloesizeandthick- |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
| f(r) | dr     |     |     |     |     |     |     |                                                      |     |     |     |     |     |
r ness distribution f(r) is represented by a delta function at
| r   |     |     |     |     |     |     |     | =0,multipliedbytheareafractionofopenwater.Thedy- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
r
whereN isthenumberdistributionintroducedabove,2πrh namics of open water formation by ice flows may then be
isthelateralareaofonefloe,and2h/rrepresentsanaverage derived by taking integrals over the prognostic Eq. (2) that
overallicefloes,weightedbythefloesizeandthicknessdis- include or exclude r =0 (a list of the variables used to de-
tribution. The above result depends on the model including scribe the FSTD response to floe collisions is provided in
an explicit joint FSTD, without which this estimate for the Table 3). The integral of f(r) over all floe sizes and thick-
lateral area would not be possible to obtain. The total basal nesses,includingopenwater,isequalto1.Therefore,ignor-
icesurfaceareaperunitoceanareaistheiceconcentration, ing thermodynamic and wave effects, we integrate Eq. (2)
c.Thepartitioningofheatfluxfromtheleadregionbetween over a range of floe sizes that include a vanishingly small
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2124 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
Table3.VariablesusedintherepresentationofmechanicalinteractionsintheFSTDmodel.
|     |     | Variable |     | Description                                              |     |     |     |     |     |     |     | Section |     |     |     |
| --- | --- | -------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
|     |     | LM       |     | MechanicalcomponentofFSTDmodel                           |     |     |     |     |     |     |     | 1       |     |     |     |
|     |     | DM/Dt    |     | Rateofchangeincorporatingicecollisions                   |     |     |     |     |     |     |     | 2.2     |     |     |     |
|     |     | Lc       |     | Normalizedfractionofconcentrationlost/gainedbycollisions |     |     |     |     |     |     |     | 2.2     |     |     |     |
(cid:15)˙
|     |     |     |        | Iceflowstrainratetensor            |     |     |     |                             |     |     |     | 2.2 |     |     |     |
| --- | --- | --- | ------ | ---------------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | E   |        | Vectorofstrainratetensorinvariants |     |     |     |                             |     |     |     | 2.2 |     |     |     |
|     |     | K(r | ,r ,r) | Collisionkernel:twofloesofsizer    |     |     |     | 1andr 2,formingafloeofsizer |     |     |     | 2.2 |     |     |     |
1 2
|     |     | P    | (r ,r | ) Probabilityoftwofloesofsizesr                |     |     |     | 1andr 2colliding |     |     |     | 2.2 |     |     |     |
| --- | --- | ---- | ----- | ---------------------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | coll | 1     | 2                                              |     |     |     |                  |     |     |     |     |     |     |     |
|     |     | δ    |       | Widthofcontactzoneforcollisionsrafting/ridging |     |     |     |                  |     |     |     | 2.2 |     |     |     |
raft/ridge
|     |     | Acz   |     | Areaoffloecontactzone                            |     |     |     |     |     |     |     | 2.2 |     |     |     |
| --- | --- | ----- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Acore |     | Areaoffloecore                                   |     |     |     |     |     |     |     | 2.2 |     |     |     |
|     |     | γ(h)  |     | Interpolationcoefficientbetweenraftingandridging |     |     |     |     |     |     |     | 2.2 |     |     |     |
intervalofsizesaroundr =(r,h)=0: Equation (9) suggests that there should be another term in
DMc.This
|         |     |                           |            |            |            |     |     | L (r)that,whenintegratedoverallsizes,leadsto |     |     |               |     |     |     |      |
| ------- | --- | ------------------------- | ---------- | ---------- | ---------- | --- | --- | -------------------------------------------- | --- | --- | ------------- | --- | --- | --- | ---- |
|         |     |                           | ∞          | ∞          |            |     |     | M                                            |     |     |               |     |     | Dt  |      |
| Z       |     |                           | Z          | Z          |            |     |     | suggeststhefollowingform:                    |     |     |               |     |     |     |      |
| L (r)dr | ≡   | lim                       |            | L          | (r,h)drdh, |     |     |                                              |     |     |               |     |     |     |      |
| M       |     |                           |            | M          |            |     |     |                                              |     |     |               |     |     |     |      |
|         |     | |((cid:15)1,(cid:15)2)|→0 |            |            |            |     |     |                                              |     | D M | c             |     |     |     |      |
| 0−      |     |                           | −(cid:15)1 | −(cid:15)2 |            |     |     | L =(∇·u)δ(r)+                                |     |     | [L (r)−δ(r)], |     |     |     | (10) |
|         |     |                           |            |            |            |     |     | M                                            |     |     | c             |     |     |     |      |
|         |     | Z (cid:20)                |            |            | (cid:21)   |     |     |                                              |     | Dt  |               |     |     |     |      |
∂f(r)
|     | =   |     | +∇·(f(r)u) |     | dr, |     |     |        |                                                 |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | ∂t  |            |     |     |     |     | whereL | (r)isyetunspecifiedexceptthatitsintegraloverall |     |     |     |     |     |     |
c
|                      |     | 0−           |                                |            |     |              |     | sizesis1,anditisnon-singularat||r||=0: |         |            |        |          |          |     |         |
| -------------------- | --- | ------------ | ------------------------------ | ---------- | --- | ------------ | --- | -------------------------------------- | ------- | ---------- | ------ | -------- | -------- | --- | ------- |
|                      |     | ∂1           |                                |            |     |              |     | Z                                      | Z       |            |        |          |          |     |         |
|                      | =   | +∇·(1u)=∇·u. |                                |            |     |              | (8) |                                        |         |            |        |          |          |     |         |
|                      |     | ∂t           |                                |            |     |              |     | L (r)                                  | dr =    | L (r)      | dr =1. |          |          |     | (11)    |
|                      |     |              |                                |            |     |              |     | c                                      |         | c          |        |          |          |     |         |
|                      |     |              |                                |            |     |              |     | 0+                                     | 0−      |            |        |          |          |     |         |
| The integral         | of  | f(r) over    | all                            | floe sizes | and | thicknesses, | but |                                        |         |            |        |          |          |     |         |
| excludingopenwater(r |     |              | = 0),isequaltotheiceconcentra- |            |     |              |     |                                        |         |            |        |          |          |     |         |
|                      |     |              |                                |            |     |              |     | The factor                             | L c (r) | quantifies | the    | relative | fraction | of  | the to- |
=0,
tion,c.IntegratingEq.(2)asbeforebutnowexcludingr talconcentrationlostduetocollisionsateachfloesize.The
∞ ∞ terms in Eq. (10) that are proportional to δ(r) represent to-
| Z       |     |     | Z Z |              |     |     |     |                                                     |           |     |            |     |               |     |        |
| ------- | --- | --- | --- | ------------ | --- | --- | --- | --------------------------------------------------- | --------- | --- | ---------- | --- | ------------- | --- | ------ |
|         |     |     |     |              |     |     |     | gether the                                          | formation | of  | open water | due | to collisions |     | driven |
| L (r)dr | ≡   | lim |     | L (r,h)drdh, |     |     |     |                                                     |           |     |            |     |               |     |        |
| M       |     |     |     | M            |     |     |     | bydivergenticemotions.Theremainingtermrepresentsthe |           |     |            |     |               |     |        |
|((cid:15)1,(cid:15)2)|→0
0+ (cid:15)1 (cid:15)2 rearrangement of ice area among floe classes. It remains to
|     | Z   | (cid:20) |     |     | (cid:21) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂f(r) derive expressions for the rate of open water formation due
|     | =   |     | +∇·(f(r)u) |     | dr, |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DMc,andtherearrangementofthefloesizeand
|     |     | ∂t  |     |     |     |     |     | tocollisions |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Dt
0+ thickness distribution in response to a unit amount of open
|     | ∂c  |               |     |     | D   | c   |     | waterformationduetocollisions,L |     |     |     | (r). |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ---- | --- | --- | --- |
|     | =   | +u·∇c+c(∇·u)≡ |     |     | M   | .   | (9) |                                 |     |     |     | c    |     |     |     |
∂t Dt Thorndike et al. (1975) described the rate of mechanical
|           |            |     |        |          |       |         |      | interactions | as depending |     | on the | divergence, |     | convergence, |     |
| --------- | ---------- | --- | ------ | -------- | ----- | ------- | ---- | ------------ | ------------ | --- | ------ | ----------- | --- | ------------ | --- |
| The above | definition |     | of the | operator | D /Dt | implies | that |              |              |     |        |             |     |              |     |
M
=∇·u. and shear of the ice flow, weighted by the relative size of
| D M (1)/Dt |     | The | subscript |     | M indicates | that | this op- |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --------- | --- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
theinvariantsoftheicestrainratetensor(cid:15)˙:
| erator represents |     | concentration |     | changes | due | to mechanical |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
interactionsonly. D M c isequaltothetotalsea-iceareawhich 1 (cid:18) ∂u ∂u (cid:19)
|     |     | D t |     |     |     |     |     | (cid:15)˙ = | i + | j   |     |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     | ij          |     |     | .   |     |     |     | (12) |
is eliminated due to the collisions of floes per unit of time. 2 ∂x ∂x
j i
SubtractingEq.(8)fromEq.(9),
Definingthedeviatoricstraintensor,(cid:15)˙(cid:48)
|     |     |     |     |     |     |     |     |     |     |     |     |     | =(cid:15)˙ | −δ ∇·u/2, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     | ij  | ij         | ij        |     |
0+ e q u a l t o t h e di v e r g e n ce -fr ee p a r t o f (cid:15)˙ , t w o r e lev a n t i n v a ri -
| Z   |     |     |     |     |     |     |     |     |     |     |     | i j |     |                |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
|     |     |     | D c |     |     |     |     |     |     |     |     |     |     | (cid:48)| 1/ 2 |     |
L (r)dr =∇·u− M . a n t s m a y b e w r it t e n a s E = ((cid:15) I , (cid:15) II ) = ( ∇ · u ,2 | − (cid:15)˙ ) . T h e
M
|     |     |     | Dt  |     |     |     |     | firstinvariantistheflowdivergenceandthesecondiscalcu- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
0−
|     |     |     |     |     |     |     |     | lated from | the determinant |     | of the | deviatoric | strain | rate | ten- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------ | ---------- | ------ | ---- | ---- |
This result implies that L (r) has a δ(r) component sor,andisequaltothemaximalshearstrainrate.Giventhese
M
|                                                      |            |                 |      |          |             |           |         | definitions, | we parameterize      |     | the | rate of | ice area | loss | due to |
| ---------------------------------------------------- | ---------- | --------------- | ---- | -------- | ----------- | --------- | ------- | ------------ | -------------------- | --- | --- | ------- | -------- | ---- | ------ |
| due to                                               | open water | creation        |      | in floe  | collisions, | or        | the in- |              |                      |     |     |         |          |      |        |
| tegral on                                            | the        | infinitesimally |      | small    | range       | near size | zero    | collisionsas |                      |     |     |         |          |      |        |
| would have                                           | vanished.  |                 | Note | that the | function    | δ(r)      | is the  |              |                      |     |     |         |          |      |        |
|                                                      |            |                 |      |          |             |           |         | D c          | 1                    |     |     |         |          |      |        |
|                                                      |            |                 |      |          |             |           |         | M =          | ((cid:15) −||E||)≤0, |     |     |         |          |      | (13)   |
| two-dimensionaldeltafunction:δ(r)=δ([r,h])≡δ(r)δ(h). |            |                 |      |          |             |           |         |              | I                    |     |     |         |          |      |        |
|                                                      |            |                 |      |          |             |           |         | Dt           | 2                    |     |     |         |          |      |        |
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2125
which allows us to write the mechanical interaction term in with respect to its first two arguments, each interaction pair
theFSTDequationas (r ,r )iscountedtwiceintheintegralinEq.(15).Thisrep-
1 2
resents the rate of change in the number of floes of size r
1 3
L M =δ(r)(cid:15) I + (||E||−(cid:15) I )[δ(r)−L c ]. (14) due to mechanical interactions. In reality, some floe colli-
2
sionsmayleadtoareboundanderosionoffloeedgesrather
This formulation is exactly equivalent to that of Thorndike
thantoamergingofthefloes,yetwedonotaccountforsuch
etal.(1975);seeAppendixfordetails.Inthecaseoficeflow
a process. The first term on the right-hand side of Eq. (15)
characterizedbypuredivergence,E=(∇·u,0)and∇·u>
representstheincreaseinfloenumberatsizer duetocolli-
0,themechanicalinteractionsarerepresentedasadeltafunc-
sionsbetweenfloesofothersizes,andthesecondtermrep-
tion at r =0, representing only the formation of open wa-
resentsthelossinfloenumberatsizer duetocombination
terbydivergenticeflow.Inpureconvergence,E=(∇·u,0)
of floes of size r with other floes. Equation (15) is a gener-
and∇·u<0,andmechanicalinteractionscreateopenwater
alizationoftheSmoluchowskicoagulationequationthathas
through collisions and L (r)=|∇·u|L (r). When the ice
M c beenpreviouslyusedtomodelthesea-icethicknessdistribu-
flow is characterized by shear motions, ||E||=(cid:15) , and col-
II tion(Godlovitchetal.,2011).IfwemultiplyEq.(15)bythe
lisionsstilloccurduetothedifferentialmotionofneighbor-
area of a floe of size r, we obtain the rate of change of the
ing floes, which forms open water at a rate of DMc =(cid:15) /2
Dt II fractionalareacoveredbyfloesofsizer duetomechanical
persecond.Otherchoicesof DMc couldsatisfyEq.(10),but
Dt interactions,whichisnothingbutthedefinitionofL M (r):
the Thorndike parameterization meets the intuitive require-
ments that in pure divergence no collisions occur, while in ∂f(r) =(πr2) ∂N(r) =L (r);(r (cid:54)=0). (16)
M
pureconvergencetheydo,andinpureshear,collisionsoccur ∂t ∂t
such that the rate of open water formation per unit strain is Wehavealreadyconcludedabovethatawayfromr =0we
reducedrelativetothecaseofpureconvergence. haveL (r)=L (r).Thereforetheaboveequationgives
M c
TheeffectsofmechanicalinteractionsontheFSDarerep-
∂N(r)
resentedbyZhangetal.(2015)similarlytoEq.(10),withthe L (r)=(πr2) , (17)
rateofarealoss(our DMc)takenfromHiblerIII(1980),and c ∂t
Dt
assumingthatallfloesofdifferentsizeshavethesameITD. where∂N/∂t istakenfromEq.(15).Werepresenttheker-
In our joint FSTD formulation, the mechanical interactions nel K(r ,r ,r) as the product of two factors. The first is
1 2
arerepresentedforfloescharacterizedbybothspecificthick- theprobabilityofcollisionviaridgingorraftingoftwofloes
ness and specific size. Here, interactions between floes are of size r and r , termed P (r ,r ) where the subscript
1 2 coll 1 2
treatedasbinarycollisions,andourmodeldoesnotconsider “coll”iseither“ridge”or“raft”,andtheprobabilitiesareto
multiple simultaneous collisions in a single time step. Such bedefinedmorespecificallyshortly.
multiple collisions lead to clustering, which is relevant for The second factor is a delta function, δ(r−R(r ,r )),
1 2
granularmediaundergoingdeformation(ShenandSankaran, that limits the pairs of collision partners to only those that
2004),withseaicebeingapossibleexample.However,Her- formafloeofsizer =R(r ,r ),specifiedbelow,andwhose
1 2
man(2013)demonstratedinnumericalsimulationsthatfloes areaissmallerthantheareaofthetwocollidingfloescom-
mayalsoaggregateintoclustersviaasequenceofbinaryin- bined.Notingagainthatthenumberdistributionandareadis-
teractionsbetweenpairsoffloes. tribution are related through N(r)=πr2f(r), we combine
The rearrangement of floe area in response to a unit Eq.(17)and(15)tofind
amountofopenwaterformation,L (r),isrepresentedusing
e
a
q
c
u
o
a
ll
l
i
t
s
o
io
t
n
he
ke
n
r
u
n
m
el
b
K
er
(r
of
1 ,
c
r
o
2
ll
;
i
r
si
)
o
.
n
L
s
e
p
tK
e
c
r
(
u
r
n
1
i
,
t
r
ti
2
m
;r
e
)
b
d
e
r
t
1
w
d
e
r
e
2
n
d
fl
r
o
b
e
e
s
L
c
(r)=L∗
c
ZZ " 1
2πr
r
2
2
r2
f(r
1
)f(r
2
)Pcoll (r
1
,r
2
)δ(r−R(r
1
,r
2
))
in the range (r ,r +dr ) and floes in the range (r ,r +
r1,r2 1 2
1 1 1 2 2 #
d
o
r
f
2
o
)
p
,
e
t
n
ha
w
t
a
f
t
o
e
r
r
m
fo
fl
rm
oe
a
s
ti
i
o
n
n.
th
I
e
n
r
g
a
e
n
n
g
e
e
ra
(
l
r
,
,
th
r
e
+
fl
d
o
r
e
),
nu
p
m
er
b
u
e
n
r
i
d
t
i
a
st
r
r
e
i
a
-
−
π
1
r2
f(r)f(r
2
)Pcoll (r,r
2
)δ(r
1
−R(r,r
2
)) dr 1dr
2
. (18)
2
bution subject to mechanical combination of floes evolves
ThecoefficientL∗ isanormalizationconstantensuringthat
accordingto c
the integral over L (r) is 1 (Eq. 11). In the discretized ver-
c
∂N(r) Z Z (cid:20) 1 sion of Eq. (18), two floe classes of discrete size rd and
= N(r )N(r )K(r ,r ;r) 1
1 2 1 2
∂t 2 rd which combine to form floes of discrete size rd do not
r1r2
ne
2
cessarilysatisfyπ(rd)2hd+π(rd)2hd=π(rd)2hd.Icevol-
(cid:21) 1 1 2 2
−N(r)N(r )K(r,r ;r ) dr dr , (15) umeconservationthatisindependentofthediscretizationis
2 2 1 1 2
achieved by determining the newly formed area of the new
wherethenotation R dr istakentomeananintegraloverall floes,ineachtimestep,usingtheconstraintthatvolumemust
r beconserved:
floe sizes and thicknesses resolved by the model. The fac-
tor of 1/2 prevents double-counting: since K is symmetric (cid:49)f(rd)hd+(cid:49)f(rd)hd=−(cid:49)f(rd)hd,
1 1 2 2
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2126 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
where(cid:49)f(r)istheareachangeatsizer inasingletimestep is not overly sensitive. Finally, we assume that ridging oc-
duetothemechanicalinteractionconsideredhere.Thusthe curs for floes thicker than 0.3m, and rafting occurs when
totalvolumelostbyfloesatsizerdandrd(left-handside)is bothfloesarethinnerthan0.3m,consistentwiththestudyof
1 2
equal to the corresponding volume gained at size rd (right- Parmerter(1975),withasmoothtransitionbetweenthetwo
3
handside). regimesimplementedbyacoefficientγ(h)whichtendsto1
forthicknessesthatarepronetoraftingandto0forridging:
2.2.1 Probabilityofcollision
K(r ,r ;r)=γ(h )γ(h )P (r ,r )δ(r−R (r ,r ))
1 2 1 2 raft 1 2 raft 1 2
We choose the functions P (r ,r ) to be proportional to +(1−γ(h )γ(h ))P (r ,r )δ(r−R (r ,r )),
coll 1 2 1 2 ridge 1 2 ridge 1 2
t i h f e pl p a r c o e b d a r b a i n li d ty om th l a y t i t n w t o he fl d o o es m o a f in s , iz a e nd r 1 th a e n y d ar r e 2 c w al i c ll ul o a v t e e r d la i p n γ(h)= 1 − 1 tanh (cid:2) (h−0.3)/0.05 (cid:3) .
2 2
a similar manner for both mechanical processes (rafting or
ridging). We consider such an overlap as an indication that
mechanical interaction has occurred. The area of each floe 2.2.2 Newfloesize
that may be deformed due to mechanical interactions is re-
stricted to a small region near the edge of the floe, repre- Theicearealostinaninteractionisdifferentforraftingand
sented in our model by a narrow annulus, which we term a ridging.Inrafting,theentirecontactzoneisreplacedbyice
“contactzone”,ofwidthδ =δ orδ =δ atthefloe whose thickness is the sum of that of the original floes. In
cz ridge cz raft
edge,whichdependsonthefloesizeandtheinteractiontype; ridging,thecontactzoneisincreasedinthicknessbyafactor
wealsotermtheinteriorsoffloes“cores”(Fig.1).Thearea of5,compressingitsareabyafactorof1/5(Parmerterand
ofasinglefloeofsizes isthereforebrokendownas Coon,1972).Giventhatourmodelassumeseachfloehasa
uniformthickness,wetreatfloesformedbyridgingorrafting
πs2=A core (s)+A cz (s)=π(s−δ cz )2+π(2δ cz s−δ c 2 z ). tobeofuniformthickness,chosentoconservevolume.This
choiceeliminatestheneedforkeepingtrackofsea-icemor-
The above-defined probability of collision between floes of
phology. Observations (Collins et al., 2015; Kohout et al.,
sizer andr isproportionaltotheproductofcontactzone
1 2 2015) have indicated that floes may break up along ridges,
areas divided by the open ocean area, A, not including the
in which case Eq. (18) may be used to provide information
coreareas:
abouttheridgedensity.Thisisapotentialfutureextensionof
P (r ,r )∝ A cz (r 1 )A cz (r 2 ) . thepresentwork.
coll 1 2 (A−A core (r 1 )−A core (r 2 ))2 Assumingwithoutlossofgeneralitythatr 1 ≤r 2 ,thearea
ofthenewlyformedfloesisthereforegivenbythesumofthe
The above probability that two floes will collide is based
areasminusthearealosttoeitherridgingorrafting.Wethen
ongeometricconstraints.However,therateofcollisionsde-
dividethisareabyπ andtakethesquareroottofindthesize
pendsalsoontheicestrainratetensor(cid:15)˙ asexplainedabove,
ofthenewlyformedfloes.Thethicknessoftheformedfloe
and this tensor depends on external forcings such as the
iscalculatedfromvolumeconservation.Wethereforehave
strength of the prevailing winds and currents (Shen et al.,
1987; Herman, 2011, 2013; Bennetts and Williams, 2015), [r,h]=R([r 1 ,h 1 ],[r 2 ,h 2 ]) raft
butthedeterminationofthatrelationshipisnotafocusofthe r !
1 V(r )+V(r )
FSTDmodelpresentedhere. = r 1 2+r 2 2− 2 A cz,raft (r 1 )/π, 1 πr2 2 ,
Data of the morphology and width distribution of ridges
andraftsasafunctionofthesizeofthecombiningicefloes [r,h]=R([r ,h ],[r ,h ])
1 1 2 2 ridge
are scarce, though there are indications that rafts can be r !
4 V(r )+V(r )
substantially larger than ridges (Hopkins et al., 1999). We = r2+r2− A (r )/π, 1 2 ,
1 2 5 cz,ridge 1 πr2
crudelydefinethewidthofthecontactzoneinridgingtobe
5m, or the size of the smaller of the two combining floes,
whereV(r)=V([r,h])=hπr2isthevolumeofanicefloe.
whicheverissmaller:
2.3 Swellfracture
δ (r ,r )=min(5m,r ,r ).
ridge 1 2 1 2
Sea surface height variations due to surface ocean waves
For rafting, we assume a larger portion of the smaller floe
strain and possibly break sea-ice floes into smaller floes of
maybeuplifted,upto10m:
varying sizes. Since this process does not create or destroy
δ (r ,r )=min(10m,r ,r ). sea-icearea,theresponseoftheFSTDtothefractureofsea
raft 1 2 1 2
icebywavesobeystheconservationlaw
Bothchoicesleadtolargerridgesandraftsasthesizeofthe
Z
interacting floes increases. Given observations of these pro- L (r)dr =0,
W
cesses,onecanrefinetheabovechoices,towhichourmodel
r
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2127
Table4.VariablesusedintherepresentationofthefractureoficebysurfacewavesintheFSTDmodel.
|     | Variable Description                              |     |     |     |     |     |     |     | Section |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- |
|     | LW IcefracturecomponentofFSTDmodel                |     |     |     |     |     |     |     | 1       |
|     | (cid:127)(r,t) Areaoffloesofsizerfracturedbywaves |     |     |     |     |     |     |     | 2.3     |
F(r,s) Floesizeandthicknessdistributionofnewfloesformedbythefractureoffloesofsizerbywaves 2.3
α(λ,h) Attenuationcoefficient(perfloe)forwavesofwavelengthλencounteringiceofthicknessh 2.3
|     | D Widthofcomputationaldomainontowhichwavesareincident   |     |     |     |     |     |     |     | 2.3 |
| --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | S(λ) Incidentwavespectrum                               |     |     |     |     |     |     |     | 2.3 |
|     | η(x) Seasurfaceheightrecord                             |     |     |     |     |     |     |     | 2.3 |
|     | φi PhaseofithcomponentofseasurfaceheightFourierspectrum |     |     |     |     |     |     |     | 2.3 |
a(λi) amplitudeofithcomponentofseasurfaceheightFourierspectrum 2.3
|     | (cid:15) crit Criticalstrainrateforbreakingoffloes |     |     |     |     |     |     |     | 2.3 |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Hs Significantwaveheight(heightof1/3highestwaves)  |     |     |     |     |     |     |     | 2.3 |
X∗
|     | Collectionofpotentialfracturelengths |     |     |     |     |     |     |     | 2.3 |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
R(r,h) Histogramoflengthsthatleadtofractureoficeofthicknessh 2.3
|        | λz Wavelengthcorrespondingtozero-crossingperiod   |           |           |                 |                      |     |     |     | 2.3 |
| ------ | ------------------------------------------------- | --------- | --------- | --------------- | -------------------- | --- | --- | --- | --- |
|        | cg Groupvelocityofwavesofwavelengthλtocrossdomain |           |           |                 |                      |     |     |     | 2.3 |
|        | Tz Zero-crossingperiodforwaverecord               |           |           |                 |                      |     |     |     | 3   |
| w h er | e L ( r ) is t h e                                | t im e ra | te o f    | c h a n g e o   | f fl o es o f s iz e |     |     |     |     |
|        | W                                                 |           |           |                 |                      | 3   |     | 4   | 6   |
|        |                                                   |           |           |                 |                      |     |     | -   | -   |
| a n d  | th ic k ne s s r = ( r ,h                         | ) d ue    | to th e f | ra c t u re o f | ic e b ys u rf a c e |     |     |     |     |
2.5
| waves | in Eq. 2, and | the integral | is  | over all sizes | and thick- |     |     |     |     |
| ----- | ------------- | ------------ | --- | -------------- | ---------- | --- | --- | --- | --- |
)m
|                                                   |                          |     |      |             |              | 2   | - 2 |     |     |
| ------------------------------------------------- | ------------------------ | --- | ---- | ----------- | ------------ | --- | --- | --- | --- |
| nesses                                            | (a list of the variables |     | used | to describe | the response | ( s |     |     |     |
| oftheFSTDtoicefracturebywavesisprovidedinTable4). |                          |     |      |             |              | s e |     |     |     |
n 1.5
| Supposethatanareaoffloes(cid:127)(r,t)dr |     |     |     | withsizesbetweenr |     | k 2  |       |     |     |
| ---------------------------------------- | --- | --- | --- | ----------------- | --- | ---- | ----- | --- | --- |
|                                          |     |     |     |                   |     | c -  |       |     |     |
|                                          | +   |     |     |                   |     | ih 1 | -4 -6 |     |     |
a n d r d r is f ra c tu r e d p er u n it t im e . L e t n e w fl oe s r es u l ti n g T -8 0
- 1
f r o m t hi s pr oc e s s h a v e th e fl o e s iz e d i st r ib u tio n F ( r , s ) d s , 0.5 -6 -8 10
|     |     |     |     |     |     | -4  |     | -   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
equaltothefractionof(cid:127)(r,t)thatbecomesfloeswithsize
|          |                                        |     |     |     |     | 4 6 | 8 10 | 12 14 | 16  |
| -------- | -------------------------------------- | --- | --- | --- | --- | --- | ---- | ----- | --- |
| betweens | ands+ds.Therateofchangeofareaoffloesof |     |     |     |     |     |      |       |     |
Period (s)
sizer duetofracturebyoceansurfacewavesisthen
Z Figure 2. The natural logarithm of the attenuation coefficient α
L (r)=−(cid:127)(r,t)+ (cid:127)(s,t)F(s,r)ds. (19) calculated by Kohout and Meylan (2008) (dashes, inside the red
W
s box) and a quadratic fit to this attenuation coefficient that is used
inSect.2.3(solidlines).Solidcontoursoutsideoftheredboxare
The first term is the loss of fractional area of size r that is extrapolatedusingthequadraticfit.Thefitisgivenbylnα(T,h¯)=
−0.3203+2.058h¯−0.9375T−0.4269h¯2+0.1566h¯T+0.0006T2.
fracturedperunittime,andthesecondistheincreaseinthe
| areaoccupiedbyfloesofsizer |     |     | duetothefractureoffloesof |     |     |     |     |     |     |
| -------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
largersizes.
KohoutandMeylan(2008)modeledfloesaslongfloating
elasticplates,andshowedoceansurfacewavestobeattenu- theattenuationcoefficientsfromafunctionofwaveperiodto
atedexponentiallyasafunctionofthenumber,(cid:51),oficefloes afunctionofwavelengthusingthedeep-watersurfacegrav-
thewavesencounterastheypropagateintoanicepack.Wave itywavedispersionrelationλ=gT2/2π.
energythereforedecaysasexp(−α(cid:51)),wheretheattenuation Scattering models may under-predict attenuation rates
|     | ¯   |     |     |     | ¯   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
coefficientisα(T,h),T isthewaveperiod,andhthemean (Williams et al., 2013b), which may allow for longer pene-
ice thickness. We approximate the number of floes per unit trationofwavesintotheMIZthanisphysicallyrealistic.Up-
|     | c(2r¯)−1, |     |     |     | r¯  |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
distance as where c is the ice concentration and dated models of the wave attenuation (Bennetts and Squire,
the average effective radius, and approximate this attenua- 2012)suggestdifferentattenuationcoefficientsasafunction
tion by fitting the attenuation coefficient α(T,h) ¯ calculated ofwaveperiodandicethickness.Wetestedourmodelwith
by Kohout and Meylan (2008) (their Fig. 6) to a quadratic the Bennetts and Squire (2012) attenuation coefficient, and
function of the period and mean thickness (Fig. 2). Kohout show in the Supplement (Sect. S1.4) that our FSTD model
andMeylan(2008)onlyreportanattenuationcoefficientfor can be sensitive to the choice of attenuation model. Future
wave periods longer than 6s and thicknesses less than 3m applications of this FSTD model should therefore carefully
(redboxinFig.2),soweextrapolatetoshorterperiodsand consider the wave attenuation formulation, based on both
higherthicknessesusingthisfitwhennecessary.Weconvert modelestimatesandobservations(e.g.,Meylanetal.,2014).
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2128 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
andr+dr
Wedeterminethefloesizedistributioncausedbythefrac- betweenr andthicknessh s whenwavesaffecta
ture of ice of size s by surface waves, F(s,r)dr, based on fullyice-covereddomainoflengthD.Weassumethatafloe
thewavespectrumS(λ)(inunitsofmeters,seeBouwsetal., ofsizeswillfractureonlywhenX∗ −X∗=r <s,andthat
|     |     |     |     |     |     |     |     |     |     |     |     | i+1 | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1998,p.11),whichisequaltothewaveenergyspectrumnor- thenumberoffracturesofsizeriseitherproportionaltoR(r)
malizedbyρg.Williamsetal.(2013a)usedaRayleighdis- (forr <s),or0(forr>=s).Thetotallengthoffracturesof
tributionforthestrainspectrumtopredictbreakingoffloes; sizer isthusproportionaltorR(r),or0,forr >s.Thefloe
however this does not determine the floe sizes produced by size distribution formed by the fracture of a floe of size s,
thebreaking,whichweaddressasfollows.First,thecontin- F(s,r)isthereforeequaltothetotallengthoffloesofsizer
uous spectrum and attenuation coefficients are used to gen- thatareformedbythisfracturingofafloeofsizes,normal-
R∞
erate realizations of the sea surface height. Next, these re- izedsuchthat F(s,r)dr =1,i.e.,
0
| alizations | are used | to  | calculate | the strain | applied | to the ice |     |     |     |     |     |        |     |     |     |
| ---------- | -------- | --- | --------- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|            |          |     |           |            |         |            |     |     |     |     |     | rR(r,h | )   |     |     |
floes. Finally, a statistical distribution of resulting floe size s
|                                                        |     |     |     |     |     |     | F(s,r)=F([s,h |     |     | s ],[r,h])= |     |     | δ(h−h | s ). | (21) |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ----------- | --- | --- | ----- | ---- | ---- |
| iscalculatedfromtheseasurfaceheightplusacriticalstrain |     |     |     |     |     |     |               |     |     |             | s   |     |       |      |      |
R
|            |         |         |           |         |     |            |     |     |     |     |     | rR(r,h | s )dr |     |     |
| ---------- | ------- | ------- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- |
| condition. | Details | of this | procedure | follow, | and | are demon- |     |     |     |     |     |        |       |     |     |
0
stratedindetailinthesupplementarymaterialsectionS3.
|     |     |     |     |     |     |     | The | upper | limit | of the | normalization | integral | in  | the denom- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | ------------- | -------- | --- | ---------- | --- |
Weconsiderforsimplicityaone-dimensionaldomainand
assumethatfloesflexwiththeseasurfaceheightfieldη(x), inator is truncated to s because the integrand vanishes for
h∂2η larger values of r as explained above. The delta function
| experiencingastrain(cid:15)= |     |     |     | (Dumontetal.,2011,p.4).If |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2∂x2 δ(h−h ) represents the fact that fracture does not change
| the maximum |         | strain, | which occurs  | at      | the trough | and crest                 |                | s          |       |                        |              |      |              |     |        |
| ----------- | ------- | ------- | ------------- | ------- | ---------- | ------------------------- | -------------- | ---------- | ----- | ---------------------- | ------------ | ---- | ------------ | --- | ------ |
|             |         |         |               |         |            |                           | ice            | thickness, | i.e., | any                    | floes formed | from | the fracture |     | of ice |
| of a wave,  | exceeds | an      | empirically   | defined |            | value (cid:15) crit , the |                |            |       |                        |              |      |              |     |        |
|             |         |         |               |         |            |                           | withthicknessh |            |       | willalsohavethicknessh |              |      | .            |     |        |
| floe will   | break.  | For a   | monochromatic |         | swell      | wave of wave-             |                |            |       | s                      |              |      | s            |     |        |
length λ, this leads to floes of size λ/2. For a discretiza- Thefunction(cid:127)(r,t)dr isthefractionalareathatbelongs
|           |                                                    |      |        |             |         |         | to   | floes of | size      | between | r and  | r+dr     | that is  | fractured | per |
| --------- | -------------------------------------------------- | ---- | ------ | ----------- | ------- | ------- | ---- | -------- | --------- | ------- | ------ | -------- | -------- | --------- | --- |
| tionintoN | λ spectrallineswithspacing(cid:49)λ,spectralampli- |      | √      |             |         |         |      |          |           |         |        |          |          |           |     |
|           |                                                    |      |        |             |         | R       | unit | time.    | It is set | equal   | to the | the area | fraction | covered   | by  |
| tudes are | defined                                            | as a | = 2S(λ | )(cid:49)λ, | so that | S(λ)dλ≈ |      |          |           |         |        |          |          |           |     |
|           |                                                    |      | i      | i           |         |         |      |          |           |         |        |          |          |           |     |
PNλ S(λ)(cid:49)λ=PNλ floesofsizer,f(r),multipliedbythefractionofthedomain
a2/2.Letthewidthofthedomainto
| i=1                           |     | i=1 | i   |     |                   |     | reachedbywavesofgroupvelocityc             |     |     |     |     |     | perunittime,c |              | /D, |
| ----------------------------- | --- | --- | --- | --- | ----------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | ------------- | ------------ | --- |
| whichtheFSTDmodelisappliedbeD |     |     |     |     | (e.g.,thewidthofa |     |                                            |     |     |     |     | g   |               |              | g   |
|                               |     |     |     |     |                   |     | multipliedbytheprobabilitythatfloesofsizer |     |     |     |     |     |               | willfracture |     |
GCM grid cell which borders on open water). A realization bywaves.Tocalculatethisprobability,wenotethatr(cid:48)R(r(cid:48))
oftheseasurfaceheightη(x)isgeneratedaccordingto
|     |     |     |     |     |     |     | is the | total | length | of the    | domain | covered | by waves | that | can |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------ | --------- | ------ | ------- | -------- | ---- | --- |
|     |     |     |     |     |     |     |        |       |        | (cid:48). |        |         | (cid:48) |      |     |
Nλ (cid:18) 2πx (cid:19) b re ak fl o e s i n to s i z e r I n teg r at i n g th i s o v er r f r o m 0 to a s iz e
| )=  | X   | −α(λi)xjcos |     | j +φ |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
η(x j a i e i , (20) r, w e fi n d t h e t o t a l w i d th o f t h e d o m a i n c o v e r e d by w a v e s
λ
|     | i=1 |     |     | i   |     |     |      |             |     |       |              |     |          |          |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ----- | ------------ | --- | -------- | -------- | --- |
|     |     |     |     |     |     |     | that | can produce |     | floes | smaller than | r,  | which is | the same | as  |
wherexrangesfrom0toD,therandomphasesφ aredrawn thelengthofthedomaincoveredwithwavesthatcanbreak
i
|                                              |     |     |     |     |     |       | floesofsizer |     | intosmallersizes.Normalizingbythedomain |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | ----- | ------------ | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| fromauniformdistributionbetween0and2π,andα(λ |     |     |     |     |     | i )is |              |     |                                         |     |     |     |     |     |     |
theattenuationcoefficientforwavesofwavelengthλ . widthD,wefindthefinalfactorintheexpressionfor(cid:127):
i
| If the | strain | is calculated | locally | from | η(x), | the critical |     |     |     |     |     |     |     |     |     |
| ------ | ------ | ------------- | ------- | ---- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |        |               |         |      |       |              |     |     |     |     |    |     |     |    |     |
Z r
| strain is | reached | almost | everywhere | for | a realistically | gen- |                           |     |     |      |     |                               |               |     |      |
| --------- | ------- | ------ | ---------- | --- | --------------- | ---- | ------------------------- | --- | --- | ---- | --- | ----------------------------- | ------------- | --- | ---- |
|           |         |        |            |     |                 |      | (cid:127)([r,h],t)=f(r)(c |     |     | /D) |     | r (cid:48) R(r (cid:48) ,h)dr | (cid:48) /D. |     | (22) |
erated wave field (see the Supplement, Fig. S10). Instead, a g
| floeisassumedtofracturewhenitisstrainedbetweenthree |         |         |         |         |        |                |     |       |          |     | 0        |         |        |      |       |
| --------------------------------------------------- | ------- | ------- | ------- | ------- | ------ | -------------- | --- | ----- | -------- | --- | -------- | ------- | ------ | ---- | ----- |
| successive                                          | local   | extrema | of η,   | where   | points | are defined to |     |       |          |     |          |         |        |      |       |
|                                                     |         |         |         |         |        |                | The | group | velocity | is  | taken to | be that | of the | mean | zero- |
| be extrema                                          | if they | are     | a local | maximum | or     | minimum over   |     |       |          |     |          |         |        |      |       |
q
|            |        |     |             |       |        |              | crossing |     | wavelength, |     | c = λ | z g . Observations |     | of  | wave |
| ---------- | ------ | --- | ----------- | ----- | ------ | ------------ | -------- | --- | ----------- | --- | ----- | ------------------ | --- | --- | ---- |
| a distance | of 10m | on  | both sides, | based | on the | observations |          |     |             |     | g     |                    |     |     |      |
8 π
of Toyota et al. (2011) who find this to be the order of the propagationinice(Collinsetal.,2015)havesuggestedthat
smallest floe size affected by wave fracture. For a triplet of thepropagationspeedoffractureinicemaybeslowerthan
successive extrema (max, min, max; or min, max, min) of the group velocity of surface waves. With more data, the
η, (x∗ ,x∗,x∗), the strain felt by the floe at x∗ is calcu- abovechoiceforc maybere-evaluated.
| i−1 | i i |     |     |     |     | i   |     |     |     | g   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lated by a finite difference approximation (see the Supple- The effects of the fracture of ice by waves on the FSD is
ment, Sect. S3). When the magnitude of this strain exceeds represented by Zhang et al. (2015) based on an expression
the critical strain, (cid:15) =3×10−5, the floe will break. This similartoEq.(19),assumingthatonlyfloeswithhorizontal
crit
determinesasetofpointsatwhichafloeofthicknesshwill size larger than a specified threshold break, that a fractured
fracture, X∗(h). From this set of points we define the size floeisequallylikelytoformanysmallersizewithinaspec-
i
|     |     |     | X∗  | −X∗. |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of the fractured floe as i+1 We form a histogram ified range, and that all floes in a given size class have the
i
R(r,h)ofthenumberofoccurrencesofeachfractureofsize same ITD. In the representation in the present paper of the
r, which is normalized so that R rR(r,h )dr =D. In this effectsoficefracturebywavesonthejointFSTD,thewave
s
way,R(r,h s )dr isequaltothenumberoffractureswithsize spectrumplaysacentralroleindeterminingtheresultingfloe
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2129
sizes, as well as the propagation distance over which ocean sizes between 0.5 and 156m. There are 14 thickness cate-
waves are attenuated by the ice field. Information about the gories,13ofwhichareequallyspacedbetween0.1to2.5m.
specific thickness of individual floe sizes informs the strain To conserve volume when thick floes combine or grow due
rate failure criterion and therefore determines which floes tofreezing,thefourteenththicknesscategoryincorporatesall
willbefractured. thicknesses greater than 2.5m. We examine the numerical
convergenceofthemodelintheSupplement(Sect.S2),find-
ingthatincreasingthisresolutiondoesnotsignificantlyalter
3 Modelresults thenumericalresults.
The difference between the model state after a single
To demonstrate and understand the model’s response to a 1h time step and the model initial conditions is shown in
variety of forcing scenarios, we first examine its response Fig. 3b–d. Cooling leads to growth in both thickness and
over a single time step in three runs with idealized forcing size (Fig. 3b) with the impact of lateral growth being less
fields. Each of these scenarios applies one of the follow- visible than the change in thickness. The shift in thickness
ing forcing fields: a net surface cooling Q=−100Wm−2 is seen by the negative tendency (blue shading) for thick-
whichinducesicegrowth,arateoficeflowconvergenceof nesses smaller than the maximum of the initial distribution,
∇·u=−5×10−9s−1 which induces floe collisions, and a and positive tendency at sizes larger than the initial maxi-
surface gravity wave field of a single wavelength λ=56m mum(redshading).Thesetendenciescorrespondtotheshift-
and amplitude of 1m, leading to ice fracture. The model is ing of floes from thinner to thicker floes due to the freez-
initialized with a size and thickness distribution composed ing.Theshiftinhorizontalsizeislessapparentinthefigure,
of two Gaussian peaks (Fig. 3a). The first (referred to as due to the separation of scales between size and thickness;
size I below) has a mean size of 90m and a mean thick- lateral growth rates are comparable to vertical growth rates
ness of 0.25 m. Ice at this size and thickness is suscepti- (1cmday−1), but given that there is more than an order of
ble to fracture by surface waves and rafting. The second magnitudedifferencebetweenthefloesizeandthickness,the
peak (size II) has a mean size of 15m and a mean thick- sizechangecorrespondstoasmallerrelativechangethanthe
ness1.5m.Iceatthissizeandthicknesstendstoridgerather thicknesseschange.Thesizeresponsewouldbemoreappar-
than raft, and is not susceptible to fracture given our speci- entforsmallerinitialfloesizesnotincludedinthisidealized
fiedwavefield.Thissecondpointisimportant,asitdemon- modelexperiment.
strates a possible scenario in which knowledge of the ITD Mechanical interactions (Fig. 3c) lead to growth at three
and FSD, separately, would not be sufficient to evolve the distinct clusters of size and thickness. The first, due to the
FSTD,assomefloes,independentoftheirthickness,willnot self-interaction(rafting)offloesofsizeI,isshownasaposi-
fracture. The initial sea-ice concentration is 75%. The do- tivetendencyatafloesizeof123mandthicknessof0.35m.
main width is D=10km, and the width of the lead region This cluster would not be resolved in a model that repre-
issettober =r =0.5m,thesmallestfloesizeresolved sentedtheicethicknessdistributiononly.Thesecondcluster
lw min
in this model. The critical strain amplitude for flexural fail- isduetoaridginginteractionbetweenfloesofsizeIandII,
ure, (cid:15) , is set to 3×10−5 in line with other studies (Ko- leadingtonewfloesofaround90msizeand0.5mthickness.
crit
houtandMeylan,2008;Dumontetal.,2011).Williamsetal. The third, due to self-interaction (ridging) between floes of
(2013a)formulatedamorecomplexexpressionforthecriti- sizeII,leadstoapositivetendencyatfloesizesaround17m
calfailurelimit,andthiswasfoundtohaveasignificantef- andthicknessaround1.7m.Boththesecondandthirdclus-
fectonwavefracturing(Williamsetal.,2013b).Weexamine tersoffloeswouldnotberesolvedinamodelthatrepresents
themodelsensitivitytosomeofthemainparametersusedin thefloesizedistributiononly,showingagaintheimportance
thesemodelsimulationsintheSupplement(Sect.S1). ofrepresentingthejointFSTD.
Whentwofloesofsizer ands combineduetoraftingor Swell fracture (Fig. 3d) leads to the fracturing of many
riding interactions, they form a new floe with effective ra- of the floes of size I, shown as a negative tendency at the
dius r(cid:48)>max(r,s). For an arbitrary floe size discretization eliminatedsizeclass.FloesofsizeIIarenotaffectedbecause
into size bins, this new size may not lie within a bin repre- they are smaller than twice the wavelength of the specified
senting a size larger than those of the two interacting floes. surface gravity wave field. Since the specified wave field is
Asaresult,interactingfloesmayaccumulateatasinglebin monochromatic,theareaoffloesofsizeIthatarebrokenis
sizeratherthanmoveintobinsrepresentinglargersizes.The shown as a positive tendency at a floe size equal to half of
minimum bin resolution necessary to avoid this problem is thewavelengthofthesurfacegravitywave,λ/2=28m.Ice
set by the interaction of two floes that are the same size r, thicknessdoesnotchangewhentheiceisfractured.
with r smaller than the ridge width δ . When two such Next, two 1-month simulations are performed using the
ridge
small floes interact via ridging in our model, one of them same initial distribution to show the behavior of the model
becomes 5 times thicker and its area is reduced by a factor forced by two different fixed strain rate scenarios (Fig. 4).
√
of 5. They therefore form a floe of size 6/5r. We select The first (Fig. 4a, b) simulates convergence of fixed magni-
√
a variable discretization, with r n+1 = 6/5r n , with 64 floe tude ((cid:15) I =−10−7,(cid:15) II =0)s−1, and the second (Fig. 4c, d)
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2130 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
Figure 3. Response of the FSTD to idealized single-process experiments over a single time step (Sect. 3). (b) Change in response to
thermodynamicforcingonly.(c)Changeinresponsetomechanicalforcingonly.(d)Changeinresponsetowaveforcingonly.Solidblack
contoursin(b–d)showtheinitialfloesizeandthicknessdistribution,andcontourintervalsarepowersof10.Thecolorbarontheright
−1).Warmcolorsindicateanincreaseinfractionalarea,
correspondstothechangeintheFSTDinunitsoffractionalareapertimestep(1s
coolcolorsindicateadecreaseinfractionalarea.
|     |     | (a)      | Convergence Only | (b)            |               | Day 0     |       | Day 15        |     |               | Day 30 |     |     |
| --- | --- | -------- | ---------------- | -------------- | ------------- | --------- | ----- | ------------- | --- | ------------- | ------ | --- | --- |
|     |     |          | 2                |                |               |           |       |               |     |               |        | -2  |     |
|     |     |          |                  |                | 1 4 0         |           | 1 4 0 | -8-6 -6       |     | 1 4 0 -8 -6   |        |     |     |
|     |     |          | C o              | n c .          |               |           |       | -8            |     |               | -6     |     |     |
|     |     | la       | T h              | i c k n ess )m | 1 2 0         |           | 1 2 0 | - 4           |     | 1 2 0         | -4     |     |     |
|     |     | itin 1.5 | V o              | l u m e        | 1 0 0         |           | 1 0 0 |               |     | 1 0 0         | -8     | -4  |     |
|     |     | I fo     |                  | ( e            | -2            |           |       |               |     |               | -6     |     |     |
|     |     |  e       |                  | ziS            | 8 0 --4-68    |           | 8 0   | -8-- 46       |     | 8 0 - 6       | -4 -8  |     |     |
|     |     | lp       |                  |  e             |               |           |       |               |     |               |        |     |     |
|     |     | itlu     | 1                | o              | 6 0           |           | 6 0   |               |     | 6 0           | 8      |     |     |
|     |     |          |                  | lF             | 4 0           |           | 4 0   | --- 864       |     | 4 0           | -- 64  | -6  |     |
|     |     | M        |                  |                |               |           |       |               |     |               | -      |     |     |
|     |     | 0.5      |                  |                | 20            | -2 -4-6-8 | 20    | -2            |     | 20            |        |     |     |
|     |     |          | 0 10             | 20 30          | 1             | 2         |       | 1             | 2   |               | 1 2    | -8  |     |
|     |     |          | Time (days)      |                | Thickness (m) |           |       | Thickness (m) |     | Thickness (m) |        |     |     |
|     |     | (c)      | Shear Only       | (d)            |               | Day 0     |       | Day 15        |     |               | Day 30 |     |     |
|     |     |          | 2                |                |               |           |       |               |     |               |        | -10 |     |
|     |     |          |                  |                | 1 4 0         |           | 1 4 0 | -8-6          |     | 1 4 0 -8-6    | -6     |     |     |
|     |     |          | C o              | n c .          |               |           |       | -6-8          |     |               | -8     |     |     |
|     |     | la       | T h              | i c k n ess )m | 1 2 0         |           | 1 2 0 | - 4           |     | 1 2 0 4       |        |     |     |
|     |     | itin 1.5 | V o              | l u m e        | 1 0 0         |           | 1 0 0 |               |     | 1 0 0 -       |        | -12 |     |
|     |     | I fo     |                  | ( e            | -2            |           |       | - 2           |     |               |        |     |     |
|     |     |          |                  | ziS            | 8 0 --4-68    |           | 8 0   | - 8 --6 4     |     | 8 0 -8-- 46   |        |     |     |
 e lp
|     |     | itlu | 1    |  e o  | 6 0 |           | 6 0 |       |     | 6 0 |        |     |     |
| --- | --- | ---- | ---- | ----- | --- | --------- | --- | ----- | --- | --- | ------ | --- | --- |
|     |     |      |      | lF    | 4 0 |           | 4 0 | - --8 |     | 4 0 | -- 864 | -14 |     |
|     |     | M    |      |       |     |           |     |       | 46  |     | -      |     |     |
|     |     | 0.   | 5    |       | 2 0 | -2 -4-6-8 | 2 0 | -2    |     | 2 0 | - 2    |     |     |
|     |     |      | 0 10 | 20 30 | 1   | 2         |     | 1     | 2   |     | 1 2    |     |     |
Figure4.Resultsoftwosimulationsofthefloesizeandthicknessdistributionforcedwithfixedice-flowstrainratesandonlymechanicalin-
teractions.(a)Iceconcentration,meanthickness,andicevolumefor1monthoffixedshear,withnoconvergence.Timeseriesarenormalized
bytheirinitialvalues.(b)Thebase10logarithmoftheFSTDatdays0,15,and30fortherunwithonlyshear.Thecolorbarcorrespondsto
thebase10logarithmoftheFSTD,contourintervalsarepowersof10.(c,d)Sameas(a,b)for1weekoffixedconvergencewithnoshear.
|     |     |     |     | =0,(cid:15) | =10−7)s−1. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
simulatesshearoffixedmagnitude((cid:15) I II In both scenarios the norm of the strain rate tensor is the
same,||E||=10−7s−1.Inthecaseofonlyshear(Fig.4c,d),
Whenthereisnoconvergence,therateofopenwaterforma-
tionduetocollisions(Eq.13)is0.5×10−7s−1,equaltothe iceconcentrationisdiminishedbyafactorofroughly18%,
magnitudeofthestrainratetensordividedby2: correspondingtoa22%increaseinmeanicethickness,and
withnochangeinicevolume.Incontrast,inthecaseofcon-
| D c(cid:12) (cid:12) | 1   |     | 1   |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M
(cid:12) = ((cid:15) I −||E||)=− ||E||. vergenceonly(Fig.4a,b),iceconcentrationisdiminishedby
| Dt (cid:12) | 2   |     | 2   |     |     |     |     |                                                  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
| shear       |     |     |     |     |     |     |     | 36%,withacorresponding56%increaseinmeanicethick- |     |     |     |     |     |
ness,againwithnochangeinicevolume.Thusshearmotions
Whenthereisnoshear,andonlyconvergence,theamountof
openwaterformationduetocollisionsis10−7s−1,equalto leadtocollisionsandthecombinationsoffloeswithonean-
|     |     |     |     |     |     |     |     | other, but | at a | reduced | rate when | compared | to convergence |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------- | --------- | -------- | -------------- |
themagnitudeofthestrainratetensor:
oficeflow,forthesamestrainratetensornorm.Inthecase
| D c(cid:12) (cid:12) | 1           |             | 1          |               |               |     |     |                                                   |     |     |     |     |     |
| -------------------- | ----------- | ----------- | ---------- | ------------- | ------------- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
| M                    |             |             |            |               |               |     |     | ofshearonly,thetwoinitialpeaksintheFSTDaresmeared |     |     |     |     |     |
| (cid:12)             | = ((cid:15) | I −||E||)=− | (|(cid:15) | I |+|(cid:15) | I |))=−||E||. |     |     |                                                   |     |     |     |     |     |
| Dt (cid:12)          | 2           |             | 2          |               |               |     |     |                                                   |     |     |     |     |     |
conv
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2131
#10-3 surface area rises as floes are broken and their lateral sides
| 7.5      |     |                   |       | 2      |     |                        |     |                                                   |     |     |     |     |     |     |     |
| -------- | --- | ----------------- | ----- | ------ | --- | ---------------------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          |     |                   |       |        |     | Mean Floe Surface Area |     | areexposed,increasingby63%overtheweek(Fig.5b,blue |     |     |     |     |     |     |     |
|          |     | Initial FSD       |       |        |     | Mean Floe Size         |     |                                                   |     |     |     |     |     |     |     |
| )%       |     | D a y   1         |       |        |     |                        |     | line).                                            |     |     |     |     |     |     |     |
|          |     | D a y   3         |       | 1.5    |     |                        |     |                                                   |     |     |     |     |     |     |     |
| ( a 5    |     | D a y   5         | 4 )m  |        |     |                        |     |                                                   |     |     |     |     |     |     |     |
| e        |     | D a y   7         | ( m   | la     |     |                        |     |                                                   |     |     |     |     |     |     |     |
| rA       |     |                   |       | itin   |     |                        |     |                                                   |     |     |     |     |     |     |     |
|  la      |     | W a v e  Spectrum | u     | I fo 1 |     |                        |     |                                                   |     |     |     |     |     |     |     |
| n        |     |                   | rtc   |        |     |                        |     |                                                   |     |     |     |     |     |     |     |
| o        |     |                   | e     |  %     |     |                        |     | 4 Conclusions                                     |     |     |     |     |     |     |     |
| itc 2. 5 |     |                   | 2 p S |        |     |                        |     |                                                   |     |     |     |     |     |     |     |
| a        |     |                   |       | 0. 5   |     |                        |     |                                                   |     |     |     |     |     |     |     |
rF
|     |     |     |     |     |     |     |     | We developed | a   | model | that | simulates | the | evolution | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ---- | --------- | --- | --------- | ------ |
| 0   |     |     | 0   | 0   |     |     |     |              |     |       |      |           |     |           |        |
0 50 100 150 0 2 4 6 FSTD, using large-scale oceanic and atmospheric forcing
| Floe size/wavelength (m) |         |                |     |        |      | Time (days) |            |            |              |      |     |        |                 |         |         |
| ------------------------ | ------- | -------------- | --- | ------ | ---- | ----------- | ---------- | ---------- | ------------ | ---- | --- | ------ | --------------- | ------- | ------- |
|                          |         |                |     |        |      |             |            | fields as  | input, which | may  | be  | useful | as an extension |         | to sea- |
|                          |         |                |     |        |      |             |            | ice models | presently    | used | in  | global | climate         | models, | in par- |
| Figure 5.                | Results | of simulations |     | of the | FSTD | forced      | with swell |            |              |      |     |        |                 |         |         |
fracture only. (a) The FSD before (black line, left axis) and af- ticular in regions with a continuously varying FSTD, such
ter (gray lines, left axis) several days of swell fracture using a asthemarginalicezone.Weincludedrepresentationsofthe
| Bretschneider | (Michel, | 1968, | p.  | 23) wave | spectrum | (orange | line, |     |     |     |     |     |     |     |     |
| ------------- | -------- | ----- | --- | -------- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
impactofthermodynamics(meltingandfreezing),mechani-
rightaxis).Asswellfracturedoesnotaffectfloethickness,thedis- cal interactionsof rafting andridging due tofloe collisions,
tributionisplottedasafunctionoffloesizeonly.(b)Themeanfloe and of floe fracture by ocean surface waves, all processes
sizeandtotallateralicesurfaceareaasafractionoftheirinitialval-
|     |     |     |     |     |     |     |     | that are | active | in marginal | or  | seasonal | sea-ice | zones. | We  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --- | -------- | ------- | ------ | --- |
uesoverthecourseof1weekoficefracturewiththespecifiedwave
demonstratedtheeffectoftheseprocessesusingmodelruns
spectrum.
forcedbyexternalforcingfieldsincludingair–seaheatflux,
|     |     |     |     |     |     |     |     | ice flows    | leading | to mechanical |            | interactions, |         | and      | specified |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------------- | ---------- | ------------- | ------- | -------- | --------- |
|     |     |     |     |     |     |     |     | surface wave | field,  | and           | considered | the           | effects | of these | forc-     |
outoverarangeoffloesizesandthicknesses(Fig.4b),with
thevarietyoffloesizesandthicknessesincreasinginnumber ingfieldsindividuallyandwhencombined.Wedemonstrated
overtime.Sincethereistwiceasmuchopenwaterformation theeffectsofmechanicalinteractionsinthepresenceofboth
|             |                |     |       |     |           |     |           | shearing | and straining |     | ice flows, | separately |     | accounting | for |
| ----------- | -------------- | --- | ----- | --- | --------- | --- | --------- | -------- | ------------- | --- | ---------- | ---------- | --- | ---------- | --- |
| in the case | of convergence |     | only, | and | therefore | an  | increased |          |               |     |            |            |     |            |     |
number of mechanical interactions, the distribution of floe ridging and rafting. We studied the effect of surface waves,
firstforidealizedsingle-wavelengthwavefields,andthenac-
sizesandthicknessissmearedmorerapidly,andoveralarger
range(Fig.4c). countingforamorerealisticsurfacewavespectrum.Weex-
Figure5showstheresponseofthejointfloesizeandthick- aminedtheresponsetomeltingandfreezingbothalongex-
istingfloebasesandlateraledges,andinopenwater,leading
nessdistributiontoasingle-weekexperimentthatsimulates
a7-dayperiodoficefracturebysurfacewaves,usingawave topancakeiceformation.
Whilethepresentpaperfocusesonthedevelopmentofpa-
| spectrum | that leads | to  | ice breaking |     | into a | broader | range of |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ------------ | --- | ------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
floe sizes. The experiment uses the Bretschneider (Michel, rameterizationsneededtorepresenttheFSTDdynamicsand
1968, p. 24) surface wave spectrum as a function of period to test the model with individual forcing fields, we hope to
nextstudytheconsequencesofrealisticforcingfieldsonthe
T,S(T)dT:
|     |     |                    |          |           |     |     |     | FSTD and | compare | model | output | to  | the few | available | ob- |
| --- | --- | ------------------ | -------- | --------- | --- | --- | --- | -------- | ------- | ----- | ------ | --- | ------- | --------- | --- |
|     | 2   | (cid:18) (cid:19)3 | (cid:16) | (cid:17)4 |     |     |     |          |         |       |        |     |         |           |     |
1H T − 1 T servations. Another important future direction is the model
| S(T)dT | = s |     | e π | T z dT, |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4πT z T z development and testing that will allow for implementation
ofthismodelintosea-icemodelsusedinGCMs,allowingfor
| where H | =2m | is the | significant | wave | height | (the | mean |     |     |     |     |     |     |     |     |
| ------- | --- | ------ | ----------- | ---- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
s realistic ice thermodynamics, constitutive stress–strain rela-
| waveheightofthe1/3highestsurfacewaves),andT |     |     |     |     |     |     | =6s |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
z
tionship,wavemodel,andicemotionsdrivenbyoceancur-
| is the mean | time    | interval | between | zero-crossings |         | of   | the ob- |           |        |        |      |       |                   |     |      |
| ----------- | ------- | -------- | ------- | -------------- | ------- | ---- | ------- | --------- | ------ | ------ | ---- | ----- | ----------------- | --- | ---- |
|             |         |          |         |                |         |      |         | rents and | winds. | At the | same | time, | an implementation |     | into |
| served wave | record. | We       | use     | the surface    | gravity | wave | dis-    |           |        |        |      |       |                   |     |      |
λ=gT2/2π a GCM would require making the model more efficient by
| persion | relation |     |     | to write | S(T)dT | as  | a wave- |           |          |            |     |          |        |        |         |
| ------- | -------- | --- | --- | -------- | ------ | --- | ------- | --------- | -------- | ---------- | --- | -------- | ------ | ------ | ------- |
|         |          |     |     |          |        |     |         | replacing | the high | resolution |     | we could | afford | to use | here in |
lengthspectrumS(λ)dλ.Thewavelengthbinsarespacedto
floesizeandthicknessbyasimplifiedapproach,possiblyas-
| correspond       | uniquely  | to      | floe size | bins,      | and | there is    | a one-to- |             |            |          |      |                |     |            |        |
| ---------------- | --------- | ------- | --------- | ---------- | --- | ----------- | --------- | ----------- | ---------- | -------- | ---- | -------------- | --- | ---------- | ------ |
|                  |           |         |           |            |     |             |           | suming a    | functional | form     | of   | the FSTD       | and | simulating | only   |
| one relationship |           | between | a wave’s  | wavelength |     | and         | the floe  |             |            |          |      |                |     |            |        |
|                  |           |         |           |            |     |             |           | its moments | as         | is often | done | in atmospheric |     | models     | of the |
| size of          | new floes | formed  | through   | fracture   |     | of existing | floes     |             |            |          |      |                |     |            |        |
particlesizedistribution.
| by that         | wave. The   | peak          | wavelength     |              | of the | wave          | spectrum |                 |            |        |           |                |                 |              |          |
| --------------- | ----------- | ------------- | -------------- | ------------ | ------ | ------------- | -------- | --------------- | ---------- | ------ | --------- | -------------- | --------------- | ------------ | -------- |
|                 |             |               |                |              |        |               |          | The study       | of         | FSTD   | dynamics, | and            | the development |              | of a     |
| is at T ≈6.75s, |             | corresponding |                | to λ≈70m.    |        | As before,    | the      |                 |            |        |           |                |                 |              |          |
|                 |             |               |                |              |        |               |          | prognostic      | FSTD       | model, | are       | made difficult |                 | by the       | scarcity |
| domain          | width D     | is set        | to 10km.       | Large        |        | floes (size   | I) are   |                 |            |        |           |                |                 |              |          |
|                 |             |               |                |              |        |               |          | of observations |            | of the | floe size | distribution   |                 | and its      | seasonal |
| rapidly         | fractured,  | with          | the fractional |              | area   | corresponding | to       |                 |            |        |           |                |                 |              |          |
|                 |             |               |                |              |        |               |          | and long-term   | evolution. |        | Such      | observations   |                 | are required | to       |
| these floes     | decreasing, |               | and the        | distribution |        | shifts        | towards  |                 |            |        |           |                |                 |              |          |
constrainuncertainparametersusedinthemodeldeveloped
| smaller | sizes (Fig. | 5a, | gray lines). | After | 1   | week, | the frac- |           |         |           |     |              |     |           |       |
| ------- | ----------- | --- | ------------ | ----- | --- | ----- | --------- | --------- | ------- | --------- | --- | ------------ | --- | --------- | ----- |
|         |             |     |              |       |     |       |           | here, and | to help | determine |     | the dominant |     | processes | which |
tionalareabelongingtofloesintherangefrom75to125m
|     |     |     |     |     |     |     |     | need to | be included | in  | FSTD | models | to be | incorporated | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ---- | ------ | ----- | ------------ | --- |
decreasesfrom37to0%,withmeanfloesizedecreasingby
globalclimatemodels.
67%(Fig.5b,blueline).Asaconsequence,thetotallateral
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2132 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
AppendixA: ComparisonofrateconstantsinEq.(14)
tothoseinThorndikeetal.(1975)
Thorndike et al. (1975) employed the following parameter-
ization of the function ψ (Eq. 1), which represents the rate
ofchangeofareabelongingtoiceofthicknesshduetome-
chanicalinteractions:
(cid:16) (cid:17)1/2
ψ = (cid:15)2+(cid:15)2 (α δ(h)+α w (h)), (A1)
I II 0 r r
∞
where R w (h)=−1,andthecoefficientsα andα are
r 0 c
0
1
α = (1+cos(θ)), (A2)
0
2
1
α = (1−cos(θ)), (A3)
c
2
whereθ =arctan((cid:15) /(cid:15) ).Usingthetrigonometricidentity,
II I
(cid:15)
cos(arctan((cid:15) /(cid:15) ))= I ,
II I ||E||
q
with||E||≡ (cid:15)2+(cid:15)2,ψ mayberewrittenas
I II
1 (cid:18) ||E||+(cid:15) ||E||−(cid:15) (cid:19)
ψ = ||E|| δ(h) I + I w , (A4)
2 ||E|| ||E|| r
1
= (δ(h)(||E||+(cid:15) )+w (||E||−(cid:15) )), (A5)
I r I
2
1
=δ(h)(cid:15) + (||E||−(cid:15) )(δ(h)+w ). (A6)
I I r
2
Identifying w =−R L (r)dh and 1(||E||−(cid:15) )= DMc re-
r c 2 I Dt
h
coversthefloe-size-integratedformofEq.(14).
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/

C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution 2133
TheSupplementrelatedtothisarticleisavailableonline Collins,C.O.,Rogers,W.E.,Marchenko,A.,andBabanin,A.V.:
atdoi:10.5194/tc-9-2119-2015-supplement. In situ measurements of an energetic wave event in the Arc-
|     |     |     |     |     |     |     |     | tic marginal |     | ice zone, | Geophys. Res. | Lett., | 42, 1863–1870, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ------------- | ------ | -------------- | --- |
doi:10.1002/2015GL063063,2015.
Dumont,D.,Kohout,A.,andBertino,L.:Awave-basedmodelfor
themarginalicezoneincludingafloebreakingparameterization,
|                   |     |          |      |          |     |              |     | J. Geophys. |     | Res., 116, | C04001, doi:10.1029/2010JC006682, |     |     |     |
| ----------------- | --- | -------- | ---- | -------- | --- | ------------ | --- | ----------- | --- | ---------- | --------------------------------- | --- | --- | --- |
| Acknowledgements. |     | We thank | Luke | Bennetts | and | an anonymous |     |             |     |            |                                   |     |     |     |
2011.
| reviewer    | for their | most detailed, |          | constructive, |           | knowledgeable, |      |          |        |          |                      |     |            |           |
| ----------- | --------- | -------------- | -------- | ------------- | --------- | -------------- | ---- | -------- | ------ | -------- | -------------------- | --- | ---------- | --------- |
|             |           |                |          |               |           |                |      | Feltham, | D. L.: | Granular | flow in the marginal |     | ice zone., | Phil. T., |
| and helpful | comments. | This           | research | was           | supported | by             | NASA |          |        |          |                      |     |            |           |
363,1677–1700,doi:10.1098/rsta.2005.1601,2005.
| under grant | NNX14AH39G. |     | C.  | Horvat | was supported |     | by the |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | ------ | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Feltham,D.L.:SeaIceRheology,Ann.Rev.FluidMech.,40,91–
| Department | of Defense | (DoD) | through |     | the National |     | Defense |     |     |     |     |     |     |     |
| ---------- | ---------- | ----- | ------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
112,doi:10.1146/annurev.fluid.40.111406.102151,2008.
| Science & | Engineering | Graduate |     | Fellowship | (NDSEG) | Program. |     |     |     |     |     |     |     |     |
| --------- | ----------- | -------- | --- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Godlovitch,D.,Illner,R.,andMonahan,A.:Smoluchowskicoagu-
| E. Tziperman | thanks | the | Weizmann | Institute | for | its hospitality |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | -------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
lationmodelsofseaicethicknessdistributiondynamics,J.Geo-
duringpartsofthiswork.
phys.Res.,116,C12005,doi:10.1029/2011JC007125,2011.
|     |     |     |     |     |     |     |     | Harvey, | L. D. | D.: Testing | alternative | parameterizations |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | ----------- | ----------------- | --- | --- |
Editedby:D.Feltham
|     |     |     |     |     |     |     |     | lateral   | melting | and            | upward basal | heat | flux in | a ther-   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------------- | ------------ | ---- | ------- | --------- |
|     |     |     |     |     |     |     |     | modynamic |         | sea ice model, | J. Geophys.  |      | Res.,   | 95, 7359, |
doi:10.1029/JC095iC05p07359,1990.
Henderson,G.R.,Barrett,B.S.,andLafleur,D.:Arcticseaiceand
References
theMadden-JulianOscillation(MJO),Clim.Dynam.,43,2185–
2196,doi:10.1007/s00382-013-2043-y,2014.
Asplin, M. G., Galley, R., Barber, D. G., and Prinsenberg, Herman, A.: Sea-ice floe-size distribution in the context of spon-
S.: Fracture of summer perennial sea ice by ocean swell taneousscalingemergenceinstochasticsystems,Phys.Rev.E.,
as a result of Arctic storms, J. Geophys. Res., 117, 1–12, 81,066123,doi:10.1103/PhysRevE.81.066123,2010.
doi:10.1029/2011JC007221,2012.
|     |     |     |     |     |     |     |     | Herman, | A.: Molecular-dynamics |     | simulation |     | of clustering | pro- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------- | --- | ---------- | --- | ------------- | ---- |
Asplin, M. G., Scharien, R., Else, B., Howell, S., Barber, D. G., cessesinsea-icefloes,Phys.Rev.E,1–25,2011.
Papakyriakou, T., and Prinsenberg, S.: Implications of frac- Herman, A.: Numerical modeling of force and contact net-
turedArcticperennialicecoveronthermodynamicanddynamic works in fragmented sea ice, Ann. Glaciol., 54, 114–120,
sea ice processes, J. Geophys. Res. Oceans, 119, 2327–2343, doi:10.3189/2013AoG62A055,2013.
doi:10.1002/2013JC009557,2014.
|     |     |     |     |     |     |     |     | Hibler, W. | D.: | A Dynamic | Thermodynamic |     | Sea Ice | Model, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------------- | --- | ------- | ------ |
Bennetts, L. G. and Squire, V. A.: Model sensitivity analysis J. Phys. Oceanogr., 9, 815–846, doi:10.1175/1520-
of scattering-induced attenuation of ice-coupled waves, Ocean 0485(1979)009<0815:ADTSIM>2.0.CO;2,1979.
Model.,45–46,1–13,doi:10.1016/j.ocemod.2012.01.002,2012. Hibler III, W. D.: Modeling a variable thickness ice cover, Mon.
Bennetts, L. G. and Williams, T. D.: Water wave transmission WeatherRev.,108,1943–1973,1980.
| by an | array of | floating | disks, | Proc. Roy. | Soc. | A, 471, | 1–18, |     |     |     |     |     |     |     |
| ----- | -------- | -------- | ------ | ---------- | ---- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Holt,B.andMartin,S.:Theeffectofastormonthe1992summer
doi:10.1098/rspa.2014.0698,2015. seaicecoveroftheBeaufort,Chukchi,andEastSiberianSeas,
Birnbaum, G. and Lüpkes, C.: A new parameterization of sur- J.Geophys.Res.,106,1017,doi:10.1029/1999JC000110,2001.
face drag in the marginal sea ice zone, Tellus A, 54, 107–123, Hopkins, M. A., Tuhkuri, J., and Lensu, M.: Rafting and
doi:10.1034/j.1600-0870.2002.00243.x,2002. ridging of thin ice sheets, J. Geophys. Res., 104, 13605,
Bitz,C.M.:Numericalmodelingofseaiceintheclimatesystem, doi:10.1029/1999JC900031,1999.
Tech.rep.,UniversityofWashington,www.atmos.uw.edu/~bitz/
Horvat,C.andTziperman,E.:EffectsoftheSeaIceFloeSizeDis-
Bitz_chapter.pdf(lastaccess:11October2015),2008. tribution on Polar Ocean Properties and Air-Sea Exchange, in:
Bitz,C.M.,Holland,M.M.,Weaver,A.J.,andEby,M.:Simulat- AbstractC11A-0341presentedat2014FallMeeting,AGU,San
ingtheice-thicknessdistributioninacoupledclimatemodel,J. Francisco,CA,15–19December,2014.
Geophys.Res.,106,2441,doi:10.1029/1999JC000113,2001. Hunke,E.C.,Lipscomb,W.H.,Turner,A.K.,Jeffery,N.,andEl-
| Bourke, | R. H. and | Garrett, | R. P.: | Sea ice | thickness | distribution |     |     |     |     |     |     |     |     |
| ------- | --------- | -------- | ------ | ------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
liot,S.:CICE:TheLosAlamosSeaIceModelDocumentation
in the Arctic Ocean, Cold Reg. Sci. Technol., 13, 259–280, andSoftwareUsersManualVersion5.0,Tech.rep.,LosAlamos
doi:10.1016/0165-232X(87)90007-3,1987. Natl.Laboratory,LosAlamos,NM,2013.
Bouws, E., Draper, L., Shearman, E., Laing, A., Feit, D., Mass, Johannessen,J.A.,Johannessen,O.M.,Svendsen,E.,Shuchman,
W., Eide, L., Francis, P., Carter, D., and Battjes, J.: Guide to R., Manley, T., Campbell, W. J., Josberger, E. G., Sandven, S.,
Waveanalysisandforecasting,WorldMeteorologicalOrganiza-
|     |     |     |     |     |     |     |     | Gascard, | J. C., | Olaussen, | T., Davidson, | K., | and Van | Leer, J.: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | ------------- | --- | ------- | --------- |
tion,1998,11–12,1998. Mesoscale eddies in the Fram Strait marginal ice zone during
Cavalieri,D.J.andParkinson,C.L.:Arcticseaicevariabilityand the1983and1984MarginalIceZoneExperiments,J.Geophys.
trends,1979–2010,TheCryosphere,6,881–889,doi:10.5194/tc- Res.,92,6754,doi:10.1029/JC092iC07p06754,1987.
6-881-2012,2012. Kohout,A.L.,Williams,M.,Toyota,T.,Lieser,J.,andHutchings,
| Chevallier, | M. and | Salas-Mélia, | D.: | The role | of sea | ice thickness |     |             |              |     |                 |     |              |      |
| ----------- | ------ | ------------ | --- | -------- | ------ | ------------- | --- | ----------- | ------------ | --- | --------------- | --- | ------------ | ---- |
|             |        |              |     |          |        |               |     | J.: In situ | observations |     | of wave-induced | sea | ice breakup, | Deep |
distributioninthearcticseaicepotentialpredictability:Adiag- SeaRes.,1–6,doi:10.1016/j.dsr2.2015.06.010,2015.
nosticapproachwithacoupledGCM,J.Clim.,25,3025–3038,
doi:10.1175/JCLI-D-11-00209.1,2012.
www.the-cryosphere.net/9/2119/2015/ TheCryosphere,9,2119–2134,2015

2134 C.HorvatandE.Tziperman:Aprognosticmodelofthesea-icefloesizeandthicknessdistribution
Kohout,A.L.andMeylan,M.H.:Anelasticplatemodelforwave Stroeve,J.C.,Serreze,M.C.,Holland,M.M.,Kay,J.E.,Malanik,
attenuationandicefloebreakinginthemarginalicezone,J.Geo- J., and Barrett, A. P.: The Arctic’s rapidly shrinking sea ice
phys.Res.,113,C09016,doi:10.1029/2007JC004434,2008. cover: A research synthesis, Clim. Change, 110, 1005–1027,
Lu, P., Li, Z. J., Zhang, Z. H., and Dong, X. L.: Aerial doi:10.1007/s10584-011-0101-1,2012.
observations of floe size distribution in the marginal ice Strong,C.andRigor,I.G.:Arcticmarginalicezonetrendingwider
zone of summer Prydz Bay, J. Geophys. Res., 113, C02011, in summer and narrower in winter, Geophys. Res. Lett., 40,
doi:10.1029/2006JC003965,2008. 4864–4868,doi:10.1002/grl.50928,2013.
McPhee, M. G.: Turbulent heat flux in the upper ocean under sea Strong,C.,Magnusdottir,G.,andStern,H.:Observedfeedbackbe-
ice,J.Geophys.Res.,97,5365,doi:10.1029/92JC00239,1992. tweenwinterseaiceandtheNorthAtlanticOscillation,J.Clim.,
Meylan, M. H., Bennetts, L. G., and A. L. Kohout: In 22,6021–6032,doi:10.1175/2009JCLI3100.1,2009.
situ measurements and analysis of ocean waves in the Thorndike,A.S.,Rothrock,D.A.,Maykut,G.A.,andColony,R.:
Antarctic marginal ice zone, Geophys. Res. Lett., 41, 1–6, Thethicknessdistributionofseaice,J.Geophys.Res.,80,4501,
doi:10.1002/2014GL060809.In,2014. doi:10.1029/JC080i033p04501,1975.
Michel, W.: Sea Spectra Simplified, Marine Technol., 5, 17–30, Toyota,T.andEnomoto,H.:AnalysisofseaicefloesintheSeaof
1968. Okhotsk using ADEOS/AVNIR images, in: Proceedings of the
Niebauer, H.: Wind and melt driven circulation in a marginal sea 16thIAHRInternationalSymposiumonIce,211–217,Interna-
iceedgefrontalsystem:anumericalmodel,Cont.ShelfRes.,1, tionalAssociationofHydraulicEngineeringandResearch,2002.
49–98,doi:10.1016/0278-4343(82)90032-2,1982. Toyota,T.,Takatsuji,S.,andNakayama,M.:Characteristicsofsea
Parkinson, C. L. and Washington, W. M.: A large-scale nu- icefloesizedistributionintheseasonalicezone,Geophys.Res.
merical model of sea ice, J. Geophys. Res., 84, 311–337, Lett.,33,L02616,doi:10.1029/2005GL024556,2006.
doi:10.1029/JC084iC01p00311,1979. Toyota, T., Haas, C., and Tamura, T.: Size distribution and shape
Parmerter,R.R.:Amodelofsimpleraftinginseaice,J.Geophys. properties of relatively small sea-ice floes in the Antarctic
Res.,80,1948,doi:10.1029/JC080i015p01948,1975. marginal ice zone in late winter, Deep-Sea Res. II, 58, 1182–
Parmerter, R. R. and Coon, M. D.: Model of pressure 1193,doi:10.1016/j.dsr2.2010.10.034,2011.
ridge formation in sea ice, J. Geophys. Res., 77, 6565, Vavrus,S.J.,Holland,M.M.,Jahn,A.,Bailey,D.A.,andBlazey,
doi:10.1029/JC077i033p06565,1972. B.A.:Twenty-first-centuryarcticclimatechangeinCCSM4,J.
Perovich,D.K.andJones,K.F.:Theseasonalevolutionofseaice Clim.,25,2696–2710,doi:10.1175/JCLI-D-11-00220.1,2012.
floesizedistribution,J.Geophys.Res.-Ocean.,119,8767–8777, Washington, W. M., Semtner, A. J., Parkinson, C., and Mor-
doi:10.1002/2014JC010136,2014. rison, L.: On the Development of a Seasonal Change Sea-
Renner, A. and Gerland, S.: Evidence of Arctic sea ice thinning Ice Model, J. Phys. Oceanogr., 6, 679–685, doi:10.1175/1520-
fromdirectobservations,Geophys.Res.Lett.,2012,5029–5036, 0485(1976)006<0679:OTDOAS>2.0.CO;2,1976.
doi:10.1002/2014GL060369.1.,2014. Williams, T. D., Bennetts, L. G., Squire, V. a., Dumont, D., and
Rothrock, D. A. and Thorndike, A. S.: Measuring the sea Bertino, L.: Wave–ice interactions in the marginal ice zone.
ice floe size distribution, J. Geophys. Res., 89, 6477–6486, Part 1: Theoretical foundations, Ocean Model., 71, 81–91,
doi:10.1029/JC089iC04p06477,1984. doi:10.1016/j.ocemod.2013.05.010,2013a.
Semtner, A. J.: A Model for the Thermodynamic Growth Williams, T. D., Bennetts, L. G., Squire, V. A., Dumont, D., and
of Sea Ice in Numerical Investigations of Climate, Bertino, L.: Wave-ice interactions in the marginal ice zone.
J. Phys. Oceanogr., 6, 379–389, doi:10.1175/1520- Part 2: Numerical implementation and sensitivity studies along
0485(1976)006<0379:AMFTTG>2.0.CO;2,1976. 1D transects of the ocean surface, Ocean Model., 71, 92–101,
Shen, H., Hibler, W., and Leppäranta, M.: On applying granular doi:10.1016/j.ocemod.2013.05.011,2013b.
flow theory to a deforming broken ice field, Acta Mech., 143– Wu, Q. and Zhang, X.: Observed evidence of an impact of the
160,doi:10.1007/BF01182545,1986. AntarcticseaicedipoleontheAntarcticoscillation,J.Clim.,24,
Shen, H. H. and Sankaran, B.: Internal Length And Time Scales 4508–4518,doi:10.1175/2011JCLI3965.1,2011.
In A Simple Shear Granular Flow, Phys. Rev. E, 70, 51308, Yu,Y.andRothrock,D.A.:Thinicethicknessfromsatellitethermal
doi:10.1103/PhysRevE.70.051308,2004. imagery,J.Geophys.Res.,101,25753,doi:10.1029/96JC02242,
Shen, H. H., Hibler, W. D., and Leppäranta, M.: The role of 1996.
floe collisions in sea ice rheology, J. Geophys. Res., 92, 7085, Zhang,J.,Lindsay,R.,Schweiger,A.,andSteele,M.:Theimpactof
doi:10.1029/JC092iC07p07085,1987. anintensesummercycloneon2012Arcticseaiceretreat,Geo-
Steele,M.:Seaicemeltingandfloegeometryinasimpleice-ocean phys.Res.Lett.,40,720–726,doi:10.1002/grl.50190,2013.
model, J. Geophys. Res., 97, 17729, doi:10.1029/92JC01755, Zhang, J., Schweiger, A., Steele, M., and Stern, H.: Sea ice floe
1992. size distribution in the marginal ice zone: Theory and numer-
Steer, A., Worby, A., and Heil, P.: Observed changes in ical experiments, J. Geophys. Res.-Ocean., 120, 3484—-3498,
sea-ice floe size distribution during early summer in the doi:10.1002/2015JC010770,2015.
western Weddell Sea, Deep-Sea Res. II, 55, 933–942,
doi:10.1016/j.dsr2.2007.12.016,2008.
TheCryosphere,9,2119–2134,2015 www.the-cryosphere.net/9/2119/2015/
