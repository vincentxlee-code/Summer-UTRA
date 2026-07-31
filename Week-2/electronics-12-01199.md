electronics
Review
Techniques and Challenges of Image Segmentation: A Review
YingYu1,2,ChunpingWang1,QiangFu1,*,RenkeKou1,FuyuHuang1,BoxiongYang2 ,TingtingYang2
andMingliangGao3
1 DepartmentofElectronicandOpticalEngineering,ArmyEngineeringUniversityofPLA,
Shijiazhuang050003,China
2 SchoolofInformationandIntelligentEngineering,UniversityofSanya,Sanya572022,China
3 SchoolofElectricalandElectronicEngineering,ShandongUniversityofTechnology,Zibo255000,China
* Correspondence:fu_qiang@aeu.edu.cn
Abstract:Imagesegmentation,whichhasbecomearesearchhotspotinthefieldofimageprocessing
andcomputervision,referstotheprocessofdividinganimageintomeaningfulandnon-overlapping
regions,anditisanessentialstepinnaturalsceneunderstanding. Despitedecadesofeffortand
manyachievements,therearestillchallengesinfeatureextractionandmodeldesign.Inthispaper,
we review the advancement in image segmentation methods systematically. According to the
segmentationprinciplesandimagedatacharacteristics,threeimportantstagesofimagesegmentation
are mainly reviewed, which are classic segmentation, collaborative segmentation, and semantic
segmentationbasedondeeplearning.Weelaborateonthemainalgorithmsandkeytechniquesin
eachstage,compare,andsummarizetheadvantagesanddefectsofdifferentsegmentationmodels,
anddiscusstheirapplicability.Finally,weanalyzethemainchallengesanddevelopmenttrendsof
imagesegmentationtechniques.
Keywords: image segmentation; co-segmentation; semantic segmentation; deep learning;
imageprocessing
1. Introduction
Imagesegmentationisoneofthemostpopularresearchfieldsincomputervision,
Citation:Yu,Y.;Wang,C.;Fu,Q.;
andformsthebasisofpatternrecognitionandimageunderstanding. Thedevelopment
Kou,R.;Huang,F.;Yang,B.;Yang,T.;
ofimagesegmentationtechniquesiscloselyrelatedtomanydisciplinesandfields,e.g.,
Gao,M.TechniquesandChallenges
autonomousvehicles[1], intelligentmedicaltechnology[2,3], imagesearchengines[4],
ofImageSegmentation:AReview.
industrialinspection,andaugmentedreality.
Electronics2023,12,1199. https://
Imagesegmentationdividesimagesintoregionswithdifferentfeaturesandextracts
doi.org/10.3390/electronics12051199
theregionsofinterest(ROIs). Theseregions,accordingtohumanvisualperception,are
AcademicEditor:HyunjinPark meaningfulandnon-overlapping.Therearetwodifficultiesinimagesegmentation:(1)how
todefine“meaningfulregions”,astheuncertaintyofvisualperceptionandthediversity
Received:7February2023
ofhumancomprehensionleadtoalackofacleardefinitionoftheobjects,itmakesimage
Revised:27February2023
Accepted:27February2023 segmentationanill-posedproblem;and(2)howtoeffectivelyrepresenttheobjectsinan
Published:2March2023 image. Digitalimagesaremadeupofpixels, thatcanbegroupedtogethertomakeup
largersetsbasedontheircolor,texture,andotherinformation. Thesearereferredtoas
“pixel sets” or “superpixels”. These low-level features reflect the local attributes of the
image, butitisdifficulttoobtainglobalinformation(e.g., shapeandposition)through
Copyright: © 2023 by the authors.
theselocalattributes.
Licensee MDPI, Basel, Switzerland.
Sincethe1970s,imagesegmentationhasreceivedcontinuousattentionfromcomputer
This article is an open access article
visionresearchers. Theclassicsegmentationmethodsmainlyfocusonhighlightingand
distributed under the terms and
obtaining the information contained in a single image, that often requires professional
conditionsoftheCreativeCommons
knowledgeandhumanintervention. However,itisdifficulttoobtainhigh-levelsemantic
Attribution(CCBY)license(https://
informationfromimages. Co-segmentationmethodsinvolveidentifyingcommonobjects
creativecommons.org/licenses/by/
fromasetofimages,thatrequirestheacquisitionofcertainpriorknowledge. Sincethe
4.0/).
Electronics2023,12,1199.https://doi.org/10.3390/electronics12051199 https://www.mdpi.com/journal/electronics

Electronics 2023, 12, x FOR PEER REVIEW 2 of 25
and obtaining the information contained in a single image, that often requires professional
knowledge and human intervention. However, it is difficult to obtain high-level semantic
information from images. Co-segmentation methods involve identifying common objects
Electronics2023,12,1199 from a set of images, that requires the acquisition of certain prior knowledge.2 Soifn24ce the
image annotation of these methods is dispensable, they are classed as semi-supervised or
weakly supervised methods. With the enrichment of large-scale fine-grained annotation
imageannotationofthesemethodsisdispensable,theyareclassedassemi-supervisedor
image datasets, image segmentation methods based on deep neural networks have grad-
weaklysupervisedmethods. Withtheenrichmentoflarge-scalefine-grainedannotationim-
ually become a popular topic.
agedatasets,imagesegmentationmethodsbasedondeepneuralnetworkshavegradually
Although many achievements have been made in image segmentation research, there
becomeapopulartopic.
are still many challenges, e.g., feature representation, model design, and optimization. In
Althoughmanyachievementshavebeenmadeinimagesegmentationresearch,there
particular, semantic segmentation is still full of challenges due to limited or sparse anno-
arestillmanychallenges,e.g.,featurerepresentation,modeldesign,andoptimization. In
tatipoanrsti,c cullaasr,ss iemmbanatliacnsceeg,m oevnetraftiitotninigs,s tliollnfgu ltlroafinchinalgle tnigmese,d aunedto glrimaditieednot rvsapnairssheianngn. oTtah-e au-
thotriso nosf, c[5la–s7s]i minbtarloadnucec,eodv esrefimttainngt,iclo sneggtmraeinnitnagtitoimn em,aentdhogdrasd aienndt vcaonmismhinogn.lyT huesaeudt hdoartsasets,
ando f[[85]– a7]nianltyrozdeduc tehdes eemvaalnutiactisoengm menettaritciosn amndet hmodetshaonddsc oomf smeomnalyntuisce sdedgamtaesnettsa,taionnd,[ 8b]ut re-
vieawnsa lhyazvede tnhoete yveatlu saotriotendm aentrdic ssuamndmmaeritzheodds imofasgeme saengtimcseengtmateinotna taiolgn,obruitthrmevsi efwrosmha tvhee per-
notyetsortedandsummarizedimagesegmentationalgorithmsfromtheperspectiveof
spective of how the technology in the field of image segmentation has evolved and devel-
howthetechnologyinthefieldofimagesegmentationhasevolvedanddevelopedtothe
oped to the present day. Therefore, it is necessary to systematically summarize the exist-
presentday. Therefore,itisnecessarytosystematicallysummarizetheexistingsegmenta-
ing segmentation methods, especially the state-of-the-art methods. We analyze and reclas-
tionmethods,especiallythestate-of-the-artmethods.Weanalyzeandreclassifytheexisting
sify the existing image segmentation methods from the perspective of algorithm develop-
imagesegmentationmethodsfromtheperspectiveofalgorithmdevelopment,elaborate
meonnt, tehleabwoorarktein ognm theech wanoirskminsgo fmtehcehseanmisemthso dosf tahnedsee nmuemtheroadtes asonmd eeninuflmueenratitael siommagee influ-
entsieagl mimenatgaeti osengamlgeonrittahtmiosn,a anldgoinrtirtohdmusc,e atnhede isnsternotdiaulcteec hthneiq eusesseonftisaelm taenchticnisqegumese notfa stieomnantic
segbmaseendtaotniodne ebpanseedur oanln deetwepor nkesusyrastle nmeattwicoarllky,s assysshteomwnatiincaFlilgyu, raes1 s.hown in Figure 1.
FigFuirgeu 1re. T1.hTeh ceacteagteogroireise soof fimimaaggee sseeggmmeennttaatitoionnm metehtohdosd.s.
2. ClassicSegmentationMethods
2. Classic Segmentation Methods
The classic segmentation algorithms were proposed for grayscale images, which
The classic segmentation algorithms were proposed for grayscale images, which
mainlyconsidergray-levelsimilarityinthesameregionandgray-leveldiscontinuityin
mainly consider gray-level similarity in the same region and gray-level discontinuity in
differentregions. Ingeneral,regiondivisionisbasedongray-levelsimilarity,andedge
diffdeerteenctti ornegisiobnass.e dIno gnegnrearya-lle, vreelgdioisnc odnitvinisuiiotyn. Ciso bloarsiemda ogne sgergamye-lnetvaetilo nsiminviloalrvietys,u asnindg edge
dettehcetisoimn iilsa rbitaysebdet wone egnrapyix-elelsvteol sdeigsmcoennttinthueitiym. aCgoelionrt oimdiaffgeer esnetgrmegeinontastoiorns uinpevroplivxeesls u, sing
andthenmergingthesesuperpixels.

Electronics 2023, 12, x FOR PEER REVIEW 3 of 25
Electronics2023,12,1199 3of24
the similarity between pixels to segment the image into different regions or superpixels,
and then merging these superpixels.
2.1. EdgeDetec2ti.o1n. Edge Detection
The positionsTwhhe epreostihtieongsra wyhleevree lthche agnrgaeys lsehvaerl pclhyainngaesn sihmaargpelya irne ganen iemraalglye athree generally the
boundariesofbdoifufenrdenatrireesg oiof ndsi.ffTerheentta rsekgoiofnesd.g Tehdee ttaesckti oofn eidsgtoe dideetenctitfiyonth ise tpoo iidnetsntoinfyt thhees epoints on these
boundaries. Edboguenddeatercietiso. nEdisgoen deeotefctthioene aisr loienset osef gthmee enatarltiieosnt smegetmhoendtsaatinodn imsaeltshoodcasl laendd is also called
theparallelbotuhne dpaarryaltleecl hbnoiuqnudea.rTyh teecdhenriiqvuaeti. vTehoe rddeirfifvearteinvtei aolro dfiftfheeregnrtaiyal loefv tehleis gurasyed level is used to
toidentifytheidoebnvtiiofuy sthceh aonbgveiosuast cthheanbgoeusn adta trhye. bInoupnradcatriyce. ,Inth perdacetriicvea, ttihvee doefrtihveatdivigei otafl the digital im-
imageisobtainagede bisy oubstianignetdhe bdyi fufesrinengc tehaep dpirfofexriemnactei oanpfporrotxhimedatififoenr efnotri atlh.eE xdaifmfeprelenstioafl. Examples of
edgedetectionerdegseu ldtsetaercetiroenp rreesseunlttse darien rFeipgruerseen2t.ed in Figure 2.
(a) (b) (c) (d)
(e) (f) (g) (h)
Figure2.EdgedFeigteucrteio 2n. rEedsguelt sdeotfedctiifofenr ernestudlitfsf eorfe dnitfifaelroepnet rdaitfofersr.en(at)iaOl oripgeinraatlo(rbs). S(ao)b OelrXig(icn)aSl o(bbe) lSYobelX (c) SobelY
(d)Sobel(e)Kir(sdch) S(of)bRelo (bee)r Ktsir(gsc)hC (afn) nRyobaenrdts( h(g))L Caapnlancyia ann.d (h) Laplacian.
TheseoperatorTshaersees oepnesritaitvoersto arneo siseenasintidvea rteo onnoliyses uaintdab alreef oornliym saugietsabwleit fholro iwmangoeisse with low noise
andcomplexitya.nTdh ceoCmapnlneyxiotyp.e Trahteo rCpaenrnfyor ompserbaetsotra pmeorfnogrmthse boepsetr aamtoorsnsgh tohwe nopinerFaitgourrse s2h.own in Figure
It has strong d2.e nIto hisaisn gstraobnilgit dy,eannodisianlgs oabpirloitcye, sasneds tahlseos pegromceenssteast itohne osfeglimneesntwateilolnw oift hlines well with
continuity,finecnoenstsin,aunitdy,s ftirnaeignhetsns,e assn.dH sotrwaiegvhetrn,ethsse. CHaonwneyvoepr,e trhaeto Craisnnmyo orepecroamtoprl eisx manodre complex and
takes longer totakexese clounteg.erI ntot hexeeaccuttuea. Ilni nthdeu astcrtiuaallp inrodduustcrtiiaoln p,raodthurcetsiohno,l da itnhgregsrhaodldieinntg igsradient is usu-
usuallyusedinaltlhye ucsaesde oinf hthigeh craesael -otifm heigrhe qrueairle-tmimenet .reOqnuitrheemceonntt.r aOrny, tthhee mcoonrteraardyv, atnhcee mdore advanced
CannyoperatoCrainsnseyl eocpteerdatinort hise scealesectoefdh iing thhqe ucaalsiety orfe hqiugihr eqmueanlitt.y requirement.
Although diffAerletnhtoiualgho pdeirfafetorernstciaaln olpoecraatetotrhs ecabno uloncdaatrei etsheo fbdouifnfedraernitesr eogfi odnifsfeerfefin-t regions effi-
ciently,thecloscuiernetalyn,d thcoen ctlionsuuirtye oanftdh ceobnotuinnudiatyri eosf ctahnen bootubnedgauraiersa ncatenendodt ubee tgounauramneteroeuds due to numer-
discontinuousopuos idnitsscoanntdinluinoeuss ipnotihnets haingdh -ldineetas iilnr tehgeio hnisg.h-Tdheetareilf orerge,iointsis. Tnheecreesfsoarrey, itto is necessary to
smooththeimsamgeoobtehfo trheeu imsinaggea bdeiffoferree unstiianlgo ap edriaffteorretnotidael toepctereadtgoer st.o detect edges.
AnotheredgeAdnetoetchteior nedmgeet hdoedtecistitohne mseertihaoldbo ius nthdea rsyertieaclh bnoiuqunde,atrhya tteccohnnciaqtueen, attheast concatenates
pointsofedgepsotiontfso romf eadgcleoss etod fboorumn da acrlyo.seSde rbiaolubnoduanrdy.a rSyertieacl hbnoiuqnudesarmy atienclhyniinqculeusd me ainly include
graph-searchinggraaplhg-osreiathrcmhisnagn adlgdoyrnitahmmics panrodg draymnamminicg parloggorraitmhmmsin.gIn aglgraoprihth-smeasr. cIhni nggraph-searching
algorithms,thepointsontheedgesarerepresentedbyagraphstructure,andthepathwith
algorithms, the points on the edges are represented by a graph structure, and the path
theminimumcostissearchedinthegraphtodeterminetheclosedboundaries,whichis
with the minimum cost is searched in the graph to determine the closed boundaries, which
alwayscomputationallyintensive. Thedynamicprogrammingalgorithmutilizesheuristic
is always computationally intensive. The dynamic programming algorithm utilizes heu-
rulestoreducethesearchcomputation.
ristic rules to reduce the search computation.
Theactivecontoursmethodapproximatestheactualcontoursoftheobjectsbymatch-
The active contours method approximates the actual contours of the objects by
ingtheclosedcurve(i.e., theinitialcontoursbasedongradient)withthelocalfeatures
matching the closed curve (i.e., the initial contours based on gradient) with the local fea-
of the image, and finds the closed curve with the minimum energy by minimizing the
tures of the image, and finds the closed curve with the minimum energy by minimizing
energyfunctiontoachieveimagesegmentation. Themethodissensitivetothelocation
the energy function to achieve image segmentation. The method is sensitive to the location
oftheinitialcontour,sotheinitializationmustbeclosetothetargetcontour. Moreover,
of the initial contour, so the initialization must be close to the target contour. Moreover,
its non-convexity easily leads to the local minimum, so it is difficult to converge to the
concaveboundary. LanktonandTannenbaum[9]proposedaframeworkthatconsidersthe
localsegmentationenergytoevolvecontours,thatcouldproducetheinitiallocalization

