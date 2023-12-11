"""Role testing files using testinfra."""


def test_ssacli_run(host):
    cmd = host.run('ssacli version')
    assert cmd.rc == 0
