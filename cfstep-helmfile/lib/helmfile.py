import ast
import os
import sys
import subprocess

def parse(string):
    d = {'true': True, 'false': False, 'True': True, 'False': False}
    return d.get(string, string)

def run_command(helmfile_command, working_directory):
    proc = subprocess.Popen(helmfile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=working_directory)
    output = proc.communicate()
    print(b''.join(output).strip().decode())
    if proc.returncode != 0:
        sys.exit(1)

def main():

    # Command List Executed in Order Provided
    
    commands = os.getenv('COMMANDS')
    working_directory = os.getenv('WORKING_DIRECTORY')

    # Global Options

    helm_binary = os.getenv('HELM_BINARY')
    helm_file = os.getenv('FILE')
    environment = os.getenv('ENVIRONMENT')
    state_values_set = os.getenv('STATE_VALUES_SET')
    state_values_file = os.getenv('STATE_VALUES_FILE')
    quiet = parse(os.getenv('QUIET', 'false'))
    kube_context = os.getenv('KUBE_CONTEXT')
    no_color = parse(os.getenv('NO_COLOR', 'false'))
    log_level = os.getenv('LOG_LEVEL')
    namespace = os.getenv('NAMESPACE')
    selector = os.getenv('SELECTOR')
    allow_no_matching_release = parse(os.getenv('ALLOW_NO_MATCHING_RELEASE', 'false'))
    interactive = parse(os.getenv('INTERACTIVE', 'false'))
    helm_help = parse(os.getenv('HELP', 'false'))
    version = parse(os.getenv('VERSION', 'false'))

    # Individual Command Options and Args

    deps_ps = os.getenv('DEPS_PS')
    repos_ps = os.getenv('REPOS_PS')
    charts_ps = os.getenv('CHARTS_PS')
    diff_ps = os.getenv('DIFF_PS')
    template_ps = os.getenv('TEMPLATE_PS')
    lint_ps = os.getenv('LINT_PS')
    sync_ps = os.getenv('SYNC_PS')
    apply_ps = os.getenv('APPLY_PS')
    status_ps = os.getenv('STATUS_PS')
    delete_ps = os.getenv('DELETE_PS')
    destroy_ps = os.getenv('DESTROY_PS')
    test_ps = os.getenv('TEST_PS')

    # Combine Global Options

    global_options = []

    if helm_binary:
        global_options.append("--helm_binary %s"%(helm_binary))
    if helm_file:
        global_options.append("--file %s"%(helm_file))
    if environment:
        global_options.append("--environment %s"%(environment))
    if state_values_set:
        global_options.append("--state-values-set %s"%(state_values_set))
    if state_values_file:
        global_options.append("--state-values-file %s"%(state_values_file))
    if quiet: 
        global_options.append("--quiet")
    if kube_context:
        global_options.append("--kube-context %s"%(kube_context))
    if no_color: 
        global_options.append("--no-color")
    if log_level:
        global_options.append("--log-level %s"%(log_level))
    if namespace:
        global_options.append("--namespace %s"%(namespace))
    if selector:
        global_options.append("--selector %s"%(selector))
    if allow_no_matching_release:
        global_options.append("--allow-no-matching-release")
    if interactive: 
        global_options.append("--interactive")
    if helm_help: 
        global_options.append("--help")
    if version: 
        global_options.append("--version")

    global_options_list = ' '.join(global_options)

    command_list = [x.strip() for x in commands.split(',')]

    for command in command_list:
        command_ps = eval("%s%s"%(command,"_ps"))
        helmfile_command = "helmfile"
        if global_options_list:
            helmfile_command = " ".join([helmfile_command, global_options_list])
        helmfile_command = " ".join([helmfile_command, command])
        if command_ps:
            helmfile_command = " ".join([helmfile_command, command_ps])
        run_command(helmfile_command, working_directory)

if __name__ == "__main__":
    main()