Electronics2023,12,1199 4of24
accordingtothelocallybasedglobalactivecontourenergyandeffectivelysegmentobjects
withheterogeneousfeatureprofiles.
Graphcutsmarksthetargetnodes(i.e., sourcenodes)andbackgroundnodes(i.e.,
sinknodes),andusesthevectorconnectionbetweendifferentnodestorepresentthefit
degreeofthenodesandthecorrespondingpixels(i.e.,thepenaltyfunction). Graphcutsis
anNP-hardproblem,soefficientapproximationalgorithmsmustbesoughttominimize
theenergyfunction,thatcanbeadoptedbyusingaswapalgorithmbasedonthesemi-
metricpropertiesofconnectionsandanexpansionalgorithmbasedonthemetricproperties
of nodes. Freedman [10] proposed an interactive segmentation graph cuts algorithm
combinedwiththepriorknowledgeofshapes,thatsolvedtheproblemstoacertainextent
ofinaccuratesegmentationinthecaseofdiffuseedgesormultipleclosesimilarobjects.
Graphcutsalgorithmsarewidelyusedinthefieldofmedicalimageanalysis.
2.2. RegionDivision
Theregiondivisionstrategyincludesserialregiondivisionandparallelregiondivision.
Thresholding is a typical parallel region division algorithm. The threshold is generally
definedbythetroughvalueinagrayhistogramwithsomeprocessingtomakethetroughs
in the histogram deeper or to convert the troughs into peaks. The optimal grayscale
thresholdcanbedeterminedbythezeroth-orderorfirst-ordercumulantmomentofthe
grayhistogramtomaximizethediscriminabilityofthedifferentcategories.
Theserialregiontechniqueinvolvesdividingtheregionsegmentationtaskintomulti-
plestepstobeperformedsequentially,andtherepresentativestepsareregiongrowingand
regionmerging.
Regiongrowinginvolvestakingmultipleseeds(singlepixelsorregions)asinitiation
pointsandcombiningthepixelswiththesameorsimilarfeaturesintheseedneighborhoods
intheregionswheretheseedislocated,accordingtoapredefinedgrowthruleuntilnomore
pixelscanbemerged. Theprincipleofregionmergingissimilartotheregiongrowing,
except that region merging measures the similarity by judging whether the difference
betweentheaveragegrayvalueofthepixelsintheregionobtainedinthepreviousstep
andthegrayvalueofitsadjacentpixelsislessthanthegiventhresholdK. Regionmerging
canbeusedtosolvetheproblemofhardnoiselossandobjectocclusion,andhasagood
effectoncontrollingthesegmentationscaleandprocessingunconventionaldata;however,
itscomputationalcostishigh,andthestoppingruleisdifficulttoaffirm.
Watershedisbasedontheconceptoftopography. Whenwaterrisesfromalowplace,
damsneedtobebuilttopreventthewaterfromreachingthemountainpeaks. Thedams
builtonthemountainpeaksdividetheentireimageintoseveralregions. Thewatershed
algorithm can obtain the closed contour and has high processing efficiency. However,
when the image is more complex, it is prone to false segmentation, that can be solved
by establishing a Gaussian mixture model (GMM). The improved watershed has high
generalizationperformance,isoftenusedinthesegmentationofMRIimagesanddigital
elevation maps, and is especially effective for segmenting medical images containing
overlappingcells(e.g.,bloodcellsegmentation).
The superpixel is a series of small irregular areas composed of pixels with similar
positionsandfeatures(e.g.,brightness,color,andtexture). Usingsuperpixelsinsteadof
pixelstorepresentfeaturescanreducethecomplexityofimageprocessing,soitisoften
usedinthepreprocessingofimagesegmentation. Imagesegmentationmethodsbasedon
superpixelgenerationmainlyincludeclusteringandgraphtheory.
2.3. GraphTheory
Theimagesegmentationmethodbasedongraphtheorymapsanimagetoagraph,
that represents pixels or regions as vertices of the graph, and represents the similarity
between vertices as weights of edges. Image segmentation, based on graph theory, is
regardedasthedivisionofverticesinthegraph,analyzingtheweightedgraphwiththe

Electronics2023,12,1199 5of24
principleandmethodbasedongraphtheory,andobtainingoptimalsegmentationwiththe
globaloptimizationofthegraph(e.g.,themin-cut).
Graph-basedregionmergingusesdifferentmetricstoobtainoptimalglobalgroup-
inginsteadofusingfixedmergingrulesinclustering. Felzenszwalbetal.[11]usedthe
minimumspanningtree(MST)tomergepixelsaftertheimagewasrepresentedasagraph.
ImagesegmentationbasedonMRF(Markovrandomfield)introducesprobabilistic
graphical models (PGMs) into the region division to represent the randomness of the
lower-levelfeaturesintheimages. Itmapstheimagetoanundigraph,whereeachvertex
inthegraphrepresentsthefeatureatthecorrespondinglocationintheimage,andeach
edgerepresentstherelationshipbetweentwovertices. AccordingtotheMarkovproperty
ofthegraph,thefeatureofeachpointisonlyrelatedtoitsadjacentfeatures.
Leordeanuetal.[12]proposedamethodbasedonspectralgraphpartitioningtofind
the correspondence between two sets of features. Adjacency matrix M is built for the
weighted graph corresponding to the image, and the mapping constraints required for
theoverallmappingareimposedontheprincipaleigenvectorsof M,sothatthecorrect
assignmentsarerecoveredaccordingtothestrongdegreeofthemainclusterof M.
2.4. ClusteringMethod
K-meansclusteringisaspecialthresholdingsegmentationalgorithmthatisproposed
basedontheLloydalgorithm. Thealgorithmoperatesasfollows: (i)initializeK points
as clustering centers; (ii) calculate the distance between each point i in the image and
K cluster centers, and select the minimum distance as the classification k ; (iii) average
i
the points of each category (the centroid) and move the cluster center to the centroid;
and(iv)repeatsteps(ii)and(iii)untilalgorithmconvergence. Simplyput,K-meansisan
iterationprocessforcomputingtheclustercenters. TheK-meanshasnoiserobustnessand
quickconvergence,butitisnotconducivetoprocessingnonadjacentregions,anditcan
onlyconvergetothelocaloptimumsolutioninsteadoftheglobaloptimumsolution.
Mean-shift[13]isaclusteringalgorithmbasedondensityestimation,thatmodelsthe
image feature space to the probability density function. Chuang [14] proposed a fuzzy
C-meansalgorithmthatintegratedspatialinformationintothemembershipfunctionfor
clusteringtogeneratemoreuniformregionsegmentation.
Spectralclusteringisacommonclusteringmethodbasedongraphtheory,thatdivides
theweightedgraphandcreatessubgraphswithlowcouplingandhighcohesion. Achanta
etal.[15]proposedasimplelineariterativeclustering(SLIC)algorithmthatusedK-means
togeneratesuperpixels;itssegmentationresultsareshowninFigure3. SLICcanbeapplied
to3Dsupervoxelgeneration. Lietal.[16]proposedasuperpixelsegmentationalgorithm
namedlinearspectralclustering(LSC),thatusedakernelfunctiontomapthecoordinates
ofthepixelvaluesintoahigh-dimensionalspace,andweightedeachpointinthefeature
Electronics 2023, 12, x FOR PEER REVIEW 6 of 25
spaceappropriatelytoobtainthesameoptimalsolutionforboththeobjectivefunctionof
K-meansandthenormalizedcut.
Figure 3. SLIC segmentation results (number of superpixels: 10, 20, 50, and 100).
Figure3.SLICsegmentationresults(numberofsuperpixels:10,20,50,and100).
22..55.. RRaannddoomm WWaallkkss
RRaannddoomm wwaallkkss iiss aa sseeggmmeennttaattiioonn aallggoorriitthhmm bbaasseedd oonn ggrraapphh tthheeoorryy,, tthhaatt iiss ccoommmmoonnllyy
uusseedd iinn iimmaaggees seeggmmeenntatatitoionn,i, mimagaeged edneoniosiinsign[g1 7[1,178,1],8a],n adnidm aimgeagmea mtchatinchgin[1g9 ][.1B9]y. aBsys igasn--
isniggnlianbge llsabtoelasd tjoa caednjatcpeinxet lpsiixnelasc icno radcacnorcdeawnicteh wpriethd epfirnededefrinueleds ,rupliexse,l spwixietlhs twhiethsa tmhee slaambeel
claabnebl ecarne pbree sreenptreedsetnotgeedt htoergetothdeirs ttion dguisitsihngduififsehr edniftfoerbejenctt os.bjects.
Grady et al. [20] transformed the segmentation problem into a discrete Dirichlet
problem. They converted the image into a connected undigraph with weight, and marked
the foreground and background of the image with one or a group of points, respectively,
as initial conditions. For the unmarked points, they calculated the probability of reaching
the foreground and background for the first time in random walks, and then took the
highest probability as its category. Yang et al. [21] proposed a constrained random walks
algorithm, that took user input as subsidiary conditions, e.g., users could assign the fore-
ground and background in the image, or draw the regions where the boundaries must
pass (hard constraint) or the regions where the boundaries can pass or not (soft con-
straint). The framework contained a constrained random walks algorithm and a local edit
algorithm, that resulted in more accurate region contours and interoperability.
Lai et al. [22] extended the random walks image segmentation idea to 3D mesh im-
ages. They represented each side of the mesh as a vertex in the graph, defined the weight
of edges by using the dihedral angle between adjacent faces, and sought a harmonic func-
tion adapted to boundary conditions. On this basis, Zhang et al. [23] proposed a fast geo-
desic curvature flow (FGCF) algorithm, that considered mesh vertices as the graph verti-
ces to reduce the number of vertices in the graph, and changed the cutting contour to the
local minimum of the weighted curve to smooth the zigzag contour. Therefore, the FGCF
with less user input permitted had increased efficiency and higher robustness in the seg-
mentation of the mesh benchmark dataset.
3. Co-Segmentation Methods
The classic segmentation methods usually focus on the feature extraction of a single
image, which makes it difficult to obtain the high-level semantic information of the image.
In 2006, Rother et al. [24] proposed the concept of collaborative segmentation for the first
time. Collaborative segmentation, or co-segmentation for short, involves extracting the
common foreground regions from multiple images with no human intervention, to obtain
prior knowledge. Figure 4 shows a set of examples of co-segmentation results.
Figure 4. Two examples of co-segmentation results.

Electronics 2023, 12, x FOR PEER REVIEW 6 of 25
Figure 3. SLIC segmentation results (number of superpixels: 10, 20, 50, and 100).
2.5. Random Walks
Random walks is a segmentation algorithm based on graph theory, that is commonly
used in image segmentation, image denoising [17,18], and image matching [19]. By as-
Electronics2023,12,1199 6of24
signing labels to adjacent pixels in accordance with predefined rules, pixels with the same
label can be represented together to distinguish different objects.
Grady et al. [20] transformed the segmentation problem into a discrete Dirichlet
Grady et al. [20] transformed the segmentation problem into a discrete Dirichlet
problem. They converted the image into a connected undigraph with weight, and marked
problem. Theyconvertedtheimageintoaconnectedundigraphwithweight,andmarked
the foreground and background of the image with one or a group of points, respectively,
theforegroundandbackgroundoftheimagewithoneoragroupofpoints,respectively,as
as initial conditions. For the unmarked points, they calculated the probability of reaching
initialconditions. Fortheunmarkedpoints,theycalculatedtheprobabilityofreachingthe
the foreground and background for the first time in random walks, and then took the
foregroundandbackgroundforthefirsttimeinrandomwalks,andthentookthehighest
highest probability as its category. Yang et al. [21] proposed a constrained random walks
probabilityasitscategory. Yangetal.[21]proposedaconstrainedrandomwalksalgorithm,
algorithm, that took user input as subsidiary conditions, e.g., users could assign the fore-
thattookuserinputassubsidiaryconditions,e.g.,userscouldassigntheforegroundand
ground and background in the image, or draw the regions where the boundaries must
background in the image, or draw the regions where the boundaries must pass (hard
pass (hard constraint) or the regions where the boundaries can pass or not (soft con-
constraint) or the regions where the boundaries can pass or not (soft constraint). The
straint). The framework contained a constrained random walks algorithm and a local edit
frameworkcontainedaconstrainedrandomwalksalgorithmandalocaleditalgorithm,
algorithm, that resulted in more accurate region contours and interoperability.
thatresultedinmoreaccurateregioncontoursandinteroperability.
Lai et al. [22] extended the random walks image segmentation idea to 3D mesh im-
Lai et al. [22] extended the random walks image segmentation idea to 3D mesh
ages. They represented each side of the mesh as a vertex in the graph, defined the weight
images. They represented each side of the mesh as a vertex in the graph, defined the
of edges by using the dihedral angle between adjacent faces, and sought a harmonic func-
weightofedgesbyusingthedihedralanglebetweenadjacentfaces,andsoughtaharmonic
tion adapted to boundary conditions. On this basis, Zhang et al. [23] proposed a fast geo-
functionadaptedtoboundaryconditions. Onthisbasis,Zhangetal.[23]proposedafast
desic curvature flow (FGCF) algorithm, that considered mesh vertices as the graph verti-
geodesic curvature flow (FGCF) algorithm, that considered mesh vertices as the graph
vceesr ttioc ersedtoucreed thuec entuhmebneurm ofb evrerotficveesr itnic tehsei ngrtahpehg, raanpdh c,haanndgcehda tnhgee cdutthtiengc uctotnintogucro tnot othuer
ltooctahle mloincaimlmumin iomf uthme wofetihgehtwedei cguhrtvede tcou srvmeotoothsm thoeo zthigtzhaegz ciognzatogucro. nTthoeurre.fTorhee,r tehfeo rFeG,tChFe
wFGitChF lewssi tuhsleers sinupsuert pineprumtiptteerdm hiattde dinhcardeaisnecdre eafsfeicdieenfficyc iaenncdy haingdhehri grohbeursrtonbeussst nine stshein sethge-
mseegnmtaetniotant ioofn tohfe tmheesmhe bsehnbcehnmcharmka drkatdasaetta.s et.
33.. CCoo--SSeeggmmeennttaattiioonn MMeetthhooddss
TThhee ccllaassssiicc sseeggmmeennttaattiioonn mmeetthhooddss uussuuaallllyy ffooccuuss oonn tthhee ffeeaattuurree eexxttrraaccttiioonn ooff aa ssiinnggllee
iimmaaggee,, wwhhiicchh mmaakkeess iitt ddiiffffiiccuulltt ttoo oobbttaaiinn tthhee hhiigghh--lleevveell sseemmaannttiicc iinnffoorrmmaattiioonn ooff tthhee iimmaaggee..
IInn 22000066,, RRootthheerr eett aall.. [[2244]] pprrooppoosseedd tthhee ccoonncceepptt ooff ccoollllaabboorraattiivvee sseeggmmeennttaattiioonn ffoorr tthhee ffiirrsstt
ttiimmee.. CCoollllaabboorraattiivvee sseeggmmeennttaattiioonn,, oorr ccoo--sseeggmmeennttaattiioonn ffoorr sshhoorrtt,, iinnvvoollvveess eexxttrraaccttiinngg tthhee
ccoommmmoonn ffoorreeggrroouunndd rreeggiioonnss ffrroomm mmuullttiippllee iimmaaggeess wwiitthh nnoo hhuummaann iinntteerrvveennttiioonn,, ttoo oobbttaaiinn
pprriioorr kknnoowwlleeddggee.. FFiigguurree 44 sshhoowwss aa sseett ooff eexxaammpplleess ooff ccoo--sseeggmmeennttaattiioonn rreessuullttss..
Figure 4. Two examples of co-segmentation results.
Figure4.Twoexamplesofco-segmentationresults.
Toachieveco-segmentation,itisnecessarytoextractthefeaturesoftheforegroundof
singleormultipleimages(theseedimage(s))aspriorknowledgeusingaclassicsegmenta-
tionmethod,andthenutilizethepriorknowledgetoprocessasetofimagescontainingthe
sameorsimilarobjects. Theextendedmodelcanbeexpressedasfollows:
E = E +E (1)
s g
where E representstheenergyfunctionofseedimagesegmentation,thatdescribesthe
s
differencebetweentheforegroundandbackgroundoftheimageandthesmoothnessof
theimage,and E representstheenergyfunctionofco-segmentation,thatdescribesthe
g
similaritybetweenforegroundsinasetofimages.Toachieveagoodco-segmentationeffect,
segmentationenergyEshouldbeminimized. Thiscanbeachievedusingtwomethods:
improvingtheclassicsegmentationmethodtominimizeE ,oroptimizingtheunsupervised
s
learningmethodtolearngoodrepresentationsinimagesetstominimizeE .
g

