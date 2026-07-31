IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021 9361
Measuring Deformed Sea Ice in Seasonal Ice
Zones Using L-Band SAR Images
Takenobu Toyota , Junno Ishiyama, and Noriaki Kimura
Abstract—In order to improve the understanding of the [2], [3]. They stressed the need to improve the dynamic
dynamical deformation processes of sea ice in the seasonal part in the model. Since the fraction of the seasonal ice
ice zone (SIZ), measures to detect deformed ice were devel-
zone (SIZ) in the Arctic Ocean is increasing in association
oped and validated using satellite L-band synthetic aperture
with the recent rapid reduction of summer sea ice extent
radar (ScanSAR) images for the southern Sea of Okhotsk.
Toapproach,seaicewascategorized intothreeicetypes,typical (see [4]–[6]), it will become more and more important in
of the sea ice in this region: nilas (thin level), pancake ice (thin the future to understand the dynamical processes of sea ice
rough),anddeformedice(thickrough),andthenthemeasuresto in the SIZ. Considering the essential effect of deformation
classifyintothesecategoriesweredevelopedusingALOS/Phased
processesonthedynamicalbehaviorandthicknessdistribution
Array type L-band Synthetic Aperture Radar (PALSAR) as a
functionofbackscattercoefficientsatHHpolarization(σ0 )and of sea ice especially in the SIZ (see [7]–[9]), developing
incidenceangle(θ),basedonthefieldobservations.Comp H a H rative the measures to detect deformed ice from satellite images
i
analysis confirmed that PALSAR can detect deformed ice more and examining its temporal evolution is expected to con-
efficientlythanRADARSAT-2(C-bandSAR).Thetemporal evo- tribute significantly to the improvement of numerical sea ice
lution of the area, judged as deformed ice from these measures,
models.
shows significant variability with both time and space, and
To monitor deformed ice, which usually occurs on a scale
deformed ice regions appear in relatively linear alignments with
a width of a few tens of kilometers in the innerice pack region,
lessthan1kminwidth,inarelativelywideregion(≥100km),
consistent with ice drift convergence. To confirm the results, the space-borne synthetic aperture radar (SAR) is expected to
PALSAR-2 images at HH and HV polarizations were examined beausefultoolbecauseofitshighspatialresolution(≤100m),
as a function of θ i , based on the four-year field observations in wide coverage (≥100 km), and high sensitivity to surface
the same area. The results revealed that σ0 and σ0 are both
subject to floe sizes as well as deformed i H c H e, and σ H 0 V is more roughness. SAR data have been proven to be efficient for
sensitive.Thisindicatesthatcareshouldbetakenwhe H n V applying the study of sea ice since the launch of Seasat in 1978 [10].
thesemeasurestotheiceareaswheresignificantlysmallfloesare While C-band SAR (4–8 GHz, wavelength = 3.8 − 7.5 cm)
dominant like the marginal ice zone. has been used most frequently for the polar sea ice research
IndexTerms—Cryosphere,deformedseaice,dynamics,remote andattemptstoestimateicesurfaceroughnesshavebeenmade
sensing, sea ice, synthetic aperture radar (SAR). (see[11],[12]),itwaspointedoutthatL-bandSAR(1–2 GHz,
15–30cm)is moresuitablefordiscriminatingridgedice from
I. INTRODUCTION level ice than C-band SAR from the comparative analysis of
airborneSARimagestargetedfortheArctic seaice [13],[14]
SEA ice plays an important role in shaping the polar
and satellite SAR images for the Baltic Sea [15] and for the
climate. Associated with the significant reduction in sea
saline ice of Lake Saroma, Hokkaido, Japan [16], and also
ice extentin the Arctic Ocean forseveraldecades, the Arctic-
thanX-bandSAR(8–12GHz,3cm)fromfieldmeasurements
wide warming trend is twice as fast as the surrounding
offAlaskancoastcoordinatedwithsatellite SAR images[17].
regions [1]. Therefore, it is quite important to reproduce the
Thisis becausethe backscattercoefficientof SAR is sensitive
seaiceextentandthicknessintheclimatemodelstopredictthe
to the surface roughness larger than the wavelength [18]
future climate in the Arctic region. However, it was reported
and the wavelength of L-band SAR is close to the surface
that none of the IntergovernmentalPanel on Climate Change
roughnessofdeformediceintheSIZ.ThecapabilityofL-band
(IPCC) climate models could reproduce the observed rapid
SAR for detecting ice features compared with C-band SAR
thinning trend of mean ice thickness in the Arctic Ocean
was confirmed not limited to the midwinter season, but also
Manuscript received June 8, 2020; revised September 18, 2020 and during the melt season [19], [20]. In fact, the capability of
October22,2020;acceptedNovember29,2020.DateofpublicationDecem- L-bandSARforextractingridgedicehadalreadybeenshown
ber 22, 2020; date of current version October 26, 2021. This work was
for the Beaufort Sea ice at the very early stage of the SAR
supportedbyJapanSocietyforthePromotionofScience (JSPS)KAKENHI
GrantNumbersJP16K00511,JP19K12304.(Correspondingauthor:Takenobu history [21]. However, to the authors’ knowledge, measures
Toyota.) for classification into ridged ice with L-band SAR, which is
Takenobu Toyota is with the Institute of Low Temperature Science,
applicable to wide areas, has not been developed yet except
Hokkaido University, Sapporo 060-0819, Japan (e-mail: toyota@lowtem.
hokudai.ac.jp). for lookup tables made up by several studies (see [14], [22]).
JunnoIshiyamaiswithTomaTownOffice, Hokkaido078-1393,Japan. Although fine polarimetric L-band SAR images were used
Noriaki Kimura is with Atmosphere and Ocean Research Institute, The
to develop measures to classify ice types (see [23], [24]),
University ofTokyo,Kashiwa277-8564,Japan.
Digital ObjectIdentifier 10.1109/TGRS.2020.3043335 the analysis area is relatively limited, and further study is
Thisworkislicensed underaCreative CommonsAttribution 4.0License. Formoreinformation, seehttps://creativecommons.org/licenses/by/4.0/

