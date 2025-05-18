
docker_host_ubuntu_packages = ["docker-ce", "docker-ce-cli", "containerd.io", "docker-buildx-plugin", "docker-compose-plugin"]

def test_docker_package_installed(host):
    # Check if the Docker package is installed
    match host.system_info.distribution:
        case "ubuntu":
            # For Ubuntu, check for the docker.io package
            for pkg_name in docker_host_ubuntu_packages:
                pkg = host.package(pkg_name)
                assert pkg.is_installed

def test_docker_service_running_and_enabled(host):
    # Check if the Docker service is running and enabled
    docker_service = host.service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled

def test_user_in_docker_group(host):
    # Check if the current user is in the Docker group
    user = host.user("vagrant")  
    assert "docker" in user.groups

def test_docker_group_exists(host):
    # Check if the Docker group exists
    docker_group = host.group("docker")
    assert docker_group.exists

def test_docker_command_available(host):
    # Check if the `docker` command is available
    docker_cmd = host.run("docker --version")
    assert docker_cmd.rc == 0
    assert "Docker version" in docker_cmd.stdout
