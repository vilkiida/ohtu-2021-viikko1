import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_vaaranlainen_tilavuus_korjaantuu_oikein(self):
        self.varasto2 = Varasto(-1)

        self.assertEqual(self.varasto2.tilavuus, 0.0)
    
    def test_vaaranlainen_saldo_korjaantuu_oikein(self):
        self.varasto3 = Varasto(10,-1)

        self.assertEqual(self.varasto3.saldo, 0.0)

    def test_alku_saldo_on_isompi_kuin_tilavuus(self):
        self.varasto4 = Varasto(10,20)

        self.assertEqual(self.varasto4.saldo,10)

    def test_varastoon_lisataan_maara_joka_on_alle_0(self):
        self.varasto.lisaa_varastoon(-1)
        
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_varastoon_lisataan_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(11)

        self.assertEqual(self.varasto.saldo, 10)
    
    def test_varastosta_otetaan_vahemman_kuin_0(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(self.varasto.ota_varastosta(-1), 0.0)
    
    def test_varastosta_otetaan_enemman_kuin_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        
        self.assertEqual(self.varasto.ota_varastosta(7), 5)
    
    def test_varastosta_otetaan_enemmän_kuin_saldoa_saldo_oikein(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(7)

        self.assertEqual(self.varasto.saldo, 0.0)
    
    def test_str_funktio_tulostaa_oikein(self):
        self.varasto.lisaa_varastoon(6)
        
        self.assertEqual(self.varasto.__str__(), "saldo = 6, vielä tilaa 4")