9362 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
0.3−0.5
|     |     |     |     |     |     |     | less than      | 1 m        | with the | mean   | being      |              | m [25] | although     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | -------- | ------ | ---------- | ------------ | ------ | ------------ |
|     |     |     |     |     |     |     | ridged ice     | of         | more     | than a | few meters |              | thick  | occasionally |
|     |     |     |     |     |     |     | appears        | [26]. This | region   | has    | several    | advantages   |        | over other   |
|     |     |     |     |     |     |     | polar regions. |            | First,   | since  | in situ    | observations |        | have been    |
conductedusingPV“Soya”everywinterincollaborationwith
JapanCoastGuard(JCG)since1996tosurveytheseaiceand
oceanographicconditionsandtotackleadhoctopicsrelatedto
|     |     |     |     |     |     |     | sea ice [Fig. | 1(b)],there |           | are     | available | field | data for    | validation |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --------- | ------- | --------- | ----- | ----------- | ---------- |
|     |     |     |     |     |     |     | to some       | extent.     | Second,   | this    | region    | does  | not contain | multi-     |
|     |     |     |     |     |     |     | year ice      | unlike      | the polar | oceans, | which     | makes | it          | simpler to |
classifyseaicetypes.Third,allthePhasedArraytypeL-band
|     |     |     |     |     |     |     | Synthetic         | Aperture | Radar    | (PALSAR) |           | images      | that                | overpassed |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | -------- | -------- | --------- | ----------- | ------------------- | ---------- |
|     |     |     |     |     |     |     | the southern      | Sea      | of       | Okhotsk  | in winter |             | were preferentially |            |
|     |     |     |     |     |     |     | acquired          | via the  | contract | between  | JCG       | and         | Japan               | Aerospace  |
|     |     |     |     |     |     |     | ExplorationAgency |          | (JAXA),  |          | which     | facilitates | the                 | monitoring |
ofdeformedice.Sincedeformediceinthisregionisproduced
|     |     |     |     |     |     |     | mainly         | by dynamical |                | thickening | processes     |                 | [9],          | [25], [27], |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | -------------- | ---------- | ------------- | --------------- | ------------- | ----------- |
|     |     |     |     |     |     |     | the monitoring |              | of deformed    |            | ice is        | expected        | to contribute | to          |
|     |     |     |     |     |     |     | clarifying     | the          | dynamical      | behavior.  |               | Hence,          | we attempted  | to          |
|     |     |     |     |     |     |     | develop        | measures     | to             | classify   | sea ice       | types           | using         | PALSAR,     |
|     |     |     |     |     |     |     | based on       | our field    | experiments.In |            | 2014,         | ALOS-2/PALSAR-2 |               |             |
|     |     |     |     |     |     |     | succeeded      | PALSAR,      |                | adding     | the functions |                 | of wider      | coverage    |
|     |     |     |     |     |     |     | with wider     | incidence    |                | angles     | (θ = 8◦–70◦)  |                 | and dual      | polariza-   |
i
|     |     |     |     |     |     |     | tions (HH,           | HV).        | These        | additional         |                            | functions   | provide             | us with     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- | ------------ | ------------------ | -------------------------- | ----------- | ------------------- | ----------- |
|     |     |     |     |     |     |     | an opportunity       |             | to examine   |                    | the applicability          |             | of L-band           | SAR         |
|     |     |     |     |     |     |     | for detecting        | deformed    |              | ice                | and the                    | properties  |                     | of HH and   |
|     |     |     |     |     |     |     | HV polarizationsmore |             |              | specifically.Thus, |                            |             | the purposesof      | this        |
|     |     |     |     |     |     |     | study are            | as follows: |              |                    |                            |             |                     |             |
|     |     |     |     |     |     |     | 1) to                | confirm     | the          | usability          | of L-band                  | SAR         | (PALSAR)            | for         |
|     |     |     |     |     |     |     | detecting            |             | deformed     | ice                | by comparing               |             | with                | a C-band    |
|     |     |     |     |     |     |     | SAR                  | image       | in           | the southern       | Sea                        | of Okhotsk; |                     |             |
|     |     |     |     |     |     |     | 2) to                | develop     | measures     |                    | to detect                  | deformed    |                     | ice using   |
|     |     |     |     |     |     |     | PALSARimageryata     |             |              |                    | ScanSARmode,andvalidatethe |             |                     |             |
|     |     |     |     |     |     |     | measures             |             | based        | on field           | experiments;               |             |                     |             |
|     |     |     |     |     |     |     | 3) to                | examine     | the          | properties         |                            | of          | dual polarizations  |             |
|     |     |     |     |     |     |     | (HH                  | and         | HV)          | with ScanSAR       |                            | mode        | (PALSAR-2)          | and         |
|     |     |     |     |     |     |     | the                  | capability  | of           | them               | for detecting              |             | deformed            | ice;        |
|     |     |     |     |     |     |     | 4) to                | investigate | factors      |                    | that can                   | affect      | the capability      | of          |
|     |     |     |     |     |     |     | L-band               | SAR         | for          | detecting          | deformed                   |             | ice quantitatively. |             |
|     |     |     |     |     |     |     | This article         |             | is organized |                    | by data                    | description | in                  | Section II, |
|     |     |     |     |     |     |     | development          | of          | the          | measures           | to classify                |             | sea ice             | into three  |
|     |     |     |     |     |     |     | ice types            | using       | PALSAR,      |                    | and validation             |             | of our              | measures    |
Fig. 1. Geographical maps of the observation area in the Sea ofOkhotsk. and investigation of dual polarizations using PALSAR-2 in
(a) Map of the whole Sea of Okhotsk. The normal sea ice extent on Section III, and discussion of the results in Section IV.
| February15      | (the average | during 1980–2010) |     | are shaded   | in sky-blue | and     |     |     |     |     |      |     |     |     |
| --------------- | ------------ | ----------------- | --- | ------------ | ----------- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- |
| the observation | points used  | for the algorithm |     | (Fig. 3) are | dotted in   | red for |     |     |     |     |      |     |     |     |
|                 |              |                   |     |              |             |         |     |     |     | II. | DATA |     |     |     |
deformedice,inblackforpancakeice,andingreenfornilas.Asquareframe
| corresponds | to the area of | (b). (b) Observation |     | area with | PV “Soya” | cruise |     |     |     |     |     |     |     |     |
| ----------- | -------------- | -------------------- | --- | --------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Intheanalysis,weattemptedtoestablishmeasurestodetect
tracks(solidlines)in2016–2019andtheapproximateiceedges(brokenlines)
|             |                |           |              |          |        |         | deformed | ice, | using | three | different | satellite | SAR | sensors. |
| ----------- | -------------- | --------- | ------------ | -------- | ------ | ------- | -------- | ---- | ----- | ----- | --------- | --------- | --- | -------- |
| during each | cruise period, | according | to the daily | ice maps | issued | by JCG. |          |      |       |       |           |           |     |          |
Different colors correspond to individual years. (https://www1.kaiho.mlit. To validate it, we used the data obtained from the field
go.jp/KAN1/drift_ice/ice_chart/ice_calendar.html).
|          |               |              |     |              |     |        | measurements. |         | Besides, | the           | meteorological |      | reanalysis    | data  |
| -------- | ------------- | ------------ | --- | ------------ | --- | ------ | ------------- | ------- | -------- | ------------- | -------------- | ---- | ------------- | ----- |
|          |               |              |     |              |     |        | set is also   | used    | as       | supplementary |                | data | for analysis. | Here, |
|          |               |              |     |              |     |        | we briefly    | explain | these    | data          | sets.          |      |               |       |
| required | to apply them | to satellite |     | SAR covering |     | a wide |               |         |          |               |                |      |               |       |
region.
|          |            |          |     |              |     |        | A. Satellite | SAR | Images |     |     |     |     |     |
| -------- | ---------- | -------- | --- | ------------ | --- | ------ | ------------ | --- | ------ | --- | --- | --- | --- | --- |
| In order | to develop | measures | to  | discriminate | ice | types, |              |     |        |     |     |     |     |     |
we focused on the sea ice in the southern Sea of Okhotsk as In this study,we focusedon the sea ice in the southernSea
|     |     |     |     |     |     |     | ofOkhotsk(43◦ |     |     | ◦ N,142◦ |     | ◦   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | --- | --- | --- | --- |
a typical SIZ [Fig. 1(a)]. The sea ice area becomesmaximum to50 to148 E,Fig.1),usingthree
at the end of February and the level ice thickness is mostly satellites SARs: PALSAR, RADARSAT-2, and PALSAR-2,

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9363
TABLEI February 13–17 in 2011 for developing the measures with
MAINSPECIFICATIONSOFSARsUSEDFORANALYSIS PALSARimages,andFebruary5–11in2016,February10–16
in 2017, February 8–14 in 2018, February 6–12 in 2019 for
the examination with PALSAR-2 images. The cruise tracks
are shown in Fig. 1(b). Among the data obtained during
these cruises, photos taken hourly from the upper deck
of the ship, aero-photos taken from the helicopter, ice
thickness data measured by means of a shipborne video
system [25], and hourly visual observations according to the
Antarctic Sea Ice Processes & Climate (ASPeCt) protocol
(http://aspect.antarctica.gov.au/)weremainlyusedforanalysis.
TABLEII
Although the ASPeCt protocol was originally designed for
ICECONDITIONSDURINGTHEOBSERVATIONPERIODS
Antarctic sea ice zone research [28], it can be applied to the
Sea of Okhotsk because it was found that the ice properties
there especially in the ice growth season are quite similar to
those of Antarctic sea ice [9].
Here, it should be noted that ice thickness measurementby
a video system is intended rather for relatively flat ice than
for significantly ridged ice. However, since the ice thickening
processesarecloselyrelatedtodeformationprocesses(rafting
and ridging) in this region [9], ice thickness data can be an
indicator of the degree of surface roughness to some extent.
Visual observationsinclude an estimate of the areal coverage,
all of which were observed with ScanSAR mode to cover thickness, floe size, topography, and snow cover of the three
a wide area. The main specifications of each SAR image dominanticetypeswithinaradiusofapproximately1kmfrom
are described in Table I. For each image, we used the data theship [28].At thesame time, threephotographs(left, front,
products, where multilook processing is performed (process- and right-side of the ship) were taken from the upper deck of
ing level: 1.5 for PALSAR and PALSAR-2, and SGF for theship,whichwerealsousedforvalidationoficeconditions.
RADARSAT-2). To further reduce the speckle noise, we took Basedonthesephotographs,seaicewascategorizedintothree
the average with the surrounding 3×3 pixels for each pixel. ice types: nilas (thin level ice), pancake (thin rough ice),
Thenominalresolutionsare71–157mforPALSAR,48–95m and deformed ice (thick rough ice), as shown in Fig. 2.
for PALSAR-2, and 73–163 m for RADARSAT-2, depending For the polar ice regions, probably we need an additional
on the range and azimuth directions. PALSAR images were category, stable (level) thick ice. However, this category was
used to develop measures to classify sea ice types. For not included here because in this region the thermodynamic
this purpose, the backscatter coefficients at HH polarization ice growth rate is limited even in winter due to abundant
(σ0 ) were analyzed with 35 images in total, which were solar radiation and first-year ice (thicker than 0.3 m) was
HH
obtainedin Januaryto Marchfrom2009to 2011.Tocompare shown to be usually deformed [9]. Therefore, we consider
the ability of detecting deformed ice between L-band and thatthreecategoriesareenoughinthisarea.Aero-photographs
C-band SARs, one RADARSAT-2 image, which was selected were taken from the helicopter at an interval of 5 min
sothattheobservationtimewastheclosesttooneofPALSAR during the flight to show the ice conditions in a wide
images, was analyzed with the PALSAR image. Only 4.6-h range.
time difference between these two images enabled direct Besides, to verify the temporal evolution of deformed ice
comparison. PALSAR-2 images were used to validate the regions, daily ice drift data were used. The ice drift data set
measures developed with PALSAR images, and to examine was constructed on a 37.5-km grid from the image of satel-
the capability of backscatter coefficients at HV polariza- lite microwave sensor, The Advanced Microwave Scanning
tion (σ0 ), compared with σ0 . The dates of the images Radiometer for EOS (AMSR-E), images using the maximum
HV HH
are February 10 and 11 in 2016, February 13 and 14 in correlationmethod[29].Theseaiceextentsonindividualdays
2017,February 12 and 13in2018,February7and11in2019 were determined with the AMSR-E-derived ice concentra-
(Table II), which were selected to overlap the “Soya” cruise tion data (https://seaice.uni-bremen.de/start/). When we need
period (Table II). The selection of two successive days for more detailed ice conditions, Moderate Resolution Imaging
eachyearexceptfor2019servedtoinvestigatethedependence Spectroradiometer (MODIS) images with a spatial resolu-
of σ0 and σ0 , which were calibrated, on a wide range of tion of 250 and 500 m (https://worldview.earthdata.nasa.gov/)
HH HV
θ because the ice conditions would remain nearly the same were referred to. When we need to examine the meteo-
i
duringthetwodays,whiletherangeofθ shiftedsignificantly. rological conditions at the time of the SAR observations,
i
the meteorological reanalysis data sets (ERA-Interim) with
B. Field Data for Validation a grid spacing of 0.125◦ were used, focusing mainly on
The sea ice observations aboard the PV “Soya” were con- 10-m wind data (http://apps.ecmwf.int/datasets/data/interim-
ductedduringFebruary8–13in2009,February4–10in2010, full-daily/levtype%3Dsfc/).

9364 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
σ0
|     |     |     |     |     |     | wavelength |     | (0.24 | m)  | [18], | of  | L-band | SAR | is expected | to  |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | --- | ----- | --- | ------ | --- | ----------- | --- |
HH
|     |     |     |     |     |     | discriminate |         | deformed      |        | ice                                 | from pancake |            | ice and          | nilas.    | Since   |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | ------------- | ------ | ----------------------------------- | ------------ | ---------- | ---------------- | --------- | ------- |
|     |     |     |     |     |     | σ0           | depends | significantly |        | on                                  | θ [31],      | we         | attempt          | to        | develop |
|     |     |     |     |     |     | HH           |         |               |        |                                     | i            |            |                  |           |         |
|     |     |     |     |     |     | measures     |         | to classify   |        | sea ice                             | into         | these      | three categories |           | as a    |
|     |     |     |     |     |     | functionofσ0 |         |               | andθ   | .Sofar,therehavebeenseveralattempts |              |            |                  |           |         |
|     |     |     |     |     |     |              |         | HH            |        | i                                   |              |            |                  |           |         |
|     |     |     |     |     |     |              |         | σ0            |        |                                     |              |            | θ                |           |         |
|     |     |     |     |     |     | which        | relate  |               | to ice | types                               | as a         | functionof |                  | i for the | polar   |
HH
|     |     |     |     |     |     | regions |             | from surface-based, |             |          | airborne,          | and     | satellite | SAR       | (see     |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | ------------------- | ----------- | -------- | ------------------ | ------- | --------- | --------- | -------- |
|     |     |     |     |     |     | [22],   | [32],       | [33]).              | However,    |          | the discrimination |         |           | of ice    | types is |
|     |     |     |     |     |     | not     | necessarily |                     | an easy     | problem  | because            |         | generally | the       | polar    |
|     |     |     |     |     |     | regions |             | contain             | various     | types    | of sea             | ice,    | including | multiyear |          |
|     |     |     |     |     |     | ice,    | first-year  |                     | ice, nilas, | pressure |                    | ridges, | and       | whatever  | at a     |
smallscale.Besides,therehasbeenadifficultyinestablishing
|     |     |     |     |     |     | measures |            | to discriminate  |              |     | sea ice   | types  | due             | to the        | limited |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ---------------- | ------------ | --- | --------- | ------ | --------------- | ------------- | ------- |
|     |     |     |     |     |     | number   |            | of observations. |              |     |           |        |                 |               |         |
|     |     |     |     |     |     |          | To develop | the              | measures,    |     | we used   | the    | photos          | taken         | hourly  |
|     |     |     |     |     |     | at       | the ASPeCt |                  | observations |     | during    | the    | cruise.         | We identified |         |
|     |     |     |     |     |     | the      | position   | of               | each photo   |     | on the    | PALSAR | images,         | using         | the     |
|     |     |     |     |     |     | GPS      | records,   | and              | estimated    |     | σ0 around |        | the observation |               | area    |
HH
dB.Sinceσ0
|     |     |     |     |     |     | withanaccuracyof2 |     |     |     |     |     | usuallyvariesonasmall |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
HH
scale(<1km),wefirstdeterminedthelowerandhigherlimits
|     |     |     |     |     |     | of  | σ0 within |     | a few | km range | of  | the position, |     | and | then the |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | -------- | --- | ------------- | --- | --- | -------- |
HH
σ0
|     |     |     |     |     |     | representative |     |     | was | obtained | by  | taking | the | average | of the |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | -------- | --- | ------ | --- | ------- | ------ |
HH
|     |     |     |     |     |     | two | limits. | θ   | was calculated |     | geometrically |     | from | the | relative |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------------- | --- | ------------- | --- | ---- | --- | -------- |
i
|     |     |     |     |     |     | position  |              | of the     | image.                    | The          | air temperature |               | range          | was            | from     |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | ---------- | ------------------------- | ------------ | --------------- | ------------- | -------------- | -------------- | -------- |
|     |     |     |     |     |     |           | ◦C           |            | ◦C.                       |              |                 |               |                |                |          |
|     |     |     |     |     |     | −10       |              | to −2      | If                        | we           | confined        | the           | data to        | the            | observa- |
|     |     |     |     |     |     | tion      | time         | of PALSAR, |                           | the          | number          | of data       | would          | be             | much     |
|     |     |     |     |     |     | reduced.  |              | Therefore, |                           | we included  |                 | the data      | taken          | within         | one      |
|     |     |     |     |     |     | day       | of the       | PALSAR     |                           | observation, |                 | if available. |                | The difference |          |
|     |     |     |     |     |     | in        | observation  |            | time between              |              | PALSAR          | and           | photographs    |                | was      |
|     |     |     |     |     |     | corrected |              | using      | reanalysis                |              | wind data       | on            | the assumption |                | that     |
|     |     |     |     |     |     | sea       | icedriftsata |            | rateof2%ofwind[34],andthe |              |                 |               |                | positionon     |          |
thePALSARimagewasestimated.Thenwemadescatterplots
|     |     |     |     |     |     | betweenσ0 |           | andθ    | inFig.3,whereicetypesarediscriminated |           |      |             |          |         |       |
| --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | ------------------------------------- | --------- | ---- | ----------- | -------- | ------- | ----- |
|     |     |     |     |     |     |           |           | HH      | i                                     |           |      |             |          |         |       |
|     |     |     |     |     |     | by        | different | colors. | The                                   | error     | bars | in Fig.     | 3 denote | the     | upper |
|     |     |     |     |     |     | and       | lower     | limits  | of                                    | σ0 around | the  | observation |          | points, | and   |
HH
|     |     |     |     |     |     | the | solid | circles | show | the representative |     |     | value | of σ0 | . Fig. 3 |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---- | ------------------ | --- | --- | ----- | ----- | -------- |
HH
|                                        |              |            |                  |              |             | sheds   | light      | on             | the possibility |            | to approximately |            |                      | classify | three     |
| -------------------------------------- | ------------ | ---------- | ---------------- | ------------ | ----------- | ------- | ---------- | -------------- | --------------- | ---------- | ---------------- | ---------- | -------------------- | -------- | --------- |
|                                        |              |            |                  |              |             | ice     | types      | by setting     | two             | threshold  |                  | lines.     | The observationsites |          |           |
|                                        |              |            |                  |              |             | of      | individual | plots          | are             | shown      | in               | Fig. 1(a). | It                   | is found | that      |
|                                        |              |            |                  |              |             | the     | data       | for deformed   |                 | ice        | come mainly      |            | from                 | inner    | ice area, |
| Fig. 2. Sample                         | photographs, | taken from | the ship,        | of ice types | categorized |         |            |                |                 |            |                  |            |                      |          |           |
|                                        |              |            |                  |              |             | whereas |            | the data       | for             | pancake    | ice and          | nilas      | from                 | the      | marginal  |
| inthisstudyas(a)deformedice,(b)pancake |              |            | ice,and(c)nilas. |              |             |         |            |                |                 |            |                  |            |                      |          |           |
|                                        |              |            |                  |              |             | ice     | zone       | (MIZ)          | and the         | near-shore |                  | region,    | respectively.        |          |           |
|                                        |              |            |                  |              |             |         | The two    | thresholdlines |                 | were       | derivedin        |            | the followingway:    |          |           |
III. ANALYTICAL METHODSAND RESULTS for the threshold between deformed ice and pancake ice,
|                |             |      |        |        |     |       |     |            |       |        |               |     |          |     | σ0 =     |
| -------------- | ----------- | ---- | ------ | ------ | --- | ----- | --- | ---------- | ----- | ------ | ------------- | --- | -------- | --- | -------- |
|                |             |      |        |        |     | first | the | regression | line  | was    | obtained      | in  | the form | of  |          |
| A. Development | of Measures | With | PALSAR | Images |     |       |     |            |       |        |               |     |          |     | HH       |
|                |             |      |        |        |     | aθ    | +b  | for the    | lower | limits | of individual |     | deformed |     | ice data |
i
1) Derivation of the Threshold Lines:: Although a quanti- in Fig. 3 with the least-squares method. The linear regression
tative estimate of surface roughness is difficult from our data was selected here based on Fig. 3, although [33] suggested
sources, it is possible to categorize the sea ice types into that the sensitivity of θ becomes higher for smaller θ . Next,
|     |     |     |     |     |     |     |     |     |     | i   |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deformedice,pancakeice,andnilas,asshowninFig.2,from another regression line was obtained in the same way for the
the photographs with certainty. The representative thickness upper limits of individual pancake ice data. By taking the
of each category is more than about 0.3 m for deformed ice, average of these two regression lines, the threshold line was
0.1–0.3 mforpancakeice,andlessthan0.1mfornilas.From derived.Thesameprocedurewasappliedforthethresholdline
theviewpointofroughness,eachcategorycorrespondstothick between pancake ice and nilas. The threshold lines obtained
equation:
rough ice, thin rough ice, and thin level ice, respectively. are expressed in the following
| Considering   | that the penetration |     | depth | of L-band     | radar  | is  |       |     |         |        |     |          |           |     |     |
| ------------- | -------------------- | --- | ----- | ------------- | ------ | --- | ----- | --- | ------- | ------ | --- | -------- | --------- | --- | --- |
|               |                      |     |       |               |        |     | σ0    | =   | −0.197θ | −7.55  |     |          | pan.−def. |     |     |
|               |                      |     |       |               |        |     |       |     |         | i      |     | (dB) for |           |     | (1) |
| about 0.3–0.5 | m for first-year     | ice | [30]  | and the radar | signal | is  | HH_pd |     |         |        |     |          |           |     |     |
|               |                      |     |       |               |        |     | σ0    | =   | −0.194θ | −11.51 |     |          | nil.−pan. |     |     |
sensitive to the surface roughness at a scale greater than its (dB) for (2)
|     |     |     |     |     |     |     |     | HH_np |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9365
Fig. 3. Scatterplots between σ H 0 H and θ i with ice types differentiated by color: red fordeformed ice, green for pancake ice, and blue fornilas. There are
24 plots in total. See Fig. 1(a) forthe locations ofthe data. The thresholds between deformed ice and pancake ice, and between pancake ice and nilas are
presented bylines inorangeandlightblue,respectively.
It is noted that the incidence angle dependencies of these slightshiftof theice area duringtheobservationtimeinterval
equations(−0.19to −0.20dB per degree)is close to the past between the two images, which is estimated to be about
result [35] (−0.21 dB per degree) for Arctic first-year sea 1 km for the representative ice drift speed (∼0.1 m · s−1),
ice. Here, it should be kept in mind that these measures were the averages were taken within the circle of 1 km radius at
derived from the data obtained for 20◦ ≤ θ ≤ 42◦. It should eachpixelonL1.Tofocusonseaice,onlytherangeindicated
i
also be noticed that these measures are applicable to sea ice by an arrow in Fig. 4, corresponding to 25◦ ≤θ ≤ 34◦ on a
i
with L-bandSAR because the incidenceangledependenceon PALSAR image,is drawn.The characteristicsof Fig. 5(a) are
seawater is much steeper, as shown later, and the brightness summarized as follows.
at L-band correlates more directly to deformation than that 1) Within sea ice area, whereasone peak which appearsat
at C- or X-band. To apply them to other sea ice regions, about 240 km in the deformed ice region is prominent
furtherstudyisrequired.Consideringthatσ0 becomeshigher for PALSAR, several comparable peaks are found not
HH
with the increase of the ice surface roughness and thickness onlyinthedeformediceregion(about250km)butalso
at a given θ [12], [36]–[38]), the upward deviation from (1) in the pancake ice area (about 300 km, 320 km) for
i
is expected to be an indicator of the degree of deformation. RADARSAT-2.
Hereafter, we use (1) and (2) to classify ice types. 2) The difference in σ0 between nilas and deformed ice
HH
2) Comparison Between PALSAR and RADARSAT-2: is somewhat larger for PALSAR (∼9 dB) than for
To examine the effectiveness of L-band SAR for detecting RADARSAT-2 (∼6 dB).
deformed ice to C-band SAR, which has been shown previ- 3) Thecontrastofσ0 betweenopenwaterandseaicearea
HH
ously in polar regions (see [14]), a comparative analysis was is stronger for RADARSAT-2 than for PALSAR.
done between a set of PALSAR and RADARSAT-2 images, First two points indicate that PALSAR is more useful to
covering the same area almost concurrently.Fig. 4 shows the discriminate deformed ice from both thin rough ice (pancake
distributions of σ0 for both satellite images. In the analysis, ice) and thin level ice (nilas) than C-band SAR. This feature
HH
we focused on how the RADARSAT-2 image represents the is consistent with the past studies [14], [16]. Although the
icetypesjudgedfromPALSAR-derivedmeasuresasexpressed third point is opposite to the result of [14], we infer that the
by (1) and (2). To address it, we set a line for cross section result depends on the sea surface conditions because C-band
(L1) and two characteristic areas (A1 and A2) for statistics SARsignalissensitivetorelativelysmallroughness[16].Itis
within sea ice area (Fig. 4) and examined the properties notedinFig.5(a)thattheiceedgeisshiftedeastwardbyafew
individually. km in a PALSAR image relative to a RADARSAT-2 image.
Fig. 5(a) shows the cross sections of σ0 along L1 for Considering the persistent southerly winds of ∼10 m · s−1
HH
PALSAR and RADARSAT-2, drawn as a functionof distance during the observation time interval, and the sharp angle
from the right-side end. L1 was selected so as to contain between the ice edges and L1, the discrepancy of ice edges
as many ice types as possible, covering a wide area in the is attributed to the slight northwardmovementof sea ice area
direction perpendicular to the satellite orbit. Considering the rather than the properties of radar signals.