Electronics2023,12,1199 7of24
TheenergyfunctionintheclassicsegmentationmodelisE . e.g.,whenusingMRF
s
segmentationmethodasE ,then
s
EMRF =EMRF+EMRF (2)
s u p
whereEMRF andEMRF aretheunarypotentialandthepairwisepotential,respectively. The
u p
formermeasuresthepropertiesofthepixelitself,andthelattermeasuresitselfinrelation
tootherpixels. InMRF,theunarypotentialrepresentstheprobabilityofapixelbelonging
to class x when a feature of the pixel is y, which is ∑ E (x ); the pairwise potential
i i xi u i
represents the probability that two adjacent pixels belong to the same category, which
is∑
xi,xj
∈ΨE
p
(cid:0) x
i
,x
j
(cid:1) . Theco-segmentationterm E
g
isusedtopenalizetheinconsistency
of multiple foreground color histograms. In the MRF-based co-segmentation models,
multifariousco-segmentationtermsandtheirminimizationmethodswereproposed.
3.1. MRF-BasedCo-Segmentation
Rotheretal.[24]extendedtheMRFsegmentationandutilizedpriorknowledgeto
solvetheill-posedproblemsinmultipleimagesegmentation. First,theysegmentedthe
foregroundoftheseedimage,andassumedthattheforegroundobjectsofasetofimages
aresimilar;then,theybuilttheenergyfunctionaccordingtotheconsistencyoftheMRF
probabilitydistributionandtheglobalconstraintoftheforegroundfeaturesimilarity;finally,
theyestimatedwhethereachpixelbelongstotheforegroundorbackgroundbyminimizing
theenergyfunctiontoachievethesegmentationoftheforegroundandbackground.
The subsequent research on MRF co-segmentation focused on the optimization of
global constraints. Vicente et al. [25] proposed an extended Boykov–Jolly model using
multiscaledecomposition,basedontheL1normmodel[24],theL2normmodel[26],and
therewardmodel[27]. Comparedwiththeabovethreemodels, theextendedBoykov–
Jolly model made great strides in reducing the number of parameters and improving
robustness. Rubioetal.[28]evaluatedtheforegroundsimilaritythroughhigh-ordergraph
matchingandintroducedhigh-ordergraphmatchingintotheMRFmodeltoformglobal
terms. Chang et al. [29] proposed a universal significance measure for images as prior
knowledge, that could add foreground positional information in the MRF model and
solvetheproblemofsignificantdifferencesintheappearance,shape,andscaleofmultiple
images. Yuetal.[30]adoptedamethodcombinedwithaco-saliencymodeltoachieve
co-segmentation, and they represented the dissimilarity between foreground objects in
eachimageandcommonobjectsinthedatasetwithaGaussianmixturemodelasanew
globalconstraint,thenaddedtheglobalconstrainttoco-segmentationenergyE,andused
graphcutstominimizetheenergyfunctioniteratively.
Theco-segmentationbasedonMRFhasgooduniversality,anditiscommonlyusedin
videoobjectdetectionandsegmentation[30,31]andinteractiveimageediting[32].
3.2. Co-SegmentationBasedonRandomWalks
Collins et al. [33] extended the random walks model to solve the co-segmentation
problem,furtherutilizedthequasiconvexitytooptimizethesegmentationalgorithm,and
providedaprofessionalCUDAlibrarytocalculatethelinearoperationoftheimagesparse
features. Fabijanska et al. [34] proposed an optimized random walks algorithm for 3D
voxel image segmentation, using a supervoxel instead of a single voxel, which greatly
saved computing time and memory resources. Dong et al. [35] proposed a subMarkov
randomwalks(subRW)algorithmwithpriorlabelknowledge,whichcombinedsubRW
withotherrandomwalksalgorithmsforseedimagesegmentation,anditachievedagood
segmentationeffectonimagescontainingslenderobjects.
The co-segmentation methods based on random walks have good flexibility and
robustness. Theyhaveachievedgoodresultsinsomeareasofmedicalimagesegmentation,
especiallyin3Dmedicalimagesegmentation[36,37].

Electronics2023,12,1199 8of24
3.3. Co-SegmentationBasedonActiveContours
Mengetal.[38]extendedtheactivecontourmethodtoco-segmentation,constructed
an energy function based on foreground consistency between images and background
inconsistencywithineachimage,andsolvedtheenergyfunctionminimizationbylevelset.
Zhangetal.[39]proposedadeformableco-segmentationalgorithmwhichtransformed
the prior heuristic information of brain anatomy contained in multiple images into the
constraintscontrollingthebrainMRIsegmentation,andacquiredtheminimumenergyfunc-
tionbylevelset,solvingtheproblemofbrainMRIimagesegmentation.Zhangetal.[40]
introducedthesaliencyoftheregionofinterestintheimageintotheactivecontouralgo-
rithmtoimprovetheeffectoftheco-segmentationofmultipleimages,andproposedalevel
setoptimizationmethodbasedonsuperpixels,hierarchicalcomputing,andconvergence
judgmenttosolvetheminimizedenergyfunction.
The co-segmentation methods based on active contours have a good effect on the
boundaryextractionofcomplexshapes,buttheirunidirectionalmovementcharacteristic
severelylimitstheirflexibility,whichisnotconducivetotherecognitionandprocessingof
objectswithweakedges.
3.4. Clustering-BasedCo-Segmentation
Clustering-basedco-segmentationisanextensionoftheclusteringsegmentationof
asingleimage. Joulinetal.[41]proposedaco-segmentationmethodbasedonspectral
clusteringanddiscriminativeclustering. Theyusedspectralclusteringtosegmentasingle
imagebasedonlocalspatialinformation,andthenuseddiscriminativeclusteringtopropa-
gatethesegmentationresultsinasetofimagestoachieveco-segmentation. Kimetal.[42]
dividedtheimageintosuperpixels,usedaweightedgraphtodescribetherelevanceof
superpixels,convertedtheweightedgraphintoanaffinitymatrixtodescribetherelation
Electronics 2023, 12, x FOR PEER REVIEoWft heintra-image,andthenadoptedspectralclusteringtoachieveco-segmentation. T9h iosf 25
finalrepresentationcanbeseeninFigure5.
Figure 5. An illustration of hierarchical graph clustering constructed between two images. Figure
Figure5.Anillustrationofhierarchicalgraphclusteringconstructedbetweentwoimages.Figure
from [42].
from[42].
IfI fththee nnuummbbeerr ooff iinniittiiaall cclluusstteerr cceenntteerrssi sisn noottl imlimiteitde,dt,h tehecl uclsutesrtienrginmg emtheothdocda ncabne be
apappplileided toto tthhee mmuullttii--oobbjjeeccttiivvee ccoo--sseeggmmeennttaattiioonnp prorobblelemm..T Thheea laglogroirthitmhmfo flololwloswtsh ethper op-ro-
cecsessesse sbbeeloloww.. FFirirsstltyly,, tthhee iimmaaggee iiss sseeggmmeennteteddi nintotol olcoaclarl ergeigoinosnos fomf umltuipltliepsleu psuerppeirxpelixel
blbolockckss ththrroouugghh iimmaaggee pprreepprroocceesssisnign.gT. hTehne,nth, tehseesleo claolcraelg rieognisoanrse aclrues cteluresdtebryeda bclyu sat ecrliunsgter-
inaglg aolrgiothrmithtmo ftoor mfortmhe tchoer rceosrpreosnpdoinngdipnrgio prriinofro irnmfoartimona.tiFoinn.a Flliyn,athlley,p trhioe rpirnifoorr imnafotiromnaitsion
isp prorpoapgaagtaetdedin ians ae tsoeft iomf aigmeasgtoesa cthoi eavcheimevuelt im-oubljteic-tocboje-scetg cmo-esnetgatmioenn.tJaotuiolinn.e Jtoaul.li[n4 3e]tu asle. d[43]
asimilaritymatrixbasedonfeaturepositionsandcolorvectorstorepresentthelocalinfor-
used a similarity matrix based on feature positions and color vectors to represent the local
mationinasingleimage;thatis,spectralclustering. Accordingtothelocalinformationand
information in a single image; that is, spectral clustering. According to the local infor-
featuremappingrelation,theexpectationmaximization(EM)wasusedtominimizetheclas-
mation and feature mapping relation, the expectation maximization (EM) was used to
sificationdiscriminantfunctiontoobtainasetofparameters. Thealgorithmcouldrealize
minimize the classification discriminant function to obtain a set of parameters. The algo-
multipleclassesandasignificantlylargernumberofimageco-segmentationseffectively.
rithm could realize multiple classes and a significantly larger number of image co-seg-
mentations effectively.
3.5. Co-Segmentation Based on Graph Theory
Co-segmentation based on graph theory partitions an image into a digraph.
In contrast to the digraph mentioned earlier, Meng et al. [44] divided each image into
several local regions based on the object detection, and then used these local regions as
nodes to construct a digraph instead of using superpixels or pixels as nodes. Nodes are
connected by directed edges, and the weight of the edges represents the local region sim-
ilarity and saliency map between the two objects. Thereupon, the image co-segmentation
problem was converted into the problem of finding the shortest path on the digraph. Fi-
nally, they obtained the shortest path through the dynamic programming (DP) algorithm.
The flowchart is shown in Figure 6.
In the same year, Meng et al. [45] proposed a new co-saliency model to extract co-
saliency maps from pairwise-constrained images. The co-saliency map consists of two
terms; that is, the saliency map based on a single image and the saliency map based on
multiple images, so it can also be called a dual-constrained saliency map. Compared to
[44], the co-saliency map obtained by pairwise-constrained graph matching is more accu-
rate. They extracted multiple saliency maps by matching similar regions between images,
transformed it into a pairwise-constrained graph matching problem, and solved the pair-
wise-constrained graph matching problem using the DP algorithm.

Electronics2023,12,1199 9of24
3.5. Co-SegmentationBasedonGraphTheory
Co-segmentationbasedongraphtheorypartitionsanimageintoadigraph.
Incontrasttothedigraphmentionedearlier,Mengetal.[44]dividedeachimageinto
severallocalregionsbasedontheobjectdetection,andthenusedtheselocalregionsas
nodestoconstructadigraphinsteadofusingsuperpixelsorpixelsasnodes. Nodesare
connectedbydirectededges,andtheweightoftheedgesrepresentsthelocalregionsimi-
larityandsaliencymapbetweenthetwoobjects. Thereupon,theimageco-segmentation
problemwasconvertedintotheproblemoffindingtheshortestpathonthedigraph.Finally,
Electronics 2023, 12, x FOR PEER REVIEW 10 of 25
theyobtainedtheshortestpaththroughthedynamicprogramming(DP)algorithm. The
flowchartisshowninFigure6.
FFiigguurree 66.. FFrraammeewwoorrkk ooff tthhee ccoo--sseeggmmeennttaattiioonn bbaasseedd oonn tthhee sshhoorrtteesstt ppaatthh aallggoorriitthhmm.. FFiigguurree ffrroomm [[4444]]..
3.6. CIon-Stehgemseanmtaetioyne aBra,sMede onng Tehtearml.a[l4 D5]ifpfursoipono sed a new co-saliency model to extract co-
saliency maps from pairwise-constrained images. The co-saliency map consists of two
Thermal diffusion image segmentation maximizes the temperature of the system by
terms;thatis,thesaliencymapbasedonasingleimageandthesaliencymapbasedon
changing the location of the heat source, and its goal is to find the optimal location of the
multiple images, so it can also be called a dual-constrained saliency map. Compared
heat source to achieve the best segmentation effect. Anisotropic diffusion is a nonlinear
to [44], the co-saliency map obtained by pairwise-constrained graph matching is more
filter that can not only reduce the Gaussian noise but also preserve image edges. It is often
accurate. They extracted multiple saliency maps by matching similar regions between
used in image processing to reduce noise while enhancing image details. Kim et al. [46]
images,transformeditintoapairwise-constrainedgraphmatchingproblem,andsolved
proposed a method called CoSand, that adopted temperature maximization modeling on
thepairwise-constrainedgraphmatchingproblemusingtheDPalgorithm.
anisotropic diffusion, where k heat sources maximize the temperature corresponding to
the segmentation of k-categories; they achieved large-scale multicategory co-segmenta-
tion by maximizing the segmentation confidence of each pixel in the image. Kim et al. [47]
realized multi-foreground co-segmentation by iteratively implementing the two tasks of
scene modeling and region labeling according to the similarity of the foreground objects
in multiple images. In the process of foreground modeling, a spatial pyramid matching
algorithm was used to extract local features, the linear support vector machine (SVM) was
used for feature matching, and the Gaussian mixture model was used for object classifi-
cation and detection. This method achieved good evaluation results on the Flickr MFC
and ImageNet, and was still accurately segmented when foreground objects did not ap-
pear in every image.

Electronics2023,12,1199 10of24
3.6. Co-SegmentationBasedonThermalDiffusion
Thermaldiffusionimagesegmentationmaximizesthetemperatureofthesystemby
changingthelocationoftheheatsource,anditsgoalistofindtheoptimallocationofthe
heatsourcetoachievethebestsegmentationeffect. Anisotropicdiffusionisanonlinear
filterthatcannotonlyreducetheGaussiannoisebutalsopreserveimageedges. Itisoften
usedinimageprocessingtoreducenoisewhileenhancingimagedetails. Kimetal.[46]
proposedamethodcalledCoSand,thatadoptedtemperaturemaximizationmodelingon
anisotropicdiffusion,wherekheatsourcesmaximizethetemperaturecorrespondingto
thesegmentationofk-categories;theyachievedlarge-scalemulticategoryco-segmentation
by maximizing the segmentation confidence of each pixel in the image. Kim et al. [47]
realizedmulti-foregroundco-segmentationbyiterativelyimplementingthetwotasksof
scenemodelingandregionlabelingaccordingtothesimilarityoftheforegroundobjects
inmultipleimages. Intheprocessofforegroundmodeling,aspatialpyramidmatching
algorithm was used to extract local features, the linear support vector machine (SVM)
was used for feature matching, and the Gaussian mixture model was used for object
classificationanddetection. ThismethodachievedgoodevaluationresultsontheFlickr
MFCandImageNet,andwasstillaccuratelysegmentedwhenforegroundobjectsdidnot
appearineveryimage.
3.7. Object-BasedCo-Segmentation
Alexeetal.[48]proposedanobject-basedmeasurementmethodtoquantifythepossi-
bilitythatanimagewindowcontainsobjectsofanycategory. Theprobabilityofwhetherit
isanobjectineachsamplingwindowwascalculatedinadvance,andthehighestscoring
windowwasusedasthefeaturecalibrationforeachcategoryofobjectsaccordingtothe
Bayesiantheory. Themethodcoulddistinguishbetweenobjectswithclearspatialbound-
aries,e.g.,telephones,aswellasamorphousbackgroundelements,e.g.,grass,thatgreatly
reducedthenumberofspecifiedcategoryobjectdetectionwindows. Vicenteetal.[49]used
foregroundobjects,measuredthesimilaritybetweenobjects,extractedthefeatureswith
thehighestscorefrommultiplecandidateobjectclasses,andachievedgoodexperimental
resultsontheiCosegdataset.
To solve the problem of multi-object segmentation, binary segmentation methods
basedontargetsimilarityrankingwereproposed,thatbuiltamodelusingthemaximum
flowofparametersandtrainedascoringfunctiontoobtaintheoptimalpredictionresult.
Thescoringfunctionisdeterminedbytheproperties,e.g.,theconvexityofallobjectsin
theforeground,thecontinuityofthecurve,thecontrastbetweentheforegroundandthe
background, and the positions of the objects in the image. Meng et al. [50] proposed a
multi-groupimageco-segmentationframework,thatcouldobtaininter-imageinformation
in each set of images, generating more accurate prior knowledge; they used MRF and
thedensemappingmodel,usedEMtosolvetheenergy E minimizationproblemofco-
segmentation,andachievedtheco-segmentationofmultipleforegroundrecognition. The
mainmethodsinco-segmentationareshowninTable1.
Table1.Comparisonandanalysisofmainco-segmentationmethods.
Methods Ref. ForegroundFeature Co-Information Optimization
[24] colorhistogram L norm graphcuts
1
quadratic
[26] colorhistogram L norm
2 pseudo-Boolean
MRF-Based
colorand
Co-Segmentation [27] rewardmodel maximumflow
texturehistograms
[25] colorhistogram Boykov–Jollymodel dualdecomposition
[46] colorandSIFTfeatures regionmatching graphcuts

