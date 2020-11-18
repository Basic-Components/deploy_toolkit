import json
from fabric import task, Connection
import invoke
from termcolor import colored


@task(aliases=["安装docker"])
def install_docker(c: Connection) -> None:
    try:
        result = c.run('curl -fsSL https://get.docker.com -o get-docker.sh', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        result = c.sudo('sh get-docker.sh', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        result = c.sudo('systemctl enable docker', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        result = c.sudo('systemctl start docker', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        with c.cd("/etc/docker/"):
            result = c.sudo("touch daemon.json", hide=True)
            daemon = {"registry-mirrors": ["https://registry.docker-cn.com", "https://hub-mirror.c.163.com", "https://docker.mirrors.ustc.edu.cn/"], "insecure-registries": ["47.98.42.103:8333"]}
            daemon_str = json.dumps(daemon)
            result = c.sudo(f"""sh -c 'echo "{daemon_str}" >> daemon.json'""", hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        result = c.sudo('systemctl restart docker', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)


@task(aliases=["链接docker到其他位置"], help={"root_path": "指定链接到的位置根目录"})
def link_docker_to_otherplace(c: Connection, root_path="/data1") -> None:
    try:
        result = c.sudo('systemctl stop docker', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        with c.cd(root_path):
            result = c.sudo(f"mv /var/lib/docker {root_path}/docker", hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        result = c.sudo(f"ln -s {root_path}/docker /var/lib/docker", hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)

    try:
        result = c.sudo('systemctl restart docker', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'write', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'write', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'write', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'write', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)
