# Ansible

Ansible is an open-source automation tool that helps in configuring and managing servers, networking devices, and cloud infrastructure. It uses a simple syntax called YAML (YAML Ain't Markup Language) to describe tasks and can be easily used by IT teams to automate repetitive tasks, deploy applications, and orchestrate complex workflows.

With Ansible, users can manage infrastructure as code, which means that they can define their desired state of infrastructure in code and let Ansible handle the execution of those changes on the target systems. Ansible is agentless, meaning that it does not require any software or daemons to be installed on the target system, making it easy to set up and use.

Some of the key features of Ansible include its ability to manage multiple systems at once, its support for task delegation and workflow orchestration, and its ability to integrate with a wide variety of tools and services. Ansible also has a large and active community of contributors, making it a popular choice for IT automation.

# Ansible uses the SSH protocol to connect to remote servers by default, so it typically uses the default SSH port, which is port 22.

However, Ansible can also use other protocols to connect to remote systems, such as HTTPS for managing network devices or the WinRM protocol for managing Windows hosts. In these cases, Ansible may use different port numbers depending on the protocol being used and the configuration of the target systems.

Here are some common port numbers that Ansible may use:

SSH: port 22
HTTPS: port 443
WinRM: port 5985 (HTTP) or 5986 (HTTPS)

# Here are some key terms associated with Ansible:

Inventory: A list of hosts and groups that Ansible manages. The inventory can be stored in a static file or dynamically generated from a database or cloud provider.

Playbook: A YAML file that defines a set of tasks to be executed on a specific set of hosts. Playbooks can be used to automate tasks such as server configuration, application deployment, and system maintenance.

Task: A single unit of work to be executed on a target host. Tasks are defined in playbooks and can include commands, scripts, or Ansible modules.

Module: A script or program that performs a specific function in Ansible, such as managing packages, configuring services, or copying files. Ansible comes with a large collection of built-in modules, and users can also create their own custom modules.

Role: A collection of tasks, files, templates, and variables that can be reused across multiple playbooks. Roles provide a way to organize and share Ansible code between teams and projects.

Handler: A task that is triggered by another task or event. Handlers are used to respond to changes in system state, such as restarting a service after a configuration file has been updated.

Facts: Information about a target host that is automatically collected by Ansible, such as the operating system version, available memory, and installed packages. Facts can be used in playbooks to conditionally execute tasks based on the current system state.

Vault: A feature of Ansible that allows users to encrypt sensitive data, such as passwords and API keys, in playbooks and inventory files. Vault uses symmetric encryption and requires a passphrase to decrypt the data.