Electronics2023,12,1199 11of24
Table1.Cont.
|     | Methods | Ref. | ForegroundFeature |     | Co-Information | Optimization |
| --- | ------- | ---- | ----------------- | --- | -------------- | ------------ |
|     |         | [29] | SIFTfeature       |     | K-means+L      | graphcuts    |
1,2
Gaussianmixturemodel
|     |     | [48] | SIFTfeature |     |     | graphcuts |
| --- | --- | ---- | ----------- | --- | --- | --------- |
(GMM)constraint
gradientprojectionand
|     |     |      | colorand          |     | improvedrandomwalk |           |
| --- | --- | ---- | ----------------- | --- | ------------------ | --------- |
|     |     | [33] |                   |     |                    | conjugate |
|     |     |      | texturehistograms |     | globalterm         |           |
gradient(GPCG)
| Co-SegmentationBased |               |      | intensityand   |     | improvedrandomwalk |                     |
| -------------------- | ------------- | ---- | -------------- | --- | ------------------ | ------------------- |
|                      |               | [34] |                |     |                    | graphsizereduction  |
|                      | onRandomWalks |      | graydifference |     | globalterm         |                     |
|                      |               |      | labelpriorfrom |     |                    | minimizetheaverage  |
|                      |               | [35] |                |     | GMMs               |                     |
|                      |               |      | userscribbles  |     |                    | reachingprobability |
|                      |               | [38] | colorhistogram |     | rewardmodel        | levelsetfunction    |
co-registeredatlasand
|                      |     | [39] |                     |     | k-means | levelsetfunction |
| -------------------- | --- | ---- | ------------------- | --- | ------- | ---------------- |
| Co-SegmentationBased |     |      | statisticalfeatures |     |         |                  |
onActiveContours
improvedChan–Vese
|     |     | [40] | saliencyinformation |     |     | levelsetfunction |
| --- | --- | ---- | ------------------- | --- | --- | ---------------- |
(C-V)model
SIFT,Gaborfilter,
|     |     | [41] |     |     | Chi-squaredistance | low-rank |
| --- | --- | ---- | --- | --- | ------------------ | -------- |
colorhistogram
|     |                  |      | colorandlocation |     |                        | expectation      |
| --- | ---------------- | ---- | ---------------- | --- | ---------------------- | ---------------- |
|     | Clustering-Based | [43] |                  |     | discriminantclustering |                  |
|     |                  |      | information      |     |                        | maximization(EM) |
Co-Segmentation
pyramidofLABcolors,
[42] HOGtextures,SURF hierarchicalclustering normalizedcutcriterion
featureshistogram
builtdigraphsaccordingto
|     |     | [44] | colorhistogram |     |     | shortestpath |
| --- | --- | ---- | -------------- | --- | --- | ------------ |
regionsimilarityandsaliency
Co-Segmentationbased
|     | onGraphTheory |      | colorand           | buildglobalitemsbasedon |                     |                |
| --- | ------------- | ---- | ------------------ | ----------------------- | ------------------- | -------------- |
|     |               | [45] |                    |                         |                     | shortestpath   |
|     |               |      | shapeinformation   |                         | digraphsandsaliency |                |
|     |               |      | labspacecolorand   |                         |                     | Sub-modularity |
|     |               | [46] |                    |                         | Gaussianconsistency |                |
|     |               |      | textureinformation |                         |                     | optimization   |
Co-SegmentationBased
| onThermalDiffusion |     |      | colorand          |     | GMM&SPM(spatial  |                    |
| ------------------ | --- | ---- | ----------------- | --- | ---------------- | ------------------ |
|                    |     | [47] |                   |     |                  | dynamicprogramming |
|                    |     |      | texturehistograms |     | pyramidmatching) |                    |
multi-scalesaliency,color
maximizingthe
|     | Object-Based | [48] | contrast,edgedensityand |     | Bayesianframework |     |
| --- | ------------ | ---- | ----------------------- | --- | ----------------- | --- |
posteriorprobability
|     | Co-Segmentation |     | superpixelsstraddling |     |     |     |
| --- | --------------- | --- | --------------------- | --- | --- | --- |
[49] 33typesoffeatures randomforestclassifier A-starsearchalgorithm
4. SemanticSegmentationBasedonDeepLearning
Withthecontinuousdevelopmentofimageacquisitionequipment,therehasbeena
greatincreaseinthecomplexityofimagedetailsandthedifferenceinobjects(e.g.,scale,
posture). Low-levelfeatures(e.g.,color,brightness,andtexture)aredifficulttoobtaingood
segmentationresultsfrom,andfeatureextractionmethodsbasedonmanualorheuristic
rulescannotmeetthecomplexneedsofcurrentimagesegmentation,thatputsforwardthe
highergeneralizationabilityofimagesegmentationmodels.
Semantic texton forests [51] and random forest [52] methods were generally used
to construct semantic segmentation classifiers before deep learning was applied to the
fieldofimagesegmentation. Forthepastfewyears,deeplearningalgorithmshavebeen
increasinglyappliedtosegmentationtasks,andthesegmentationeffectandperformance
have been significantly improved. The original approach divides the image into small
patchestotrainaneuralnetworkandthenclassifiesthepixels. Thispatchclassification

Electronics 2023, 12, x FOR PEER REVIEW 12 of 25
pyramid of LAB colors,
normalized cut crite-
[42] HOG textures, SURF fea- hierarchical clustering
rion
tures histogram
built digraphs according to region
Co-Segmentation [44] color histogram shortest path
similarity and saliency
based on Graph
color and shape infor- build global items based on digraphs
Theory [45] shortest path
mation and saliency
lab space color and texture Sub-modularity opti-
Co-Segmentation [46] Gaussian consistency
information mization
Based on Thermal
color and texture histo- GMM & SPM (spatial pyramid
Diffusion [47] dynamic programming
grams matching)
multi-scale saliency, color
maximizing the poste-
[48] contrast, edge density and Bayesian framework
Object-Based Co- rior probability
superpixels straddling
Segmentation
A-star search algo-
[49] 33 types of features random forest classifier
rithm
4. Semantic Segmentation Based on Deep Learning
With the continuous development of image acquisition equipment, there has been a
great increase in the complexity of image details and the difference in objects (e.g., scale,
posture). Low-level features (e.g., color, brightness, and texture) are difficult to obtain
good segmentation results from, and feature extraction methods based on manual or heu-
ristic rules cannot meet the complex needs of current image segmentation, that puts for-
ward the higher generalization ability of image segmentation models.
Semantic texton forests [51] and random forest [52] methods were generally used to
construct semantic segmentation classifiers before deep learning was applied to the field
of image segmentation. For the past few years, deep learning algorithms have been in-
creasingly applied to segmentation tasks, and the segmentation effect and performance
Electronics2023,12,1199 12of24
have been significantly improved. The original approach divides the image into small
patches to train a neural network and then classifies the pixels. This patch classification
algorithm [53] has been adopted because the fully connected layers of the neural network
algorithm[53]hasbeenadoptedbecausethefullyconnectedlayersoftheneuralnetwork
require fixed-size images.
requirefixed-sizeimages.
In 2015, Long et al. [54] proposed fully convolutional networks (FCNs) with convo-
In2015,Longetal.[54]proposedfullyconvolutionalnetworks(FCNs)withconvo-
lution instead of full connection, that made it possible to input any image size, and the
lutioninsteadoffullconnection,thatmadeitpossibletoinputanyimagesize,andthe
FCN architecture is shown in Figure 7. FCNs prove that neural networks can perform end-
FCN architecture is shown in Figure 7. FCNs prove that neural networks can perform
to-end semantic segmentation training, laying a foundation for deep neural networks in
end-to-endsemanticsegmentationtraining,layingafoundationfordeepneuralnetworks
semantic segmentation.
insemanticsegmentation.
Figure7.Fullyconvolutionalnetworksarchitecture.
Figure 7. Fully convolutional networks architecture.
SubsequentnetworkswereadvancedbasedontheFCNmodel. Thefollowingsection
introducesthemaintechnologiesandrepresentativemodelsfromtheperspectiveofhow
semanticsegmentationnetworkswork. Themainsemanticsegmentationalgorithmsbased
ondeeplearningareshowninTable2.
4.1. Encoder–DecoderArchitecture
Encoder–decoderarchitectureisbasedonFCNs. PriortoFCNs,convolutionalneu-
ral networks (CNNs) achieved good effects in image classification, e.g., LeNet-5 [55],
AlexNet[56],andVGG[57],whoseoutputlayersarethecategoriesofimages. However,
semanticsegmentationneedstomapthehigh-levelfeaturesbacktotheoriginalimage
sizeafterobtaininghigh-levelsemanticinformation. Thisrequiresanencoder–decoder
architecture.
In the encoder stage, convolution and pooling operations are mainly performed
toextracthigh-dimensionalfeaturescontainingsemanticinformation. Theconvolution
operationinvolvesperformingthemultiplicationandsummingoftheimage-specificregion
withdifferentconvolutionkernelspixel-for-pixel, andthentransformingtheactivation
function to obtain a feature map. The pooling operation involves sampling within a
certain region (the pooling window), and then using a certain sampling statistic as the
representativefeatureoftheregion. Thebackboneblockscommonlyusedinsegmentation
networkencodersareVGG,Inception[58,59],andResNet[60].
Inthedecoderstage,anoperationisperformedtogenerateasemanticsegmentation
mask by the high-dimensional feature vector. The process to map back the multi-level
featuresextractedbytheencodertotheoriginalimageiscalledup-sampling.
• Theinterpolationmethodusesaspecifiedinterpolationstrategytoinsertnewelements
betweenthepixelsoftheoriginalimage,therebyexpandingthesizeoftheimageand
achievingtheeffectofup-sampling.Interpolationdoesnotrequiretrainingparameters
andisoftenusedinearlyup-samplingtasks;
• The FCN adopts deconvolution for up-sampling. Deconvolution, also known as
transposedconvolution,reversestheparametersoftheoriginalconvolutionkernel
upsidedownandflippedhorizontally,andfillsthespacesbetweenandaroundthe
elementsoftheoriginalimage;
• SegNet[61]adoptstheup-samplingmethodofunpooling. Unpoolingrepresentsthe
inverseoperationofmax-poolingintheCNN.Duringmaximumpooling,notonly

Electronics2023,12,1199 13of24
themaximumvalueofthepoolingwindow,butalsothecoordinatepositionofthe
maximumvaluesshouldberecorded;inthecaseofunpooling,themaximumvalueof
thispositionisactivated,andthevaluesinotherpositionsareallsetto0;
• Wangetal.[62]proposedadenseup-samplingconvolution(DUC),thecoreideaof
whichistoconvertthelabelmappinginthefeaturemapintosmallerlabelmapping
withmultiplechannels. Thistransformationcanbeachievedbydirectlyusingconvo-
lutionsbetweentheinputfeaturemapandtheoutputlabelmap,withouttheneedto
interpolateextravaluesduringtheup-samplingprocess.
4.2. SkipConnections
Skip connections or shortcut connections were developed to improve rough pixel
positioning. Withdeepneuralnetworktraining,theperformancedecreasesasthedepth
increases, which is a degradation problem. To ameliorate this problem, different skip
connectionstructureshavebeenproposedinResNetandDenseNet[63]. Incontrast,U-
Net[64]proposedanewlongskipconnection,asshowninFigure8. U-Netmakesjump
connectionsandcascadesoffeaturesfromlayersintheencodertothecorrespondinglayers
inthedecodertoobtainthefine-graineddetailsofimages. Itwasproposedtosolvethe
Electronics 2023, 12, x FOR PEER REVpIErWob lemofannotationsinimagesegmentationbasedonbiologicalmicroscopes,and14i tohf a2s5
sincebeenwidelyusedinresearchonmedicalimagesegmentation.
Figure 8. U-Net architecture. Figure from [64].
Figure8.U-Netarchitecture.Figurefrom[64].
44..33.. DDiillaatteedd CCoonnvvoolluuttiioonn
DDiillaatteedd ccoonnvvoolluuttiioonn,, aallssoo kknnoowwnn aass aattrroouuss ccoonnvvoolluuttiioonn,, iiss ccoonnssttrruucctteedd bbyy iinnsseerrttiinngg
hhoolleess iinnttoo tthhee ccoonnvvoolulutitoionnk keernrneellt otoe xepxapnadndth tehree rceecpetpivteivfiee flideladn adnrde druedceutchee thcoem copmutpautitoan-
dtiuonri ndgudrionwg nd-osawmnp-slainmgp.IlninFgC. INn, FthCeNm, athxe-p mooalxin-pgoloalyienrgs laaryeerresp alarcee rdepblyadceilda tbeyd dcoilnavteodlu ctoionn-
tvoolmutaiionnt ation mthaeinrteacieni vthine greficeelidvinofg tfhieeldco orfr ethsep oconrdriensgpolanydeirngan ladytehre anhdig thhere hsioglhu trieosnoloufttiohne
foefa tthuer efemataupr.e map.
TThhee DDeeeeppLLaabb sseerriieess [[6655––6688]] aarree ccllaassssiicc mmooddeellss iinn tthhee ffiieelldd ooff sseemmaannttiicc sseeggmmeennttaattiioonn..
PPrriioorr ttoop puutttitninggf ofrowrwaradrdD eDepeeLpaLbaVb1 ,Vt1h,e tsheem saenmticansetigcm seengtmateionntarteiosunl trsewsuelrtes uwsuerael lyusrouualglhy
drouuegtho dthueet troa ntshfee rtriannvsafreira nincevalorisatnincet hloespt oino ltihneg pporoocliensgs, parnodcethsse, parnodb athbeil ipstriocbraeblaitliisotnics hriep-
blaettiwonesehnipla bbeetlwseneont luasbeedlsf noortp urseeddic ftoior np.reTdoicatmioenl.i oTroa atemtehleioserapter othbelesme ps,roDbeleepmLsa, bDeVe1p[L6a5b]
uVs1e s[6d5i]l autseeds cdoinlavtoeldu tcioonnvtoolusotilovne ttho esoplrvoeb ltehme porforbelseomlu toiof nrerseodluutcitoionn redduuricntigounp d-usarminpgl iunpg-,
sampling, and uses fully connected conditional random fields (fully connected CRFs) to
optimize the post-processing of segmented images to obtain objects at multi-scales and
context information.
Yu et al. [69] used dilated convolution to aggregate multiscale context information.
They adopted a context module with eight convolutional layers, among which seven lay-
ers applied different 3 × 3 convolution kernels with different dilation factors (i.e., [1, 1, 2,
4, 8, 16, 1]), that proved that the simplified adaptive network could further improve the
accuracy and precision of image segmentation without any resolution being lost. In [70],
they proposed a dilated residual network (DRN) based on ResNet, that included five
groups of convolutional layers. The down-sampling of the latter two groups (i.e., G4 and
G5) was removed to maintain the spatial resolution of the feature map. Instead of this, the
subsequent convolutions of G4 and G5 used dilated convolutions with dilatation rates
𝑟 =2 and 𝑟=4, respectively.
Wang et al. [62] proposed a hybrid dilated convolution (HDC) to effectively deal with
the “gridding” problem caused by dilated convolution. The HDC makes the final size of
the receptive field of a series of convolution operations completely cover a square region
without any holes or missing edges. To enable this, they used a different dilation rate for
each layer, instead of using the same dilation rate for all layers after previous down-sam-
pling.

