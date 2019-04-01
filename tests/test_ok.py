# -*- coding: utf-8 -*-


def test_oks(testdir):
    # create a temporary pytest test module
    testdir.makepyfile(
        """
        def test_sth():
            assert True
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest()

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["*OK*"])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
