TheCryosphere,13,2869–2885,2019
https://doi.org/10.5194/tc-13-2869-2019
©Author(s)2019.Thisworkisdistributedunder
theCreativeCommonsAttribution4.0License.
Estimating the sea ice floe size distribution using satellite altimetry:
| theory, | climatology, |     | and | model | comparison |     |     |     |
| ------- | ------------ | --- | --- | ----- | ---------- | --- | --- | --- |
ChristopherHorvat1,LettieA.Roach2,3,RachelTilling4,5,CeciliaM.Bitz2,BaylorFox-Kemper1,ColinGuider6,
KaitlinHill7,AndyRidout8,andAndrewShepherd9
1InstituteatBrownforEnvironmentandSociety,BrownUniversity,Providence,RI,USA
2DepartmentofAtmosphericSciences,UniversityofWashington,Seattle,WA,USA
3NationalInstituteofWaterandAtmosphericResearch,Wellington,NewZealand
4CryosphericSciencesLaboratory,NASAGoddardSpaceFlightCenter,Greenbelt,MD,USA
5EarthSystemScienceInterdisciplinaryCenter,UniversityofMaryland,CollegePark,MD,USA
6DepartmentofMathematics,UniversityofNorthCarolina,ChapelHill,NC,USA
7SchoolofMathematics,UniversityofMinnesota,Minneapolis,MN,USA
8CentreforPolarObservationandModelling,UniversityCollegeLondon,London,UK
9CentreforPolarObservationandModelling,UniversityofLeeds,Leeds,UK
Correspondence:ChristopherHorvat(horvat@brown.edu)
Received:3June2019–Discussionstarted:17June2019
Revised:19September2019–Accepted:23September2019–Published:8November2019
Abstract.Insea-ice-coveredareas,theseaicefloesizedis- prognostic floe size and thickness distribution and coupled
tribution(FSD)playsanimportantroleinmanyprocessesaf- wavemodel,findinggoodagreementinregionswheremod-
fecting the coupled sea–ice–ocean–atmosphere system. Ob- eledoceansurfacewavescauseseaicefracture.
| servations                                          | of the           | FSD are sparse   | – traditionally | taken           | via a          |     |     |     |
| --------------------------------------------------- | ---------------- | ---------------- | --------------- | --------------- | -------------- | --- | --- | --- |
| painstaking                                         | analysis         | of ice surface   | photography     | –               | and the        |     |     |     |
| seasonal                                            | and inter-annual | evolution        | of floe         | size regionally |                |     |     |     |
| andgloballyislargelyunknown.Frequently,measuredFSDs |                  |                  |                 |                 | 1 Introduction |     |     |     |
| are assessed                                        | using            | a single number, | the scaling     | exponent        | of             |     |     |     |
the closest power-law fit to the observed floe size data, al- Earth’s polar oceans are covered with sea ice: a thin, het-
though in the absence of adequate datasets there have been erogeneousinterfacethatplaysanimportantroleinthecou-
limitedtestsofthis“power-lawhypothesis”.Herewederive plingbetweenoceanandatmosphere.Seaiceisacollection
and explain a mathematical technique for deriving statistics ofmanyindividualpieces,calledfloes,whichmaybechar-
|            |         |                     |             |            | acterized | in terms of a horizontal | length scale, | their “size”. |
| ---------- | ------- | ------------------- | ----------- | ---------- | --------- | ------------------------ | ------------- | ------------- |
| of the sea | ice FSD | from polar-orbiting | altimeters, | satellites |           |                          |               |               |
withsub-dailyreturntimestopolarregionswithhighalong- On the large scales relevant to global climate modeling, the
track resolutions. Applied to the CryoSat-2 radar altimetric statistical variability of floe size is described using the floe
record, covering the period from 2010 to 2018, and incor- sizedistribution(FSD;RothrockandThorndike,1984).
porating11millionindividualfloesamples,weproducethe The FSD is an important property of the sea ice cover
thatinfluencesthemultiscaletemporalandgeographicvari-
firstpan-Arcticclimatologyandseasonalcycleofseaicefloe
sizestatistics.Wethenperformthefirstpan-Arctictestofthe ability of sea ice, akin to the grain size in sedimentology
power-lawhypothesis,findinglimitedsupportintherangeof or particle size distribution in atmospheric chemistry. The
floe sizes typically analyzed in photographic observational scaleofindividualfloesplaysaroleinmanysea-ice-related
studies.Wecomparetheseasonalvariabilityinobservedfloe processes: sea ice melt rate (Steele, 1992; Horvat et al.,
|               |         |               |             |           | 2016; Horvat | and Tziperman,                             | 2018), the | evolution of the |
| ------------- | ------- | ------------- | ----------- | --------- | ------------ | ------------------------------------------ | ---------- | ---------------- |
| size to fully | coupled | climate model | simulations | including | a            |                                            |            |                  |
|               |         |               |             |           | oceanic      | mixed layer (ManucharyanandThompson,2017), |            |                  |
PublishedbyCopernicusPublicationsonbehalfoftheEuropeanGeosciencesUnion.

2870 C.Horvatetal.:Floesfromaltimetry
atmospheric boundary layer exchange (Birnbaum and Lüp- toclimatechangestudies(Laxonetal.,2003;Kwok,2018),
kes, 2002; Lüpkes and Birnbaum, 2005; Tsamados et al., andhavebeenevaluatedandvalidatedusingfieldcampaign
2014),theseaiceresponsetoappliedstress(Feltham,2008; data (Skourup et al., 2017; Sandberg Sorensen et al., 2018;
Wilchinsky and Feltham, 2011), and the propagation of Tillingetal.,2018).
waves into the ice (Squire et al., 1995; Squire, 2007; Smith One-dimensionalmeasurementsofseaiceproperties,like
andThomson,2016).TheimportanceoftheseaiceFSDhas along-trackaltimetricmeasurementsoficeopenwater,have
led to the development of diagnostic FSD models of vary- long been sought to describe the two-dimensional ice sur-
ing complexity (Williams et al., 2013; Zhang et al., 2015; face. Rothrock and Thorndike (1984) originally described a
Batesonetal.,2019)andaprognosticfloesizeandthickness method for reconstructing the sea ice floe size distribution
distribution (FSTD) scheme (Horvat and Tziperman, 2015; inaregionusingstraight-linemeasurementsoverthegeom-
Roachetal.,2018a). etry of floes. Lindsay and Rothrock (1995) later compiled
Despitethepotentialrelevanceofseaicefloesizetopolar thestatisticsofleadandicespacingsintwo-dimensionalim-
climateevolution,thereremainnoclimate-scaleassessments agery. Other work has taken place to derive and understand
of average floe size or the FSD. The observational record the width distribution of individual leads in visual imagery
of floe statistics derives from visual imagery localized in and altimetry (Wadhams et al., 1988; Key and Peckham,
spaceandtime(i.e.,RothrockandThorndike,1984;Toyota 1991;Key,1993;WerneckeandKaleschke,2015),whichcan
etal.,2006,2011;Steeretal.,2008)orfromrepeatmeasure- beusedtoestimateheatfluxesandturbulenttransferbetween
mentsinthesameregionovermultiplemonths(Hwangetal., the ocean and atmosphere. To date, however, these studies
2017;Sternetal.,2018a),whichmaysubsequentlybeused havenotbeendesignedtofacilitateacomparisonwithmodel
tocompileaseasonalcycleoftheFSD(PerovichandJones, data, nor have altimetric studies been used to compile floe
2014; Stern et al., 2018a). FSD measurements are obtained sizestatistics.Theseobjectivesarethefocusofthiswork.
byidentifyingindividualfloeswithinatwo-dimensionalim- We outline the mathematical theory that allows for com-
age of the sea ice surface. Because floe sizes span several parison of altimetric datasets and the FSD in Sect. 2. In
orders of magnitude, accurate representations of the FSD – Sect.3weapplythismethodtoanewdatasetofsegmented
eveninrelativelysmallgeographicaldomainsandinperfect CryoSat-2sea-ice-typedatafrom2010to2018.Usingthese
lightingandsurfaceconditions–requirehighresolutionand dataweproducethefirstclimatologicalmapsofmeanseaice
highobservationalcoverage.Nearlyallmeasurementsofthe floesizeandfragmentationfortheArcticOcean.Wethentest
FSDhavebeenmadeinaccordancewitha“power-law”scal- thepower-lawhypothesis,findinglimitedsupportforpower-
ing hypothesis commonly used to describe multiscale sys- lawscalingacrossmostofthedatasetinSect.4.Oneofthe
tems(MandelbrotandWheeler,1983),inwhichtheresulting keyaimsofthepaperistodevelopfloesizedistributionmea-
FSDisfittoastraightlineinlogarithmiccoordinates,whose surements that are useful for model validation and calibra-
slope, α, is reported as an intrinsic property of the floe mo- tion. In Sect. 5, we show a proof of concept, demonstrating
saic.Thereislargeuncertaintyinthesescalingcoefficients, howaltimetricdatacanbeusedtoconstrainandevaluatenew
the range they apply over, and their applicability and origin modelsoftheFSD,comparingtheCryoSat-2FSDdatatoa
(Herman,2011;HorvatandTziperman,2017;Hermanetal., climatemodelsimulationwithaprognosticFSTDmodel.We
2018; Stern et al., 2018b). Improvements in the quality and concludeinSect.6.
quantityofavailableFSDdataareneededbeforearrivingat
consensus-derived FSD statistics to guide and assess model
performance. 2 Floechordsandthefloesizedistribution
Here we outline a method that exploits satellite radar al-
timetry to construct the FSD and its moments across polar Foranindividualpassoverseaicebyapolar-orbitingsatel-
regionswithsub-kilometerspatialresolution,sub-dailytem- litealtimeter,returnwaveformsalongthesatelliteorbittrack
poralresolution,andspanningmultipleordersofmagnitude areassignedasurfacetypedependingonthewaveformshape
insize.Altimeters,liketheonescarriedontheEnvisat,ICE- and coincident sea ice concentration (Tilling et al., 2018).
Sat, CryoSat-2, and ICESat-2 satellites, make repeated, fre- A “floe chord” of length D is a continuous series of points
quent passes over polar oceans, and substantial efforts have identifiedasseaice,coveringageographicdistanceD(Till-
beenmadetoprocessthesatellitereturnstodiscriminatebe- ing et al., 2019a, b). Define a floe’s size, r, as its “effec-
tween open water, floes, and leads. The altimetric returns tive radius” – the square root of the floe’s area divided by
have found many uses, including reconstructing the sea ice π (Rothrock and Thorndike, 1984; Horvat and Tziperman,
thicknessfield(Laxonetal.,2013;Tillingetal.,2016,2018) 2015)Weuseradiusinsteadofdiameter,asappearsinsome
and ocean surface circulation under sea ice (Peacock and otherobservationalstudies,forcomparisonwithmodelout-
Laxon,2004;Armitageetal.,2018).Fieldsinferredfromal- put in Sect. 5. Because the satellite path is at an unknown
timetryhaveledtoadvancesinunderstandingpolarsystems: anglewithrespecttothe(alsounknown)floegeometry,any
from forecast and climate prediction (Day et al., 2014) to individual floe chord measurement is not a floe size mea-
modelvalidation (Schröderet al.,2018; Allardetal., 2018) surement. Converting between suitably processed altimetric
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