9366 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
in A1, A2 is mainly composed of deformed ice. The his-
tograms of σ0 within A1 and A2 are shown in Fig. 5(b)
HH
for individual images. According to (1), the threshold values
of σ0 for PALSAR between deformed ice and pancake ice
HH
are −14.2 dB at A1 (θ = 33.5◦) and −12.0 dB at A2 (θ =
i i
22.6◦). Therefore,Fig. 5(b) shows thatA2 is occupiedalmost
completely with deformed ice, while A1 is covered largely
with nilas and pancake ice but only slightly (3.6%) with
deformedice. Fig. 5(b) shows that whereasthe rangesof σ0
HH
for PALSAR are clearly separated between A1 and A2, those
for RADARSAT-2 are significantly overlapped. Considering
theeffectofθ forRADARSAT-2,theoverlappedrangewould
i
increase further. Besides, the peak in the histogram of A2 is
muchhigherandsharperforPALSARthanforRADARSAT-2.
This indicates that L-band SAR is much more useful to
discriminatedeformedicefromthinleveliceorthinroughice,
comparedwithC-bandSAR,whichisconsistentwithFig.5(a)
and past studies (see [14], [16]).
3) Mapping of Deformed Ice: As a next step, we attempt
to find out the features of temporalevolution of deformedice
regions by mapping them from January to March in 2010.
To minimize the speckle noises which often appear at a pixel
scale, we took the following method: first, we categorized
each pixel into deformed ice, pancake ice, and nilas, using
(1) and (2). Then, we set windows composed of 9 × 9 pixels
(about 1 km square) and calculated the fractions of each ice
type (F , F , and F ) by
d p n
N N N
F = d , F = p , F = n (3)
d 9×9 p 9×9 n 9×9
where N , N , and N denote the number of pixels catego-
d p n
rized into deformed ice, pancake ice, and nilas, respectively.
By mapping F for each PALSAR image, we obtained the
d
temporal evolution of deformed ice regions in the southern
SeaofOkhotsk.Sinceitisdifficulttodistinguishbetweensea
iceandopenwaterjustfromPALSAR,we determinedseaice
extentbytheareawhereiceconcentrationisgreaterthan15%
in the AMSR-E-derived ice concentration maps.
The results show that sea ice area started to extend around
the Gulf of Patience off Sakhalin [Fig. 1(a)] with deformed
ice occupying about half of the total ice area on January 7,
and spread rapidly to cover the wide area off Sakhalin with
a decrease in deformed ice regions by January 31, probably
because deformed ice was disintegrated by the divergent
motion caused by prevailing easterly winds. In February,
sea ice area further spread southward to cover the area
Fig.4. σ0 distribution of(a)PALSARand(b)RADARAT-2,whichwere
HH aroundHokkaido,with largetemporalvariabilityof deformed
observed nearly at thesametime(01:13 UTCforPALSARand20:36UTC
forRadarsat-2).Timedifferenceisonly4h37m.Aredline(L1)showsthe ice regions. In March, sea ice area began to retreat northward
cross-sectionallineforFig.5(a),whiletworedcircles(A1andA2)showthe until the end of March. In these figures, deformedice regions
areausedforstatistics inFig.5(b).
arecharacterizedby:1)largetemporalvariabilityofthemand
2) rather aligned distribution with about a few tens of km in
To minimize such discrepancy caused by the slight move- width and about a few hundreds of km in length.
ment (∼1 km) of sea ice area, it would be better to compare To verify these characteristics from a physical view-
the statistics of areal distribution of σ0 between the two point, two successive maps on February 17 [Fig. 6(a)] and
HH
images. To do so, we selected two characteristic circular 22 [Fig. 6(b)] are shown as an example. It is noticeable that
areas (A1 and A2) with a radius of 15 km within sea ice the deformed ice region increased significantly in a wide
area. According to Fig. 4(a) and MODIS images, whereas area off east Sakhalin during this period. For comparison,
mixture of pancake ice and nilas is the dominant category we mapped the mean divergence/convergence pattern of sea

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9367
Fig. 5. Comparative analysis between PALSAR and RADARSAT-2 (a) Cross sections of σ0 along L1 in Fig. 4 for PALSAR (red) and RADARSAT-2
HH
(black) with a focus on the range pointed by the arrow in Fig. 4. Ice types described in the figure were derived from the threshold curves of (1) and (2).
OpenwaterareawasdeterminedfromtheAMSR-E-derivediceconcentration mapandMODISimagesonFebruary22,2010.(b)Histogramsofσ0 within
HH
A1 and A2 in Fig. 4 for (Left) PALSAR and (Right) RADARSAT-2. Two vertical broken lines denote the thresholds between nilas and pancake ice and
betweenpancakeiceanddeformediceatA1(θ
i
=33.5◦)andA2(θ
i
=22.6◦),determinedby(1)and(2).NotethatwhereasA2iscoveredalmostcompletely
withdeformedice,A1mostlywithnilas andpancake ice.

