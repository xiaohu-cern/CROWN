# all in pb
xs = {}

# for lep in ["E", "Mu", "Tau"]:
#     xs[f"DYto2{lep}_M_50_amcatnloFXFX"] = 2094.2

for lep in ["E", "Mu", "Tau"]:
    xs[f"Wto{lep}Nu"] = 9013.3 + 12128.4

xs["WtoLNu"] = (9013.3 + 12128.4)*3

xs["TTto2L2Nu"] = 923.6 * (1 - 0.6741) * (1 - 0.6741)
xs["TTto4Q"] = 923.6 * 0.6741 * 0.6741
xs["TTtoLNu2Q"] = 923.6 * 0.6741 * (1 - 0.6741) * 2

xs["WWto2L2Nu"] = 11.79
xs["WWtoLNu2Q"] = 15.87
xs["WWto4Q"] = 50.79

xs["WZto3LNu"] = 4.924
xs["WZto2L2Q"] = 7.568
xs["WZtoLNu2Q"] = 15.87

xs["ZZto2L2Nu"] = 1.031
xs["ZZto4L"] = 1.39
xs["ZZto2L2Q"] = 6.788
xs["ZZto2Nu2Q"] = 4.826

xs["TbarBtoLminusNuB-s"] = 4.534 * (1 - 0.6741)
xs["TBbartoLplusNuBbar-s"] = 7.244 * (1 - 0.6741)
xs["TbarBQtoLNu-t"] = 23.34
xs["TbarBQto2Q-t"] = 46.73
xs["TBbarQtoLNu-t"] = 38.6
xs["TBbarQto2Q-t"] = 77.26

xs["TWminusto2L2Nu"] = 87.9 * (0.4995) * (1 - 0.6741) * (1 - 0.6741)
xs["TbarWplusto2L2Nu"] = 87.9 * (0.5005) * (1 - 0.6741) * (1 - 0.6741)
xs["TWminustoLNu2Q"] = (87.9 * (0.4995) * (((1 - 0.6741) * (0.6741)) + ((0.6741) * (1 - 0.6741))))
xs["TbarWplustoLNu2Q"] = (87.9 * (0.5005) * (((1 - 0.6741) * (0.6741)) + ((0.6741) * (1 - 0.6741))))
xs["TWminusto4Q"] = 87.9 * (0.4995) * (0.6741) * (0.6741)
xs["TbarWplusto4Q"] = 87.9 * (0.5005) * (0.6741) * (0.6741)