| C.Horvatetal.:Floesfromaltimetry |              |               |     |         |                 |            |           |     |     |     |     |     |     | 2871 |
| -------------------------------- | ------------ | ------------- | --- | ------- | --------------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | ---- |
| floe chord                       | measurements |               | and | floe    | size statistics | is         | therefore |     |     |     |     |     |     |      |
| the subject                      | of           | this section. |     | Details | on the          | processing | of the    |     |     |     |     |     |     |      |
CryoSat-2waveform,usedtoproduceadatasetoffloechords
| spanning | the period | 2010–2018, |     | are | outlined | in Sect. | 3 and |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --- | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Tillingetal.(2019b).
| For a                            | domain | of horizontal |             | area                  | A, and      | over a             | period of |           |          |        |       |              |                |         |
| -------------------------------- | ------ | ------------- | ----------- | --------------------- | ----------- | ------------------ | --------- | --------- | -------- | ------ | ----- | ------------ | -------------- | ------- |
| time (cid:49)T                   | that   | corresponds   | to          | several               | repeat      | satellite          | passes,   |           |          |        |       |              |                |         |
| we bin the                       | set    | of recorded   | floe        | chords                | to          | form a probability |           |           |          |        |       |              |                |         |
| distribution                     | S(D),  | which         | we          | term                  | the “floe   | chord              | distribu- |           |          |        |       |              |                |         |
| tion” (FCD),                     | where  |               | S(D)dD      | is equal              | to          | the number         | frac-     |           |          |        |       |              |                |         |
| tionoffloechordsinAover(cid:49)T |        |               |             | withlengthbetweenDand |             |                    |           |           |          |        |       |              |                |         |
| D+dD,                            | and is | normalized    |             | to 1.                 | To collapse | all                | measured  |           |          |        |       |              |                |         |
| chords onto                      | a      | single        | independent | scalar                | coordinate  |                    | (D), we   |           |          |        |       |              |                |         |
|                                  |        |               |             |                       |             |                    |           | Figure 1. | Relating | a floe | chord | to floe size | for a circular | floe. A |
followtheexampleofturbulencestatistics(Batchelor,1953)
satellitetrack(dashedblackline)passesoverafloeofradiusr(solid
| and assume | that | the | floe chord | distribution |     | data | are homo- |     |     |     |     |     |     |     |
| ---------- | ---- | --- | ---------- | ------------ | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
blackline).ThetrackrecordsaseriesofechoesoflengthD,which
geneous,isotropic,andstationarywithintheregionandtime isthelengthofachord(redline)identifiedbyitsinteriorangle,θ.
| data are    | collected. | In  | the same  | region, | we     | define | the (non- |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --------- | ------- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| cumulative) | number     |     | FSD P(r), | where   | P(r)dr | is     | the frac- |     |     |     |     |     |     |     |
r+dr
| tional number |         | of floes   | with | a size    | between | r and    | in      |     |     |     |     |     |     |     |
| ------------- | ------- | ---------- | ---- | --------- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| A, and        | is also | normalized |      | to 1. The | FSD     | inherits | the as- |     |     |     |     |     |     |     |
sumptions of homogeneity, isotropy, and stationarity from Fe(D;r) so long as the homogeneous, isotropic, stationary,
theFCD.OurobjectiveistorelatetheFCD,S(D),orquanti- andscale-invarianceassumptionsareretained,andtheevalu-
tiesderivedfromtheFCD,tothestatisticsoftheFSD,P(r). ationofpower-lawscalingisinfactindependentofFe(D;r).
Bayes’ theorem relates S(D) and P(r) through condi- To proceed and arrive at a concrete (although not gen-
tionalprobabilities, eral) realization of these functions,we will assume all floes
|                         |     |     |     |     |     |     |     | are perfect | circles. | In  | assessments | of  | the relationship | be- |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ----------- | --- | ---------------- | --- |
| F(r;D)S(D)=Fe(D;r)P(r). |     |     |     |     |     |     | (1) |             |          |     |             |     |                  |     |
tweenmajorandminoraxesofindividualfloes,the“round-
|                 |     |             |     |        |         |       |       | ness” parameter |     | for a      | floe is | typically | within  | 15% of 1   |
| --------------- | --- | ----------- | --- | ------ | ------- | ----- | ----- | --------------- | --- | ---------- | ------- | --------- | ------- | ---------- |
| The conditional |     | probability |     | F(r;D) | relates | given | chord |                 |     |            |         |           |         |            |
|                 |     |             |     |        |         |       |       | (Rothrock       | and | Thorndike, | 1984;   | Toyota    | et al., | 2011; Per- |
lengthstothefloesizedistributionthatcouldgeneratethem:
|          |                                             |     |     |     |     |     |     | ovich and | Jones, | 2014; | Gherardi | and Lagomarsino, |     | 2015; |
| -------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | -------- | ---------------- | --- | ----- |
| F(r;D)dr | istheprobabilitythatfloeswithsizeintherange |     |     |     |     |     |     |           |        |       |          |                  |     |       |
Alberelloetal.,2019),suggestingthatthiscircularassump-
r+dR
| from r to |     | were | sampled | given | a chord | of  | length D. |     |     |     |     |     |     |     |
| --------- | --- | ---- | ------- | ----- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tion,whilesimplistic,isbroadlyappropriate.Nevertheless,it
| The conditional                                    |     | probability |     | Fe(D;r) | relates | given | floe sizes |             |              |          |           |              |               |              |
| -------------------------------------------------- | --- | ----------- | --- | ------- | ------- | ----- | ---------- | ----------- | ------------ | -------- | --------- | ------------ | ------------- | ------------ |
|                                                    |     |             |     |         |         |       |            | will likely | be necessary |          | to amend  | the analysis |               | below in the |
| tothechordlengthdistributiontheygenerate:Fe(D;r)dD |     |             |     |         |         |       | is         |             |              |          |           |              |               |              |
|                                                    |     |             |     |         |         |       |            | future to   | account      | for more | realistic | shape        | distributions | and          |
theprobabilityofmeasuringafloechordoflengthfromDto
geometries(e.g.,diamonds;WilchinskyandFeltham,2006),
| D+dDgiventhatafloeofsizer |     |     |     | wasmeasured. |     |     |     |          |             |     |            |            |       |           |
| ------------------------- | --- | --- | --- | ------------ | --- | --- | --- | -------- | ----------- | --- | ---------- | ---------- | ----- | --------- |
|                           |     |     |     |              |     |     |     | regional | differences | in  | floe shape | properties | (such | as in re- |
Fe(D;r)
| This | second | probability |     | distribution |     | can | be de- |     |     |     |     |     |     |     |
| ---- | ------ | ----------- | --- | ------------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
gionswhereshearstressdeterminesfracturepatternsandfloe
rivedfromfirstprinciplesunderasingleassumption:thatthe
shapes;SchulsonandHibler,1991),ortoevaluatethesensi-
chordlengthdistributionthatwouldbesampledfromasetof
tivityoftheresultsthatfollowtotheassumedshapedistribu-
floesofsizerisindependentofr(equivalently,thefloeshape
tion.SolvingforFe(D;r)isageometricproblemthatrelates
distributionisscale-invariant).Formally,thisrequirementis
|     |     |     |     |     |     |     |     | the possible | measured |     | chord | lengths to | the underlying | floe |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ----- | ---------- | -------------- | ---- |
Fe(D;r)dD=G(ξ)dξ, (2) size,andwesolvethisexplicitlyforcircularfloeshere.Sim-
|     |     |     |     |     |     |     |     | ilar geometric | problems |     | have | been identified | and | solved in |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ---- | --------------- | --- | --------- |
whereG(ξ)=G(D)isanunknownfunctionthatintegrates otherfields(e.g.,Ponsetal.,2006;Nereetal.,2007),andwe
2r
to1overtheintervalfromξ =0to1.Underthisassumption, thereforeleaverefinementofFe(D;r)tofuturework.
the distribution of possible chord lengths measured from Considerthespecialcasethatallfloesareperfectcircles,
floes of size r has the same functional form independent illustratedinFig.1.Becausethereisnocorrelationbetween
of r. The probability distribution F(D;r) may be derived thestatisticsoflocalseaicedeformationandpredetermined
by considering the geometric relationship between straight- satellite tracks, an individual recorded floe chord, D, orig-
line satellite passes and the geometry of the floes they pass inating from a floe of radius r, was obtained from a satel-
over. Individual floe shapes are highly variable: making an lite trajectory that crosses the floe at a random interior an-
assumption about the distribution of floe shapes may intro- gle θ; thus the distribution of θ is uniform. Because of ro-
duce biases in the statistics derived from the FCD. Yet as tational symmetry, we need only consider θ ∈[0,π), sam-
we prove in Appendix A, the ability to derive FSD statis- pled according to a probability distribution T(θ;r)=π−1.
tics from the FCD does not depend on the precise form of The length D is thus a chord of this circular floe, with
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

