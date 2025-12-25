# Username is much less of a thing inside containers
$PROMPT = '{env_name}{BOLD_GREEN}{hostname}{BOLD_BLUE} {cwd}{branch_color}{curr_branch: {}}{NO_COLOR} {BOLD_BLUE}{prompt_end}{NO_COLOR} '
$TITLE = '{current_job:{} | }{hostname}: {cwd} | xonsh'

# Don't store history, on the assumption that containers are ephemeral
$XONSH_HISTORY_BACKEND = 'dummy'
