# Here are some commonly used Ansible commands:

ansible: This command allows you to execute an ad-hoc command on a set of target hosts. For example, the following command runs the ping module on all hosts in the web group:

ansible web -m ping

ansible-playbook: This command allows you to execute a playbook on a set of target hosts. For example, the following command runs the webserver.yml playbook on all hosts in the web group:

ansible-playbook webserver.yml -i inventory.ini -u remote_user

ansible-galaxy: This command allows you to search for and download pre-built roles from the Ansible Galaxy community. For example, the following command installs the geerlingguy.mysql role:

ansible-galaxy install geerlingguy.mysql

ansible-vault: This command allows you to encrypt and decrypt sensitive data in Ansible playbooks and inventory files. For example, the following command encrypts a file named secrets.yml:

ansible-vault encrypt secrets.yml

ansible-doc: This command displays documentation for Ansible modules. For example, the following command displays the documentation for the copy module:

ansible-doc copy

ansible-inventory: This command displays the current inventory configuration. For example, the following command displays the hosts and groups defined in the default inventory file:

ansible-inventory --list

