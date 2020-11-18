import json
from fabric import task, Connection
import invoke
from termcolor import colored


@task(aliases=["安装docker-compose"],
      help={"mirror": "是否使用国内镜像",
            "raspbian": "是否是给raspbian系统安装"})
def install_dockercompose(c: Connection, mirror=True, raspbian=False) -> None:
    if raspbian:
        try:
            result = c.sudo('apt install -y libffi-dev', hide=True)
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

        try:
            result = c.sudo('pip install docker-compose', hide=True)
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

    else:
        try:
            host = "github.com"
            if mirror:
                host = "get.daocloud.io"
            result = c.sudo(f'curl -L "https://{host}/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose', hide=True)
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

        try:
            result = c.sudo('chmod +x /usr/local/bin/docker-compose', hide=True)
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

        try:
            result = c.sudo('ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose', hide=True)
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

    try:
        result = c.sudo('docker-compose --version', hide=True)
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
