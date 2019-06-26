import argparse

parser = argparse.ArgumentParser(description="PyTorch implementation of ECO")
parser.add_argument('dataset', type=str, choices=['ucf101',
                                                  'jhmdb21',
                                                  'jester',
                                                  'somethingv2',
                                                  'hmdb51',
                                                  'kinetics',
                                                  'epickitchen_verb',
                                                  'epickitchen_noun',
                                                  'yfcc100m'])
parser.add_argument('modality', type=str, choices=['RGB', 'Flow', 'RGBDiff'])
parser.add_argument(
    '--working_directory',
    default='.',
    help='path to working directory')
parser.add_argument('--finetune_model', type=str, default=None)
# ========================= Bohb Configs ==========================
parser.add_argument('--bohb_iterations', type=int, default=5)
parser.add_argument('--min_budget', type=float, default=0.1)
parser.add_argument('--max_budget', type=float, default=1)
parser.add_argument('--eta', type=int, default=3)
parser.add_argument('--bohb_workers', type=int, default=1)
parser.add_argument('--val_perc', type=float,
                    default=1., help="Percentage of validation examples")
# ========================= Model Configs ==========================
parser.add_argument(
    '--arch',
    type=str,
    default="resnet101",
    choices=[
        'resnet50',
        'resnet101',
        'ECO',
        'ECOfull'])
parser.add_argument('--num_segments', type=int, default=3)
parser.add_argument('--consensus_type', type=str, default='avg',
                    choices=['avg', 'max', 'topk', 'identity', 'rnn', 'cnn'])

parser.add_argument('--k', type=int, default=3)

parser.add_argument('--dropout', '--do', default=0.5, type=float,
                    metavar='DO', help='dropout ratio (default: 0.5)')
parser.add_argument('--loss_type', type=str, default="nll",
                    choices=['nll', 'normal'])
parser.add_argument(
    '--img_feature_dim',
    default=256,
    type=int,
    help="the feature dimension for each frame")
parser.add_argument('--freeze_interval', '--fz_i', type=int,
                    default=[2, 63, -1, -1], nargs="+")
parser.add_argument('--pretrain', type=str, default='imagenet')

# ========================= Learning Configs ==========================
parser.add_argument('--epochs', default=45, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('-b', '--batch-size', default=256, type=int,
                    metavar='N', help='mini-batch size (default: 256)')
parser.add_argument('-i', '--iter-size', default=1, type=int,
                    metavar='N', help='number of iterations before on update')
parser.add_argument('--lr', '--learning-rate', default=0.001, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument(
    '--lr_steps',
    default=[
        20,
        40],
    type=float,
    nargs="+",
    metavar='LRSteps',
    help='epochs to decay learning rate by 10')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 5e-4)')
parser.add_argument(
    '--clip-gradient',
    '--gd',
    default=None,
    type=float,
    metavar='W',
    help='gradient norm clipping (default: disabled)')
parser.add_argument(
    '--no_partialbn',
    '--npb',
    default=False,
    action="store_true")
parser.add_argument(
    '--freeze_eco',
    '--feco',
    default=False,
    action="store_true")
parser.add_argument('--nesterov', default=False)
parser.add_argument('--optimizer', default='SGD', choices=['SGD', 'Adam'])
temp_str1 = 'if number of epochs that validation Prec@1'
temp_str2 = 'saturates, then decrease lr by 10 (default: 5)'
temp_str = temp_str1 + temp_str2
parser.add_argument(
    '--num_saturate',
    type=int,
    default=5,
    help=temp_str)

# ========================= Monitor Configs ==========================
parser.add_argument('--print-freq', '-p', default=20, type=int,
                    metavar='N', help='print frequency (default: 10)')
parser.add_argument('--print', default=True, type=bool,
                    help='If True print while training')
parser.add_argument('--eval-freq', '-ef', default=5, type=int,
                    metavar='N', help='evaluation frequency (default: 5)')


# ========================= Runtime Configs ==========================
parser.add_argument('-j', '--workers', default=4, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--snapshot_pref', type=str, default="")
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
                    help='manual epoch number (useful on restarts)')
parser.add_argument('--gpus', nargs='+', type=int, default=None)
parser.add_argument('--flow_prefix', default="", type=str)
parser.add_argument('--rgb_prefix', default="", type=str)


parser.add_argument(
    '--shift',
    default=False,
    action="store_true",
    help='use shift for models')
parser.add_argument('--shift_div', default=8, type=int,
                    help='number of div for shift (default: 8)')
parser.add_argument(
    '--shift_place',
    default='blockres',
    type=str,
    help='place for shift (default: stageres)')

parser.add_argument(
    '--temporal_pool',
    default=False,
    action="store_true",
    help='add temporal pooling')
parser.add_argument(
    '--non_local',
    default=False,
    action="store_true",
    help='add non local block')

parser.add_argument(
    '--dense_sample',
    default=False,
    action="store_true",
    help='use dense sample for video dataset')