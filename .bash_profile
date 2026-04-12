# Start ssh-agent and add key automatically
eval $(ssh-agent -s) > /dev/null
ssh-add ~/.ssh/id_ed25519