9368 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
Fig.6. Examplesofthedeformediceareafractionextractedusingouralgorithm(a)onFebruary17and(b)February22,2010,and(c)meandivergenceof
AMSR-E-derived icedriftduringFebruary17–21,2010.Notethatdeformedicefraction(Fd >0%)increased eastofSakhalin significantly, consistent with
theicedriftconvergence patternthere.
ice drift during this period, using AMSR-E-derived ice drift judgedasdeformedicefromourmeasures,appearscommonly
data [Fig. 6(c)]. This figure shows that ice drift convergence in the MIZalongthe ice edges,as shownin Fig. 6(a)and(b),
is prominentespecially off east Sakhalin, where deformedice irrespective of ice drift conditions. Although it might be
regions increased. This applies in most cases and therefore possible that deformation processes become more active due
supports the validity of our measures to some extent. At the to wave–ice interaction in the MIZ, there is a possibil-
sametime,itisalsonoticedthatinmostofthemaps,thearea, ity that other factors affected the radar signal significantly.

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9369
Fig. 7. MODIS images during the observations onboard the PV “Soya” in the southern Sea of Okhotsk for 2016–2019, showing the representative ice
conditions ineachyear.Notethaticeconditions aresignificantly different amongthesefouryears (Datasource:https://worldview.earthdata.nasa.gov/).
Thus, our measures need further examination from field Meanthicknesswithastandarddeviationineachyearislisted
observations. inTableII.Itisclearlyshownthatasawholeicethicknesswas
significantlythickerin2018(meanicethickness:0.46m)than
in2016(0.19m)and2019(0.17m).Asa whole,the orderof
B. Further Examination With ALOS-2/PALSAR-2Images yearsformeanicethicknessis2016≈20192017<2018.
Here, our measures are tested for PALSAR-2, which has The major differencebetween 2016and 2019 is dominantice
theadditionalfunctionsofdualpolarizationatScanSARmode type: pancake ice in 2016 and nilas in 2019, reflecting the
(Swathwidth:350–490km)andawiderrangeofθ (8◦–70◦), difference in ice thickness variation between these two years
i
to examine to what extent they are available and how they in Fig. 8. The ice thickness in 2017 is rather close to the
can benefit from dual polarization data, based on the field normal, averaged for 20 years (Table II).
observations conducted onboard the PV “Soya” in Februaries The characteristic of the ridge statistics in each year is
for four years (2016–2019). coincident with ice thickness in Table II, where the fractions
1) Ice Conditions in 2016–2019:The ice conditionsduring of ridged ice area and volume were calculated, based on
the observation periods were significantly different, as shown the ASPeCt observations, in the same way that [39] did
inMODISimages(Fig.7).Whereasnewlyformedicecovered for Antarctic sea ice. According to Table II, deformed ice
a wide area in this region in 2016 and 2019, developed contributed about half of the total area and about 90% of the
ice was prominent in 2017 and especially in 2018. This is total ice volume in 2018, significantly higher compared with
elucidated by the statistics of ice thickness data monitoredby other years. Again, the statistics of deformed ice in 2017 is
thevideosystemandvisualobservationsbasedontheASPeCt closetothenormal.Theorderofyearsfordegreeofdeformed
protocol. For comparison, all ice thickness data are plotted ice is 2016 ≈ 2019  2017 < 2018, which is the same
as a function of latitude in Fig. 8 for the individual years. as for ice thickness. This result confirms that ice thickness

9370 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
Fig.8. Icethickness distribution obtained fromthevideosystem,asafunction oflatitude for(a)2016,(b)2017,(c)2018,and(d)2019.
distribution can be a good proxy for the degree of surface 2) Validation From Field Measurements: To validate our
roughnessinthisregion.Anotherdifferenticefeaturebetween measures based on field data, we obtained σ0 and θ at the
HH i
the four years is dominant floe size: pancake ice in 2016, ship position at the observation time and compared the ice
2–20 m in 2017, 20–100 m in 2018, and nilas in 2019. Such categorypredictedbythemeasureswiththerealiceconditions
a significantlydifferentice conditionsamongthese fouryears around the ship. Considering its high spatial variability, σ0
HH
will serve to interpret the properties of PALSAR-2 images. isgivenby(mean)± (astandarddeviation)withintheareaof

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9371
TABLEIII or topography, and thereby is expected to be more sensitive
VALIDATIONOFOURALGORITHMWITHALOS-2/PALSAR-2 to vertical structure and less sensitive to θ
i
[10]. Hence, they
state that cross-polarization SAR (σ0 ) is more suitable for
HV
mapping ice deformation features such as ridges and rubble
areas especially for first-year ice which is less affected by
air bubbles. The second, third, and fourth points are well
explained by this property.
To show the differencebetween σ0 and σ0 more clearly,
HH HV
their cross sections along L1 [in Fig. 10(a)] are drawn
in Fig. 11. The data on February 12 and 13 are superimposed
to see the dependence on a wide range of θ , assuming that
i
the ice conditions did not change much during these two
days. Since the ice conditions are usually quite different
between the MIZ and inner ice pack area, inner ice pack
area is marked in Fig. 11. Fig. 11 elucidates the features
2km×2kmaroundtheship.Sincethemeasureswerederived (Points 1–4) found in Fig. 10. Especially, Points 2 is clearly
from PALSAR for 20◦ <θ < 42◦ (Fig. 3), it would be ideal shown at 30◦ ≤θ i ≤ 45◦ on February 12 and 7◦ ≤ θ i ≤ 17◦
i
on February 13, where σ0 decreases with the increase of
thatvalidationbe done within thisrange.However,dueto the HH
θ more rapidly than σ0 . This result is comparable to [13]
limited number of observations we extrapolated the measures i HV
somewhat for θ less than 20◦ or larger than 42◦. The results (compare with their Fig. 7). Besides, it is noticeable that for
i both σ0 and σ0 at 30◦ ≤ θ ≤ 45◦, the decreasing rate
are shown in Table III. HH HV i
with the increase of θ is more rapid in the open water on
Focusing on the cases where our ship was in the ice i
February 13 compared with sea ice area on February 12,
area, five points were available for validation. According to
indicating that in sea ice area both radar signals are less
Table III, the measures represent the real conditions well.
As an example, three sets of the σ0 maps and photos are sensitive to θ i compared with open water. This property is
HH coincident with the past results for C-band σ0 [33].
shown in Fig. 9. Especially for the case of February 13, HH
In Fig. 11, extremely low values of σ0 and σ0 appear
2018 [Fig. 9(c) and (d)], our ship was surrounded by a HH HV
at θ ≈ 51◦ near the western ice edge on February 12.
vast pancake ice area near the ice edge, which was well i
Considering the on-ice winds (i.e., westerly) of 5–15 m·s−1
predictedby our measures. For the case of February13, 2017
and cold air temperature (−9 ◦C to −7 ◦C) on this day, it is
[Fig. 9(a) and (b)], deformed ice floes can certainly be found
likely that significantly flat sea surface produced due to wave
in the photo.In Fig. 9(e) and (f), new ice sheet (nilas) is well
attenuationinthepresenceofgreaseiceismostresponsiblefor
represented. Thus, it can be said that our measures work well
this. This speculation is supported by the in situ observation
to some extent to classify sea ice into three categories. If we
can assume that σ0 is most sensitive to surface roughness conducted in the similar situation in the same area during the
HH
at a given θ , the upward deviation from the threshold line cruise in 2016. The on-site ice sampling observation revealed
i
thatthe observationarea was coveredwith grease ice of 8 cm
(1) is considered to represent the degree of ice deformation.
thick,andbothσ0 andσ0 showedabout8-dBlowervalues,
Therefore, hereafter the deviation from (1) is referred to as HH HV
compared with the surrounding area. This result is similar to
HH anomaly, expressed as
that of [40], which found a frazil slick near the ice edge
(HH anomaly)=σ0 −σ0 (dB) (4) appears dark on Seasat SAR (L-band) images. Considering
HH HH_pd
that seawater surface within inner sea ice area tends to be
and will be used to examine the validity for detecting signifi-
considerably flat due to wave attenuation, this justifies the
cantly deformed ice.
assumption that basically the SAR signals in inner sea ice
3)PropertiesofDualPolarization:Toexamineandcompare
area representthe propertiesof sea ice, much less affected by
the general properties of HH and HV polarizations, one set
seawater.
of images obtained on February 12, 2018 are exemplified
Onthe otherhand,in lessconcentratedsea ice arealikethe
in Fig. 10. The features found in Fig. 10 are listed as
MIZ, seawater surface may become rough forced by winds
follows.
and waves. In such a case, the radar signals from sea surface
1) As a whole σ H 0 V is about 10 dB lower than σ H 0 H . may becomecomparableto those from sea ice. To extractsea
2) A strong dependence on θ i for both polarizations, with ice properties, we need to know how the radar signals from
σ H 0 V being less affected by θ i within the sea ice area. sea surface depend on surface conditions and θ i . To this end,
3) σ H 0 V has some advantage in detecting sea ice area for we selected open water area along L1 in each PALSAR-2
smaller θ i . image carefully,referringto MODISimages, andthen plotted
4) The contrast between sea and land is much greater at σ0 and σ0 all together as a function of θ in Fig. 12.
σ H 0 V than at σ H 0 H . It H i H s found H t V hat whereas the variation range of i σ H 0 H exceeds
Ingeneral,σ0 atL-bandislesssensitivetointernalvolume 7 dB at a given θ , caused by Bragg-scattering under various
HV i
scattering from bubbles and brine pockets and is enhanced wind speeds, ranging from 2 to 13 m·s−1 [41], [42], that
mainly by multiple bouncing produced by surface roughness of σ0 is much reduced to mostly less than 5 dB. This
HV