Electronics2023,12,1199 14of24
andusesfullyconnectedconditionalrandomfields(fullyconnectedCRFs)tooptimize
the post-processing of segmented images to obtain objects at multi-scales and context
information.
Yuetal.[69]useddilatedconvolutiontoaggregatemultiscalecontextinformation.
Theyadoptedacontextmodulewitheightconvolutionallayers,amongwhichsevenlayers
applied different 3 × 3 convolution kernels with different dilation factors (i.e., [1, 1, 2,
4,8,16,1]),thatprovedthatthesimplifiedadaptivenetworkcouldfurtherimprovethe
accuracyandprecisionofimagesegmentationwithoutanyresolutionbeinglost. In[70],
they proposed a dilated residual network (DRN) based on ResNet, that included five
groupsofconvolutionallayers. Thedown-samplingofthelattertwogroups(i.e.,G4and
G5)wasremovedtomaintainthespatialresolutionofthefeaturemap. Insteadofthis,
thesubsequentconvolutionsofG4andG5useddilatedconvolutionswithdilatationrates
r =2andr =4,respectively.
Wang et al. [62] proposed a hybrid dilated convolution (HDC) to effectively deal
withthe“gridding”problemcausedbydilatedconvolution. TheHDCmakesthefinal
sizeofthereceptivefieldofaseriesofconvolutionoperationscompletelycoverasquare
Electronics 2023, 12, x FOR PEER REVrIeEgWi onwithoutanyholesormissingedges. Toenablethis,theyusedadifferentd1i5l aotfi o2n5
rate for each layer, instead of using the same dilation rate for all layers after previous
down-sampling.
4.4. Multiscale Feature Extraction
4.4. MultiscaleFeatureExtraction
Spatial pyramid pooling (SPP) was proposed to solve the problem of the CNNs re-
Spatial pyramid pooling (SPP) was proposed to solve the problem of the CNNs
qreuqiruiinrgin fgixfiexde-sdi-zsei zienpinupt uimt iamgaesg.e Hs.eH eet aelt. a[7l.1[]7 d1e]vdeelvoepleodp ethdet hSPePS-PnPe-t naentda nvdervifeierdifi ietds eitfs-
feefcfeticvteivneenses sisni nsesmemanatnict icsesgemgmenetnattaiotino nanadn dobojbejcetc tddeteetcetcitoionn. .TToo mmaakkee tthhee mmoosstt ooff iimmaaggee
ccoonntteexxtt iinnffoorrmmaattiioonn,, ZZhhaaoo eett aall.. [[7722]] ddeevveellooppeedd PPSSPPNNeett wwiitthh aa ppyyrraammiidd ppoooolliinngg mmoodduullee
((PPPPMM)),, aass sshhoowwnn iinn FFiigguurree 99.. UUssiinngg RReessNNeett aass tthhee bbaacckkbboonnee nneettwwoorrkk,, tthhee PPSSPPNNeett uuttiilliizzeedd
PPPPMM ttoo eexxttrraacctta anndda gaggrgergeagtaeted idffiefrfeernetnstu sburebgrieogniofnea fteuarteusraetsd aitff edrieffnetrsecnatl essc,atlheas,t twhearte wtheerne
tuhpe-ns aumpp-slaemdapnleddc aonndca ctoennacatetedntaotefodr mto tfhoermfe athtuer feematuapre, tmhaatpc, atrhraiet dcabrortihedl obcoatlha nlodcagll oabnadl
gcolonbtaelx tcoinnftoerxmt iantifoonrm. Iattiiosnp. aIrt tiics uplaarrltyicuwlaorrltyh wnootritnhg ntohtaitngth tehnatu mthbe enruomf pbeyrr aomf ipdyrlaaymeirds
laanydertsh eansdiz ethoef seiazceh olfa yeaercha rleayvearr iaarbel ev,atrhiaatbdlee, pthenadt doenptehneds oizne tohfet hsiezfee aotfu trheem feaaptuinrep umtatpo
itnhpeuPtP tMo t.he PPM.
Figure 9. The PSPNet with the pyramid pooling module. Figure from [72].
Figure9.ThePSPNetwiththepyramidpoolingmodule.Figurefrom[72].
GGhhiiaassii aannddF Fowowlklekses[7 3[7]3d]e sdcersibcreidbeadm au lmti-ureltsio-rluestioolnutrieocno nrsetcrounctsitornucatricohni teacrtcuhrietebcatuserde
boansaedL aopnl aac Liaanplpayciraanm pidy,rathmaitdu, stehdats uksipedc oskninpe cctoinonnescftrioomns hfrigohme rh-rigeshoelru-rteiosnolfuetaiotunr efemataupres
manadpsm aunltdip mlicualttiivpelicgaattivineg gtaotirnegfi ntoe sreegfimnee nsetagtmioennbtaotuionnd abroiuesndreacroienss trreuccotnesdtrfuroctmedl ofwroemr-
lroewsoelur-trieosnolmuatiposn smucacpess ssiuvcecleys.sively.
DDeeeeppLLaabb VV22 [[6666]] iinnttrroodduucceedd aattrroouuss ssppaattiiaall ppyyrraammiidd ppoooolliinngg ((AASSPPPP)) ttoo eexxppaanndd tthhee
rreecceeppttiivvee ffiieelldd aanndd ccaappttuurree mmuullttiissccaallee ffeeaattuurreess.. TThhee AASSPPPP mmoodduullee ccoonnttaaiinneedd ffoouurr ppaarraalllleell
ddiillaatteedd ccoonnvvoolluuttiioonnss wwiitthh ddiiffffeerreenntt ddiillaattiioonn rraatteess,, aass sshhoowwnn iinn FFiigguurree 1100.. RReeffeerrrriinngg ttoo tthhee
HHDDCC mmeetthhoodd,, DDeeeeppLLaabb VV33 [[6677]] aapppplliieedd bbootthh ccaassccaaddee mmoodduulleess aanndd ppaarraalllleell mmoodduulleess ooff
ddiillaatteedd ccoonnvvoolluuttiioonn, ,ggrroouuppeedd ththe epapraarlalellle clocnovnovloultuiotino inn itnheth AeSAPPSP mPomduoldeu, alen,da andddaeddd tehde
1th ×e 11 ×con1vcoolnuvtioolnu tliaoynelra aynedr abnadtcbha ntcohrmnoarlimzaatliioznat iionn thine tAhSePAPS mPPodmuoled.u Tleh.eT DheeeDpeLeapbL Vab3
Vsig3nsiifgicnainfitclayn itmlypirmovperdo voend tohne tphreevpioreuvsi oDuesepDLeaebp Lvaebrsvioenrss iownitshwouitth DouentsDeeCnRsFe CpRoFst-pporsot--
cessing. Moreover, using Xception as the backbone network and DeepLab V3 as the de-
coder, DeepLab V3+ [68] adopted dilated depth wise separable convolutions instead of
max-pooling and batch normalization to refine the segmentation boundaries.
Figure 10. Atrous spatial pyramid pooling module. Figure from [66].

Electronics 2023, 12, x FOR PEER REVIEW 15 of 25
4.4. Multiscale Feature Extraction
Spatial pyramid pooling (SPP) was proposed to solve the problem of the CNNs re-
quiring fixed-size input images. He et al. [71] developed the SPP-net and verified its ef-
fectiveness in semantic segmentation and object detection. To make the most of image
context information, Zhao et al. [72] developed PSPNet with a pyramid pooling module
(PPM), as shown in Figure 9. Using ResNet as the backbone network, the PSPNet utilized
PPM to extract and aggregate different subregion features at different scales, that were
then up-sampled and concatenated to form the feature map, that carried both local and
global context information. It is particularly worth noting that the number of pyramid
layers and the size of each layer are variable, that depend on the size of the feature map
input to the PPM.
Figure 9. The PSPNet with the pyramid pooling module. Figure from [72].
Ghiasi and Fowlkes [73] described a multi-resolution reconstruction architecture
based on a Laplacian pyramid, that used skip connections from higher-resolution feature
maps and multiplicative gating to refine segmentation boundaries reconstructed from
lower-resolution maps successively.
DeepLab V2 [66] introduced atrous spatial pyramid pooling (ASPP) to expand the
receptive field and capture multiscale features. The ASPP module contained four parallel
dilated convolutions with different dilation rates, as shown in Figure 10. Referring to the
HDC method, DeepLab V3 [67] applied both cascade modules and parallel modules of
Electronics2023,12,1199 15of24
dilated convolution, grouped the parallel convolution in the ASPP module, and added the
1 × 1 convolution layer and batch normalization in the ASPP module. The DeepLab V3
significantly improved on the previous DeepLab versions without DenseCRF post-pro-
pcerossciensgs.i nMgo.rMeoovreero,v uesr,inugs iXncgeXptcieopnt iaosn thase tbhaeckbbaocknbe onneetwneotrwk oarnkda DndeeDpLeeapb LVa3b aVs3 thaes tdhee-
dcoedcoedr,e Dr,eDeepeLpaLba bV3V+3 +[6[86]8 a]daodpotpetde dddilialtaetded ddeeppthth wwisisee sseeppaarraabbllee ccoonnvvoolluuttiioonnss iinnsstteeaadd ooff
mmaaxx--ppoooolliinngg aanndd bbaattcchh nnoorrmmaalliizzaattiioonn ttoo rreefifinnee tthhee sseeggmmeennttaattiioonn bboouunnddaarriieess..
FFiigguurree 1100.. AAttrroouuss ssppaattiiaall ppyyrraammiidd ppoooolliinngg mmoodduullee.. FFiigguurree ffrroomm [[6666]]..
TheschemeofFPN(featurepyramidnetwork)[74]issimilartotheskipconnections
oftheU-Netmodel,thatisbeneficialforobtaininghighresolutionandstrongsemantic
featuresforobjectdetectionwithsignificantsizedifferencesintheimages. Heetal.[75]
proposedanadaptivepyramidcontextnetwork(APCNet)tosolvetheoptimalsolution
ofsemanticsegmentation. Theyutilizedmultipleadaptivecontextmodules(ACMs)to
build multiscale contextual feature representations; each ACM used the global image
representationtoestimatethelocalaffinityweightsofeachsubregionandcalculatedthe
optimalcontextvectoraccordingtotheselocalaffinityweights.
Yeetal.[76]developedanenhancedfeaturepyramidnetwork(EFPN),thatcombined
asemanticenhancementmodule(SEM),edgeextractionmodule(EEM),andcontextag-
gregationmodel(CAM)intoadecodernetworktoimprovetherobustnessofmulti-level
featurefusion,andaddedaglobalfusionmodel(GFM)intotheencodernetworktocapture
moredeepsemanticinformationandtransmitittoeachlayerefficiently. Amongthem,
theSEMupgradedtheASPPmodulebymodifyingsmallerdilationratestoenhanceand
obtainlow-levelfeaturesandreplacingthepoolinglayerwithashortresidualconnection
inpost-processingtoavoidthelossofshallowsemanticinformation,thatsimplifiedthe
networkwithadenserconnection.
Wuetal.[77]proposedFPANet,afeaturepyramidaggregationnetworkforreal-time
semantic segmentation. FPANet is also an encoder–decoder model, using ResNet and
ASPPintheencoderstageandasemanticbidirectionalfeaturepyramidnetwork(SeBiFPN)
inthedecoderstage. Reducingthenumberoffeaturechannelswithalightweightfeature
pyramidfusionmodule(FPFM),theSeBiFPNwasutilizedtoobtainboththesemanticand
spatialinformationofimagesandfusefeaturesofdifferentlevels.
4.5. AttentionMechanisms
Torepresentthedependencybetweendifferentregionsinanimage,especiallythelong-
distanceregions,andobtaintheirsemanticrelevance,somemethodscommonlyusedinthe
fieldofnaturallanguageprocessing(NLP)havebeenappliedtocomputervision,thathave
madegoodachievementsinsemanticsegmentation. Theattentionmechanismwasfirstput
forwardinthecomputervisionfieldin2014. TheGoogleMindteam[78]adoptedtherecur-
rentneuralnetwork(RNN)modeltoapplyattentionmechanismstoimageclassification,
makingattentionmechanismsgraduallypopularinimageprocessingtasks.
RNN can model the short-term dependence between pixels, connect pixels, and
processthemsequentially,whichestablishesaglobalcontextrelationship. Visinetal.[79]
proposedaReSegnetworkbasedonReNet[80],andeachReNetlayerconsistedoffour

Electronics 2023, 12, x FOR PEER REVIEW 16 of 25
The scheme of FPN (feature pyramid network) [74] is similar to the skip connections
of the U-Net model, that is beneficial for obtaining high resolution and strong semantic
features for object detection with significant size differences in the images. He et al. [75]
proposed an adaptive pyramid context network (APCNet) to solve the optimal solution
of semantic segmentation. They utilized multiple adaptive context modules (ACMs) to
build multiscale contextual feature representations; each ACM used the global image rep-
resentation to estimate the local affinity weights of each subregion and calculated the op-
timal context vector according to these local affinity weights.
Ye et al. [76] developed an enhanced feature pyramid network (EFPN), that com-
bined a semantic enhancement module (SEM), edge extraction module (EEM), and context
aggregation model (CAM) into a decoder network to improve the robustness of multi-
level feature fusion, and added a global fusion model (GFM) into the encoder network to
capture more deep semantic information and transmit it to each layer efficiently. Among
them, the SEM upgraded the ASPP module by modifying smaller dilation rates to enhance
and obtain low-level features and replacing the pooling layer with a short residual con-
nection in post-processing to avoid the loss of shallow semantic information, that simpli-
fied the network with a denser connection.
Wu et al. [77] proposed FPANet, a feature pyramid aggregation network for real-
time semantic segmentation. FPANet is also an encoder–decoder model, using ResNet
and ASPP in the encoder stage and a semantic bidirectional feature pyramid network (Se-
BiFPN) in the decoder stage. Reducing the number of feature channels with a lightweight
feature pyramid fusion module (FPFM), the SeBiFPN was utilized to obtain both the se-
mantic and spatial information of images and fuse features of different levels.
4.5. Attention Mechanisms
To represent the dependency between different regions in an image, especially the
long-distance regions, and obtain their semantic relevance, some methods commonly
used in the field of natural language processing (NLP) have been applied to computer
vision, that have made good achievements in semantic segmentation. The attention mech-
anism was first put forward in the computer vision field in 2014. The Google Mind team
[78] adopted the recurrent neural network (RNN) model to apply attention mechanisms
to image classification, making attention mechanisms gradually popular in image pro-
cessing tasks.
Electronics2023,12,1199 16of24
RNN can model the short-term dependence between pixels, connect pixels, and pro-
cess them sequentially, which establishes a global context relationship. Visin et al. [79]
proposed a ReSeg network based on ReNet [80], and each ReNet layer consisted of four
RRNNNNss tthhaatt sswweepptt iinn bbootthh hhoorriizzoonnttaall aanndd vveerrttiiccaall ddiirreeccttiioonnss aaccrroossss tthhee iimmaaggee ttoo oobbttaaiinn
gglloobbaall iinnffoorrmmaattiioonn.. TThhee RReeSSeegg aarrcchhiitteeccttuurree iiss sshhoowwnn iinn FFiigguurree 1111..
Figure 11. The ReSeg architecture. Figure from [79].
Figure11.TheReSegarchitecture.Figurefrom[79].
LLSSTTMM ((lloonngg sshhoorrtt--tteerrmm mmeemmoorryy)) aaddddss aa nneeww ffuunnccttiioonn ttoo rreeccoorrdd lloonngg--tteerrmm mmeemmoorryy,,
tthhaatt ccaann rreepprreesseennt tlolnong-gd-disitsatnacnec ededpeepnednednecnec. eB.yeBoyne eotn ale.t [8a1l.] u[8s1e]du LsSeTdML StoT aMchtioevaec phiixeevle-
pfoixr-epl-ifxoerl- pseixgemlesengtamtieonnt aotfi osnceonfes icmenaegeims, awgehsi,chw phricohvepdro tvheadt itmhaatgiem taexgteutreex itnufroerimnfaotrimona tainodn
aspnadtisapl amtioadleml poadrealmpeatrearms ceoteurlsd cboeu lledarbneedle ianr na e2dDi LnSaTM2D mLoSdTeMl. Lmiaondge el.t aLl.i a[8n2g] petroapl.o[s8e2d]
pa rsoepmosaendtica sseemgmanentitcasteiognm menotdateilo bnamseodd eolnb tahsee dgoranpthh eLgSrTaMph mLoSdTeMl, mthoadt eelx,ttehnadteedxt eLnSdTeMd
Electronics 2023, 12, x FOR PEER REVIEW 17 of 25
LfrSoTmM sferqoumensteiqaul ednattiaa lodr amtauoltridmimuletindsiimoneanls idoantaal tdoa taa gteonaergaeln gerraaplghr astprhucsttururec,t ufurer,thfuerrt hener-
ehnahnacinncgin tgheth gelogbloabl acolncotenxtte xvtisvuisaul afelafteuartuesr.e s.
BothRNNandLSTMhavetheirlimitations,e.g.,weakenedlong-distancedependence,
requiring too manyBpoathra RmNeNte rasn,da nLdSTnMot haalvloew thineigr plimariatallteiolnosp, eer.agt.,i ownesa.kOenketda yloentga-dl.is[8ta3n]ce depend-
ence, requiring too many parameters, and not allowing parallel operations. Oktay et al.
proposedattentionU-Net,asshowninFigure12,thatintroducedanattentionmechanism
[83] proposed attention U-Net, as shown in Figure 12, that introduced an attention mech-
inU-Net. Priortosplicingthefeaturesateachresolutionoftheencoderwiththecorre-
anism in U-Net. Prior to splicing the features at each resolution of the encoder with the
sponding features in the decoder, they used attention gate (AG) modules to supervise
corresponding features in the decoder, they used attention gate (AG) modules to super-
thefeaturesofthepreviouslayerthroughthefeaturesofthenextlayer,thusreadjusting
vise the features of the previous layer through the features of the next layer, thus read-
theoutputfeaturesoftheencoder. TheAGmodulesadjustedtheactivationvalueadap-
justing the output features of the encoder. The AG modules adjusted the activation value
tivelybygeneratingagatedsignalandsuppressedthefeatureresponsesoftheunrelated
adaptively by generating a gated signal and suppressed the feature responses of the un-
backgroundregionsprogressivelytocontroltheimportanceofdifferentspatialfeatures.
related background regions progressively to control the importance of different spatial
Paletal.[84]proposedanattentionUW-Net,thatachievedagoodperformanceonmedical
features. Pal et al. [84] proposed an attention UW-Net, that achieved a good performance
chestX-rayimages. TheattentionUW-NetimprovesaskipconnectionbasedontheU-Net
on medical chest X-ray images. The attention UW-Net improves a skip connection based
segmentationnetwork,i.e.,adenseconnectionisaddedbetweentheB-5andB-6blocksof
on the U-Net segmentation network, i.e., a dense connection is added between the B-5 and
theoriginalU-Netarchitecture,thatallowsthenetworktolearnthedetailslostintheprevi-
B-6 blocks of the original U-Net architecture, that allows the network to learn the details
ousmax-poolingandeffectivelyreducestheinformationloss. Inaddition,animproved
lost in the previous max-pooling and effectively reduces the information loss. In addition,
attentiongateisdesigned,thatmodifiestheresamplingoftheattentionvectorsbycopying
an improved attention gate is designed, that modifies the resampling of the attention vec-
thevectorspaceinthechannelattention,whichcouldbetterrealizetheattentiontothe
tors by copying the vector space in the channel attention, which could better realize the
salientregionandthesuppressionoftheirrelevantbackgroundregion.
attention to the salient region and the suppression of the irrelevant background region.
Figure12.TheatFteignutiroen 1U2.- TNheet aatrtcehnittieocnt uUr-eN.eFti gaurcrheitferoctmur[e8. 3F]i.gure from [83].
Self-attentionmSeelcfh-aatnteinsmtiosna mreemchoasntilsymuss aerde imnotshtelye unsceodd einr ntheet wenocrokdteor rneeptwreosrekn ttot hreepresent the
correlationbetwcoererneldatiifofenr ebnettwreegenio dnisff(epriexnetl sre)goirondsif (fperixeenlts)c hora ndnifefelsreonft tchheafnenaetlusr oef mthaep fse.aItture maps. It
computes a weighted sum of pairwise affinities across all positions of a single sample to
update the feature at each position. Self-attention mechanisms have produced many in-
fluential achievements in image segmentation, e.g., PSANet [85], DANet [86], APCNet
[75], CARAFE [87], and CARAFE++ [88].
In 2017, Vaswani et al. [89] proposed the transformer, a deep neural network solely
based on a self-attention mechanism, dispensing with convolutions and recurrence en-
tirely. Thereafter, transformer and its variants (i.e., X-transformer) were used in the field
of computer vision. With the self-attention mechanism of the transformer and CNN pre-
training model, the improved network [90,91] achieved some breakthroughs. Dosovitskiy
et al. [92] proposed a vision transformer (ViT), that proved that transformer could substi-
tute for CNN in classification and prediction of image patch sequences. As shown in Fig-
ure 13, they divided the image into patches of fixed sizes, lined up the image patches, and
input the patches sequence vector into a transformer encoder (the right-hand diagram),
that consisted of alternating multi-head attention layers and multi-layer perceptron
(MLP).

