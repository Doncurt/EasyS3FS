'''Tests for the S3FS module including tests for login'''

import unittest
from EasyS3FS import EasyS3FS


class testLogin(unittest.TestCase):
    '''Test the login function'''
    def testLoginType(self):
        key1='AKIAI3PPE3FGQRFVYACA'
        secret1='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'
        test1=EasyS3FS(key1,secret1)
        self.assertEqual(type(test1),EasyS3FS)



unittest.main()
