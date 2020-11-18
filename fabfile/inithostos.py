import json
from fabric import task, Connection
import invoke
from termcolor import colored


@task(aliases=["raspbian的更新包管理器"])
def apt_update(c: Connection) -> None:
    """更新包管理器."""
    try:
        result = c.sudo("""sudo apt update -y""", hide=True)
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


@task(aliases=["重启机器"])
def reboot(c: Connection) -> None:
    try:
        result = c.sudo("""sudo reboot""", hide=True)
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


@task(aliases=["更新内核"])
def apt_upgrade(c: Connection) -> None:
    """更新内核并重启"""
    apt_update(c)
    try:
        result = c.sudo("""sudo apt upgrade -y""", hide=True)
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
    reboot(c)


@task(aliases=["raspbian的apt换源"])
def raspbian_apt_change_mirror(c: Connection) -> None:
    """换源后更新包和内核然后重启."""
    try:
        result = c.sudo("""sh -c 'echo "deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi" > /etc/apt/sources.list'""", hide=True)
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
        result = c.sudo("""sh -c 'echo "deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui" > /etc/apt/sources.list.d/raspi.list'""", hide=True)
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
    apt_upgrade(c)


@task(aliases=["安装包"])
def install_package(c: Connection, package: str) -> None:
    """安装nano和vim并设置美化vim."""
    try:
        result = c.sudo(f"apt-get install -y {package}", hide=True)
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


@task(aliases=["安装zsh"])
def install_zsh(c: Connection) -> None:
    """安装zsh并安装oh-my-zsh."""
    install_package(c, package="zsh")
    try:
        result = c.sudo("wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh", hide=True)
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
    reboot(c)


@task(aliases=["安装编辑器"])
def install_editor(c: Connection) -> None:
    """安装nano和vim并设置美化vim."""
    install_package(c, package="nano")
    install_package(c, package="vim")
    try:
        result = c.sudo("update-alternatives --display vi", hide=True)
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
        result = c.put(local="vimrc", remote=".vimrc")
    except Exception as e:
        print(colored(str(e), 'white', 'on_yellow'))
        raise e
    else:
        msg = f"put file on {result.connection.host}, got stdout:\n{result.stdout}"
        print(msg)


@task(aliases=["状态"])
def check_status(c: Connection) -> None:
    # 检查硬盘使用状态
    try:
        result = c.sudo("df -h", hide=True)
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
    # 检查内存使用状态
    try:
        result = c.sudo("free -m", hide=True)
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
    # 检查io和cpu使用情况
    try:
        result = c.sudo("iostat 1 1", hide=True)
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


@task(aliases=["清除缓存"], help={"level": "清空缓存的等级, 只能是1, 2, 3."})
def free_cache(c: Connection, level=1) -> None:
    if level not in (1, 2, 3):
        raise AttributeError("等级只能是1,2,3")
    try:
        result = c.sudo(f"sh -c 'echo {level} > /proc/sys/vm/drop_caches'", hide=True)
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
