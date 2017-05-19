with import <nixpkgs> {};
with pkgs.python35Packages;

buildPythonPackage{
    name = "scrappy";
    buildInputs = [ python35Full
                    python35Packages.setuptools
                    python35Packages.urllib3
                    python35Packages.beautifulsoup4
                   ]; 

}

