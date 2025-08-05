postfix_ubuntu_packages = [
    "postfix",
    "mailutils",
    "libsasl2-2",
    "ca-certificates",
    "libsasl2-modules",
]


def test_postfix_package_installed(host):
    match host.system_info.distribution:
        case "ubuntu":
            for pkg_name in postfix_ubuntu_packages:
                pkg = host.package(pkg_name)
                assert pkg.is_installed


def test_postfix_service_running_and_enabled(host):
    docker_service = host.service("postfix")
    assert docker_service.is_running
    assert docker_service.is_enabled
