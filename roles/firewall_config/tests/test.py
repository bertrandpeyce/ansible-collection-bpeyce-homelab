def test_package_installed(host):
    # Check if the Docker package is installed
    match host.system_info.distribution:
        case "ubuntu":
            # For Ubuntu, check for the docker.io package
            for pkg_name in ["ufw"]:
                pkg = host.package(pkg_name)
                assert pkg.is_installed


def test_service_running_and_enabled(host):
    # Check if the Docker service is running and enabled
    ufw_service = host.service("ufw")
    assert ufw_service.is_running
    assert ufw_service.is_enabled


def test_ufw_enabled(host):
    # Check if the Docker service is running and enabled
    ufw_status_cmd = host.run("ufw status verbose")
    assert ufw_status_cmd.rc == 0
    assert "Status: active" in ufw_status_cmd.stdout
    assert "Logging: on" in ufw_status_cmd.stdout
    assert "Default: deny (incoming), deny (outgoing)" in ufw_status_cmd.stdout
