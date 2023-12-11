import pytest


@pytest.mark.parametrize("param,value", [
    ("fs.nr_open",1048576600),
    ("net.ipv4.tcp_congestion_control","bbr"),
])
def test_parameters_set(host, param, value):
    assert host.sysctl(param) == value
