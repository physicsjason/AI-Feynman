project('aifeynman', 'c',
  meson_version: '>=0.64.0',
  default_options: ['warning_level=2'])

add_languages('fortran')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()
python = import('python').find_installation().full_path()

dest = 'aifeynman'

python_sources = [
    'aifeynman/__init__.py',
    'aifeynman/dimensionalAnalysis.py',
    'aifeynman/getPowers.py',
    'aifeynman/get_demos.py',
    'aifeynman/get_pareto.py',
    'aifeynman/resources.py',
    'aifeynman/test_points.py',
    'aifeynman/RPN_to_eq.py',
    'aifeynman/RPN_to_pytorch.py',
    'aifeynman/S_NN_eval.py',
    'aifeynman/S_NN_get_gradients.py',
    'aifeynman/S_NN_train.py',
    'aifeynman/S_add_bf_on_numbers_on_pareto.py',
    'aifeynman/S_add_snap_expr_on_pareto.py',
    'aifeynman/S_add_sym_on_pareto.py',
    'aifeynman/S_brute_force.py',
    'aifeynman/S_brute_force_comp.py',
    'aifeynman/S_brute_force_gen_sym.py',
    'aifeynman/S_brute_force_number.py',
    'aifeynman/S_change_output.py',
    'aifeynman/S_combine_pareto.py',
    'aifeynman/S_compositionality.py',
    'aifeynman/S_final_gd.py',
    'aifeynman/S_gen_sym.py',
    'aifeynman/S_get_expr_complexity.py',
    'aifeynman/S_get_number_DL.py',
    'aifeynman/S_get_number_DL_snapped.py',
    'aifeynman/S_get_symbolic_expr_error.py',
    'aifeynman/S_gradient_decomposition.py',
    'aifeynman/S_polyfit.py',
    'aifeynman/S_polyfit_utils.py',
    'aifeynman/S_remove_input_neuron.py',
    'aifeynman/S_run_aifeynman.py',
    'aifeynman/S_run_bf_polyfit.py',
    'aifeynman/S_separability.py',
    'aifeynman/S_snap.py',
    'aifeynman/S_symmetry.py']

config_sources = ['aifeynman/10ops.txt',
                  'aifeynman/14ops.txt',
                  'aifeynman/19ops.txt',
                  'aifeynman/7ops.txt',
                  'aifeynman/arity2templates.txt']

fortran_sources = ['aifeynman/symbolic_regress1.f90',
                  'aifeynman/symbolic_regress2.f90',
                  'aifeynman/symbolic_regress3.f90',
                  'aifeynman/symbolic_regress_mdl2.f90',
                  'aifeynman/symbolic_regress_mdl3.f90',
                  'aifeynman/symbolic_regress_mdl4.f90',
                  'aifeynman/symbolic_regress_mdl5.f90']

all_sources = python_sources + config_sources + fortran_sources


py.install_sources(
  all_sources,
  subdir: dest
)


# for f2py
incdir_numpy = run_command(py,
  ['-c', 'import os; import numpy; print(os.path.relpath(numpy.get_include()))'],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import os; import numpy.f2py; print(os.path.relpath(numpy.f2py.get_include()))'],
    check : true
).stdout().strip()

inc_np = include_directories(incdir_numpy, incdir_f2py)

fortran_target = ['symbolic_regress1',
                  'symbolic_regress2',
                  'symbolic_regress3',
                  'symbolic_regress_mdl2',
                  'symbolic_regress_mdl3',
                  'symbolic_regress_mdl4',
                  'symbolic_regress_mdl5']
foreach fix : fortran_target

  fibby_source = custom_target(f'_@fix@module.c',
    input : [f'aifeynman/@fix@.f90'],  # .f so no F90 wrappers
    output : [f'_@fix@module.c', f'_@fix@-f2pywrappers.f'],
    command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', f'_@fix@', '--lower'],
  )

  py.extension_module(f'_@fix@',
    [f'aifeynman/@fix@.f90', fibby_source],
    incdir_f2py / 'fortranobject.c',
    include_directories: inc_np,
    dependencies: py_dep,
    install: true,
    subdir: dest
  )

endforeach

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
 configure_file(
   input: 'aifeynman/template.sh.in',
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
