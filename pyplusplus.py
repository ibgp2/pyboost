import os, pathlib
from pygccxml import parser
from pyplusplus import module_builder

def make_bindings_auto(
    headers_dir,
    headers_ext = "hpp",
    filename_bindings_auto = "src/bindings_auto.cpp",
    module_name = "pyboost",
    generator_path = "/usr/bin/castxml",
    generator_name = "castxml",
    compiler = "gnu",
    compiler_path = "/usr/bin/g++"
):
    cwd = pathlib.Path().absolute()
    os.chdir(headers_dir)
    headers = [f for f in find(extension="hpp")]

    # Configurations que vous pouvez avoir à changer sur votre système
    # Créé une configuration pour CastXML
    xml_generator_config = parser.xml_generator_configuration_t(
        xml_generator_path=generator_path,
        xml_generator=generator_name,
        compiler=compiler,
        compiler_path=compiler_path
    )

    # Analyse les fichiers sources et créé un objet module_builder
    builder = module_builder.module_builder_t(
        headers,
        xml_generator_path=generator_path,
        xml_generator_config=xml_generator_config
    )

    # Détecte automatiquement les propriétés et les accesseurs/mutateurs associés
    builder.classes().add_properties(exclude_accessors=True)

    # Définit un nom pour le module
    builder.build_code_creator(module_name=module_name)

    # Écrit le fichier d'interface C++
    os.chdir(str(cwd))
    if os.path.exists(filename_bindings_auto):
        os.remove(filename_bindings_auto)
    builder.write_module(filename_bindings_auto)
