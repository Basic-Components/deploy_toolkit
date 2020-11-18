import json
from fabric import task, Connection
import invoke
from termcolor import colored


@task(aliases=["创建swarm集群"])
def init_swarm(c: Connection) -> None:
    try:
        result = c.sudo('docker swarm init', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'white', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'white', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'white', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'white', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)


@task(aliases=["查看集群添加manager节点的token"])
def swarm_manager_token(c: Connection) -> None:
    try:
        result = c.sudo('docker swarm join-token manager', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'white', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'white', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'white', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'white', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)


@task(aliases=["查看集群添加worker节点的token"])
def swarm_worker_token(c: Connection) -> None:
    try:
        result = c.sudo('docker swarm join-token worker', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'white', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'white', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'white', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'white', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)


@task(aliases=["加入swarm集群"], help={"token": "加入集群的token", "manager": "集群的manager"})
def join_swarm(c: Connection, token: str, manager: str) -> None:
    try:
        result = c.sudo(f'docker swarm join --token {token} {manager}:2377', hide=True)
    except invoke.exceptions.UnexpectedExit as uee:
        print(colored(uee, 'white', 'on_red'))
        raise uee
    except invoke.exceptions.Failure as fe:
        print(colored(fe, 'white', 'on_cyan'))
        raise fe
    except invoke.exceptions.ThreadException as te:
        print(colored(te, 'white', 'on_cyan'))
        raise te
    except Exception as e:
        print(colored(str(e), 'white', 'on_yellow'))
        raise e
    else:
        msg = f"Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)