9372 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
Fig. 9. Three sets of the distribution of σ0 for (Left) PALSAR-2 and (Right) photographs showing the ice conditions (circles) around the ship at the
HH
observationtime.(a)and(b)OnFebruary13,2017.(c)and(d)OnFebruary13,2018.(e)and(f)OnFebruary7,2019.“+”inred[(a)and(e)]andinblack
(c)denotes theshipposition. Thebrokenlines inthefigures(a),(c),and(e)denote iceedges determined byJCG.
means that σ0 is not so sensitive to sea surface conditions The regression line is drawn in Fig. 12 with the root mean
HV
| σ0  |     | 26◦ ≤ θ | ≤ 46◦. |     |     | deviationofσ0 |     |     |     |
| --- | --- | ------- | ------ | --- | --- | ------------- | --- | --- | --- |
as especially for This is probably square error(1.03dB). Since the from (5) is
| HH  |     | i   |     |     |     |     |     | HV  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
because in most cases, sea surface slope is not steep enough considered to be caused mainly by steep surface produced on
to generate the cross-polarization component significantly, ice, we refer to it as HV anomaly to represent the degree of
as pointed out by Dierking [31]. Based on almost linear ice surface roughness hereafter. HV anomaly is expressed as
| relationshipbetweenσ0 |     | andθ for26◦ | ≤θ ≤46◦ inFig.12, | follows: |     |     |     |     |     |
| --------------------- | --- | ----------- | ----------------- | -------- | --- | --- | --- | --- | --- |
|                       |     | HV i        | i                 |          |     |     |     |     |     |
itcanbeassumedthatthissloperepresentsthedependenceof (HV anomaly)=σ0 −σ0 .
(6)
σ0 on θ for flat surface to some extent within this range HV HV_ow
HV i
| θ   |     |     |     | Here,itshouldbenotedthatthedependenceofσ |     |     |     | 0 onθ | is  |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ----- | --- |
of i . Hence a regression line, as expressed by (5), was H V i
derived with the least-squares method as a reference for flat somewhatweakerforseaicethanforopenwater,asmentioned
surface earlier. Therefore, HV anomaly may be somewhat affected
θ
|     |     |     |     | by i . Even | so, it would | be possible | to use this | parameter | as  |
| --- | --- | --- | --- | ----------- | ------------ | ----------- | ----------- | --------- | --- |
σ0 =−0.636θ −5.78 (dB). (5) an indicator of ice surface roughnesswhen the variation of θ
|     | HV_ow | i   |     |     |     |     |     |     | i   |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9373
Fig.10. Distribution of(a)σ0 and(b)σ0 onFebruary 12,2018.Notethateach colortoneis settohavethesameintervals between thetwofiguresto
facilitate comparison. Thebrok H e H n lines deno H t V e iceedges determined withcomprehensive databyJCG.θ i is25.7◦ atthenearest range(right-hand side)and
55.5◦ atthefarthest range(left-hand side).Thecross-sectional lineL1in(a)isthesameasthatshowninFig.4.
is small. Ideally, it would be desirable to define HV anomaly significantly different ice conditions among the four years
bythedeviationfromσ atlevelsea icelikenilas.However, facilitate to interpret the results. HH and HV anomalies
HV
we took this method here because our data were too limited are plotted as a function of latitude in Fig. 13(a) and (b),
to derive a formula for level sea ice. respectively. To apply (4) and (6), the image where θ along
i
4) Properties of HH and HV Anomalies: In this section, L2 is within the range of 26◦ ≤ θ ≤ 46◦ was selected in
i
we verify to what extent HH anomaly and HV anomaly, each year.
introducedintheprevioussection,canrepresentthedegreeof In both Fig. 13(a) and (b), the values in each year are
ice deformation. For this purpose, we took the cross sections clearly distinguished, reflecting the individual ice conditions.
of σ0 and σ0 along L2 of 150 km length in Fig. 10(a) Unexpectedly, it is remarkable that as a whole the order of
HH HV
and compared the results among the four years. Line L2 was HH anomaly is 2019 < 2016 ≈ 2018 < 2017 in Fig. 13(a)
selected so that it lies within the ice-covered area in all the and that of HV anomaly is 2019 < 2016 < 2018 < 2017 in
years and its direction is parallel to the satellite orbit, i.e., θ Fig. 13(b), both of which do not coincide with the order of
i
is kept constant on the cross section line, to minimize the meanicethicknessinTableII(2016≈20192017<2018).
effects of open water area and θ . It is expected that the To confirm this discrepancy, we recalculated mean ice
i

9374 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
F 25 ig .7 . ◦ 1 – 1 5 . 5.5◦ Cr f o o s r s F s e e b c r t u io ar n y o 1 f 2 σ a H 0 n H d ( 6 b .1 la ◦ c – k 4 ) 5. a 4 n ◦ d fo σ r H 0 V Fe ( b r r e u d a ) ry al 1 o 3 n . g T L h 1 e i s n ign F i i fi g c . a 1 n 0 tl ( y a) h o ig n h F v e a b l r u u e a s ry of 1 σ 2 H 0 ( V th a in tθ l i in ∼ e) 2 a 6 n ◦ d co 1 r 3 re ( s t p h o ic n k d l t i o ne I ) tu i r n up 20 Is 1 l 8 a . nd T . he range of θ i is
Fig.12. Backscatter coefficients forHH(black)andHV(red)polarization intheopenwaterarea,plottedasafunctionofθ i withlinesofregression(solid
sky-blue)androotmeansquareerror(brokensky-blue).
thickness for the limited areas around L2. The result was in 2016 are much higher than in 2019, considering that the
0.23 ± 0.13 m for 2016, 0.39 ± 0.17 m for 2017, dominantice type is pancake ice in 2016. On the other hand,
0.46 ± 0.23 m for 2018, and 0.20 ± 0.11 m for 2019, which given the significant difference in ice thickness conditions
is almost the same as the total average. between 2016 and 2018 (Fig. 8), it is noticeable that HH
Among the above results, coincident with ice thickness anomaly is almost the same between these two years. As for
distribution are significantly lower values of HH and HV HV anomaly, the difference in θ between these two years
i
anomalies in 2019. It is prominent especially to the south might affect the result. However, it should be noted that HV
of 44.9◦ N. In this year nilas was dominant, occupying 35% anomaly in 2017 is constantly higher than in 2018 even for
of the total sea ice area in the observation area (Fig. 14). the same θ (= 45.6◦).
i
Although mean ice thickness is almost the same between Thus, our results indicate that only the effect of ice sur-
2016 and 2019, it is reasonable that HH and HV anomalies face roughness, i.e., the degree of ice deformation, cannot

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9375
Fig.13. Crosssectionof(a)HHanomalyand(b)HVanomalyalongL2inFig.10(a),whereHHanomalymeansthedeviationofσ0 from(1),whileHV
HH
anomaly means the deviation ofσ0 from(4). Bothanomalies were introduced torepresent the degree ofdeformation. Thenumbers in parentheses denote
HV
incidence angleoflineL2ineachPALSAR-2image.
explain Fig. 13 and another effect should be considered to yearswith the categoryof 2–20 m beingdominantwith 44%.
explain the observed σ0 and σ0 . This will be discussed On the other hand, ice floe in 2019 is characterized by the
HH HV
in Section IV. dominance of nilas, occupying 35%. These features were
confirmedfromaerophotostakennearL2fromthehelicopter
(not shown). Whereas tiny floes less than a few meters are
IV. DISCUSSION
dominanteven in the midst of sea ice area in 2016, relatively
A. Possible Effects of Floe Size on σ H 0 H and σ H 0 V small floes (∼a few tens of meters) in 2017 and large floes
Here we discuss the possible factors other than ice surface (∼a few hundreds of meters) in 2018 are prominent.
roughness, which can affect the radar signals, to explain the The effect of floe size on the radar backscatter
discrepancy discussed in the previous section. Since seawater was suggested by previous studies from C-band SAR.
intheseaiceareaandgreaseiceusuallyhaveasmoothsurface Sandven et al. [43] showed from concurrent field measure-
due to wave attenuation, it is unlikely that they affected σ0 ments with ERS 1 SAR near the MIZ in the Barents Sea that
HH
andσ0 significantlybecausethesmoothsurfacesaresomuch σ0 at C-band is about 5 dB higher for small floes (∼20 m)
HV VV
weaker/darkerthattheirvariationcannotexplainthelargevari- than for large floes (>500 m). If their results are applicable
ations observed. Therefore, the plausible factors should come for σ0 at L-bandSAR, HH anomalyin 2018becomeslarger
HH
from the sea ice properties. As mentioned in Section III-B1, than that in 2017, as expected. Thus, that may explain the
another different ice feature between four years is dominant discrepancyin 2018.However,to ourknowledge,quantitative
floe size. Fig. 14 shows the histogramsof each floe size cate- estimates about the effect of floe sizes at L-band SAR are
goryforindividualyears,compiledfromASPeCtobservations. few. Although Dierking and Busch [14] made a lookup table
As a whole, the order of floe sizes is 2016 < 2017  2018. forice classifications with JERS-1 (σ0 at L-band)separately
HH
In 2016 pancake ice, occupying 34% of total sea ice area, forfracturedice andconsolidatedice,theirdifferencewasnot
is dominant and the largest floe category is 20–100 m with necessarily clear.
only3%,whereasin2018thedominantcategoryis20–100m How can floe size distribution affect the radar signal? The
with 29% and even floes larger than 2 km occupied 10%. possible mechanism is explained by the schematic picture
In 2017, floe size conditions are intermediate between these in Fig. 15. For a given ice concentration, the total perimeter

