"""Role testing files using testinfra."""


def test_dns_server(host):
    cmd = host.run("dig clickadu.com")
    assert cmd.rc == 0
    assert 'SERVER: 8.8.8.8' in cmd.stdout
