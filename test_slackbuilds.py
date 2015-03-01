#!/usr/bin/env python

import os
import unittest
from slackbuilds import prepare_tarball_list, download_slackbuild_src
from slackbuilds import download_package_src_64bit


class TestSlackbuilds(unittest.TestCase):
    '''Test case for slackbuilds.py'''
    def test_pkg_yajl(self):
        url = "http://slackbuilds.org/repository/14.1/libraries/yajl/?search=yajl"
        list = [u'http://github.com/lloyd/yajl/tarball/2.1.0/lloyd-yajl-2.1.0-0-ga0ecdde.tar.gz',
                u'http://slackbuilds.org/slackbuilds/14.1/libraries/yajl.tar.gz']
        self.assertEqual(prepare_tarball_list(url), list)

    def test_pkg_ghc(self):
        url = "http://slackbuilds.org/repository/14.1/haskell/ghc/"
        list = [u'http://www.haskell.org/ghc/dist/7.6.2/ghc-7.6.2-i386-unknown-linux.tar.bz2',
                u'http://www.haskell.org/ghc/dist/7.6.2/ghc-7.6.2-x86_64-unknown-linux.tar.bz2',
                u'http://slackbuilds.org/slackbuilds/14.1/haskell/ghc.tar.gz']
        self.assertEqual(prepare_tarball_list(url), list)

    def test_if_pkg_src_is_downloaded(self):
        url = "http://slackbuilds.org/repository/14.1/haskell/ghc/"
        prepare_tarball_list(url)
        download_slackbuild_src()
        self.assertTrue(os.path.exists('ghc.tar.gz'))

    def _download_machine_specific_packages(self):
        url = "http://slackbuilds.org/repository/14.1/haskell/ghc/"
        prepare_tarball_list(url)
        download_package_src_64bit()
        self.assertTrue(os.path.exists('ghc-7.6.2-x86_64-unknown-linux.tar.gz'))

if __name__ == '__main__':
    unittest.main()
