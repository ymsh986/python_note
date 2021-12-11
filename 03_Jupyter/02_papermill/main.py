import papermill as pm

new_beta = [1, 2, 3]

pm.execute_notebook('try_papermill.ipynb',
                    'try_papermill_output.ipynb',
                    parameters=dict(alpha=['hello', 'world', 1],
                                    beta=new_beta,
                                    gamma={1: 'hello', 2: 'world'},
                                    epsilon=100))
