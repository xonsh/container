# Username is much less of a thing inside containers
$PROMPT = $PROMPT.replace('{user}@','')
$TITLE = $TITLE.replace('{user}@','')

# Don't store history, on the assumption that containers are ephemeral
$XONSH_HISTORY_BACKEND = 'dummy'
