If you want to disable the "using outdated libraries" warning that appears after each apt install command, you can add the following line to the /etc/apt/apt.conf file:

APT::Immediate-Configure "0";

This configuration option disables the immediate configuration step that runs after each package installation, which is what triggers the warning. With this option set, the configuration step will be deferred until the next apt-get configure command is run.

Note that disabling the immediate configuration step may cause some services or applications to not work properly until the next apt-get configure command is run. It is recommended to only use this option if you have a specific reason to do so and are aware of the potential consequences.

Alternatively, you can use the --no-install-recommends option with the apt install command to prevent the installation of recommended packages, which can reduce the likelihood of encountering the "using outdated libraries" warning. However, this option may also cause some packages or dependencies to be missing, so it should be used with caution.