9376 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
Fig.14. Histograms ofseaice floesizeobtained fromASPeCtobservations for(a)2016,(b)2017, (c)2018,and(d)2019.Thenotation offloesizeisas
follows:F:frazilice, P:pancake ice, N:nilas, B:brashice,R1:2–20m,R2:20–100m,R3:100–500m,R4:500m–2km,andR5:>2km.
| of ice floes,                                 | i.e., | the total | length of | the boundaries |         | between calculated by |     |     |     |     |
| --------------------------------------------- | ----- | --------- | --------- | -------------- | ------- | --------------------- | --- | --- | --- | --- |
| sea iceandseawater,becomeslongerasthefloesize |       |           |           |                | becomes |                       |     |     |     |     |
(cid:4)M
| smaller.   | Considering | that     | sea ice freeboard |     | creates   | more or  |       |         |     |     |
| ---------- | ----------- | -------- | ----------------- | --- | --------- | -------- | ----- | ------- | --- | --- |
|            |             |          |                   |     |           |          | P =   | (4A )/D |     |     |
|            |             |          |                   |     |           |          | total | i i     |     | (7) |
| less steep | roughness   | at those | boundaries,       | it  | is likely | that the |       |         |     |     |
i=1
| radar backscatter |     | is enhanced | at ice | margins | at both | HH and |     |     |     |     |
| ----------------- | --- | ----------- | ------ | ------- | ------- | ------ | --- | --- | --- | --- |
HV polarizations as well as in the inner deformed ice region. where M, A , and D are the number of categories, the areal
i i
Therefore, it seems reasonable that this mechanism works fraction of category i, and the representative floe size of
to decrease the total radar backscatter when floe sizes are category i, respectively. The calculated P per unit area
total
|     |     |     |     |     |     | km2) 2.91×106 |     | 1.49×106 |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --- | --- |
significantly larger than normal like 2018, and vice versa. (1 is m for 2016, m for 2017,
Although the lookup table by Dierking and Busch [14] is not 0.74×106 mfor2018,and1.26×106 mfor2019.Referenced
necessarily clear, when looking at the bright ice floe margins tothevaluein2017close tothenormal,the ratioisestimated
in their Figs. 3 and 4 and Plates 1-3of [44],it is obviousthat as1.95for2016,0.50for2018,and0.85for2019.Therefore,
this effect is significant for σ0 at L-band. roughlyestimated,thetotalperimeterin2016istwiceof2017,
HH
To be more specific, we estimate the approximate ratio four times of 2018, and 2.3 times of 2019.
of total perimeter between these four years, based on the Giventhe factthattheHH anomalyin 2016withsmalland
floe size histogram in Fig. 14. In calculation, the floe size little deformed ice floes is comparable to that in 2018 with
for each category is represented by 0.5 m for pancake ice, large and much deformed ice [Table II, Fig. 13(a)], it is
2 m for brash ice, 10 m for 2–20 m, 50 m for 20–100 m, inferred that the effect of four times total perimeter on HH
| 300 m for | 100–500 | km, 1000 | m for | 0.5–2 | km, and | 2000 m                       |     |                   |            |     |
| --------- | ------- | -------- | ----- | ----- | ------- | ---------------------------- | --- | ----------------- | ---------- | --- |
|           |         |          |       |       |         | anomalyis almostcomparableto |     | twice ice surface | roughness, |     |
>2
for km. No perimeter is assumed for grease ice and nilas. assuming that ice surface roughness is proportional to ice
Suppose A and D to be the given total sea ice area and thickness. The reason why HH anomaly was the highest
floe diameter,(cid:2)respec(cid:3)tively. The number of ice floes is given in 2017 is presumably because the ice thickness and floe size
by N = 4A/ πD2 and then the total perimeter becomes conditionswereclose to thenormalandourmeasuresworked
P = N · πD = 4A/D. In this way, the total perimeter effectively, compared with 2016 and 2018. The lowest HH
of sea ice including all categories for each year can be anomalyin2019isattributedmainlytothedominanceofnilas.

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9377
Fig.15. Schematic pictures, showing howfloesizedistribution affects σ0 andσ0 .(a)Forsmaller icefloes withlessdeformed icelike 2016and2017.
|     |     |     |     |     |     | HH HV |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
(b)Forlargericefloeswithmuchdeformedicelike2018.Icefloesin2019arecharacterized bydominanceofnilas,asshowninFig.14.Inthefigures,red
| andbluearrowsdenotebackscattering |     | atthedeformediceandicemargins,respectively. |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Considering that the mean HH anomaly along L2 is that at sea ice. Considering that θ is relatively low at the
i
−3.3 ±
2.9 dB in 2019, which is close to the threshold east side (i.e., near range side) ice edges in Fig. 6, this effect
valuebetweennilas-pancakeice (−3.9dB)obtainedfrom(2), may be also significant. Therefore,it is likely that the smaller
it seems that our measures worked well in this year. As for floesizeconditionsandlowericeconcentrationintheMIZare
bothresponsiblefortheenhancementofσ0
HV anomaly,the effectof floe size distributionshouldbe sig- ,misleadingusin
HH
nificantaswell, in lightof the factthatthe valuesin 2017are detectingdeformedice. This is the limitation of our measures
θ
higher than those in 2018 when i is exactly the same and when applying it to the MIZ.
| ridged ice    | is more prominent    | [Fig.         | 13(b)].       |            |               |              |                   |              |              |                 |        |
| ------------- | -------------------- | ------------- | ------------- | ---------- | ------------- | ------------ | ----------------- | ------------ | ------------ | --------------- | ------ |
| Thus,         | our result indicates | that the      | reduced       | (enhanced) | total         |              |                   |              |              |                 |        |
|               |                      |               |               |            |               | B. Relative  | Importance        | of Deformed  | Ice          | and Floe Size   |        |
| perimeter     | due to the dominance | of            | larger        | (smaller)  | ice floes     |              |                   |              |              |                 |        |
|               |                      |               |               |            |               | Finally,     | we examine        | the relative | importance   | of these        | two    |
| also affects  | the radar signal     | significantly |               | at both    | HH and HV     |              |                   |              |              |                 |        |
|               |                      |               |               |            |               | factors,     | i.e., ice surface | roughness    | (degree      | of deformation) |        |
| polarizations | and should           | be taken      | into account  |            | for detecting |              |                   |              |              |                 |        |
|               |                      |               |               |            |               | versus total | floe perimeter    | (floe        | size effect) | for HH          | and HV |
| deformed      | ice with L-band      | SAR.          | This explains | why        | the MIZ       |              |                   |              |              |                 |        |
alongtheiceedgeswasoftenjudgedasdeformedicefromour polarizations. For this purpose, we introduce the following
parameter:
| measures, | as shown in | Fig. 6(a) and | (b). | In the | MIZ, subject |     |     |     |     |     |     |
| --------- | ----------- | ------------- | ---- | ------ | ------------ | --- | --- | --- | --- | --- | --- |
to ocean waves, smaller ice floes tend to be produced due =(HH anomaly)−(HV anomaly).
(8)
| to wave-induced | breakup | processes. | Consequently, |     | the floe |     |     |     |     |     |     |
| --------------- | ------- | ---------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
size conditions in the MIZ are usually quite different from Note that each right-hand term in (8) is expressed as the
those in the inner ice pack region where most of the samples summation of the effects of degree of deformation (R) and
|     |     |     |     |     |     |     | (F). |     |    |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
werecollectedfordevelopingourmeasures[Fig.1(a)].Onthe floe size The cross section of along L2 is shown
other hand, it should also be kept in mind that the MIZ with in Fig. 16. It is remarkable that  is separated between the
lowericeconcentrationismoresubjecttoopenwaterthanthe four years in Fig. 16. Here we should keep in mind that HV
θ
inner ice pack region. As shown in Fig. 11 and also by [45], anomaly somewhat contains the effect of , which comes
i
the sensitivity of backscatter to θ becomes much higher at fromthe differentsensitivity of σ0 to θ betweenopenwater
|     |       |     | i   |     |     |     |     |     | HV  | i   |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| θ   | ≤30◦) |     |     | σ0  |     |     |     |     |     |     |     |
low i (especially for open water and may exceed and sea ice. To avoid this, we compare the results between
HH

9378 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
Fig.16. Crosssectionof=(HHanomaly)−(HVanomaly)indBalonglineL2inFig.10(a).
2017and2018(bothθ = 45.6◦) andbetween 2016and2019 its margin, which should work to increase both effects of R
i
(both θ = 27.2◦) separately. and F in 2016 compared with 2019. It would be difficult to
i
Regarding2017and 2018, Fig. 16 shows that  of 2018 is separate these two effects. We infer that somewhat steep and
constantlyafewdBhigherthanthatof2017.Thisisdescribed randomly oriented roughness produced by raised rims acted
as follows: to enhance the HV signals effectively.
Tosummarize,ourresultsshowedthatwhilefloesizeaffects
R2018+F2018−R2018−F2018 > R2017+F2017−R2017−F2017.
HH HH HV HV HH HH HV HV both HH and HV signals, the HV signal is more sensitive to
Then it can be rewritten as follows: floe size effect for both relatively thick ice and pancake ice
thantheHHsignal.Becauseofthisproperty,σ0 isconsidered
R
H
20
H
18−2017−F
H
20
H
17−2018
to be more sensitive to the MIZ, characteriz
H
ed
V
by small ice
>R2018−2017−F2017−2018 (9) floes and the presence of pancake ice, than σ0 . Therefore,
HV HV HH
itisexpectedthatourmeasuresworkmoreeffectivelytodetect
where R H 20 H 18−2017 stands for the difference of R at HH deformed ice by combining σ0 with σ0 .
polarization between 2018 and 2017, for example. Equa- HH HV
Yet, a question remains as to why our measures did not
tion (9) means that the enhancement of radar signals by R
worksuccessfullytodetectdeformedicein2018unlike2017.
in 2018 relative to that by F in 2017 is a few dB larger
Fig. 13(a)shows that HH anomalyin 2018 is close to zero or
at HH polarization than at HV polarization. In other words, even negative with the mean along L2 being −0.6 ± 1.2 (sd)
the increase of R in 2018 worked more efficiently at HH dBincontrastto1.5±1.6dBin2017,althoughdeformedice
polarization than at HV polarization. From the viewpoint of
was more prominent in 2018 than in 2017. We infer that our
floe size effect, it can be said that the enhancement of radar
measureswerederivedfromthefieldmeasurementsin2009to
signalsdueto F in2017wasmoreeffectiveatHVpolarization
2011,whenfloesizewasmoderateandfloeslargerthan500m
than at HH polarization.
were absent, quite different from those in 2018. On the other
Regarding 2016 and 2019,  is also constantly separated
hand, the ice conditions in 2017 were close to the normal,
inFig. 16.Inthiscase, ridgedice areawascommonlylimited
averaged for 2000–2019 (Table II). Probably that is why our
to only about 10% of total ice area (Table II). The major
measuresworkedwellto detectdeformedice in 2017,butnot
difference is that the dominant floe category was pancake
so much in 2018.
ice in 2016, whereas nilas in 2019. Therefore, ice surface is
Here,weroughlyestimatetheeffectof F in2018.Sinceice
somewhatrougherandfloesizeeffectisstrongerin2016than
surface roughness due to R in 2018 is about 1.2 times larger
in2019.Sincein2019islargerthanthatin2016,itfollows:
than in 2017, judging from the ratio of mean ice thickness,
R2016−2019+F2016−2019 the mean HH anomaly along L2 in 2018 is expected to be
HV HV >R2016−2019+F2016−2019.
(10)
1.8 (=1.5 × 1.2) dB for the same floe size conditions as
HH HH in2017.Thisis2.4dBhigherthantherealvalue.Considering
Equation (10) means that in total the HV radar signals are that the total floe perimeter in 2018 is about half of that
more sensitive to the increase of ice surface roughness and in 2017, it is roughly estimated that twice the total floe
total perimeter than the HH radar signals for less deformed perimeter increases σ0 at L-band by 2–3 dB. This cautions
HH
thin ice. This result is coincident with [31]. It is unlikely that us to take the floe size conditions into account as well as ice
F works effectively for nilas because the freeboard is quite deformationwhendevelopingandapplyingthemeasureswith
small. On the other hand, pancake ice has raised rims around L-band SAR.

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9379
V. CONCLUSION All these results indicate that we should be careful when
applying our measures to the sea ice regions where floe
For better understanding of deformation processes in the
size distribution is significantly different from the normal
SIZ, we developed measures to detect deformed ice using
conditions in the southern Sea of Okhotsk. To find out a
ALOS/PALSAR images as a preliminary step toward moni-
universal measure, which is applicable to all the sea ice area,
toring the temporal evolution of deformed ice regions, based
weneedfurtherinvestigationabouthowicesurfaceroughness
on the field measurements aboard PV “Soya” in the Sea of
and floe size distribution affect the radar signal with the
Okhotsk. This region has some advantage over other polar
dependence on θ quantitatively. Especially, theoretical work
regions for this purpose in that the absence of multiyear ice i
on the relationship radar signals and surface roughness is
makes the classification of sea ice types simpler. Comparison
required in the future. Recently, rigorous statistical methods
between PALSAR and RADARSAT-2 confirmed that L-band
have been introduced to study ice-type classification with the
SAR is more useful to detect deformed ice than C-band
θ effect [46], [47], and further development is expected. For
SAR, which is consistent with the past studies. Assuming i
this purpose, the international research expedition, “Multidis-
that brightnesscorrelatesto deformation,at least for the three
ciplinarydriftingObservatoryfor the Studyof Arctic Climate
ice categories (nilas, pancake ice, and deformed ice) found
(MOSAiC),” which is ongoing in the Arctic Ocean from
in this region and for L-band, the measures were derived by
October2019to October2020,is expectedto provideuswith
plotting σ0 as a function of θ and calculating the threshold
HH i an opportunity to extend this result.
linesbetweendifferenticetypeswiththeleast-squaresmethod.
Mapping deformed ice regions with these measures revealed
the following properties. ACKNOWLEDGMENT
1) Forcedbywindsandoceanwaves,deformediceregions Observations in the Sea of Okhotsk were conducted in
arequitevariablewith bothtime andspace.Inthe inner collaboration with Japan Coast Guard, PV “Soya,” and many
ice pack region, the temporalevolutionof deformedice colleagues, especially Jun Nishioka, Associate Professor, and
regions was consistent with the convergence/divergence Dr.MasatoItoh.Theauthorsappreciatetheirdedicatedsupport
zone of ice drift. throughout the cruise. Technical support for the analysis of
2) The area, judged as deformed ice from our measures, RADARSAT-2 by Prof. Hiroyuki Wakabayashi is acknowl-
appears in relatively linear alignments mainly along the edged.Criticalreadingofthisarticleandbeneficialcomments
ice edge and with a width of a few tens of kilometers by Dr. Suman Singha was very helpful to improve this
in the inner ice pack region. article. Discussions with Prof. Christian Haas, Prof. Gun-
Toconfirmtheaboveresults, we examinedthe applicability nar Spreen, Dr. James Imber, Prof. Humio Mitsudera, Prof.
of our measures to ALOS-2/PALSAR-2 images, based on the Naoto Ebuchi, and Dr. Kazuki Nakamura are also acknowl-
four-year field measurements (2016–2019) conducted aboard edged. Some of the figures were made with the help of
thePV“Soya”inthesameregion.Theresultsaresummarized Dr. Kazuya Ono. ALOS/Phased Array type L-band Syn-
as follows: thetic Aperture Radar (PALSAR) and ALOS-2/PALSAR-2
3) The validity of our measures was confirmed to some images were provided by Japan Aerospace Exploration
extent from direct comparison with the real ice condi- Agency (JAXA) through the ALOS Research Project
tions for 19◦ ≤θ ≤56◦. (PI:No.573)andthe2ndResearchProjectontheEarthObser-
i
4) In open water area, the variability of σ0 was much vations(PI:ER2A4N012).RADARSAT-2datawerepurchased
HV
reducedcomparedwith σ0 andthe dependenceofσ0 through ImageONE Co., Ltd., Tokyo, Japan, RADARSAT-
HH HV
on θ is somewhat larger than that within sea ice area. 2 Data and Products ©MacDonald, DETTWEILER and
i
5) Both σ0 and σ0 are affectedsignificantlynotonlyby ASSOCIATES LTD. (2011)—All Rights reserved.
HH HV
ice surface roughness but also by floe size distribution
through the total perimeter of sea ice floes.
REFERENCES
6) The relative contribution of floe size distribution to the
radarsignalsisestimatedtobelargeratHVpolarization [1] J. E. Overland and M. C. Serreze, “Advances in Arctic atmospheric
research,” in Arctic Climate Change (Atmospheric and Oceanographic
than at HH polarization by a few dB.
Sciences Library), vol. 43, P. Lemke and H. W. Jacobi, Eds. Berlin,
Regarding Item 5, in terms of contribution to the enhance- Germany:Springer, 2012,pp.11–26.
ment of σ0 , it is roughly estimated that four times the [2] P. Rampal, J. Weiss, C. Dubois, and J.-M. Campin, “IPCC climate
HH models do not capture Arctic sea ice drift acceleration: Consequences
total perimeter (i.e., 1/4 floe size for the same sea ice area) in terms of projected sea ice thinning and decline,” J. Geophys. Res.,
is comparable to about twice the ice surface roughness and vol.116,Sep.2011,Art.no.C00D07,doi:10.1029/2011JC007110.
enhance σ0 at L-band by 4–6 dB. From these results, it is [3] H. R. Langehaug, F. Geyer, L. H. Smedsrud, and Y. Gao,
HH “Arctic sea ice decline and ice export in the CMIP5 historical
most likely that the linear alignments along the ice edge simulations,” Ocean Model., vol. 71, pp.114–126, Nov. 2013, doi:
described in Item 2 are attributed not to deformed ice, but 10.1016/j.ocemod.2012.12.006.
[4] D.J.CavalieriandC.L.Parkinson,“Arcticseaicevariabilityandtrends,
to smaller ice floes with lower ice concentration, produced
1979–2010,” Cryosphere, vol. 6, no. 4, pp.881–889, Aug. 2012, doi:
by the wave-induced breakup. To distinguish deformed ice 10.5194/tc-6-881-2012.
regions from the region subject to such a floe size effect like [5] J.C.Stroeve,M.C.Serreze,M.M.Holland,J.E.Kay,J.Malanik,and
the MIZ, combining our measures with σ0 might be useful, A.P.Barrett, “TheArctic’s rapidlyshrinkingseaicecover:Aresearch
HV synthesis,” Climatic Change, vol. 110, nos. 3–4, pp.1005–1027,
as suggested by Items 4 and 6. Feb.2012,doi:10.1007/s10584-011-0101-1.