Electronics2023,12,1199 17of24
computesaweightedsumofpairwiseaffinitiesacrossallpositionsofasinglesampleto
updatethefeatureateachposition. Self-attentionmechanismshaveproducedmanyinflu-
entialachievementsinimagesegmentation,e.g.,PSANet[85],DANet[86],APCNet[75],
CARAFE[87],andCARAFE++[88].
In2017,Vaswanietal.[89]proposedthetransformer,adeepneuralnetworksolely
basedonaself-attentionmechanism,dispensingwithconvolutionsandrecurrenceentirely.
Thereafter,transformeranditsvariants(i.e.,X-transformer)wereusedinthefieldofcom-
putervision. Withtheself-attentionmechanismofthetransformerandCNNpre-training
model,theimprovednetwork[90,91]achievedsomebreakthroughs. Dosovitskiyetal.[92]
proposed a vision transformer (ViT), that proved that transformer could substitute for
CNNinclassificationandpredictionofimagepatchsequences. AsshowninFigure13,
theydividedtheimageintopatchesoffixedsizes,lineduptheimagepatches,andinput
Electronics 2023, 12, x FOR PEER REVtIhEWe patches sequence vector into a transformer encoder (the right-hand1d8 ioafg 2r5a m), that

consistedofalternatingmulti-headattentionlayersandmulti-layerperceptron(MLP).
Electronics 2023, 12, x FOR PEER REVIEW  18 of 25

FFiigguurree 1133. .TTheh VeiVTi Tmomdoeld. eFli.gFuirge ufrroemfr [o9m2]. [92].
Figure 13. The ViT model. Figure from [92].
LLiuiu eet tala. l[.9[39]3 d]edveelvoepleodp tehde tshweins wtrainnstfroarnmsefro,r tmhaetr h,aths aatchhiaevseadc himiepvreedssiivme ppreersfosriv-eperfor-
mance in image semantic segmentation and instance segmentation. The swin transformer  manceiLniuim eta agle. [s9e3m] daenvteiclospeegdm theen stawtiino ntraannsdfoirnmstearn, tcheast ehgams aecnhtiaetvieodn .imTphreessswivien ptrearfnosrf-ormer
advanced the sliding window approach, that built hierarchical feature maps by merging
advmaanncceed int himeasglied sienmgawntiinc dseogwmaenptpartiooanc ahn,dth inasttabnucielt shegiemraenrctahtiicoanl. Tfehaet uswreinm traapnssfboyrmmere rging
image patches in deeper layers, calculated self-attention in each local window, and uti-
imaagdevapnacetcdh tehse isnliddienegp weirnldaoywer asp,pcraolaccuhla, ttheadt sbeulifl-ta htiteernatricohnicainl feeaatcuhrel omcaaplsw biyn mdoerwg,inagn d uti-
lized cyclic-shifting window partition approaches alternatively in the consecutive swin  lizeimdacgyec lpica-tcshheisft iinn gdewepinedr olawyerpsa, rctailtciuolnataepd psreolfa-acthteenstiaolnte irnn eaaticvhe lloycainl wthinedcoown, saencdu tuivtie-
swin
transformer blocks to introduce cross-window connections between neighboring non-
transformer lized cyclic-shifting window partition approaches alternatively in the consecutive swin  blocks to introduce cross-window connections between neighboring non-
overlapping windows. The swin transformer network replaced the standard multi-head
transformer blocks to introduce cross-window connections between neighboring non-
self-attention (MSA) module in a transformer block with shifted window approach, with  overlappingwindows. Theswintransformernetworkreplacedthestandardmulti-head
overlapping windows. The swin transformer network replaced the standard multi-head
tsheelf o-athtteern latiyoenrs( rMemSAain)imngo tdhuel seaimnea, atsr asnhosfwonrm ine Fribgulorcek 14w. ithshiftedwindowapproach,with
self-attention (MSA) module in a transformer block with shifted window approach, with
theotherlayersremainingthesame,asshowninFigure14.
the other layers remaining the same, as shown in Figure 14.

Figure 14. The architecture of a swin transformer. Figure from [93].
Figure 14. The architecture of a swin transformer. Figure from [93].
TFiagbuler e2.1 C4o.mThpaeraisrocnh iatnedct aunraelyosfisa osfw seinmtarnatnics fsoegrmmeenr.taFtiigonu rmeeftrhoomds[ b9a3s]e.d on deep learning.
Table 2. Comparison and analyEsxips eofr ismemenantsti c segmentation methods based on deep learning.
Pub.
| Algorithms  |         | Backbone  |                                |     | Major Contributions  |
| ----------- | ------- | --------- | ------------------------------ | --- | -------------------- |
|             | YeaPru  |           | Datasets ExperimmIeonUts ( %)  |     |                      |
b.
| Algorithms  |       | Backbone  |                  |           | Major Contributions            |
| ----------- | ----- | --------- | ---------------- | --------- | ------------------------------ |
|             | Year  |           | PASDCaAtaLs ets  | mIoU (%)  |                                |
|             |       |           |                  | 62.7      | The forerunner for end-to-end  |
| FCN [54]    | 2015  | VGG-16    | VOCP A20S1C1A    |           |                                |
L
|           |       |         |                  | 62.7        | Tsehme faonrteicru snegnmere fnotra etinodn- to-end  |
| --------- | ----- | ------- | ---------------- | ----------- | ---------------------------------------------------- |
| FCN [54]  | 2015  | VGG-16  | NYVUODCv 22 011  | 34.0        |                                                      |
|           |       |         | PhCN-UY3U7D3 v2  | 92.0334 .0  | semantic segmentation                                |
Encoder–decoder structure,
| U-Net [64]   | 2015  | VGG-16  |                    |              |                                                      |
| ------------ | ----- | ------- | ------------------ | ------------ | ---------------------------------------------------- |
|              |       |         | DICP-hHCe-LUa3 73  | 77.5962 .03  | Ensckoidpe cro–ndneecoctdioern ss tructure,          |
| U-Net [64]   | 2015  | VGG-16  |                    |              |                                                      |
|              |       |         | CaDmIVCi-dH eLa    | 60.747 .56   | Transferreds kthipe  cmoanxn-epcotioolninsg  in-     |
| SegNet [61]  | 2016  | VGG-16  |                    |              |                                                      |
|              |       |         | SUN CRaGmBVDi d    | 28.2670 .4   | Tradniscfeesr rtoed th teh ed mecaoxd-epro oling in- |
| SegNet [61]  | 2016  | VGG-16  |                    |              |                                                      |
|              |       |         | SUN RGBD           | 28.27        | dices to the decoder                                 |

Electronics2023,12,1199 18of24
Table2.Comparisonandanalysisofsemanticsegmentationmethodsbasedondeeplearning.
Experiments
| Algorithms | Pub.Year | Backbone |          |         | MajorContributions |
| ---------- | -------- | -------- | -------- | ------- | ------------------ |
|            |          |          | Datasets | mIoU(%) |                    |
PASCAL
|               |      |        |          | 62.7  | Theforerunnerforend-to-end |
| ------------- | ---- | ------ | -------- | ----- | -------------------------- |
| FCN[54]       |      |        | VOC2011  |       |                            |
|               | 2015 | VGG-16 |          |       | semanticsegmentation       |
|               |      |        | NYUDv2   | 34.0  |                            |
|               |      |        | PhC-U373 | 92.03 | Encoder–decoderstructure,  |
| U-Net[64]     | 2015 | VGG-16 |          |       | skipconnections            |
|               |      |        | DIC-HeLa | 77.56 |                            |
|               |      |        | CamVid   | 60.4  | Transferredthemax-pooling  |
| SegNet[61]    | 2016 | VGG-16 |          |       |                            |
|               |      |        | SUNRGBD  | 28.27 | indicestothedecoder        |
|               |      |        | PASCAL   |       | Atrousconvolution,fully    |
| DeepLabv1[65] | 2016 | VGG-16 |          | 71.6  |                            |
|               |      |        | VOC2012  |       | connectedCRFs              |
Dilatedconvolutions,multi-scale
PASCAL
| MSCA[88] | 2016 | VGG-16 |     | 75.3 | contextaggregation,front-end |
| -------- | ---- | ------ | --- | ---- | ---------------------------- |
VOC2012
contextmodule
PASCAL
Reconstructionup-sampling
77.5
| LRR[73] | 2016 | ResNet/VGG-16 | VOC2011 |     | module,Laplacian |
| ------- | ---- | ------------- | ------- | --- | ---------------- |
pyramidrefinement
|           |      |              | Cityscapes | 69.7 |                      |
| --------- | ---- | ------------ | ---------- | ---- | -------------------- |
|           |      |              | CamVid     | 91.6 |                      |
|           |      |              | Oxford     |      | ExtensionofReNetto   |
| ReSeg[79] | 2016 | VGG-16&ReNet |            | 93.7 |                      |
|           |      |              | Flowers    |      | semanticsegmentation |
|           |      |              | CamVid     | 58.8 |                      |
ModifiedConv4/5ofResNet,
| DRN[70] | 2017 | ResNet-101 | Cityscapes | 70.9 |     |
| ------- | ---- | ---------- | ---------- | ---- | --- |
dilatedconvolution
PASCAL
85.4
VOC2012
| PSPNet[72] | 2017 | ResNet50 |            |      | Spatialpyramidpooling(SPP) |
| ---------- | ---- | -------- | ---------- | ---- | -------------------------- |
|            |      |          | Cityscapes | 80.2 |                            |
PASCAL
|               |      | VGG-16/ |         | 79.7 | Atrousspatialpyramidpooling |
| ------------- | ---- | ------- | ------- | ---- | --------------------------- |
| DeepLabV2[66] | 2017 |         | VOC2012 |      |                             |
(ASPP),fullyconnectedCRFs
ResNet-101
|     |     |     | Cityscapes | 70.4 |     |
| --- | --- | --- | ---------- | ---- | --- |
PASCAL
86.9
VOC2012
| DeepLabV3[67] | 2017 | ResNet-101 |            |      | CascadedorparallelASPPmodules |
| ------------- | ---- | ---------- | ---------- | ---- | ----------------------------- |
|               |      |            | Cityscapes | 81.3 |                               |
PASCAL
|                |      |          |         | 89.0 | Anewencoder–decoderstructure |
| -------------- | ---- | -------- | ------- | ---- | ---------------------------- |
| DeepLabV3+[68] | 2018 | Xception | VOC2012 |      |                              |
withDeepLabV3asanencoder
|     |     |     | Cityscapes | 82.1 |     |
| --- | --- | --- | ---------- | ---- | --- |
PASCAL
|             |      |         |         | 83.1 | HDC(hybriddilationconvolution) |
| ----------- | ---- | ------- | ------- | ---- | ------------------------------ |
|             |      | ResNet- | VOC2012 |      |                                |
| DUC-HDC[62] | 2018 |         |         |      | wasproposedtosolvethegridding  |
101/ResNet-152
|     |     |     | Cityscapes | 80.1 | causedbydilatedconvolutions |
| --- | --- | --- | ---------- | ---- | --------------------------- |
multi-class
|                    |      |         | abdominal | –   |                                 |
| ------------------ | ---- | ------- | --------- | --- | ------------------------------- |
|                    |      | VGG-16  |           |     | Anovelself-attentiongating(AGs) |
| AttentionU-Net[83] | 2018 |         | CT-150    |     |                                 |
|                    |      | withAGs |           |     | filter,skipconnections          |
TCIAPancreas
–
CT-82

Electronics2023,12,1199 19of24
Table2.Cont.
Experiments
| Algorithms | Pub.Year | Backbone |          |         | MajorContributions |
| ---------- | -------- | -------- | -------- | ------- | ------------------ |
|            |          |          | Datasets | mIoU(%) |                    |
|            |          |          | ADE20K   | 81.51   |                    |
Point-wisespatialattentionmaps
|            |      |            | PASCAL  |      | fromtwoparallelbranches, |
| ---------- | ---- | ---------- | ------- | ---- | ------------------------ |
| PSANet[85] | 2018 | ResNet-101 |         | 85.7 |                          |
|            |      |            | VOC2012 |      | bi-directioninformation  |
propagationmodel
|     |     |     | Cityscapes | 81.4 |     |
| --- | --- | --- | ---------- | ---- | --- |
PASCAL
84.2
VOC2012
Multi-scale,global-guidedlocal
PASCAL
APCNet[75] 2019 ResNet-101 54.7 affinity(GLA),adaptivecontext
|     |     |     | Context    |       | modules(ACMs) |
| --- | --- | --- | ---------- | ----- | ------------- |
|     |     |     | ADE20K     | 45.38 |               |
|     |     |     | Cityscapes | 81.5  |               |
PASCALVOC
82.6
|           |      |            | 2012 |     | Dualattention:positionattention |
| --------- | ---- | ---------- | ---- | --- | ------------------------------- |
| DANet[86] | 2019 | ResNet-101 |      |     | moduleandchannel                |
PASCAL
52.6
attentionmodule
Context
|     |     |     | COCOStuff | 39.7 |     |
| --- | --- | --- | --------- | ---- | --- |
Pyramidpoolingmodule(PPM),
CARAFE[87] 2019 ResNet-50 ADE20k 42.23 featurepyramidnetwork(FPN),
multi-levelfeaturefusion(FUSE)
PASCAL
86.4
VOC2012
PPM,multi-scalefeaturefusion
| EFPN[76] | 2021 | VGG-16 | Cityscapes | 82.3 |     |
| -------- | ---- | ------ | ---------- | ---- | --- |
modulewithaparallelbranch
PASCAL
53.9
Context
PPM,FPN,FUSE,adaptivekernels
| CARAFE++[88] | 2021 | ResNet-101 | ADE20k | 43.94 |     |
| ------------ | ---- | ---------- | ------ | ----- | --- |
on-the-fly
Anovelshiftedwindowingscheme,
SwinTransformer
|     | 2021 | Swin-L | Swin-L | 53.5 | ageneralbackbonenetworkfor |
| --- | ---- | ------ | ------ | ---- | -------------------------- |
[93]
computervision
Skipconnections,
anintermediatelayerthatcombines
| AttentionUW-Net |      |          | NIHChest |     | thefeaturemapsofthefourth-layer |
| --------------- | ---- | -------- | -------- | --- | ------------------------------- |
|                 | 2022 | ResNet50 |          | –   |                                 |
| [84]            |      |          | X-ray    |     | encoderwiththefeaturemapsof     |
thelast-layerencoderlayer,
attentionmechanism
BilateraldirectionalFPN,
|     |     |     | Cityscapes | 75.9 |     |
| --- | --- | --- | ---------- | ---- | --- |
lightweightASPP,featurepyramid
| FPANet[77] | 2022 | ResNet18 |     |     |     |
| ---------- | ---- | -------- | --- | --- | --- |
fusionmodule(FPFM),border
|     |                |     | CamVid | 74.7 | refinementmodule(BRM) |
| --- | -------------- | --- | ------ | ---- | --------------------- |
|     | 5. Conclusions |     |        |      |                       |
According to the chronological evolution of image segmentation technology, we
havecomprehensivelysortedtheclassicsegmentationalgorithmsandthecurrentpopular
deeplearningalgorithms,elaboratedontherepresentativesolutionsofeachstage,and
enumeratedtheclassicalgorithmswithcertaininfluences. Ingeneral,thedevelopment
ofimagesegmentationshowsatrendfromcoarse-grainedtofine-grained,frommanual
featureextractiontoadaptivelearning,andfromsingle-image-orientedtosegmentation
basedoncommonfeaturesofbigdata.

