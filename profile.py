import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

# Run the bash file to setup Anaconda
node.addService(rspec.Execute(shell="sh", command="sudo chmod 755 /local/repository/setup.sh"))
node.addService(rspec.Execute(shell="sh", command="sudo /local/repository/setup.sh"))


node.addService(rspec.Execute(shell="/bin/sh",
                              command='git clone https://github.com/longld/peda.git ~/peda'))
node.addService(rspec.Execute(shell="/bin/sh",
                              command='echo "source ~/peda/peda.py" >> ~/.gdbinit'))
# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
