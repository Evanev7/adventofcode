{
  description = "PYTHON FLAKE PYTHON FLAKE";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  };

  outputs =
    { nixpkgs, self }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };
    in
    with pkgs;
    {
      devShells.${system}.default = mkShell rec {
        buildInputs = [
          python3
          rustc
          cargo
          rustfmt
          rust-analyzer
          bacon
          clippy
        ];
      };
    };
}