Electronics2023,12,1199 20of24
Withthedevelopmentofimageacquisitiontechnology,thetypesofimagesarebe-
comingmorevaried, thatbringsmorechallengesinimagesegmentationwithdifferent
dimensions,scales,resolutions,andimagingmodes. Researchersexpecttheuseofagen-
eralnetworkwithimprovedadaptabilityandgeneralizationability[94]. SincetheFCN
was proposed, deep neural network research has shown obvious advantages in scene
understandingandobjectrecognition. Futureresearchdirectionsstillfocusondeepneural
networks, aiming to further improve the accuracy, real-time ability, and robustness of
thenetwork. Withthegreatbreakthroughmadebytheswintransformerinthefieldof
computervisionin2021,imagesegmentationhasenteredthetransformerstagefromthe
CNNstage, andthetransformermaybringnewadvancestocomputervisionresearch.
Nevertheless,deeplearningalsohasitsshortcomings,e.g.,deeplearningisinexplicable,
whichlimitstherobustness,reliability,andperformanceoptimizationofitsdownstream
tasks. Thecurrentresearchdirectionsandchallengesofimagesegmentationareasfollows:
1. Semanticsegmentation,instancesegmentation,andpanoramicsegmentationarestill
the research hotspots of image segmentation. Instance segmentation predicts the
pixel regions contained in each instance; panoramic segmentation integrates both
semanticsegmentationandinstancesegmentation,andassignsacategorylabeland
an instance ID to each pixel of the image. Especially in panoramic segmentation,
countable,oruncountableinstancesaredifficulttorecognizeinasingleworkflow,so
itisachallengingtasktobuildaneffectivenetworktosimultaneouslyidentifyboth
largeinter-categorydifferencesandsmallintra-categorydifferences;
2. Withthepopularizationofimageacquisitionequipment(e.g.,LiDARcameras),RGB-
depth,3D-pointclouds,voxels,andmeshsegmentationhavegraduallybecomere-
searchhotspots,whichhaveawiderequirementinfacerecognition[95],autonomous
vehicles,VR,AR,architecturalmodeling,etc. Althoughtherehasbeensomeprogress
intheresearchof3Dimagesegmentation,e.g.,regiongrowth,randomwalks,and
clusteringinclassicalgorithms,andSVM,randomforest,andAdaBoostinmachine
learningalgorithms,therepresentationandprocessingof3Ddata,whichareunstruc-
tured,redundant,disordered,andunevenlydistributed,remainamajorchallenge;
3. Insomefields,itisdifficulttousesupervisedlearningalgorithmstotrainthenetwork
duetoalackofdatasetsorfine-grainedannotations. Semi-supervisedandunsuper-
visedsemanticsegmentationcanbeselectedinthesecases,wherethenetworkcanbe
trainedonthebenchmarkdatasetfirst,andthelower-levelparametersofthenetwork
canthenbefixed,andthefullyconnectedlayerorsomehigh-levelparameterscanbe
trainedonthesmall-sampledataset. Thisistransferlearning,thatdoesnotrequire
abundantlabeledsamples. Reinforcementlearningisalsoapossiblesolution, but
itisrarelystudiedinthefieldofimagesegmentation. Inaddition,few-shotimage
semanticsegmentationisalsoahotresearchdirection;
4. Deep learning networks require a significant amount of computing resources in
thetrainingprocess,thatalsoillustratesthecomputationalcomplexityofthedeep
neuralnetwork. Real-time(ornearreal-time)segmentationisrequiredinmanyfields,
e.g., videoprocessingtomeetthehumanvisionmechanismofatleast25fps, and
most current networks are far below this frame rate. Some lightweight networks
have improved the speed of the segmentation to a certain extent, but there is still
a large amount of room for improvement in the balance of model accuracy and
real-timeperformance.
AuthorContributions:Conceptualization,C.W.andQ.F.;methodology,C.W.andQ.F.;investigation,
R.K.andF.H.;resources,Q.F.;datacuration,B.Y.,T.Y.andM.G.;writing—originaldraftpreparation,
Y.Y.;writing—reviewandediting,Y.Y.andC.W.;supervision,Q.F.andM.G.;projectadministration,
C.W.andQ.F.;fundingacquisition,Q.F.andF.H.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.

Electronics2023,12,1199 21of24
Funding: This research was supported by the National Natural Science Foundation of China
(No. 62171467), the Hainan Provincial Natural Science Foundation of China (No. 621QN270),
andtheSpecificResearchFundofTheInnovationPlatformforAcademiciansofHainanProvince
(No.YSPTZX202144).
DataAvailabilityStatement:Notapplicable.
Acknowledgments:TheauthorsgratefullyacknowledgeDongdongZhang,ChangfengFeng,and
HuiyingWangfortheirfruitfuldiscussions.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Anwesh, K.; Pal, D.; Ganguly, D.; Chatterjee, K.; Roy, S. Number plate recognition from enhanced super-resolution using
generativeadversarialnetwork.Multimed.ToolsAppl.2022,1–17.[CrossRef]
2. Jin,B.;Cruz,L.;Gonçalves,N.DeepFacialDiagnosis:DeepTransferLearningfromFaceRecognitiontoFacialDiagnosis.IEEE
Access2020,8,123649–123661.[CrossRef]
3. Zhao,M.;Liu,Q.;Jha,R.;Deng,R.;Yao,T.;Mahadevan-Jansen,A.;Tyska,M.J.;Millis,B.A.;Huo,Y.VoxelEmbed:3DInstance
SegmentationandTrackingwithVoxelEmbeddingbasedDeepLearning. InProceedingsoftheInternationalWorkshopon
MachineLearninginMedicalImaging,Strasbourg,France,27September2021;Volume12966,pp.437–446.[CrossRef]
4. Yao,T.;Qu,C.;Liu,Q.;Deng,R.;Tian,Y.;Xu,J.;Jha,A.;Bao,S.;Zhao,M.;Fogo,A.B.;etal. CompoundFigureSeparationof
BiomedicalImageswithSideLoss. InProceedingsoftheDeepGenerativeModels,andDataAugmentation,Labelling,and
Imperfections,Strasbourg,France,1October2021;Volume13003,pp.173–183.[CrossRef]
5. Minaee,S.;Boykov,Y.;Porikli,F.;Plaza,A.;Kehtarnavaz,N.;Terzopoulos,D.ImageSegmentationUsingDeepLearning: A
Survey.IEEETrans.PatternAnal.Mach.Intell.2022,44,3523–3542.[CrossRef][PubMed]
6. Zhang,X.;Yao,Q.A.;Zhao,J.;Jin,Z.J.;Feng,Y.C.ImageSemanticSegmentationBasedonFullyConvolutionalNeuralNetwork.
Comput.Eng.Appl.2022,44,45–57.
7. Garcia-Garcia,A.;Orts-Escolano,S.;Oprea,S.;Villena-Martinez,V.;Martinez-Gonzalez,P.;Garcia-Rodriguez,J.Asurveyondeep
learningtechniquesforimageandvideosemanticsegmentation.Appl.SoftComput.2018,70,41–65.[CrossRef]
8. Yu,Y.;Wang,C.;Fu,Q.;Kou,R.;Wu,W.;Liu,T.ASurveyofEvaluationMetricsandMethodsforSemanticSegmentation.Comput.
Eng.Appl.2023;onlinepreprint.
9. Lankton,S.;Tannenbaum,A.LocalizingRegion-BasedActiveContours.IEEETrans.ImageProcess.2008,17,2029–2039.[CrossRef]
10. Freedman,D.;Tao,Z.InteractiveGraphCutbasedSegmentationwithShapePriors.InProceedingsoftheIEEEComputerSociety
ConferenceonComputerVisionandPatternRecognition(CVPR),SanDiego,CA,USA,20–25June2005;Volume1,pp.755–762.
[CrossRef]
11. Felzenszwalb,P.F.;Huttenlocher,D.P.EfficientGraph-BasedImageSegmentation.Int.J.Comput.Vis.2004,59,167–181.[CrossRef]
12. Leordeanu,M.;Hebert,M.ASpectralTechniqueforCorrespondenceProblemsusingPairwiseConstraints.InProceedingsofthe
10thIEEEInternationalConferenceonComputerVision(ICCV’05),Beijing,China,17–21October2005;Volume2,pp.1482–1489.
[CrossRef]
13. Comaniciu,D.;Meer,P.MeanShift:ARobustApproachTowardFeatureSpaceAnalysis.IEEETrans.PatternAnal.Mach.Intell.
2002,24,603–619.[CrossRef]
14. Chuang,K.S.;Tzeng,H.L.;Chen,S.;Wu,J.;Chen,T.J.FuzzyC-meansClusteringwithSpatialInformationforImageSegmentation.
Comput.Med.ImagingGraph.Off.J.Comput.Med.ImagingSoc.2006,30,9–15.[CrossRef]
15. Achanta,R.;Shaji,A.;Smith,K.;Lucchi,A.;Fua,P.;Süsstrunk,S.SLICSuperpixelsComparedtoState-of-the-ArtSu-perpixel
Method.IEEETrans.PatternAnal.Mach.Intell.2012,34,2274–2282.[CrossRef]
16. Li, Z.; Chen, J.SuperpixelSegmentationusingLinearSpectralClustering. InProceedingsofthe2015IEEEConferenceon
ComputerVisionandPatternRecognition(CVPR),Boston,MA,USA,7–12June2015;pp.1356–1363.[CrossRef]
17. Pan,W.;Lu,X.Q.;Gong,Y.H.;Tang,W.M.;Liu,J.;He,Y.;Qiu,G.P.HLO:Half-kernelLaplacianOperatorforSur-faceSmoothing.
Comput.AidedDes.2020,121,102807.[CrossRef]
18. Chen,H.B.;Zhen,X.;Gu,X.J.;Yan,H.;Cervino,L.;Xiao,Y.;Zhou,L.H.SPARSE:SeedPointAuto-GenerationforRandomWalks
SegmentationEnhancementinmedicalinhomogeneoustargetsdelineationofmorphologicalMRandCTimages.J.Appl.Clin.
Med.Phys.2015,16,387–402.[CrossRef][PubMed]
19. Drouyer,S.;Beucher,S.;Bilodeau,M.;Moreaud,M.;Sorbier,L.SparseStereoDisparityMapDensificationusingHierarchical
ImageSegmentation.InMathematicalMorphologyandItsApplicationstoSignalandImageProcessing;LectureNotesinComputer
Science;Springer:Berlin/Heidelberg,Germany,2017;Volume1022.[CrossRef]
20. Grady, L.RandomWalksforImageSegmentation. IEEETrans. PatternAnal. Mach. Intell. 2006, 28, 1768–1783. [CrossRef]
[PubMed]
21. Yang,W.;Cai,J.;Zheng,J.;Luo,J.User-FriendlyInteractiveImageSegmentationThroughUnifiedCombinatorialUserInputs.
IEEETrans.ImageProcess.2010,19,2470–2479.[CrossRef][PubMed]

Electronics2023,12,1199 22of24
22. Lai,Y.K.;Hu,S.M.;Martin,R.R.;Rosin,P.L.FastMeshSegmentationusingRandomWalks. InProceedingsofthe2008ACM
SymposiumonSolidandPhysicalModeling,NewYork,NY,USA,2June2008;pp.183–191.[CrossRef]
23. Zhang,J.;Wu,C.;Cai,J.;Zheng,J.;Tai,X.MeshSnapping:RobustInteractiveMeshCuttingusingFastGeodesicCurvatureFlow.
Comput.Graph.Forum2010,29,517–526.[CrossRef]
24. Rother,C.;Minka,T.P.;Blake,A.;Kolmogorov,V.CosegmentationofImagePairsbyHistogramMatching—IncorporatingaGlobal
ConstraintintoMRFs.InProceedingsoftheIEEEComputerSocietyConferenceonComputerVisionandPatternRecognition
(CVPR),NewYork,NY,USA,17–22June2006;pp.993–1000.[CrossRef]
25. Vicente,S.;Kolmogorov,V.;Rother,C.CosegmentationRevisited:ModelsandOptimization.LectureNotesinComputerScience.
InProceedingsoftheComputerVision(ECCV),Crete,Greece,5–11September2010;pp.465–479.[CrossRef]
26. Mukherjee,L.;Singh,V.;Dyer,C.R.Half-integrality-basedAlgorithmsforCosegmentationofImages.InProceedingsoftheIEEE
ConferenceonComputerVisionandPatternRecognition(CVPR),Miami,FL,USA,20–25June2009;pp.2028–2035.[CrossRef]
27. Hochbaum,D.S.;Singh,V.AnEfficientAlgorithmforCo-segmentation.InProceedingsofthe12thIEEEInternationalCon-ference
onComputerVision(ICCV),Kyoto,Japan,29September–2October2009;pp.269–276.[CrossRef]
28. Rubio,J.C.;Serrat,J.;López,A.;Paragios,N.UnsupervisedCo-segmentationthroughRegionMatching.InProceedingsofthe
2012IEEEConferenceonComputerVisionandPatternRecognition(CVPR),Providence,RI,USA,16–21June2012;pp.749–756.
[CrossRef]
29. Chang,K.;Liu,T.;Lai,S.FromCo-saliencytoCo-segmentation: AnEfficientandFullyUnsupervisedEnergyMinimization
Model.InProceedingsofthe24thIEEEConferenceonComputerVisionandPatternRecognition(CVPR),ColoradoSprings,CO,
USA,20–25June2011;pp.2129–2136.[CrossRef]
30. Yu,H.;Xian,M.;Qi,X.UnsupervisedCo-segmentationbasedonaNewGlobalGMMConstraintinMRF.InProceedingsofthe
IEEEInternationalConferenceonImageProcessing(ICIP),Paris,France,27–30October2014;pp.4412–4416.[CrossRef]
31. Wang,C.;Guo,Y.;Zhu,J.;Wang,L.;Wang,L.VideoObjectCo-SegmentationviaSubspaceClusteringandQuadraticPseudo-
BooleanOptimizationinanMRFFramework.IEEETrans.Multimed.2014,16,903–916.[CrossRef]
32. Zhu,J.;Wang,L.;Gao,J.;Yang,R.Spatial-TemporalFusionforHighAccuracyDepthMapsusingDynamicMRFs.IEEETrans.
PatternAnal.Mach.Intell.2010,32,899–909.[CrossRef]
33. Collins,M.D.;Xu,J.;Grady,L.;Singh,V.RandomWalksbasedMulti-imageSegmentation:QuasiconvexityResultsandGPU-
basedSolutions.InProceedingsofthe2012IEEEConferenceonComputerVisionandPatternRecognition,Providence,RI,USA,
16–21June2012;pp.1656–1663.[CrossRef]
34. Fabijanska,A.;Goclawski,J.TheSegmentationof3DImagesusingtheRandomWalkingTechniqueonaRandomlyCreated
ImageAdjacencyGraph.IEEETrans.ImageProcess.2015,24,524–537.[CrossRef]
35. Dong,X.P.;Shen,J.B.;Shao,L.;Gool,L.V.Sub-MarkovRandomWalkforImageSegmentation.IEEETrans.ImageProcess.2016,25,
516–527.[CrossRef]
36. Zhou,J.;Wang,W.M.;Zhang,J.;Yin,B.C.;Liu,X.P.3Dshapesegmentationusingmultiplerandomwalkers. J.Comput. Appl.
Math.2018,329,353–363.[CrossRef]
37. Dong,C.;Zeng,X.;Lin,L.;Hu,H.;Han,X.;Naghedolfeizi,M.;Aberra,D.;Chen,Y.W.AnImprovedRandomWalkerwithBayes
ModelforVolumetricMedicalImageSegmentation.J.Healthc.Eng.2017,2017,6506049.[CrossRef][PubMed]
38. Meng,F.;Li,H.;Liu,G.ImageCo-segmentationviaActiveContours.InProceedingsofthe2012IEEEInternationalSymposium
onCircuitsandSystems(ISCAS),Seoul,RepublicofKorea,20–23May2012;pp.2773–2776.[CrossRef]
39. Zhang,T.;Xia,Y.;Feng,D.D.ADeformableCosegmentationAlgorithmforBrainMRImages. InProceedingsoftheAnnual
InternationalConferenceoftheIEEEEngineeringinMedicineandBiologySociety,SanDiego,CA,USA,28August–1September
2012;pp.3215–3218.[CrossRef]
40. Zhang,Z.;Liu,X.;Soomro,N.Q.;Abou-El-Hossein,K.AnEfficientImageCo-segmentationAlgorithmbasedonActiveContour
andImageSaliency. InProceedingsofthe20167thInternationalConferenceonMechanical,Industrial,andManufacturing
Technologies(MIMT2016),CapeTown,SouthAfrica,1–3February2016;Volume54,p.08004.[CrossRef]
41. Joulin,A.;Bach,F.;Ponce,J.DiscriminativeClusteringforImageCo-segmentation.InProceedingsofthe2010IEEEComputer
SocietyConferenceonComputerVisionandPatternRecognition(CVPR),SanFrancisco,CA,USA,13–18June2010;pp.1943–1950.
[CrossRef]
42. Kim,E.;Li,H.;Huang,X.AHierarchicalImageClusteringCosegmentationFramework.InProceedingsoftheIEEEComputer
SocietyConferenceonComputerVisionandPatternRecognition(CVPR),Providence,RI,USA,16–21June2012;pp.686–693.
[CrossRef]
43. Joulin,A.;Bach,F.;Ponce,J.Multi-classCosegmentation.InProceedingsofthe2012IEEEConferenceonComputerVisionand
PatternRecognition(CVPR),Providence,RI,USA,16–21June2012;pp.542–549.[CrossRef]
44. Meng,F.;Li,H.;Liu,G.;Ngan,K.N.ObjectCo-SegmentationBasedonShortestPathAlgorithmandSaliencyModel.IEEETrans.
Multimed.2012,14,1429–1441.[CrossRef]
45. Meng, F.M.; Li, H.; Liu, G.H. A New Co-saliency Model via Pairwise Constraint Graph Matching. In Proceedings of the
InternationalSymposiumonIntelligentSignalProcessingandCommunicationsSystems,Tamsui,Taiwan,4–7November2012;
IEEEComputerSocietyPress:LosAlamitos,CA,USA,2012;pp.781–786.[CrossRef]