9380 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.59,NO.11,NOVEMBER2021
[6] I.H.Onarheim,T.Eldevik,L.H.Smedsrud,andJ.C.Stroeve,“Seasonal [25] T.Toyota,T.Kawamura,K.I.Ohshima,H.Shimoda,andM.Wakatsuchi
and regional manifestation of Arctic sea ice loss,” J. Climate, vol. 31, “Thickness distribution, texture and stratigraphy, and a simple proba-
no.12,pp.4917–4932,Jun.2018,doi:10.1175/JCLI-D-17-0427.1. bilistic model for dynamical thickening of sea ice in the southern Sea
[7] A. P. Worby, M. O. Jeffries, W. F. Weeks, K. Morris, and R. Jaña, ofOkhotsk,”J.Geophys.Res.,vol.109,no.C6,2004,Art.no.C06001,
“Thethicknessdistributionofseaiceandsnowcoverduringlatewinter doi:10.1029/2003JC002090.
in the Bellingshausen and Amundsen seas, Antarctica,” J. Geophys. [26] Y. Fukamachi, G. Mizuta, K. I. Ohshima, T. Toyota, N. Kimura, and
Res., Oceans, vol. 101, no. C12, pp.28441–28455, Dec. 1996, doi: M.Wakatsuchi,“Seaicethickness inthesouthwestern SeaofOkhotsk
10.1029/96jc02737. revealed by a moored ice-profiling sonar,” J. Geophys. Res., vol. 111,
[8] M.O.Jeffries,S.Li,R.A.Jana,H.R.Krouse,andB.Hurst-Cushing, no.C9,2006,Art.no.C09018,doi:10.1029/2005JC003327.
“Late winter first-year ice floe thickness variability, seawater flooding
[27] T. Toyota and N. Kimura, “An examination of the sea ice rheology
andsnowiceformation intheAmundsenandRossSeas,”inAntarctic
for seasonal ice zones based on ice drift and thickness observations,”
Sea Ice: Physical processes, Interactions and Variability (Antarctic J. Geophys. Res., Oceans, vol. 123, no. 2, pp.1406–1428, Feb. 2018,
Research Series), vol. 74, M. O. Jeffries, Ed. Washington, DC, USA:
doi:10.1002/2017jc013627.
AmericanGeophysical Union,1998,pp.69–87.
[28] A. P. Worby and I. Allison, “A technique for making ship-based
[9] T. Toyota, S. Takatsuji, K. Tateyama, K. Naoki, and K. I. Ohshima,
observations of Antarctic sea ice thickness and characteristics. Part I:
“Properties of sea ice and overlying snow in the southern Sea of
Observational technique and results,” Antarctic Cooperat. Res. Centre,
Okhotsk,” J. Oceanogr., vol. 63, no. 3, pp.393–411, Jun. 2007, doi:
Univ.Tasmania,Hobart, TAS,Australia, Res.Rep.14,1999,p.63.
10.1007/s10872-007-0037-2.
[10] M.Shokrand N.K.Sinha, “Remote sensing principles relevant tosea [29] N.Kimura,A.Nishimura,Y.Tanaka,andH.Yamaguchi, “Influenceof
ice,” in Sea Ice: Physics and Remote Sensing. Washington, DC, USA: winter sea-ice motion on summerice cover in the Arctic,” Polar Res.,
AmericanGeophysical Union,2015,pp.271–335. vol.32,no.1,2013,Art.no.20193,doi:10.3402/polar.v32i0.20193.
[11] A. Gegiuc, M. Similä, J. Karvonen, M. Lensu, M. Mäkynen, and [30] M. Hallikainen and D. P. Winebrenner, “The physical basis for sea
J.Vainio, “Estimation of degree of sea ice ridging based on dual- ice remote sensing,” in Microwave Remote Sensing of Sea Ice (Geo-
polarized C-band SARdata,” Cryosphere, vol.12, no.1, pp.343–364, physical Monograph Series), vol. 68, F. D. Carsey, Ed. Washington,
Jan.2018,doi:10.5194/tc-12-343-2018. DC, USA: American Geophysical Union, Jan. 1992, pp.29–46, doi:
[12] S.M.Cafarella etal.,“Estimation oflevel anddeformedfirst-yearsea 10.1029/GM068p0029.
ice surface roughness in the Canadian Arctic archipelago from C-and [31] W. Dierking, “Sea ice monitoring by synthetic aperture radar,”
L-bandsyntheticapertureradar,”Can.J.RemoteSens.,vol.45,nos.3–4, Oceanography, vol. 26, no. 2, pp.100–111, Jun. 2013, doi:
pp.457–475,Jul.2019,doi:10.1080/07038992.2019.1647102. 10.5670/oceanog.2013.33.
[13] E.RignotandM.R.Drinkwater, “Winter sea-icemappingfrommulti- [32] R. Onstott, R. Moore, S. Gogineni, and C. Delker, “Four years
parameter synthetic-aperture radar data,” J. Glaciol., vol. 40, no. 134, of low-altitude sea ice broad-band backscatter measurements,”
pp.31–45,1994,doi:10.3189/s0022143000003774. IEEE J. Ocean. Eng., vol. 7, no. 1, pp.44–50, Jan. 1982, doi:
[14] W. Dierking and T. Busche, “Sea ice monitoring by L-band SAR: 10.1109/JOE.1982.1145511.
An assessment based on literature and comparisons of JERS-1 and
[33] R. G. Onstott, “SAR and scatterometer signatures of sea ice,” in
ERS-1 imagery,” IEEE Trans. Geosci. Remote Sens., vol. 44, no. 4,
MicrowaveRemoteSensingofSeaIce(GeophysicalMonographSeries),
pp.957–970,Apr.2006,doi:10.1109/TGRS.2005.861745.
vol.68,F.Carsey,Ed.Washington,DC,USA:AGU,1992,pp.73–104,
[15] L. E. B. Eriksson et al., “Evaluation of new spaceborne SAR sensors
doi:10.1029/GM068p0073.
forsea-icemonitoringintheBalticSea,”Can.J.RemoteSens.,vol.36,
[34] N. Kimura and M. Wakatsuchi, “Relationship between sea-ice
no.1,pp.S56–S73,Jan.2010,doi:10.5589/m10-020.
motion and geostrophic wind in the Northern Hemisphere,” Geo-
[16] H. Wakabayashi, K. Hirano, F. Nishio, M. Aota, and S. Takahashi,
phys. Res. Lett., vol. 27, no. 22, pp.3735–3738, Nov. 2000, doi:
“AstudyofseaiceintheSeaofOkhotskwithSARdata,” PolarRec.,
10.1029/2000GL011495.
vol.31,no.178,pp.305–314,Jul.1995.
[17] D.O.Dammann,H.Eicken,A.R.Mahoney,E.Saiet,F.J.Meyer,and [35] M.S.Mahmud,T.Geldsetzer,S.E.L.Howell,J.J.Yackel,V.Nandan,
J. C. George, “Traversing sea ice—linking surface roughness and ice and R. K. Scharien, “Incidence angle dependence of HH-polarized
trafficabilitythroughSARpolarimetryandinterferometry,”IEEEJ.Sel. C-andL-BandwintertimebackscatteroverArcticseaice,”IEEETrans.
Topics Appl. EarthObserv. Remote Sens.,vol. 11, no.2, pp.416–433, Geosci. RemoteSens.,vol.56,no.11,pp.6686–6698,Nov.2018,doi:
Feb.2018,doi:10.1109/JSTARS.2017.2764961. 10.1109/TGRS.2018.2841343.
[18] R. Massom, “Basic remote-sensing principles relating to the mea- [36] T. Matsuoka et al., “Deriving sea-ice thickness and ice types in the
surement of sea ice and its snow cover,” in Polar Remote Sensing: Sea of Okhotsk using dual-frequency airborne SAR (Pi-SAR) data,”
Atmosphere and Oceans, vol. 1, D. Lubin and R. Massom, Eds. Ann. Glaciol., vol. 34, pp.429–434, Sep. 2002. [Online]. Available:
Chichester, U.K.:Praxis,2006,pp.356–380. https://www.cambridge.org/core/journals/annals-of-glaciology/article/
[19] J. A. Casey, S. E. L. Howell, A. Tivy, and C. Haas, “Separability deriving-seaice-thickness-and-ice-types-in-the-sea-of-okhotsk-using-
of sea ice types from wide swath C- and L-band synthetic aperture dualfrequency-airborne-sar-pisar-data/86ED428F1C6B40EA30FEAD34
radarimageryacquiredduringthemeltseason,”RemoteSens.Environ., 26B298B5, doi:10.3189/172756402781817392.
vol.174,pp.314–328,Mar.2016,doi:10.1016/j.rse.2015.12.021. [37] T. Toyota, K. Nakamura, S. Uto, K. I. Ohshima, and N. Ebuchi,
[20] S. E. L. Howell et al., “Comparing L- and C-band synthetic aper- “Retrieval of sea ice thickness distribution in the seasonal ice zone
ture radar estimates of sea ice motion over different ice regimes,” from airborne L-band SAR,” Int. J. Remote Sens., vol. 30, no. 12,
Remote Sens. Environ., vol. 204, pp.380–391, Jan. 2018, doi: pp.3171–3189,Jun.2009,doi:10.1080/01431160802558790.
10.1016/j.rse.2017.10.017. [38] T. Toyota, S. Ono, K. Cho, and K. I. Ohshima, “Retrieval of sea-
[21] J. F. Vesecky, M. P. Smith, and R. Samadani, “Extraction of lead ice thickness distribution in the Sea of Okhotsk from ALOS/PALSAR
and ridge characteristics from SAR images of sea ice,” IEEE Trans. backscatterdata,”Ann.Glaciol.,vol.52,no.57,pp.177–184,2011,doi:
Geosci. Remote Sens., vol. 28, no. 4, pp.740–744, Jul. 1990, doi: 10.3189/172756411795931732.
10.1109/TGRS.1990.573005.
[39] A.P.Worby,C.A.Geiger,M.J.Paget,M.L.VanWoert,S.F.Ackley,
[22] M. R. Drinkwater, “Active microwave remote sensing observations of
and T. L. DeLiberty, “Thickness distribution of Antarctic sea ice,”
WeddellSeaice,”inAntarcticSeaIce:PhysicalProcesses,Interactions
J. Geophys. Res., vol. 113, no. C5, 2008, Art. no. C05S92, doi:
and Variety (Antarctic Research Series), vol. 74, M. O. Jeffries, Ed.
10.1029/2007JC004254.
Washington, DC,USA:AGU,1998,pp.187–212.
[40] P. Wadhams and B. Holt, “Waves in frazil and pancake ice and their
[23] K. Nakamura, H. Wakabayashi, K. Naoki, F. Nishio, T. Moriyama,
detection inSeasatsyntheticaperture radarimagery,”J.Geophys.Res.,
and S. Uratsuka, “Observation of sea-ice thickness in the Sea of
vol.96,no.C5,pp.8835–8852,1991,doi:10.1029/91JC00457.
Okhotsk by using dual-frequency and fully polarimetric airborne SAR
(pi-SAR) data,” IEEE Trans. Geosci. Remote Sens., vol. 43, no. 11, [41] G. R. Valenzuela, “Theories for the interaction of electromagnetic
pp.2460–2469,Nov.2005,doi:10.1109/TGRS.2005.853928. and oceanic waves—A review,” Boundary-Layer Meteorol., vol. 13,
[24] S.Singha,M.Johansson,N.Hughes,S.M.Hvidegaard,andH.Skourup, nos.1–4,pp.61–85,Jan.1978,doi:10.1007/bf00913863.
“Arctic sea ice characterization using spaceborne fully polarimetric [42] O. Isoguchi and M. Shimada, “An L-band ocean geophysical
L-,C-,and X-band SAR with validation by airborne measurements,” model function derived from PALSAR,” IEEE Trans. Geosci.
IEEE Trans. Geosci. Remote Sens., vol. 56, no. 7, pp.3715–3734, Remote Sens., vol. 47, no. 7, pp.1925–1936, Jul. 2009, doi:
Jul.2018,doi:10.1109/TGRS.2018.2809504. 10.1109/TGRS.2008.2010864.

