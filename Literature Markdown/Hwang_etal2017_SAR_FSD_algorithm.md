Hwang, B, et al 2017 A practical algorithm for the retrieval of floe size distribution of
Arctic sea ice from high-resolution satellite Synthetic Aperture Radar imagery. Elem Sci
Anth, 5: 38, DOI: https://doi.org/10.1525/elementa.154
RESEARCH ARTICLE
A practical algorithm for the retrieval of floe size
distribution of Arctic sea ice from high-resolution
satellite Synthetic Aperture Radar imagery
Byongjun Hwang*, Jinchang Ren†, Samuel McCormack†, Craig Berry†, Ismail Ben Ayed‡,
Hans C. Graber§ and Erchan Aptoula‖
In this study, we present an algorithm for summer sea ice conditions that semi-automatically produces
the floe size distribution of Arctic sea ice from high-resolution satellite Synthetic Aperture Radar data.
Currently, floe size distribution data from satellite images are very rare in the literature, mainly due to
the lack of a reliable algorithm to produce such data. Here, we developed the algorithm by combining
various image analysis methods, including Kernel Graph Cuts, distance transformation and watershed
transformation, and a rule-based boundary revalidation. The developed algorithm has been validated
against the ground truth that was extracted manually with the aid of 1-m resolution visible satellite data.
Comprehensive validation analysis has shown both perspectives and limitations. The algorithm tends to fail
to detect small floes (mostly less than 100 m in mean caliper diameter) compared to ground truth, which
is mainly due to limitations in water-ice segmentation. Some variability in the power law exponent of floe
size distribution is observed due to the effects of control parameters in the process of de-noising, Kernel
Graph Cuts segmentation, thresholds for boundary revalidation and image resolution. Nonetheless, the
algorithm, for floes larger than 100 m, has shown a reasonable agreement with ground truth under various
selections of these control parameters. Considering that the coverage and spatial resolution of satellite
Synthetic Aperture Radar data have increased significantly in recent years, the developed algorithm opens
a new possibility to produce large volumes of floe size distribution data, which is essential for improving
our understanding and prediction of the Arctic sea ice cover.
Keywords: sea ice floe size; Synthetic Aperture Radar; image processing; Arctic
1. Introduction be derived to verify the parameterized evolution of FSD
Determining the processes that govern the evolution of and its impacts on sea ice dynamics and thermodynamics
sea ice is critical to the improvement of predictive forecasts in the models (Williams et al. 2013b; Zhang et al. 2016).
of sea ice conditions. A key parameter necessary for study- However, records of the evolution of the in situ FSD from
ing this evolution and validating the parameterization in satellite observations are rare.
sea ice models is the sea ice floe size distribution (FSD). The latest satellite Synthetic Aperture Radar (SAR)
Sea ice models estimate the FSD through floe breakup images cover large areas of the Arctic Ocean on a regu-
parameterizations (e.g., Williams et al. 2013a; Horvat and lar basis and/or on demand at spatial resolutions ranging
Tziperman, 2015; Zhang et al. 2015), and the parameter- from sub-meter to hundreds of meters. Satellite SAR has
ized FSD is then used to calculate thermodynamic melt also generated a vast historical inventory of images since
(Steele, 1992; Zhang et al. 2016). This is a highly coupled the 1990s (or since 2007 for high-resolution images), and
process. It is essential that the in situ evolution of FSD an increasing number of high-resolution (~ 3–20 m) satel-
lite data are being acquired. To process SAR imagery effi-
ciently and robustly it requires proven algorithms that are
not only applicable across various SAR sensors (to produce
* Scottish Association for Marine Science, Oban, Argyll, UK
accurate FSD) but also fast enough to digest large quanti-
† University of Strathclyde, Glasgow, UK
ties of imagery. Developing such an algorithm is compli-
‡ École de Technologie Supérieure, Montréal, CA
cated and challenging due to i) the variability in intensity
§ Rosenstiel School of Marine and Atmospheric Science,
(backscattering coefficient), ii) the high level of noise
University of Miami, Miami, Florida, US
(speckles) in the imagery, and iii) the lack of edge discrimi-
‖ Institute of Information Technologies, Gebze Technical
University, Kocaeli, TR nation between touching floes. The primary objective of
Corresponding author: Byongjun Hwang (phil.hwang@sams.ac.uk) this paper is to introduce a new FSD retrieval algorithm
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 2 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
that has been developed and validated for the satellite 2.2 Issues of water-ice segmentation from SAR
SAR imagery. Obtaining accurate water-ice segmentation from SAR
imagery is important for FSD retrieval, and several algo-
2. Brief review of FSD retrieval and water-ice rithms were proposed for this problem. Early attempts
segmentation efforts include ISODATA cluster analysis (Kwok, 1992) and grey
2.1 Previous FSD retrieval efforts level co-occurrence probability texture features (Barber
Sea ice FSD was first studied by using a set of aerial pho- and LeDrew, 1991). Later, dynamic local thresholding and
tographs by Rothrock and Thorndike (1984). Since then, an expert system with known geophysical parameters
FSD has been derived from aerial photography, satellite were investigated for water-ice segmentation and ice type
visible and SAR imagery (e.g., Holt and Martin, 2001; classification (Haverkamp et al., 1995). Deng and Clausi
Toyota et al. 2011; Wang et al. 2016). FSD derived from (2005) proposed a function-based Markov Random Field
aerial photos and/or visible satellite imagery was used Model algorithm that did not require any training data
mainly for case studies that examined the effect of lat- but a small set of control parameters. The algorithm uses
eral melt of small floes (Toyota et al., 2006, 2011). These intensity only for water-ice separation but also incorpo-
case studies occurred during relatively short periods rates gray-level co-occurrence probability texture features
of time and in restricted locations (like near the ship). for sea ice type classification. This algorithm was later
Thus, full FSD evolution during winter-to-summer tran- incorporated into the map-guided system to aid the ice
sition has not been measured. Satellite SAR can provide charting by human experts (Maillard et al., 2005; Clausi et
a high level of flexibility by taking images through cloud al., 2010). Further development includes watershed and
and darkness, so monitoring the continuous evolution iterative region growing with semantics (Yu and Clausi,
of FSD can be realized. Previously, the major stumbling 2008). The algorithm produces regions (polygons), each
block in using SAR was coarse spatial resolution of SAR labeled via maximum a priori estimation. Such a labeling
(> ~ 100 m) and low signal-to-noise level, which made it is based on backscattering (backscattering mean, covari-
difficult to resolve individual floes reliably. Recent SAR ance and number of pixels within the region). The authors
technology has significantly improved its spatial resolu- reported an accuracy higher than 80% when compared
tion (~ 1–20 m) and signal-to-noise quality, which makes with an ice expert system (Clausi et al., 2010).
it possible to resolve small floes (~ 50–100 m) near the Most of the aforementioned algorithms assume that
regime shift between mechanical breakup and lateral the distribution of image data within each segmentation
melt (Toyota et al., 2011). region follows a Gaussian model. However, SAR image dis-
FSD retrieval from aerial photos and visible imagery tribution can vary from Gaussian to Gamma depending
utilizes simple thresholding methods for sea ice segmen- on sea ice condition, sea surface roughness and incident
tation followed by morphological eroding/expanding angle. Therefore, an efficient algorithm that does not fit
operator to split touching floes (e.g., Steer et al., 2008; a specific image distribution would be ideal for sea-ice
Toyota et al., 2011). The retrieved images are often man- SAR segmentation. Recently, Salah et al. (2011) proposed
ually inspected and corrected. The major differences parametric kernel graph cuts (KGC), an unsupervised and
between aerial photos/visible and SAR are the high versatile method that can adapt to any image distribu-
level of speckle noise and inter- and intra-image vari- tion. Instead of fitting a specific distribution shape, KGC
ability in intensity in SAR. This high noise and variability seeks the modes of the image distribution via mean-shift
makes it even more difficult to apply a simple thresh- updates and assigns pixels to such modes using a kernel-
olding method to SAR to produce satisfactory results. induced, non-Euclidean distance. This approach relaxes
Holt and Martin (2001) used local dynamic threshold- the need for knowing a priori the correct statistical image
ing (Haverkamp et al., 1995) for sea ice segmentation to model within each region. Evaluated over many synthetic
derive FSD from ERS-1 SAR data, which combined with and real images with various image distributions (e.g.,
correction to wind-roughened open water to reduce the Gaussian, Gamma and exponential) and contrasts, KGC
effect of variable intensity within the SAR images. They yielded consistently competitive results in comparison to
also implemented a restricted shrinking/growing algo- choosing the correct models (Salah et al., 2011).
rithm (Soh et al., 1998) to split touching ice floes. This In the next section, the developed algorithm is detailed
method is similar to the erosion/expansion operator used in several steps. This description is then followed by case
by Steer et al. (2008), but the growth of pixels is restricted studies (Section 4) in which the algorithm-produced FSD
so that the original floe boundary can be preserved when results are validated against manually produced “ground
floes are split. Such a shrinking/growing algorithm is truth” data.
computationally expensive and difficult to implement, as
the number of iterations varies from floe to floe and the 3. Description of the proposed algorithm
correct “marker” (skeleton image) is difficult to achieve. 3.1 Preprocessing and water-ice segmentation
A recent study by Zhang and Skjetne (2015) applied the Figure 1 illustrates the processing steps and examples of
gradient vector flow snakes algorithm to aerial photo- outputs from each step (SAR, water-ice segmented image,
graphs to delineate the boundaries of touching sea ice floe-splitting image and FSD). A combination of de-nois-
floes. The results suggested better handling of detecting ing filters was applied to reduce speckle noise in the SAR
correct floe boundaries if the seed and initial contour can images, including median, bilateral and Gaussian filters.
be reasonably assumed. Water-ice segmentation was computed by using paramet-
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 3 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Figure 1: Overall workflow of the proposed algorithm. The example image shown in the figure is Case 2 (Table 1),
which was acquired on July 31, 2014. DOI: https://doi.org/10.1525/elementa.154.f1
ric KGC (Salah et al., 2011). We used SAR intensity only, as the incident angle dependent variation (IADV) is rela-
image intensity is in general sufficient for water-ice discrim- tively small for TS-X SM images. The IADV can be large
ination, while texture features are effective for ice type clas- for some wide-area swath images such as Radarsat-2
sification (Clausi and Yue, 2004; Deng and Clausi, 2005). ScanSAR Wide (500 × 500 km). However, the swath size
In this study, we used TerraSAR-X (TS-X) single-polarized of TS-X SM images are relatively small (~ 30 × 50 km) and
(HH) StripMap (SM) multi look ground range detected the IADV within the image is also very small (less than
image products. Before applying KGC, the original TS-X a couple of degrees). Thus, IADV within the image was
data were radiometrically calibrated to backscattering ignored. In addition, the KGC algorithm can handle some
coefficient (σ) values (using Sentinel-1 Toolbox). They internal intensity variation by adjusting to various image
0
were linearly scaled to 8-bit gray-scale intensity, and then distributions.
were applied with a low-pass Gaussian filter and a bilat- Let I:x∈ Ω⊂R 2→I
x
=I(x)∈R be our processed
eral filter (Tomasi and Manduchi, 1998) to reduce speckle image function. The process of image segmentation
noises. The incidence angle dependencies of the observed is to find a partition {R}k of Ω into k homogene-
l l=1
σ over various types of sea ice were not corrected, as ous regions. Let λ denote a variable labeling function
0
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 4 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
of W, which assigns each pixel to a region parameter applied to the binary water-ice image. For each pixel in
μ :R ={p ∈ Ω |λ(p)= μ }. The problem consists of find- the image, the inverse distance transform calculates the
l l l
ing a labeling function l that minimizes the following distance between the pixel and the nearest water pixel
functional (Salah et al., 2011): of the binary image (the Euclidean distance was used by
default). Thus, the ice interior away from open water has
E(λ)= −∑∑D(I −μ )+βR(λ) (1) larger negative values in the inverse distance transform,
x l forming the basin of the watershed. Any un-detected
1≤l≤kx∈Rl
“false” holes would produce unnecessary minima that
where D is a kernel-induced, non-Euclidean distance evalu- lead to over-splitting of the floe (see Section 4.5 for more
ated by the radial basis function kernel: D(t)=exp(−t2), with details). We applied a rule-based post-processing (i.e.,
σ2
σ the width of the kernel. R(λ)=∑ r(λ(x),λ(y)) is boundary revalidation) to reduce erroneous floe-splitting
{x,y}∈N
a region boundary smoothness term, with N neighbor- or merging. In this post-processing, all the watershed
hood set containing all pairs of neighboring pixels, and boundaries neighboring more than two ice areas were
r(λ(x),λ(y)) is a regularization function given by the in question for its validity of floe splitting or merging. In
truncated squared absolute difference (Boykov et al., this study, we used two geometric and two intensity-based
2001): r(λ(x),λ(y)=min(const2,|μ −μ |2) where const rules to revalidate the boundaries in question. More com-
λ(x) λ(y)
is a constant. Minimization of E is carried out by iterat- prehensive description of the rule-based revalidation rules
ing two steps: (i) optimization with respect to partition is available in Ren et al. (2015).
{R}k using swap moves from combinatorial graph-cut
l l=1
optimization (Boykov et al., 2001); and (ii) optimization • Rule 1: if current boundary length < threshold 1 (T ),
1
with respect to region parameters μ using fixed-point then split the neighboring ice regions. The length of
l
iterations (Salah et al., 2011), which interestingly yield the boundary in question between touching ice floes
mean-shift updates (Comaniciu and Meer, 2002). Such is proportional to floe size; i.e., the smaller the floes,
mean-shift updates drive each parameter μ towards the the shorter the length of touching boundaries. Thus,
l
mode of the image distribution of region R. The two main threshold T defines the upper limit of the expected
l 1
control parameters of the KGC algorithm are k (the num- length of the touching boundaries.
ber of regions) and β, which controls the weight of the • Rule 2: if current boundary length < average length
smoothness term. We choose β less than 0.01 to keep the of all neighboring boundaries, then split the neigh-
details in the water-ice segmented image. The selection boring ice regions. The length of the touching
of k is dependent on image distribution, e.g., Gaussian boundary in question is likely shorter than the mean
mixture vs Gamma mixture, and the values of k that we length of other non-touching floe boundaries.
selected were between 2 and 18. For instance, when the • Rule 3: |difference between all neighboring region
actual image distribution approaches Gamma mixture, we intensities| > threshold 3 (T ). If two different ice
3
observed that higher values of k produce better results. floes are touching each other, there is a higher
The optimal labeling λˆ produced by KGC is a continuous possibility that these floes have different intensities.
variable in the range [0, 1], and our results were obtained • Rule 4: |mean intensity of the current bound-
by thresholding λˆ. For water-ice segmentation, only one ary – mean intensity of neighboring ice regions| >
cut-off threshold (τ) (typically τ = 0.1) is required to dis- threshold 4 (T ), then split the ice regions. When two
4
tinguish between water and ice pixels. For ice-type clas- or more floes are touching one another, the touching
sification, two cut-off thresholds are required to classify boundaries are likely to have different intensities due
pixels into open water, first-year ice and multiyear ice. We to stronger backscattering at the floe edge or exist-
note that the ice type classification is based on an opti- ence of open water in between.
mization of the relative contrast in backscattering inten-
sity between first-year ice and multiyear ice for each TS-X 3.3 Manual inspection and correction
image, not accounting for backscattering variation due to Manual inspection/correction was performed at two
incident angle. A globally applicable algorithm for ice type stages. At the first stage, the (black and white) water-
classification is being currently developed for L-, C- and ice image, produced from the KGC algorithm, was visu-
Ku-band SAR by Nghiem et al. (2016). ally inspected to check any erroneous segmentation
(Figure 1). The inspection was done by comparing the
3.2 Floe splitting water-ice image with the original TS-X image, which nor-
Floe splitting was performed through a combination of mally took a few minutes. If the resulting water-ice map
distance transformation, watershed and simple rule-based was not satisfactory (based on a perception of the human
boundary revalidation processing (Ren et al., 2015). We expert), the SAR image was reprocessed with a different
tried to avoid using any sort of shrinking/growing algo- set of KGC parameters (i.e., k or β). Once satisfactory, the
rithm (Soh et al., 1998; Steer et al., 2008), as they will lead water-ice binary image was used to perform floe splitting
to deformation of the floes and inaccurate FSD estimation, as described in Section 3.2 to produce the ice floe-split-
and the implementation requires expensive computing. ting image (Figure 1).
Once the binary water-ice image (0 = water and 1 = ice) The second stage inspection took place after floe split-
has been produced from the SAR image by using the KGC ting had finished. The floe-splitting image was examined
algorithm (see Section 3.1), the distance transform was visually by comparing the floe-splitting image (as shown
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 5 of 23
high-resolution satellite Synthetic Aperture Radar imagery
in Figures 4 and 5) with the original TS-X image. Common line over a truncated range of the CFND. Finding the trun-
errors from the algorithm include a) over-splitting of elon- cated range for LSF is done by visually examining the dis-
gated floes, b) over-splitting due to unmasked melt ponds, tribution. In this study, LSF α was derived for a n umber of
and c) lack of splitting of closely packed floes. Once these truncated ranges for the validation. A recent study shows
errors were identified, they were corrected by removing that the power-law exponent α can be estimated directly
over-split boundary or adding new boundary. This proce- from the distribution and does not require any prescribed
dure typically took about less than an hour. We repeated truncation range (Clauset et al., 2009; Virkar and Clauset,
this procedure, normally two to three times, until satis- 2014). This method (hereinafter referred as VC14) pro-
factory (based on the perception of the human expert) vides a statistically sound estimate of (non-cumulative) α
results are achieved. The whole process took about one or and x (the lower bound to the power-law behavior), and
min
two hours per case, and the final results were then used to a goodness-of-fit to test of whether the data in question
determine the FSD. Further discussions about the effects represent a power-law distribution or not (e.g., a power-
of visual inspection/correction on FSD retrieval can be law distribution if p-value > 0.1; otherwise not the power-
found in Section 4.3. law). As described in Appendix A, the (non-cumulative) α
from VC14 can be converted to cumulative α by subtract-
3.4 FSD calculation ing 1 (or adding 1 if α is defined in negative).
In the final image from the floe-splitting algorithm, all
detected floe boundaries were converted into water pixels 4. Validation results against ground truth
(0 = water). As such, each floe consisted of connected ice 4.1 Selected datasets
pixels, which can be analyzed to calculate the floe size. The We selected four cases for the validation of the algorithm
size of an ice floe can be measured by 1) the area, 2) the in which “ground truth” data were manually produced. The
mean caliper diameter, and 3) the perimeter (Rothrock and selection was made to present diverse sea ice conditions in
Thorndike, 1984). These properties are highly correlated, summer. All selected cases consisted of TerraSAR-X (TS-X)
so that measuring one of them can provide approxima- single-polarized (HH) StripMap (SM) images acquired
tion of the others. Rothrock and Thorndike (1984) found during the summer of 2014, as part of the Marginal Ice
that the area of floes was correlated to the mean caliper Zone (MIZ) project, supported by the U.S. Office of Naval
diameter (i.e., A = 0.66 d2). This relationship satisfies that Research. For all selected TS-X SAR images, we found
perimeter = πd, assuming the floe approximates as a cir- co-located high-resolution visible-band (HRV) images, a
cle. Previous studies defined floe size as the diameter of a result of the declassification effort of the MEDEA group,
circle or a side of a square with the same area of the floe from the U.S. Geological Survey Global Fiducials Library
(Steer et al., 2008; Toyota et al., 2011). If the floe shapes (GFL) (http://gfl.usgs.gov) (Table 1). The exact acquisi-
are irregular, the caliper diameter provides the most real- tion time for TS-X data is known, while such information is
istic representation of the floe size. Thus, in this study the unknown for the GFL HRV images. Nonetheless the same
mean caliper diameter was adopted, which can be calcu- ice floes between TS-X SAR and HRV images can be identi-
lated for each floe by finding the distance between two fied clearly as they did not move very much (Figure 2).
parallel calipers that are just tangent to opposite sides of For the selected SAR images, the intensity values were cali-
the floe and then averaging over all orientations of the brated radiometrically and also scaled linearly to grayscale
calipers. However, caution should be taken for small floes and re-projected to a UTM coordinate, prior to the applica-
as the limited number of tangent lines may provide incor- tion of the proposed algorithm. The pixel spacing of the
rect representation of the size. In this study, the validation original TS-X SM images is 1.25 m, and the pixel spacing of
results were compared as a floe number density distribu- the HRV images is 1 m.
tion (FND) and/or a cumulative floe number distribution Case 1 represents summer ice conditions in which very
(CFND). CFND, or N(d), is power law as N(d) ∝ d-α, where d large floes (> 2 km) are loosely dispersed with smaller
is the mean caliper diameter and α is the power law expo- floes (< 0.5–1 km) (Figure 2a). In Case 2, floes of diverse
nent (Rothrock and Thorndike, 1984). sizes occur in a closely packed ice condition (Figure 2b).
In practice, the power-law exponent α can be calculated For both cases, the same ice floes shown in the SAR
by using a number of different methods. Previously α was images can be easily identified in the corresponding HRV
estimated by fitting the slope of the CFND plot in log-log images (Figure 2a and b), although slight movement
space using a least-square fit (LSF), which exhibits a straight of floes can be seen between the two images. Cases 3
Table 1: Summary of the selected datasets for the validation exercise. DOI: https://doi.org/10.1525/elementa.154.t1
Case SAR acquisition SAR image SAR image location HRV image acquisition HRV image
date (2014) size (km) date (2014) size (km)
1 July 31 10 × 14 74.1°N, 149.0°W July 30 11 × 13
2 July 31 19 × 16 74.5°N, 140.2°W July 31 18 × 16
3 Aug 26 3 × 3 74.7°N, 154.7°W Aug 26 4 × 4
4 Aug 12 3 × 3 74.7°N, 154.7°W Aug 11 4 × 4
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 6 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
Figure 2: SAR and HRV images for four selected cases (Cases 1–4). DOI: https://doi.org/10.1525/elementa.154.f2
represents a late summer ice condition where sea ice floes some cases, however, tracing actual boundaries in TS-X
are highly fragmented; i.e., most of ice floes are less than are quite challenging, especially under compact ice con-
300 m (Figure 2c). Both SAR and HRV images show that ditions. In those cases, the manually traced boundaries
closely packed clusters of small floes occur at the bottom- may not accurately represent the shape of floes in the
left and top-right of the images, with some scattering of SAR images.
floes between two clusters. Case 4 also represents a late In our study, GT data were produced as follows. We
summer ice condition where a mixture of small and large first downsized the image, reducing the resolution of the
floes are clustered together (Figure 2d). In this case, the selected TS-X SAR by 50%; i.e., the pixel spacing (ps) = 2.5
ice condition was much more dynamic, and identifying m. This resolution accommodates a more manageable file
the same floes between SAR and HRV images was more size during manual tracing of touching boundaries of the
challenging. floes. We produced a water-ice segmented image by using
the interactive feature extraction module in ENVI®, rather
4.2 Ground truth (GT) data than KGC. The main reason for this approach was to avoid
It is difficult to obtain a single, absolutely accurate ground using the same algorithm being validated. The ENVI®
truth (GT) that can provide a baseline to measure the valid- module implements an edge-preserving watershed and
ity of the algorithm-produced outputs. As human percep- merging algorithms, and produces a reasonable outcome
tion of texture and intensity of the image may vary from if the threshold is well defined. We manually adjusted the
person to person, manual segmentation can still contain threshold to have as accurate a water-ice image as pos-
inherent variations. Manual segmentation of SAR imagery sible, with the aid of the corresponding HRV image. As
is particularly challenging due to the existence of speckle for the next step, the boundaries between touching floes
and backscattering changes caused by surface rough- were manually traced. Thus, GT images contain open
ness, melting and incident angle. Despite these problems, water and ice regions, with all touching floes separated by
operational sea ice charts have been produced by sea ice manually traced boundaries.
experts through manual analysis of SAR imagery and are Producing GT images took more than three days of a sea
considered as reasonable GT data to validate relevant algo- ice expert’s time for each case. The procedure of drawing
rithms (e.g., Karvonen, 2014). a vector line for each touching boundary was very labor
In this study, we did not use 1-m resolution HRV image extensive. We note that the image size used for GT was
directly to build GT, as the floes were moved around about 10 × 10 km or smaller. In practice, a larger image
between TS-X image and the corresponding HRV image size (e.g., 30 × 30 km or larger) is used to derive FSD.
(due to difference in acquisition time). We used the HRV In such a case, the expert time required for the manual
image as a guide to split touching boundaries, espe- analysis can increase significantly, especially for closely
cially for difficult cases where the floe boundaries were compacted ice conditions. One of the advantages using
unclear in the TS-X image, which provided more objec- the algorithm is to save the human expert labor time in
tive delineation of individual floes in the TS-X image. producing FSD; e.g., it typically takes about one or two
The motivation of building GT was to produce baseline hours for an expert to check and correct the errors from
data that accurately represented the FSD. While build- the algorithm. As part of the algorithm, a manual inspec-
ing GT, we made an effort to trace the floe boundaries as tion/correction is required (see Section 3.3); however, the
seen in HRV images to preserve the shape of the floes. In required expert time is significantly reduced from three
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 7 of 23
high-resolution satellite Synthetic Aperture Radar imagery
days to a couple of hours or less to simply check for any 8, which, as confirmed in HRV image, is clearly a separate
obvious errors. one. However, the algorithm failed to split this small floe
from floe 8 (Figure 4) due to insufficient evidence in the
4.3 Validation results – visual comparison SAR image. Similar issues can be found in floes 6 and 7 in
To validate the algorithm results with the GT data, we first Figure 4.
decreased the image resolution of the selected TS-X SAR One important issue is the existence of low intensity
images by 50% (i.e., pixel spacing = 2.5 m) and applied spots (“false” holes) within an ice area. In Figure 4, there
speckle noise filters prior to running the algorithm. For are low intensity (darker tones) areas in the middle of floe 9.
speckle filtering, we kept the same parameters for median Those low intensity areas can occur due to thinner ice and
(5 × 5), Gaussian (7 × 7) and bilateral (half-width = 15) melt ponds. In the algorithm, we employed speckle filters
filters for all cases. To produce a water-ice image, we set and the KGC smoothing term β to reduce insignificant
KGC parameters as follows: k = 3, β = 0.001 for Cases 1 low intensity spots within ice floes. However, those low
and 2, and k = 3, β = 0.000 for Cases 3 and 4. For Cases intensity spots cannot be removed in some occasions (i.e.,
1 and 2 (typical of early to mid-summer ice condition), large melt ponds), and will result in “false” local minima,
we applied more smoothing (β = 0.001 in KGC) during leading to an over-splitting of floes. In this case, floe 9 was
production of a water-ice image to reduce the effects of over-split by the algorithm but corrected through visual
“false” holes (e.g., low-intensity areas mainly caused by inspection. Another common case for over-splitting can
the presence of melt ponds) within ice floes. Melt ponds be found in floe 10. As can be seen in the HRV image,
(i.e., pools of water formed on sea ice during melting) are floe 10 is clearly a single floe. However, this floe appears
most widespread in late spring, when the effects of “false” to be an aggregation of two floes (e.g., a two hump-like
holes are most significant. In summer, their effects are less shape) in the SAR image with small floes clustered around
significant, as the melt ponds are drained down from the the floe. As the distance transformation is calculated from
ice surface. the floe edge, this two hump-like shape leads to two local
Figure 3 shows the algorithm results for SAR images minima and ends up with over-splitting. If the shape of a
along with GT. When visually compared to GT, the algo- sea ice floe is close to a circle, this issue does not occur.
rithm results agree reasonably well with GT for large ice However, we do find that actual sea ice floes come with
floes but not for smaller floes (Figure 3). To examine the very irregular shapes (such as long elongated ellipse, two
algorithm results in more detail, we cut out a section of hump-like, rectangle and so on). One of the objectives of
HRV, SAR and algorithm-derived floe-split images for Case 2 the visual inspection is to identify and correct those errors.
(Figure 4). Here we would like to pay attention to the floes Next we examine how the algorithm detects small floes.
marked in numbers 1–8 in Figure 4. Those large (≥ ~1 km) For this aim, we selected three sub-areas (marked as A, B
floes are in general well delineated by the algorithm. and C in Figure 4) and magnified these areas in Figure 5.
However, small floes surround some of those large floes, When examining Figure 5, one can see that medium-sized
which makes it difficult to identify the exact floe bound- floes (≥ ~ 200 m) are relatively well delineated by the algo-
ary in SAR images. For example, following a close look at rithm (see floes marked as 1 in sub-areas A–C). Note that
floe 8, one can identify a small floe at the bottom of floe the algorithm successfully resolves small (≥ ~ 100 m) floes
Figure 3: Comparison between algorithm and ground truth shown for SAR images for Cases 1–4. The detected
floe boundaries in both the algorithm (Alg.) and ground truth (GT) images are shown in red lines. DOI: https://doi.
org/10.1525/elementa.154.f3
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 8 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
Figure 4: Comparative HRV, SAR and algorithm-derived floe-split images for Case 2. In the images, the numbers
1–11 and the letters A–C are marked to help the comparison between high-resolution visible (HRV) (top), TerraSAR-X
Synthetic Aperture Radar (SAR) (middle) and algorithm-derived floe-split (bottom) images. In the algorithm-derived
floe-split image, the floe boundaries delineated by the algorithm are shown in red lines and corresponding ellipse fits
in blue lines. The numbers (1–11) represent large (~1 km or larger) floes, and the letters (A–C) represent the sub-areas
that contain small (< ~ 1 km) floes. DOI: https://doi.org/10.1525/elementa.154.f4
Figure 5: Comparative close-up views of the HRV, SAR and algorithm-derived floe-split images for Case 2.
The images are shown for the three sub-areas that contain small (< ~ 1 km) floes (marked as A, B and C in Figure
4). The images are shown for high-resolution visible (HRV) (top), TerraSAR-X Synthetic Aperture Radar (SAR) (mid-
dle) and algorithm-derived floe-split (bottom) images. In the algorithm-derived floe-split image, the floe boundaries
delineated by the algorithm are shown in red lines and corresponding ellipse fits in blue lines. DOI: https://doi.
org/10.1525/elementa.154.f5
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 9 of 23
high-resolution satellite Synthetic Aperture Radar imagery
in sub-area C, as the floes are more dispersed. However, in by the algorithm was much smaller than the one from
sub-areas A and B, small floes are much more packed, and GT; i.e., the algorithm FND was only 40–50% of GT FND
it is very difficult to separate them in a TS-X SAR image (see for Cases 1, 2 and 4 (Figure 6). Most of the floes unde-
floes marked as “2” in sub-areas A and B). The algorithm tected by the algorithm are small floes (≤100 m); i.e., the
considers those small floes that are closely packed together algorithm FND was only 40% or less of GT FND for these
as one larger floe (> ~ 200 m) instead of many individual three cases (Figure 6). This difference suggests that the
ones. The result will be an underestimation of the number algorithm is failing to resolve small (≤100 m) floes, as dis-
density of small floes but overestimation of the number cussed in S ection 4.3.
density of larger floes. This limitation can be partly over- This difference in FND is not due to any difference in
come by using SAR images with a higher resolution. image resolution between the algorithm and GT, as the
same SAR image was used for both the algorithm and GT.
4.4 Validation results – statistical comparison Two factors contributing to the difference are summa-
In Section 4.3 we examined the algorithm results qualita- rized as follows. First, we set the lower pixel limit as 25
tively based on visual comparison with GT. Next we extend pixels, meaning that we ignored any ice area that had less
our validation exercise into a quantitative assessment. We than 25 pixels (equivalent to about 12.5 m in diameter) in
compare the algorithm results with GT in terms of FND the algorithm. Second, de-noising filters and smoothness
and CFND. We first compare FNDs between the algo- term β were applied to subdue low intensity spots caused
rithm and GT (Figure 6). Here we note that FND derived by speckle noise, melt ponds and different ice types
Figure 6: Comparison between algorithm and ground truth as shown in floe number density distribution
plots. Ground truth (GT manual) and algorithm are shown in blue and red colors, respectively. In the figure, N is the
total number of floes, D_mean the mean floe size, and D_median the median floe size. DOI: https://doi.org/10.1525/
elementa.154.f6
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 10 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
(see Section 3.1 and 5.1). This inevitably smoothed out Next we examine the algorithm results using CFND.
some details of the segmented water-ice images. Small We first compare the CFND plots between the algorithm
open water areas between floes are needed for the floe- and GT. For Case 1, CFNDs between the algorithm and GT
splitting algorithm to find the correct floe boundaries, match reasonably well to each other until d is less than
especially for small floes (see Figure 5). We also note that 200 m (Figure 7a). For Case 2, the algorithm CFND match
FND derived by the algorithm in Case 3 is much higher very well with GT until d = 200 m and then slightly deviate
(almost 70% of GT FND) than that in other cases (Figure 6c), from GT until d = 100 m (Figure 7b). The effects of limited
where FND of small (≤100 m) floes from the algo- number of small floes are shown as “flattening” of CFNDs.
rithm approaches almost 60% of GT FND. This result is For Cases 1 and 2, the flattening occurs at d = ~50 m in
partly because no smoothness term in KGC was applied both the algorithm and GT CFNDs (Figure 7a and b). This
(β = 0.00) for this case, and thus more details in the water- flattening can be seen more clearly in GT CFNDs, as they
ice image have been kept. We also note that the algorithm exhibit a straighter line before the flattening. For Case 3,
overestimates FND for d = 100–200 m by ~40% (Figure 6c). the algorithm CFND matches with GT until d = 150 m
We attribute this overestimation to the fact that the algo- and then deviates slightly upward from GT until d = 50 m
rithm derives small floes that are tightly packed together (Figure 8c). For Case 4, the algorithm CFND looks steeper
as a large floe (see Section 4.3). In summary, the algorithm than GT (Figure 7d).
overestimates, compared to GT, mean and median d by Table 2 contains the α values estimated from both the
19–81 m and 23–39 m, respectively, and the overestima- LSF and VC14 methods. LSF α was determined by linearly
tion is the highest in Cases 1, followed by Case 2, 4 and 3 fitting (an outlier-resistant linear regression) CFND in
(Figure 6). log-log space over a truncated floe size range (α ) such
range
Figure 7: Comparison between algorithm and ground truth shown in cumulative floe number density distri-
bution plots. Ground truth (GT-manual) and algorithm are shown in blue and red colors, respectively. N is the total
number of floes. DOI: https://doi.org/10.1525/elementa.154.f7
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 11 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Figure 8: Number density distribution of gray scale intensity values from SAR imagery. (a) Number density
distribution of gray scale intensity values from TerraSAR-X SAR imagery before applying speckle filtering; values for
the same SAR imagery after applying (b) median (3 × 3) filter, (c) median + bilateral (half-width = 7) filters, and (d)
median + bilateral + Gaussian (7 × 7) filters. DOI: https://doi.org/10.1525/elementa.154.f8
as 50–100 m, 100–500 m or 100–500 m. The α value condition (e.g., Cases 1 and 2). Also note that the number
from VC14 were converted to (cumulative) α values by of samples and the size of image used in the validation
subtracting 1 for the comparison with α from CFND (see are quite small. In our normal FSD retrieval, we typically
Appendix A for details). For Case 1, the algorithm α values use SAR images of 30 × 30 km or larger in size. In this
are slightly higher (steeper) than GT values (up to 0.09 case, the algorithm-derived CFND typically exhibits a
for LSF α or up to 0.04 for VC14 α, Table 2). For Case 2, straight line and the number of floes exceeds 1,000 (see
the differences in α increase up to 0.15 (LSF α) or 0.19 Section 5.4).
(VC14 α), indicating a steeper slope from the algorithm In summary, our validation results showed that FND
(Table 2). For Case 3, similar to other cases, the algorithm derived from the algorithm is consistently smaller than
α from LSF is slightly higher (an overestimation of α), those from the GT, especially for small (< 100 m) floes.
but VC14 α shows an underestimation of the algorithm We attribute this underestimation of small floes to the
α (Table 2). Note that VC14 α is not statistically signifi- lower pixel limit (25 pixel, ~12.5 m in d) set in the algo-
cant to be assumed as the power-law distribution (p-value rithm and the limitation in the water-ice segmentation.
from the goodness-of-the-fit < 0.1), which casts a doubt This limitation leads to an overestimation of the algo-
whether such α estimates can be trusted. For Case 4, the rithm α (i.e., steeper slope), as the algorithm tends to
differences in α further increase up to 0.37 (LSF α) or treat those unresolved small floes as larger floes. This
0.432 (VC14 α), indicating a much steeper slope from the overestimation tends to be more significant for a late
algorithm (Table 2). This difference (an overestimation of summer ice condition (Case 4). We also note that the size
α from the algorithm) can be attributed to the algorithm’s of SAR imagery that was used for the validation is much
inability to resolve small (d < 100 m) floes. The algorithm smaller (~10 × 10 km and ~3 × 3 km), and the number
tends to see multiple small floes as a larger floe due to its of floes derived by the algorithm was also quite small
limitation in water-ice segmentation (see Figures 4 and 5). (e.g., N = 555 for Case 4). Thus, the results should be
This increases the number of floes with d = 100–300 m, interpreted with caution. In the next section, we discuss
which causes a steeper slope in CFND (see Figure 7d). various factors affecting the algorithm performance,
This overestimation is more significant for a late sum- including the effect of limited number of floes in a small
mer condition (e.g., Case 4) than for an early summer image size.
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 12 of 23   Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
Table 2: Summary of α values estimated from the least-square fit (LSF)a and VC14b methods. DOI: https://doi.
org/10.1525/elementa.154.t2
| Case | Power-law  | Floe size (m) range  |      | GT α Algorithm αc  |     | ∆α  |
| ---- | ---------- | -------------------- | ---- | ------------------ | --- | --- |
|      | estimator  |                      | (α ) |                    |     |     |
range
|     | LSFa |     |  50–1000 | 1.50 | 1.47 | 0.03  |
| --- | ---- | --- | -------- | ---- | ---- | ----- |
|     | LSF  |     | 100–1000 | 1.46 | 1.52 | –0.06 |
1
|     | LSF   |     | 100–500 | 1.69 | 1.78 | –0.09 |
| --- | ----- | --- | ------- | ---- | ---- | ----- |
|     | VC14b |     | n/ad    | 1.79 | 1.83 | –0.04 |
LSF 50–1000 1.61 1.61 0.00 Downloaded from http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf by guest on 28 May 2026
|     | LSF |     | 100–1000 | 1.57 | 1.65 | –0.08 |
| --- | --- | --- | -------- | ---- | ---- | ----- |
2
|     | LSF   |     | 100–500  | 1.67  | 1.82  | –0.15 |
| --- | ----- | --- | -------- | ----- | ----- | ----- |
|     | VC14b |     | n/a      | 1.66  | 1.85  | –0.19 |
|     | LSF   |     | 50–300   | 3.76  | 3.86  | –0.10 |
| 3   | LSF   |     | 100–300  | 4.93  | 5.06  | –0.12 |
|     | VC14b |     | n/a      | 3.20e | 3.09e | 0.11e |
|     | LSF   |     | 50–1000  | 2.20  | 2.20  | 0.00  |
|     | LSF   |     | 100–1000 | 2.23  | 2.24  | –0.01 |
4
|     | LSF   |     | 100–500 | 2.15 | 2.52 | –0.37 |
| --- | ----- | --- | ------- | ---- | ---- | ----- |
|     | VC14b |     | n/a     | 2.11 | 2.53 | –0.42 |
aCalculated by fitting the slope of CFND in log-log space for various truncated floe size ranges.
bCalculated as suggested by Clauset et al. (2009) and Virkar and Clauset (2014).
cManually revised, through manual inspection/correction. We set the threshold T = 1000 m for Cases 1 and 2, and T = 200 m for
1 1
Cases 3 and 4.
dNot applicable.
eEstimates of α by ground truth (GT) and algorithm that failed the goodness-of-the-fit test (p-value < 0.1), indicating that the
 power-law distribution is not a suitable model.
5. Further discussion and parameter analysis  spots and is not good enough to be used as a base map for
the floe-splitting purpose (see Figure 9d).
5.1 Effects of speckle filtering and KGC parameters
on water-ice segmentation In the example described above, we set k = 2 (Gaussian-
In  the  algorithm,  accurate  segmentation  of  water-ice  mixture) and β = 0.00 (no smoothing) in KGC to cre-
regions is a very important prerequisite for FSD retrieval,  ate  water-ice  segmentation,  in  order  to  demonstrate
as the segmented water-ice image is be used as a base map  the effects of de-noising filters. As mentioned earlier,
to split the boundaries of touching floes (see Section 3).  KGC has shown a potential to produce good segmenta-
In the algorithm, a combination of de-noising filters and  tion results for a range of image distributions such as
KGC is employed to produce accurate water-ice segmenta- Gaussian, Gamma and exponential. In our case, this capa-
tion. SAR imagery acquired over sea ice areas often exhib- bility of KGC is important, as SAR imagery often exhib-
its a Gamma-like image distribution (see the example for  its a Gamma-like distribution, and de-noising alone fails
Case 1 SAR imagery in Figure 8a), which is difficult to  to produce accurate water-ice segmentation. In KGC, the
segment by using conventional methods such as K-mean.  selection of k is dependent on image distribution, e.g.,
Applying even a modest median (3 × 3) filter can signifi- Gaussian mixture vs Gamma mixture. To test this point,
cantly improve the image distribution toward a Gaussian  we set various k values to produce water-ice segmenta-
(Figure 8b), and so does the corresponding water-ice seg- tion, the results of which are shown in Figure 10. We
mentation (Figure 9b). Despite this improvement, the  can see that low intensity spots are greatly reduced when
water-ice image still contains many low intensity spots  we use k = 4 (Figure 10b). Applying higher k (k = 6) fur-
(Figure 9b). These low intensity spots commonly occur  ther reduces low intensity spots within ice regions, but
in sea ice SAR imagery and can be attributed to unfil- also increases high intensity spots (white spots) in water
tered speckle noise, melt ponds and different ice types.  regions (Figure 10c). Much better segmentation results
More distinctive bi-modal Gaussian distribution can be  can be achieved by applying de-noising filters and higher
achieved by applying additional bilateral (half-width = 15)  k (k = 4), although some low intensity spots still occur
 filter (Figure 8c), which further subdues low intensity  within ice regions (Figure 10d).
spots while preserving the floe edges (Figure 9c). Addi- Another KGC parameter β controls the smoothness in
tional Gaussian filter does not improve the image distri- water-ice segmentation (see Section 3.1). To test the effect
bution as the number density distribution remains almost  of β, we produced water-ice segmentation for three differ-
unchanged (Figure 8d), and so does the associated water- ent β values, i.e., β = 0.000, β = 0.001 and β = 0.01. The
ice image which is also almost unchanged in this particu- results are shown in Figure 11. In this test, we kept k = 4
lar case (Figure 9d). As shown in the results, de-noising  and de-noising filters as before. As seen in Figure 11, a slight
filters can significantly reduce low intensity spots and  addition of smoothness (i.e., β = 0.001) greatly improves
improve water-ice segmentation. However, the resulting  the removal of low intensity spots (dark spots) within ice
water-ice segmentation still contains many low intensity  regions (Figure 11b). For the remaining low intensity

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 13 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Figure 9: Water-ice image for Case 1 produced with various speckle filters. The segmentation results were derived
from the TerraSAR-X SAR image (pixel spacing = 2.5 m) (a) without any speckle filter, (b) with a median (3 × 3) filter,
(c) with median and bilateral (half-width = 15) filters, and (d) with median, bilateral and Gaussian (7 × 7) filters. We
set kernel graph cuts (KGC) parameters k = 2 and β = 0.00 (no smoothing) for the segmentation to demonstrate the
effects of speckle filtering. In each panel there are two small red boxes that have been blown up and re-displayed
in the lower left and right corners. No manual inspection/correction was applied for the results shown here. DOI:
https://doi.org/10.1525/elementa.154.f9
spots, they can be further removed by applying a higher β We note that more advanced speckle filters are available
(i.e, β = 0.01) at the expense of losing details of floe edges (e.g., Zabalza et al., 2015), and applying those advanced
(Figure 11c). In our validation exercise described in Section filters can potentially improve the results especially for
4, we used β = 0.01 for Cases 1 and 2 (early to mid-summer) better resolving small floes. As for now, however, a com-
and β = 0.00 for Cases 3 and 4 (late summer). Note, smooth- bined use of speckle filters and KGC is quite effective in
ing is not required for late summer cases, as the effect of producing accurate water-ice segmentation image that
low intensity spots is relatively small (not shown here). For can be used as a base map for floe splitting.
early to mid-summer cases, applying a low β would have
better resolved smaller floes but also promoted over-split- 5.2 Effects of boundary revalidation parameters on
ting of larger ice floes. For example, α and N were increased FSD retrieval
by 0.07 and 257, respectively, when we used β = 0.001 In the previous section, our discussion was focused on
instead of β = 0.01 (from α = 1.51 and N = 832 for β = 0.01) the effects of speckle filters and KGC parameters in pro-
(Figure 11). Applying β = 0.00 (no smoothing) increases ducing accurate water-ice segmentation images. In this
both α and N by 1.81 and 2,225, respectively (Figure 11). section, we turn our attention to the effects of boundary
This over-splitting can be minimized by applying a higher β. revalidation parameters on floe splitting. In our algorithm,
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 14 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
Figure 10: Water-ice image for Case 1 produced with various KGC parameters with and without speckle filter-
ing. The kernel graph cuts (KGC) parameter k for (a) is k = 3, (b) k = 4, (c) k = 6, and (d) k = 4. For (a)–(c), no speckle
filter was applied to TerraSAR-X SAR imagery prior to the water-ice segmentation (see Figures 8a and 9a); for (d),
speckle filters (median, bilateral and Gaussian) were applied to the SAR imagery (see Figures 8d and 9d). In each panel
there are two small red boxes that have been blown up and re-displayed in the lower left and right corners. No manual
inspection/correction was applied for the results shown here. DOI: https://doi.org/10.1525/elementa.154.f10
we used inverse distance transformation combined with boundary of touching floes. For example, if T is too large,
1
watershed to identify the boundaries between touching all the boundaries detected by the algorithm are regarded
ice floes. As this approach normally leads to over-splitting as floe boundaries, promoting over-splitting of floes. If T
1
of floes, we employed a rule-based boundary revalidation is too small, the algorithm can fail to detect some of the
process (see Section 3.2). “real” floe boundaries. To test the effects of T, we derived
1
Among four rules used in this study, we set the constant CFND and α for three different T for all cases, and sum-
1
value for the thresholds for Rules 2–4. Rule 2 regulates marize the results in Table 3. The α value derived from
whether the length of the boundary in question is shorter the algorithm varies with the selection of T, but the dif-
1
than the mean length of other non-touching floe bound- ference in α is within 0.14 for usual selection of T (i.e.,
1
aries or not. If it is shorter, the boundary in question is T = 500 or 1000 m for early to mid-summer, T = 200
1 1
regarded as valid. Rules 3 and 4 examine the difference in or 500 m for late summer). The difference in α between
intensity values among ice regions and along the bound- T = 200 m and T = 1000 m increases up to 0.15 for Case
1 1
ary in question (see Section 3). 1 and up to 0.10 for Case 2 (Table 3).
Different thresholds for Rule 1 (T ) were used depend- As another note for our selected cases, we observed rela-
1
ing on ice conditions. Rule 1 examines whether the length tively small changes inα after visual inspection/correction.
of the boundary in question is short enough to be a valid The largest difference in α (0.05) was found in Case 2
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from  Art. 38, page 15 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Downloaded from http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf by guest on 28 May 2026
Figure 11: Water-ice image for Case 1 produced with various KGC β values. Examples are shown for Case 1 (pixel
spacing = 2.5 m). For (a)–(c), speckle filters (median, bilateral and Gaussian) were applied, and kernel graph cuts (KGC)
k = 4 was used (see Figure 10d). The α value shown in each image is calculated from the algorithm. In each panel there
are two small red boxes that have been blown up and re-displayed in the lower left and right corners. No manual
inspection/correction was applied for the results shown here. DOI: https://doi.org/10.1525/elementa.154.f11
Table 3: Summary of α values for different selections of the boundary revalidation parameter, threshold boundary
length (T ). DOI: https://doi.org/10.1525/elementa.154.t3
1
α valueb (number of floes)
| Case | T  (m)a Before manual correction |     | After manual correction |     |
| ---- | -------------------------------- | --- | ----------------------- | --- |
1
|     | GTc | n/a        |     | 1.79 (1,896)c |
| --- | --- | ---------- | --- | ------------- |
|     | 200 | 1.74 (740) |     | n/a           |
1
|     | 500c | 1.86 (766)c  |     | 1.83 (817)c   |
| --- | ---- | ------------ | --- | ------------- |
|     | 1000 | 1.72 (777)   |     | n/a           |
|     | GTc  | n/a          |     | 1.66 (5,934)c |
|     | 200  | 1.66 (2,894) |     | n/a           |
2
|     | 500c | 1.80 (3,003)c |     | 1.85 (2,984)c |
| --- | ---- | ------------- | --- | ------------- |
|     | 1000 | 1.79 (3,027)  |     | n/a           |
|     | GTc  | n/a           |     | 3.20d (714)c  |
|     | 200c | 3.09d (498)c  |     | 3.09d (498)c  |
3
|     | 500   | 3.09d (498) |     | n/a           |
| --- | ----- | ----------- | --- | ------------- |
|     | 1000  | 3.09d (498) |     | n/a           |
|     | GTc   | n/a         |     | 2.11 (1,059)c |
|     | 200c  | 2.83 (573)c |     | 2.53 (555)c   |
4
|     | 500  | 2.75 (580) |     | n/a |
| --- | ---- | ---------- | --- | --- |
|     | 1000 | 2.75 (580) |     | n/a |
aBoundary revalidation parameter T defining the upper limit of the expected length of the touching boundaries.
1
bValues for α calculated by the VC14 method.
cGround truth (GT) and the algorithm values used in the validation exercise in Section 4.3.
dEstimates of α by ground truth (GT) and algorithm that failed the goodness-of-the-fit test (p-value <0.1), indicating that the
 power-law distribution is not a suitable model.
(early  summer  case)  and  the  smallest  was  found  in  a larger data set), we found that the difference due to
Cases 3 and 4 (late summer cases). This finding is partly  manual inspection was about 0.16 on average, but it
because  over-splitting commonly occurs in larger floes,  increased up to 0.67 for some cases. The cases show-
and visual inspection/correction is more difficult for  ing  larger  difference  are  typically  associated  with  a)
small floes. The small changes in α (∆α ≤ 0.05) for the  over-splitting by unfiltered melt ponds, b) over-split-
four selected cases raises a question whether the man- ting of elongated floes, and c)  under-splitting of closely
ual inspection is required. In practice (when we analyze  packed floes.

Art. 38, page 16 of 23   Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
5.3 Effects of image resolution resolution, but slightly decreases or remains the same
As discussed in Section 4.1, we used the half resolution  from the half resolution to the full resolution (Table 4).
images (ps = 2.5 m) to derive FSD. In this section, we  The increase of the algorithm α from the quarter resolu-
extend our discussions and analyze how the image reso- tion to the half resolution is expected, as a higher reso-
lution would affect FSD retrieval. For this purpose, we  lution is helpful to resolve small floes. However, smaller
added two more image resolutions, i.e., a full resolution  or similar α from the full resolutions is unexpected,
(ps = 1.25 m) and a less than quarter resolution (degraded  especially for Case 4 which is almost 0.50 less (Table 4).
to 15% of the full resolution) (ps = 8.33 m). Table 4 sum- Why does the full resolution image produce a smaller
marizes the results in α and N for all four selected cases.  (less steep) α? Here we first compare x  (lower-bound
min
First, we note that the algorithm α is very comparable  to the power-law behavior estimated by the method of
Downloaded from http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf by guest on 28 May 2026
between full and half resolutions for Cases 1 and 2 (i.e., the  Vikar and Clauset, (2014) between the half resolution and
difference is ≤0.01) (Table 4). For Cases 3 and 4, the differ- the full resolution for Case 3. At the half and full resolu-
ence is much larger, i.e., 1.48 for Case 3 and 0.50 for Case 4  tion x  is 158 m and 79 m, respectively, which indicates
min
(Table 4). The results from Cases 3 and 4 need to be inter- the ability to resolve smaller floes at the full resolution.
preted with caution as the derived FSD may not represent  In Section 4.4, the algorithm showed a higher (steeper)
floe statistics due to the small number of floes derived in  α than GT, mainly because the algorithm saw a congrega-
a limited size coverage of the image (i.e., ~3 × 3 km). In  tion of small (d < 100 m) floes as a larger floe (Figure 5),
particular, the goodness-of-the-fit test showed that VC14  which increased the number of floes with d = 100–300 m
α for Case 3 is not statistically significant (i.e., unlikely the  (Figure 6). We speculate that the increased (full) image
power-law), and that the VC14 method failed to estimate  resolution has helped to resolve such small floes that were
α for the quarter resolution (Table 4).    otherwise detected as a larger floe at the half resolution,
In Figure 12, the FSD results from Case 2 are shown  which caused less steep slope in CFND (Figure 12).
for detailed analysis. First, the difference in FND mainly  As mentioned earlier, the validation cases were made
occurs in small (≤100 m) floes, where the FND of small  for small sub-images (~10 × 10 km or  3 × 3 km). Thus,
~
(<100 m) floes from the full resolution is almost doubled  the number of floes derived by the algorithm can be very
or 7 times higher than the ones from half or quarter reso- small, especially for the quarter resolution. In the next sec-
lutions, respectively. Also note that the mean and median  tion, we use a larger image to examine how CFND and α
d derived by the algorithm become smaller as the image  behave between different image resolutions if sufficient
resolution increases, which suggests that a higher image  number of floes can be derived.
resolution is certainly helpful to resolve small (≤100 m)
floes. 5.4 FSD retrieval from a larger image
Comparison  of α  for  different  image  resolution  is  In previous sections, we found some of the algorithm
summarized in Table 4. For Cases 1 and 2, the algo- results might not be representative due to an insufficient
rithm α increases from the quarter resolution to the half  number of floes derived from small sub-images. In our
Table 4: Summary of α values for various image resolutions. DOI: https://doi.org/10.1525/elementa.154.t4
| Case Image   | Pixel   α valuea |       | Number of  |
| ------------ | ---------------- | ----- | ---------- |
|  resolution  | size (m)         |       | floes      |
| GTb          | 2.50             | 1.79b | 1,896b     |
| Quarter      | 8.33             | 1.74  | 249        |
1
| Halfb   | 2.50 | 1.83b | 817b   |
| ------- | ---- | ----- | ------ |
| Full    | 1.25 | 1.83  | 1,546  |
| GTb     | 2.50 | 1.66b | 5,934b |
| Quarter | 8.33 | 1.74  | 1,414  |
2
| Halfb   | 2.50 | 1.85b   | 2,984b |
| ------- | ---- | ------- | ------ |
| Full    | 1.25 | 1.84    | 5,408  |
| GTb     | 2.50 | 3.20b,c | 714b   |
| Quarter | 8.33 | n/a     | n/a    |
3
| Halfb   | 2.50 | 3.09b,c | 498b   |
| ------- | ---- | ------- | ------ |
| Full    | 1.25 | 4.57    | 809    |
| GTb     | 2.50 | 2.11b   | 1,059b |
| Quarter | 8.33 | 2.08    | 90     |
4
| Halfb | 2.50 | 2.53b | 555b |
| ----- | ---- | ----- | ---- |
| Full  | 1.25 | 2.03  | 719  |
aValues for α (after manual correction) calculated by the VC14 method.
bGround truth (GT) and the algorithm values used in the validation exercise in Section 4.3.
cEstimates of α by GT and algorithm that failed the goodness-of-the-fit test (p-value <0.1), indicating that the power-law distribution
is not a suitable model.

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 17 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Figure 12: FSD results for Case 2 produced for different image resolutions. Floe size distribution results are
shown for (A) quarter resolution (pixel spacing = 8.3 m), (B) half resolution (pixel spacing = 2.5 m), and (C) full reso-
lution (pixel spacing = 1.25 m). The results are shown as floe-splitting image (left), and distributions of floe number
density (middle) and cumulative floe number density (right). DOI: https://doi.org/10.1525/elementa.154.f12
normal FSD retrieval, we typically use a larger SAR image sub-images. Figure 13 shows FSD results derived from
(30 × 30 km or larger) to derive FSD, and the derived SAR images with two different resolutions (quarter and
CFNDs usually exhibit quite a straight line, with the num- half resolutions) for Case 1. First, the number of floes
ber of floes derived from the algorithm exceeding over derived from the algorithm is 1,898 (even for the quarter
1,000. The size of TS-X images used for the validation exer- image resolution), and CFND exhibits quite a straight line
cise was much smaller than 30 × 30 km (Table 1). This is (no local deviation visible). The α values are slightly lower
because the validation image size was limited by finding than the validation case (1.74 from the larger image vs.
the area that overlapped between TS-X and HRV images, 1.83 from the validation). This difference can be attributed
and this process became difficult due to cloud cover in the to regional differences (larger vs. small areas) or simply an
HRV images. insufficient number of floes in the validation results. Also
In this section, our objectives are twofold. First, we re- note that the difference in α between the VC14 and LSF
examine how the shape of CFND plots changes with a methods is very small (less than 0.05) (Figure 13). Second,
larger number of samples. For this purpose, we divided the difference in VC14 α between quarter and half reso-
the original SAR images (30 × 60 km) into sub-images lutions is also small (within 0.09) for the large image
(30 × 30 km), and derived corresponding FSDs from those (Table 4 and Figure 13).
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 18 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
Figure 13: The algorithm results from a larger SAR (30×30 km) image for Case 1. Panel A shows TerraSAR-X SAR
(left), floe-split map (middle) and corresponding distributions of floe number density and cumulative floe number
density for the quarter image resolution (pixel spacing = 8.33 m). Panel B shows the same but for the half image reso-
lution (pixel spacing = 2.50 m). The α values shown are calculated using both the VC14 and LSF methods. The esti-
mates of α from the VC14 method are not statistically significant for both resolutions. The LSF α values are derived
for α = 200–3000 m. In the floe number density plots, floe size group is as follow: group 1 is for 0 m ≤ d < 100
range
m, group 2 is for 100 m ≤ d < 200 m…, group 16 is for d ≥ 1600 m. Manual inspection/correction was applied for the
results. DOI: https://doi.org/10.1525/elementa.154.f13
Figure 14 shows the same comparison results between speckle filtering, (ii) water-ice segmentation by kernel
two image resolutions for Case 3. Similar to Case 1, the graph cuts (KCG) and (iii) floe splitting by a combination
number of floes exceeds 4,000, and CFND exhibits quite of distance transformation, watershed and rule-based
a straight line. In particular, we note that FNDs for small boundary revalidation methods. To test the performance
floes (< 200 m, floe size group 1 and 2) derived from the of the algorithm, we selected four cases that represent sea
half resolution image are significant higher than those ice conditions during early to later summer. All selected
from the quarter resolution image (Figure 14), which cases consisted of both TerraSAR-X SAR (TS-X SAR, Strip-
makes the total number of floes 13,554 for the half resolu- Map, single polarization HH) and high-resolution visible-
tion image. In the validation case (image size = 4 × 4 km), band (HRV) imagery (USGS GFL). Ground truth (GT), used
the VC14 method failed to estimate α from the quarter as baseline data to validate the algorithm, was created for
resolution image (Table 4). We speculated this failure was each case by using a feature extraction module in ENVI®
owing to insufficient floe number (N = 103 for the quar- and then manually tracing floe boundaries with the aid of
ter resolution) from the small image. For the larger image HRV images.
(30 × 30 km), the difference in α between quarter and half The results show that the algorithm considerably
resolutions is reduced to 0.23, due to sufficient numbers underestimated the number density of small (d ≤ 100 m)
of floes derived for both resolutions. More importantly, ice floes. This underestimation is mainly due to a lower
the VC14 α values are statistically significant (p-value > 0.1 pixel limit (25 pixels) used in the algorithm as well as the
for the goodness-of-the-fit). The difference in α in Case 3 limitation in water-ice segmentation, especially for small
is larger than what we found in Case 1 (0.09), likely due floes that were closely packed together. These combined
to a much higher number of small floes. Nonetheless, this effects caused almost 36–75 % underestimation for small
confirms that CFND and α can be reasonably compara- (d ≤ 100 m) floes, while increased the number of larger
ble between quarter (ps = 8.33 m) and half (ps = 2.50 m) (d = 100–300 m) floes. This has led to the algorithm α
image resolutions if a sufficient number of floes can be over-estimated by 0.04–0.19 (Cases 1 and 2, early summer
derived from a larger image. case) or by 0.12–0.42 (Cases 3 and 4, late summer case)
(Table 2). The relatively large difference in α between GT
6. Summary and closing remarks and the algorithm for Case 4 highlights its limitation, i.e.,
In this study, we have presented a set of algorithms that detecting a congregation of small floes as a larger floe.
derive summer sea ice FSD from high-resolution SAR This effect is more severe in a late summer condition
imagery. The proposed algorithm is comprised of (i) when small floes are closely packed (Figures 4 and 5).
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 19 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Figure 14: The algorithm results from a larger SAR (30×30 km) image for Case 3. Panel A shows TerraSAR-X SAR
(left), floe-split map (middle) and corresponding distributions of floe number density and cumulative floe number
density for the quarter image resolution (pixel spacing = 8.33 m). Panel B shows the same but for the half image
resolution (pixel spacing = 2.50 m). The α values shown are calculated using both the VC14 and LSF methods. The
estimates of α from VC14 are statistically significant for both resolutions (i.e., the power-law distribution). The LSF α
values are derived for α = 200–1000 m. In the floe number density plots, floe size group is as follow: group 1 is for
range
0 m ≤ d < 100 m, group 2 is for 100 m ≤ d < 200 m…, group 16 is for d ≥ 1600 m. No manual inspection/correction
was applied for the results. DOI: https://doi.org/10.1525/elementa.154.f14
This limitation may be overcome by using a higher resolu- remaining low intensity spots (for early to mid-summer
tion image, as the algorithm α became more comparable cases), producing water-ice segmentation maps that are
to GT α when the full resolution image was used (Table 4). good enough for floe splitting.
Several factors affecting algorithm performance were Floe splitting was done by a combination of inverse dis-
addressed. The results showed that a combination of tance transformation, watershed and rule-based bound-
speckle filtering and KGC was effective in producing the ary revalidation, using the water-ice segmented image (as
best water-ice segmentation (Section 5.1). SAR imagery described above) as a base map (see Section 3.2). We exam-
acquired over sea ice areas often exhibits a Gamma- ined the effects of boundary revalidation parameters to
mixture image distribution (Figure 8a), for which it is determine whether a certain boundary detected by water-
difficult to produce water-ice segmentation using conven- shed will be kept (splitting) or discarded (merging). Our dis-
tional methods such as K-means. We found that speckle cussion was focused around T for Rule 1, which determined
1
filters (median, bilateral, Gaussian) could be used to refine either splitting or merging based on the length of the bound-
the image distribution into a Gaussian by subduing low ary in question. The selection of different T did affect the
1
intensity spots (“false” holes) that were caused by unfil- algorithm CFND and α, but the difference in α was relatively
tered speckles, melt ponds and different ice types within small if T was reasonably selected (Table 3). For instance,
1
ice regions (Figures 8 and 9). Despite the improvement, the difference in α remained within 0.14 for Cases 1 and 2
speckle filters themselves would not be sufficient to pro- (early to mid-summer ice condition) between various T val-
1
duce satisfactory water-ice image for floe splitting (i.e., ues (Table 4). Note, we typically use T = 500 or T = 1000
1 1
too many low intensity spots) (Figure 9d). This limita- m for the image acquired during early to mid-summer ice
tion could be improved by employing a larger k in KGC condition). Our results also showed that the difference in α
to further subdue unwanted low intensity spots even between before and after manual (visual) inspection are quite
before applying speckle filters (Figure 10a–c). By com- small (within 0.05) for all four cases (Table 3). Although the
bining KGC with a larger k with speckle filters, significant validation results showed that manual inspection could have
improvement could be achieved. However, water-ice seg- a very small impact on the derived α, in practice the manual
mentation map still contained some low intensity spots inspection could have a significant impact on the results
for early to mid-summer cases (Figure 10d). Slight addi- (e.g., causing a difference in α up to 0.67 for some cases). The
tion of smoothness β in KGC effectively subdued the cases showing larger difference are typically associated with
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 20 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
a) over-splitting by unfiltered melt ponds, b) over-splitting of idea. One of the critical issues for SAR imagery acquired
elongated floes, and c) under-splitting of closely packed floes. during early summer is the significant presence of large
We also addressed how different image resolutions melt ponds. Melt ponds are potentially important for
would affect the FSD retrieval (Section 5.3). The results FSD, because they serve as “weaker points” for the floes
were compared in three different resolutions; i.e., the to break up (Arntsen et al., 2015). At the same time, those
quarter resolution (ps = 8.3 m), the half resolution (ps melt ponds at their maximum can cause significant prob-
= 2.5 m) and the full resolution (ps = 1.25 m). The com- lems for FSD retrieval, in which cases the current algo-
parison results showed that the algorithm α values at the rithm (even with smoothing, large β) cannot eliminate
half resolution were higher (steeper) than the ones at the the low intensity spots caused by large melt ponds. In
quarter resolution (Table 4). This effect was expected, the future, automatically masking melt ponds would be
as a higher resolution is helpful to resolve small floes needed to robustly derive FSD from early summer SAR
(Figure 12). The algorithm α values at the full resolution, imagery.
however, were smaller (less steep) than the ones at the
half resolution (Table 4). We speculate that the result of Appendix A: Comparison with previous studies
lower α values at the full resolution is likely due to the Regarding the comparison of the exponent α values, we
increased resolution that helped to resolve the small floes first note that the exponent α values reported in previ-
that were otherwise detected as a larger floe at the half ous studies are dependent on whether the slope in log-
resolution. log space is derived from cumulative distribution or
When we examined the validity of FSD statistics from a non-cumulative distribution (see Stern et al., 2017b, for
larger (30 × 30 km) image (see Section 5.4), the number more detailed discussions). In previous studies, a cumu-
of floes derived from the algorithm exceeded 1,000, and lative distribution was typically used to estimate α (i.e.,
CFNDs exhibited quite straight lines (i.e., no local devia- the slope of the distribution in log-log space) (Table A1).
tion as shown in validation cases). For larger images, the In a few studies, non-cumulative distribution was used to
difference in α between quarter and half resolution was estimate α, in which case non-cumulative α can be con-
0.09–0.23 (Figure 13 and 14). verted to cumulative α by subtracting 1 (or adding 1 if α
In conclusion, the results showed that the algorithm is defined as negative). For, non-cumulative α from Stern
α varied between 0.04 and 0.42, including the valida- et al. (2017a) and Hwang et al. (2017) would have ranges
tion against GT and the effects of different image reso- of 1.0–1.6 and 1.9–2.5, respectively, when converted to
lutions, as well as the effects of control parameters cumulative α (Table A1).
such as k, β and T and visual (manual) inspection. This As can be seen in Table A1, the range of cumulative α
1
degree of variability means that a combination of the values from Rothrock and Thorndike (1984), Holt and
algorithm and manual inspection could be used to Martin (2001) and Perovich and Jones (2014) is 1.7–2.5.
derive FSD from SAR imagery with some accuracy com- The range of cumulative α values from this study is 1.5–
pared to what a human expert could manually produce. 2.2, if Case 3 is excluded (see Table 4 in this study), which
Here we stress that our purpose of the algorithm devel- is comparable to previous studies. Note that the selected
opment is to minimize (not replace) the labor and time cases used in this study were drawn from a larger dataset
of a human expert, to provide consistent FSD retrieval, in Hwang et al. (2017); i.e., we selected the four cases that
and to mimic what an expert produces manually with had corresponding 1-m resolution visible images among
sufficient time and effort. Human intervention by an the dataset used in Hwang et al. (2017). In Hwang et al.
expert is still necessary to check and correct errors at (2017), we used the algorithm developed in this study
the end of production of water-ice segmented image to segment and delineate floe boundary from TS-X data,
and floe splitting, but much less time and effort is but used another (non-cumulative) method suggested
needed in comparison to conventional fully manual by Clauset et al. (2009) and Virkar and Clauset (2014) to
FSD retrieval. In our case, an expert spent at least three calculate power law coefficient α. In Hwang et al. (2017),
full days to construct GT, yet with the algorithm, the the mean α values for July and August are 1.9 and 2.5
expert spent only a couple of hours to check and cor- (when converted to cumulative α), respectively, which
rect errors. are also within the range reported in previous studies. We
For future work, there are still remaining challenges note that the cumulative α value for Case 3 in this study
in the algorithm; i.e., (i) resolving small (≤100 m) floes, is much higher than other cases (Table 4). This case rep-
(ii) more automated correction for the errors, and (iii) resents a convex curve of cumulative distribution, not a
melt pond detection. Small (≤100 m) floes may be better straight line, representing a homogeneous floe size regime
resolved by employing more advanced speckle filters (e.g., (Figure 7c). This relatively high α may reflect that the
Zabalza et al., 2015) and/or optimization-based schemes. power law is not a suitable model to fit the distribution.
We are currently working on these algorithms to see When the goodness-of-the-fit test (Clauset et al., 2009;
whether more details of floe edges can be preserved while Virkar and Clauset, 2014) is applied to Case 3, it shows the
suppressing low intensity spots in SAR imagery. In this distribution is unlikely a power law distribution.
study, we used four simple rules to validate the boundary, The cumulative α values from Wang et al. (2016) are
but more comprehensive rules can be added to further much shallower (1.0–1.5) than the reported values stated
reduce the errors. Combining the rule-based method with above (Table A1). If the non-cumulative α values in Stern
other algorithms such as active contour is an interesting et al. (2017a) are converted into cumulative α values, their
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 21 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Table A1: The range of exponent α values from previous studies in the Beaufort Sea (adapted from Stern et al., 2017b).
DOI: https://doi.org/10.1525/elementa.154.ta1
Time period Exponent α range Floe size range (m) Data source
June 21, 1974–Aug 1.7–2.5 (cumulative) 100–20,000 Aerial photography, Rothrock and
18, 1975 Thorndike (1984)
Aug 14–20, 1992 1.9–2.2 (cumulative) 900–10,000 ERS-1 SAR, Holt and Martin (2001)
June–Sept, 1998 2.0–2.2 (cumulative), 10–10,000 Aerial photography, Perovich and
following seasonal cycle Jones (2014)
Summer–autumn, 2014 1.0–1.5 (cumulative) 5–10,000 High resolution visible satellite
data, Wang et al. (2016)
Mar–Oct, 2013, 2014 2.0–2.6 (non-cumulative), 10–13,000 MODIS, and high-resolution
following seasonal cycle satellite data
July–Aug, 2014 2.9 (non-cumulative, July mean) 200–3,000 TerraSAR-X, Hwang et al (2017)
and 3.5 (non-cumulative,
Aug mean)
Four samples in 1.5–2.2a (cumulative, GT) 50–3,000 TerraSAR-X, This study
July–Aug, 2014 1.5–2.2a (cumulative, algorithm)
aValues exclude Case 3.
values (1.0–1.6) become comparable to Wang et al. (2016). Advanced Remote Sensing and German Aerospace Center
Here, we note that Stern et al. (2017a) mostly used MODIS (DLR, TSX SSS projects phwang_OCE2306) for the Ter-
images (a pixel size of 250 m) to derive their α values. raSAR-X data. We thank U.S. Geological Survey for the
Although the α values from MODIS have shown some Global Fiducials Library images. We thank Harry Stern for
consistency with the values from 1-m resolution MEDEA comments on the manuscript.
images (referred as HRV images in this study) for limited
cases during May to early July (Figures 12 in Stern et al., Funding information
2017a), the TS-X derived α values were generally steeper Funding was provided by the Office of Naval Research
(Figure 13 in Stern et al., 2017a). We note that MODIS reso- (grants N00014-12-1-0359, N00014-12-1-0448) as part
lution may be insufficient to resolve small floes in summer, of the Marginal Ice Zone, Department Research Initiative,
and this may result in a shallow slope from MODIS. Wang ONR MIZ, by the UK Natural Environment Research Coun-
et al. (2016), however, used high-resolution satellite data cil (grants NE/M00600X/1, NE/L012707/1), and by the
(such as MEDEA and Landsat), where it is expected that BAGEP Award of the Science Academy.
their α values would be consistent with previous studies
and our study. In particular, MEDEA data used in Wang et Competing interests
al. (2016) covered the Beaufort Sea (74–76N, 149–150W) The authors have no competing interests to declare.
and spanned August 2–16. Some possible causes for the
inconsistencies include 1) actual spatial and temporal Author contributions
variability in FSD, 2) sampling variability, 3) inadequacy of • Contributed to conception and design: BH, JR
the power law as a model of the FSD, and 4) poor analysis • Contributed to acquisition of data: HG, BH
method (Stern et al., 2017b). Considerable variability in • Contributed to analysis and interpretation of data:
FSD can occur within a relatively short distance (Hwang et BH, JR, SM, CB, IB, EA
al., 2017), and limited coverage of satellite image can pro- • Drafted and/or revised the article: BH, JR, IB, HG, EA
duce some inconsistency, especially if only a few images • Approved the submitted version for publication: BH,
were analyzed for comparison. For some cases (like Case JR, IB, HG, EA
3 in this study), the power law is not the best model to
describe the FSD. Poor analysis including inappropriate References
binning and truncation of the distribution can cause some Arntsen, AE, Song, AJ, Perovich, DK and
variability in the retrieved FSD (see Stern et al., 2017b). Richter-Menge, JA 2015 Observations of the sum-
mer breakup of an Arctic sea ice cover. G eophys
Data Accessibility Statement Res Lett 42: 8057–8063. DOI: https://doi.
The FSD results are available by contacting BH (phil. org/10.1002/2015GL065224
hwang@sams.ac.uk). Barber, DG and LeDrew, E 1991 SAR sea ice discrimina-
tion using texture statistics: a multivariate approach,
Acknowledgements Photogrammetric Engineering & Remote Sensing 57:
We gratefully acknowledge the support from the Office 385–395.
of Naval Research and UK Natural Environment Research Boykov, Y, Veksler, O and Zabih, R 2001 Fast approxi-
Council. We thank Center for Southeastern Tropical mate energy minimization via graph cuts. IEEE
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Art. 38, page 22 of 23 Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from
high-resolution satellite Synthetic Aperture Radar imagery
Trans Pattern Anal Mach Intell 23(11): 1222–1239. ice classification and mapping for surface albedo
DOI: https://doi.org/10.1109/34.969114 parameterization in sea ice modeling. AGU Fall
Clauset, A, Shalizi, CR and Newman, MEJ 2009 Meeting, San Francisco, 12–16 December.
Power-law distributions in empirical data. Ren, J, Hwang, B, Murray, P, Sakhalkar, S and
SIAM Review 51(4): 661–703. DOI: https://doi. McCormack, S 2015 Effective SAR sea ice image
org/10.1137/070710111 segmentation and touch floe separation using a
Clausi, DA, Qin, AK, Chowdhury, MS, Yu, P and combined multi-stage approach. In Proc IEEE Int
Mailard, P 2010 MAGIC: Map-guided ice classifica- Geoscience and Remote Sensing Symposium, Milan,
tion system. Can J Remote Sensing 36(1): S13–S25. Italy, 1040–1043. DOI: https://doi.org/10.1109/
DOI: https://doi.org/10.5589/m10-008 igarss.2015.7325947
Clausi, DA and Yue, B 2004 Comparing cooccurrence Rothrock, DA and Thorndike, AS 1984 Measuring
probabilities and Markov random fields for tex- the sea ice floe size distribution. J Geophys Res
ture analysis of SAR ice imagery. IEEE Trans Geosci 89: 6477–6486. DOI: https://doi.org/10.1029/
Remote Sens 42(1): 215–228. DOI: https://doi. JC089iC04p06477
org/10.1109/TGRS.2003.817218 Salah, MB, Mitiche, A and Ayed, IB 2011 Multire-
Comaniciu, D and Meer, P 2002 Mean shift: A robust gion image segmentation by parametric ker-
approach toward feature space analysis. IEEE Trans nel graph cuts. IEEE Trans Image Processing
Pattern Anal Mach Intell 24(5): 603–619. DOI: 20(2): 545–557. DOI: https://doi.org/10.1109/
https://doi.org/10.1109/34.1000236 TIP.2010.2066982
Deng, H and Clausi, DA 2005 Unsupervised segmenta- Soh, L-K, Holt, B and Tsatoulis, C 1998 Identifying
tion of Synthetic Aperture Radar sea ice imagery ice floes and computing ice floe distributions in
using a novel Markov random field model. IEEE SAR images. In Tsatoulis, C and Kwok, R (eds.),
Trans Geosc Remote Sens 43(3): 528–538. DOI: Analysis of SAR Data of the Polar Regions, 9–34,
https://doi.org/10.1109/TGRS.2004.839589 Springer-Verlag, New York. DOI: https://doi.
Haverkamp, D, Soh, LK and Tsatsoulis, C 1995 A org/10.1007/978-3-642-60282-5_2
comprehensive, automated approach to determin- Steele, M 1992 Sea ice melting and floe geom-
ing sea ice thickness from SAR data. IEEE Trans etry in a simple ice-ocean model. J Geophys
Geos Remote Sens 33: 46–57. DOI: https://doi. Res 97: 17729–17738. DOI: https://doi.
org/10.1109/36.368223 org/10.1029/92JC01755
Holt, B and Martin, S 2001 The effect of a storm on Steer, A, Worby, AP and Heil, P 2008 Observed changes
the 1992 summer sea ice cover of the Beau- in sea-ice floe size distribution during early sum-
fort, Chukchi, and East Siberian Seas. J Geophys mer in the western Weddell Sea. Deep-Sea Research
Res 106(C1): 1017–1032. DOI: https://doi. II 55: 933–942. DOI: https://doi.org/10.1016/j.
org/10.1029/1999JC000110 dsr2.2007.12.016
Horvat, C and Tziperman, E 2015 A prognostic model of Stern, HL, Schweiger, AJ, Stark, M, Zhang, J, Steele,
the sea ice floe size and thickness distribution. The M and Hwang, B 2017a Seasonal Evolution of the
Cryosphere Discuss 9: 2955–2997. DOI: https://doi. Sea-Ice Floe Size Distribution in the Beaufort and
org/10.5194/tcd-9-2955-2015 Chukchi Seas. Elementa (under review).
Hwang, B, Wilkinson, J, Maksym, E, Graber, HC, Stern, HL, Schweiger, AJ, Zhang, J and Steele, M 2017b
Schweiger, A, Horvat, C, Perovich, DK, Arnt- Is it possible to reconcile disparate studies of the
sen, AE, Stanton, TP, Ren, J and Wadhams, P sea-ice floe size distribution? Elementa (under
2017 Winter-to-summer transition of Arctic sea ice review).
breakup and floe size distribution in the Beaufort Tomasi, C and Manduchi, R 1998 Bilateral Filtering for
Sea. Elem Sci Anth. In press. Gray and Color Images. In Proceedings of the IEEE
Karvonen, J 2014 A sea ice concentration estimation International Conference on Computer Vision ‘98,
algorithm utilizing radiometer and SAR data. 836–846. January, New Delhi. DOI: https://doi.
The Cryosphere 8: 1639–1650. DOI: https://doi. org/10.1109/iccv.1998.710815
org/10.5194/tc-8-1639-2014 Toyota, T, Haas, C and Tamura, T 2011 Size distribution
Kwok, R, Rignot, E and Holt, B 1992 Identification of and shape properties of relatively small sea ice floes
sea ice types in Spaceborne Synthetic Aperture in the Antarctic marginal ice zone in late winter.
Radar data. J Geophys Res 97(C2): 2391–2402. DOI: Deep-Sea Research II 58(9–10): 1182–1193. DOI:
https://doi.org/10.1029/91JC02652 https://doi.org/10.1016/j.dsr2.2010.10.034
Maillard, P, Clausi, DA and Deng, H 2005 Map-guided Toyota, T, Takatsuji, S and Nakayama, M 2006 Charac-
sea ice segmentation and classification using SAR teristics of sea ice floe size distribution in the sea-
imagery and a MRF segmentation scheme. IEEE sonal ice zone. Geophys Res Lett 33(L02): 616. DOI:
Trans Geosc Remote Sens 43(12): 2940–2951. DOI: https://doi.org/10.1029/2005GL024556
https://doi.org/10.1109/TGRS.2005.857897 Virkar, Y and Clauset, A 2014 Power-law distribu-
Nghiem, SV, Clemente-Colón, P, Perovich, DK, tions in binned empirical data, The Annals of
Polashenski, C, Simpson, WR, Rigor, IG, Woods, Applied Statistics 8(1): 89–119. DOI: https://doi.
JE, Nguyen, D and Neumann, G 2016 Arctic sea org/10.1214/13-AOAS710
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026