Electronics2023,12,1199 23of24
46. Kim,G.;Xing,E.P.;Li,F.F.;Kanade,T.DistributedCosegmentationviaSubmodularOptimizationonAnisotropicDiffusion.In
Proceedingsofthe2011InternationalConferenceonComputerVision,Barcelona,Spain,6–13November2011;pp. 169–176.
[CrossRef]
47. Kim,G.;Xing,E.P.OnMultipleForegroundCosegmentation.InProceedingsofthe2012IEEEConferenceonComputerVision
andPatternRecognition,Providence,RI,USA,16–21June2012;pp.837–844.[CrossRef]
48. Alexe,B.;Deselaers,T.;Ferrari,V.WhatIsanObject?InProceedingsofthe2010IEEEComputerSocietyConferenceonComputer
VisionandPatternRecognition,SanFrancisco,CA,USA,13–18June2010;pp.73–80.[CrossRef]
49. Vicente,S.;Rother,C.;Kolmogorov,V.Objectcosegmentation. InProceedingsoftheIEEEComputerSocietyConferenceon
ComputerVisionandPatternRecognition(CVPR),ColoradoSprings,CO,USA,20–25June2011.[CrossRef]
50. Meng,F.;Cai,J.;Li,H.CosegmentationofMultipleImageGroups.Comput.Vis.ImageUnderst.2016,146,67–76.[CrossRef]
51. Johnson,M.;Shotton,J.;Cipolla,R.SemanticTextonForestsforImageCategorizationandSegmentation.InDecisionForestsfor
ComputerVisionandMedicalImageAnalysis,AdvancesinComputerVisionandPatternRecognition;Criminisi,A.,Shotton,J.,Eds.;
Springer:London,UK,2013.[CrossRef]
52. Lindner,C.;Thiagarajah,S.;Wilkinson,J.M.;ThearcOGENConsortium;Wallis,G.A.;Cootes,T.F.FullyAutomaticSegmentation
oftheProximalFemurusingRandomForestRegressionVoting.IEEETrans.Med.Imaging2013,32,1462–1472.[CrossRef]
53. Li,H.S.; Zhao,R.; Wang,X.G.HighlyEfficientForwardandBackwardPropagationofConvolutionalNeuralNetworksfor
PixelwiseClassification.arXiv2014,arXiv:1412.4526.
54. Long,J.;Shelhamer,E.;Darrell,T.FullyConvolutionalNetworksforSemanticSegmentation.IEEETrans.PatternAnal.Mach.
Intell2017,39,640–651.[CrossRef]
55. Lecun,Y.;Bottou,L.;Bengio,Y.;Haffner,P.Gradient-basedLearningAppliedtoDocumentRecognition. Proc. IEEE1998,86,
2278–2324.[CrossRef]
56. Krizhevsky,A.;Sutskever,I.;Hinton,G.E.ImageNetClassificationwithDeepConvolutionalNeuralNetworks.Commun.ACM
2017,60,84–90.[CrossRef]
57. Karen,S.;Andrew,Z.VeryDeepConvolutionalNetworksforLarge-ScaleImageRecognition.arXiv2014,arXiv:1409.1556.
58. Szegedy,C.;Liu,W.;Jia,Y.Q.;Sermanet,P.;Reed,S.;Anguelov,D.;Erhan,D.;Vanhoucke,V.;Rabinovich,A.GoingDeeperwith
Convolutions.InProceedingsofthe2015IEEEConferenceonComputerVisionandPatternRecognition(CVPR),Boston,MA,
USA,7–12June2015;pp.1–9.[CrossRef]
59. Szegedy,C.;Vanhoucke,V.;Ioffe,S.;Shlens,J.;Wojna,Z.RethinkingtheInceptionArchitectureforComputerVisio.InProceedings
ofthe2016IEEEConferenceonComputerVisionandPatternRecognition(CVPR),LasVegas,NV,USA,27–30June2016;pp.
2818–2826.[CrossRef]
60. He, K.M.; Zhang, X.Y.; Ren, S.Q.; Sun, J.Deep Residual Learningfor Image Recognition. In Proceedings ofthe 2016 IEEE
ConferenceonComputerVisionandPatternRecognition(CVPR),LasVegas,NV,USA,27–30June2016;pp.770–778.[CrossRef]
61. Badrinarayanan, V.; Kendall, A.; Cipolla, R. SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Seg-
mentation.IEEETrans.PatternAnal.Mach.Intell.2017,39,2481–2495.[CrossRef]
62. Wang,P.;Chen,P.;Yuan,Y.;Liu,D.;Huang,Z.H.;Hou,X.D.;Cottrell,G.UnderstandingConvolutionforSemanticSegmentation.
InProceedingsofthe2018IEEEWinterConferenceonApplicationsofComputerVision(WACV),LakeTahoe,NV,USA,12–15
March2018;pp.1451–1460.[CrossRef]
63. Huang,G.;Liu,Z.;VanDerMaaten,L.;Weinberger,K.DenselyConnectedConvolutionalNetworks.InProceedingsofthe2017
IEEEConferenceonComputerVisionandPatternRecognition(CVPR),Honolulu,HI,USA,21–26July2017;pp. 2261–2269.
[CrossRef]
64. Ronneberger, O.; Fischer, P.; Brox, T. U-Net: Convolutional Networks for Biomedical Image Segmentation. arXiv 2015,
arXiv:1505.04597.
65. Chen,L.C.;Papandreou,G.;Kokkinos,I.;Murphy,K.;Yuille,A.L.SemanticImageSegmentationwithDeepConvolutionalNets
andFullyConnectedCRFs.arXiv2014,arXiv:1412.7062.[CrossRef]
66. Chen,L.C.;Papandreou,G.;Kokkinos,I.;Murphy,K.;Yuille,A.L.DeepLab:SemanticImageSegmentationwithDeepConvolu-
tionalNets,AtrousConvolution,andFullyConnectedCRFs.arXiv2017,arXiv:1606.00915.[CrossRef][PubMed]
67. Chen,L.C.;Papandreou,G.;Schroff,F.;Adam,H.RethinkingAtrousConvolutionforSemanticImageSegmentation.arXiv2017,
arXiv:1706.05587.
68. Chen,L.C.;Zhu,Y.;Papandreou,G.;Schroff,F.;Adam,H.Encoder-DecoderwithAtrousSeparableConvolutionforSemantic
ImageSegmentation.ProceedingoftheEuropeanconferenceoncomputervision(ECCV).arXiv2018,arXiv:1802.02611.
69. Yu,F.;Koltun,V.Multi-ScaleContextAggregationbyDilatedConvolutions.arXiv2015,arXiv:1511.07122.[CrossRef]
70. Yu,F.;Koltun,V.;Funkhouser,T.DilatedResidualNetworks.InProceedingsofthe2017IEEEConferenceonComputerVision
andPatternRecognition(CVPR),Honolulu,HI,USA,21–26July2017;pp.636–644.[CrossRef]
71. He,K.;Zhang,X.;Ren,S.;Sun,J.SpatialPyramidPoolinginDeepConvolutionalNetworksforVisualRecognition.IEEETrans.
PatternAnal.Mach.Intell.2015,37,1904–1916.[CrossRef]
72. Zhao,H.S.;Shi,J.P.;Qi,X.J.;Jia,J.Y.PyramidSceneParsingNetwork.arXiv2017,arXiv:1612.01105v2.[CrossRef]
73. Ghiasi,G.;Fowlkes,C.LaplacianPyramidReconstructionandRefinementforSemanticSegmentation.InProceedingsofthe
EuropeanConferenceonComputerVision(ECCV),Amsterdam,TheNetherlands,11–14October2016.[CrossRef]

Electronics2023,12,1199 24of24
74. Lin,T.Y.;Dollar,P.;Girshick,R.;He,K.;Hariharan,B.;Belongie,S.FeaturePyramidNetworksforObjectDetection.arXiv2017,
arXiv:1612.03144.32.
75. He,J.;Deng,Z.;Zhou,L.;Wang,Y.;Qiao,Y.AdaptivePyramidContextNetworkforSemanticSegmentation.InProceedingsof
the2019IEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR),LongBeach,CA,USA,15–20June2019;
pp.7511–7520.[CrossRef]
76. Ye,M.;Ouyang,J.;Chen,G.;Zhang,J.;Yu,X.EnhancedFeaturePyramidNetworkforSemanticSegmentation.InProceedingsof
the25thInternationalConferenceonPatternRecognition(ICPR),Milan,Italy,10–15January2021;pp.3209–3216.[CrossRef]
77. Wu,Y.;Jiang,J.;Huang,Z.;Tian,Y.FPANet:Featurepyramidaggregationnetworkforreal-timesemanticsegmentation.Appl.
Intell.2022,52,3319–3336.[CrossRef]
78. Mnih,V.;Heess,N.;Graves,A.;Kavukcuoglu,K.RecurrentModelsofVisualAttention.InProceedingsofthe27thInternational
Conference on Neural Information Processing Systems (NIPS’14), Montreal, QC, Canada, 8–13 December 2014; Volume 2,
pp.2204–2212.
79. Visin,F.;Romero,A.;Cho,K.;Matteucci,M.;Ciccone,M.;Kastner,K.;Bengio,Y.;Courville,A.ReSeg: ARecurrentNeural
Network-BasedModelforSemanticSegmentation.arXiv2015,arXiv:1511.07053.
80. Visin,F.;Kastner,K.;Cho,K.;Matteucci,M.;Courville,A.;Bengio,Y.ReNet:ARecurrentNeuralNetworkBasedAlternativeto
ConvolutionalNetworks.arXiv2015,arXiv:1505.00393.
81. Byeon, W.; Breuel, T.M.; Raue, F.; Liwicki, M.ScenelabelingwithLSTMrecurrentneuralnetworks. InProceedingsofthe
2015IEEEConferenceonComputerVisionandPatternRecognition(CVPR),Boston,MA,USA,7–12June2015;pp.3547–3555.
[CrossRef]
82. Liang,X.;Shen,X.;Feng,J.;Lin,L.;Yan,S.SemanticObjectParsingwithGraphLSTM.InComputerVision—ECCV2016,Lecture
NotesinComputerScience;Leibe,B.,Matas,J.,Sebe,N.,Welling,M.,Eds.;Springer: Cham,Switzerland,2016;Volume9905.
[CrossRef]
83. Oktay,O.;Schlemper,J.;Folgoc,L.;Lee,M.;Heinrich,M.P.;Misawa,K.;Mori,K.;McDonagh,S.;Hammerla,N.;Kainz,B.;etal.
AttentionU-Net:LearningWheretoLookforthePancreas.arXiv2018,arXiv:1804.03999.
84. Pal,D.;Reddy,P.B.;Roy,S.AttentionUW-Net: Afullyconnectedmodelforautomaticsegmentationandannotationofchest
X-ray.Comput.Biol.Med.2022,150,106083.[CrossRef][PubMed]
85. Zhao,H.;Zhang,Y.;Liu,S.;Shi,J.;Loy,C.C.;Lin,D.;Jia,J.PSANet:Point-wiseSpatialAttentionNetworkforSceneParsing.In
Proceedingsofthe15thEuropeanConference,Munich,Germany,8–14September2018.[CrossRef]
86. Fu,J.;Liu,J.;Tian,H.;Fang,Z.;Lu,H.DualAttentionNetworkforSceneSegmentation.InProceedingsofthe2019IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), Long Beach, CA, USA, 15–20 June 2019; pp. 3141–3149.
[CrossRef]
87. Wang,J.;Chen,K.;Xu,R.;Liu,Z.;Loy,C.C.;Lin,D.CARAFE:Content-AwareReAssemblyofFEatures.InProceedingsofthe
2019IEEE/CVFInternationalConferenceonComputerVision(ICCV),Seoul,RepublicofKorea,27October–2November2019;
pp.3007–3016.[CrossRef]
88. Wang,J.;Chen,K.;Xu,R.;Liu,Z.;Loy,C.C.;Lin,D.CARAFE++:UnifiedContent-AwareReAssemblyofFEatures.IEEETrans.
PatternAnal.Mach.Intell.2021,44,4674–4687.[CrossRef]
89. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I.AttentionisAllYouNeed.In
Proceedingsofthe31stInternationalConferenceonNeuralInformationProcessingSystems,RedHook,NY,USA,4–9December
2017;pp.6000–6010.
90. Weissenborn,D.;Täckström,O.;Uszkoreit,J.ScalingAutoregressiveVideoModels.arXiv2020,arXiv:1906.02634.
91. Cordonnier, J.B.; Loukas, A.; Jaggi, M. On the Relationship between Self-Attention and Convolutional Layers. arXiv 2020,
arXiv:1911.03584.
92. Dosovitskiy,A.;Beyer,L.;Kolesnikov,A.;Weissenborn,D.;Zhai,X.;Unterthiner,T.;Dehghani,M.;Minderer,M.;Heigold,G.;
Gelly,S.;etal.AnImageisWorth16×16Words:TransformersforImageRecognitionatScale.InProceedingsoftheInternational
ConferenceonLearningRepresentations(ICLR),Virtual,3–7May2021.[CrossRef]
93. Liu,Z.;Lin,Y.;Cao,Y.;Hu,H.;Wei,Y.;Zhang,Z.;Lin,S.;Guo,B.SwinTransformer: HierarchicalVisionTransformerusing
ShiftedWindows.arXiv2021,arXiv:2103.14030.
94. Zheng,Q.;Yang,M.;Yang,J.;Zhang,Q.;Zhang,X.ImprovementofGeneralizationAbilityofDeepCNNviaImplicitRegulariza-
tioninTwo-StageTrainingProcess.IEEEAccess2018,6,15844–15869.[CrossRef]
95. Jin,B.;Cruz,L.;Gonçalves,N.PseudoRGB-DFaceRecognition.IEEESens.J.2022,22,21780–21794.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
