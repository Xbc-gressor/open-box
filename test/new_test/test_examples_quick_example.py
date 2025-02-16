# License: MIT
import numpy as np
import matplotlib.pyplot as plt
from openbox import Optimizer, space as sp
from openbox.utils.constants import SUCCESS

import numpy

# Define Objective Function
def branin(config):
    x1, x2 = config['x1'], config['x2']
    y = (x2 - 5.1 / (4 * np.pi ** 2) * x1 ** 2 + 5 / np.pi * x1 - 6) ** 2 \
        + 10 * (1 - 1 / (8 * np.pi)) * np.cos(x1) + 10
    return {'objectives': [y]}


def test_examples_quick_example():
    max_runs = 20

    # Define Search Space
    space = sp.Space()
    x1 = sp.Real("x1", -5, 10, default_value=0)
    x2 = sp.Real("x2", 0, 15, default_value=0)
    space.add_variables([x1, x2])

    # Run
    opt = Optimizer(
        branin,
        space,
        max_runs=max_runs,
        # surrogate_type='gp',
        surrogate_type='auto',
        task_id='quick_start',
        logging_dir='logs/pytest/',
        # Have a try on the new HTML visualization feature!
        visualization='advanced',   # or 'basic'. For 'advanced', run 'pip install "openbox[extra]"' first
        auto_open_html=False,       # open the visualization page in your browser automatically
    )
    history = opt.run()

    print(history)

    history.plot_convergence(true_minimum=0.397887)
    # plt.show()
    plt.savefig('logs/pytest/quick_example_convergence.png')
    plt.close()

    # install pyrfr to use get_importance()
    print(history.get_importance())

    # Have a try on the new HTML visualization feature!
    # You can also call visualize_html() after optimization.
    # For 'show_importance' and 'verify_surrogate', run 'pip install "openbox[extra]"' first
    history.visualize_html(open_html=False, show_importance=True, verify_surrogate=True, optimizer=opt,
                           logging_dir='logs/pytest/')

    assert history.trial_states.count(SUCCESS) == max_runs
