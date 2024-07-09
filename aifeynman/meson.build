dest = 'aifeynman'

python_sources = [
    '__init__.py',
    'dimensionalAnalysis.py',
    'getPowers.py',
    'get_demos.py',
    'get_pareto.py',
    'resources.py',
    'test_points.py',
    'RPN_to_eq.py',
    'RPN_to_pytorch.py',
    'S_NN_eval.py',
    'S_NN_get_gradients.py',
    'S_NN_train.py',
    'S_add_bf_on_numbers_on_pareto.py',
    'S_add_snap_expr_on_pareto.py',
    'S_add_sym_on_pareto.py',
    'S_brute_force.py',
    'S_brute_force_comp.py',
    'S_brute_force_gen_sym.py',
    'S_brute_force_number.py',
    'S_change_output.py',
    'S_combine_pareto.py',
    'S_compositionality.py',
    'S_final_gd.py',
    'S_gen_sym.py',
    'S_get_expr_complexity.py',
    'S_get_number_DL.py',
    'S_get_number_DL_snapped.py',
    'S_get_symbolic_expr_error.py',
    'S_gradient_decomposition.py',
    'S_polyfit.py',
    'S_polyfit_utils.py',
    'S_remove_input_neuron.py',
    'S_run_aifeynman.py',
    'S_run_bf_polyfit.py',
    'S_separability.py',
    'S_snap.py',
    'S_symmetry.py']

config_sources = ['10ops.txt',
                  '14ops.txt',
                  '19ops.txt',
                  '7ops.txt',
                  'arity2templates.txt']

all_sources = python_sources + config_sources


py.install_sources(
  all_sources,
  subdir: dest
)

#py.extension_module('_symbolic_regress1',
#                    'symbolic_regress1.f90',
#                    install: true,
#                    link_language: 'fortran',
#                    subdir: dest
#)

py.extension_module('_symbolic_regress2',
                    'symbolic_regress2.f90',
                    install: true,
                    link_language: 'fortran',
                    subdir: dest
)

py.extension_module('_symbolic_regress3',
                    'symbolic_regress3.f90',
                    install: true,
                    link_language: 'fortran',
                    subdir: dest
)

py.extension_module('_symbolic_regress_mdl2',
                    'symbolic_regress_mdl2.f90',
                    install: true,
                    link_language: 'fortran',
                    subdir: dest
)

py.extension_module('_symbolic_regress_mdl3',
                    'symbolic_regress_mdl3.f90',
                    install: true,
                    link_language: 'fortran',
                    subdir: dest
)

py.extension_module('_symbolic_regress_mdl4',
                    'symbolic_regress_mdl4.f90',
                    install: true,
                    link_language: 'fortran',
                    subdir: dest
)

py.extension_module('_symbolic_regress_mdl5',
                    'symbolic_regress_mdl5.f90',
                    install: true,
                    link_language: 'fortran',
                    subdir: dest
)

###
#p = import('python')
#numpy_dep = py.dependency('numpy')
#py.extension_module('_symbolic_regress1',
#                    'symbolic_regress1module.c'
#                    'symbolic_regress1.f90',
#                    dependencies: dependency('numpy'),
#                    install: true,
#                    subdir: dest
#)
f2py = find_program('f2py')
numpy_dep = import('python').find_installation()
fortran_sources = ['symbolic_regress1.f90']
# Create custom targets to run f2py
foreach source : fortran_sources
  basename = source.split('/')[-1].split('.')[0]
  so_file = '_' + basename + '.so'
  f2py_command = [
    f2py,
    '-c', source,
    '-m', '_' + basename,
  ]

  # Create a custom target to build the shared object
  custom_target(so_file,
    output: so_file,
    input: source,
    command: f2py_command,
    install: true,
    install_dir: py.get_install_dir(),
  )
endforeach

#py_mod.add_console_script('feynman_sr1', 'aifeynman._symbolic_regress1', 'go')

# Console scripts
scripts = [
  ['feynman_sr1', 'aifeynman._symbolic_regress1'],
  ['feynman_sr2', 'aifeynman._symbolic_regress2'],
  ['feynman_sr3', 'aifeynman._symbolic_regress3'],
  ['feynman_sr_mdl_mult', 'aifeynman._symbolic_regress_mdl3'],
  ['feynman_sr_mdl_plus', 'aifeynman._symbolic_regress_mdl2'],
  ['feynman_sr_mdl4', 'aifeynman._symbolic_regress_mdl4'],
  ['feynman_sr_mdl5', 'aifeynman._symbolic_regress_mdl5']
]


foreach script : scripts
  exec = configure_file(
    input: 'template.sh.in',
    output: script[0],
    configuration: {
      'module': script[1],
      'python': python
    },
    install: true,
    install_mode: 'rwxr-xr-x',
    install_dir: get_option('bindir')
  )
endforeach

# Add the post-install script
meson.add_install_script('post_install.py')
