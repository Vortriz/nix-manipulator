{
  lib,
  buildPythonApplication,
  uv-build,
  tree-sitter,
  tree-sitter-grammars,
  pydantic,
  pygments,
  pytestCheckHook,
}:
buildPythonApplication {
  pname = "nima";
  version = "0.1.3-dev";

  pyproject = true;
  pythonRelaxDeps = true;

  build-system = [ uv-build ];

  src = lib.fileset.toSource {
    root = ./.;
    fileset = lib.fileset.unions [
      ./src
      ./tests
      ./pyproject.toml
      ./uv.lock
      ./README.md
    ];
  };

  dependencies = [
    tree-sitter
    tree-sitter-grammars.tree-sitter-nix
    pydantic
    pygments
  ];

  doCheck = true;

  nativeCheckInputs = [
    pytestCheckHook
  ];

  checkPhase = ''
    pytest -v -m "not nixpkgs"
  '';

  disabledTests = [
    "test_some_nixpkgs_packages"
  ];

  pythonImportsCheck = [ "nima" ];

  meta = {
    description = "A Python library for parsing, manipulating, and reconstructing Nix source code";
    homepage = "https://github.com/Vortriz/nix-manipulator";
    license = lib.licenses.lgpl3Plus;
    mainProgram = "nima";
  };
}
