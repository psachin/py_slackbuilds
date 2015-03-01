#!/usr/bin/env python

import unittest
from slackbuilds import download_tarball

class TestSlackbuilds(unittest.TestCase):
    '''Test case for slackbuilds.py'''
    def test_if_tarball_is_downloadable(self):
        url = "http://slackbuilds.org/repository/14.1/libraries/yajl/?search=yajl"
        list = [u'http://github.com/lloyd/yajl/tarball/2.1.0/lloyd-yajl-2.1.0-0-ga0ecdde.tar.gz',
                u'http://slackbuilds.org/slackbuilds/14.1/libraries/yajl.tar.gz']
        self.assertEqual(download_tarball(url), list)


if __name__ == '__main__':
    unittest.main()
