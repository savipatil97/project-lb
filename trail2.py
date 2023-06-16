import facter
test = """
server {
    listen 80;
    server_name ipadd;

    location / {
        proxy_pass http://ipadd:5000;

    }
}
"""
facts = facter.Facter()
ip_machine = str(facts["networking"]["ip"])
ele = str(test).replace('ipadd', ip_machine)
