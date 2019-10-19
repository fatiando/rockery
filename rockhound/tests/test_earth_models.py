"""
Test the PREM loading function.
"""
import numpy.testing as npt

from ..earth_models import fetch_prem
from ..earth_models import fetch_ak135f
from ..earth_models import fetch_iasp91
from ..earth_models import fetch_mean
from ..earth_models import fetch_pema
from ..earth_models import fetch_pemc
from ..earth_models import fetch_pemo
from ..earth_models import fetch_mc35
from ..earth_models import fetch_stw105
from ..earth_models import fetch_tna_sna


def test_prem_file_name_only():
    "Only fetch the file name."
    fname = fetch_prem(load=False)
    assert fname.endswith("PREM_1s.csv")


def test_prem():
    "Sanity checks for the prem DataFrame"
    prem = fetch_prem()
    assert prem.shape == (199, 10)
    npt.assert_allclose(prem["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(prem["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(prem["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(prem["depth"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(prem["density"].min(), 1.02, rtol=1e-06)
    npt.assert_allclose(prem["density"].max(), 13.0885, rtol=1e-06)
    npt.assert_allclose(prem["Vpv"].min(), 1.45, rtol=1e-06)
    npt.assert_allclose(prem["Vpv"].max(), 13.71662, rtol=1e-06)
    npt.assert_allclose(prem["Vph"].min(), 1.45, rtol=1e-06)
    npt.assert_allclose(prem["Vph"].max(), 13.71662, rtol=1e-06)
    npt.assert_allclose(prem["Vsv"].min(), 0, rtol=1e-06)
    npt.assert_allclose(prem["Vsv"].max(), 7.26597, rtol=1e-06)
    npt.assert_allclose(prem["Vsh"].min(), 0, rtol=1e-06)
    npt.assert_allclose(prem["Vsh"].max(), 7.26597, rtol=1e-06)
    npt.assert_allclose(prem["eta"].min(), 0.90039, rtol=1e-06)
    npt.assert_allclose(prem["eta"].max(), 1, rtol=1e-06)
    npt.assert_allclose(prem["Q_mu"].min(), 0, rtol=1e-06)
    npt.assert_allclose(prem["Q_mu"].max(), 600, rtol=1e-06)
    npt.assert_allclose(prem["Q_kappa"].min(), 1327.7, rtol=1e-06)
    npt.assert_allclose(prem["Q_kappa"].max(), 57823, rtol=1e-06)


def test_ak135f_file_name_only():
    "Only fetch the file name."
    fname = fetch_ak135f(load=False)
    assert fname.endswith("AK135F_AVG_IDV.csv")


def test_ak135f():
    "Sanity checks for the ak135f DataFrame"
    ak135f = fetch_ak135f()
    assert ak135f.shape == (145, 6)
    npt.assert_allclose(ak135f["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(ak135f["depth"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(ak135f["density"].min(), 1.02, rtol=1e-06)
    npt.assert_allclose(ak135f["density"].max(), 13.0122, rtol=1e-06)
    npt.assert_allclose(ak135f["Vp"].min(), 1.45, rtol=1e-06)
    npt.assert_allclose(ak135f["Vp"].max(), 13.6601, rtol=1e-06)
    npt.assert_allclose(ak135f["Vs"].max(), 7.2817, rtol=1e-06)
    npt.assert_allclose(ak135f["Vs"].min(), 0, rtol=1e-06)
    npt.assert_allclose(ak135f["Q_mu"].min(), 0, rtol=1e-06)
    npt.assert_allclose(ak135f["Q_mu"].max(), 599.99, rtol=1e-06)
    npt.assert_allclose(ak135f["Q_kappa"].min(), 163.35, rtol=1e-06)
    npt.assert_allclose(ak135f["Q_kappa"].max(), 57822, rtol=1e-06)


def test_iasp91_file_name_only():
    "Only fetch the file name."
    fname = fetch_iasp91(load=False)
    assert fname.endswith("IASP91.csv")


def test_iasp91():
    "Sanity checks for the iasp91 DataFrame"
    iasp91 = fetch_iasp91()
    assert iasp91.shape == (152, 4)
    npt.assert_allclose(iasp91["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(iasp91["depth"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(iasp91["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(iasp91["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(iasp91["Vp"].min(), 5.8, rtol=1e-06)
    npt.assert_allclose(iasp91["Vp"].max(), 13.6908, rtol=1e-06)
    npt.assert_allclose(iasp91["Vs"].min(), 0, rtol=1e-06)
    npt.assert_allclose(iasp91["Vs"].max(), 7.3015, rtol=1e-06)


def test_mean_file_name_only():
    "Only fetch the file name."
    fname = fetch_mean(load=False)
    assert fname.endswith("MEAN.nc")


def test_mean():
    "Sanity checks for the mean DataFrame"
    mean = fetch_mean()
    assert mean.shape == (180, 6)
    npt.assert_allclose(mean["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(mean["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(mean["density"].min(), 2.72, rtol=1e-06)
    npt.assert_allclose(mean["density"].max(), 13.0122, rtol=1e-06)
    npt.assert_allclose(mean["Vp"].min(), 5.8, rtol=1e-06)
    npt.assert_allclose(mean["Vp"].max(), 13.6908, rtol=1e-06)
    npt.assert_allclose(mean["Vs"].min(), 0, rtol=1e-06)
    npt.assert_allclose(mean["Vs"].max(), 7.3015, rtol=1e-06)
    npt.assert_allclose(mean["Q_kappa"].min(), 99999, rtol=1e-06)
    npt.assert_allclose(mean["Q_kappa"].max(), 99999, rtol=1e-06)
    npt.assert_allclose(mean["Q_mu"].min(), 0, rtol=1e-06)
    npt.assert_allclose(mean["Q_mu"].max(), 312, rtol=1e-06)


def test_pema_file_name_only():
    "Only fetch the file name."
    fname = fetch_pema(load=False)
    assert fname.endswith("PEMA.csv")


def test_pema():
    "Sanity checks for the pema DataFrame"
    pema = fetch_pema()
    assert pema.shape == (191, 5)
    npt.assert_allclose(pema["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pema["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(pema["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pema["depth"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(pema["density"].min(), 1.03, rtol=1e-06)
    npt.assert_allclose(pema["density"].max(), 13.012, rtol=1e-06)
    npt.assert_allclose(pema["Vp"].min(), 1.5, rtol=1e-06)
    npt.assert_allclose(pema["Vp"].max(), 13.732, rtol=1e-06)
    npt.assert_allclose(pema["Vs"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pema["Vs"].max(), 7.243, rtol=1e-06)


def test_pemc_file_name_only():
    "Only fetch the file name."
    fname = fetch_pemc(load=False)
    assert fname.endswith("PEMC.csv")


def test_pemc():
    "Sanity checks for the pemc DataFrame"
    pemc = fetch_pemc()
    assert pemc.shape == (190, 5)
    npt.assert_allclose(pemc["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pemc["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(pemc["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pemc["depth"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(pemc["density"].min(), 2.72, rtol=1e-06)
    npt.assert_allclose(pemc["density"].max(), 13.012, rtol=1e-06)
    npt.assert_allclose(pemc["Vp"].min(), 5.8, rtol=1e-06)
    npt.assert_allclose(pemc["Vp"].max(), 13.732, rtol=1e-06)
    npt.assert_allclose(pemc["Vs"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pemc["Vs"].max(), 7.243, rtol=1e-06)


def test_pemo_file_name_only():
    "Only fetch the file name."
    fname = fetch_pemo(load=False)
    assert fname.endswith("PEMO.csv")


def test_pemo():
    "Sanity checks for the pemo DataFrame"
    pemo = fetch_pemo()
    assert pemo.shape == (191, 5)
    npt.assert_allclose(pemo["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pemo["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(pemo["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pemo["depth"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(pemo["density"].min(), 1.03, rtol=1e-06)
    npt.assert_allclose(pemo["density"].max(), 13.012, rtol=1e-06)
    npt.assert_allclose(pemo["Vp"].min(), 1.5, rtol=1e-06)
    npt.assert_allclose(pemo["Vp"].max(), 13.732, rtol=1e-06)
    npt.assert_allclose(pemo["Vs"].min(), 0, rtol=1e-06)
    npt.assert_allclose(pemo["Vs"].max(), 7.243, rtol=1e-06)


def test_mc35_file_name_only():
    "Only fetch the file name."
    fname = fetch_mc35(load=False)
    assert fname.endswith("MC35.csv")


def test_mc35():
    "Sanity checks for the mc35 DataFrame"
    mc35 = fetch_mc35()
    assert mc35.shape == (151, 2)
    npt.assert_allclose(mc35["depth"].min(), 0, rtol=1e-06)
    npt.assert_allclose(mc35["depth"].max(), 2885.3, rtol=1e-06)
    npt.assert_allclose(mc35["Vs"].min(), 3, rtol=1e-06)
    npt.assert_allclose(mc35["Vs"].max(), 7.24338, rtol=1e-06)


def test_stw105_file_name_only():
    "Only fetch the file name."
    fname = fetch_stw105(load=False)
    assert fname.endswith("STW105.txt")


def test_stw105():
    "Sanity checks for the stw105 DataFrame"
    stw105 = fetch_stw105()
    assert stw105.shape == (750, 9)
    npt.assert_allclose(stw105["radius"].min(), 0, rtol=1e-06)
    npt.assert_allclose(stw105["radius"].max(), 6.371e06, rtol=1e-06)
    npt.assert_allclose(stw105["density"].min(), 1020, rtol=1e-06)
    npt.assert_allclose(stw105["density"].max(), 13088.48, rtol=1e-06)
    npt.assert_allclose(stw105["Vpv"].min(), 1450, rtol=1e-06)
    npt.assert_allclose(stw105["Vpv"].max(), 13716.6, rtol=1e-06)
    npt.assert_allclose(stw105["Vph"].min(), 1450, rtol=1e-06)
    npt.assert_allclose(stw105["Vph"].max(), 13716.6, rtol=1e-06)
    npt.assert_allclose(stw105["Vsv"].min(), 0, rtol=1e-06)
    npt.assert_allclose(stw105["Vsv"].max(), 7265.97, rtol=1e-06)
    npt.assert_allclose(stw105["Vsh"].min(), 0, rtol=1e-06)
    npt.assert_allclose(stw105["Vsh"].max(), 7265.97, rtol=1e-06)
    npt.assert_allclose(stw105["eta"].min(), 0.91129, rtol=1e-06)
    npt.assert_allclose(stw105["eta"].max(), 1, rtol=1e-06)
    npt.assert_allclose(stw105["Q_mu"].min(), 0, rtol=1e-06)
    npt.assert_allclose(stw105["Q_mu"].max(), 355, rtol=1e-06)
    npt.assert_allclose(stw105["Q_kappa"].min(), 943, rtol=1e-06)
    npt.assert_allclose(stw105["Q_kappa"].max(), 57822.5, rtol=1e-06)


def test_tna_sna_file_name_only():
    "Only fetch the file name."
    fname = fetch_tna_sna(load=False)
    assert fname.endswith("StartingVsModel_TNA-SNA-average_IDV.csv")


def test_tna_sna():
    "Sanity checks for the tna_sna DataFrame"
    tna_sna = fetch_tna_sna()
    assert tna_sna.shape == (221, 2)
    npt.assert_allclose(tna_sna["radius"].min(), 3480, rtol=1e-06)
    npt.assert_allclose(tna_sna["radius"].max(), 6371.0, rtol=1e-06)
    npt.assert_allclose(tna_sna["Vs"].min(), 3.2, rtol=1e-06)
    npt.assert_allclose(tna_sna["Vs"].max(), 7.29, rtol=1e-06)
