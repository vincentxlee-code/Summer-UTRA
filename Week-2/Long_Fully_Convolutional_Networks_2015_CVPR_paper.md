|     |     | Fully | Convolutional |     |     | Networks |                | for Semantic |               | Segmentation |     |     |     |     |
| --- | --- | ----- | ------------- | --- | --- | -------- | -------------- | ------------ | ------------- | ------------ | --- | --- | --- | --- |
|     |     |       | JonathanLong∗ |     |     |          | EvanShelhamer∗ |              | TrevorDarrell |              |     |     |     |     |
UCBerkeley
{jonlong,shelhamer,trevor}@cs.berkeley.edu
|     |     |     | A b s t | ra c t |     |     |     |     |     |      |                       |                    |     | io n ntation g.t. |
| --- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- | ---- | --------------------- | ------------------ | --- | ----------------- |
|     |     |     |         |        |     |     |     |     |     | fo r | w a r d / in f e re n | c e pixelwise pred | i   | c t               |
e
g m
Convolutionalnetwor ks a r e po w erfulvisualmodelsthat b a c k w a r d /l e a r n in g s e
| yield hierarchies |     | of             | features. | We      | show        | that | convolu- |     |     |     |     |     |     |     |
| ----------------- | --- | -------------- | --------- | ------- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
| tional networks   |     | by themselves, |           | trained | end-to-end, |      | pixels-  |     |     |     |     |     |     |     |
to-pixels, exceed the state-of-the-art in semantic segmen- 2564096 409621
|     |     |     |     |     |     |     |     |     |     | 384 | 384 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
256
| tation.               | Our key | insight    | is to  | build          | “fully | convolutional” |         |     |     |     |     |     |     |     |
| --------------------- | ------- | ---------- | ------ | -------------- | ------ | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| networks              | that    | take input | of     | arbitrary      | size   | and            | produce |     | 96  |     |     |     |     |     |
| correspondingly-sized |         |            | output | with efficient |        | inference      | and     |     |     |     |     |     |     |     |
learning. We define and detail the space of fully convolu- 21
tionalnetworks,explaintheirapplicationtospatiallydense Figure 1. Fully convolutional networks can efficiently learn to
makedensepredictionsforper-pixeltaskslikesemanticsegmen-
| predictiontasks,anddrawconnectionstopriormodels. |     |     |     |     |     |     | We  |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tation.
adaptcontemporaryclassificationnetworks(AlexNet[20],
theVGGnet[31],andGoogLeNet[32])intofullyconvolu- We show that a fully convolutional network (FCN)
|                 |     |              |     |               |                 |     |     | trained | end-to-end, | pixels-to-pixels |     | on  | semantic | segmen- |
| --------------- | --- | ------------ | --- | ------------- | --------------- | --- | --- | ------- | ----------- | ---------------- | --- | --- | -------- | ------- |
| tional networks |     | and transfer |     | their learned | representations |     |     |         |             |                  |     |     |          |         |
byfine-tuning[3]tothesegmentationtask.Wethendefinea tation exceeds the state-of-the-art without further machin-
|                   |     |      |          |          |             |     |      | ery. Toourknowledge, |     |     | thisisthefirstworktotrainFCNs |     |     |     |
| ----------------- | --- | ---- | -------- | -------- | ----------- | --- | ---- | -------------------- | --- | --- | ----------------------------- | --- | --- | --- |
| skip architecture |     | that | combines | semantic | information |     | from |                      |     |     |                               |     |     |     |
end-to-end(1)forpixelwisepredictionand(2)fromsuper-
| a deep, | coarse | layer | with appearance |     | information |     | from a |     |     |     |     |     |     |     |
| ------- | ------ | ----- | --------------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
shallow, fine layer to produce accurate and detailed seg- visedpre-training. Fullyconvolutionalversionsofexisting
networkspredictdenseoutputsfromarbitrary-sizedinputs.
mentations.Ourfullyconvolutionalnetworkachievesstate-
of-the-artsegmentationofPASCALVOC(20%relativeim- Bothlearningandinferenceareperformedwhole-image-at-
|     |     |     |     |     |     |     |     | a-time by | dense | feedforward | computation |     | and | backpropa- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----------- | ----------- | --- | --- | ---------- |
provementto62.2%meanIUon2012),NYUDv2,andSIFT
|             |           |     |            |      |           |      |        | gation. In-networkupsamplinglayersenablepixelwisepre- |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | ---- | --------- | ---- | ------ | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Flow, while | inference |     | takes less | than | one fifth | of a | second |                                                       |     |     |     |     |     |     |
foratypicalimage. dictionandlearninginnetswithsubsampledpooling.
|     |     |     |     |     |     |     |     | This | method | is efficient, | both | asymptotically |     | and abso- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ------------- | ---- | -------------- | --- | --------- |
lutely,andprecludestheneedforthecomplicationsinother
1.Introduction works. Patchwisetrainingiscommon[27,2,7,28,9],but
|               |     |          |     |         |          |     |        | lackstheefficiencyoffullyconvolutionaltraining. |     |     |     |     |     | Ourap- |
| ------------- | --- | -------- | --- | ------- | -------- | --- | ------ | ----------------------------------------------- | --- | --- | --- | --- | --- | ------ |
| Convolutional |     | networks | are | driving | advances | in  | recog- |                                                 |     |     |     |     |     |        |
proachdoesnotmakeuseofpre-andpost-processingcom-
| nition. | Convnets | are | not only | improving | for | whole-image |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | -------- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
plications,includingsuperpixels[7,15],proposals[15,13],
| classification[20,31,32], |     |     | butalsomakingprogressonlo- |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orpost-hocrefinementbyrandomfieldsorlocalclassifiers
| caltaskswithstructuredoutput. |     |     |     | Theseincludeadvancesin |     |     |     |          |           |           |        |         |     |                |
| ----------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | -------- | --------- | --------- | ------ | ------- | --- | -------------- |
|                               |     |     |     |                        |     |     |     | [7, 15]. | Our model | transfers | recent | success |     | in classifica- |
bounding box object detection [29, 10, 17], part and key- tion[20,31,32]todensepredictionbyreinterpretingclas-
pointprediction[39,24],andlocalcorrespondence[24,8].
|                |         |            |              |             |          |             |       | sification    | nets as          | fully | convolutional | and       | fine-tuning | from  |
| -------------- | ------- | ---------- | ------------ | ----------- | -------- | ----------- | ----- | ------------- | ---------------- | ----- | ------------- | --------- | ----------- | ----- |
| The            | natural | next step  | in the       | progression |          | from coarse | to    |               |                  |       |               |           |             |       |
|                |         |            |              |             |          |             |       | their learned | representations. |       | In            | contrast, | previous    | works |
| fine inference |         | is to make | a prediction |             | at every | pixel.      | Prior |               |                  |       |               |           |             |       |
haveappliedsmallconvnetswithoutsupervisedpre-training
| approaches | have | used | convnets | for | semantic | segmentation |     |     |     |     |     |     |     |     |
| ---------- | ---- | ---- | -------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[7,28,27].
[27,2,7,28,15,13,9],inwhicheachpixelislabeledwith
|           |        |           |        |            |     |      |        | Semantic | segmentation |     | faces | an inherent |     | tension be- |
| --------- | ------ | --------- | ------ | ---------- | --- | ---- | ------ | -------- | ------------ | --- | ----- | ----------- | --- | ----------- |
| the class | of its | enclosing | object | or region, | but | with | short- |          |              |     |       |             |     |             |
comingsthatthisworkaddresses. tween semantics and location: global information resolves
|     |     |     |     |     |     |     |     | whatwhilelocalinformationresolveswhere. |     |     |     |     |     | Deepfeature |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ----------- |
∗Authorscontributedequally hierarchies encode location and semantics in a nonlinear
1