TOYOTAetal.: MEASURINGDEFORMEDSEAICEINSIZSUSINGL-BANDSARIMAGES 9381
[43] S. Sandven, O. M. Johannessen, M. W. Miles, L. H. Pettersson, and JunnoIshiyama received themaster’sdegreefrom
K.Kloster,“Barents seaseasonalicezonefeatures andprocesses from Hokkaido University, Sapporo, Japan, in 2017.
ERS 1 synthetic aperture radar: Seasonal ice zone experiment 1992,” He wrote the master’s thesis on the theme of this
J.Geophys.Res.,Oceans,vol.104,no.C7,pp.15843–15857,Jul.1999, article.
doi:10.1029/1998JC900050. He works topromote the agricultural products as
[44] M.R.Drinkwater, R.Kwok, D.P.Winebrenner, and E.Rignot, “Mul- aStaffofTohmaTownOffice,Hokkaido, Japan.
| tifrequency | polarimetric |       | synthetic | aperture | radar           | observations | of sea     |     |     |     |     |
| ----------- | ------------ | ----- | --------- | -------- | --------------- | ------------ | ---------- | --- | --- | --- | --- |
|             | J. Geophys.  | Res., |           |          |                 |              |            |     |     |     |     |
| ice,”       |              |       | vol. 96,  | no. C11, | pp.20679–20698, |              | 1991, doi: |     |     |     |     |
10.1029/91JC01915.
| [45] F.Gohin, | “Some          | active | and passive        | microwave | signatures             |     | ofAntarctic |     |     |     |     |
| ------------- | -------------- | ------ | ------------------ | --------- | ---------------------- | --- | ----------- | --- | --- | --- | --- |
| seaice        | frommid-winter |        | tospring1991,”Int. |           | J. RemoteSens.,vol.16, |     |             |     |     |     |     |
no.11,pp.2031–2054,Jul.1995,doi:10.1080/01431169508954537.
| [46] J. Lohse, | A.         | P. Doulgeris,  | and  | W. Dierking, | “Mapping     | sea-ice | types      |     |     |     |     |
| -------------- | ---------- | -------------- | ---- | ------------ | ------------ | ------- | ---------- | --- | --- | --- | --- |
| from           | Sentinel-1 | considering    | the  | surface-type | dependent    | effect  | of inci-   |     |     |     |     |
| dence          | angle,”    | Ann. Glaciol., | vol. | 61, no.      | 82, pp.1–11, | Jun.    | 2020, doi: |     |     |     |     |
10.1017/aog.2020.45.
| [47] A. Cristea, | J.           | van Houtte, | and      | A. P. Doulgeris, | “Integrating |     | incidence |     |     |     |     |
| ---------------- | ------------ | ----------- | -------- | ---------------- | ------------ | --- | --------- | --- | --- | --- | --- |
| angle            | dependencies |             | into the | clustering-based | segmentation |     | of SAR    |     |     |     |     |
images,”IEEEJ.Sel.TopicsAppl.EarthObserv.RemoteSens.,vol.13,
pp.2925–2939,2020,doi:10.1109/JSTARS.2020.2993067.
|     |     | Takenobu            |             | Toyota    | received the | Ph.D.         | degree from   |     |     |     |     |
| --- | --- | ------------------- | ----------- | --------- | ------------ | ------------- | ------------- | --- | --- | --- | --- |
|     |     | HokkaidoUniversity, |             |           | Sapporo,     | Japan,in1998. |               |     |     |     |     |
|     |     |                     | He is an    | Assistant | Professor    | with          | the Institute |     |     |     |     |
|     |     | ofLow               | Temperature |           | Science,     | Hokkaido      | University.   |     |     |     |     |
|     |     | He                  | is also     | an expert | in sea ice   | physics,      | especially    |     |     |     |     |
inner structure, dynamic processes, and the inter- Noriaki Kimura received the Ph.D. degree from
|     |     | actions | with | snow | and atmosphere. | He  | has been |                     |                |         |     |
| --- | --- | ------- | ---- | ---- | --------------- | --- | -------- | ------------------- | -------------- | ------- | --- |
|     |     |         |      |      |                 |     |          | HokkaidoUniversity, | Sapporo,Japan, | in2000. |     |
leadingtheseaiceobservationintheSeaofOkhotsk
|     |     |     |          |        |                 |       |         | He is a Project | Researcher          | with the Atmosphere |     |
| --- | --- | --- | -------- | ------ | --------------- | ----- | ------- | --------------- | ------------------- | ------------------- | --- |
|     |     | for | about 25 | years. | He has authored | about | 45 ref- |                 |                     |                     |     |
|     |     |     |          |        |                 |       |         | and Ocean       | Research Institute, | The University      | of  |
ereedarticlesininternational scientificjournals.His Tokyo, Kashiwa, Japan. He is also an expert in
research interests include thephysical processes on remotesensingofseaice. Hehas authored 27arti-
| various scales | intheseasonal |     | icezoneforapplying |     | tothenumerical |     | seaice |                       |               |           |     |
| -------------- | ------------- | --- | ------------------ | --- | -------------- | --- | ------ | --------------------- | ------------- | --------- | --- |
|                |               |     |                    |     |                |     |        | cles in peer-reviewed | international | journals. | His |
models.
|     |     |     |     |     |     |     |     | research interests | include the | physical processes | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------- | ------------------ | --- |
Dr. Toyota is the Head of the Sea Ice, Lake and River Ice Division, seaiceespecially onlargespatial scales.
| International | Association | of  | Cryospheric | Sciences, | and | International | Union |     |     |     |     |
| ------------- | ----------- | --- | ----------- | --------- | --- | ------------- | ----- | --- | --- | --- | --- |
ofGeodesyandGeophysics.
