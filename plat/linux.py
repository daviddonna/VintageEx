import os
import subprocess


def run_and_wait(view, cmd):
    term = view.settings().get('vintageex_linux_terminal')
    term = term or os.path.expandvars("$COLORTERM") or os.path.expandvars("$TERM")
    subprocess.Popen([
            term, '-e',
            "bash -c \"%s; read -p 'Press RETURN to exit.'\"" % cmd]).wait()


def bash_escape_double_quoted_text(text):
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('$', '\\$')


def filter_region(view, text, command):
    shell = view.settings().get('vintageex_linux_shell')
    shell = shell or os.path.expandvars("$SHELL")
    escaped = bash_escape_double_quoted_text(text)
    p = subprocess.Popen([shell, '-c', 'echo "%s" | %s' % (escaped, command)],
                         stdout=subprocess.PIPE)
    return p.communicate()[0][:-1]