local-to-global pyramid. We define a skip architecture to [7], and Pinheiro and Collobert [28]; boundary prediction
takeadvantageofthisfeaturespectrumthatcombinesdeep, for electron microscopy by Ciresan et al. [2] and for natu-
coarse,semanticinformationandshallow,fine,appearance ral images by a hybrid convnet/nearest neighbor model by
informationinSection4.2(seeFigure3). GaninandLempitsky[9];andimagerestorationanddepth
Inthenextsection,wereviewrelatedworkondeepclas- estimationbyEigenetal.[4,5].Commonelementsofthese
| sification | nets, | FCNs, | and | recent | approaches | to  | semantic | approachesinclude |     |     |     |     |     |     |
| ---------- | ----- | ----- | --- | ------ | ---------- | --- | -------- | ----------------- | --- | --- | --- | --- | --- | --- |
segmentation using convnets. The following sections ex- • smallmodelsrestrictingcapacityandreceptivefields;
plainFCNdesignanddensepredictiontradeoffs,introduce • patchwisetraining[27,2,7,28,9];
our architecture with in-network upsampling and multi- • post-processing by superpixel projection, random field
layer combinations, and describe our experimental frame- regularization,filtering,orlocalclassification[7,2,9];
work. Finally, we demonstrate state-of-the-art results on • inputshiftingandoutputinterlacingfordenseoutput[29,
| PASCALVOC2011-2,NYUDv2,andSIFTFlow. |     |     |     |     |     |     |     | 28,9]; |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
•
multi-scalepyramidprocessing[7,28,9];
| 2.Relatedwork |     |     |     |     |     |     |     | • saturatingtanhnonlinearities[7,4,28];and |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
• ensembles[2,9],
| Our | approach | draws | on  | recent | successes | of  | deep nets |     |     |     |     |     |     |     |
| --- | -------- | ----- | --- | ------ | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
whereasourmethoddoeswithoutthismachinery.However,
| for image | classification |     | [20, | 31, 32] | and | transfer | learning |             |           |     |          |         |                    |     |
| --------- | -------------- | --- | ---- | ------- | --- | -------- | -------- | ----------- | --------- | --- | -------- | ------- | ------------------ | --- |
|           |                |     |      |         |     |          |          | we do study | patchwise |     | training | 3.4 and | “shift-and-stitch” |     |
[3, 38]. Transfer was first demonstrated on various visual dense output 3.2 from the perspective of FCNs. We also
| recognition | tasks | [3, | 38], then | on  | detection, | and | on both |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --------- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
discussin-networkupsampling3.3,ofwhichthefullycon-
| instance | and | semantic | segmentation |     | in  | hybrid | proposal- |     |     |     |     |     |     |     |
| -------- | --- | -------- | ------------ | --- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
nectedpredictionbyEigenetal.[5]isaspecialcase.
classifiermodels[10,15,13].Wenowre-architectandfine-
Unliketheseexistingmethods,weadaptandextenddeep
tuneclassificationnetstodirect,densepredictionofseman-
classificationarchitectures,usingimageclassificationassu-
| tic segmentation. |     | We  | chart | the space | of  | FCNs | and situate |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----- | --------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
pervisedpre-training,andfine-tunefullyconvolutionallyto
priormodels,bothhistoricalandrecent,inthisframework.
|       |               |     |          |     |        |            |     | learn simply | and | efficiently | from | whole | image | inputs and |
| ----- | ------------- | --- | -------- | --- | ------ | ---------- | --- | ------------ | --- | ----------- | ---- | ----- | ----- | ---------- |
| Fully | convolutional |     | networks |     | To our | knowledge, | the |              |     |             |      |       |       |            |
wholeimagegroundthruths.
| idea of | extending | a convnet |     | to arbitrary-sized |     |     | inputs first |     |     |     |     |     |     |     |
| ------- | --------- | --------- | --- | ------------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Hariharanetal.[15]andGuptaetal.[13]likewiseadapt
| appeared                             | in Matan | et              | al. [26], | which | extended |                 | the classic |                     |                     |        |             |               |       |            |
| ------------------------------------ | -------- | --------------- | --------- | ----- | -------- | --------------- | ----------- | ------------------- | ------------------- | ------ | ----------- | ------------- | ----- | ---------- |
|                                      |          |                 |           |       |          |                 |             | deep classification |                     | nets   | to semantic | segmentation, |       | but do     |
| LeNet[21]torecognizestringsofdigits. |          |                 |           |       |          | Becausetheirnet |             |                     |                     |        |             |               |       |            |
|                                      |          |                 |           |       |          |                 |             | so in hybrid        | proposal-classifier |        | models.     |               | These | approaches |
| was limited                          | to       | one-dimensional |           | input | strings, | Matan           | et al.      |                     |                     |        |             |               |       |            |
|                                      |          |                 |           |       |          |                 |             | fine-tune           | an R-CNN            | system | [10]        | by sampling   |       | bounding   |
usedViterbidecodingtoobtaintheiroutputs.WolfandPlatt
|     |     |     |     |     |     |     |     | boxes and/or | region | proposals | for | detection, | semantic | seg- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | --- | ---------- | -------- | ---- |
[37]expandconvnetoutputsto2-dimensionalmapsofde-
|     |     |     |     |     |     |     |     | mentation, | and | instance | segmentation. |     | Neither | method is |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------------- | --- | ------- | --------- |
tectionscoresforthefourcornersofpostaladdressblocks.
|         |       |            |       |     |           |     |          | learned | end-to-end. | They | achieve | state-of-the-art |     | segmen- |
| ------- | ----- | ---------- | ----- | --- | --------- | --- | -------- | ------- | ----------- | ---- | ------- | ---------------- | --- | ------- |
| Both of | these | historical | works | do  | inference | and | learning |         |             |      |         |                  |     |         |
tationresultsonPASCALVOCandNYUDv2respectively,
| fully convolutionally |     |     | for detection. |     | Ning | et al. | [27] define |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------------- | --- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
sowedirectlycompareourstandalone,end-to-endFCNto
aconvnetforcoarsemulticlasssegmentationofC.elegans
theirsemanticsegmentationresultsinSection5.
tissueswithfullyconvolutionalinference.
Wefusefeaturesacrosslayerstodefineanonlinearlocal-
Fullyconvolutionalcomputationhasalsobeenexploited
|                |     |        |              |     |       |         |        | to-global | representation |     | that we | tune end-to-end. |     | In con- |
| -------------- | --- | ------ | ------------ | --- | ----- | ------- | ------ | --------- | -------------- | --- | ------- | ---------------- | --- | ------- |
| in the present |     | era of | many-layered |     | nets. | Sliding | window |           |                |     |         |                  |     |         |
temporaryworkHariharanetal.[16]alsousemultiplelay-
| detection | by Sermanet |     | et al. | [29], | semantic | segmentation |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------ | ----- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ersintheirhybridmodelforsemanticsegmentation.
| by Pinheiro | and | Collobert |     | [28], and | image | restoration | by  |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | --------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Eigenetal.[4]dofullyconvolutionalinference.
|     |     |     |     |     |     |     | Fullycon- | 3.Fullyconvolutionalnetworks |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
volutionaltrainingisrare,butusedeffectivelybyTompson
et al. [35] to learn an end-to-end part detector and spatial Each layer of data in a convnet is a three-dimensional
modelforposeestimation,althoughtheydonotexpositon arrayofsizeh×w×d,wherehandw arespatialdimen-
oranalyzethismethod. sions, and d is the feature or channel dimension. The first
|                |     |     | et  | al.  |         |     |          | layeristheimage,withpixelsizeh×w,anddcolorchan- |     |     |     |     |     |     |
| -------------- | --- | --- | --- | ---- | ------- | --- | -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Alternatively, |     | He  |     | [17] | discard |     | the non- |                                                 |     |     |     |     |     |     |
convolutional portion of classification nets to make a nels. Locationsinhigherlayerscorrespondtothelocations
feature extractor. They combine proposals and spatial in the image they are path-connected to, which are called
pyramid pooling to yield a localized, fixed-length feature theirreceptivefields.
for classification. While fast and effective, this hybrid Convnets are built on translation invariance. Their ba-
modelcannotbelearnedend-to-end. siccomponents(convolution,pooling,andactivationfunc-
Dense prediction with convnets Several recent works tions) operate on local input regions, and depend only on
haveappliedconvnetstodensepredictionproblems,includ- relativespatialcoordinates. Writingx forthedatavector
ij
ingsemanticsegmentationbyNingetal.[27],Farabetetal. atlocation(i,j)inaparticularlayer,andy ij forthefollow-

