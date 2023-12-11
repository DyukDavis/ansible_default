"""Role testing files using testinfra."""


def test_snoopy_installed(host):
    assert host.package("snoopy").is_installed

def test_snoopy_log(host):
    log = host.file("/var/log/auth.log")
    assert log.contains("ogin:root ssh:((undefined)) sid:")