| 2872 |     |     |     |     |     |     |     |     |     | C.Horvatetal.:Floesfromaltimetry |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
D=2rsin(θ/2).Accordingly,
|     |     |     |     |     |     |     |     | r and P | can represent |                                        | only those | floes whose |     | size is | larger |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | -------------------------------------- | ---------- | ----------- | --- | ------- | ------ |
|     |     |     |     |     |     |     |     | thanr   | =D            | /2,thesmallestpossiblefloesizesampled. |            |             |     |         |        |
|     |     |     | (   |     |     |     |     | m i n   | m             | in                                     |            |             |     |         |        |
∂θ 2 √ 1 r >D/2, For pe r f ect po w er-law distributions beginning at a scale of
| Fe(D;r)=T(θ;r) |     |     | =   | π        |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                |     |     |     | (2r)2−D2 |     |     | (3) |     |     |     |     |     |     |     |     |
∂D 0 otherwise, r or before, both metrics are functions of r . However,
|     |     |     |     |     |     |     |     | min |     |     |     |     | min |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fortherealFCDsmeasuredhere,amaximumfloesizeexists,
whichisaprobabilityfunctionthatmeetstheabovecriterion andapower-lawscalingisnotfoundapproachingr min ,sothe
| (Eq.2). |     |     |     |     |     |     |     | useofsuchmetricsisjustified(seeSect.4).Becauseofthe |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ThenthmomentofthefloechorddistributionS(D)isde- finitesamplingresolutionofthealtimeter,chordsthatwould
fined originate from floes with a diameter near the sampling res-
|     |     |     |     |     |     |     |     | olution may | not | be observed, | and | thus (cid:104)Dn(cid:105)≤A |     | (cid:104)rn(cid:105). | We  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | --------------------------- | --- | --------------------- | --- |
|     | ∞   |     | ∞   |     | ∞   |     |     |             |     |              |     |                             |     | n                     |     |
|     | Z   |     | Z   |     | Z   |     |     |             |     |              |     |                             |     |                       |     |
(cid:104)Dn(cid:105)≡ DnS(D)dD= DnFe(D;r)dD. explore this uncertainty in Appendix B. For a known floe
|     |     |     |     | drP(r) |     |     | (4) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sizedistribution,theerrordecreasesexponentiallyasafunc-
|     | 0            |         | 0   |            | 0   |       |            | tionofthedistributionalmomentbeingconsidered,thoughit |      |     |          |              |        |     |      |
| --- | ------------ | ------- | --- | ---------- | --- | ----- | ---------- | ----------------------------------------------------- | ---- | --- | -------- | ------------ | ------ | --- | ---- |
|     |              |         |     |            |     |       |            | can be large                                          | (20% | or  | more) in | pathological | cases. | For | dis- |
| For | any function | Fe(D;r) |     | satisfying | the | scale | invariance |                                                       |      |     |          |              |        |     |      |
tributionaltailscharacterizedbyobservedscalingexponents
above,theright-handsidemaybeexpressedintermsofmo-
(Sternetal.,2018b),andformomentsconsideredhere,this
| ments | of P(r) | (see Appendix |     | A). | For circular | floes, | using |             |     |               |     |                |     |              |     |
| ----- | ------- | ------------- | --- | --- | ------------ | ------ | ----- | ----------- | --- | ------------- | --- | -------------- | --- | ------------ | --- |
|       |         |               |     |     |              |        |       | uncertainty | can | be determined |     | systematically |     | and vanishes |     |
Eq.(3),
formeasurementspacingssmallerthantheradiusofthemost
∞ 2r common floe size. This resolution error does not affect the
|     | Z   | Z   |     | Dn  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2 analysis of the power-law hypothesis, as that analysis is fo-
| (cid:104)Dn(cid:105)= |     | drP(r) |     |     | dD  |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p cused on the distributional tail. However, because P is pro-
|     |     |      | π (2r)2−D2 |     |     |     |     |                                                    |     |     |     |     |     |     |     |
| --- | --- | ---- | ---------- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 0    |            |     |     |     |     | portionaltoanegativemomentoftheFCD,itissensitiveto |     |     |     |     |     |     |     |
|     | ∞   |      |            | π   |     |     |     | changesinthenumberofsmallchordlengths.Becauseofthe |     |     |     |     |     |     |     |
|     | Z   | 2n+1 | Z2         |     |     |     |     |                                                    |     |     |     |     |     |     |     |
= drP(r) rn sin(x)ndx=A (cid:104)rn(cid:105), (5) measurement uncertainty for smaller chord lengths we will
n
|     |     | π   |     |     |     |     |     | focusinsteadonr,whichisapositivemomentoftheFCD. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   |     | 0   |     |     |     |     |                                                 |     |     |     |     |     |     |     |
2.1 Evaluatingthefloesizepower-lawhypothesiswith
| where           | D ≡ξ | =sin(x),(cid:104)rn(cid:105)isthenthmomentofP(r),and |     |     |     |     |     |               |     |     |     |     |     |     |     |
| --------------- | ---- | ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|                 | 2r   |                                                      |     |     |     |     |     | floechorddata |     |     |     |     |     |     |     |
| thecoefficientA |      | is                                                   |     |     |     |     |     |               |     |     |     |     |     |     |     |
n
|     |     |     |      |     |     |            |          | Suppose | the | FSD P(r) | has | a power-law |     | tail that | be- |
| --- | --- | --- | ---- | --- | --- | ---------- | -------- | ------- | --- | -------- | --- | ----------- | --- | --------- | --- |
|     | 1   |     | π    |     |     |            |          |         |     |          |     |             |     |           |     |
|     | Z   | 2n  | +1Z2 |     | n   | (cid:18)n+ | (cid:19) |         |     |          |     |             |     |           | ≡   |
ξnG(ξ)dξ= sin(x)ndx= 2 1 1 g in s at so m e s p ec i fie d va l ue r 1 . T h e n f o r r > r 1 , P (r )
| An ≡ |     |     |     |     | B   |     | , , |     |     | −   |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
π π 2 2 P (r ;α ,C ) = C r α , f or a n u n k n o w n c o ef fi cie n t C a n d
|       | 0      |                                         | 0   |          |     |       |           | power-lawslopeα.IntegratingEq.(1)overallr, |     |     |     |     |     |     |     |
| ----- | ------ | --------------------------------------- | --- | -------- | --- | ----- | --------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| where | B is   | the beta function.                      |     | For n=0, | 1,  | 2, or | 3, then A |                                            |     |     |     |     |     |     |     |
|       |        |                                         |     |          |     |       | n         |                                            | ∞   |     |     |     |     |     |     |
|       | 4,2,or | 32.TwoimportantFSD-derivedquantitiesare |     |          |     |       |           |                                            | Z   |     |     |     |     |     |     |
is1,
|         | π    | 3π        |     |          |     |           |        | S(D)= | Fe(D;r)P(r)dr, |     |     |     |     |     | (8) |
| ------- | ---- | --------- | --- | -------- | --- | --------- | ------ | ----- | -------------- | --- | --- | --- | --- | --- | --- |
| derived | from | ratios of | FSD | moments, | and | therefore | can be |       |                |     |     |     |     |     |     |
0
| obtained | from | the FCD | directly: | the | “representative |     | radius” |     |     |     |     |     |     |     |     |
| -------- | ---- | ------- | --------- | --- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
(HorvatandTziperman,2017;Roachetal.,2018a), wheretheintegraloftheleft-handsideofEq.(1)isequalto
R
|     |     |     |     |     |     |     |     | S(D)as | F(r;D)dr | =1.UndertheassumptionofEq.(2), |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------------------------------ | --- | --- | --- | --- | --- |
∞
R r3P(r)dr if P is a power law, so is S(D) (Appendix A). For circular
|     |     | (cid:104)r3(cid:105) |     | 3π (cid:104)D3(cid:105) |     |     |     |        |     |     |     |     |     |     |     |
| --- | --- | -------------------- | --- | ----------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| r ≡ | 0   | =                    | =   |                         | ,   |     | (6) | floes, |     |     |     |     |     |     |     |
∞
|                                                     | R        | (cid:104)r2(cid:105) |     | 16 (cid:104)D2(cid:105) |     |     |     |       |     |            |     |     |     |     |     |
| --------------------------------------------------- | -------- | -------------------- | --- | ----------------------- | --- | --- | --- | ----- | --- | ---------- | --- | --- | --- | --- | --- |
|                                                     | r2P(r)dr |                      |     |                         |     |     |     |       | ∞   |            |     |     |     |     |     |
|                                                     |          |                      |     |                         |     |     |     |       | 2CZ | r−α        |     |     |     |     |     |
|                                                     | 0        |                      |     |                         |     |     |     | S(D)= |     |            | dr. |     |     |     | (9) |
|                                                     |          |                      |     |                         |     |     |     |       | π   | p (2r)2−D2 |     |     |     |     |     |
| andthefloeperimeterpericearea,ameasureofseaicefrag- |          |                      |     |                         |     |     |     |       | r1  |            |     |     |     |     |     |
mentation,
Becauseofthesamplingresolutionofthealtimeterthereisa
(cid:28)D∗≡2·r
|     | ∞         |     |     |     |     |     |     | minimumresolvedchordscaleD |             |          |     | .IfD    |           |           | ,   |
| --- | --------- | --- | --- | --- | --- | --- | --- | -------------------------- | ----------- | -------- | --- | ------- | --------- | --------- | --- |
|     | R rP(r)dr |     |     |     |     |     |     |                            |             |          |     | min     | min       |           | 1   |
|     |           |     |     |     |     |     |     | there is                   | an explicit | solution | for | S(D), a | power-law | distribu- |     |
π (cid:104)D1(cid:105)
| ≡   | 0   | =   |                        |     |     |     |     | tionovertherange(D∗,∞), |     |     |     |     |     |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| P   |     |     |                        | .   |     |     | (7) |                         |     |     |     |     |     |     |     |
|     | ∞   |     | 2 (cid:104)D2(cid:105) |     |     |     |     |                         |     |     |     |     |     |     |     |
R r2P(r)dr
(cid:18) (cid:19) 2α−1
1 α
|     | 0   |     |     |     |     |     |     | S(D)=C·B |     | ,   | D −α | ≡C D | −α, |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- | ---- | --- | --- | ---- |
α
|       |         |            |     |            |         |      |         |     |     | 2 2 | π   |     |     |     |     |
| ----- | ------- | ---------- | --- | ---------- | ------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| These | derived | quantities |     | are useful | because | they | require |     |     |     |     |     |     |     |     |
nofurtherinformationabouttheseaice(suchasitsconcen- where B is the beta function. The coefficient C is a multi-
α
tration) to compare against modeled FSDs. However, both plicativefactorindependentofsize,andthepower-lawexpo-
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

| C.Horvatetal.:Floesfromaltimetry |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2873 |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
nentforaFCDisthesameastheexponentforFSD,where ucl.ac.uk/csopr/seaice.html, last access: 9 January 2019).
thetwoarerelatedbyEq.(1). CryoSat-2 radar echo returns are defined as “lead”, “floe”,
Moments of a power-law tail can be evaluated explicitly “openocean”,or“ambiguous”accordingtowaveformshape
(forα>n+1), and sea ice concentration (Tilling et al., 2016, 2018), at an
|                        |        |     |        |     |     |     |      | approximately | constant       |         | along-track | spacing    |               | D   | =300m. |
| ---------------------- | ------ | --- | ------ | --- | --- | --- | ---- | ------------- | -------------- | ------- | ----------- | ---------- | ------------- | --- | ------ |
|                        | ∞      |     |        |     |     |     |      |               |                |         |             |            |               | min |        |
|                        | Z      |     | rn+1−α |     |     |     |      |               |                |         |             |            |               |     |        |
|                        |        |     |        |     |     |     |      | Floe chords   | are            | defined | as a        | continuous | sequence      |     | of one |
| (cid:104)rn(cid:105)=C | rn−αdr | =C  | 1      | .   |     |     | (11) |               |                |         |             |            |               |     |        |
|                        |        |     |        |     |     |     |      | or more       | “floe echoes”, |         | with        | a gap of   | one ambiguous |     | echo   |
n+1−α
|     |     |     |     |     |     |     |     | permitted | within | a floe | sequence | to  | allow | for anomalous |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------ | -------- | --- | ----- | ------------- | --- |
r1
|     |     |     |     |     |     |     |     | returns. | A chord | length | is taken | from | the midpoint |     | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | -------- | ---- | ------------ | --- | ------ |
ThenforboththeFCDandFSD,theratiooftwomomentsis
|     |     |     |     |     |     |     |     | first to themidpoint |     | of  | the last | radarecho. | Individual |     | chord |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------- | ---------- | ---------- | --- | ----- |
independentoftheunknowncoefficientC,i.e.,
|     |     |     |     |     |     |     |     | lengths | can be | underestimated |     | when | continuous |     | floes are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------------- | --- | ---- | ---------- | --- | --------- |
(cid:104)Dn+(cid:15)−1(cid:105) separated artificially by producing two or more ambiguous
n−α
R ≡ =D(cid:15) , (12) echoesinsequence,orwhenhighlyreflectiveleadsdominate
| n,(cid:15) | (cid:104)Dn−1(cid:105) |     | minn+(cid:15)−α |     |     |     |     |              |        |       |     |          |          |       |      |
| ---------- | ---------------------- | --- | --------------- | --- | --- | --- | --- | ------------ | ------ | ----- | --- | -------- | -------- | ----- | ---- |
|            |                        |     |                 |     |     |     |     | the waveform | return | close | to  | the floe | edge and | cause | mea- |
n+(cid:15)<α. surement dropout (Tilling et al., 2019b). Lead contamina-
| valid for |     | The | power-law |     | coefficient | can | be ob- |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tainedforanyn,(cid:15) as tion,or“snagging”(ArmitageandDavidson,2014),ismore
|               |     |            |             |     |     |     |      | likely when                                          | the | altimeter | cuts | off a small | section |     | of a floe, |
| ------------- | --- | ---------- | ----------- | --- | --- | --- | ---- | ---------------------------------------------------- | --- | --------- | ---- | ----------- | ------- | --- | ---------- |
|               |     | R          |             |     |     |     |      | i.e.,forsmallvaluesofθ.Overestimatesofchordlengthcan |     |           |      |             |         |     |            |
| α =n+(cid:15) |     | n,(cid:15) | = constant. |     |     |     | (13) |                                                      |     |           |      |             |         |     |            |
| n,(cid:15)    |     | −D(cid:15) |             |     |     |     |      |                                                      |     |           |      |             |         |     |            |
R n,(cid:15) alsooccurwhenicefloesareinclosecontactwithneighbor-
min
ingfloes.Therefore,floechordlengthsshouldbeconsidered
In the analysis below we will arbitrarily select only n= a satellite-derived product, not a true measurement of floe
| 0.5,(cid:15)=1 | for comparison |     | (for | scaling | coefficients | α>1.5, |     |                                      |     |     |     |     |     |             |     |
| -------------- | -------------- | --- | ---- | ------- | ------------ | ------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | ----------- | --- |
|                |                |     |      |         |              |        |     | size.TheminimumchordlengthretrievalD |     |     |     |     |     | islimitedto |     |
min
thebulkofreportedpower-lawcoefficientsareinthisrange; the CryoSat-2 footprint (∼300m along-track) (see the dis-
Sternetal.,2018b).Becausetheobservationswillnotbeper-
cussioninAppendixB).However,surfacediscriminationvia
| fect power-law |     | distributions, |     | we will | use α | ≡α∗ | as an |           |           |          |     |        |         |      |       |
| -------------- | --- | -------------- | --- | ------- | ----- | --- | ----- | --------- | --------- | -------- | --- | ------ | ------- | ---- | ----- |
|                |     |                |     |         | 0.5,1 |     |       | altimetry | is highly | accurate | in  | months | without | melt | ponds |
estimator.Asecondestimateofthepower-lawscalingcoef- (Peacock and Laxon, 2004; Guerreiro et al., 2017; Quartly
| ficient, αˆ, | is computed |     | via the | maximum | likelihood |     | estima- |                |        |            |     |           |        |           |     |
| ------------ | ----------- | --- | ------- | ------- | ---------- | --- | ------- | -------------- | ------ | ---------- | --- | --------- | ------ | --------- | --- |
|              |             |     |         |         |            |     |         | et al., 2019), | giving | confidence |     | that floe | echoes | represent | a   |
tor (Muniruzzaman, 1957; Clauset et al., 2009; Virkar and coherent length of ice. More details on the details of chord
Clauset,2014)(detailsinAppendixC)as
identificationmaybefoundinTillingetal.(2019b).Indeed,
theserawfloechorddatahavebeenusedsuccessfullytore-
N
αˆ =1+ , (14) duce biases in altimeter-observed satellite sea ice thickness
P N
ln Di estimatesfromaltimeterswithdifferentfootprintsizes(Till-
Dmin
|     | i=1 |     |     |     |     |     |     | ingetal.,2019b).Hereweanalyzetheseaicefloesizedis- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
tributionusingthatfloechordproduct.
whereN isthenumberofchords.Ifthepower-lawhypoth-
Figure2showsanexampleoffloechorddataforasingle
| esis holds, | then | the two | estimates | of  | α agree, | although | the |           |       |          |        |       |         |       |       |
| ----------- | ---- | ------- | --------- | --- | -------- | -------- | --- | --------- | ----- | -------- | ------ | ----- | ------- | ----- | ----- |
|             |      |         |           |     |          |          |     | CryoSat-2 | track | over the | Arctic | on 21 | January | 2014. | Free- |
αˆ
| agreement | of  | and | α n,(cid:15) is | not sufficient |     | to confirm | the |              |     |        |               |     |         |             |     |
| --------- | --- | --- | --------------- | -------------- | --- | ---------- | --- | ------------ | --- | ------ | ------------- | --- | ------- | ----------- | --- |
|           |     |     |                 |                |     |            |     | board values | for | echoes | discriminated |     | as floe | are plotted | in  |
power-lawhypothesis.IntheSupplementSect.S1,wecom-
|     |     |     |     |     |     |     |     | Fig. 2b | as a function | of  | the along-track |     | distance | in  | kilome- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --------------- | --- | -------- | --- | ------- |
parethesetwoestimateswhentheyareevaluatedagainstsyn-
ters,andcorrespondtothebluecircleinFig.2a.Floechords
theticdatasetsdrawnfromatruepower-lawdistribution.The
areidentifiedasblacksegmentsinFig.2b.Thehistogramof
| two agree | even | when | the size | of the | data is relatively |     | small |     |     |     |     |     |     |     |     |
| --------- | ---- | ---- | -------- | ------ | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
all741identifiedchordsforthissinglesatellitepassisshown
(N <25).WhileinpracticeEq.(13)iseasytoapply,itonly
inlog-logspaceinFig.2d.
| holds when | α   | >n+1, | and | unlike | the method | of  | Clauset |     |     |     |     |     |     |     |     |
| ---------- | --- | ----- | --- | ------ | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
n,(cid:15) The full CryoSat-2 dataset examined here spans the time
etal.(2009),itdoesnotallowforarobuststatisticalanalysis
|     |     |     |     |     |     |     |     | period | from October |     | 2010 | to November |     | 2018, | and floe |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ---- | ----------- | --- | ----- | -------- |
ofthepower-lawfit,andshouldonlybeusedwhenthedata
|     |     |     |     |     |     |     |     | chords measured |     | using | the above | technique |     | are binned | into |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | --------- | --------- | --- | ---------- | ---- |
areassumedtofollowapower-lawalready.
|     |     |     |     |     |     |     |     | the CICE   | sea ice | model’s | two-dimensional |            |     | sea ice | grid for |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | --------------- | ---------- | --- | ------- | -------- |
|     |     |     |     |     |     |     |     | each month | and     | year    | to facilitate   | comparison |     | with    | model    |
3 Climatologyandtrendsinfloepropertiesderived products. This implies that we invoke the principles of
isotropy,homogeneity,andstationarityoftheFCD,required
fromCryoSat-2altimetry
|     |     |     |     |     |     |     |     | to produce | such | a distribution, |     | on the | length | scale | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --------------- | --- | ------ | ------ | ----- | ------ |
WeapplytheanalytictechniquedescribedinSect.2toafloe CICEmodelgrid(O(25km))andtimescaleofamonth.For
chord dataset constructed from the CryoSat-2 radar altime- every grid cell i, month m, and year y, we have a vector of
terprocessedbytheCenterforPolarObservationandMod- floechords{D }fromwhichwebuildaFCD.Thebase10
i,m,y
elling(CPOM)overtheperiodfromOctober2010topresent logarithmofthetotalnumberoffloechordsrecordedineach
(CPOM data products are available at http://www.cpom. gridcellpermonthisshowninFig.2a.Becausethesatellite
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

2874 C.Horvatetal.:Floesfromaltimetry
Figure2.ConstructingaFCDfromaltimetry.(a)Base10logarithmofthenumberoffloechordsidentifiedandbinnedintotheCESMgrid,
acrossallCryoSatreturnsintheArcticfrom2010to2018.Blacklineisasinglesatellitetrackon21January2014.(b)Subsectionofthe
track centered on the blue dot in (a). Blue line is freeboard of sea ice in radar echoes defined as “floes” along the track. Black lines are
chordsidentifiedfromthefreeboardretrieval.(c)TotalnumberofchordsmeasuredineachmonthintheArctic.Plotiscenteredon1January.
(d)FCDforthesatellitetrackdepictedin(a).Blackmarksonthexaxisarethelogarithmicallyspacedchordlengthbins.
passesaredensestnearthepole,themeasurementdensityis ability.Thereisnostatisticallysignificantlineartrendatthe
highest near the pole as well. Figure 2c shows the number p=0.05level.
of Arctic measurements in each month. Sea ice type from The geographic variability of representative radius over
CryoSat-2 is not available during summer months, as melt the “early winter” (October–December) and “late winter”
ponds make it difficult to discriminate between leads and (February–April) periods is shown in Fig. 3c–d, for all grid
ponded floe surfaces, and we do not include measurements areas.Wedisplayonlythoseareaswithatleast25recorded
from May to September. Across the entire set of satellite floe lengths in each month during the averaging period. In
tracks included here, 11 million chord lengths are recorded Sect.S2andFig.S1,weexaminethesensitivityofbulkFSD
intheArctic. statisticstothisthreshold,findingsimilarseasonalcyclesand
Figure 3a shows the seasonal cycle of Arctic representa- climatologies. The largest representative radii in the Arctic
tive radius over the CryoSat-2 period obtained by applying lieintheinteriorArcticnearthepole,withatongueoflarge
Eq.(6)tothebinnedCryoSat-2floechordproduct.Individ- floes that extends along the Canadian Arctic in late winter.
ualyearsareplottedasthinlines,andtheclimatologicalav- Thereisanotableincreaseinrepresentativeradiuswithlat-
erage is shown in red. Details on how temporal and spatial itude. In Fig. S2, we show that this relationship cannot be
averagestatisticsarecomputedareincludedinAppendixD. explained as a result of the increasing density of measure-
During the months of October–December, the climatolog- mentsnearthepoleandmaythereforebeageophysicalsig-
ical representative radius is roughly 35% larger (7.06km nal.Thesmallestrepresentativeradii(below1km)lieinthe
vs.5.18km)thanduringFebruary–April.Thisseasonalcycle BeringStraitandtheRussianArcticinearlywinterandinthe
is broadly consistent across years. A possible interpretation LaptevSeainlatewinter.Thedifferenceinrepresentativera-
of this seasonal cycle is that large first-year ice pans form diusbetweenfallandspringisaccountedforbythereduction
inOctoberandarelaterfracturedintosmallerfloesthrough- offloesizesinregionsneartheArcticinterior(seeFig.6).
out the winter months. This concept is supported by obser-
vations that large-scale fracturing of sea ice in the Beaufort
Seaisdominatedbycoastalprocessesandthereforecanonly 4 Evaluatingthepower-lawhypothesisusingfloesize
occuronceseaicefreezestothecoastinmidwinter(Richter- statisticsderivedfromCryoSat-2
Menge, 2002), although such an interpretation is specula-
tiveandmustbeevaluatedfurtherasthismethodisrefined. Givenacollectionofchordlengths,wewouldliketoexam-
Figure3bshowsannual-averagerepresentativeradiusinred inewhetheritisdistributedaccordingtoapowerlaw.Under
for each full year from 2011 to 2017, with thin lines cor- theassumptionsofSect.2,thescalingbehavioroftheFSDis
responding to the individual months within that year. Sea- thesameasoftheFCD(seeAppendixA).Weusethestatis-
sonalvariabilityissignificantlylargerthaninter-annualvari- ticalmethodologyoutlinedinClausetetal.(2007,2009)and
VirkarandClauset(2014)(whichwetermtheMLEmethod)
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

| C.Horvatetal.:Floesfromaltimetry |     |     |     |     |     |     |     |     |     |     |     |     |     | 2875 |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
it,P(αˆ,D∗).Wealsocomputethedistancebetweenthe
|     |     |     |     |     |     |     | observedFCDandP(αˆ,D∗).Ap |      |     |              |                              | value,p,isequalto   |       |             |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | ---- | --- | ------------ | ---------------------------- | ------------------- | ----- | ----------- |
|     |     |     |     |     |     |     | thefractionofthoseM       |      |     |              | syntheticFCDsthatare“further |                     |       |             |
|     |     |     |     |     |     |     | away”                     | from | the | hypothesized |                              | power-law           | model | than is     |
|     |     |     |     |     |     |     | theobservedFCD.WeuseM     |      |     |              |                              | =10000,whichpermits |       |             |
|     |     |     |     |     |     |     | computation               |      | of  | p within     | 0.005                        | (Clauset            | et    | al., 2009), |
andruleoutthepower-lawhypothesisunderthecondi-
tionp<0.1(VirkarandClauset,2014).
Wenotethatapowerlawdescribesthescalingofadistri-
|     |     |     |     |     |     |     | bution’s  | tail.          | Previous | observational |             | studies  | have    | discussed   |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | -------- | ------------- | ----------- | -------- | ------- | ----------- |
|     |     |     |     |     |     |     | “double   | power          | laws”    | (i.e.,        | Toyota      | et al.,  | 2011),  | i.e., two   |
|     |     |     |     |     |     |     | power-law | distributions  |          | of            | a different | exponent |         | joined at a |
|     |     |     |     |     |     |     | specified | scale.         | The      | methods       | employed    | here     | would   | capably     |
|     |     |     |     |     |     |     | capture   | the large-size |          | power-law     | scaling     |          | but not | the small-  |
scalescaling.Suchdoublepowerlawsarenecessarilyscale-
Figure3.(a,b)TemporalandgeographicvariabilityofArcticrep-
variant,andrequireatleastthreeparameterstodescribe.The
resentativeradius.(a)ClimatologyofArctic-averagerepresentative
radius in units of kilometers (red line). Thin lines are individual conceptualandmathematicalsimplicityofthepower-lawhy-
|                                                            |     |                |     |        |                |        | pothesis       | does | not apply | in  | such a | case, and | we do | not con- |
| ---------------------------------------------------------- | --- | -------------- | --- | ------ | -------------- | ------ | -------------- | ---- | --------- | --- | ------ | --------- | ----- | -------- |
| CryoSat-2 years.                                           | (b) | Annual-average |     | Arctic | representative | radius |                |      |           |     |        |           |       |          |
| (redline).Thinlinesaretheaverageinindividualmonths.(c)Cli- |     |                |     |        |                |        | siderthemhere. |      |           |     |        |           |       |          |
matologicalrepresentativeradiusinthemonthsOctober–December. The MLE method is a rigorous test of the power-law hy-
(d)Sameas(c)butforFebruary–April. pothesisthateliminatespotentialhumanbiaswheninterpret-
|     |     |     |     |     |     |     | ing observational |          | data. | To     | illustrate | why        | this is | important, |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | ----- | ------ | ---------- | ---------- | ------- | ---------- |
|     |     |     |     |     |     |     | we first          | consider | the   | entire | set of     | 11 million | chord   | lengths    |
toevaluateshapeparametersofthemostlikelypower-lawfit
|     |     |     |     |     |     |     | recorded | in the | Arctic | in all | months | (October–April), |     | span- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | ------ | ------ | ---------------- | --- | ----- |
andtotestitsplausibility.Thismethodhasbeenusedtoeval-
|     |     |     |     |     |     |     | ning a | length | range | from | 300m to | 100km. | The | histogram |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ----- | ---- | ------- | ------ | --- | --------- |
uatepower-lawbehaviorinarecentFSDmodel(Horvatand of these floe chords is the black line in Fig. 4a (hashes on
| Tziperman, | 2017) | and observational |     | studies | (Hwang | et al., |     |     |     |     |     |     |     |     |
| ---------- | ----- | ----------------- | --- | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
blacklinearethelogarithmicallyspacedbincenters).Begin-
2017;Sternetal.,2018b)andproceedsasfollows.
|                   |     |     |      |                |     |           | ning from | D∗=D |         | =900m, | αˆ           | =1.97 | (blue       | line) and |
| ----------------- | --- | --- | ---- | -------------- | --- | --------- | --------- | ---- | ------- | ------ | ------------ | ----- | ----------- | --------- |
|                   |     |     |      |                |     |           |           |      | min     |        |              | all   |             |           |
|                   |     |     |      |                |     |           | α∗ =2.05  | (not | shown). | The    | observations |       | are further | away      |
| 1. Lower-truncate |     | the | FCD. | First identify |     | a minimum |           |      |         |        |              |       |             |           |
|                   |     |     |      |                |     |           | all       |      |         |        |              | ,D∗)  |             |           |
chordscale,D∗,abovewhichwehypothesizeapower- from synthetic data drawn from P(αˆ in each of the
all
|           |     |         |            |      |       |          | M =1000 | random | draws |     | (p =0/1000) |     | and we | reject the |
| --------- | --- | ------- | ---------- | ---- | ----- | -------- | ------- | ------ | ----- | --- | ----------- | --- | ------ | ---------- |
| law tail, | and | analyze | only those | floe | chord | measure- |         |        |       |     | all         |     |        |            |
ments.Weeither(a)chooseD∗ tobe900m(toreduce power-lawhypothesisforthesemeasurements.Wenotethat
|            |     |            |          |     |                  |     | if the resolution |           | bias | explored | in                  | Appendix | B proves | to be      |
| ---------- | --- | ---------- | -------- | --- | ---------------- | --- | ----------------- | --------- | ---- | -------- | ------------------- | -------- | -------- | ---------- |
| the impact | of  | small-size | sampling |     | errors discussed | in  |                   |           |      |          |                     |          |          |            |
|            |     |            |          |     |                  |     | larger than       | expected, |      | the      | underrepresentation |          | of       | small floe |
Sect.2)or(b)usetheschemedescribedinClausetetal.
|        |             |     |      |        |          | D∗    | lengthsmayaffecttheanalysisofthefulldistribution. |     |     |     |     |     |     |     |
| ------ | ----------- | --- | ---- | ------ | -------- | ----- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| (2007) | to evaluate | the | most | likely | value of | for a |                                                   |     |     |     |     |     |     |     |
ExaminingthetailofthedistributioninFig.4a,themax-
| power-law | tail. | The length | of  | this lower-truncated |     | dis- |     |     |     |     |     |         |     |     |
| --------- | ----- | ---------- | --- | -------------------- | --- | ---- | --- | --- | --- | --- | --- | ------- | --- | --- |
|           |       |            |     |                      |     |      |     |     |     |     | D∗  | ≈15.0km |     |     |
tribution is N. In the descriptions that follow, we use imum likelihood estimate of is (red vertical
|     |     |     |     |     |     |     | line, vertical |     | shaded | region | is the | range | of uncertainty | for |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------ | ------ | ----- | -------------- | --- |
thesubscript“all”todescribecase(a)and“tail”tode-
D∗),abovewhichthereare∼40000chordlengthmeasure-
scribecase(b).
mentsbetween24.7and99km(0.4%ofthedataset).Onthe
2. Compute power-law scaling estimates and parame- truncatedFCD,αˆ =4.65(redline,dashedlinesareuncer-
tail
|                  |     |     |        |               |     |            | taintyrangesforαˆ |     |      | )andα∗ | =4.67(notshown),similarto |     |     |     |
| ---------------- | --- | --- | ------ | ------------- | --- | ---------- | ----------------- | --- | ---- | ------ | ------------------------- | --- | --- | --- |
| ter uncertainty. |     | We  | obtain | two estimates |     | of the FCD |                   |     | tail |        |                           |     |     |     |
|                  |     |     |        |               | α∗  |            |                   |     |      |        | tail                      |     |     |     |
scaling estimate, either computing via Eq. (13) or thelarge-scaleroll-offreportedinobservations(Toyotaetal.,
computing αˆ, and uncertainty estimates in both αˆ and 2016).EvenwhenrestrictedtotheFCDtail,p =0/1000.
tail
D∗
via the MLE method (Eq. 14). That the two esti- Finding no statistical basis for a power-law fit to the tail
mates of α agree is a necessary condition for the FCD inFig.4aunderscoresthechallengeinusingthehumaneye
(andthusFSD)tobepower-lawdistributed.
toobservepower-lawscaling.Whiletheblackandredlines
|            |     |              |     |               |     |         | in Fig. | 4a appear | similar | across | much | of  | the range | of sizes |
| ---------- | --- | ------------ | --- | ------------- | --- | ------- | ------- | --------- | ------- | ------ | ---- | --- | --------- | -------- |
| 3. Examine | the | plausibility | of  | the power-law |     | fit. We |         |           |         |        |      |     |           |          |
above24.7km,examiningthemisfitbetweenthepower-law
| generate | M FCDs | of  | size N | (the same | number | of syn- |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | ------ | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
estimatesandthedatashowsthatthetwocurvesinfactdiffer
| thetic | chords | as observed | chords), | with | each | synthetic |     |     |     |     |     |     |     |     |
| ------ | ------ | ----------- | -------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
significantlyacrosstheentirefitrange.Amisfiterrorcanbe
| FCDdrawnfromthehypothesizedpower-lawdistribu- |     |     |     |     |     |     | definedas |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
P(αˆ,D∗).
| tion |     | For each | of  | these synthetic |     | FCDs, we |           |     |          |     |            |     |     |     |
| ---- | --- | -------- | --- | --------------- | --- | -------- | --------- | --- | -------- | --- | ---------- | --- | --- | --- |
|      |     |          |     |                 |     |          | *(cid:12) |     | ,D∗)−P(x |     | (cid:12) + |     |     |     |
computetheKolmogorov–Smirnovdistancebetweenit (cid:12)P(x i ,αˆ tail i ) (cid:12)
|         |              |     |           |       |      |           | E=  |     |        |      | ,   |     |     | (15) |
| ------- | ------------ | --- | --------- | ----- | ---- | --------- | --- | --- | ------ | ---- | --- | --- | --- | ---- |
|         |              |     |           |       |      |           |     |     | ,αˆ    | ,D∗) |     |     |     |      |
| and the | hypothesized |     | power-law | model | that | generated |     | P(x | i tail |      |     |     |     |      |
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

2876 C.Horvatetal.:Floesfromaltimetry
Figure4.Examiningthepower-lawhypothesis.(a)HistogramofallchordlengthsrecordedintheArcticforthemonthsNovember–April
(black).Bincentersareindicatedbyhashesandarelogarithmicallyspaced.Thebluelineispower-lawfittoallobservedsizesaccording
to Eq. (14). The red line is power-law fit to the tail. Dashed red lines are fit lines using the ±1 standard deviation values of αˆ. The red
verticallineisthemostlikelybeginningofthepower-lawtail,D∗ ,withshadedregion±1standarddeviationinD∗
.(b)Sameas(a),but
formeasurementsinApril.(c)Maximumlikelihoodestimateofthebeginningofthepower-lawtail,D∗
(km)forallmeasurementsateach
geographiclocationovertheobservationalperiod.OnlylocationswithN>1000areplotted.(d)Maximumlikelihoodestimateofpower-
lawtailexponent,αˆ tail,forthesamepoints.Coloredvalueshavemorethan200chordlengthsinthetailandp>0.1.Zerovaluesarethose
locationsplottedin(c)butwhereeitherp<0.1ortherearefewerthan200measurementsinthetail.(e)Numberofchordlengthsinthetail
(aboveD∗
)ateachlocation.
where x represents the bin locations, angle brackets de- for 8% of the total floe area and 1.4% of the perimeter per
i
noteanaverageovertherelevantbins,andP(x )represents square meter. The misfit error between the April FCD tail
i
theobservedhistogramvalues.Overtherangefrom24.7to and P(αˆ ,D∗) is 76%. Accumulating all measured chord
tail
100km,themisfiterroris33%.Thevisualagreement,misfit lengths from October to May into the CESM model grid,
error,andapparentslopeandshapeofthedistributiondepend wefindzerolocationsthatsupportapower-lawdistribution
sensitivelyonthebinspacingandthelogarithmicplotting. acrosstherangeofmeasurements(i.e.,p >0.1).Forgrid
all
Seaiceparameterizationsthatassumeapower-lawdistri- areas with N >1000, we show the value of D∗ computed
bution may significantly bias sea ice statistics. The imposi- using the local FCD in Fig. 4c. Values of D∗ range from
tion of any fixed distributional shape, when FSD dynamics 2km along the Russian Arctic to more than 10km near the
arescale-variant,leadstoimplicitnonlocalredistributionof NorthPole.
seaicebetweenfloesizecategories(HorvatandTziperman, WhilemostoftheArctichasatleast1000totalmeasure-
2017). To see this in practice we compare the difference in mentsacrossallyears,FCDtails(D>D∗)arenotaswell-
Arctic-wide representative radius, r, which is used in pa- sampled. We investigate these tails including regions with
rameterizations of wave attenuation and ice thermodynam- at least 200 measured floe chords larger than D∗. The per-
ics, between the most-likely power-law fit to the data and centageofgeographicareaswithatleast1000totalmeasure-
the“true”valueobtainedviaEq.(6).Theobservationsyield mentsthathaveatailwithatleast200measurementsis44%;
r =10.2km,versus34.5kmforthepower-lawfit.Examining onaverageD∗ is5.4kmfortheseregions.Formostofthese
onlythetailofthedistribution(chordlengthsabove24.7km) regionswecannotruleoutapower-lawtail.Forthesubset
yields better agreement: 23.7km for the observations and ofregionswith1000totalmeasurements,200measurements
24.4kmforthefitline.Yetthistailconstitutesjust1%ofall in the tail, and where the power-law hypothesis cannot be
measuredchordlengths,correspondingtojust18%oftotal ruledout,theaverageD∗ is6.5kmandaverageαˆ is3.34,
tail
iceareaand4.5%oftheperimeterpersquaremeter(Eq.7). withinthetypicalrangeofArcticFSDmeasurements(Stern
Segmenting the chord length data into individual months etal.,2018b).InFig.4dweshowthevaluesofαˆ atthese
tail
in the Arctic, there are none where p >0. Examining locations.Coloredcellsarethosewithp>0.1andatailwith
all
only the tail of each month’s distribution, p <0.1 in all at least 200 measurements. In Fig. 4e we show the base 10
tail
months. Only in April is there a nonzero p =0.04, for logarithmoftheMLEtailforallgeographiclocations.Those
tail
whichtheanalysisofFig.4aisrepeatedasFig.4b.InApril, regions for which a power law cannot be ruled out are gen-
αˆ =1.99,αˆ =5.70,andD∗=30.7km.Thetailconsists erally those with the largest floes and the highest sampling,
all tail
of 1618 measured chord lengths up to 97.5km, accounting clustered near the central Arctic. The weakest support for a
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

C.Horvatetal.:Floesfromaltimetry 2877
Figure 5. Top row: Temporal variability of power-law fits to Arctic FCDs. (a) Estimate of the most likely power-law scaling coefficient
forallrecordedfloechordsasafunctionofmonthoverallyears,calculatedfromtheMLEmethodEq.(14)(redlines)orEq.(13)(blue
lines).Thicklinesareclimatologicalaverages,andthinlinesareindividualyears.Plotiscenteredon1January.(b)Like(a),butplottedfor
individualyearsoverallmonths.Thicklinesaretheaverageovermonthsplottedin(b)andthinlinesareindividualmonthsineachyear.
(c–d)Sameas(a–b),butforthedistributionaltailstartingfromD∗
computedusingtheMLEmethod.“Arctic”referstopointsabove60
◦
N.
power-law tail is in the Chukchi and Beaufort seas, where 5 Anexamplemodel–observationcomparisonoffloe
power-law floe size distributions have often been reported. sizevariability
We note that our choice of tail length plays an important
role in whether the power-law hypothesis is rejected in the A principal aim of this work is to allow model–data com-
tailacrosstheArctic.Forexample,thefractionofArcticre- parisonsandfacilitatetestingrapidlydevelopingFSD–FSTD
gionswithatleast1000totalmeasurements,atailofatleast models.Herewedemonstratehowsuchacomparisoncanbe
100, 200, and 400 measurements, and that does not reject madeandprovideusefulinformationtomodelers,eveninthe
the power-law hypothesis is 72%, 52%, and 15%, respec- presenceofthehighuncertaintiesinthisnascentFSDrecon-
tively.Thebetter-sampledtheFCD–FSD,themorelikelythe struction technique. With the gridded data provided above,
power-lawhypothesisisrejected. we may now directly compare development-stage sea ice
Scalingcoefficientscanprovideusefulinformationabout models that incorporate FSD effects to observations. To do
the distributional shape. In Fig. 5a–d we show the seasonal so,weusetheRoachetal.(2018a)prognosticmodelforthe
and inter-annual variability of power-law estimates in the FSD–FSTD,basedontheHorvatandTziperman(2015)the-
Arctic.Figure5aplotstheclimatologyofthepower-lawscal- oreticalFSTDframework,implementedintotheCICE5.1.2
ing estimates when including all measured chord lengths in (Hunke et al., 2015) sea ice model. The FSTD is a sea ice
dark red (using Eq. 13) or blue (using 14). Individual years statevariable,subjecttointeractionoffivekeyphysicalpro-
are thin red or blue lines. The two estimates disagree. Be- cesses:lateralgrowth,lateralmelt,fracturebyoceansurface
causeagreementbetweenthetwoestimatesisnecessaryfor waves, welding of floes in freezing conditions, and wave-
the power-law hypothesis to be true (see Sect. 4, Sect. S1), dependent new ice growth (Horvat and Tziperman, 2015,
this alone is sufficient to rule it out. There is a seasonal 2017; Roach et al., 2018a, b). Previously published model
cycle in the power-law fitting to the full distribution, with runs(Roachetal.,2018a)focusedontheimpactoftheFSD
α increasing (steepening) from September to January and onlateralmelt,whichislargelydrivenbysmallfloes(Steele,
all
remaining flat until April and no significant linear trend at 1992),andsofloesizesabove1kmwerenotconsidered.As
thep=0.05levelfortheannual-averagevalueofα .Fig- alargerrangeofscalesisresolvedintheCryoSat-2observa-
all
ure5c–drepeatthisanalysisonthetailofthosemonthlydis- tional product, we conducted a model run that extended the
tributions. In this case, the two estimates agree well. There floesizecategoriestoscaleslargerthan1km,using24loga-
isadifferentseasonalcycleinthesteepnessofthedistribu- rithmicallyspacedfloesizecategoriesfrom0.5mto33km.
tionaltail:shallowestinearlywinterandsteeperinlatewin- This FSTD model simulation is coupled to a slab ocean
ter.Thisindicatesthatthechangesacrossthewintermonths modelandtheWAVEWATCHIIIoceansurfacewavemodel
may be due to a reduction of the largest floes and a steep- (Tolman,2009),forcedbytheJRA-55atmosphericreanaly-
ening of the distributional tail, although there is significant sis(JRA-55,2013)overtheperiodfrom2000to2016.These
inter-annualvariabilityamongtheseestimates.Asimilarsea- wave-coupled runs are branched at year 2000 from a stand-
sonal cycle to that found in Fig. 6a, c, with an FSD that aloneseaicerunfrom1975to2000,spunupusingrepeated
steepensfromSeptembertoApril,wasfoundinimageanal- 1975atmosphericforcing.Additionalmodelphysicsbeyond
ysis of floes in the Beaufort and Chukchi seas (Stern et al., those processes outlined in Roach et al. (2018a) have been
2018b), with α≈2.5, although the distribution steepened added to determine the initial size of newly formed sea ice
monotonically over that period. There is no significant lin- floes as a function of the ocean surface wave field. Details
ear trend at the p=0.05 level in the annual-averaged FSD onthisnewparameterization,modelinitialization,andspin-
tailslope(Fig.5d). up,aredescribedinRoachetal.(2019).Recallingthefinite
measurement resolution of the CryoSat-2 dataset, the mod-
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

2878 C.Horvatetal.:Floesfromaltimetry
Figure6.Geographicandclimatologicalcomparisonofmodeledandobservedrepresentativeradii.(a–b)Averagerepresentativeradiusfrom
NovembertoDecemberin(a)theCryoSat-2observationaldatasetand(b)theFSTDmodel.Greyshadedregionsin(b)aretheinteriorof
contoursin(a),whichrepresent“packice”unaffectedbywavesinthemodelsimulations.(c)ClimatologyofArctic-averagerepresentative
radius in units of kilometer for the MIZ in observations (red) and the model (blue). Green line is the annual average for the “pack”, the
excludedregionsin(b).Thinlinesareaveragesinindividualyearsfrom2011to2016intheMIZ.(d–e)Sameas(a–b),butforthemonths
ofFebruary–April.(f)Annual-averageArcticrepresentativeradiusforwave-affectedregionsinMIZobservations(red),MIZmodel(blue),
andpackiceobservations.ThinlinesaretheaverageinindividualmonthsintheMIZobservations.
eled representative radius is calculated only including floe tive radii greater than 18km. The MIZ region accounts for
sizecategoriesfrom150m(asfloesizesareradii,thiscorre- 37% of grid areas with at least 25 chord measurements in
sponds to a radius equal to the minimum chord length) and months from October to December and 35% of such areas
larger.WeincludeallFCDmeasurementshere(chordlengths for the period February–March. Note that the month of Oc-
above300m)tomakethebroadestcomparison,butnotethat toberisabsentfromtheseplotsbecausenowell-sampledre-
thepotentialunderrepresentationoffloeswithdiametersnear gionsareclassifiedasMIZacrossallmodelyearsaccording
thesamplingresolutionmayleadtoinaccuratevaluesofr in tothecriteriaoutlinedinAppendixD.
regionsmainlyconsistingofsuchfloes. Figure6ccomparestheobserved(red)andmodeled(blue)
Figure 6a–b, d–e compare modeled and observed clima- Arctic-averagerepresentativeradii fortheMIZover thepe-
tologies of Arctic representative radius (for floe diameters riod 2011–2016 as in Fig. 3a. The seasonal cycle of repre-
300mandlarger)averagedover2011–2016andthemonths sentative radius in the MIZ is different in the observations
ofOctober–December(a,b)andFebruary–May(c,d).Geo- (redline;thinorangelinesareindividualmonths)thanwhen
graphicvariabilityofrepresentativeradiusisbroadlysimilar all geographic regions are included (Fig. 3a). The seasonal
between model and observation: the largest floes lie in the cycleofrepresentativeradiusinthepackiceregion(i.e.,not
Arcticinterior,withregionsofsmallerfloesinthestraitsand the MIZ) is shown as a green line in Fig. 6c. In the MIZ,
continental margins. Across the interior Arctic, simulated averagerepresentativeradiiaresmaller(onaverage4.17km
representativeradiiaresignificantlylargerthanarefoundin vs. 6.49km in the pack ice region). In contrast to the sea-
the observations, as the Roach et al. (2018a) FSTD model sonalvariationacrossallgeographicregions(Fig.3a)aswell
does not include processes that break up large floes in the as in the pack ice, floes are larger in February–April than
absenceofoceansurfacewaves.Tocompareseasonalitybe- in November–December (5.40km vs. 3.15km). In both the
tween model and observations, we compare only those re- MIZ and pack ice regions, however, average representative
gionsthatexperiencewavefractureinthemodelruns,areas radiusissimilarinlatewinter.Thelargestdifferencebetween
wecollectivelytermthemarginalicezone(MIZ).TheMIZis thetworegionsisfromNovembertoDecember,whererep-
definedbyexcludingcategoriesthatdonotexperiencewave resentativeradiiaremorethantwiceaslargeinthepackice
fracture in a given month (see Appendix D), shown as the thantheMIZ.
contouredregionsinFig.6a–b,d–fandgreyedoutinFig.6b, Figure 6f shows the annual average representative radius
e.Allexcluded“packice”regionshavemodeledrepresenta- intheMIZ(red),packice(green),andmodeledMIZregions
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

C.Horvatetal.:Floesfromaltimetry 2879
(blue).ModeledMIZrepresentativeradiihaveasimilarmag- Floesizemodelingeffortshavefocusedonmarginalicezone
nitude compared to the MIZ observations, though these re- processes(HorvatandTziperman,2015;Zhangetal.,2015),
gionshavesmallerfloesthantheinterior.Toaddressthescale and particularly floe sizes below about 1km because these
mismatch between the too-high modeled floe sizes and ob- small floes play an important role in sea ice thermodynam-
served representative radii in the interior Arctic, as well as ics for floe sizes. The CryoSat-2 observations, however, are
the strong and different seasonal cycle in representative ra- best suited to resolving floe chords of several hundred me-
diusinbothregions,modelingeffortsmustincludeadditional ters and above. New satellite altimeters like ICESat-2 have
mechanismsforreducingfloesizeintheArcticinterioraway thepotentialtoincreasethechordlengthresolutiontoscales
fromwaves,suchasmechanicalfragmentation(Toyotaetal., of20–100mandprovideinsightatsmallerscales.
2006;Ryndersetal.,2016)orridgedynamics(Robertsetal., Weemphasizestronglythatrefinementmaybenecessary
2019),toobtainrealisticrepresentativeradiiacrosstheentire to apply this method for operational purposes, trend anal-
Arctic,astheseprocessesarenotpresentinthemodelused ysis, and further model validation. This paper has focused
tomakethiscomparison. ontheframeworkformakingaltimetricmeasurementsofthe
FSDandcomparisontomodeloutput,buttheobtainedchord
lengths and distributions have not been carefully validated
6 Conclusions againstotherobservationalmethods,andthiswillbeneces-
sarybeforefurtherapplicationofthismethod.Beforedoing
Herewedevelopedanddemonstratedamethodforderiving so, we have tried to outline the most significant uncertain-
the statistics of the sea ice FSD from satellite radar altime- ties in the method. The typical assumptions of homogene-
termeasurementsofchordlength.Thismethodprovidesthe ity, isotropy, and stationarity are invoked here at the length
firstpan-Arcticaccountingofclimate-relevantquantitiesde- scale of the CICE model grid (O(25)km on each side) and
rivedfromtheFSD,permitstestingofexistingscalinglaws timescaleof1month.Thesestatisticalassumptionsmaynot
previouslyusedtocharacterizedistributionsoffloesize,and besatisfiedif,forexample,thenumberofmeasurementsin
allows for gridded comparisons between FSD models and agivenregionin1monthisinsufficienttosampletheknown
observations.Usingthisnewtechniqueweproducedclima- anisotropy of the sea ice floe field, and additional passes
tological,annual-average,andgeographicmeanmomentsof changethemeanchordlengthsignificantly(seeSect.S2and
theArcticFSDacrossarangeofresolvedlengthscalesfrom Fig.S1).Whilewefoundlittleevidenceforpower-lawscal-
300mto100km. ing throughout most areas of the Arctic, this may be sensi-
Withthecombinationofsatellitealtimetryandmathemat- tivetothegeographic(heretheCICEmodelgridofapproxi-
ical theory, we were able to rigorously examine the power- mately25km×25km)andtemporal(hereallmeasurements
law hypothesis related to the FSD under simple assump- from2010to2018)windowsweusetocollectandevaluate
tions about the underlying floe chord data and the fidelity chord length measurements for a power law. The assump-
of CryoSat-2 satellite retrievals. Segmenting measurements tion of scale-invariant sampling, observational uncertainty
bygeographiclocation,bymonth,andbyyear,wefindlim- becauseofthefinitesamplingresolution,analysisofambigu-
ited statistical basis for a power-law scaling beginning be- ousreturns,andtheaccuracyofretrievalsinregionsofthin
low about 6.5km. In a limited number of geographic loca- seaicemayalsoaffecttheinferredsizeofseaicefloes.This
tions, we find the observational data cannot rule out power- inturnmayaffecttheclimatologiesdescribedinthisstudy.
lawscaling,exceptfortypicalsizesaboveabout6.5km.As- While processed CryoSat-2 data have been validated
suming a power-law floe size distribution can bias sea ice againstbothvisualimageryandground-basedobservations,
modeloutputandconceptualunderstanding,thegeographic theywerenotdesignedwiththisapplicationinmind–addi-
variability and lack of consistent multi-scale behavior rein- tionalqualitycontrolmaybenecessaryforclimatestudiesof
forces the need for sea ice models to account for floe-scale changing floe properties. The positive comparison between
processesratherthandiagnoseadistributionalshape. modelandobservationinSect.5couldalsobeduetoacom-
Observations that span the polar regions and different pensationbetweenthesemeasurementuncertaintiesandwill
years and seasons are valuable for future refinement of needtobere-examinedinfuturevalidationwork.Yetobser-
process-based models of the FSD. In Sect. 5, we demon- vationaluncertaintiesregarding,forexample,thefloeshape
strated how such model–observation comparisons can be distribution can be roughly estimated at the order of the er-
√
madeandcanprovideusefulinsightsformodeldevelopers. rorineffectiveradiusobtainedforcircularfloes(r = A/π)
√
At present, some general features of floe size evolution (in orasquare(r = A/4),witharelativeerrorof25%.Con-
particularthemagnitudeandseasonalcycleoftherepresen- strainingmodelresultsbeyondthisscaleoferrorwillrequire
tative radius) are broadly similar between model and obser- further refinement. However, as shown in Fig. 6, at present
vationinthemarginalicezone.Yetthereisasignificantscale themodel–datamismatchintheinteriorArcticcanexceeda
mismatch in the interior Arctic between the presented sim- factorof3.Evenwithexpectedlevelsoferrorinthepresent
ulations and this observational product because of missing derived FCD–FSD product, some constraints on the model
fragmentationphysicsintheabsenceofoceansurfacewaves. canbeconsideredatpresentwiththismethod.Afuturecom-
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

2880 C.Horvatetal.:Floesfromaltimetry
parisonofresultsfromtheIce-Sat2andCryoSat-2altimeters
willprovideinsightsintotherelevanceofmeasurementand
| statistical | uncertainties, | as  | will comparison |     | of altimetrically |     |
| ----------- | -------------- | --- | --------------- | --- | ----------------- | --- |
derivedfloechordmeasurementswithvisualimagery.
| Even | accounting | for important |     | caveats | that arise | from |
| ---- | ---------- | ------------- | --- | ------- | ---------- | ---- |
makingsatellitemeasurements,remotelysensingtheseaice
| FSD from       | altimeters | at sub-daily |                | resolutions | can             | provide a |
| -------------- | ---------- | ------------ | -------------- | ----------- | --------------- | --------- |
| significant    | increase   | in data      | for comparison |             | and analysis    | of        |
| new sea        | ice models | that         | parameterize   | the         | FSD. Previously |           |
| the difficulty | of         | making       | measurements   | of          | the FSD         | at rele-  |
vantspatialandtemporalscaleshasinhibitedthewidespread
| adoption | of such         | floe-sensitive | sea            | ice models. | Understand-       |     |
| -------- | --------------- | -------------- | -------------- | ----------- | ----------------- | --- |
| ing sea  | ice variability | at             | the floe scale | is          | also an important |     |
aspectofseaiceforecasting,andtheabilitytoremotelyas-
| sess the | sea ice | FSD at near-real | time | will | allow for | further |
| -------- | ------- | ---------------- | ---- | ---- | --------- | ------- |
improvementofoperationalforecastingnetworks.
| Dataavailability.                |           | CPOM sea   | ice data, | including   | raw floe           | length |
| -------------------------------- | --------- | ---------- | --------- | ----------- | ------------------ | ------ |
| data, are                        | available | through    | the CPOM  | data portal | at http://www.     |        |
| cpom.ucl.ac.uk/csopr/seaice.html |           |            | (last     | access:     | 1 November         | 2019). |
| The processed                    | FCD–FSD   | statistics | are       | available   | at https://github. |        |
com/chhorvat/CRYOSAT-FLOES/(lastaccess:1November2019).
| The Roach | et al. | (2018a) FSTD | model | is publicly | developed | and |
| --------- | ------ | ------------ | ----- | ----------- | --------- | --- |
availableathttps://github.com/lettie-roach/(lastaccess:1Novem-
ber2019).
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

