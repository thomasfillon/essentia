#!/usr/bin/env python

# Copyright (C) 2006-2016  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License
# version 3 along with this program. If not, see http://www.gnu.org/licenses/



from essentia_test import *


class TestSpectrumToCent(TestCase):
    def testRegression(self):
        """ Simple regression test, comparing normal behaviour. Here we check that the method behaves the same as directly calling 
        TriangularBands with known bands. """
        audio = MonoLoader(filename = join(testdata.audio_dir, 'generated/synthesised/sin440_sweep_0db.wav'),
                           sampleRate = 44100)()

        fft = Spectrum()
        frameSize_default = 4410
        zeroPadding_default = 65536 - frameSize_default
        window = Windowing(type = 'hamming', zeroPadding = zeroPadding_default)
        frequencyBands_default = [163.86474121, 164.814, 165.76875779, 166.72904643, 167.69489797, 168.66634464, 169.64341883, 170.62615316, 171.61458041, 172.60873356, 173.60864578, 174.61435043, 175.62588108, 176.64327145, 177.66655552, 178.6957674, 179.73094145, 180.7721122, 181.8193144, 182.87258297, 183.93195307, 184.99746003, 186.06913941, 187.14702697, 188.23115867, 189.32157068, 190.41829938, 191.52138137, 192.63085344, 193.74675263, 194.86911615, 195.99798145, 197.13338621, 198.2753683, 199.42396582, 200.5792171, 201.74116069, 202.90983534, 204.08528006, 205.26753406, 206.45663679, 207.65262792, 208.85554735, 210.06543523, 211.28233192, 212.50627802, 213.73731436, 214.97548203, 216.22082232, 217.47337681, 218.73318726, 220.00029573, 221.27474447, 222.55657603, 223.84583316, 225.14255888, 226.44679645, 227.7585894, 229.07798149, 230.40501673, 231.73973942, 233.08219407, 234.43242548, 235.79047871, 237.15639906, 238.5302321, 239.91202368, 241.30181989, 242.69966711, 244.10561198, 245.51970141, 246.94198257, 248.37250292, 249.81131019, 251.25845239, 252.7139778, 254.17793498, 255.65037278, 257.13134032, 258.62088702, 260.11906258, 261.62591698, 263.1415005, 264.6658637, 266.19905745, 267.74113291, 269.29214151, 270.85213502, 272.42116547, 273.99928523, 275.58654694, 277.18300357, 278.78870837, 280.40371493, 282.02807713, 283.66184916, 285.30508553, 286.95784108, 288.62017094, 290.29213058, 291.97377579, 293.66516266, 295.36634764, 297.07738749, 298.79833929, 300.52926046, 302.27020875, 304.02124226, 305.7824194, 307.55379893, 309.33543997, 311.12740194, 312.92974464, 314.74252821, 316.56581313, 318.39966023, 320.2441307, 322.09928608, 323.96518826, 325.8418995, 327.72948242, 329.628, 331.53751558, 333.45809287, 335.38979595, 337.33268927, 339.28683766, 341.25230632, 343.22916082, 345.21746712, 347.21729156, 349.22870087, 351.25176215, 353.28654291, 355.33311103, 357.3915348, 359.4618829, 361.54422441, 363.63862879, 365.74516594, 367.86390613, 369.99492006, 372.13827883, 374.29405395, 376.46231734, 378.64314136, 380.83659876, 383.04276274, 385.26170689, 387.49350525, 389.73823229, 391.9959629, 394.26677242, 396.55073659, 398.84793164, 401.1584342, 403.48232137, 405.81967068, 408.17056012, 410.53506812, 412.91327357, 415.30525583, 417.71109471, 420.13087046, 422.56466384, 425.01255603, 427.47462872, 429.95096405, 432.44164465, 434.94675361, 437.46637452, 440.00059145, 442.54948895, 445.11315206, 447.69166631, 450.28511775, 452.8935929, 455.5171788, 458.15596297, 460.81003346, 463.47947883, 466.16438814, 468.86485097, 471.58095742, 474.31279811, 477.0604642, 479.82404735, 482.60363978, 485.39933423, 488.21122397, 491.03940281, 493.88396514, 496.74500584, 499.62262039, 502.51690478, 505.4279556, 508.35586996, 511.30074555, 514.26268064, 517.24177404, 520.23812516, 523.25183396, 526.283001, 529.33172741, 532.39811491, 535.48226581, 538.58428302, 541.70427003, 544.84233095, 547.99857046, 551.17309388, 554.36600713, 557.57741674, 560.80742986, 564.05615425, 567.32369831, 570.61017106, 573.91568216, 577.24034188, 580.58426116, 583.94755157, 587.33032533, 590.73269529, 594.15477498, 597.59667858, 601.05852092, 604.54041751, 608.04248452, 611.5648388, 615.10759787, 618.67087993, 622.25480388, 625.85948929, 629.48505643, 633.13162626, 636.79932046, 640.4882614, 644.19857215, 647.93037651, 651.683799, 655.45896484, 659.256, 663.07503116, 666.91618574, 670.7795919, 674.66537854, 678.57367532, 682.50461263, 686.45832163, 690.43493423, 694.43458312, 698.45740173, 702.5035243, 706.57308582, 710.66622206, 714.78306961, 718.92376581, 723.08844881, 727.27725758, 731.49033188, 735.72781226, 739.98984012, 744.27655765, 748.58810789, 752.92463468, 757.28628272, 761.67319753, 766.08552548, 770.52341378, 774.9870105, 779.47646459, 783.99192581, 788.53354483, 793.10147319, 797.69586328, 802.31686841, 806.96464274, 811.63934136, 816.34112024, 821.07013624, 825.82654715, 830.61051167, 835.42218941, 840.26174092, 845.12932767, 850.02511206, 854.94925744, 859.90192811, 864.8832893, 869.89350722, 874.93274905, 880.0011829, 885.09897789, 890.22630411, 895.38333263, 900.57023551, 905.78718581, 911.0343576, 916.31192594, 921.62006693, 926.95895766, 932.32877628, 937.72970193, 943.16191483, 948.62559622, 954.1209284, 959.64809471, 965.20727957, 970.79866846, 976.42244793, 982.07880563, 987.76793027, 993.49001168, 999.24524077, 1005.03380956, 1010.85591119, 1016.71173992, 1022.60149111, 1028.52536128, 1034.48354809, 1040.47625032, 1046.50366792, 1052.56600199, 1058.66345481, 1064.79622982, 1070.96453162, 1077.16856604, 1083.40854007, 1089.68466189, 1095.99714092, 1102.34618777, 1108.73201427, 1115.15483349, 1121.61485972, 1128.1123085, 1134.64739662, 1141.22034213, 1147.83136431, 1154.48068376, 1161.16852233, 1167.89510315, 1174.66065065, 1181.46539058, 1188.30954996, 1195.19335715, 1202.11704183, 1209.08083501, 1216.08496904, 1223.1296776, 1230.21519574, 1237.34175987, 1244.50960776, 1251.71897858, 1258.97011286, 1266.26325253, 1273.59864092, 1280.97652279, 1288.3971443, 1295.86075303, 1303.367598, 1310.91792969, 1318.512, 1326.15006231, 1333.83237147, 1341.55918379, 1349.33075708, 1357.14735064, 1365.00922526, 1372.91664326, 1380.86986847, 1388.86916624, 1396.91480347, 1405.0070486, 1413.14617164, 1421.33244413, 1429.56613921, 1437.84753161, 1446.17689763, 1454.55451517, 1462.98066376, 1471.45562452, 1479.97968024, 1488.55311531, 1497.17621578, 1505.84926937, 1514.57256544, 1523.34639506, 1532.17105095, 1541.04682755, 1549.97402101, 1558.95292917, 1567.98385162, 1577.06708966, 1586.20294637, 1595.39172656, 1604.63373682, 1613.92928549, 1623.27868273, 1632.68224047, 1642.14027248, 1651.6530943, 1661.22102334, 1670.84437883, 1680.52348185, 1690.25865534, 1700.05022412, 1709.89851488, 1719.80385621, 1729.7665786, 1739.78701445, 1749.86549809, 1760.0023658, 1770.19795579, 1780.45260822, 1790.76666526, 1801.14047101, 1811.57437162, 1822.06871519, 1832.62385188, 1843.24013385, 1853.91791532, 1864.65755255, 1875.45940387, 1886.32382967, 1897.25119245, 1908.2418568, 1919.29618942, 1930.41455913, 1941.59733691, 1952.84489586, 1964.15761126, 1975.53586055, 1986.98002336, 1998.49048154, 2010.06761913, 2021.71182239, 2033.42347983, 2045.20298221, 2057.05072256, 2068.96709617, 2080.95250063, 2093.00733583, 2105.13200398, 2117.32690962, 2129.59245963, 2141.92906325, 2154.33713208, 2166.81708013, 2179.36932378, 2191.99428184, 2204.69237553, 2217.46402854, 2230.30966698, 2243.22971944, 2256.22461701, 2269.29479325, 2282.44068425, 2295.66272863, 2308.96136752, 2322.33704465, 2335.79020629, 2349.32130131, 2362.93078115, 2376.61909992, 2390.3867143, 2404.23408367, 2418.16167003, 2432.16993807, 2446.25935519, 2460.43039147, 2474.68351973, 2489.01921553, 2503.43795716, 2517.94022571, 2532.52650505, 2547.19728185, 2561.95304559, 2576.7942886, 2591.72150606, 2606.73519601, 2621.83585938, 2637.024, 2652.30012463, 2667.66474294, 2683.11836759, 2698.66151417, 2714.29470128, 2730.01845053, 2745.83328653, 2761.73973694, 2777.73833248, 2793.82960694, 2810.01409721, 2826.29234327, 2842.66488826, 2859.13227843, 2875.69506322, 2892.35379525, 2909.10903034, 2925.96132751, 2942.91124905, 2959.95936048, 2977.10623062, 2994.35243157, 3011.69853874, 3029.14513089, 3046.69279012, 3064.3421019, 3082.09365511, 3099.94804202, 3117.90585834, 3135.96770323, 3154.13417933, 3172.40589275, 3190.78345313, 3209.26747363, 3227.85857098, 3246.55736546, 3265.36448095, 3284.28054495, 3303.3061886, 3322.44204668, 3341.68875766, 3361.0469637, 3380.51731068, 3400.10044824, 3419.79702976, 3439.60771242, 3459.5331572, 3479.5740289, 3499.73099619, 3520.0047316, 3540.39591157, 3560.90521644, 3581.53333051, 3602.28094203, 3623.14874323, 3644.13743038, 3665.24770376, 3686.48026771, 3707.83583065, 3729.3151051, 3750.91880773, 3772.64765933, 3794.50238489, 3816.48371359, 3838.59237883, 3860.82911827, 3883.19467382, 3905.68979172, 3928.31522251, 3951.07172109, 3973.96004673, 3996.98096309, 4020.13523825, 4043.42364477, 4066.84695966, 4090.40596443, 4114.10144513, 4137.93419234, 4161.90500126, 4186.01467167, 4210.26400797, 4234.65381925, 4259.18491926, 4283.8581265, 4308.67426417, 4333.63416026, 4358.73864756, 4383.98856368, 4409.38475107, 4434.92805708, 4460.61933395, 4486.45943888, 4512.44923401, 4538.5895865, 4564.8813685, 4591.32545725, 4617.92273505, 4644.67408931, 4671.58041259, 4698.64260261, 4725.86156231, 4753.23819983, 4780.7734286, 4808.46816734, 4836.32334006, 4864.33987615, 4892.51871039, 4920.86078295, 4949.36703947, 4978.03843105, 5006.87591431, 5035.88045142, 5065.0530101, 5094.39456369, 5123.90609118, 5153.5885772, 5183.44301212, 5213.47039201, 5243.67171875, 5274.048, 5304.60024925, 5335.32948589, 5366.23673517, 5397.32302834, 5428.58940257, 5460.03690106, 5491.66657305, 5523.47947387, 5555.47666496, 5587.65921388, 5620.02819441, 5652.58468654, 5685.32977651, 5718.26455686, 5751.39012645, 5784.70759051, 5818.21806068, 5851.92265502, 5885.82249809, 5919.91872096, 5954.21246124, 5988.70486313, 6023.39707748, 6058.29026178, 6093.38558023, 6128.6842038, 6164.18731022, 6199.89608404, 6235.81171668, 6271.93540647, 6308.26835866, 6344.8117855, 6381.56690626, 6418.53494727, 6455.71714196, 6493.11473091, 6530.7289619, 6568.5610899, 6606.6123772, 6644.88409336, 6683.37751531, 6722.09392739, 6761.03462137, 6800.20089649, 6839.59405953, 6879.21542484, 6919.06631439, 6959.1480578, 6999.46199238, 7040.00946321, 7080.79182314, 7121.81043289, 7163.06666102, 7204.56188406, 7246.29748647, 7288.27486077, 7330.49540752, 7372.96053542, 7415.67166129, 7458.63021021, 7501.83761546, 7545.29531867, 7589.00476979, 7632.96742718, 7677.18475766, 7721.65823653, 7766.38934764, 7811.37958344, 7856.63044503, 7902.14344219, 7947.92009346, 7993.96192617, 8040.27047651, 8086.84728955, 8133.69391932, 8180.81192886, 8228.20289025, 8275.86838469, 8323.81000253, 8372.02934333, 8420.52801594, 8469.30763849, 8518.36983853, 8567.716253, 8617.34852834, 8667.26832052, 8717.47729512, 8767.97712735, 8818.76950214, 8869.85611415, 8921.2386679, 8972.91887776, 9024.89846802, 9077.17917299, 9129.762737, 9182.6509145, 9235.8454701, 9289.34817862, 9343.16082517, 9397.28520522, 9451.72312461, 9506.47639966, 9561.54685721, 9616.93633467, 9672.64668011, 9728.6797523, 9785.03742077, 9841.7215659, 9898.73407893, 9956.0768621, 10013.75182863, 10071.76090284, 10130.1060202, 10188.78912739, 10247.81218235, 10307.1771544, 10366.88602423, 10426.94078403, 10487.34343751, 10548.096]
        truthTriangles = TriangularBands(inputSize = 61126,
                                         frequencyBands = frequencyBands_default, 
                                         log = False, 
                                         sampleRate = 44100)
        centTriangles = SpectrumToCent(inputSize = 61126,
                                       minimumFrequency = 164.814, 
                                       bands = 720,
                                       log = False, 
                                       sampleRate = 44100)

        for frame in FrameGenerator(audio, frameSize = 2048, hopSize = 512):
            truthBands = truthTriangles(fft(window(frame)))
            centBands, centFreqs = centTriangles(fft(window(frame)))
            self.assert_(not any(numpy.isnan(centBands)))
            self.assert_(not any(numpy.isinf(centBands)))
            self.assert_(all(centBands >= 0.0))
            self.assertAlmostEqualVector(centBands, truthBands, 1.0e-3)
        print centFreqs



    def testZero(self):
        speaks = SpectralPeaks()
        (freqs, mags) = speaks(numpy.zeros(1024, dtype='f4'))
        self.assert_(len(freqs) == 0)
        self.assert_(len(mags) == 0)



    def testEmpty(self):
        # Feeding an empty array shouldn't crash and throw an exception
        self.assertComputeFails(SpectrumToCent(), [])



    def testOne(self):
        # Feeding an array of size 1 shouldn't crash and throw an exception
        self.assertComputeFails(SpectrumToCent(), [0])



    def testInvalidParam(self):
        self.assertConfigureFails(SpectrumToCent(), {'sampleRate': 0})
        self.assertConfigureFails(SpectrumToCent(), {'minimumFrequency': 0})
        self.assertConfigureFails(SpectrumToCent(), {'centBinResolution': 0})
        self.assertConfigureFails(SpectrumToCent(), {'bands': 0})
        #Test that SpectrumToCent throws an exception when asking for bands above the Nyquist frequency.
        self.assertConfigureFails(SpectrumToCent(), { 'bands': 2000 })

    def testInsufficientResolution(self):
        self.assertRaises(EssentiaException, lambda: SpectrumToCent(sampleRate = 44100)([0] * 513))

suite = allTests(TestSpectrumToCent)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