Hwang et al: A practical algorithm for the retrieval of floe size distribution of Arctic sea ice from Art. 38, page 23 of 23
high-resolution satellite Synthetic Aperture Radar imagery
Wang, Y, Holt, B, Rogers, WE, Thomson, J and Zabalza, J, Ren, J, Zheng, J, Han, J, Zhao, H, Li, S and
Shen, HH 2016 Wind and wave influences on sea Marshall, S 2015 Novel two dimensional singu-
ice floe size and leads in the Beaufort and Chukchi lar spectrum analysis for effective feature extrac-
Seas during the summer-fall transition 2014. J tion and data classification in hyperspectral
Geophys Res 121(2): 1502–1525. DOI: https://doi. imaging, IEEE Trans. Geoscience and Remote Sens
org/10.1002/2015JC011349 53(8): 4418–4433. DOI: https://doi.org/10.1109/
Williams, TD, Bennetts, LG, Squire, VA, Dumont, D TGRS.2015.2398468
and Bertinoa, L 2013a Wave-ice interactions in Zhang, J, Schweiger, A, Steele, M and Stern, H 2015
the marginal ice zone. Part 1: Theoretical founda- Sea ice floe size distribution in the marginal ice
tions, Ocean Model 71: 81–91. DOI: https://doi. zone: Theory and numerical experiments. J Geophys
org/10.1016/j.ocemod.2013.05.010 Res Oceans 120: 3484–3498. DOI: https://doi.
Williams, TD, Bennetts, LG, Squire, VA, Dumont, D org/10.1002/2015JC010770
and Bertinoa, L 2013b Wave-ice interactions in the Zhang, J, Stern, H, Hwang, B, Schweiger, A, Steele,
marginal ice zone. Part 2: Numerical implementa- M, Stark, M and Graber, HC 2016 Modeling the
tion and sensitivity studies along 1D transects of seasonal evolution of the Arctic sea ice floe size
the ocean surface. Ocean Model 71: 92–101. DOI: distribution. Elementa: Science of the Anthropocene
https://doi.org/10.1016/j.ocemod.2013.05.011 4: 000126. DOI: https://doi.org/10.12952/journal.
Yu, Q and Clausi, DA 2008 IRGS: image segmenta- elementa.000126
tion using edge penalties and region growing. Zhang, Q and Skjetne, R 2015 Image processing for identi-
IEEE Transactions on Pattern Analysis and Machine fication of sea-ice floe and the floe size distributions,
Intelligence 30(12): 2126–2139. DOI: https://doi. IEEE Trans Geosc Remote Sens 53(5): 2913–2924.
org/10.1109/TPAMI.2008.15 DOI: https://doi.org/10.1109/TGRS.2014.2366640
How to cite this article: Hwang, B, Ren, J, McCormack, S, Berry, C, Ayed, IB, Graber, HC and Aptoula, E 2017 A practical
algorithm for the retrieval of floe size distribution of Arctic sea ice from high-resolution satellite Synthetic Aperture Radar
imagery. Elem Sci Anth, 5: 38, DOI: https://doi.org/10.1525/elementa.154
Domain Editor-in-Chief: Jody W. Deming, University of Washington, WA, US
Guest Editor: Craig M. Lee, Applied Physics Laboratory, University of Washington, US
Knowledge Domain: Ocean Science
Part of an Elementa Special Feature: Marginal Ice Zone Processes in the Summertime Arctic
Submitted: 20 December 2016 Accepted: 20 June 2017 Published: 20 July 2017
Copyright: © 2017 The Author(s). This is an open-access article distributed under the terms of the Creative Commons
Attribution 4.0 International License (CC-BY 4.0), which permits unrestricted use, distribution, and reproduction in any medium,
provided the original author and source are credited. See http://creativecommons.org/licenses/by/4.0/.
Elem Sci Anth is a peer-reviewed open access
OPEN ACCESS
journal published by University of California Press.
Downloaded
from
http://online.ucpress.edu/elementa/article-pdf/doi/10.1525/elementa.154/473140/154-3386-2-pb.pdf
by
guest
on
28
May
2026