C.Horvatetal.:Floesfromaltimetry 2881
AppendixA: ProofthattheFCDandFSDhavethe AppendixB: Boundsontherelationshipbetweenchord
samestatisticalproperties lengthandfloesizemoments
For generic probability distributions S(D) and P(r), and a Therealaltimetricdataproducthasafinitesamplingresolu-
probability function Fe(D;r), via Eq. (4) we have the rela- tion D
min
, which can bias the computed FSD moments and
tionship power-law decay profile. For example, applied to real data
with a finite sampling resolution, the integrals in Eqs. (4)
∞ r
Z Z to (5) are taken beginning at the minimum observed chord
(cid:104)Dn(cid:105)= drP(r) DnFe(D;r)dD, (A1) lengths D and floe sizes r =D /2. Moments of the
min min min
0 0 distributions S and P reflect only statistics for floes larger
than D and r , respectively. All other aspects of this
where we restrict the upper bounds on the second integral min min
becauseFe(D;r)iszeroforD>r.Underthescale-invariant
derivation remain the same, as Fe(D;r) is zero for any r <
D/2.However,therelationshipexpressedinEq.(4)becomes
sampling assumption Fe(D;r)dD=G(ξ)dξ, where ξ = D
2r
forD<2r (ξ <1).Therefore, ∞ π
Z 2n+1 Z2
∞ 1 (cid:104)Dn(cid:105)= drP(r) rn sin(x)ndx, (B1)
Z Z π
(cid:104)Dn(cid:105)= drP(r) rnξnG(ξ)dξ, (A2) rmin Y(r)
 ∞ 