| inglayer,thesefunctionscomputeoutputsy |     |     |     |     | by  |     |     |     |     |     |     | ``tabby cat" |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
ij
y ij =f ks ({x si+δi,sj+δj } 0≤δi,δj≤k ) 96256384384 2564096 4096 1000
wherek iscalledthekernelsize,sisthestrideorsubsam-
convolutionalization
| pling factor, | and | f determines |     | the layer | type: | a matrix |     |     |     |     |     |                   |     |
| ------------- | --- | ------------ | --- | --------- | ----- | -------- | --- | --- | --- | --- | --- | ----------------- | --- |
|               |     | ks           |     |           |       |          |     |     |     |     |     | tabby cat heatmap |     |
multiplicationforconvolutionoraveragepooling,aspatial
maxformaxpooling,oranelementwisenonlinearityforan
activationfunction,andsoonforothertypesoflayers.
|     |     |     |     |     |     |     |     |     |     | 2564096 | 4096 1000 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- |
384384
| This | functional | form | is maintained | under | composition, |     |     |     | 256 |     |     |     |     |
| ---- | ---------- | ---- | ------------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
withkernelsizeandstrideobeyingthetransformationrule
96
|     |     |                    |     |                                     |     |     | Figure 2.      | Transforming     | fully | connected | layers | into       | convolution |
| --- | --- | ------------------ | --- | ----------------------------------- | --- | --- | -------------- | ---------------- | ----- | --------- | ------ | ---------- | ----------- |
|     | f   | ◦g =(f             | ◦g) |                                     | .   |     |                |                  |       |           |        |            |             |
|     | ks  | k(cid:48)s(cid:48) |     | k(cid:48)+(k−1)s(cid:48),ss(cid:48) |     |     |                |                  |       |           |        |            |             |
|     |     |                    |     |                                     |     |     | layers enables | a classification |       | net to    | output | a heatmap. | Adding      |
While a general deep net computes a general nonlinear layersandaspatialloss(asinFigure1)producesanefficientma-
function, a net with only layers of this form computes a chineforend-to-enddenselearning.
nonlinearfilter,whichwecalladeepfilterorfullyconvolu- Furthermore, whiletheresultingmapsareequivalentto
| tional network. |     | An FCN | naturally | operates | on  | an input of |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
theevaluationoftheoriginalnetonparticularinputpatches,
anysize,andproducesanoutputofcorresponding(possibly
|     |     |     |     |     |     |     | the computation |     | is highly | amortized | over | the | overlapping |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --------- | ---- | --- | ----------- |
resampled)spatialdimensions. regionsofthosepatches. Forexample,whileAlexNettakes
| A real-valued |     | loss function |     | composed | with an | FCN de- |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
1.2ms(onatypicalGPU)toinfertheclassificationscores
fines a task. If the loss function is a sum over the spatial ofa227×227image,thefullyconvolutionalnettakes22ms
(cid:80)
dimensions of the final layer, (cid:96)(x;θ) = (cid:96)(cid:48)(x ;θ), its toproducea10×10gridofoutputsfroma500×500image,
|     |     |     |     |     | ij  | ij  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gradientwillbeasumoverthegradientsofeachofitsspa-
whichismorethan5timesfasterthanthena¨ıveapproach1.
tialcomponents.Thusstochasticgradientdescenton(cid:96)com- Thespatialoutputmapsoftheseconvolutionalizedmod-
putedonwholeimageswillbethesameasstochasticgradi-
elsmakethemanaturalchoicefordenseproblemslikese-
entdescenton(cid:96)(cid:48),takingallofthefinallayerreceptivefields
|     |     |     |     |     |     |     | mantic segmentation. |     | With | ground | truth | available | at ev- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ---- | ------ | ----- | --------- | ------ |
asaminibatch.
|      |       |           |        |                        |     |      | ery output       | cell, both | the      | forward        | and backward |        | passes are |
| ---- | ----- | --------- | ------ | ---------------------- | --- | ---- | ---------------- | ---------- | -------- | -------------- | ------------ | ------ | ---------- |
| When | these | receptive | fields | overlap significantly, |     | both |                  |            |          |                |              |        |            |
|      |       |           |        |                        |     |      | straightforward, |            | and both | take advantage |              | of the | inherent   |
feedforward computation and backpropagation are much computational efficiency (and aggressive optimization) of
moreefficientwhencomputedlayer-by-layeroveranentire
|     |     |     |     |     |     |     | convolution. | The | corresponding |     | backward | times | for the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | -------- | ----- | ------- |
imageinsteadofindependentlypatch-by-patch.
AlexNetexampleare2.4msforasingleimageand37ms
We next explain how to convert classification nets into forafullyconvolutional10×10outputmap,resultingina
| fully convolutional |     | nets | that produce | coarse | output | maps. |     |     |     |     |     |     |     |
| ------------------- | --- | ---- | ------------ | ------ | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
speedupsimilartothatoftheforwardpass.
For pixelwise prediction, we need to connect these coarse While our reinterpretation of classification nets as fully
outputsbacktothepixels.Section3.2describesatrick,fast
convolutionalyieldsoutputmapsforinputsofanysize,the
| scanning[11],introducedforthispurpose. |       |                   |     |                        | Wegaininsight |         |                    |              |                |             |         |                 |           |
| -------------------------------------- | ----- | ----------------- | --- | ---------------------- | ------------- | ------- | ------------------ | ------------ | -------------- | ----------- | ------- | --------------- | --------- |
|                                        |       |                   |     |                        |               |         | output dimensions  |              | are typically  |             | reduced | by subsampling. |           |
| into this                              | trick | by reinterpreting |     | it as an equivalent    |               | network |                    |              |                |             |         |                 |           |
|                                        |       |                   |     |                        |               |         | The classification |              | nets subsample |             | to keep | filters         | small and |
| modification.                          |       | As an efficient,  |     | effective alternative, |               | we in-  |                    |              |                |             |         |                 |           |
|                                        |       |                   |     |                        |               |         | computational      | requirements |                | reasonable. |         | This coarsens   | the       |
troducedeconvolutionlayersforupsamplinginSection3.3. outputofafullyconvolutionalversionofthesenets,reduc-
InSection3.4weconsidertrainingbypatchwisesampling,
ingitfromthesizeoftheinputbyafactorequaltothepixel
andgiveevidenceinSection4.3thatourwholeimagetrain-
strideofthereceptivefieldsoftheoutputunits.
ingisfasterandequallyeffective.
3.2.Shift-and-stitchisfilterrarefaction
3.1.Adaptingclassifiersfordenseprediction
|     |     |     |     |     |     |     | Dense | predictions | can | be obtained | from | coarse | outputs |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ----------- | ---- | ------ | ------- |
Typicalrecognitionnets,includingLeNet[21],AlexNet
bystitchingtogetheroutputfromshiftedversionsofthein-
| [20], and | its | deeper successors |     | [31, 32], | ostensibly | take |     |     |     |     |     |     |     |
| --------- | --- | ----------------- | --- | --------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
put. Iftheoutputisdownsampledbyafactoroff,shiftthe
| fixed-sized | inputs | and produce |     | non-spatial | outputs. | The |     |     |     |     |     |     |     |
| ----------- | ------ | ----------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
inputxpixelstotherightandypixelsdown,onceforevery
| fully connected |      | layers of | these        | nets have | fixed | dimensions  |            |         |      |         |         |       |            |
| --------------- | ---- | --------- | ------------ | --------- | ----- | ----------- | ---------- | ------- | ---- | ------- | ------- | ----- | ---------- |
|                 |      |           |              |           |       |             | (x,y) s.t. | 0 ≤ x,y | < f. | Process | each of | these | f2 inputs, |
| and throw       | away | spatial   | coordinates. | However,  |       | these fully |            |         |      |         |         |       |            |
andinterlacetheoutputssothatthepredictionscorrespond
| connected | layers | can also | be viewed | as  | convolutions | with |     |     |     |     |     |     |     |
| --------- | ------ | -------- | --------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
kernelsthatcovertheirentireinputregions. Doingsocasts tothepixelsatthecentersoftheirreceptivefields.
| them into | fully | convolutional |     | networks | that take | input of |     |     |     |     |     |     |     |
| --------- | ----- | ------------- | --- | -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
1Assumingefficientbatchingofsingleimageinputs.Theclassification
| any size | and output | classification |     | maps. | This transforma- |     |     |     |     |     |     |     |     |
| -------- | ---------- | -------------- | --- | ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
scoresforasingleimagebyitselftake5.4mstoproduce,whichisnearly
tionisillustratedinFigure2. 25timesslowerthanthefullyconvolutionalversion.

