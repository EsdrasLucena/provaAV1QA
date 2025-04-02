import unittest

from provaAV1QA.validacao_cpf.app.validacao import validar_cpf


class testValidacaoCpf(unittest.TestCase):

    def testCpfValido(self):
        self.assertTrue(validar_cpf("701.117.554-76"))
        self.assertTrue(validar_cpf("12345678912"))
        self.assertTrue(validar_cpf("662.981.054-68"))

    def testCpfInvalido(self):
        self.assertFalse(validar_cpf("000.000.000-00"))  # Tstando com todos os numeros iguais
        self.assertFalse(validar_cpf("123.456.789-00"))  # Testando com os dígitos verificadores errados
        self.assertFalse(validar_cpf("54998624724"))  # Testando com o dígito final incorreto
        self.assertFalse(validar_cpf("746.935.130-21"))  # Testando com mais um dígito verificador incorreto

    def testCpfFormatacao(self):
        self.assertTrue(validar_cpf("70111755476"))  # Testando sem pontuação
        self.assertTrue(validar_cpf("701.117.554-76"))  # Testando com pontuação
        self.assertFalse(validar_cpf("701-117-554.76"))  # Testando com formato estranho
        self.assertFalse(validar_cpf("701.11t.5s4-2A"))  # Testando com o cpf contendo letra

    def testCpfTamanhoInvalido(self):
        self.assertFalse(validar_cpf("123456789"))  # Testando com cpf com menos de 11 dígitos
        self.assertFalse(validar_cpf("12345678901234"))  # Testando com cpf com mais de 11 dígitos

if __name__ == "__main__":
    unittest.main()


