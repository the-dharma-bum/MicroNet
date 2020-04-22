# +---------------------------------------------------------------------------------------+ #
# |                                                                                       | #
# |                                         MAIN                                          | #
# |                                                                                       | #
# +---------------------------------------------------------------------------------------+ #


import torch
from model import Model
from trainer import Trainer
import config as cfg

# +---------------------------------------------------------------------------------------+ #
# |                                                                                       | #
# |                             THIS FILE SHOULD NOT BE MODIFIED                          | #
# |                   ALL HYPER PARAMETERS SHOULD BE CONFIGURED IN config.py              | #
# |                                                                                       | #
# +---------------------------------------------------------------------------------------+ #

def build():
    print('Building Model...')
    model = Model()
    trainer = Trainer(model)
    print(trainer)
    return model, trainer


def load_trained(path):
    model, trainer = build()
    model = torch.load(path)
    return model, trainer


def train():
    model, trainer = build()
    try:
        trainer.run()
    except KeyboardInterrupt:
        prefix = 'INTERRUPTED_EPOCH_' + str(trainer.state['epoch']) + '_'
        checkpoints_filename = prefix + cfg.get_experiment_name() + '.pt'
        torch.save(model.net.state_dict(), path)
        print()
        print(80*'_')
        print('Training Interrupted')
        print('Current State saved.')


def test(path):
    model, trainer = load_trained(path)
    model.eval()
    test_loss, test_acc = trainer.test()
    print(80*'_')
    print(f'Loss......: {test_loss}')
    print(f'Accuracy..: {test_acc}')
    print(80*'_')



if __name__ == '__main__':
    build()
    #train()
    #test()