Although performing this transformation na¨ıvely in- Inourexperiments,wefindthatin-networkupsampling
creasesthecostbyafactoroff2,thereisawell-knowntrick isfastandeffectiveforlearningdenseprediction. Ourbest
for efficiently producing identical results [11, 29] known segmentation architecture uses these layers to learn to up-
to the wavelet community as the a` trous algorithm [25]. sampleforrefinedpredictioninSection4.2.
Consideralayer(convolutionorpooling)withinputstride
3.4.Patchwisetrainingislosssampling
| s, and a   | subsequent |            | convolution |     | layer with   | filter  | weights |               |     |               |     |          |             |     |     |
| ---------- | ---------- | ---------- | ----------- | --- | ------------ | ------- | ------- | ------------- | --- | ------------- | --- | -------- | ----------- | --- | --- |
| f (eliding | the        | irrelevant | feature     |     | dimensions). | Setting | the     |               |     |               |     |          |             |     |     |
| ij         |            |            |             |     |              |         |         | In stochastic |     | optimization, |     | gradient | computation |     | is  |
lower layer’s input stride to 1 upsamples its output by a driven by the training distribution. Both patchwise train-
factor of s. However, convolving the original filter with ing and fully convolutional training can be made to pro-
| the upsampled |     | output | does | not produce | the | same | result as |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---- | ----------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
duceanydistribution,althoughtheirrelativecomputational
shift-and-stitch, because the original filter only sees a re- efficiency depends on overlap and minibatch size. Whole
| duced portion |     | of its (now | upsampled) |     | input. | To reproduce |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ---------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
imagefullyconvolutionaltrainingisidenticaltopatchwise
thetrick,rarefythefilterbyenlargingitas trainingwhereeachbatchconsistsofallthereceptivefields
|     |     |     |     |     |     |     |     | of the units | below | the | loss for | an image | (or | collection | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | -------- | -------- | --- | ---------- | --- |
(cid:26)
|     |     | f   | ifsdividesbothiandj; |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f(cid:48) = i/s,j/s images).Whilethisismoreefficientthanuniformsampling
ij
0 otherwise, ofpatches,itreducesthenumberofpossiblebatches. How-
|             |                |     |             |     |         |           |     | ever, random | selection |             | of patches | within   | an            | image may | be   |
| ----------- | -------------- | --- | ----------- | --- | ------- | --------- | --- | ------------ | --------- | ----------- | ---------- | -------- | ------------- | --------- | ---- |
| (with i and | j zero-based). |     | Reproducing |     | thefull | netoutput |     |              |           |             |            |          |               |           |      |
|             |                |     |             |     |         |           |     | recovered    | simply.   | Restricting |            | the loss | to a randomly |           | sam- |
ofthetrickinvolvesrepeatingthisfilterenlargementlayer- pledsubsetofitsspatialterms(or, equivalentlyapplyinga
| by-layeruntilallsubsamplingisremoved. |     |     |     |     | (Inpractice,this |     |     |             |     |           |         |     |        |         |       |
| ------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | ----------- | --- | --------- | ------- | --- | ------ | ------- | ----- |
|                                       |     |     |     |     |                  |     |     | DropConnect |     | mask [36] | between | the | output | and the | loss) |
canbedoneefficientlybyprocessingsubsampledversions
excludespatchesfromthegradientcomputation.
oftheupsampledinput.) If the kept patches still have significant overlap, fully
Decreasingsubsamplingwithinanetisatradeoff:thefil-
|     |     |     |     |     |     |     |     | convolutional |     | computation | will | still speed | up  | training. | If  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ---- | ----------- | --- | --------- | --- |
tersseefinerinformation, buthavesmallerreceptivefields gradients are accumulated over multiple backward passes,
and take longer to compute. The shift-and-stitch trick is batchescanincludepatchesfromseveralimages.2
| another | kind of | tradeoff: | the | output | is denser | without | de- |     |     |     |     |     |     |     |     |
| ------- | ------- | --------- | --- | ------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Samplinginpatchwisetrainingcancorrectclassimbal-
creasingthereceptivefieldsizesofthefilters,butthefilters ance[27,7,2]andmitigatethespatialcorrelationofdense
| are prohibited |     | from accessing |     | information |     | at a finer | scale |                 |     |                               |     |     |     |           |     |
| -------------- | --- | -------------- | --- | ----------- | --- | ---------- | ----- | --------------- | --- | ----------------------------- | --- | --- | --- | --------- | --- |
|                |     |                |     |             |     |            |       | patches[28,15]. |     | Infullyconvolutionaltraining, |     |     |     | classbal- |     |
thantheiroriginaldesign. ance can also be achieved by weighting the loss, and loss
| Although | we  | have | done | preliminary | experiments |     | with |     |     |     |     |     |     |     |     |
| -------- | --- | ---- | ---- | ----------- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
samplingcanbeusedtoaddressspatialcorrelation.
this trick, we do not use it in our model. We find learn- WeexploretrainingwithsamplinginSection4.3,anddo
ingthroughupsampling,asdescribedinthenextsection,to notfindthatityieldsfasterorbetterconvergencefordense
| be more | effective | and | efficient, | especially | when | combined |     |             |                                            |     |     |     |     |     |     |
| ------- | --------- | --- | ---------- | ---------- | ---- | -------- | --- | ----------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|         |           |     |            |            |      |          |     | prediction. | Wholeimagetrainingiseffectiveandefficient. |     |     |     |     |     |     |
withtheskiplayerfusiondescribedlateron.
4.SegmentationArchitecture
3.3.Upsamplingisbackwardsstridedconvolution
|         |     |            |     |        |         |          |        | We cast | ILSVRC | classifiers |     | into | FCNs | and augment |     |
| ------- | --- | ---------- | --- | ------ | ------- | -------- | ------ | ------- | ------ | ----------- | --- | ---- | ---- | ----------- | --- |
| Another | way | to connect |     | coarse | outputs | to dense | pixels |         |        |             |     |      |      |             |     |
themfordensepredictionwithin-networkupsamplingand
| isinterpolation. |     | Forinstance, |     | simplebilinearinterpolation |     |     |     |                 |     |                                      |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | --------------------------- | --- | --- | --- | --------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|                  |     |              |     |                             |     |     |     | apixelwiseloss. |     | Wetrainforsegmentationbyfine-tuning. |     |     |     |     |     |
computeseachoutputy fromthenearestfourinputsbya Next,weaddskipsbetweenlayerstofusecoarse,semantic
ij
linearmapthatdependsonlyontherelativepositionsofthe
|     |     |     |     |     |     |     |     | andlocal,appearanceinformation. |     |     |     | Thisskiparchitectureis |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
inputandoutputcells. learnedend-to-endtorefinethesemanticsandspatialpreci-
| Inasense,upsamplingwithfactorf |     |     |     |     | isconvolutionwith |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sionoftheoutput.
afractionalinputstrideof1/f. Solongasf isintegral, a Forthisinvestigation,wetrainandvalidateonthePAS-
naturalwaytoupsampleisthereforebackwardsconvolution CALVOC2011segmentationchallenge[6]. Wetrainwith
| (sometimes | called | deconvolution) |     |     | with an | output | stride of |             |             |     |          |      |              |      |     |
| ---------- | ------ | -------------- | --- | --- | ------- | ------ | --------- | ----------- | ----------- | --- | -------- | ---- | ------------ | ---- | --- |
|            |        |                |     |     |         |        |           | a per-pixel | multinomial |     | logistic | loss | and validate | with | the |
f. Suchanoperationistrivialtoimplement,sinceitsimply standardmetricofmeanpixelintersectionoverunion,with
| reverses | the forward |     | and backward |     | passes | of convolution. |     |                                                 |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ------------ | --- | ------ | --------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          |             |     |              |     |        |                 |     | themeantakenoverallclasses,includingbackground. |     |     |     |     |     |     | The |
Thus upsampling is performed in-network for end-to-end training ignores pixels that are masked out (as ambiguous
learningbybackpropagationfromthepixelwiseloss. ordifficult)inthegroundtruth.
Notethatthedeconvolutionfilterinsuchalayerneednot
2Notethatnoteverypossiblepatchisincludedthisway,sincethere-
| be fixed | (e.g., | to bilinear | upsampling), |     | but | can be | learned. |                                                           |     |     |     |     |     |          |     |
| -------- | ------ | ----------- | ------------ | --- | --- | ------ | -------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- |
|          |        |             |              |     |     |        |          | ceptivefieldsofthefinallayerunitslieonafixed,stridedgrid. |     |     |     |     |     | However, |     |
Astackofdeconvolutionlayersandactivationfunctionscan
byshiftingtheimagerightanddownbyarandomvalueuptothestride,
evenlearnanonlinearupsampling. randomselectionfromallpossiblepatchesmayberecovered.

32x upsampled
image conv1 pool1 conv2 pool2 conv3 pool3 conv4 pool4 conv5 pool5 conv6-7 prediction (FCN-32s)
|     |     |     |     |     |     |     |     | 2x conv7 | 16x upsampled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
prediction (FCN-16s)
pool4
8x upsampled
|     |     |     |     |     |     |     |     | 4x conv7 | prediction (FCN-8s) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------- | --- |
2x pool4
pool3
Figure3. OurDAGnetslearntocombinecoarse,highlayerinformationwithfine,lowlayerinformation.Poolingandpredictionlayersare
shownasgridsthatrevealrelativespatialcoarseness,whileintermediatelayersareshownasverticallines.Firstrow(FCN-32s):Oursingle-
streamnet,describedinSection4.1,upsamplesstride32predictionsbacktopixelsinasinglestep. Secondrow(FCN-16s): Combining
predictionsfromboththefinallayerandthepool4layer,atstride16,letsournetpredictfinerdetails,whileretaininghigh-levelsemantic
information.Thirdrow(FCN-8s):Additionalpredictionsfrompool3,atstride8,providefurtherprecision.
|     |     |     |     |     |     | Table1. Weadaptandextendthreeclassificationconvnets. |     |     |     | We  |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
4.1.FromclassifiertodenseFCN
compareperformancebymeanintersectionoveruniononthevali-
Webeginbyconvolutionalizingprovenclassificationar- dationsetofPASCALVOC2011andbyinferencetime(averaged
chitectures as in Section 3. We consider the AlexNet3 ar- over20trialsfora500×500inputonanNVIDIATeslaK40c).
Wedetailthearchitectureoftheadaptednetswithregardtodense
| chitecture | [20] that won | ILSVRC12, | as well | as the | VGG |     |     |     |     |     |
| ---------- | ------------- | --------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
prediction:numberofparameterlayers,receptivefieldsizeofout-
| nets [31] | and the GoogLeNet4 | [32] | which | did exception- |     |     |     |     |     |     |
| --------- | ------------------ | ---- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
ally well in ILSVRC14. We pick the VGG 16-layer net5, putunits,andthecoarseststridewithinthenet. (Thesenumbers
givethebestperformanceobtainedatafixedlearningrate,notbest
whichwefoundtobeequivalenttothe19-layernetonthis
performancepossible.)
task. ForGoogLeNet,weuseonlythefinallosslayer,and
|     |     |     |     |     |     |     | FCN- | FCN- |     | FCN- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | ---- |
improveperformancebydiscardingthefinalaveragepool-
|            |               |          |               |     |           |     | AlexNet | VGG16 | GoogLeNet4 |     |
| ---------- | ------------- | -------- | ------------- | --- | --------- | --- | ------- | ----- | ---------- | --- |
| ing layer. | We decapitate | each net | by discarding |     | the final |     |         |       |            |     |
classifier layer, and convert all fully connected layers to meanIU 39.8 56.0 42.5
|               |               |        |             |        |       | forwardtime | 50ms | 210ms | 59ms |     |
| ------------- | ------------- | ------ | ----------- | ------ | ----- | ----------- | ---- | ----- | ---- | --- |
| convolutions. | We append     | a 1×1  | convolution | with   | chan- |             |      |       |      |     |
|               |               |        |             |        |       | conv.layers | 8    | 16    |      | 22  |
| nel dimension | 21 to predict | scores | for each    | of the | PAS-  |             |      |       |      |     |
CAL classes (including background) at each of the coarse parameters 57M 134M 6M
|                   |          |                    |     |       |        | rfsize | 355 | 404 |     | 907 |
| ----------------- | -------- | ------------------ | --- | ----- | ------ | ------ | --- | --- | --- | --- |
| output locations, | followed | by a deconvolution |     | layer | to bi- |        |     |     |     |     |
linearlyupsamplethecoarseoutputstopixel-denseoutputs maxstride 32 32 32
as described in Section 3.3. Table 1 compares the prelim- appearstobestate-of-the-artat56.0meanIUonval,com-
inaryvalidationresultsalongwiththebasiccharacteristics
|         |                |                  |          |       |      | pared to  | 52.6 on test [15]. | Training           | on extra | data raises |
| ------- | -------------- | ---------------- | -------- | ----- | ---- | --------- | ------------------ | ------------------ | -------- | ----------- |
| of each | net. We report | the best results | achieved | after | con- |           |                    |                    |          |             |
|         |                |                  |          |       |      | FCN-VGG16 | to 59.4 mean       | IU and FCN-AlexNet |          | to 48.0     |
vergenceatafixedlearningrate(atleast175epochs). meanIUonasubsetofval7. Despitesimilarclassification
Fine-tuningfromclassificationtosegmentationgaverea-
accuracy,ourimplementationofGoogLeNetdidnotmatch
sonable predictions for each net. Even the worst model theVGG16segmentationresult.
| achieved | ∼ 75% of | state-of-the-art | performance. |     | The |     |     |     |     |     |
| -------- | -------- | ---------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
segmentation-equipped VGG net (FCN-VGG16) already 4.2.Combiningwhatandwhere
3UsingthepubliclyavailableCaffeNetreferencemodel. Wedefineanewfullyconvolutionalnet(FCN)forseg-
| 4Since | there is no publicly | available version | of  | GoogLeNet, | we use |     |     |     |     |     |
| ------ | -------------------- | ----------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
mentationthatcombineslayersofthefeaturehierarchyand
ourownreimplementation.Ourversionistrainedwithlessextensivedata
|     |     |     |     |     |     | refinesthespatialprecisionoftheoutput. |     |     | SeeFigure3. |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | ----------- | --- |
augmentation,andgets68.5%top-1and88.4%top-5ILSVRCaccuracy.
5UsingthepubliclyavailableversionfromtheCaffemodelzoo. While fully convolutionalized classifiers can be fine-

tuned to segmentation as shown in 4.1, and even score FCN-32s FCN-16s FCN-8s Groundtruth
highlyonthestandardmetric,theiroutputisdissatisfyingly
coarse(seeFigure4).The32pixelstrideatthefinalpredic-
tionlayerlimitsthescaleofdetailintheupsampledoutput.
We address this by adding skips [1] that combine the
final prediction layer with lower layers with finer strides.
ThisturnsalinetopologyintoaDAG,withedgesthatskip
aheadfromlowerlayerstohigherones(Figure3). Asthey
see fewer pixels, the finer scale predictions should need
Figure4. Refiningfullyconvolutionalnetsbyfusinginformation
fewerlayers,soitmakessensetomakethemfromshallower
from layers with different strides improves segmentation detail.
netoutputs.Combiningfinelayersandcoarselayersletsthe
The first three images show the output from our 32, 16, and 8
modelmakelocalpredictionsthatrespectglobalstructure.
pixelstridenets(seeFigure3).
ByanalogytothejetofKoenderickandvanDoorn[19],we
callournonlinearfeaturehierarchythedeepjet. Table2. ComparisonofskipFCNsonasubset7ofPASCALVOC
We first divide the output stride in half by predicting 2011 segval. Learning is end-to-end, except for FCN-32s-fixed,
from a 16 pixel stride layer. We add a 1×1 convolution whereonlythelastlayerisfine-tuned.NotethatFCN-32sisFCN-
layer on top of pool4 to produce additional class predic- VGG16,renamedtohighlightstride.
tions. We fuse this output with the predictions computed pixel mean mean f.w.
on top of conv7 (convolutionalized fc7) at stride 32 by acc. acc. IU IU
adding a 2× upsampling layer and summing6 both predic- FCN-32s-fixed 83.0 59.7 45.4 72.0
tions(seeFigure3). Weinitializethe2×upsamplingtobi- FCN-32s 89.1 73.3 59.4 81.4
linearinterpolation, butallowtheparameterstobelearned FCN-16s 90.0 75.7 62.4 83.0
as described in Section 3.3. Finally, the stride 16 predic- FCN-8s 90.3 75.9 62.7 83.2
tions are upsampled back to the image. We call this net
FCN-16s. FCN-16s is learned end-to-end, initialized with maintain its receptive field size. In addition to their com-
the parameters of the last, coarser net, which we now call putationalcost,wehaddifficultylearningsuchlargefilters.
FCN-32s. Thenewparametersactingonpool4arezero- Weattemptedtore-architectthelayersabovepool5with
initializedsothatthenetstartswithunmodifiedpredictions. smallerfilters,butdidnotachievecomparableperformance;
Thelearningrateisdecreasedbyafactorof100. one possible explanation is that the ILSVRC initialization
Learningthisskipnetimprovesperformanceontheval- oftheupperlayersisimportant.
idation set by 3.0 mean IU to 62.4. Figure 4 shows im- Anotherwaytoobtainfinerpredictionsistousetheshift-
provementinthefinestructureoftheoutput. Wecompared and-stitch trick described in Section 3.2. In limited exper-
thisfusionwithlearningonlyfromthepool4layer,which iments, we found the cost to improvement ratio from this
resulted in poor performance, and simply decreasing the methodtobeworsethanlayerfusion.
learningratewithoutaddingtheskip, whichresultedinan
insignificantperformanceimprovement without improving 4.3.Experimentalframework
thequalityoftheoutput.
Optimization We train by SGD with momentum. We
We continue in this fashion by fusing predictions from
useaminibatchsizeof20imagesandfixedlearningratesof
pool3 with a 2× upsampling of predictions fused from
10−3,10−4,and5−5 forFCN-AlexNet,FCN-VGG16,and
pool4 and conv7, building the net FCN-8s. We obtain
FCN-GoogLeNet, respectively, chosen by line search. We
aminoradditionalimprovementto62.7meanIU,andfind
usemomentum0.9,weightdecayof5−4 or2−4,anddou-
a slight improvement in the smoothness and detail of our
bledlearningrateforbiases,althoughwefoundtrainingto
output. Atthispointourfusionimprovementshavemetdi-
besensitivetothelearningratealone.Wezero-initializethe
minishingreturns,bothwithrespecttotheIUmetricwhich
classscoringlayer,asrandominitializationyieldedneither
emphasizeslarge-scalecorrectness,andalsointermsofthe
betterperformancenorfasterconvergence.Dropoutwasin-
improvementvisiblee.g. inFigure4,sowedonotcontinue
cludedwhereusedintheoriginalclassifiernets.
fusingevenlowerlayers.
Fine-tuning We fine-tune all layers by back-
Refinement by other means Decreasing the stride of
propagation through the whole net. Fine-tuning the
pooling layers is the most straightforward way to obtain
output classifier alone yields only 70% of the full fine-
finerpredictions. However,doingsoisproblematicforour
tuningperformanceascomparedinTable2. Trainingfrom
VGG16-based net. Setting the pool5 stride to 1 requires
scratch is not feasible considering the time required to
our convolutionalized fc6 to have kernel size 14×14 to
learnthebaseclassificationnets. (NotethattheVGGnetis
6Maxfusionmadelearningdifficultduetogradientswitching. trainedinstages, whileweinitializefromthefull16-layer

1.2 1.2 layer deconvolutional filters are fixed to bilinear interpola-
full images tion,whileintermediateupsamplinglayersareinitializedto
| 1.0 | 50% sampling |     |     | 1.0 |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bilinearupsampling,andthenlearned.
25% sampling
|      |     |     |     |      |     |     |     | Augmentation                                         |     | We                                  | tried augmenting |     | the | training data |
| ---- | --- | --- | --- | ---- | --- | --- | --- | ---------------------------------------------------- | --- | ----------------------------------- | ---------------- | --- | --- | ------------- |
| 0.8  |     |     |     | 0.8  |     |     |     |                                                      |     |                                     |                  |     |     |               |
| ssol |     |     |     | ssol |     |     |     | byrandomlymirroringand“jittering”theimagesbytrans-   |     |                                     |                  |     |     |               |
| 0.6  |     |     |     | 0.6  |     |     |     | latingthemupto32pixels(thecoarsestscaleofprediction) |     |                                     |                  |     |     |               |
|      |     |     |     |      |     |     |     | ineachdirection.                                     |     | Thisyieldednonoticeableimprovement. |                  |     |     |               |
| 0.4  |     |     |     | 0.4  |     |     |     |                                                      |     |                                     |                  |     |     |               |
|      |     |     |     |      |     |     |     | Implementation                                       |     | Allmodelsaretrainedandtestedwith    |                  |     |     |               |
500 1000 1500 10000 20000 30000 Caffe [18] on a single NVIDIA Tesla K40c. Our models
|     | iteration number |     |     | relative time (num. images processed) |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andcodearepubliclyavailableat
Figure5. Trainingonwholeimagesisjustaseffectiveassampling
http://fcn.berkeleyvision.org.
| patches, but            | results | in faster | (wall                          | time) | convergence | by  | making |     |     |     |     |     |     |     |
| ----------------------- | ------- | --------- | ------------------------------ | ----- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| moreefficientuseofdata. |         |           | Leftshowstheeffectofsamplingon |       |             |     |        |     |     |     |     |     |     |     |
5.Results
convergencerateforafixedexpectedbatchsize,whilerightplots
thesamebyrelativewalltime. We test our FCN on semantic segmentation and scene
version.) Fine-tuningtakesthreedaysonasingleGPUfor parsing, exploring PASCAL VOC, NYUDv2, and SIFT
the coarse FCN-32s version, and about one day each to Flow. Although these tasks have historically distinguished
upgradetotheFCN-16sandFCN-8sversions. between objects and regions, we treat both uniformly as
MoreTrainingData ThePASCALVOC2011segmen- pixelprediction. WeevaluateourFCNskiparchitectureon
eachofthesedatasets,andthenextendittomulti-modalin-
| tationtrainingsetlabels1112images. |     |     |     |     | Hariharanetal.[14] |     |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
collected labels for a larger set of 8498 PASCAL training putforNYUDv2andmulti-taskpredictionforthesemantic
images, which was used to train the previous state-of-the- andgeometriclabelsofSIFTFlow.
artsystem,SDS[15]. ThistrainingdataimprovestheFCN- Metrics Wereportfourmetricsfromcommonsemantic
VGG16validationscore7by3.4pointsto59.4meanIU. segmentation and scene parsing evaluations that are varia-
|       |          |     |           |     |         |      |          | tions on pixel | accuracy |     | and region | intersection |     | over union |
| ----- | -------- | --- | --------- | --- | ------- | ---- | -------- | -------------- | -------- | --- | ---------- | ------------ | --- | ---------- |
| Patch | Sampling | As  | explained | in  | Section | 3.4, | our full |                |          |     |            |              |     |            |
image training effectively batches each image into a regu- (IU).Letn bethenumberofpixelsofclassipredictedto
ij
|     |     |     |     |     |     |     |     | belongtoclassj,wheretherearen |     |     |     |     | differentclasses,and |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | -------------------- | --- |
lar grid of large, overlapping patches. By contrast, prior cl
(cid:80)
workrandomlysamplespatchesoverafulldataset[27,2,7, lett i = n ij bethetotalnumberofpixelsofclassi. We
j
| 28,9], potentiallyresultinginhighervariancebatchesthat |     |     |     |                       |     |     |     | compute:         |     |          |           |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --------------------- | --- | --- | --- | ---------------- | --- | -------- | --------- | --- | --- | --- |
|                                                        |     |     |     |                       |     |     |     | • pixelaccuracy: |     | (cid:80) | /(cid:80) |     |     |     |
| mayaccelerateconvergence[22].                          |     |     |     | Westudythistradeoffby |     |     |     |                  |     | n ii     | t i       |     |     |     |
|                                                        |     |     |     |                       |     |     |     |                  |     | i        | i         |     |     |     |
spatiallysamplingthelossinthemannerdescribedearlier, • meanaccuraccy: (1/n )(cid:80) n /t
|     |     |     |     |     |     |     |     |     |     |     | cl i     | ii i |          |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | --- |
|     |     |     |     |     |     |     |     |     |     |     | (cid:16) |      | (cid:17) |     |
makinganindependentchoicetoignoreeachfinallayercell • meanIU:(1/n )(cid:80) n / t +(cid:80) n −n
|                         |     |     |     |                          |     |     |     |                        | cl  | i ii | i   | j ji | ii  |     |
| ----------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | ---------------------- | --- | ---- | --- | ---- | --- | --- |
| withsomeprobability1−p. |     |     |     | Toavoidchangingtheeffec- |     |     |     |                        |     |      |     |      |     |     |
|                         |     |     |     |                          |     |     |     | • frequencyweightedIU: |     |      |     |      |     |     |
tive batch size, we simultaneously increase the number of (cid:16) (cid:17)
|              |                 |             |           |           |           |             |         | ((cid:80) )−1(cid:80) |          | +(cid:80)       |           |                   |             |              |
| ------------ | --------------- | ----------- | --------- | --------- | --------- | ----------- | ------- | --------------------- | -------- | --------------- | --------- | ----------------- | ----------- | ------------ |
|              |                 |             |           |           |           |             |         | k t k                 | i tn i   | ii / t i        | j n ji    | −n ii             |             |              |
| images per   | batch           | by a factor | 1/p.      | Note      | that      | due to      | the ef- |                       |          |                 |           |                   |             |              |
|              |                 |             |           |           |           |             |         | PASCAL                | VOC      | Table           | 3 gives   | the               | performance | of our       |
| ficiency     | of convolution, |             | this form | of        | rejection | sampling    | is      |                       |          |                 |           |                   |             |              |
|              |                 |             |           |           |           |             |         | FCN-8s on             | the test | sets            | of PASCAL |                   | VOC 2011    | and 2012,    |
| still faster | than patchwise  |             | training  | for       | large     | enough      | values  |                       |          |                 |           |                   |             |              |
|              |                 |             |           |           |           |             |         | and compares          | it       | to the previous |           | state-of-the-art, |             | SDS [15],    |
| of p (e.g.,  | at least        | for p       | > 0.2     | according | to        | the numbers |         |                       |          |                 |           |                   |             |              |
|              |                 |             |           |           |           |             |         | and the well-known    |          | R-CNN           | [10].     | We                | achieve     | the best re- |
| in Section   | 3.1).           | Figure      | 5 shows   | the       | effect of | this        | form of |                       |          |                 |           |                   |             |              |
IU8
|          |                 |     |     |           |          |      |     | sults on mean |     | by a | relative | margin | of 20%. | Inference |
| -------- | --------------- | --- | --- | --------- | -------- | ---- | --- | ------------- | --- | ---- | -------- | ------ | ------- | --------- |
| sampling | on convergence. |     | We  | find that | sampling | does | not |               |     |      |          |        |         |           |
timeisreduced114×(convnetonly,ignoringproposalsand
| have a significant |     | effect | on convergence |     | rate | compared | to  |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | -------------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
refinement)or286×(overall).
wholeimagetraining,buttakessignificantlymoretimedue
to the larger number of images that need to be considered Table3. Ourfullyconvolutionalnetgivesa20%relativeimprove-
| per batch. | We therefore |     | choose | unsampled, |     | whole | image |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | ---------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
mentoverthestate-of-the-artonthePASCALVOC2011and2012
traininginourotherexperiments. testsetsandreducesinferencetime.
| Class | Balancing | Fully | convolutional |     | training |     | can bal- |     |     |        |     |        |     |           |
| ----- | --------- | ----- | ------------- | --- | -------- | --- | -------- | --- | --- | ------ | --- | ------ | --- | --------- |
|       |           |       |               |     |          |     |          |     |     | meanIU |     | meanIU |     | inference |
ance classes by weighting or sampling the loss. Although VOC2011test VOC2012test time
our labels are mildly unbalanced (about 3/4 are back- R-CNN[10] 47.9 - -
ground),wefindclassbalancingunnecessary. SDS[15] 52.6 51.6 ∼50s
DensePrediction Thescoresareupsampledtotheinput FCN-8s 62.7 62.2 ∼175ms
| dimensions | by deconvolution |     |     | layers | within | the net. | Final |        |      |       |       |         |           |           |
| ---------- | ---------------- | --- | --- | ------ | ------ | -------- | ----- | ------ | ---- | ----- | ----- | ------- | --------- | --------- |
|            |                  |     |     |        |        |          |       | NYUDv2 | [30] | is an | RGB-D | dataset | collected | using the |
7Therearetrainingimagesfrom[14]includedinthePASCALVOC
2011valset,sowevalidateonthenon-intersectingsetof736images. 8Thisistheonlymetricprovidedbythetestserver.

Table4. ResultsonNYUDv2. RGBDisearly-fusionofthe Table 5. Results on SIFT Flow9 with class segmentation
RGBanddepthchannelsattheinput.HHAisthedepthembed- (center) and geometric segmentation (right). Tighe [33] is
dingof[13]ashorizontaldisparity,heightaboveground,and a non-parametric transfer method. Tighe 1 is an exemplar
theangleofthelocalsurfacenormalwiththeinferredgravity SVM while 2 is SVM + MRF. Farabet is a multi-scale con-
direction. RGB-HHA is the jointly trained late fusion model vnettrainedonclass-balancedsamples(1)ornaturalfrequency
thatsumsRGBandHHApredictions. samples(2). Pinheiroisamulti-scale,recurrentconvnet,de-
pixel mean mean f.w. notedRCNN 3 (◦3).Themetricforgeometryispixelaccuracy.
acc. acc. IU IU
Guptaetal.[13] 60.3 - 28.6 47.0 pixel mean mean f.w. geom.
acc. acc. IU IU acc.
FCN-32sRGB 60.0 42.2 29.2 43.9
Liuetal.[23] 76.7 - - - -
FCN-32sRGBD 61.5 42.4 30.5 45.5
Tigheetal.[33] - - - - 90.8
FCN-32sHHA 57.1 35.2 24.2 40.4
Tigheetal.[34]1 75.6 41.1 - - -
FCN-32sRGB-HHA 64.3 44.9 32.8 48.0
Tigheetal.[34]2 78.6 39.2 - - -
FCN-16sRGB-HHA 65.4 46.1 34.0 49.5
Farabetetal.[7]1 72.3 50.8 - - -
Microsoft Kinect. It has 1449 RGB-D images, with pixel- Farabetetal.[7]2 78.5 29.6 - - -
wiselabelsthathavebeencoalescedintoa40classseman- Pinheiroetal.[28] 77.7 29.8 - - -
ticsegmentationtaskbyGuptaetal.[12]. Wereportresults FCN-16s 85.2 51.7 39.5 76.1 94.3
onthestandardsplitof795trainingimagesand654testing
images. (Note: all model selection is performed on PAS-
FCN-8s SDS[15] GroundTruth Image
CAL2011val.)Table4givestheperformanceofourmodel
in several variations. First we train our unmodified coarse
model(FCN-32s)onRGBimages. Toadddepthinforma-
tion, we train on a model upgraded to take four-channel
RGB-D input (early fusion). This provides little benefit,
perhaps due to the difficultly of propagating meaningful
gradientsallthewaythroughthemodel. Followingthesuc-
cessofGuptaetal.[13],wetrythethree-dimensionalHHA
encodingofdepth,trainingnetsonjustthisinformation,as
wellasa“latefusion”ofRGBandHHAwherethepredic-
tionsfrombothnetsaresummedatthefinallayer, andthe
resulting two-stream net is learned end-to-end. Finally we
upgradethislatefusionnettoa16-strideversion.
SIFTFlowisadatasetof2,688imageswithpixellabels
for 33 semantic categories (“bridge”, “mountain”, “sun”),
as well as three geometric categories (“horizontal”, “verti-
cal”,and“sky”). AnFCNcannaturallylearnajointrepre-
sentationthatsimultaneouslypredictsbothtypesoflabels.
Figure 6. Fully convolutional segmentation nets produce state-
We learn a two-headed version of FCN-16s with seman-
of-the-art performance on PASCAL. The left column shows the
ticandgeometricpredictionlayersandlosses. Thelearned
outputofourhighestperformingnet,FCN-8s. Thesecondshows
modelperformsaswellonbothtasksastwoindependently thesegmentationsproducedbythepreviousstate-of-the-artsystem
trainedmodels,whilelearningandinferenceareessentially byHariharanetal.[15].Noticethefinestructuresrecovered(first
as fast as each independent model by itself. The results in row),abilitytoseparatecloselyinteractingobjects(secondrow),
Table5,computedonthestandardsplitinto2,488training androbustnesstooccluders(thirdrow). Thefourthrowshowsa
and200testimages,9 showstate-of-the-artperformanceon failurecase:thenetseeslifejacketsinaboataspeople.
bothtasks. nets to segmentation, and improving the architecture with
multi-resolutionlayercombinationsdramaticallyimproves
6.Conclusion
the state-of-the-art, while simultaneously simplifying and
speedinguplearningandinference.
Fully convolutional networks are a rich class of mod-
els, of which modern classification convnets are a spe- Acknowledgements This work was supported in part
cial case. Recognizing this, extending these classification byDARPA’sMSEEandSMISCprograms,NSFawardsIIS-
1427425, IIS-1212798, IIS-1116411, and the NSF GRFP,
9ThreeoftheSIFTFlowcategoriesarenotpresentinthetestset. We
Toyota, and the Berkeley Vision and Learning Center. We
madepredictionsacrossall33categories,butonlyincludedcategoriesac-
tuallypresentinthetestsetinourevaluation. gratefully acknowledge NVIDIA for GPU donation. We

thank Bharath Hariharan and Saurabh Gupta for their ad- [15] B.Hariharan,P.Arbela´ez,R.Girshick,andJ.Malik. Simul-
vice and dataset tools. We thank Sergio Guadarrama for taneous detection and segmentation. In European Confer-
|                              |     |                      |     | enceonComputerVision(ECCV),2014. |     | 1,2,4,5,7,8 |     |
| ---------------------------- | --- | -------------------- | --- | -------------------------------- | --- | ----------- | --- |
| reproducingGoogLeNetinCaffe. |     | WethankJitendraMalik |     |                                  |     |             |     |
for his helpful comments. Thanks to Wei Liu for pointing [16] B. Hariharan, P. Arbela´ez, R. Girshick, and J. Malik. Hy-
outanissuewthourSIFTFlowmeanIUcomputationand percolumnsforobjectsegmentationandfine-grainedlocal-
ization. InComputerVisionandPatternRecognition,2015.
anerrorinourfrequencyweightedmeanIUformula.
2
References [17] K.He,X.Zhang,S.Ren,andJ.Sun.Spatialpyramidpooling
|     |     |     |     | in deep | convolutional networks | for visual recognition. | In  |
| --- | --- | --- | --- | ------- | ---------------------- | ----------------------- | --- |
[1] C. M. Bishop. Pattern recognition and machine learning, ECCV,2014. 1,2
page229. Springer-VerlagNewYork,2006. 6 [18] Y.Jia,E.Shelhamer,J.Donahue,S.Karayev,J.Long,R.Gir-
[2] D.C.Ciresan,A.Giusti,L.M.Gambardella,andJ.Schmid- shick, S. Guadarrama, and T. Darrell. Caffe: Convolu-
huber. Deepneuralnetworkssegmentneuronalmembranes tionalarchitectureforfastfeatureembedding.arXivpreprint
inelectronmicroscopyimages. InNIPS,pages2852–2860, arXiv:1408.5093,2014. 7
2012. 1,2,4,7 [19] J.J.KoenderinkandA.J.vanDoorn. Representationoflo-
[3] J. Donahue, Y. Jia, O. Vinyals, J. Hoffman, N. Zhang, cal geometry in the visual system. Biological cybernetics,
E.Tzeng,andT.Darrell.DeCAF:Adeepconvolutionalacti- 55(6):367–375,1987. 6
vationfeatureforgenericvisualrecognition.InICML,2014. [20] A. Krizhevsky, I. Sutskever, and G. E. Hinton. Imagenet
1,2 classification with deep convolutional neural networks. In
NIPS,2012.
| [4] D.Eigen,D.Krishnan,andR.Fergus. |     | Restoringanimage |     |     | 1,2,3,5 |     |     |
| ----------------------------------- | --- | ---------------- | --- | --- | ------- | --- | --- |
takenthroughawindowcoveredwithdirtorrain. InCom- [21] Y.LeCun,B.Boser,J.Denker,D.Henderson,R.E.Howard,
puter Vision (ICCV), 2013 IEEE International Conference W.Hubbard,andL.D.Jackel. Backpropagationappliedto
on,pages633–640.IEEE,2013. 2 hand-writtenzipcoderecognition. InNeuralComputation,
1989. 2,3
| [5] D.Eigen,C.Puhrsch,andR.Fergus. |     | Depthmapprediction |     |     |     |     |     |
| ---------------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |
fromasingleimageusingamulti-scaledeepnetwork.arXiv [22] Y. A. LeCun, L. Bottou, G. B. Orr, and K.-R. Mu¨ller. Ef-
preprintarXiv:1406.2283,2014. 2 ficient backprop. In Neural networks: Tricks of the trade,
|                    |              |                    |          | pages9–48.Springer,1998. | 7   |     |     |
| ------------------ | ------------ | ------------------ | -------- | ------------------------ | --- | --- | --- |
| [6] M. Everingham, | L. Van Gool, | C. K. I. Williams, | J. Winn, |                          |     |     |     |
and A. Zisserman. The PASCAL Visual Object Classes [23] C.Liu,J.Yuen,andA.Torralba.Siftflow:Densecorrespon-
Challenge 2011 (VOC2011) Results. http://www.pascal- dence across scenes and its applications. Pattern Analysis
network.org/challenges/VOC/voc2011/workshop/index.html. andMachineIntelligence,IEEETransactionson,33(5):978–
| 4   |     |     |     | 994,2011. | 8   |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- |
[7] C.Farabet,C.Couprie,L.Najman,andY.LeCun. Learning [24] J.Long,N.Zhang,andT.Darrell. Doconvnetslearncorre-
hierarchicalfeaturesforscenelabeling.PatternAnalysisand spondence? InNIPS,2014. 1
MachineIntelligence,IEEETransactionson,2013. 1,2,4, [25] S. Mallat. A wavelet tour of signal processing. Academic
| 7,8 |     |     |     | press,2ndedition,1999. | 4   |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- |
[8] P.Fischer,A.Dosovitskiy,andT.Brox.Descriptormatching [26] O.Matan,C.J.Burges,Y.LeCun,andJ.S.Denker. Multi-
withconvolutionalneuralnetworks: acomparisontoSIFT. digitrecognitionusingaspacedisplacementneuralnetwork.
CoRR,abs/1405.5769,2014. 1 InNIPS,pages488–495.Citeseer,1991. 2
[9] Y.GaninandV.Lempitsky. N4-fields:Neuralnetworknear- [27] F.Ning,D.Delhomme,Y.LeCun,F.Piano,L.Bottou,and
estneighborfieldsforimagetransforms. InACCV,2014. 1, P.E.Barbano.Towardautomaticphenotypingofdeveloping
| 2,7 |     |     |     | embryosfromvideos.ImageProcessing,IEEETransactions |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
[10] R.Girshick,J.Donahue,T.Darrell,andJ.Malik. Richfea- on,14(9):1360–1371,2005. 1,2,4,7
ture hierarchies for accurate object detection and semantic [28] P. H. Pinheiro and R. Collobert. Recurrent convolutional
InComputerVisionandPatternRecognition,
segmentation. neural networks for scene labeling. In ICML, 2014. 1, 2,
| 2014. 1,2,7 |     |     |     | 4,7,8 |     |     |     |
| ----------- | --- | --- | --- | ----- | --- | --- | --- |
[11] A.Giusti,D.C.Cires¸an,J.Masci,L.M.Gambardella,and [29] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus,
J.Schmidhuber.Fastimagescanningwithdeepmax-pooling andY.LeCun. Overfeat:Integratedrecognition,localization
| convolutionalneuralnetworks. |     | InICIP,2013. | 3,4 |     |     | InICLR,2014. |     |
| ---------------------------- | --- | ------------ | --- | --- | --- | ------------ | --- |
anddetectionusingconvolutionalnetworks.
| [12] S.Gupta,P.Arbelaez,andJ.Malik. |     | Perceptualorganization |     | 1,2,4 |     |     |     |
| ----------------------------------- | --- | ---------------------- | --- | ----- | --- | --- | --- |
and recognition of indoor scenes from RGB-D images. In [30] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus. Indoor
CVPR,2013. 8 segmentation and support inference from rgbd images. In
|                                                |     |     |          | ECCV,2012. | 7   |     |     |
| ---------------------------------------------- | --- | --- | -------- | ---------- | --- | --- | --- |
| [13] S.Gupta,R.Girshick,P.Arbelaez,andJ.Malik. |     |     | Learning |            |     |     |     |
rich features from RGB-D images for object detection and [31] K. Simonyan and A. Zisserman. Very deep convolu-
segmentation. InECCV.Springer,2014. 1,2,8 tional networks for large-scale image recognition. CoRR,
[14] B.Hariharan,P.Arbelaez,L.Bourdev,S.Maji,andJ.Malik. abs/1409.1556,2014. 1,2,3,5
Semanticcontoursfrominversedetectors. InInternational [32] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed,
ConferenceonComputerVision(ICCV),2011. 7 D.Anguelov, D.Erhan, V.Vanhoucke, andA.Rabinovich.

Going deeper with convolutions. CoRR, abs/1409.4842,
2014. 1,2,3,5
[33] J.TigheandS.Lazebnik. Superparsing: scalablenonpara-
metricimageparsingwithsuperpixels.InECCV,pages352–
365.Springer,2010. 8
[34] J.TigheandS.Lazebnik.Findingthings:Imageparsingwith
regionsandper-exemplardetectors. InCVPR,2013. 8
[35] J.Tompson,A.Jain,Y.LeCun,andC.Bregler.Jointtraining
ofaconvolutionalnetworkandagraphicalmodelforhuman
poseestimation. CoRR,abs/1406.2984,2014. 2
[36] L.Wan,M.Zeiler,S.Zhang,Y.L.Cun,andR.Fergus. Reg-
ularization of neural networks using dropconnect. In Pro-
ceedings of the 30th International Conference on Machine
Learning(ICML-13),pages1058–1066,2013. 4
[37] R.WolfandJ.C.Platt. Postaladdressblocklocationusing
aconvolutionallocatornetwork. AdvancesinNeuralInfor-
mationProcessingSystems,pages745–745,1994. 2
[38] M.D.ZeilerandR.Fergus. Visualizingandunderstanding
convolutional networks. In Computer Vision–ECCV 2014,
pages818–833.Springer,2014. 2
[39] N. Zhang, J. Donahue, R. Girshick, and T. Darrell. Part-
based r-cnns for fine-grained category detection. In Com-
puter Vision–ECCV 2014, pages 834–849. Springer, 2014.
1