0 0 R drP(r)2n+1 rnS (Y(r))
= Z ∞ drP(r)rn Z 1 ξnG(ξ)dξ, (A3) =A n (cid:104)rn(cid:105)    1− rmin A π (cid:104)rn(cid:105) n    , (B2)
 n 
0 0
=A n ·(cid:104)rn(cid:105), (A4) ≡A n (cid:104)rn(cid:105)[1−E(P(r);n)], (B3)
whereA n isthenthmomentofG(ξ),aconstantthatdepends where Y(r)≡sin−1(Dmin), S (y)=Ry sinn(x)dx, and E is
onthefunctionalformofG.Foranysuchprobabilityfunc- 2r n 0
the error in relating the nth moments of S(D) and P(r).
tion(forexamplethatderivedinSect.2forcircularfloes),the
SinceP(r)isunknown,E cannotbecomputedapriori.The
moments of the FSD and the moments of the FCD are pro-
functionS (Y(r))expressesthepercentageofchordsformed
n
portional.Mostofthehypotheticalstatisticaldistributionswe
fromfloesofsizerthatwouldbesmallerthanD ,although
min
wouldconsider(forexample,powerlaws)canbefullydeter-
itisnotreadilyexpressedasafunctionofn.Themostpatho-
mined in terms of their moments, and thus the relationship
logical distribution is when P(r) is a delta function at r ,
min
betweenmomentsoftheFSDandFCDistypicallysufficient
P(r)=δ(r−r ), Y(r )=π/2, and E=1 as no chord
min min
toreconstructtheunderlyingFSD.
lengthswouldbemeasured.
Supposing P(r) were a power-law function, converting
Wecancomputetheerrorfunctionforanydeltafunction
Eq.()toanintegraloverξ from0to1,wehave
distributionas
S(D)= Z ∞ Fe(D;r)P(r)dr = Z 1 P(D/2ξ)G(ξ) dξ. (A5) E(δ(r−r ∗ );n)= S n S (Y ( ( π r∗ ) )) , (B4)
ξ n 2
0 0
andthemisfitistheproportionoftheintegralofsinn(x)be-
Forapower-lawfunction,P(D/(2ξ))∝
(cid:16)
D
(cid:17)−α
and
tween0andY(r∗).Becausesin(x)ismonotonicallyincreas-
ξ ingfromx=0toπ/2,theintegralofS isboundedabove:
n
Z 1 (cid:18) D (cid:19)n
S(D)∝·D −α ξα−1G(ξ)dξ =A α−1 D −α. (A6) S n (Y(r ∗ ))≤Y(r ∗ )sinn(Y(r ∗ ))=Y(r ∗ ) 2 m r∗ in , (B5)
0
andthemisfiterrorisboundedaboveby
From Eqs. (A4) and (A6), and under the assumptions of
Sect. 2, all moments of the FSD and FCD are related by (cid:18) D (cid:19)n Y(r∗)
E(δ(r−r ∗;n))≤ min . (B6)
a computable function of the moment only, and power-law 2r∗ B(n+1,1)
2 2
FSDsarederivedfrompower-lawFCDswiththesamescal-
inglaw.WhiletheproportionalityofmomentsandEq.(A6) ThereciprocalofBisequaltoπ atn=0anddecreasessub-
prove that an observed power-law FCD must reflect an un- linearly,andsoawayfromr theerrortermdecaysexpo-
min
derlyingpower-lawFSD,thesameanalysisusedtoarriveat nentiallywithnandissmallevenfornearlypathologicaldis-
Eq. (A6) can be repeated to find P(r) given a power-law- tributions (for n=1, r∗=D , for example, E≤π/24≈
min
distributedS(D)aswell. 14%.Knowingthedistributionoferrorsbehavesinthisway
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

2882 C.Horvatetal.:Floesfromaltimetry
allowsustoestablishupperboundsbyintegratingP asasum tivewithrespecttoαandsettozero,
ofδfunctions.
Wenotethatincreasingresolutionoffloechordswillresult 1 +ln(D ∗ )= 1 X N ln D i , (C4)
in tighter bounds on this error. When Y(r)∗≤1, which oc- α−1 N D∗
i=1
curswhenr∗≥ Dmin ≈0.59D ,wecanexploitatighter
boundusingthef 2 a s c in t (1 th ) atsinn(x) m ≤ in xn, whichresolvesasasolutionforthemostlikelyα:
N
Y(r∗)n+1 (cid:18) D (cid:19)n αˆ =1+ . (C5)
S n (Y(r ∗ ))≤ n+1 ≤Y(r ∗ ) 2 m r∗ in . (B7) P N ln D D ∗ i
i=1
Usingthesameexampleasabove(n=1,r∗=D )bounds
min The above analysis concerns the most likely α that ex-
the error E≤π2/144≈7%. A real-world distribution of
plainstheFCD.Wemayaskaseparatequestion:whatisthe
floe sizes must have a peak value above zero; thus by in-
mostlikelyα,whichwedefineasα ,thatwouldexplainthe
P
creasing the sampling resolution (say, for example, to near
FSD, given the explicit relationship that can be derived be-
the size of pancakes, i.e., D ≈20m or less, approached
min tween S(D) and a power-law-distributed P(r) examined in
bytheICESat-2altimeter),thisboundtakesoveranderrors
Eq.(10).
arereducedsubstantially.
We can explicitly solve Eq. (B3) for distributions S(D)=C·B (cid:18) 1 , α (cid:19) 2α−1 D −α, (C6)
with power-law tails. These distributions are peaked at 2 2 π
the minimum floe size, and so will have high mo-
whereC isunknown.Repeatingtheaboveanalysis,
ment error. For power laws with α=−1, −2, −3, or
−4, E(P(r;α,r min ),1) is 1, 4, 16, or 25%. For n=2, Y N
E(P(r;α,r min ),2) is .003, .04, 2, or 9.6%: the increase L≡ln S(D i )=
in error with decreasing α is because sharper power-law i=1
s e l s o t p s e c s al c e o . ncentratemostofthedistributiontowardsthesmall- ln  CNB (cid:18) 1 , α P (cid:19)N 2(αP −1) !N Y N D −αP   (C7)
2 2 π i
i=1
AppendixC: Maximumlikelihoodestimationforchord
(cid:18) (cid:19)
1 α
lengthdistributions =NlnC+NlnB , P +N(α −1)ln2
P
2 2
Givenasetoffloechords{D} andanestimateofthebegin-
i N
ningofapower-lawtailD∗,wewouldliketofindthemost −Nlnπ−α X lnD . (C8)
P i
likelypower-lawfloesizedistributionP(r;α,r min )thatgen- i
erated them. As discussed in Appendix A, moments of the
Next we take the derivative of L with respect to α and
P
FSDandFCDarerelatedbyamultiplicativefactor,andthe
setting to zero. We use the fact that B(x,y)=B(y,x)
distributionsthemselveswillsharethesamepower-lawexpo- and ∂B(x,y) =B(x,y)(ψ(x)−ψ(x+y)), where ψ is the
nent.Thuswemaytestthepower-lawhypothesisdirectlyon ∂x
digammafunction,tofind
theFCDS(D).Thepower-lawhypothesismeansthatS(D)
isoftheform ∂lnB (cid:18) 1 , α P (cid:19) α = 1 (cid:18) ψ (cid:16)α P (cid:17) −ψ (cid:18) α P +1 (cid:19)(cid:19) . (C9)
P
2 2 2 2 2
(α−1) (cid:18) D (cid:19)−α
S(D)= D∗ D∗ . (C1) Themaximumlikelihoodα P isthesolutiontothetranscen-
dentalequation,
Following Muniruzzaman (1957) and Clauset et al. (2009)
(see also the derivation in Stern et al., 2018a), we compute 1 (cid:20) ψ (cid:16)α P (cid:17) −ψ (cid:18) α P +1 (cid:19)(cid:21) +ln2= 1 X N lnD , (C10)
i
thelog-likelihoodoftheobservationsforagivenα(Eq.10), 2 2 2 N
i=1
L≡ln Y N S(D )=ln "(cid:18) α−1 (cid:19)N Y N (cid:18) D i (cid:19)−α # , (C2) whichisanalternativemethodforobtainingtheFSDscaling.
i D∗ D∗
i=1 i=1
AppendixD: AveragingandsegmentingFSDstatistics
N
=Nln(α−1)+N(α−1)lnD ∗−α X lnD . (C3)
i
Due to limitations in the number of floe chords recorded at
i
any particular location over time, we do not include all ge-
As the natural log is monotonically increasing in its argu- ographiclocationswhencomputinghemisphericmeans.Av-
ment,tofindthemostlikelyα,denotedαˆ,wetakethederiva- eraging is performed by including only geographic regions
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

C.Horvatetal.:Floesfromaltimetry 2883
wherethereareatleast25recordedfloechords.Theareabe- Financialsupport. This research has been supported by the Na-
ingaveragedoveristhusnotfixedintime.Forseasonalcycle tionalOceanicandAtmosphericAdministration,ClimateProgram
plots,weonlyincludemonthswhichhaveenoughmeasure- Office(grantno.NA16NWS4620043),theNationalScienceFoun-
ments for all fully sampled CryoSat-2 years (2011–2018). dation, Division of Mathematical Sciences (grant nos. 1321794,
1641020, 1350795, and 1643431), the Office of Naval Research
For annual averages, we include only those years where all
(grantno.N00014-17-1-2963),theMarsdenFund(grantno.VUW-
CryoSat-2months(excludingJune–September)haveenough
1408),andtheNewZealandDeepSouthNationalChallenge(grant
measurements.
no.C01X1445).
When masking additional regions to perform the model–
observationcomparisonsinFig.6,wenotethatbecausethe
Roach et al. (2018a) model does not include processes that
Reviewstatement. ThispaperwaseditedbyJenniferHutchingsand
fragment larger floes into smaller floes in the absence of
reviewedbyThomasArmitageandoneanonymousreferee.
ocean surface waves, regions in the interior Arctic without
wave activity have nearly all sea ice area belonging to the
highest floe size categories. Nearly all regions where wave
fractureisanactiveprocessalsohaverepresentativeradiibe-
References
lowabout10km(Roachetal.,2019).Wedefineregionsthat
donotexperiencewavefractureasthosewithanabnormally
Alberello, A., Onorato, M., Bennetts, L., Vichi, M., Eayrs, C.,
highsimulatedrepresentativeradius,whichwechoosetobe
MacHutchon, K., and Toffoli, A.: Brief communication: Pan-
the22ndfloesizecategory(r =18.6km)orabove.Themask
cake ice floe size distribution during the winter expansion of
andcomparisonsinFig.6aremadebyexcludingallsuchar- the Antarctic marginal ice zone, The Cryosphere, 13, 41–48,
eas. https://doi.org/10.5194/tc-13-41-2019,2019.
Allard, R. A., Farrell, S. L., Hebert, D. A., Johnston, W. F.,
Li, L., Kurtz, N. T., Phelps, M. W., Posey, P. G., Till-
Supplement. Thesupplementrelatedtothisarticleisavailableon- ing, R., Ridout, A., and Wallcraft, A. J.: Utilizing CryoSat-
lineat:https://doi.org/10.5194/tc-13-2869-2019-supplement. 2 sea ice thickness to initialize a coupled ice-ocean mod-
eling system, J. Geophys. Res.-Oceans, 62, 1265–1280,
https://doi.org/10.1016/j.asr.2017.12.030,2018.
Authorcontributions. CH derived the mathematical theory and Armitage, T. W. K. and Davidson, M. W. J.: Using the
wrotethepaper.LRbuiltandperformedtheclimatemodelsimula- Interferometric Capabilities of the ESA CryoSat-2 Mis-
tion.RT,AR,andASprovidedandinterpretedtheCryoSat-2data. sion to Improve the Accuracy of Sea Ice Freeboard Re-
KH,CG,CB,andBKcontributedtothestudydesign.Allauthors trievals, IEEE Trans. Geosci. Remote Sens., 52, 529–536,
haveparticipatedinpaperpreparation. https://doi.org/10.1109/TGRS.2013.2242082,2014.
Armitage, T. W. K., Bacon, S., and Kwok, R.: Arctic Sea
Level and Surface Circulation Response to the Arc-
tic Oscillation, Geophys. Res. Lett., 45, 6576–6584,
Competinginterests. Theauthorsdeclarenocompetinginterests.
https://doi.org/10.1029/2018GL078386,2018.
Batchelor, G. K.: The theory of homogeneous turbulence, Cam-
bridgeUniversityPress,1953.
Acknowledgements. CHwassupportedbytheNOAAClimateand
Bateson,A.W.,Feltham,D.L.,Schröder,D.,Hosekova,L.,Ridley,
GlobalChangePostdoctoralFellowshipProgram,administeredby
J. K., and Aksenov, Y.: Impact of floe size distribution on sea-
UCAR’sCooperativeProgramsfortheAdvancementofEarthSys-
sonalfragmentationandmeltofArcticseaice,TheCryosphere
tem Science (CPAESS), sponsored in part through cooperative
Discuss.,https://doi.org/10.5194/tc-2019-44,inreview,2019.
agreementnumberNA16NWS4620043,years2017–2021,withthe
Birnbaum, G. and Lüpkes, C.: A new parameterization of sur-
National Oceanic and Atmospheric Administration (NOAA) and
face drag in the marginal sea ice zone, Tellus A, 54, 107–123,
theU.S.DepartmentofCommerce(DOC).CH,CG,andKHthank
https://doi.org/10.1034/j.1600-0870.2002.00243.x,2002.
the American Mathematical Society for their support through the
Clauset,A.,Young,M.,andGleditsch,K.S.:OntheFrequencyof
MathematicsResearchCommunity“DifferentialEquations,Proba-
SevereTerroristEvents,J.Conf.Resolut.,51,58–87,2007.
bility,andSeaIce”,fundedbyNSFgrants1321794and1641020.
Clauset, A., Shalizi, C. R., Newman, M. E. J., Rohilla
LR was funded via Marsden contract VUW-1408 and the New
Shalizi, C., and J Newman, M. E.: Power-Law Dis-
Zealand Deep South National Science Challenge, MBIE contract
tributions in Empirical Data, SIAM Rev., 51, 661–703,
number C01X1445. CMB was supported by the National Science
https://doi.org/10.1137/070710111,2009.
FoundationgrantPLR-1643431.BFKwassupportedbyONRgrant
Day, J. J., Hawkins, E., and Tietsche, S.: Will Arc-
N00014-17-1-2963andNSFgrant1350795.RT,AR,andASwere
tic sea ice thickness initialization improve seasonal
supportedbytheUKNERCCentreforPolarObservationandMod-
forecast skill?, Geophys. Res. Lett., 41, 7566–7575,
ellingandtheEuropeanSpaceAgency.
https://doi.org/10.1002/2014GL061694,2014.
Feltham,D.L.:SeaIceRheology,Ann.Rev.FluidMechan.,40,91–
112, https://doi.org/10.1146/annurev.fluid.40.111406.102151,
2008.
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019

2884 C.Horvatetal.:Floesfromaltimetry
Gherardi, M. and Lagomarsino, M. C.: Characterizing the J., Haas, C., Hendricks, S., Krishfield, R., Kurtz, N., Far-
size and shape of sea ice floes, Sci. Rep., 5, 10226, rell, S., and Davidson, M.: CryoSat-2 estimates of Arctic sea
https://doi.org/10.1038/srep10226,2015. ice thickness and volume, Geophys. Res. Lett., 40, 732–737,
Guerreiro, K., Fleury, S., Zakharova, E., Kouraev, A., Rémy, https://doi.org/10.1002/grl.50193,2013.
F., and Maisongrande, P.: Comparison of CryoSat-2 and EN- Lindsay,R.W.andRothrock,D.A.:Arcticseaiceleadsfromad-
VISATradarfreeboardoverArcticseaice:towardanimproved vancedveryhighresolutionradiometerimages,J.Geophys.Res.,
Envisat freeboard retrieval, The Cryosphere, 11, 2059–2073, 100,4533,https://doi.org/10.1029/94JC02393,1995.
https://doi.org/10.5194/tc-11-2059-2017,2017. Lüpkes, C. and Birnbaum, G.: Surface drag in the Arctic
Herman, A.: Molecular-dynamics simulation of cluster- marginal sea-ice zone: A comparison of different param-
ing processes in sea-ice floes, Phys. Rev. E, 84, 1–11, eterisation concepts, Bound.-Lay. Meteorol., 117, 179–211,
https://doi.org/10.1103/PhysRevE.84.056104,2011. https://doi.org/10.1007/s10546-005-1445-8,2005.
Herman,A.,Evers,K.-U.,andReimer,N.:Floe-sizedistributionsin Mandelbrot,B.B.andWheeler,J.A.:TheFractalGeometryofNa-
laboratoryicebrokenbywaves,TheCryosphere,12,685–699, ture, Vol. 51, W. H. Freeman, https://doi.org/10.1119/1.13295,
https://doi.org/10.5194/tc-12-685-2018,2018 1983.
Horvat, C. and Tziperman, E.: A prognostic model of the sea-ice Manucharyan, G. E. and Thompson, A. F.: Subme-
floe size and thickness distribution, The Cryosphere, 9, 2119– soscale Sea Ice-Ocean Interactions in Marginal Ice
2134,https://doi.org/10.5194/tc-9-2119-2015,2015. Zones, J. Geophys. Res.-Oceans, 122, 9455–9475,
Horvat, C. and Tziperman, E.: The evolution of scaling laws in https://doi.org/10.1002/2017JC012895,2017.
theseaicefloesizedistribution,J.Geophys.Res.-Oceans,122, Muniruzzaman, A. N. M.: On Measures of Location
7630–7650,https://doi.org/10.1002/2016JC012573,2017. and Dispersion and Tests of Hypotheses in a Pareto
Horvat,C.andTziperman,E.:UnderstandingMeltingduetoOcean Population, Calc. Stat. Assoc. Bull., 7, 115–123,
EddyHeatFluxesattheEdgeofSea-IceFloes,Geophys.Res. https://doi.org/10.1177/0008068319570303,1957.
Lett., 45, 9721–9730, https://doi.org/10.1029/2018GL079363, Nere, N. K., Ramkrishna, D., Parker, B. E., Bell, W. V., and
2018. Mohan, P.: Transformation of the Chord-Length Distributions
Horvat,C.,Tziperman,E.,andCampin,J.-M.:Interactionofseaice to Size Distributions for Nonspherical Particles with Ori-
floesize,oceaneddies,andseaicemelting,Geophys.Res.Lett., entation Bias †, Indust. Eng. Chem. Res., 46, 3041–3047,
43,8083–8090,https://doi.org/10.1002/2016GL069742,2016. https://doi.org/10.1021/ie0609463,2007.
Hunke, E. C., Lipscomb, W. H., Turner, A. K., Jeffery, N., and Peacock, N. R. and Laxon, S. W.: Sea surface height determina-
Elliott,S.:CICE:theLosAlamosSeaIceModelDocumenta- tionintheArcticOceanfromERSaltimetry,J.Geophys.Res.-
tion and Software User’s Manual Version 5.1 LA-CC-06-012, Oceans, 109, C07001, https://doi.org/10.1029/2001JC001026,
Tech. rep., Los Alamos National Laboratory, available at: http: 2004.
//oceans11.lanl.gov/trac/CICE (last access: 1 November 2019), Perovich,D.K.andJones,K.F.:Theseasonalevolutionofseaice
2015. floesizedistribution,J.Geophys.Res.-Oceans,119,8767–8777,
Hwang,B.,Wilkinson,J.,Maksym,E.,Graber,H.C.,Schweiger, https://doi.org/10.1002/2014JC010136,2014.
A., Horvat, C., Perovich, D. K., Arntsen, A. E., Stanton, T. P., Pons, M.-N., Milferstedt, K., and Morgenroth, E.: Modeling of
Ren,J.,Wadhams,P.,Maksym,T.,Graber,H.C.,Schweiger,A., chord length distributions, Chem. Eng. Sci., 61, 3962–3973,
Horvat,C.,Perovich,D.K.,Arntsen,A.E.,Timothy,P.,Ren,J., https://doi.org/10.1016/j.ces.2006.01.036,2006.
andWadhams,P.:Winter-to-summertransitionofArcticseaice Quartly,G.D.,Rinne,E.,Passaro,M.,Andersen,O.B.,Dinardo,
breakupandfloesizedistributionintheBeaufortSea,Elementa: S.,Fleury,S.,Guillot,A.,Hendricks,S.,Kurekin,A.A.,Müller,
Sci.Anthrop.,5,40,https://doi.org/10.1525/elementa.232,2017. F. L., Ricker, R., Skourup, H., and Tsamados, M.: Retrieving
JRA-55:JRA-55:Japanese55-yearReanalysis,Daily3-Hourlyand Sea Level and Freeboard in the Arctic: A Review of Current
6-HourlyData,ResearchDataArchiveattheNationalCenterfor Radar Altimetry Methodologies and Future Perspectives, Re-
AtmosphericResearch,ComputationalandInformationSystems moteSens.,11,881,https://doi.org/10.3390/rs11070881,2019.
Laboratory,2013. Richter-Menge, J. A.: Relating arctic pack ice stress and defor-
Key,J.:Estimatingtheareafractionofgeophysicalfieldsfrommea- mation under winter conditions, J. Geophys. Res., 107, 8040,
surements along a transect, IEEE Tran. Geosci. Remote Sens., https://doi.org/10.1029/2000JC000477,2002.
31,1099–1102,https://doi.org/10.1109/36.263782,1993. Roach, L. A., Horvat, C., Dean, S. M., and Bitz, C. M.: An
Key,J.andPeckham,S.:Probableerrorsinwidthdistributionsof emergent sea ice floe size distribution in a global coupled
sea ice leads measured along a transect, J. Geophys. Res., 96, ocean–seaicemodel,J.Geophys.Res.-Oceans,123,4322–4337,
18417,https://doi.org/10.1029/91JC01843,1991. https://doi.org/10.1029/2017JC013692,2018a.
Kwok, R.: Arctic sea ice thickness, volume, and multiyear ice Roach, L. A., Smith, M. M., and Dean, S. M.: Quantify-
coverage: losses and coupled variability (1958–2018), En- ing growth of pancake sea ice floes using images from
viron. Res. Lett., 13, 105005, https://doi.org/10.1088/1748- drifting buoys, J. Geophys. Res.-Oceans, 123, 2851–2866,
9326/aae3ec,2018. https://doi.org/10.1002/2017JC013693,2018b.
Laxon,S.,Peacock,N.,andSmith,D.:Highinterannualvariability Roach, L., Bitz, C., Horvat, C., and Dean, S.: Advances in mod-
ofseaicethicknessintheArcticregion,Nature,425,947–950, elling interactions between sea ice and ocean surface waves,
https://doi.org/10.1038/nature02050,2003. Journal of Advances in Modeling Earth Systems, 1–14, in re-
Laxon, S. W., Giles, K. A., Ridout, A. L., Wingham, D. J., view,2019.
Willatt, R., Cullen, R., Kwok, R., Schweiger, A., Zhang,
TheCryosphere,13,2869–2885,2019 www.the-cryosphere.net/13/2869/2019/

C.Horvatetal.:Floesfromaltimetry 2885
Roberts,A.F.,Hunke,E.C.,Kamal,S.M.,Lipscomb,W.H.,Hor- Tilling, R., Ridout, A., and Shepherd, A.: Assessing the impact
vat, C., and Maslowski, W.: A Variational Method for Sea Ice ofleadandfloesamplingonArcticseaicethicknessestimates
RidginginEarthSystemModels,J.Adv.Model.EarthSyst.,p. from Envisat and CryoSat-2, J. Geophys. Res.-Oceans, 124,
2018MS001395,https://doi.org/10.1029/2018MS001395,2019. https://doi.org/10.1029/2019JC015232,2019a.
Rothrock, D. A. and Thorndike, A. S.: Measuring the Sea Tilling, R., Ridout, A., and Shepherd, A.: Assessing the impact
Ice Floe Size Distribution, J. Geophys. Res., 89, 6477–6486, ofleadandfloesamplingonArcticseaicethicknessestimates
https://doi.org/10.1029/JC089iC04p06477,1984. from Envisat and CryoSat-2, J. Geophys. Res.-Oceans, 124,
Rynders, S., Aksenov, Y., Feltham, D., Nurser, G., and Naveira https://doi.org/10.1029/2019JC015232,2019b.
Garabato, A.: Modelling MIZ dynamics in a global model, in: Tolman, H. L. H. L.: User manual and system documentation of
EGUGeneralAssemblyConferenceAbstracts,p.1004,2016. WAVEWATCH III TM version 3.14, Technical Note 276, 276,
SandbergSorensen,L.,Simonsen,S.,Langley,K.,Gray,L.,Helm, 194, available at: ftp://ftp.ifremer.fr/ifremer/cersat/products/
V., Nilsson, J., Stenseng, L., Skourup, H., Forsberg, R., and gridded/wavewatch3/HINDCAST/publications/Tolman_
Davidson,M.:ValidationofCryoSat-2SARInDataoverAust- etal_MMAB276_2009.pdf\%0Apapers3://publication/uuid/
fonnaIceCapUsingAirborneLaserScannerMeasurements,Re- E1C39B58-DBCB-4F8A-ADCD-F2D2210DDC46(lastaccess:
moteSens.,10,1354,https://doi.org/10.3390/rs10091354,2018. 1November2019),2009.
Schröder, D., Feltham, D. L., Tsamados, M., Ridout, A., and Toyota,T.,Takatsuji,S.,andNakayama,M.:Characteristicsofsea
Tilling, R.: New insight from CryoSat-2 sea ice thick- icefloesizedistributionintheseasonalicezone,Geophys.Res.
ness for sea ice modelling, The Cryosphere, 13, 125–139, Lett.,33,L02616,https://doi.org/10.1029/2005GL024556,2006.
https://doi.org/10.5194/tc-13-125-2019,2019. Toyota, T., Haas, C., and Tamura, T.: Size distribution and shape
Schulson, E. M. and Hibler, W. D.: The fracture of ice on scales properties of relatively small sea-ice floes in the Antarctic
large and small: Arctic leads and wing cracks, J. Glaciol., 37, marginalicezoneinlatewinter,Deep-SeaRes.PartII,58,1182–
319–322,https://doi.org/10.1017/S0022143000005748,1991. 1193,https://doi.org/10.1016/j.dsr2.2010.10.034,2011.
Skourup, H., Simonsen, S. B., Sorensen, L., Bella, A., Forsberg, Toyota,T.,Kohout,A.,andFraser,A.D.:Formationprocessesof
R.,Hvidegaard,S.,andHelm,V.:ESACryoVEx/EUICE-ARC seaicefloesizedistributionintheinteriorpackanditsrelation-
2016-AirborneFieldCampaignwithASIRASRadarandLaser shiptothemarginalicezoneoffEastAntarctica,DeepSeaRes.
ScanneroverAustfonna,FramStraitandtheWandelSea,Tech. Pt II, 131, 28–40, https://doi.org/10.1016/j.dsr2.2015.10.003,
rep.,NationalSpaceInstitute,TechnicalUniversityofDenmark, 2016.
2017. Tsamados, M., Feltham, D. L., Schroeder, D., Flocco, D., Far-
Smith,M.andThomson,J.:Scalingobservationsofsurfacewaves rell, S. L., Kurtz, N., Laxon, S. W., and Bacon, S.: Impact
in the Beaufort Sea, Elementa: Science of the Anthropocene, of Variable Atmospheric and Oceanic Form Drag on Simula-
4, 000097, https://doi.org/10.12952/journal.elementa.000097, tions of Arctic Sea Ice*, J. Phys. Oceanogr., 44, 1329–1353,
2016. https://doi.org/10.1175/JPO-D-13-0215.1,2014.
Squire, V. A.: Of ocean waves and sea-ice re- Virkar, Y. and Clauset, A.: Power-law distributions in
visited, Cold Reg. Sci. Technol., 49, 110–133, binned empirical data, The Ann. Appl. Stat., 8, 89–119,
https://doi.org/10.1016/j.coldregions.2007.04.007,2007. https://doi.org/10.1214/13-AOAS710,2014.
Squire, V. A., Dugan, J. P., Wadhams, P., Rot- Wadhams, P., Squire, V. a., Goodman, D. J., Cowan, A. M.,
tier, P. J., and Liu, A. K.: Of Ocean Waves and and Moore, S. C.: The attenuation rates of ocean waves
Sea Ice, Annu. Rev. Fluid Mechan., 27, 115–168, in the marginal ice zone, J. Geophys. Res., 93, 6799,
https://doi.org/10.1146/annurev.fl.27.010195.000555,1995. https://doi.org/10.1029/JC093iC06p06799,1988.
Steele, M.: Sea ice melting and floe geometry in a simple Wernecke, A. and Kaleschke, L.: Lead detection in Arctic
ice-ocean model, J. Geophys. Res.-Oceans, 97, 17729–17738, sea ice from CryoSat-2: quality assessment, lead area frac-
https://doi.org/10.1029/92JC01755,1992. tion and width distribution, The Cryosphere, 9, 1955–1968,
Steer, A., Worby, A., and Heil, P.: Observed changes in sea- https://doi.org/10.5194/tc-9-1955-2015,2015.
ice floe size distribution during early summer in the west- Wilchinsky, A. V. and Feltham, D. L.: Modelling the rhe-
ern Weddell Sea, Deep Sea Res. Part II, 55, 933–942, ology of sea ice as a collection of diamond-shaped
https://doi.org/10.1016/j.dsr2.2007.12.016,2008. floes, J. Non-Newton. Fluid Mechan., 138, 22–32,
Stern,H.L.,Schweiger,A.J.,Stark,M.,Zhang,J.,Steele,M.,and https://doi.org/10.1016/j.jnnfm.2006.05.001,2006.
Hwang,B.:Seasonalevolutionofthesea-icefloesizedistribu- Wilchinsky,A.V.andFeltham,D.L.:ModelingCoulombicfailure
tionintheBeaufortandChukchiseas,Elem.Sci.Anth.,6,48, of sea ice with leads, J. Geophys. Res.-Oceans, 116, C08040,
https://doi.org/10.1525/elementa.304,2018a. https://doi.org/10.1029/2011JC007071,2011.
Stern,H.L.,Schweiger,A.J.,Zhang,J.,andSteele,M.:Onrecon- Williams, T. D., Bennetts, L. G., Squire, V. A., Dumont, D., and
cilingdisparatestudiesofthesea-icefloesizedistribution,Elem. Bertino, L.: Wave-ice interactions in the marginal ice zone.
Sci.Anth.,6,49,https://doi.org/10.1525/elementa.304,2018b. Part 1: Theoretical foundations, Ocean Modell., 71, 81–91,
Tilling,R.,Ridout,A.,andShepherd,A.:Near-real-timeArcticsea https://doi.org/10.1016/j.ocemod.2013.05.010,2013.
icethicknessandvolumefromCryoSat-2,TheCryosphere,10, Zhang, J., Schweiger, A., Steele, M., and Stern, H.: Sea ice floe
2003–2012,https://doi.org/10.5194/tc-10-2003-2016,2016. size distribution in the marginal ice zone: Theory and numer-
Tilling,R.,Ridout,A.,andShepherd,A.:EstimatingArcticseaice ical experiments, J. Geophys. Res.-Oceans, 120, 3484–3498,
thicknessandvolumeusingCryoSat-2radaraltimeterdata,Adv. https://doi.org/10.1002/2015JC010770,2015.
SpaceRes.,https://doi.org/10.1016/j.asr.2017.10.051,2018.
www.the-cryosphere.net/13/2869/2019/ TheCryosphere,13,2869–2885,2019
