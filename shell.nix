{ pkgs ? import <nixpkgs> {} }:

let
  python3 = pkgs.python3.withPackages (ps: with ps; [
    black
  ]);
in

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    pyright
  ];

  shellHook = ''
    export PATH=$PATH:${builtins.toString ./.}/node_modules/.bin
    python3 -m venv .venv
    source .venv/bin/activate
  '';
}