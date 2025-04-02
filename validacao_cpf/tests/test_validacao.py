import unittest

from provaAV1QA.validacao_cpf.app.validacao import validar_cpf


class testValidacaoCpf(unittest.TestCase):

    def testCpfValido(self):
        self.assertTrue(validar_cpf("701.117.554-76"))
        self.assertTrue(validar_cpf("12345678912"))
        self.assertTrue(validar_cpf("662.981.054-68"))

    def testCpfInvalido(self):
        self.assertFalse(validar_cpf("000.000.000-00"))  # Todos iguais
        self.assertFalse(validar_cpf("123.456.789-00"))  # Dígitos verificadores errados
        self.assertFalse(validar_cpf("54998624724"))  # Dígito final incorreto
        self.assertFalse(validar_cpf("746.935.130-21"))  # Dígito verificador incorreto

    def testCpfFormatacao(self):
        self.assertTrue(validar_cpf("70111755476"))  # Sem pontuação
        self.assertTrue(validar_cpf("701.117.554-76"))  # Com pontuação
        self.assertFalse(validar_cpf("701-117-554.76"))  # Formato estranho
        self.assertFalse(validar_cpf("701.11t.5s4-2A"))  # Contém letra

    def testCpfTamanhoInvalido(self):
        self.assertFalse(validar_cpf("123456789"))  # Menos de 11 dígitos
        self.assertFalse(validar_cpf("12345678901234"))  # Mais de 11 dígitos

if __name__ == "__main__":
    unittest.main()


